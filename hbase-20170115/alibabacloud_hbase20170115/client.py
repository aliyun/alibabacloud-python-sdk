# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_hbase20170115 import models as hbase_20170115_models
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
            'ap-northeast-2-pop': 'hbase.aliyuncs.com',
            'ap-south-1': 'hbase.aliyuncs.com',
            'ap-southeast-2': 'hbase.aliyuncs.com',
            'cn-beijing-finance-1': 'hbase.aliyuncs.com',
            'cn-beijing-finance-pop': 'hbase.aliyuncs.com',
            'cn-beijing-gov-1': 'hbase.aliyuncs.com',
            'cn-beijing-nu16-b01': 'hbase.aliyuncs.com',
            'cn-edge-1': 'hbase.aliyuncs.com',
            'cn-fujian': 'hbase.aliyuncs.com',
            'cn-haidian-cm12-c01': 'hbase.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'hbase.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'hbase.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'hbase.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'hbase.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'hbase.aliyuncs.com',
            'cn-hangzhou-test-306': 'hbase.aliyuncs.com',
            'cn-hongkong-finance-pop': 'hbase.aliyuncs.com',
            'cn-qingdao-nebula': 'hbase.aliyuncs.com',
            'cn-shanghai-et15-b01': 'hbase.aliyuncs.com',
            'cn-shanghai-et2-b01': 'hbase.aliyuncs.com',
            'cn-shanghai-inner': 'hbase.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'hbase.aliyuncs.com',
            'cn-shenzhen-inner': 'hbase.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'hbase.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'hbase.aliyuncs.com',
            'cn-wuhan': 'hbase.aliyuncs.com',
            'cn-wulanchabu': 'hbase.aliyuncs.com',
            'cn-yushanfang': 'hbase.aliyuncs.com',
            'cn-zhangbei': 'hbase.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'hbase.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'hbase.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'hbase.aliyuncs.com',
            'eu-west-1-oxs': 'hbase.aliyuncs.com',
            'rus-west-1-pop': 'hbase.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('hbase', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_user_hdfs_info_with_options(
        self,
        request: hbase_20170115_models.AddUserHdfsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.AddUserHdfsInfoResponse:
        """
        @param request: AddUserHdfsInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUserHdfsInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.ext_info):
            query['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='AddUserHdfsInfo',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.AddUserHdfsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_hdfs_info_with_options_async(
        self,
        request: hbase_20170115_models.AddUserHdfsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.AddUserHdfsInfoResponse:
        """
        @param request: AddUserHdfsInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUserHdfsInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.ext_info):
            query['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='AddUserHdfsInfo',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.AddUserHdfsInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user_hdfs_info(
        self,
        request: hbase_20170115_models.AddUserHdfsInfoRequest,
    ) -> hbase_20170115_models.AddUserHdfsInfoResponse:
        """
        @param request: AddUserHdfsInfoRequest
        @return: AddUserHdfsInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_user_hdfs_info_with_options(request, runtime)

    async def add_user_hdfs_info_async(
        self,
        request: hbase_20170115_models.AddUserHdfsInfoRequest,
    ) -> hbase_20170115_models.AddUserHdfsInfoResponse:
        """
        @param request: AddUserHdfsInfoRequest
        @return: AddUserHdfsInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_user_hdfs_info_with_options_async(request, runtime)

    def allocate_public_network_address_with_options(
        self,
        request: hbase_20170115_models.AllocatePublicNetworkAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.AllocatePublicNetworkAddressResponse:
        """
        @param request: AllocatePublicNetworkAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocatePublicNetworkAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
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
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.AllocatePublicNetworkAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_public_network_address_with_options_async(
        self,
        request: hbase_20170115_models.AllocatePublicNetworkAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.AllocatePublicNetworkAddressResponse:
        """
        @param request: AllocatePublicNetworkAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocatePublicNetworkAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
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
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.AllocatePublicNetworkAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_public_network_address(
        self,
        request: hbase_20170115_models.AllocatePublicNetworkAddressRequest,
    ) -> hbase_20170115_models.AllocatePublicNetworkAddressResponse:
        """
        @param request: AllocatePublicNetworkAddressRequest
        @return: AllocatePublicNetworkAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.allocate_public_network_address_with_options(request, runtime)

    async def allocate_public_network_address_async(
        self,
        request: hbase_20170115_models.AllocatePublicNetworkAddressRequest,
    ) -> hbase_20170115_models.AllocatePublicNetworkAddressResponse:
        """
        @param request: AllocatePublicNetworkAddressRequest
        @return: AllocatePublicNetworkAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.allocate_public_network_address_with_options_async(request, runtime)

    def check_versions_of_components_with_options(
        self,
        request: hbase_20170115_models.CheckVersionsOfComponentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.CheckVersionsOfComponentsResponse:
        """
        @param request: CheckVersionsOfComponentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckVersionsOfComponentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.components):
            query['Components'] = request.components
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='CheckVersionsOfComponents',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.CheckVersionsOfComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_versions_of_components_with_options_async(
        self,
        request: hbase_20170115_models.CheckVersionsOfComponentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.CheckVersionsOfComponentsResponse:
        """
        @param request: CheckVersionsOfComponentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckVersionsOfComponentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.components):
            query['Components'] = request.components
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='CheckVersionsOfComponents',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.CheckVersionsOfComponentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_versions_of_components(
        self,
        request: hbase_20170115_models.CheckVersionsOfComponentsRequest,
    ) -> hbase_20170115_models.CheckVersionsOfComponentsResponse:
        """
        @param request: CheckVersionsOfComponentsRequest
        @return: CheckVersionsOfComponentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_versions_of_components_with_options(request, runtime)

    async def check_versions_of_components_async(
        self,
        request: hbase_20170115_models.CheckVersionsOfComponentsRequest,
    ) -> hbase_20170115_models.CheckVersionsOfComponentsResponse:
        """
        @param request: CheckVersionsOfComponentsRequest
        @return: CheckVersionsOfComponentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_versions_of_components_with_options_async(request, runtime)

    def close_backup_with_options(
        self,
        request: hbase_20170115_models.CloseBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.CloseBackupResponse:
        """
        @param request: CloseBackupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloseBackupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='CloseBackup',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.CloseBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_backup_with_options_async(
        self,
        request: hbase_20170115_models.CloseBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.CloseBackupResponse:
        """
        @param request: CloseBackupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloseBackupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='CloseBackup',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.CloseBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_backup(
        self,
        request: hbase_20170115_models.CloseBackupRequest,
    ) -> hbase_20170115_models.CloseBackupResponse:
        """
        @param request: CloseBackupRequest
        @return: CloseBackupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.close_backup_with_options(request, runtime)

    async def close_backup_async(
        self,
        request: hbase_20170115_models.CloseBackupRequest,
    ) -> hbase_20170115_models.CloseBackupResponse:
        """
        @param request: CloseBackupRequest
        @return: CloseBackupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.close_backup_with_options_async(request, runtime)

    def convert_cluster_with_options(
        self,
        request: hbase_20170115_models.ConvertClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ConvertClusterResponse:
        """
        @param request: ConvertClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConvertClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='ConvertCluster',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ConvertClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def convert_cluster_with_options_async(
        self,
        request: hbase_20170115_models.ConvertClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ConvertClusterResponse:
        """
        @param request: ConvertClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConvertClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='ConvertCluster',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ConvertClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def convert_cluster(
        self,
        request: hbase_20170115_models.ConvertClusterRequest,
    ) -> hbase_20170115_models.ConvertClusterResponse:
        """
        @param request: ConvertClusterRequest
        @return: ConvertClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.convert_cluster_with_options(request, runtime)

    async def convert_cluster_async(
        self,
        request: hbase_20170115_models.ConvertClusterRequest,
    ) -> hbase_20170115_models.ConvertClusterResponse:
        """
        @param request: ConvertClusterRequest
        @return: ConvertClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.convert_cluster_with_options_async(request, runtime)

    def create_cluster_with_options(
        self,
        request: hbase_20170115_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.CreateClusterResponse:
        """
        @summary 创建实例
        
        @param request: CreateClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cloud_type):
            query['CloudType'] = request.cloud_type
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.cold_storage_size):
            query['ColdStorageSize'] = request.cold_storage_size
        if not UtilClient.is_unset(request.core_disk_quantity):
            query['CoreDiskQuantity'] = request.core_disk_quantity
        if not UtilClient.is_unset(request.core_disk_size):
            query['CoreDiskSize'] = request.core_disk_size
        if not UtilClient.is_unset(request.core_disk_type):
            query['CoreDiskType'] = request.core_disk_type
        if not UtilClient.is_unset(request.core_instance_quantity):
            query['CoreInstanceQuantity'] = request.core_instance_quantity
        if not UtilClient.is_unset(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not UtilClient.is_unset(request.db_instance_conn_type):
            query['DbInstanceConnType'] = request.db_instance_conn_type
        if not UtilClient.is_unset(request.db_instance_type):
            query['DbInstanceType'] = request.db_instance_type
        if not UtilClient.is_unset(request.db_type):
            query['DbType'] = request.db_type
        if not UtilClient.is_unset(request.dep_mode):
            query['DepMode'] = request.dep_mode
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.is_cold_storage):
            query['IsColdStorage'] = request.is_cold_storage
        if not UtilClient.is_unset(request.master_instance_type):
            query['MasterInstanceType'] = request.master_instance_type
        if not UtilClient.is_unset(request.net_type):
            query['NetType'] = request.net_type
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not UtilClient.is_unset(request.src_dbinstance_id):
            query['SrcDBInstanceId'] = request.src_dbinstance_id
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
            action='CreateCluster',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_with_options_async(
        self,
        request: hbase_20170115_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.CreateClusterResponse:
        """
        @summary 创建实例
        
        @param request: CreateClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cloud_type):
            query['CloudType'] = request.cloud_type
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.cold_storage_size):
            query['ColdStorageSize'] = request.cold_storage_size
        if not UtilClient.is_unset(request.core_disk_quantity):
            query['CoreDiskQuantity'] = request.core_disk_quantity
        if not UtilClient.is_unset(request.core_disk_size):
            query['CoreDiskSize'] = request.core_disk_size
        if not UtilClient.is_unset(request.core_disk_type):
            query['CoreDiskType'] = request.core_disk_type
        if not UtilClient.is_unset(request.core_instance_quantity):
            query['CoreInstanceQuantity'] = request.core_instance_quantity
        if not UtilClient.is_unset(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not UtilClient.is_unset(request.db_instance_conn_type):
            query['DbInstanceConnType'] = request.db_instance_conn_type
        if not UtilClient.is_unset(request.db_instance_type):
            query['DbInstanceType'] = request.db_instance_type
        if not UtilClient.is_unset(request.db_type):
            query['DbType'] = request.db_type
        if not UtilClient.is_unset(request.dep_mode):
            query['DepMode'] = request.dep_mode
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.is_cold_storage):
            query['IsColdStorage'] = request.is_cold_storage
        if not UtilClient.is_unset(request.master_instance_type):
            query['MasterInstanceType'] = request.master_instance_type
        if not UtilClient.is_unset(request.net_type):
            query['NetType'] = request.net_type
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not UtilClient.is_unset(request.src_dbinstance_id):
            query['SrcDBInstanceId'] = request.src_dbinstance_id
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
            action='CreateCluster',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.CreateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster(
        self,
        request: hbase_20170115_models.CreateClusterRequest,
    ) -> hbase_20170115_models.CreateClusterResponse:
        """
        @summary 创建实例
        
        @param request: CreateClusterRequest
        @return: CreateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    async def create_cluster_async(
        self,
        request: hbase_20170115_models.CreateClusterRequest,
    ) -> hbase_20170115_models.CreateClusterResponse:
        """
        @summary 创建实例
        
        @param request: CreateClusterRequest
        @return: CreateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_with_options_async(request, runtime)

    def create_global_resource_with_options(
        self,
        request: hbase_20170115_models.CreateGlobalResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.CreateGlobalResourceResponse:
        """
        @param request: CreateGlobalResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGlobalResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGlobalResource',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.CreateGlobalResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_global_resource_with_options_async(
        self,
        request: hbase_20170115_models.CreateGlobalResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.CreateGlobalResourceResponse:
        """
        @param request: CreateGlobalResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGlobalResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGlobalResource',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.CreateGlobalResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_global_resource(
        self,
        request: hbase_20170115_models.CreateGlobalResourceRequest,
    ) -> hbase_20170115_models.CreateGlobalResourceResponse:
        """
        @param request: CreateGlobalResourceRequest
        @return: CreateGlobalResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_global_resource_with_options(request, runtime)

    async def create_global_resource_async(
        self,
        request: hbase_20170115_models.CreateGlobalResourceRequest,
    ) -> hbase_20170115_models.CreateGlobalResourceResponse:
        """
        @param request: CreateGlobalResourceRequest
        @return: CreateGlobalResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_global_resource_with_options_async(request, runtime)

    def create_hbase_slb_server_with_options(
        self,
        request: hbase_20170115_models.CreateHbaseSlbServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.CreateHbaseSlbServerResponse:
        """
        @param request: CreateHbaseSlbServerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHbaseSlbServerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.slb_server):
            query['SlbServer'] = request.slb_server
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHbaseSlbServer',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.CreateHbaseSlbServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_hbase_slb_server_with_options_async(
        self,
        request: hbase_20170115_models.CreateHbaseSlbServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.CreateHbaseSlbServerResponse:
        """
        @param request: CreateHbaseSlbServerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHbaseSlbServerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.slb_server):
            query['SlbServer'] = request.slb_server
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHbaseSlbServer',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.CreateHbaseSlbServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_hbase_slb_server(
        self,
        request: hbase_20170115_models.CreateHbaseSlbServerRequest,
    ) -> hbase_20170115_models.CreateHbaseSlbServerResponse:
        """
        @param request: CreateHbaseSlbServerRequest
        @return: CreateHbaseSlbServerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_hbase_slb_server_with_options(request, runtime)

    async def create_hbase_slb_server_async(
        self,
        request: hbase_20170115_models.CreateHbaseSlbServerRequest,
    ) -> hbase_20170115_models.CreateHbaseSlbServerResponse:
        """
        @param request: CreateHbaseSlbServerRequest
        @return: CreateHbaseSlbServerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_hbase_slb_server_with_options_async(request, runtime)

    def create_subscription_with_options(
        self,
        request: hbase_20170115_models.CreateSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.CreateSubscriptionResponse:
        """
        @summary 创建订阅
        
        @param request: CreateSubscriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSubscriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_instance_id):
            query['DestinationInstanceId'] = request.destination_instance_id
        if not UtilClient.is_unset(request.destination_instance_region_id):
            query['DestinationInstanceRegionId'] = request.destination_instance_region_id
        if not UtilClient.is_unset(request.extra_context):
            query['ExtraContext'] = request.extra_context
        if not UtilClient.is_unset(request.mapping):
            query['Mapping'] = request.mapping
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.slb_server):
            query['SlbServer'] = request.slb_server
        if not UtilClient.is_unset(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not UtilClient.is_unset(request.source_instance_region_id):
            query['SourceInstanceRegionId'] = request.source_instance_region_id
        if not UtilClient.is_unset(request.subscription_description):
            query['SubscriptionDescription'] = request.subscription_description
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSubscription',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.CreateSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_subscription_with_options_async(
        self,
        request: hbase_20170115_models.CreateSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.CreateSubscriptionResponse:
        """
        @summary 创建订阅
        
        @param request: CreateSubscriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSubscriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_instance_id):
            query['DestinationInstanceId'] = request.destination_instance_id
        if not UtilClient.is_unset(request.destination_instance_region_id):
            query['DestinationInstanceRegionId'] = request.destination_instance_region_id
        if not UtilClient.is_unset(request.extra_context):
            query['ExtraContext'] = request.extra_context
        if not UtilClient.is_unset(request.mapping):
            query['Mapping'] = request.mapping
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.slb_server):
            query['SlbServer'] = request.slb_server
        if not UtilClient.is_unset(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not UtilClient.is_unset(request.source_instance_region_id):
            query['SourceInstanceRegionId'] = request.source_instance_region_id
        if not UtilClient.is_unset(request.subscription_description):
            query['SubscriptionDescription'] = request.subscription_description
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSubscription',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.CreateSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_subscription(
        self,
        request: hbase_20170115_models.CreateSubscriptionRequest,
    ) -> hbase_20170115_models.CreateSubscriptionResponse:
        """
        @summary 创建订阅
        
        @param request: CreateSubscriptionRequest
        @return: CreateSubscriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_subscription_with_options(request, runtime)

    async def create_subscription_async(
        self,
        request: hbase_20170115_models.CreateSubscriptionRequest,
    ) -> hbase_20170115_models.CreateSubscriptionResponse:
        """
        @summary 创建订阅
        
        @param request: CreateSubscriptionRequest
        @return: CreateSubscriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_subscription_with_options_async(request, runtime)

    def delete_cluster_with_options(
        self,
        request: hbase_20170115_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DeleteClusterResponse:
        """
        @param request: DeleteClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DeleteCluster',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DeleteClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_with_options_async(
        self,
        request: hbase_20170115_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DeleteClusterResponse:
        """
        @param request: DeleteClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DeleteCluster',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DeleteClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster(
        self,
        request: hbase_20170115_models.DeleteClusterRequest,
    ) -> hbase_20170115_models.DeleteClusterResponse:
        """
        @param request: DeleteClusterRequest
        @return: DeleteClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    async def delete_cluster_async(
        self,
        request: hbase_20170115_models.DeleteClusterRequest,
    ) -> hbase_20170115_models.DeleteClusterResponse:
        """
        @param request: DeleteClusterRequest
        @return: DeleteClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_cluster_with_options_async(request, runtime)

    def delete_global_resource_with_options(
        self,
        request: hbase_20170115_models.DeleteGlobalResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DeleteGlobalResourceResponse:
        """
        @param request: DeleteGlobalResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGlobalResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGlobalResource',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DeleteGlobalResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_global_resource_with_options_async(
        self,
        request: hbase_20170115_models.DeleteGlobalResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DeleteGlobalResourceResponse:
        """
        @param request: DeleteGlobalResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGlobalResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGlobalResource',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DeleteGlobalResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_global_resource(
        self,
        request: hbase_20170115_models.DeleteGlobalResourceRequest,
    ) -> hbase_20170115_models.DeleteGlobalResourceResponse:
        """
        @param request: DeleteGlobalResourceRequest
        @return: DeleteGlobalResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_global_resource_with_options(request, runtime)

    async def delete_global_resource_async(
        self,
        request: hbase_20170115_models.DeleteGlobalResourceRequest,
    ) -> hbase_20170115_models.DeleteGlobalResourceResponse:
        """
        @param request: DeleteGlobalResourceRequest
        @return: DeleteGlobalResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_global_resource_with_options_async(request, runtime)

    def delete_hbase_slb_server_with_options(
        self,
        request: hbase_20170115_models.DeleteHbaseSlbServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DeleteHbaseSlbServerResponse:
        """
        @param request: DeleteHbaseSlbServerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHbaseSlbServerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.slb_server):
            query['SlbServer'] = request.slb_server
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHbaseSlbServer',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DeleteHbaseSlbServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hbase_slb_server_with_options_async(
        self,
        request: hbase_20170115_models.DeleteHbaseSlbServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DeleteHbaseSlbServerResponse:
        """
        @param request: DeleteHbaseSlbServerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHbaseSlbServerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.slb_server):
            query['SlbServer'] = request.slb_server
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHbaseSlbServer',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DeleteHbaseSlbServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hbase_slb_server(
        self,
        request: hbase_20170115_models.DeleteHbaseSlbServerRequest,
    ) -> hbase_20170115_models.DeleteHbaseSlbServerResponse:
        """
        @param request: DeleteHbaseSlbServerRequest
        @return: DeleteHbaseSlbServerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_hbase_slb_server_with_options(request, runtime)

    async def delete_hbase_slb_server_async(
        self,
        request: hbase_20170115_models.DeleteHbaseSlbServerRequest,
    ) -> hbase_20170115_models.DeleteHbaseSlbServerResponse:
        """
        @param request: DeleteHbaseSlbServerRequest
        @return: DeleteHbaseSlbServerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_hbase_slb_server_with_options_async(request, runtime)

    def delete_serverless_instance_with_options(
        self,
        request: hbase_20170115_models.DeleteServerlessInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DeleteServerlessInstanceResponse:
        """
        @param request: DeleteServerlessInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServerlessInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DeleteServerlessInstance',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DeleteServerlessInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_serverless_instance_with_options_async(
        self,
        request: hbase_20170115_models.DeleteServerlessInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DeleteServerlessInstanceResponse:
        """
        @param request: DeleteServerlessInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServerlessInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DeleteServerlessInstance',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DeleteServerlessInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_serverless_instance(
        self,
        request: hbase_20170115_models.DeleteServerlessInstanceRequest,
    ) -> hbase_20170115_models.DeleteServerlessInstanceResponse:
        """
        @param request: DeleteServerlessInstanceRequest
        @return: DeleteServerlessInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_serverless_instance_with_options(request, runtime)

    async def delete_serverless_instance_async(
        self,
        request: hbase_20170115_models.DeleteServerlessInstanceRequest,
    ) -> hbase_20170115_models.DeleteServerlessInstanceResponse:
        """
        @param request: DeleteServerlessInstanceRequest
        @return: DeleteServerlessInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_serverless_instance_with_options_async(request, runtime)

    def delete_user_hdfs_info_with_options(
        self,
        request: hbase_20170115_models.DeleteUserHdfsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DeleteUserHdfsInfoResponse:
        """
        @param request: DeleteUserHdfsInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserHdfsInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.name_service):
            query['NameService'] = request.name_service
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DeleteUserHdfsInfo',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DeleteUserHdfsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_hdfs_info_with_options_async(
        self,
        request: hbase_20170115_models.DeleteUserHdfsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DeleteUserHdfsInfoResponse:
        """
        @param request: DeleteUserHdfsInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserHdfsInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.name_service):
            query['NameService'] = request.name_service
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DeleteUserHdfsInfo',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DeleteUserHdfsInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_hdfs_info(
        self,
        request: hbase_20170115_models.DeleteUserHdfsInfoRequest,
    ) -> hbase_20170115_models.DeleteUserHdfsInfoResponse:
        """
        @param request: DeleteUserHdfsInfoRequest
        @return: DeleteUserHdfsInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_user_hdfs_info_with_options(request, runtime)

    async def delete_user_hdfs_info_async(
        self,
        request: hbase_20170115_models.DeleteUserHdfsInfoRequest,
    ) -> hbase_20170115_models.DeleteUserHdfsInfoResponse:
        """
        @param request: DeleteUserHdfsInfoRequest
        @return: DeleteUserHdfsInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_hdfs_info_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: hbase_20170115_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeBackupPolicyResponse:
        """
        @param request: DescribeBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DescribeBackupPolicy',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_policy_with_options_async(
        self,
        request: hbase_20170115_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeBackupPolicyResponse:
        """
        @param request: DescribeBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DescribeBackupPolicy',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_policy(
        self,
        request: hbase_20170115_models.DescribeBackupPolicyRequest,
    ) -> hbase_20170115_models.DescribeBackupPolicyResponse:
        """
        @param request: DescribeBackupPolicyRequest
        @return: DescribeBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: hbase_20170115_models.DescribeBackupPolicyRequest,
    ) -> hbase_20170115_models.DescribeBackupPolicyResponse:
        """
        @param request: DescribeBackupPolicyRequest
        @return: DescribeBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_backups_with_options(
        self,
        request: hbase_20170115_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeBackupsResponse:
        """
        @param request: DescribeBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.end_time_utc):
            query['EndTimeUTC'] = request.end_time_utc
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
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.start_time_utc):
            query['StartTimeUTC'] = request.start_time_utc
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackups',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backups_with_options_async(
        self,
        request: hbase_20170115_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeBackupsResponse:
        """
        @param request: DescribeBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.end_time_utc):
            query['EndTimeUTC'] = request.end_time_utc
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
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.start_time_utc):
            query['StartTimeUTC'] = request.start_time_utc
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackups',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeBackupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backups(
        self,
        request: hbase_20170115_models.DescribeBackupsRequest,
    ) -> hbase_20170115_models.DescribeBackupsResponse:
        """
        @param request: DescribeBackupsRequest
        @return: DescribeBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    async def describe_backups_async(
        self,
        request: hbase_20170115_models.DescribeBackupsRequest,
    ) -> hbase_20170115_models.DescribeBackupsResponse:
        """
        @param request: DescribeBackupsRequest
        @return: DescribeBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backups_with_options_async(request, runtime)

    def describe_cluster_attribute_with_options(
        self,
        request: hbase_20170115_models.DescribeClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeClusterAttributeResponse:
        """
        @param request: DescribeClusterAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DescribeClusterAttribute',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeClusterAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_attribute_with_options_async(
        self,
        request: hbase_20170115_models.DescribeClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeClusterAttributeResponse:
        """
        @param request: DescribeClusterAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DescribeClusterAttribute',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeClusterAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_attribute(
        self,
        request: hbase_20170115_models.DescribeClusterAttributeRequest,
    ) -> hbase_20170115_models.DescribeClusterAttributeResponse:
        """
        @param request: DescribeClusterAttributeRequest
        @return: DescribeClusterAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_attribute_with_options(request, runtime)

    async def describe_cluster_attribute_async(
        self,
        request: hbase_20170115_models.DescribeClusterAttributeRequest,
    ) -> hbase_20170115_models.DescribeClusterAttributeResponse:
        """
        @param request: DescribeClusterAttributeRequest
        @return: DescribeClusterAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_attribute_with_options_async(request, runtime)

    def describe_cluster_connect_addrs_with_options(
        self,
        request: hbase_20170115_models.DescribeClusterConnectAddrsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeClusterConnectAddrsResponse:
        """
        @param request: DescribeClusterConnectAddrsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterConnectAddrsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DescribeClusterConnectAddrs',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeClusterConnectAddrsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_connect_addrs_with_options_async(
        self,
        request: hbase_20170115_models.DescribeClusterConnectAddrsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeClusterConnectAddrsResponse:
        """
        @param request: DescribeClusterConnectAddrsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterConnectAddrsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DescribeClusterConnectAddrs',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeClusterConnectAddrsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_connect_addrs(
        self,
        request: hbase_20170115_models.DescribeClusterConnectAddrsRequest,
    ) -> hbase_20170115_models.DescribeClusterConnectAddrsResponse:
        """
        @param request: DescribeClusterConnectAddrsRequest
        @return: DescribeClusterConnectAddrsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_connect_addrs_with_options(request, runtime)

    async def describe_cluster_connect_addrs_async(
        self,
        request: hbase_20170115_models.DescribeClusterConnectAddrsRequest,
    ) -> hbase_20170115_models.DescribeClusterConnectAddrsResponse:
        """
        @param request: DescribeClusterConnectAddrsRequest
        @return: DescribeClusterConnectAddrsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_connect_addrs_with_options_async(request, runtime)

    def describe_cluster_list_with_options(
        self,
        request: hbase_20170115_models.DescribeClusterListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeClusterListResponse:
        """
        @param request: DescribeClusterListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.db_type):
            query['DbType'] = request.db_type
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
        if not UtilClient.is_unset(request.status_list):
            query['StatusList'] = request.status_list
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterList',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeClusterListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_list_with_options_async(
        self,
        request: hbase_20170115_models.DescribeClusterListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeClusterListResponse:
        """
        @param request: DescribeClusterListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.db_type):
            query['DbType'] = request.db_type
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
        if not UtilClient.is_unset(request.status_list):
            query['StatusList'] = request.status_list
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterList',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeClusterListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_list(
        self,
        request: hbase_20170115_models.DescribeClusterListRequest,
    ) -> hbase_20170115_models.DescribeClusterListResponse:
        """
        @param request: DescribeClusterListRequest
        @return: DescribeClusterListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_list_with_options(request, runtime)

    async def describe_cluster_list_async(
        self,
        request: hbase_20170115_models.DescribeClusterListRequest,
    ) -> hbase_20170115_models.DescribeClusterListResponse:
        """
        @param request: DescribeClusterListRequest
        @return: DescribeClusterListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_list_with_options_async(request, runtime)

    def describe_cluster_model_with_options(
        self,
        request: hbase_20170115_models.DescribeClusterModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeClusterModelResponse:
        """
        @param request: DescribeClusterModelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterModelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DescribeClusterModel',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeClusterModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_model_with_options_async(
        self,
        request: hbase_20170115_models.DescribeClusterModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeClusterModelResponse:
        """
        @param request: DescribeClusterModelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterModelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DescribeClusterModel',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeClusterModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_model(
        self,
        request: hbase_20170115_models.DescribeClusterModelRequest,
    ) -> hbase_20170115_models.DescribeClusterModelResponse:
        """
        @param request: DescribeClusterModelRequest
        @return: DescribeClusterModelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_model_with_options(request, runtime)

    async def describe_cluster_model_async(
        self,
        request: hbase_20170115_models.DescribeClusterModelRequest,
    ) -> hbase_20170115_models.DescribeClusterModelResponse:
        """
        @param request: DescribeClusterModelRequest
        @return: DescribeClusterModelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_model_with_options_async(request, runtime)

    def describe_cluster_white_list_with_options(
        self,
        request: hbase_20170115_models.DescribeClusterWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeClusterWhiteListResponse:
        """
        @param request: DescribeClusterWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DescribeClusterWhiteList',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeClusterWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_white_list_with_options_async(
        self,
        request: hbase_20170115_models.DescribeClusterWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeClusterWhiteListResponse:
        """
        @param request: DescribeClusterWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DescribeClusterWhiteList',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeClusterWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_white_list(
        self,
        request: hbase_20170115_models.DescribeClusterWhiteListRequest,
    ) -> hbase_20170115_models.DescribeClusterWhiteListResponse:
        """
        @param request: DescribeClusterWhiteListRequest
        @return: DescribeClusterWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_white_list_with_options(request, runtime)

    async def describe_cluster_white_list_async(
        self,
        request: hbase_20170115_models.DescribeClusterWhiteListRequest,
    ) -> hbase_20170115_models.DescribeClusterWhiteListResponse:
        """
        @param request: DescribeClusterWhiteListRequest
        @return: DescribeClusterWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_white_list_with_options_async(request, runtime)

    def describe_cold_storage_with_options(
        self,
        request: hbase_20170115_models.DescribeColdStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeColdStorageResponse:
        """
        @param request: DescribeColdStorageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeColdStorageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DescribeColdStorage',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeColdStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cold_storage_with_options_async(
        self,
        request: hbase_20170115_models.DescribeColdStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeColdStorageResponse:
        """
        @param request: DescribeColdStorageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeColdStorageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DescribeColdStorage',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeColdStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cold_storage(
        self,
        request: hbase_20170115_models.DescribeColdStorageRequest,
    ) -> hbase_20170115_models.DescribeColdStorageResponse:
        """
        @param request: DescribeColdStorageRequest
        @return: DescribeColdStorageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cold_storage_with_options(request, runtime)

    async def describe_cold_storage_async(
        self,
        request: hbase_20170115_models.DescribeColdStorageRequest,
    ) -> hbase_20170115_models.DescribeColdStorageResponse:
        """
        @param request: DescribeColdStorageRequest
        @return: DescribeColdStorageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cold_storage_with_options_async(request, runtime)

    def describe_multi_mod_db_attribute_with_options(
        self,
        request: hbase_20170115_models.DescribeMultiModDbAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeMultiModDbAttributeResponse:
        """
        @param request: DescribeMultiModDbAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMultiModDbAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DescribeMultiModDbAttribute',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeMultiModDbAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_multi_mod_db_attribute_with_options_async(
        self,
        request: hbase_20170115_models.DescribeMultiModDbAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeMultiModDbAttributeResponse:
        """
        @param request: DescribeMultiModDbAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMultiModDbAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DescribeMultiModDbAttribute',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeMultiModDbAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_multi_mod_db_attribute(
        self,
        request: hbase_20170115_models.DescribeMultiModDbAttributeRequest,
    ) -> hbase_20170115_models.DescribeMultiModDbAttributeResponse:
        """
        @param request: DescribeMultiModDbAttributeRequest
        @return: DescribeMultiModDbAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_multi_mod_db_attribute_with_options(request, runtime)

    async def describe_multi_mod_db_attribute_async(
        self,
        request: hbase_20170115_models.DescribeMultiModDbAttributeRequest,
    ) -> hbase_20170115_models.DescribeMultiModDbAttributeResponse:
        """
        @param request: DescribeMultiModDbAttributeRequest
        @return: DescribeMultiModDbAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_multi_mod_db_attribute_with_options_async(request, runtime)

    def describe_rds_vswitchs_with_options(
        self,
        request: hbase_20170115_models.DescribeRdsVSwitchsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeRdsVSwitchsResponse:
        """
        @param request: DescribeRdsVSwitchsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRdsVSwitchsResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRdsVSwitchs',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeRdsVSwitchsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rds_vswitchs_with_options_async(
        self,
        request: hbase_20170115_models.DescribeRdsVSwitchsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeRdsVSwitchsResponse:
        """
        @param request: DescribeRdsVSwitchsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRdsVSwitchsResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRdsVSwitchs',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeRdsVSwitchsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rds_vswitchs(
        self,
        request: hbase_20170115_models.DescribeRdsVSwitchsRequest,
    ) -> hbase_20170115_models.DescribeRdsVSwitchsResponse:
        """
        @param request: DescribeRdsVSwitchsRequest
        @return: DescribeRdsVSwitchsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_vswitchs_with_options(request, runtime)

    async def describe_rds_vswitchs_async(
        self,
        request: hbase_20170115_models.DescribeRdsVSwitchsRequest,
    ) -> hbase_20170115_models.DescribeRdsVSwitchsResponse:
        """
        @param request: DescribeRdsVSwitchsRequest
        @return: DescribeRdsVSwitchsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_rds_vswitchs_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: hbase_20170115_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeRegionsResponse:
        """
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DescribeRegions',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: hbase_20170115_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeRegionsResponse:
        """
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DescribeRegions',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: hbase_20170115_models.DescribeRegionsRequest,
    ) -> hbase_20170115_models.DescribeRegionsResponse:
        """
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: hbase_20170115_models.DescribeRegionsRequest,
    ) -> hbase_20170115_models.DescribeRegionsResponse:
        """
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_serverless_instance_with_options(
        self,
        request: hbase_20170115_models.DescribeServerlessInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeServerlessInstanceResponse:
        """
        @param request: DescribeServerlessInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServerlessInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServerlessInstance',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeServerlessInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_serverless_instance_with_options_async(
        self,
        request: hbase_20170115_models.DescribeServerlessInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeServerlessInstanceResponse:
        """
        @param request: DescribeServerlessInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServerlessInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServerlessInstance',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeServerlessInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_serverless_instance(
        self,
        request: hbase_20170115_models.DescribeServerlessInstanceRequest,
    ) -> hbase_20170115_models.DescribeServerlessInstanceResponse:
        """
        @param request: DescribeServerlessInstanceRequest
        @return: DescribeServerlessInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_serverless_instance_with_options(request, runtime)

    async def describe_serverless_instance_async(
        self,
        request: hbase_20170115_models.DescribeServerlessInstanceRequest,
    ) -> hbase_20170115_models.DescribeServerlessInstanceResponse:
        """
        @param request: DescribeServerlessInstanceRequest
        @return: DescribeServerlessInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_serverless_instance_with_options_async(request, runtime)

    def describe_subscription_initialize_progress_with_options(
        self,
        request: hbase_20170115_models.DescribeSubscriptionInitializeProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeSubscriptionInitializeProgressResponse:
        """
        @summary 查询订阅进度
        
        @param request: DescribeSubscriptionInitializeProgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSubscriptionInitializeProgressResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.subscription_id):
            query['SubscriptionId'] = request.subscription_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptionInitializeProgress',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeSubscriptionInitializeProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_subscription_initialize_progress_with_options_async(
        self,
        request: hbase_20170115_models.DescribeSubscriptionInitializeProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeSubscriptionInitializeProgressResponse:
        """
        @summary 查询订阅进度
        
        @param request: DescribeSubscriptionInitializeProgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSubscriptionInitializeProgressResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.subscription_id):
            query['SubscriptionId'] = request.subscription_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptionInitializeProgress',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeSubscriptionInitializeProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_subscription_initialize_progress(
        self,
        request: hbase_20170115_models.DescribeSubscriptionInitializeProgressRequest,
    ) -> hbase_20170115_models.DescribeSubscriptionInitializeProgressResponse:
        """
        @summary 查询订阅进度
        
        @param request: DescribeSubscriptionInitializeProgressRequest
        @return: DescribeSubscriptionInitializeProgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_subscription_initialize_progress_with_options(request, runtime)

    async def describe_subscription_initialize_progress_async(
        self,
        request: hbase_20170115_models.DescribeSubscriptionInitializeProgressRequest,
    ) -> hbase_20170115_models.DescribeSubscriptionInitializeProgressResponse:
        """
        @summary 查询订阅进度
        
        @param request: DescribeSubscriptionInitializeProgressRequest
        @return: DescribeSubscriptionInitializeProgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_subscription_initialize_progress_with_options_async(request, runtime)

    def describe_subscription_performance_with_options(
        self,
        request: hbase_20170115_models.DescribeSubscriptionPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeSubscriptionPerformanceResponse:
        """
        @summary 查询订阅
        
        @param request: DescribeSubscriptionPerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSubscriptionPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.subscription_id):
            query['SubscriptionId'] = request.subscription_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptionPerformance',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeSubscriptionPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_subscription_performance_with_options_async(
        self,
        request: hbase_20170115_models.DescribeSubscriptionPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeSubscriptionPerformanceResponse:
        """
        @summary 查询订阅
        
        @param request: DescribeSubscriptionPerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSubscriptionPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.subscription_id):
            query['SubscriptionId'] = request.subscription_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptionPerformance',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeSubscriptionPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_subscription_performance(
        self,
        request: hbase_20170115_models.DescribeSubscriptionPerformanceRequest,
    ) -> hbase_20170115_models.DescribeSubscriptionPerformanceResponse:
        """
        @summary 查询订阅
        
        @param request: DescribeSubscriptionPerformanceRequest
        @return: DescribeSubscriptionPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_subscription_performance_with_options(request, runtime)

    async def describe_subscription_performance_async(
        self,
        request: hbase_20170115_models.DescribeSubscriptionPerformanceRequest,
    ) -> hbase_20170115_models.DescribeSubscriptionPerformanceResponse:
        """
        @summary 查询订阅
        
        @param request: DescribeSubscriptionPerformanceRequest
        @return: DescribeSubscriptionPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_subscription_performance_with_options_async(request, runtime)

    def describe_subscription_permission_with_options(
        self,
        request: hbase_20170115_models.DescribeSubscriptionPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeSubscriptionPermissionResponse:
        """
        @summary 查询订阅权限
        
        @param request: DescribeSubscriptionPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSubscriptionPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='DescribeSubscriptionPermission',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeSubscriptionPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_subscription_permission_with_options_async(
        self,
        request: hbase_20170115_models.DescribeSubscriptionPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeSubscriptionPermissionResponse:
        """
        @summary 查询订阅权限
        
        @param request: DescribeSubscriptionPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSubscriptionPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='DescribeSubscriptionPermission',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeSubscriptionPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_subscription_permission(
        self,
        request: hbase_20170115_models.DescribeSubscriptionPermissionRequest,
    ) -> hbase_20170115_models.DescribeSubscriptionPermissionResponse:
        """
        @summary 查询订阅权限
        
        @param request: DescribeSubscriptionPermissionRequest
        @return: DescribeSubscriptionPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_subscription_permission_with_options(request, runtime)

    async def describe_subscription_permission_async(
        self,
        request: hbase_20170115_models.DescribeSubscriptionPermissionRequest,
    ) -> hbase_20170115_models.DescribeSubscriptionPermissionResponse:
        """
        @summary 查询订阅权限
        
        @param request: DescribeSubscriptionPermissionRequest
        @return: DescribeSubscriptionPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_subscription_permission_with_options_async(request, runtime)

    def describe_subscriptions_with_options(
        self,
        request: hbase_20170115_models.DescribeSubscriptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeSubscriptionsResponse:
        """
        @summary 查询订阅列表
        
        @param request: DescribeSubscriptionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSubscriptionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.subscription_id):
            query['SubscriptionId'] = request.subscription_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptions',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeSubscriptionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_subscriptions_with_options_async(
        self,
        request: hbase_20170115_models.DescribeSubscriptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.DescribeSubscriptionsResponse:
        """
        @summary 查询订阅列表
        
        @param request: DescribeSubscriptionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSubscriptionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.subscription_id):
            query['SubscriptionId'] = request.subscription_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptions',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.DescribeSubscriptionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_subscriptions(
        self,
        request: hbase_20170115_models.DescribeSubscriptionsRequest,
    ) -> hbase_20170115_models.DescribeSubscriptionsResponse:
        """
        @summary 查询订阅列表
        
        @param request: DescribeSubscriptionsRequest
        @return: DescribeSubscriptionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_subscriptions_with_options(request, runtime)

    async def describe_subscriptions_async(
        self,
        request: hbase_20170115_models.DescribeSubscriptionsRequest,
    ) -> hbase_20170115_models.DescribeSubscriptionsResponse:
        """
        @summary 查询订阅列表
        
        @param request: DescribeSubscriptionsRequest
        @return: DescribeSubscriptionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_subscriptions_with_options_async(request, runtime)

    def enable_serverless_public_connection_with_options(
        self,
        request: hbase_20170115_models.EnableServerlessPublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.EnableServerlessPublicConnectionResponse:
        """
        @param request: EnableServerlessPublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableServerlessPublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='EnableServerlessPublicConnection',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.EnableServerlessPublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_serverless_public_connection_with_options_async(
        self,
        request: hbase_20170115_models.EnableServerlessPublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.EnableServerlessPublicConnectionResponse:
        """
        @param request: EnableServerlessPublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableServerlessPublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='EnableServerlessPublicConnection',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.EnableServerlessPublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_serverless_public_connection(
        self,
        request: hbase_20170115_models.EnableServerlessPublicConnectionRequest,
    ) -> hbase_20170115_models.EnableServerlessPublicConnectionResponse:
        """
        @param request: EnableServerlessPublicConnectionRequest
        @return: EnableServerlessPublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_serverless_public_connection_with_options(request, runtime)

    async def enable_serverless_public_connection_async(
        self,
        request: hbase_20170115_models.EnableServerlessPublicConnectionRequest,
    ) -> hbase_20170115_models.EnableServerlessPublicConnectionResponse:
        """
        @param request: EnableServerlessPublicConnectionRequest
        @return: EnableServerlessPublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_serverless_public_connection_with_options_async(request, runtime)

    def get_multimode_cms_url_with_options(
        self,
        request: hbase_20170115_models.GetMultimodeCmsUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.GetMultimodeCmsUrlResponse:
        """
        @param request: GetMultimodeCmsUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMultimodeCmsUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='GetMultimodeCmsUrl',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.GetMultimodeCmsUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_multimode_cms_url_with_options_async(
        self,
        request: hbase_20170115_models.GetMultimodeCmsUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.GetMultimodeCmsUrlResponse:
        """
        @param request: GetMultimodeCmsUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMultimodeCmsUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='GetMultimodeCmsUrl',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.GetMultimodeCmsUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_multimode_cms_url(
        self,
        request: hbase_20170115_models.GetMultimodeCmsUrlRequest,
    ) -> hbase_20170115_models.GetMultimodeCmsUrlResponse:
        """
        @param request: GetMultimodeCmsUrlRequest
        @return: GetMultimodeCmsUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_multimode_cms_url_with_options(request, runtime)

    async def get_multimode_cms_url_async(
        self,
        request: hbase_20170115_models.GetMultimodeCmsUrlRequest,
    ) -> hbase_20170115_models.GetMultimodeCmsUrlResponse:
        """
        @param request: GetMultimodeCmsUrlRequest
        @return: GetMultimodeCmsUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_multimode_cms_url_with_options_async(request, runtime)

    def list_cluster_service_config_with_options(
        self,
        request: hbase_20170115_models.ListClusterServiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ListClusterServiceConfigResponse:
        """
        @param request: ListClusterServiceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClusterServiceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
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
            action='ListClusterServiceConfig',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ListClusterServiceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_service_config_with_options_async(
        self,
        request: hbase_20170115_models.ListClusterServiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ListClusterServiceConfigResponse:
        """
        @param request: ListClusterServiceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClusterServiceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
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
            action='ListClusterServiceConfig',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ListClusterServiceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_service_config(
        self,
        request: hbase_20170115_models.ListClusterServiceConfigRequest,
    ) -> hbase_20170115_models.ListClusterServiceConfigResponse:
        """
        @param request: ListClusterServiceConfigRequest
        @return: ListClusterServiceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_service_config_with_options(request, runtime)

    async def list_cluster_service_config_async(
        self,
        request: hbase_20170115_models.ListClusterServiceConfigRequest,
    ) -> hbase_20170115_models.ListClusterServiceConfigResponse:
        """
        @param request: ListClusterServiceConfigRequest
        @return: ListClusterServiceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_service_config_with_options_async(request, runtime)

    def list_cluster_service_config_history_with_options(
        self,
        request: hbase_20170115_models.ListClusterServiceConfigHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ListClusterServiceConfigHistoryResponse:
        """
        @param request: ListClusterServiceConfigHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClusterServiceConfigHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
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
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterServiceConfigHistory',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ListClusterServiceConfigHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_service_config_history_with_options_async(
        self,
        request: hbase_20170115_models.ListClusterServiceConfigHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ListClusterServiceConfigHistoryResponse:
        """
        @param request: ListClusterServiceConfigHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClusterServiceConfigHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
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
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterServiceConfigHistory',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ListClusterServiceConfigHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_service_config_history(
        self,
        request: hbase_20170115_models.ListClusterServiceConfigHistoryRequest,
    ) -> hbase_20170115_models.ListClusterServiceConfigHistoryResponse:
        """
        @param request: ListClusterServiceConfigHistoryRequest
        @return: ListClusterServiceConfigHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_service_config_history_with_options(request, runtime)

    async def list_cluster_service_config_history_async(
        self,
        request: hbase_20170115_models.ListClusterServiceConfigHistoryRequest,
    ) -> hbase_20170115_models.ListClusterServiceConfigHistoryResponse:
        """
        @param request: ListClusterServiceConfigHistoryRequest
        @return: ListClusterServiceConfigHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_service_config_history_with_options_async(request, runtime)

    def list_hbase_instances_with_options(
        self,
        request: hbase_20170115_models.ListHbaseInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ListHbaseInstancesResponse:
        """
        @summary 查询hbase实例列表
        
        @param request: ListHbaseInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHbaseInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHbaseInstances',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ListHbaseInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hbase_instances_with_options_async(
        self,
        request: hbase_20170115_models.ListHbaseInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ListHbaseInstancesResponse:
        """
        @summary 查询hbase实例列表
        
        @param request: ListHbaseInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHbaseInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHbaseInstances',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ListHbaseInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hbase_instances(
        self,
        request: hbase_20170115_models.ListHbaseInstancesRequest,
    ) -> hbase_20170115_models.ListHbaseInstancesResponse:
        """
        @summary 查询hbase实例列表
        
        @param request: ListHbaseInstancesRequest
        @return: ListHbaseInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_hbase_instances_with_options(request, runtime)

    async def list_hbase_instances_async(
        self,
        request: hbase_20170115_models.ListHbaseInstancesRequest,
    ) -> hbase_20170115_models.ListHbaseInstancesResponse:
        """
        @summary 查询hbase实例列表
        
        @param request: ListHbaseInstancesRequest
        @return: ListHbaseInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_hbase_instances_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: hbase_20170115_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ListTagResourcesResponse:
        """
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
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: hbase_20170115_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ListTagResourcesResponse:
        """
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
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: hbase_20170115_models.ListTagResourcesRequest,
    ) -> hbase_20170115_models.ListTagResourcesResponse:
        """
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: hbase_20170115_models.ListTagResourcesRequest,
    ) -> hbase_20170115_models.ListTagResourcesResponse:
        """
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_backup_policy_with_options(
        self,
        request: hbase_20170115_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ModifyBackupPolicyResponse:
        """
        @param request: ModifyBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preferred_backup_end_time_utc):
            query['PreferredBackupEndTimeUTC'] = request.preferred_backup_end_time_utc
        if not UtilClient.is_unset(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not UtilClient.is_unset(request.preferred_backup_start_time_utc):
            query['PreferredBackupStartTimeUTC'] = request.preferred_backup_start_time_utc
        if not UtilClient.is_unset(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='ModifyBackupPolicy',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ModifyBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_policy_with_options_async(
        self,
        request: hbase_20170115_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ModifyBackupPolicyResponse:
        """
        @param request: ModifyBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preferred_backup_end_time_utc):
            query['PreferredBackupEndTimeUTC'] = request.preferred_backup_end_time_utc
        if not UtilClient.is_unset(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not UtilClient.is_unset(request.preferred_backup_start_time_utc):
            query['PreferredBackupStartTimeUTC'] = request.preferred_backup_start_time_utc
        if not UtilClient.is_unset(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='ModifyBackupPolicy',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ModifyBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_policy(
        self,
        request: hbase_20170115_models.ModifyBackupPolicyRequest,
    ) -> hbase_20170115_models.ModifyBackupPolicyResponse:
        """
        @param request: ModifyBackupPolicyRequest
        @return: ModifyBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    async def modify_backup_policy_async(
        self,
        request: hbase_20170115_models.ModifyBackupPolicyRequest,
    ) -> hbase_20170115_models.ModifyBackupPolicyResponse:
        """
        @param request: ModifyBackupPolicyRequest
        @return: ModifyBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_policy_with_options_async(request, runtime)

    def modify_cluster_name_with_options(
        self,
        request: hbase_20170115_models.ModifyClusterNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ModifyClusterNameResponse:
        """
        @param request: ModifyClusterNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='ModifyClusterName',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ModifyClusterNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_name_with_options_async(
        self,
        request: hbase_20170115_models.ModifyClusterNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ModifyClusterNameResponse:
        """
        @param request: ModifyClusterNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='ModifyClusterName',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ModifyClusterNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cluster_name(
        self,
        request: hbase_20170115_models.ModifyClusterNameRequest,
    ) -> hbase_20170115_models.ModifyClusterNameResponse:
        """
        @param request: ModifyClusterNameRequest
        @return: ModifyClusterNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_name_with_options(request, runtime)

    async def modify_cluster_name_async(
        self,
        request: hbase_20170115_models.ModifyClusterNameRequest,
    ) -> hbase_20170115_models.ModifyClusterNameResponse:
        """
        @param request: ModifyClusterNameRequest
        @return: ModifyClusterNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_cluster_name_with_options_async(request, runtime)

    def modify_cluster_net_type_with_options(
        self,
        request: hbase_20170115_models.ModifyClusterNetTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ModifyClusterNetTypeResponse:
        """
        @param request: ModifyClusterNetTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterNetTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.net_type):
            query['NetType'] = request.net_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='ModifyClusterNetType',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ModifyClusterNetTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_net_type_with_options_async(
        self,
        request: hbase_20170115_models.ModifyClusterNetTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ModifyClusterNetTypeResponse:
        """
        @param request: ModifyClusterNetTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterNetTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.net_type):
            query['NetType'] = request.net_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='ModifyClusterNetType',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ModifyClusterNetTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cluster_net_type(
        self,
        request: hbase_20170115_models.ModifyClusterNetTypeRequest,
    ) -> hbase_20170115_models.ModifyClusterNetTypeResponse:
        """
        @param request: ModifyClusterNetTypeRequest
        @return: ModifyClusterNetTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_net_type_with_options(request, runtime)

    async def modify_cluster_net_type_async(
        self,
        request: hbase_20170115_models.ModifyClusterNetTypeRequest,
    ) -> hbase_20170115_models.ModifyClusterNetTypeResponse:
        """
        @param request: ModifyClusterNetTypeRequest
        @return: ModifyClusterNetTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_cluster_net_type_with_options_async(request, runtime)

    def modify_cluster_security_ip_list_with_options(
        self,
        request: hbase_20170115_models.ModifyClusterSecurityIpListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ModifyClusterSecurityIpListResponse:
        """
        @param request: ModifyClusterSecurityIpListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterSecurityIpListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_ip_list):
            query['SecurityIpList'] = request.security_ip_list
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClusterSecurityIpList',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ModifyClusterSecurityIpListResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_security_ip_list_with_options_async(
        self,
        request: hbase_20170115_models.ModifyClusterSecurityIpListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ModifyClusterSecurityIpListResponse:
        """
        @param request: ModifyClusterSecurityIpListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterSecurityIpListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_ip_list):
            query['SecurityIpList'] = request.security_ip_list
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClusterSecurityIpList',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ModifyClusterSecurityIpListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cluster_security_ip_list(
        self,
        request: hbase_20170115_models.ModifyClusterSecurityIpListRequest,
    ) -> hbase_20170115_models.ModifyClusterSecurityIpListResponse:
        """
        @param request: ModifyClusterSecurityIpListRequest
        @return: ModifyClusterSecurityIpListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_security_ip_list_with_options(request, runtime)

    async def modify_cluster_security_ip_list_async(
        self,
        request: hbase_20170115_models.ModifyClusterSecurityIpListRequest,
    ) -> hbase_20170115_models.ModifyClusterSecurityIpListResponse:
        """
        @param request: ModifyClusterSecurityIpListRequest
        @return: ModifyClusterSecurityIpListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_cluster_security_ip_list_with_options_async(request, runtime)

    def modify_cluster_service_config_with_options(
        self,
        request: hbase_20170115_models.ModifyClusterServiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ModifyClusterServiceConfigResponse:
        """
        @param request: ModifyClusterServiceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterServiceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
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
        if not UtilClient.is_unset(request.restart):
            query['Restart'] = request.restart
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClusterServiceConfig',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ModifyClusterServiceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_service_config_with_options_async(
        self,
        request: hbase_20170115_models.ModifyClusterServiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ModifyClusterServiceConfigResponse:
        """
        @param request: ModifyClusterServiceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterServiceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
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
        if not UtilClient.is_unset(request.restart):
            query['Restart'] = request.restart
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClusterServiceConfig',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ModifyClusterServiceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cluster_service_config(
        self,
        request: hbase_20170115_models.ModifyClusterServiceConfigRequest,
    ) -> hbase_20170115_models.ModifyClusterServiceConfigResponse:
        """
        @param request: ModifyClusterServiceConfigRequest
        @return: ModifyClusterServiceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_service_config_with_options(request, runtime)

    async def modify_cluster_service_config_async(
        self,
        request: hbase_20170115_models.ModifyClusterServiceConfigRequest,
    ) -> hbase_20170115_models.ModifyClusterServiceConfigResponse:
        """
        @param request: ModifyClusterServiceConfigRequest
        @return: ModifyClusterServiceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_cluster_service_config_with_options_async(request, runtime)

    def modify_has_root_password_with_options(
        self,
        request: hbase_20170115_models.ModifyHasRootPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ModifyHasRootPasswordResponse:
        """
        @param request: ModifyHasRootPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHasRootPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.has_password):
            query['HasPassword'] = request.has_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='ModifyHasRootPassword',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ModifyHasRootPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_has_root_password_with_options_async(
        self,
        request: hbase_20170115_models.ModifyHasRootPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ModifyHasRootPasswordResponse:
        """
        @param request: ModifyHasRootPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHasRootPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.has_password):
            query['HasPassword'] = request.has_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='ModifyHasRootPassword',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ModifyHasRootPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_has_root_password(
        self,
        request: hbase_20170115_models.ModifyHasRootPasswordRequest,
    ) -> hbase_20170115_models.ModifyHasRootPasswordResponse:
        """
        @param request: ModifyHasRootPasswordRequest
        @return: ModifyHasRootPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_has_root_password_with_options(request, runtime)

    async def modify_has_root_password_async(
        self,
        request: hbase_20170115_models.ModifyHasRootPasswordRequest,
    ) -> hbase_20170115_models.ModifyHasRootPasswordResponse:
        """
        @param request: ModifyHasRootPasswordRequest
        @return: ModifyHasRootPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_has_root_password_with_options_async(request, runtime)

    def modify_restart_cluster_with_options(
        self,
        request: hbase_20170115_models.ModifyRestartClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ModifyRestartClusterResponse:
        """
        @param request: ModifyRestartClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyRestartClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.components):
            query['Components'] = request.components
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='ModifyRestartCluster',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ModifyRestartClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_restart_cluster_with_options_async(
        self,
        request: hbase_20170115_models.ModifyRestartClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ModifyRestartClusterResponse:
        """
        @param request: ModifyRestartClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyRestartClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.components):
            query['Components'] = request.components
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='ModifyRestartCluster',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ModifyRestartClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_restart_cluster(
        self,
        request: hbase_20170115_models.ModifyRestartClusterRequest,
    ) -> hbase_20170115_models.ModifyRestartClusterResponse:
        """
        @param request: ModifyRestartClusterRequest
        @return: ModifyRestartClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_restart_cluster_with_options(request, runtime)

    async def modify_restart_cluster_async(
        self,
        request: hbase_20170115_models.ModifyRestartClusterRequest,
    ) -> hbase_20170115_models.ModifyRestartClusterResponse:
        """
        @param request: ModifyRestartClusterRequest
        @return: ModifyRestartClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_restart_cluster_with_options_async(request, runtime)

    def modify_rollback_has_for_hbase_with_options(
        self,
        request: hbase_20170115_models.ModifyRollbackHasForHbaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ModifyRollbackHasForHbaseResponse:
        """
        @param request: ModifyRollbackHasForHbaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyRollbackHasForHbaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='ModifyRollbackHasForHbase',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ModifyRollbackHasForHbaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_rollback_has_for_hbase_with_options_async(
        self,
        request: hbase_20170115_models.ModifyRollbackHasForHbaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ModifyRollbackHasForHbaseResponse:
        """
        @param request: ModifyRollbackHasForHbaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyRollbackHasForHbaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='ModifyRollbackHasForHbase',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ModifyRollbackHasForHbaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_rollback_has_for_hbase(
        self,
        request: hbase_20170115_models.ModifyRollbackHasForHbaseRequest,
    ) -> hbase_20170115_models.ModifyRollbackHasForHbaseResponse:
        """
        @param request: ModifyRollbackHasForHbaseRequest
        @return: ModifyRollbackHasForHbaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_rollback_has_for_hbase_with_options(request, runtime)

    async def modify_rollback_has_for_hbase_async(
        self,
        request: hbase_20170115_models.ModifyRollbackHasForHbaseRequest,
    ) -> hbase_20170115_models.ModifyRollbackHasForHbaseResponse:
        """
        @param request: ModifyRollbackHasForHbaseRequest
        @return: ModifyRollbackHasForHbaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_rollback_has_for_hbase_with_options_async(request, runtime)

    def modify_subscription_description_with_options(
        self,
        request: hbase_20170115_models.ModifySubscriptionDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ModifySubscriptionDescriptionResponse:
        """
        @summary 更新订阅描述
        
        @param request: ModifySubscriptionDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySubscriptionDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.subscription_description):
            query['SubscriptionDescription'] = request.subscription_description
        if not UtilClient.is_unset(request.subscription_id):
            query['SubscriptionId'] = request.subscription_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySubscriptionDescription',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ModifySubscriptionDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_subscription_description_with_options_async(
        self,
        request: hbase_20170115_models.ModifySubscriptionDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ModifySubscriptionDescriptionResponse:
        """
        @summary 更新订阅描述
        
        @param request: ModifySubscriptionDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySubscriptionDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.subscription_description):
            query['SubscriptionDescription'] = request.subscription_description
        if not UtilClient.is_unset(request.subscription_id):
            query['SubscriptionId'] = request.subscription_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySubscriptionDescription',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ModifySubscriptionDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_subscription_description(
        self,
        request: hbase_20170115_models.ModifySubscriptionDescriptionRequest,
    ) -> hbase_20170115_models.ModifySubscriptionDescriptionResponse:
        """
        @summary 更新订阅描述
        
        @param request: ModifySubscriptionDescriptionRequest
        @return: ModifySubscriptionDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_subscription_description_with_options(request, runtime)

    async def modify_subscription_description_async(
        self,
        request: hbase_20170115_models.ModifySubscriptionDescriptionRequest,
    ) -> hbase_20170115_models.ModifySubscriptionDescriptionResponse:
        """
        @summary 更新订阅描述
        
        @param request: ModifySubscriptionDescriptionRequest
        @return: ModifySubscriptionDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_subscription_description_with_options_async(request, runtime)

    def modify_subscription_mapping_with_options(
        self,
        request: hbase_20170115_models.ModifySubscriptionMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ModifySubscriptionMappingResponse:
        """
        @summary 更新订阅
        
        @param request: ModifySubscriptionMappingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySubscriptionMappingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mapping):
            query['Mapping'] = request.mapping
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.subscription_id):
            query['SubscriptionId'] = request.subscription_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySubscriptionMapping',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ModifySubscriptionMappingResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_subscription_mapping_with_options_async(
        self,
        request: hbase_20170115_models.ModifySubscriptionMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ModifySubscriptionMappingResponse:
        """
        @summary 更新订阅
        
        @param request: ModifySubscriptionMappingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySubscriptionMappingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mapping):
            query['Mapping'] = request.mapping
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.subscription_id):
            query['SubscriptionId'] = request.subscription_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySubscriptionMapping',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ModifySubscriptionMappingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_subscription_mapping(
        self,
        request: hbase_20170115_models.ModifySubscriptionMappingRequest,
    ) -> hbase_20170115_models.ModifySubscriptionMappingResponse:
        """
        @summary 更新订阅
        
        @param request: ModifySubscriptionMappingRequest
        @return: ModifySubscriptionMappingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_subscription_mapping_with_options(request, runtime)

    async def modify_subscription_mapping_async(
        self,
        request: hbase_20170115_models.ModifySubscriptionMappingRequest,
    ) -> hbase_20170115_models.ModifySubscriptionMappingResponse:
        """
        @summary 更新订阅
        
        @param request: ModifySubscriptionMappingRequest
        @return: ModifySubscriptionMappingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_subscription_mapping_with_options_async(request, runtime)

    def modify_subscription_permission_with_options(
        self,
        request: hbase_20170115_models.ModifySubscriptionPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ModifySubscriptionPermissionResponse:
        """
        @summary 更新订阅权限
        
        @param request: ModifySubscriptionPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySubscriptionPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySubscriptionPermission',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ModifySubscriptionPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_subscription_permission_with_options_async(
        self,
        request: hbase_20170115_models.ModifySubscriptionPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ModifySubscriptionPermissionResponse:
        """
        @summary 更新订阅权限
        
        @param request: ModifySubscriptionPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySubscriptionPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySubscriptionPermission',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ModifySubscriptionPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_subscription_permission(
        self,
        request: hbase_20170115_models.ModifySubscriptionPermissionRequest,
    ) -> hbase_20170115_models.ModifySubscriptionPermissionResponse:
        """
        @summary 更新订阅权限
        
        @param request: ModifySubscriptionPermissionRequest
        @return: ModifySubscriptionPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_subscription_permission_with_options(request, runtime)

    async def modify_subscription_permission_async(
        self,
        request: hbase_20170115_models.ModifySubscriptionPermissionRequest,
    ) -> hbase_20170115_models.ModifySubscriptionPermissionResponse:
        """
        @summary 更新订阅权限
        
        @param request: ModifySubscriptionPermissionRequest
        @return: ModifySubscriptionPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_subscription_permission_with_options_async(request, runtime)

    def modify_uiproxy_account_password_with_options(
        self,
        request: hbase_20170115_models.ModifyUIProxyAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ModifyUIProxyAccountPasswordResponse:
        """
        @param request: ModifyUIProxyAccountPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyUIProxyAccountPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='ModifyUIProxyAccountPassword',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ModifyUIProxyAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_uiproxy_account_password_with_options_async(
        self,
        request: hbase_20170115_models.ModifyUIProxyAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ModifyUIProxyAccountPasswordResponse:
        """
        @param request: ModifyUIProxyAccountPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyUIProxyAccountPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='ModifyUIProxyAccountPassword',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ModifyUIProxyAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_uiproxy_account_password(
        self,
        request: hbase_20170115_models.ModifyUIProxyAccountPasswordRequest,
    ) -> hbase_20170115_models.ModifyUIProxyAccountPasswordResponse:
        """
        @param request: ModifyUIProxyAccountPasswordRequest
        @return: ModifyUIProxyAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_uiproxy_account_password_with_options(request, runtime)

    async def modify_uiproxy_account_password_async(
        self,
        request: hbase_20170115_models.ModifyUIProxyAccountPasswordRequest,
    ) -> hbase_20170115_models.ModifyUIProxyAccountPasswordResponse:
        """
        @param request: ModifyUIProxyAccountPasswordRequest
        @return: ModifyUIProxyAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_uiproxy_account_password_with_options_async(request, runtime)

    def modify_upgrade_to_has_for_hbase_with_options(
        self,
        request: hbase_20170115_models.ModifyUpgradeToHasForHbaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ModifyUpgradeToHasForHbaseResponse:
        """
        @param request: ModifyUpgradeToHasForHbaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyUpgradeToHasForHbaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.has_password):
            query['HasPassword'] = request.has_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='ModifyUpgradeToHasForHbase',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ModifyUpgradeToHasForHbaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_upgrade_to_has_for_hbase_with_options_async(
        self,
        request: hbase_20170115_models.ModifyUpgradeToHasForHbaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ModifyUpgradeToHasForHbaseResponse:
        """
        @param request: ModifyUpgradeToHasForHbaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyUpgradeToHasForHbaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.has_password):
            query['HasPassword'] = request.has_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='ModifyUpgradeToHasForHbase',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ModifyUpgradeToHasForHbaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_upgrade_to_has_for_hbase(
        self,
        request: hbase_20170115_models.ModifyUpgradeToHasForHbaseRequest,
    ) -> hbase_20170115_models.ModifyUpgradeToHasForHbaseResponse:
        """
        @param request: ModifyUpgradeToHasForHbaseRequest
        @return: ModifyUpgradeToHasForHbaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_upgrade_to_has_for_hbase_with_options(request, runtime)

    async def modify_upgrade_to_has_for_hbase_async(
        self,
        request: hbase_20170115_models.ModifyUpgradeToHasForHbaseRequest,
    ) -> hbase_20170115_models.ModifyUpgradeToHasForHbaseResponse:
        """
        @param request: ModifyUpgradeToHasForHbaseRequest
        @return: ModifyUpgradeToHasForHbaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_upgrade_to_has_for_hbase_with_options_async(request, runtime)

    def multimod_add_components_with_options(
        self,
        request: hbase_20170115_models.MultimodAddComponentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.MultimodAddComponentsResponse:
        """
        @param request: MultimodAddComponentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MultimodAddComponentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.components):
            query['Components'] = request.components
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='MultimodAddComponents',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.MultimodAddComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def multimod_add_components_with_options_async(
        self,
        request: hbase_20170115_models.MultimodAddComponentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.MultimodAddComponentsResponse:
        """
        @param request: MultimodAddComponentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MultimodAddComponentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.components):
            query['Components'] = request.components
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='MultimodAddComponents',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.MultimodAddComponentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def multimod_add_components(
        self,
        request: hbase_20170115_models.MultimodAddComponentsRequest,
    ) -> hbase_20170115_models.MultimodAddComponentsResponse:
        """
        @param request: MultimodAddComponentsRequest
        @return: MultimodAddComponentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.multimod_add_components_with_options(request, runtime)

    async def multimod_add_components_async(
        self,
        request: hbase_20170115_models.MultimodAddComponentsRequest,
    ) -> hbase_20170115_models.MultimodAddComponentsResponse:
        """
        @param request: MultimodAddComponentsRequest
        @return: MultimodAddComponentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.multimod_add_components_with_options_async(request, runtime)

    def open_backup_with_options(
        self,
        request: hbase_20170115_models.OpenBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.OpenBackupResponse:
        """
        @param request: OpenBackupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenBackupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenBackup',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.OpenBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_backup_with_options_async(
        self,
        request: hbase_20170115_models.OpenBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.OpenBackupResponse:
        """
        @param request: OpenBackupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenBackupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenBackup',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.OpenBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_backup(
        self,
        request: hbase_20170115_models.OpenBackupRequest,
    ) -> hbase_20170115_models.OpenBackupResponse:
        """
        @param request: OpenBackupRequest
        @return: OpenBackupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.open_backup_with_options(request, runtime)

    async def open_backup_async(
        self,
        request: hbase_20170115_models.OpenBackupRequest,
    ) -> hbase_20170115_models.OpenBackupResponse:
        """
        @param request: OpenBackupRequest
        @return: OpenBackupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.open_backup_with_options_async(request, runtime)

    def query_hbase_ha_dbwith_options(
        self,
        request: hbase_20170115_models.QueryHBaseHaDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.QueryHBaseHaDBResponse:
        """
        @param request: QueryHBaseHaDBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryHBaseHaDBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='QueryHBaseHaDB',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.QueryHBaseHaDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_hbase_ha_dbwith_options_async(
        self,
        request: hbase_20170115_models.QueryHBaseHaDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.QueryHBaseHaDBResponse:
        """
        @param request: QueryHBaseHaDBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryHBaseHaDBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='QueryHBaseHaDB',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.QueryHBaseHaDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_hbase_ha_db(
        self,
        request: hbase_20170115_models.QueryHBaseHaDBRequest,
    ) -> hbase_20170115_models.QueryHBaseHaDBResponse:
        """
        @param request: QueryHBaseHaDBRequest
        @return: QueryHBaseHaDBResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_hbase_ha_dbwith_options(request, runtime)

    async def query_hbase_ha_db_async(
        self,
        request: hbase_20170115_models.QueryHBaseHaDBRequest,
    ) -> hbase_20170115_models.QueryHBaseHaDBResponse:
        """
        @param request: QueryHBaseHaDBRequest
        @return: QueryHBaseHaDBResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_hbase_ha_dbwith_options_async(request, runtime)

    def query_spark_relate_hbase_with_options(
        self,
        request: hbase_20170115_models.QuerySparkRelateHBaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.QuerySparkRelateHBaseResponse:
        """
        @param request: QuerySparkRelateHBaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySparkRelateHBaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='QuerySparkRelateHBase',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.QuerySparkRelateHBaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_spark_relate_hbase_with_options_async(
        self,
        request: hbase_20170115_models.QuerySparkRelateHBaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.QuerySparkRelateHBaseResponse:
        """
        @param request: QuerySparkRelateHBaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySparkRelateHBaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='QuerySparkRelateHBase',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.QuerySparkRelateHBaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_spark_relate_hbase(
        self,
        request: hbase_20170115_models.QuerySparkRelateHBaseRequest,
    ) -> hbase_20170115_models.QuerySparkRelateHBaseResponse:
        """
        @param request: QuerySparkRelateHBaseRequest
        @return: QuerySparkRelateHBaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_spark_relate_hbase_with_options(request, runtime)

    async def query_spark_relate_hbase_async(
        self,
        request: hbase_20170115_models.QuerySparkRelateHBaseRequest,
    ) -> hbase_20170115_models.QuerySparkRelateHBaseResponse:
        """
        @param request: QuerySparkRelateHBaseRequest
        @return: QuerySparkRelateHBaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_spark_relate_hbase_with_options_async(request, runtime)

    def query_xpack_related_dbwith_options(
        self,
        request: hbase_20170115_models.QueryXpackRelatedDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.QueryXpackRelatedDBResponse:
        """
        @param request: QueryXpackRelatedDBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryXpackRelatedDBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.relate_db_type):
            query['RelateDbType'] = request.relate_db_type
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
            action='QueryXpackRelatedDB',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.QueryXpackRelatedDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_xpack_related_dbwith_options_async(
        self,
        request: hbase_20170115_models.QueryXpackRelatedDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.QueryXpackRelatedDBResponse:
        """
        @param request: QueryXpackRelatedDBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryXpackRelatedDBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.relate_db_type):
            query['RelateDbType'] = request.relate_db_type
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
            action='QueryXpackRelatedDB',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.QueryXpackRelatedDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_xpack_related_db(
        self,
        request: hbase_20170115_models.QueryXpackRelatedDBRequest,
    ) -> hbase_20170115_models.QueryXpackRelatedDBResponse:
        """
        @param request: QueryXpackRelatedDBRequest
        @return: QueryXpackRelatedDBResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_xpack_related_dbwith_options(request, runtime)

    async def query_xpack_related_db_async(
        self,
        request: hbase_20170115_models.QueryXpackRelatedDBRequest,
    ) -> hbase_20170115_models.QueryXpackRelatedDBResponse:
        """
        @param request: QueryXpackRelatedDBRequest
        @return: QueryXpackRelatedDBResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_xpack_related_dbwith_options_async(request, runtime)

    def relate_db_for_hbase_ha_with_options(
        self,
        request: hbase_20170115_models.RelateDbForHBaseHaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.RelateDbForHBaseHaResponse:
        """
        @param request: RelateDbForHBaseHaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RelateDbForHBaseHaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.ha_active):
            query['HaActive'] = request.ha_active
        if not UtilClient.is_unset(request.ha_active_cluster_key):
            query['HaActiveClusterKey'] = request.ha_active_cluster_key
        if not UtilClient.is_unset(request.ha_active_dbtype):
            query['HaActiveDBType'] = request.ha_active_dbtype
        if not UtilClient.is_unset(request.ha_active_hbase_fs_dir):
            query['HaActiveHbaseFsDir'] = request.ha_active_hbase_fs_dir
        if not UtilClient.is_unset(request.ha_active_hdfs_uri):
            query['HaActiveHdfsUri'] = request.ha_active_hdfs_uri
        if not UtilClient.is_unset(request.ha_active_password):
            query['HaActivePassword'] = request.ha_active_password
        if not UtilClient.is_unset(request.ha_active_user):
            query['HaActiveUser'] = request.ha_active_user
        if not UtilClient.is_unset(request.ha_active_version):
            query['HaActiveVersion'] = request.ha_active_version
        if not UtilClient.is_unset(request.ha_migrate_type):
            query['HaMigrateType'] = request.ha_migrate_type
        if not UtilClient.is_unset(request.ha_standby):
            query['HaStandby'] = request.ha_standby
        if not UtilClient.is_unset(request.ha_standby_cluster_key):
            query['HaStandbyClusterKey'] = request.ha_standby_cluster_key
        if not UtilClient.is_unset(request.ha_standby_dbtype):
            query['HaStandbyDBType'] = request.ha_standby_dbtype
        if not UtilClient.is_unset(request.ha_standby_hbase_fs_dir):
            query['HaStandbyHbaseFsDir'] = request.ha_standby_hbase_fs_dir
        if not UtilClient.is_unset(request.ha_standby_hdfs_uri):
            query['HaStandbyHdfsUri'] = request.ha_standby_hdfs_uri
        if not UtilClient.is_unset(request.ha_standby_password):
            query['HaStandbyPassword'] = request.ha_standby_password
        if not UtilClient.is_unset(request.ha_standby_user):
            query['HaStandbyUser'] = request.ha_standby_user
        if not UtilClient.is_unset(request.ha_standby_version):
            query['HaStandbyVersion'] = request.ha_standby_version
        if not UtilClient.is_unset(request.ha_tables):
            query['HaTables'] = request.ha_tables
        if not UtilClient.is_unset(request.is_active_standard):
            query['IsActiveStandard'] = request.is_active_standard
        if not UtilClient.is_unset(request.is_standby_standard):
            query['IsStandbyStandard'] = request.is_standby_standard
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='RelateDbForHBaseHa',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.RelateDbForHBaseHaResponse(),
            self.call_api(params, req, runtime)
        )

    async def relate_db_for_hbase_ha_with_options_async(
        self,
        request: hbase_20170115_models.RelateDbForHBaseHaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.RelateDbForHBaseHaResponse:
        """
        @param request: RelateDbForHBaseHaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RelateDbForHBaseHaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.ha_active):
            query['HaActive'] = request.ha_active
        if not UtilClient.is_unset(request.ha_active_cluster_key):
            query['HaActiveClusterKey'] = request.ha_active_cluster_key
        if not UtilClient.is_unset(request.ha_active_dbtype):
            query['HaActiveDBType'] = request.ha_active_dbtype
        if not UtilClient.is_unset(request.ha_active_hbase_fs_dir):
            query['HaActiveHbaseFsDir'] = request.ha_active_hbase_fs_dir
        if not UtilClient.is_unset(request.ha_active_hdfs_uri):
            query['HaActiveHdfsUri'] = request.ha_active_hdfs_uri
        if not UtilClient.is_unset(request.ha_active_password):
            query['HaActivePassword'] = request.ha_active_password
        if not UtilClient.is_unset(request.ha_active_user):
            query['HaActiveUser'] = request.ha_active_user
        if not UtilClient.is_unset(request.ha_active_version):
            query['HaActiveVersion'] = request.ha_active_version
        if not UtilClient.is_unset(request.ha_migrate_type):
            query['HaMigrateType'] = request.ha_migrate_type
        if not UtilClient.is_unset(request.ha_standby):
            query['HaStandby'] = request.ha_standby
        if not UtilClient.is_unset(request.ha_standby_cluster_key):
            query['HaStandbyClusterKey'] = request.ha_standby_cluster_key
        if not UtilClient.is_unset(request.ha_standby_dbtype):
            query['HaStandbyDBType'] = request.ha_standby_dbtype
        if not UtilClient.is_unset(request.ha_standby_hbase_fs_dir):
            query['HaStandbyHbaseFsDir'] = request.ha_standby_hbase_fs_dir
        if not UtilClient.is_unset(request.ha_standby_hdfs_uri):
            query['HaStandbyHdfsUri'] = request.ha_standby_hdfs_uri
        if not UtilClient.is_unset(request.ha_standby_password):
            query['HaStandbyPassword'] = request.ha_standby_password
        if not UtilClient.is_unset(request.ha_standby_user):
            query['HaStandbyUser'] = request.ha_standby_user
        if not UtilClient.is_unset(request.ha_standby_version):
            query['HaStandbyVersion'] = request.ha_standby_version
        if not UtilClient.is_unset(request.ha_tables):
            query['HaTables'] = request.ha_tables
        if not UtilClient.is_unset(request.is_active_standard):
            query['IsActiveStandard'] = request.is_active_standard
        if not UtilClient.is_unset(request.is_standby_standard):
            query['IsStandbyStandard'] = request.is_standby_standard
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='RelateDbForHBaseHa',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.RelateDbForHBaseHaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def relate_db_for_hbase_ha(
        self,
        request: hbase_20170115_models.RelateDbForHBaseHaRequest,
    ) -> hbase_20170115_models.RelateDbForHBaseHaResponse:
        """
        @param request: RelateDbForHBaseHaRequest
        @return: RelateDbForHBaseHaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.relate_db_for_hbase_ha_with_options(request, runtime)

    async def relate_db_for_hbase_ha_async(
        self,
        request: hbase_20170115_models.RelateDbForHBaseHaRequest,
    ) -> hbase_20170115_models.RelateDbForHBaseHaResponse:
        """
        @param request: RelateDbForHBaseHaRequest
        @return: RelateDbForHBaseHaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.relate_db_for_hbase_ha_with_options_async(request, runtime)

    def release_public_network_address_with_options(
        self,
        request: hbase_20170115_models.ReleasePublicNetworkAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ReleasePublicNetworkAddressResponse:
        """
        @param request: ReleasePublicNetworkAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleasePublicNetworkAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
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
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ReleasePublicNetworkAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_public_network_address_with_options_async(
        self,
        request: hbase_20170115_models.ReleasePublicNetworkAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ReleasePublicNetworkAddressResponse:
        """
        @param request: ReleasePublicNetworkAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleasePublicNetworkAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
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
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ReleasePublicNetworkAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_public_network_address(
        self,
        request: hbase_20170115_models.ReleasePublicNetworkAddressRequest,
    ) -> hbase_20170115_models.ReleasePublicNetworkAddressResponse:
        """
        @param request: ReleasePublicNetworkAddressRequest
        @return: ReleasePublicNetworkAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_public_network_address_with_options(request, runtime)

    async def release_public_network_address_async(
        self,
        request: hbase_20170115_models.ReleasePublicNetworkAddressRequest,
    ) -> hbase_20170115_models.ReleasePublicNetworkAddressResponse:
        """
        @param request: ReleasePublicNetworkAddressRequest
        @return: ReleasePublicNetworkAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_public_network_address_with_options_async(request, runtime)

    def release_subscription_with_options(
        self,
        request: hbase_20170115_models.ReleaseSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ReleaseSubscriptionResponse:
        """
        @summary 是否订阅
        
        @param request: ReleaseSubscriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseSubscriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.subscription_id):
            query['SubscriptionId'] = request.subscription_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseSubscription',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ReleaseSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_subscription_with_options_async(
        self,
        request: hbase_20170115_models.ReleaseSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ReleaseSubscriptionResponse:
        """
        @summary 是否订阅
        
        @param request: ReleaseSubscriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseSubscriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.subscription_id):
            query['SubscriptionId'] = request.subscription_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseSubscription',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ReleaseSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_subscription(
        self,
        request: hbase_20170115_models.ReleaseSubscriptionRequest,
    ) -> hbase_20170115_models.ReleaseSubscriptionResponse:
        """
        @summary 是否订阅
        
        @param request: ReleaseSubscriptionRequest
        @return: ReleaseSubscriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_subscription_with_options(request, runtime)

    async def release_subscription_async(
        self,
        request: hbase_20170115_models.ReleaseSubscriptionRequest,
    ) -> hbase_20170115_models.ReleaseSubscriptionResponse:
        """
        @summary 是否订阅
        
        @param request: ReleaseSubscriptionRequest
        @return: ReleaseSubscriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_subscription_with_options_async(request, runtime)

    def renew_cluster_with_options(
        self,
        request: hbase_20170115_models.RenewClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.RenewClusterResponse:
        """
        @param request: RenewClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='RenewCluster',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.RenewClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_cluster_with_options_async(
        self,
        request: hbase_20170115_models.RenewClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.RenewClusterResponse:
        """
        @param request: RenewClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='RenewCluster',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.RenewClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_cluster(
        self,
        request: hbase_20170115_models.RenewClusterRequest,
    ) -> hbase_20170115_models.RenewClusterResponse:
        """
        @param request: RenewClusterRequest
        @return: RenewClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.renew_cluster_with_options(request, runtime)

    async def renew_cluster_async(
        self,
        request: hbase_20170115_models.RenewClusterRequest,
    ) -> hbase_20170115_models.RenewClusterResponse:
        """
        @param request: RenewClusterRequest
        @return: RenewClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.renew_cluster_with_options_async(request, runtime)

    def resize_cluster_with_options(
        self,
        request: hbase_20170115_models.ResizeClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ResizeClusterResponse:
        """
        @param request: ResizeClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResizeClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cloud_type):
            query['CloudType'] = request.cloud_type
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cold_storage_size):
            query['ColdStorageSize'] = request.cold_storage_size
        if not UtilClient.is_unset(request.core_disk_quantity):
            query['CoreDiskQuantity'] = request.core_disk_quantity
        if not UtilClient.is_unset(request.core_disk_size):
            query['CoreDiskSize'] = request.core_disk_size
        if not UtilClient.is_unset(request.core_disk_type):
            query['CoreDiskType'] = request.core_disk_type
        if not UtilClient.is_unset(request.core_instance_quantity):
            query['CoreInstanceQuantity'] = request.core_instance_quantity
        if not UtilClient.is_unset(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.is_cold_storage):
            query['IsColdStorage'] = request.is_cold_storage
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.upgrade_type):
            query['UpgradeType'] = request.upgrade_type
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResizeCluster',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ResizeClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def resize_cluster_with_options_async(
        self,
        request: hbase_20170115_models.ResizeClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.ResizeClusterResponse:
        """
        @param request: ResizeClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResizeClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cloud_type):
            query['CloudType'] = request.cloud_type
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cold_storage_size):
            query['ColdStorageSize'] = request.cold_storage_size
        if not UtilClient.is_unset(request.core_disk_quantity):
            query['CoreDiskQuantity'] = request.core_disk_quantity
        if not UtilClient.is_unset(request.core_disk_size):
            query['CoreDiskSize'] = request.core_disk_size
        if not UtilClient.is_unset(request.core_disk_type):
            query['CoreDiskType'] = request.core_disk_type
        if not UtilClient.is_unset(request.core_instance_quantity):
            query['CoreInstanceQuantity'] = request.core_instance_quantity
        if not UtilClient.is_unset(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.is_cold_storage):
            query['IsColdStorage'] = request.is_cold_storage
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.upgrade_type):
            query['UpgradeType'] = request.upgrade_type
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResizeCluster',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.ResizeClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resize_cluster(
        self,
        request: hbase_20170115_models.ResizeClusterRequest,
    ) -> hbase_20170115_models.ResizeClusterResponse:
        """
        @param request: ResizeClusterRequest
        @return: ResizeClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.resize_cluster_with_options(request, runtime)

    async def resize_cluster_async(
        self,
        request: hbase_20170115_models.ResizeClusterRequest,
    ) -> hbase_20170115_models.ResizeClusterResponse:
        """
        @param request: ResizeClusterRequest
        @return: ResizeClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.resize_cluster_with_options_async(request, runtime)

    def spark_relate_hbase_with_options(
        self,
        request: hbase_20170115_models.SparkRelateHBaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.SparkRelateHBaseResponse:
        """
        @param request: SparkRelateHBaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SparkRelateHBaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.hbase_cluster_ids):
            query['HBaseClusterIds'] = request.hbase_cluster_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='SparkRelateHBase',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.SparkRelateHBaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def spark_relate_hbase_with_options_async(
        self,
        request: hbase_20170115_models.SparkRelateHBaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.SparkRelateHBaseResponse:
        """
        @param request: SparkRelateHBaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SparkRelateHBaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.hbase_cluster_ids):
            query['HBaseClusterIds'] = request.hbase_cluster_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='SparkRelateHBase',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.SparkRelateHBaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def spark_relate_hbase(
        self,
        request: hbase_20170115_models.SparkRelateHBaseRequest,
    ) -> hbase_20170115_models.SparkRelateHBaseResponse:
        """
        @param request: SparkRelateHBaseRequest
        @return: SparkRelateHBaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.spark_relate_hbase_with_options(request, runtime)

    async def spark_relate_hbase_async(
        self,
        request: hbase_20170115_models.SparkRelateHBaseRequest,
    ) -> hbase_20170115_models.SparkRelateHBaseResponse:
        """
        @param request: SparkRelateHBaseRequest
        @return: SparkRelateHBaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.spark_relate_hbase_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: hbase_20170115_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.TagResourcesResponse:
        """
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
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: hbase_20170115_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.TagResourcesResponse:
        """
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
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: hbase_20170115_models.TagResourcesRequest,
    ) -> hbase_20170115_models.TagResourcesResponse:
        """
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: hbase_20170115_models.TagResourcesRequest,
    ) -> hbase_20170115_models.TagResourcesResponse:
        """
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: hbase_20170115_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.UntagResourcesResponse:
        """
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
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: hbase_20170115_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.UntagResourcesResponse:
        """
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
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: hbase_20170115_models.UntagResourcesRequest,
    ) -> hbase_20170115_models.UntagResourcesResponse:
        """
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: hbase_20170115_models.UntagResourcesRequest,
    ) -> hbase_20170115_models.UntagResourcesResponse:
        """
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def upgrade_minor_version_with_options(
        self,
        request: hbase_20170115_models.UpgradeMinorVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.UpgradeMinorVersionResponse:
        """
        @param request: UpgradeMinorVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeMinorVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.components):
            query['Components'] = request.components
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.upgrade_version):
            query['UpgradeVersion'] = request.upgrade_version
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeMinorVersion',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.UpgradeMinorVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_minor_version_with_options_async(
        self,
        request: hbase_20170115_models.UpgradeMinorVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.UpgradeMinorVersionResponse:
        """
        @param request: UpgradeMinorVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeMinorVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.components):
            query['Components'] = request.components
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.upgrade_version):
            query['UpgradeVersion'] = request.upgrade_version
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeMinorVersion',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.UpgradeMinorVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_minor_version(
        self,
        request: hbase_20170115_models.UpgradeMinorVersionRequest,
    ) -> hbase_20170115_models.UpgradeMinorVersionResponse:
        """
        @param request: UpgradeMinorVersionRequest
        @return: UpgradeMinorVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_minor_version_with_options(request, runtime)

    async def upgrade_minor_version_async(
        self,
        request: hbase_20170115_models.UpgradeMinorVersionRequest,
    ) -> hbase_20170115_models.UpgradeMinorVersionResponse:
        """
        @param request: UpgradeMinorVersionRequest
        @return: UpgradeMinorVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_minor_version_with_options_async(request, runtime)

    def xpack_relate_dbwith_options(
        self,
        request: hbase_20170115_models.XpackRelateDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.XpackRelateDBResponse:
        """
        @param request: XpackRelateDBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: XpackRelateDBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.db_cluster_ids):
            query['DbClusterIds'] = request.db_cluster_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.relate_db_type):
            query['RelateDbType'] = request.relate_db_type
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
            action='XpackRelateDB',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.XpackRelateDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def xpack_relate_dbwith_options_async(
        self,
        request: hbase_20170115_models.XpackRelateDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20170115_models.XpackRelateDBResponse:
        """
        @param request: XpackRelateDBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: XpackRelateDBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.db_cluster_ids):
            query['DbClusterIds'] = request.db_cluster_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.relate_db_type):
            query['RelateDbType'] = request.relate_db_type
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
            action='XpackRelateDB',
            version='2017-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20170115_models.XpackRelateDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def xpack_relate_db(
        self,
        request: hbase_20170115_models.XpackRelateDBRequest,
    ) -> hbase_20170115_models.XpackRelateDBResponse:
        """
        @param request: XpackRelateDBRequest
        @return: XpackRelateDBResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.xpack_relate_dbwith_options(request, runtime)

    async def xpack_relate_db_async(
        self,
        request: hbase_20170115_models.XpackRelateDBRequest,
    ) -> hbase_20170115_models.XpackRelateDBResponse:
        """
        @param request: XpackRelateDBRequest
        @return: XpackRelateDBResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.xpack_relate_dbwith_options_async(request, runtime)
