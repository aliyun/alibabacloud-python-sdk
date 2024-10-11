# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_clickhouse20220101 import models as clickhouse_20220101_models
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
            'ap-northeast-2-pop': 'clickhouse.aliyuncs.com',
            'ap-southeast-1': 'clickhouse.aliyuncs.com',
            'cn-beijing': 'clickhouse.aliyuncs.com',
            'cn-beijing-finance-1': 'clickhouse.aliyuncs.com',
            'cn-beijing-finance-pop': 'clickhouse.aliyuncs.com',
            'cn-beijing-gov-1': 'clickhouse.aliyuncs.com',
            'cn-beijing-nu16-b01': 'clickhouse.aliyuncs.com',
            'cn-edge-1': 'clickhouse.aliyuncs.com',
            'cn-fujian': 'clickhouse.aliyuncs.com',
            'cn-haidian-cm12-c01': 'clickhouse.aliyuncs.com',
            'cn-hangzhou': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-finance': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-test-306': 'clickhouse.aliyuncs.com',
            'cn-hongkong': 'clickhouse.aliyuncs.com',
            'cn-hongkong-finance-pop': 'clickhouse.aliyuncs.com',
            'cn-north-2-gov-1': 'clickhouse.aliyuncs.com',
            'cn-qingdao': 'clickhouse.aliyuncs.com',
            'cn-qingdao-nebula': 'clickhouse.aliyuncs.com',
            'cn-shanghai': 'clickhouse.aliyuncs.com',
            'cn-shanghai-et15-b01': 'clickhouse.aliyuncs.com',
            'cn-shanghai-et2-b01': 'clickhouse.aliyuncs.com',
            'cn-shanghai-finance-1': 'clickhouse.aliyuncs.com',
            'cn-shanghai-inner': 'clickhouse.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'clickhouse.aliyuncs.com',
            'cn-shenzhen': 'clickhouse.aliyuncs.com',
            'cn-shenzhen-finance-1': 'clickhouse.aliyuncs.com',
            'cn-shenzhen-inner': 'clickhouse.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'clickhouse.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'clickhouse.aliyuncs.com',
            'cn-wuhan': 'clickhouse.aliyuncs.com',
            'cn-yushanfang': 'clickhouse.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'clickhouse.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'clickhouse.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'clickhouse.aliyuncs.com',
            'eu-west-1-oxs': 'clickhouse.aliyuncs.com',
            'me-east-1': 'clickhouse.aliyuncs.com',
            'rus-west-1-pop': 'clickhouse.aliyuncs.com',
            'us-east-1': 'clickhouse.aliyuncs.com',
            'us-west-1': 'clickhouse.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('clickhouse', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def allocate_virtual_ware_house_public_connection_with_options(
        self,
        request: clickhouse_20220101_models.AllocateVirtualWareHousePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.AllocateVirtualWareHousePublicConnectionResponse:
        """
        @summary 申请计算组公网SLB
        
        @param request: AllocateVirtualWareHousePublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocateVirtualWareHousePublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateVirtualWareHousePublicConnection',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.AllocateVirtualWareHousePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_virtual_ware_house_public_connection_with_options_async(
        self,
        request: clickhouse_20220101_models.AllocateVirtualWareHousePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.AllocateVirtualWareHousePublicConnectionResponse:
        """
        @summary 申请计算组公网SLB
        
        @param request: AllocateVirtualWareHousePublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocateVirtualWareHousePublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateVirtualWareHousePublicConnection',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.AllocateVirtualWareHousePublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_virtual_ware_house_public_connection(
        self,
        request: clickhouse_20220101_models.AllocateVirtualWareHousePublicConnectionRequest,
    ) -> clickhouse_20220101_models.AllocateVirtualWareHousePublicConnectionResponse:
        """
        @summary 申请计算组公网SLB
        
        @param request: AllocateVirtualWareHousePublicConnectionRequest
        @return: AllocateVirtualWareHousePublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.allocate_virtual_ware_house_public_connection_with_options(request, runtime)

    async def allocate_virtual_ware_house_public_connection_async(
        self,
        request: clickhouse_20220101_models.AllocateVirtualWareHousePublicConnectionRequest,
    ) -> clickhouse_20220101_models.AllocateVirtualWareHousePublicConnectionResponse:
        """
        @summary 申请计算组公网SLB
        
        @param request: AllocateVirtualWareHousePublicConnectionRequest
        @return: AllocateVirtualWareHousePublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.allocate_virtual_ware_house_public_connection_with_options_async(request, runtime)

    def check_create_cluster_with_options(
        self,
        request: clickhouse_20220101_models.CheckCreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.CheckCreateClusterResponse:
        """
        @summary 创建实例检查
        
        @param request: CheckCreateClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckCreateClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.virtual_ware_house_cache_storage):
            query['VirtualWareHouseCacheStorage'] = request.virtual_ware_house_cache_storage
        if not UtilClient.is_unset(request.virtual_ware_house_class):
            query['VirtualWareHouseClass'] = request.virtual_ware_house_class
        if not UtilClient.is_unset(request.virtual_ware_house_description):
            query['VirtualWareHouseDescription'] = request.virtual_ware_house_description
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckCreateCluster',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.CheckCreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_create_cluster_with_options_async(
        self,
        request: clickhouse_20220101_models.CheckCreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.CheckCreateClusterResponse:
        """
        @summary 创建实例检查
        
        @param request: CheckCreateClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckCreateClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.virtual_ware_house_cache_storage):
            query['VirtualWareHouseCacheStorage'] = request.virtual_ware_house_cache_storage
        if not UtilClient.is_unset(request.virtual_ware_house_class):
            query['VirtualWareHouseClass'] = request.virtual_ware_house_class
        if not UtilClient.is_unset(request.virtual_ware_house_description):
            query['VirtualWareHouseDescription'] = request.virtual_ware_house_description
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckCreateCluster',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.CheckCreateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_create_cluster(
        self,
        request: clickhouse_20220101_models.CheckCreateClusterRequest,
    ) -> clickhouse_20220101_models.CheckCreateClusterResponse:
        """
        @summary 创建实例检查
        
        @param request: CheckCreateClusterRequest
        @return: CheckCreateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_create_cluster_with_options(request, runtime)

    async def check_create_cluster_async(
        self,
        request: clickhouse_20220101_models.CheckCreateClusterRequest,
    ) -> clickhouse_20220101_models.CheckCreateClusterResponse:
        """
        @summary 创建实例检查
        
        @param request: CheckCreateClusterRequest
        @return: CheckCreateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_create_cluster_with_options_async(request, runtime)

    def check_create_virtual_ware_house_with_options(
        self,
        request: clickhouse_20220101_models.CheckCreateVirtualWareHouseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.CheckCreateVirtualWareHouseResponse:
        """
        @summary 创建计算组检查
        
        @param request: CheckCreateVirtualWareHouseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckCreateVirtualWareHouseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_cache_storage):
            query['VirtualWareHouseCacheStorage'] = request.virtual_ware_house_cache_storage
        if not UtilClient.is_unset(request.virtual_ware_house_class):
            query['VirtualWareHouseClass'] = request.virtual_ware_house_class
        if not UtilClient.is_unset(request.virtual_ware_house_description):
            query['VirtualWareHouseDescription'] = request.virtual_ware_house_description
        if not UtilClient.is_unset(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckCreateVirtualWareHouse',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.CheckCreateVirtualWareHouseResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_create_virtual_ware_house_with_options_async(
        self,
        request: clickhouse_20220101_models.CheckCreateVirtualWareHouseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.CheckCreateVirtualWareHouseResponse:
        """
        @summary 创建计算组检查
        
        @param request: CheckCreateVirtualWareHouseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckCreateVirtualWareHouseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_cache_storage):
            query['VirtualWareHouseCacheStorage'] = request.virtual_ware_house_cache_storage
        if not UtilClient.is_unset(request.virtual_ware_house_class):
            query['VirtualWareHouseClass'] = request.virtual_ware_house_class
        if not UtilClient.is_unset(request.virtual_ware_house_description):
            query['VirtualWareHouseDescription'] = request.virtual_ware_house_description
        if not UtilClient.is_unset(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckCreateVirtualWareHouse',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.CheckCreateVirtualWareHouseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_create_virtual_ware_house(
        self,
        request: clickhouse_20220101_models.CheckCreateVirtualWareHouseRequest,
    ) -> clickhouse_20220101_models.CheckCreateVirtualWareHouseResponse:
        """
        @summary 创建计算组检查
        
        @param request: CheckCreateVirtualWareHouseRequest
        @return: CheckCreateVirtualWareHouseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_create_virtual_ware_house_with_options(request, runtime)

    async def check_create_virtual_ware_house_async(
        self,
        request: clickhouse_20220101_models.CheckCreateVirtualWareHouseRequest,
    ) -> clickhouse_20220101_models.CheckCreateVirtualWareHouseResponse:
        """
        @summary 创建计算组检查
        
        @param request: CheckCreateVirtualWareHouseRequest
        @return: CheckCreateVirtualWareHouseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_create_virtual_ware_house_with_options_async(request, runtime)

    def check_delete_virtual_ware_house_with_options(
        self,
        request: clickhouse_20220101_models.CheckDeleteVirtualWareHouseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.CheckDeleteVirtualWareHouseResponse:
        """
        @summary 删除计算组检查
        
        @param request: CheckDeleteVirtualWareHouseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckDeleteVirtualWareHouseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDeleteVirtualWareHouse',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.CheckDeleteVirtualWareHouseResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_delete_virtual_ware_house_with_options_async(
        self,
        request: clickhouse_20220101_models.CheckDeleteVirtualWareHouseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.CheckDeleteVirtualWareHouseResponse:
        """
        @summary 删除计算组检查
        
        @param request: CheckDeleteVirtualWareHouseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckDeleteVirtualWareHouseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDeleteVirtualWareHouse',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.CheckDeleteVirtualWareHouseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_delete_virtual_ware_house(
        self,
        request: clickhouse_20220101_models.CheckDeleteVirtualWareHouseRequest,
    ) -> clickhouse_20220101_models.CheckDeleteVirtualWareHouseResponse:
        """
        @summary 删除计算组检查
        
        @param request: CheckDeleteVirtualWareHouseRequest
        @return: CheckDeleteVirtualWareHouseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_delete_virtual_ware_house_with_options(request, runtime)

    async def check_delete_virtual_ware_house_async(
        self,
        request: clickhouse_20220101_models.CheckDeleteVirtualWareHouseRequest,
    ) -> clickhouse_20220101_models.CheckDeleteVirtualWareHouseResponse:
        """
        @summary 删除计算组检查
        
        @param request: CheckDeleteVirtualWareHouseRequest
        @return: CheckDeleteVirtualWareHouseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_delete_virtual_ware_house_with_options_async(request, runtime)

    def check_modify_virtual_ware_house_resource_with_options(
        self,
        request: clickhouse_20220101_models.CheckModifyVirtualWareHouseResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.CheckModifyVirtualWareHouseResourceResponse:
        """
        @summary 计算组变配检查
        
        @param request: CheckModifyVirtualWareHouseResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckModifyVirtualWareHouseResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_cache_storage):
            query['VirtualWareHouseCacheStorage'] = request.virtual_ware_house_cache_storage
        if not UtilClient.is_unset(request.virtual_ware_house_class):
            query['VirtualWareHouseClass'] = request.virtual_ware_house_class
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckModifyVirtualWareHouseResource',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.CheckModifyVirtualWareHouseResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_modify_virtual_ware_house_resource_with_options_async(
        self,
        request: clickhouse_20220101_models.CheckModifyVirtualWareHouseResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.CheckModifyVirtualWareHouseResourceResponse:
        """
        @summary 计算组变配检查
        
        @param request: CheckModifyVirtualWareHouseResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckModifyVirtualWareHouseResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_cache_storage):
            query['VirtualWareHouseCacheStorage'] = request.virtual_ware_house_cache_storage
        if not UtilClient.is_unset(request.virtual_ware_house_class):
            query['VirtualWareHouseClass'] = request.virtual_ware_house_class
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckModifyVirtualWareHouseResource',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.CheckModifyVirtualWareHouseResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_modify_virtual_ware_house_resource(
        self,
        request: clickhouse_20220101_models.CheckModifyVirtualWareHouseResourceRequest,
    ) -> clickhouse_20220101_models.CheckModifyVirtualWareHouseResourceResponse:
        """
        @summary 计算组变配检查
        
        @param request: CheckModifyVirtualWareHouseResourceRequest
        @return: CheckModifyVirtualWareHouseResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_modify_virtual_ware_house_resource_with_options(request, runtime)

    async def check_modify_virtual_ware_house_resource_async(
        self,
        request: clickhouse_20220101_models.CheckModifyVirtualWareHouseResourceRequest,
    ) -> clickhouse_20220101_models.CheckModifyVirtualWareHouseResourceResponse:
        """
        @summary 计算组变配检查
        
        @param request: CheckModifyVirtualWareHouseResourceRequest
        @return: CheckModifyVirtualWareHouseResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_modify_virtual_ware_house_resource_with_options_async(request, runtime)

    def create_account_with_options(
        self,
        request: clickhouse_20220101_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.CreateAccountResponse:
        """
        @summary 创建实例账户
        
        @param request: CreateAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_sha_256hex):
            query['PasswordSha256Hex'] = request.password_sha_256hex
        if not UtilClient.is_unset(request.privilege_type):
            query['PrivilegeType'] = request.privilege_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.CreateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_account_with_options_async(
        self,
        request: clickhouse_20220101_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.CreateAccountResponse:
        """
        @summary 创建实例账户
        
        @param request: CreateAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_sha_256hex):
            query['PasswordSha256Hex'] = request.password_sha_256hex
        if not UtilClient.is_unset(request.privilege_type):
            query['PrivilegeType'] = request.privilege_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.CreateAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_account(
        self,
        request: clickhouse_20220101_models.CreateAccountRequest,
    ) -> clickhouse_20220101_models.CreateAccountResponse:
        """
        @summary 创建实例账户
        
        @param request: CreateAccountRequest
        @return: CreateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: clickhouse_20220101_models.CreateAccountRequest,
    ) -> clickhouse_20220101_models.CreateAccountResponse:
        """
        @summary 创建实例账户
        
        @param request: CreateAccountRequest
        @return: CreateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def create_cluster_with_options(
        self,
        request: clickhouse_20220101_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.CreateClusterResponse:
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
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.virtual_ware_house_cache_storage):
            query['VirtualWareHouseCacheStorage'] = request.virtual_ware_house_cache_storage
        if not UtilClient.is_unset(request.virtual_ware_house_class):
            query['VirtualWareHouseClass'] = request.virtual_ware_house_class
        if not UtilClient.is_unset(request.virtual_ware_house_description):
            query['VirtualWareHouseDescription'] = request.virtual_ware_house_description
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_with_options_async(
        self,
        request: clickhouse_20220101_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.CreateClusterResponse:
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
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.virtual_ware_house_cache_storage):
            query['VirtualWareHouseCacheStorage'] = request.virtual_ware_house_cache_storage
        if not UtilClient.is_unset(request.virtual_ware_house_class):
            query['VirtualWareHouseClass'] = request.virtual_ware_house_class
        if not UtilClient.is_unset(request.virtual_ware_house_description):
            query['VirtualWareHouseDescription'] = request.virtual_ware_house_description
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.CreateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster(
        self,
        request: clickhouse_20220101_models.CreateClusterRequest,
    ) -> clickhouse_20220101_models.CreateClusterResponse:
        """
        @summary 创建实例
        
        @param request: CreateClusterRequest
        @return: CreateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    async def create_cluster_async(
        self,
        request: clickhouse_20220101_models.CreateClusterRequest,
    ) -> clickhouse_20220101_models.CreateClusterResponse:
        """
        @summary 创建实例
        
        @param request: CreateClusterRequest
        @return: CreateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_with_options_async(request, runtime)

    def create_virtual_ware_house_with_options(
        self,
        request: clickhouse_20220101_models.CreateVirtualWareHouseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.CreateVirtualWareHouseResponse:
        """
        @summary 创建计算组
        
        @param request: CreateVirtualWareHouseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVirtualWareHouseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_cache_storage):
            query['VirtualWareHouseCacheStorage'] = request.virtual_ware_house_cache_storage
        if not UtilClient.is_unset(request.virtual_ware_house_class):
            query['VirtualWareHouseClass'] = request.virtual_ware_house_class
        if not UtilClient.is_unset(request.virtual_ware_house_description):
            query['VirtualWareHouseDescription'] = request.virtual_ware_house_description
        if not UtilClient.is_unset(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVirtualWareHouse',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.CreateVirtualWareHouseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_virtual_ware_house_with_options_async(
        self,
        request: clickhouse_20220101_models.CreateVirtualWareHouseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.CreateVirtualWareHouseResponse:
        """
        @summary 创建计算组
        
        @param request: CreateVirtualWareHouseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVirtualWareHouseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_cache_storage):
            query['VirtualWareHouseCacheStorage'] = request.virtual_ware_house_cache_storage
        if not UtilClient.is_unset(request.virtual_ware_house_class):
            query['VirtualWareHouseClass'] = request.virtual_ware_house_class
        if not UtilClient.is_unset(request.virtual_ware_house_description):
            query['VirtualWareHouseDescription'] = request.virtual_ware_house_description
        if not UtilClient.is_unset(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVirtualWareHouse',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.CreateVirtualWareHouseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_virtual_ware_house(
        self,
        request: clickhouse_20220101_models.CreateVirtualWareHouseRequest,
    ) -> clickhouse_20220101_models.CreateVirtualWareHouseResponse:
        """
        @summary 创建计算组
        
        @param request: CreateVirtualWareHouseRequest
        @return: CreateVirtualWareHouseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_virtual_ware_house_with_options(request, runtime)

    async def create_virtual_ware_house_async(
        self,
        request: clickhouse_20220101_models.CreateVirtualWareHouseRequest,
    ) -> clickhouse_20220101_models.CreateVirtualWareHouseResponse:
        """
        @summary 创建计算组
        
        @param request: CreateVirtualWareHouseRequest
        @return: CreateVirtualWareHouseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_virtual_ware_house_with_options_async(request, runtime)

    def delete_account_with_options(
        self,
        request: clickhouse_20220101_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DeleteAccountResponse:
        """
        @summary 删除实例账户
        
        @param request: DeleteAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DeleteAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_account_with_options_async(
        self,
        request: clickhouse_20220101_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DeleteAccountResponse:
        """
        @summary 删除实例账户
        
        @param request: DeleteAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DeleteAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_account(
        self,
        request: clickhouse_20220101_models.DeleteAccountRequest,
    ) -> clickhouse_20220101_models.DeleteAccountResponse:
        """
        @summary 删除实例账户
        
        @param request: DeleteAccountRequest
        @return: DeleteAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    async def delete_account_async(
        self,
        request: clickhouse_20220101_models.DeleteAccountRequest,
    ) -> clickhouse_20220101_models.DeleteAccountResponse:
        """
        @summary 删除实例账户
        
        @param request: DeleteAccountRequest
        @return: DeleteAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_account_with_options_async(request, runtime)

    def delete_cluster_with_options(
        self,
        request: clickhouse_20220101_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DeleteClusterResponse:
        """
        @summary 删除实例
        
        @param request: DeleteClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DeleteClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_with_options_async(
        self,
        request: clickhouse_20220101_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DeleteClusterResponse:
        """
        @summary 删除实例
        
        @param request: DeleteClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DeleteClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster(
        self,
        request: clickhouse_20220101_models.DeleteClusterRequest,
    ) -> clickhouse_20220101_models.DeleteClusterResponse:
        """
        @summary 删除实例
        
        @param request: DeleteClusterRequest
        @return: DeleteClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    async def delete_cluster_async(
        self,
        request: clickhouse_20220101_models.DeleteClusterRequest,
    ) -> clickhouse_20220101_models.DeleteClusterResponse:
        """
        @summary 删除实例
        
        @param request: DeleteClusterRequest
        @return: DeleteClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_cluster_with_options_async(request, runtime)

    def delete_cluster_security_ipgroup_with_options(
        self,
        request: clickhouse_20220101_models.DeleteClusterSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DeleteClusterSecurityIPGroupResponse:
        """
        @summary 删除实例IP白名单组
        
        @param request: DeleteClusterSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClusterSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteClusterSecurityIPGroup',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DeleteClusterSecurityIPGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_security_ipgroup_with_options_async(
        self,
        request: clickhouse_20220101_models.DeleteClusterSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DeleteClusterSecurityIPGroupResponse:
        """
        @summary 删除实例IP白名单组
        
        @param request: DeleteClusterSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClusterSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteClusterSecurityIPGroup',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DeleteClusterSecurityIPGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster_security_ipgroup(
        self,
        request: clickhouse_20220101_models.DeleteClusterSecurityIPGroupRequest,
    ) -> clickhouse_20220101_models.DeleteClusterSecurityIPGroupResponse:
        """
        @summary 删除实例IP白名单组
        
        @param request: DeleteClusterSecurityIPGroupRequest
        @return: DeleteClusterSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_security_ipgroup_with_options(request, runtime)

    async def delete_cluster_security_ipgroup_async(
        self,
        request: clickhouse_20220101_models.DeleteClusterSecurityIPGroupRequest,
    ) -> clickhouse_20220101_models.DeleteClusterSecurityIPGroupResponse:
        """
        @summary 删除实例IP白名单组
        
        @param request: DeleteClusterSecurityIPGroupRequest
        @return: DeleteClusterSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_cluster_security_ipgroup_with_options_async(request, runtime)

    def delete_virtual_ware_house_with_options(
        self,
        request: clickhouse_20220101_models.DeleteVirtualWareHouseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DeleteVirtualWareHouseResponse:
        """
        @summary 删除计算组
        
        @param request: DeleteVirtualWareHouseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVirtualWareHouseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVirtualWareHouse',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DeleteVirtualWareHouseResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_virtual_ware_house_with_options_async(
        self,
        request: clickhouse_20220101_models.DeleteVirtualWareHouseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DeleteVirtualWareHouseResponse:
        """
        @summary 删除计算组
        
        @param request: DeleteVirtualWareHouseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVirtualWareHouseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVirtualWareHouse',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DeleteVirtualWareHouseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_virtual_ware_house(
        self,
        request: clickhouse_20220101_models.DeleteVirtualWareHouseRequest,
    ) -> clickhouse_20220101_models.DeleteVirtualWareHouseResponse:
        """
        @summary 删除计算组
        
        @param request: DeleteVirtualWareHouseRequest
        @return: DeleteVirtualWareHouseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_virtual_ware_house_with_options(request, runtime)

    async def delete_virtual_ware_house_async(
        self,
        request: clickhouse_20220101_models.DeleteVirtualWareHouseRequest,
    ) -> clickhouse_20220101_models.DeleteVirtualWareHouseResponse:
        """
        @summary 删除计算组
        
        @param request: DeleteVirtualWareHouseRequest
        @return: DeleteVirtualWareHouseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_virtual_ware_house_with_options_async(request, runtime)

    def describe_account_with_options(
        self,
        request: clickhouse_20220101_models.DescribeAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DescribeAccountResponse:
        """
        @summary 查看实例账户详情
        
        @param request: DescribeAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccount',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DescribeAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_account_with_options_async(
        self,
        request: clickhouse_20220101_models.DescribeAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DescribeAccountResponse:
        """
        @summary 查看实例账户详情
        
        @param request: DescribeAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccount',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DescribeAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_account(
        self,
        request: clickhouse_20220101_models.DescribeAccountRequest,
    ) -> clickhouse_20220101_models.DescribeAccountResponse:
        """
        @summary 查看实例账户详情
        
        @param request: DescribeAccountRequest
        @return: DescribeAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_account_with_options(request, runtime)

    async def describe_account_async(
        self,
        request: clickhouse_20220101_models.DescribeAccountRequest,
    ) -> clickhouse_20220101_models.DescribeAccountResponse:
        """
        @summary 查看实例账户详情
        
        @param request: DescribeAccountRequest
        @return: DescribeAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_account_with_options_async(request, runtime)

    def describe_cluster_with_options(
        self,
        request: clickhouse_20220101_models.DescribeClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DescribeClusterResponse:
        """
        @summary 查看实例详情
        
        @param request: DescribeClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCluster',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DescribeClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_with_options_async(
        self,
        request: clickhouse_20220101_models.DescribeClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DescribeClusterResponse:
        """
        @summary 查看实例详情
        
        @param request: DescribeClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCluster',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DescribeClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster(
        self,
        request: clickhouse_20220101_models.DescribeClusterRequest,
    ) -> clickhouse_20220101_models.DescribeClusterResponse:
        """
        @summary 查看实例详情
        
        @param request: DescribeClusterRequest
        @return: DescribeClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_with_options(request, runtime)

    async def describe_cluster_async(
        self,
        request: clickhouse_20220101_models.DescribeClusterRequest,
    ) -> clickhouse_20220101_models.DescribeClusterResponse:
        """
        @summary 查看实例详情
        
        @param request: DescribeClusterRequest
        @return: DescribeClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_with_options_async(request, runtime)

    def describe_cluster_security_info_with_options(
        self,
        request: clickhouse_20220101_models.DescribeClusterSecurityInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DescribeClusterSecurityInfoResponse:
        """
        @summary 查看实例白名单配置
        
        @param request: DescribeClusterSecurityInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterSecurityInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterSecurityInfo',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DescribeClusterSecurityInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_security_info_with_options_async(
        self,
        request: clickhouse_20220101_models.DescribeClusterSecurityInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DescribeClusterSecurityInfoResponse:
        """
        @summary 查看实例白名单配置
        
        @param request: DescribeClusterSecurityInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterSecurityInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterSecurityInfo',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DescribeClusterSecurityInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_security_info(
        self,
        request: clickhouse_20220101_models.DescribeClusterSecurityInfoRequest,
    ) -> clickhouse_20220101_models.DescribeClusterSecurityInfoResponse:
        """
        @summary 查看实例白名单配置
        
        @param request: DescribeClusterSecurityInfoRequest
        @return: DescribeClusterSecurityInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_security_info_with_options(request, runtime)

    async def describe_cluster_security_info_async(
        self,
        request: clickhouse_20220101_models.DescribeClusterSecurityInfoRequest,
    ) -> clickhouse_20220101_models.DescribeClusterSecurityInfoResponse:
        """
        @summary 查看实例白名单配置
        
        @param request: DescribeClusterSecurityInfoRequest
        @return: DescribeClusterSecurityInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_security_info_with_options_async(request, runtime)

    def describe_cluster_status_set_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DescribeClusterStatusSetResponse:
        """
        @summary 查看实例状态集合
        
        @param request: DescribeClusterStatusSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterStatusSetResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeClusterStatusSet',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DescribeClusterStatusSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_status_set_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DescribeClusterStatusSetResponse:
        """
        @summary 查看实例状态集合
        
        @param request: DescribeClusterStatusSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterStatusSetResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeClusterStatusSet',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DescribeClusterStatusSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_status_set(self) -> clickhouse_20220101_models.DescribeClusterStatusSetResponse:
        """
        @summary 查看实例状态集合
        
        @return: DescribeClusterStatusSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_status_set_with_options(runtime)

    async def describe_cluster_status_set_async(self) -> clickhouse_20220101_models.DescribeClusterStatusSetResponse:
        """
        @summary 查看实例状态集合
        
        @return: DescribeClusterStatusSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_status_set_with_options_async(runtime)

    def describe_regions_with_options(
        self,
        request: clickhouse_20220101_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DescribeRegionsResponse:
        """
        @summary 查看可服务Region和Zone
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: clickhouse_20220101_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DescribeRegionsResponse:
        """
        @summary 查看可服务Region和Zone
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: clickhouse_20220101_models.DescribeRegionsRequest,
    ) -> clickhouse_20220101_models.DescribeRegionsResponse:
        """
        @summary 查看可服务Region和Zone
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: clickhouse_20220101_models.DescribeRegionsRequest,
    ) -> clickhouse_20220101_models.DescribeRegionsResponse:
        """
        @summary 查看可服务Region和Zone
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_running_query_with_options(
        self,
        request: clickhouse_20220101_models.DescribeRunningQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DescribeRunningQueryResponse:
        """
        @summary 查看计算组正在运行查询列表
        
        @param request: DescribeRunningQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRunningQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_duration_ms):
            query['QueryDurationMs'] = request.query_duration_ms
        if not UtilClient.is_unset(request.query_id):
            query['QueryId'] = request.query_id
        if not UtilClient.is_unset(request.query_key_word):
            query['QueryKeyWord'] = request.query_key_word
        if not UtilClient.is_unset(request.query_user):
            query['QueryUser'] = request.query_user
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRunningQuery',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DescribeRunningQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_running_query_with_options_async(
        self,
        request: clickhouse_20220101_models.DescribeRunningQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DescribeRunningQueryResponse:
        """
        @summary 查看计算组正在运行查询列表
        
        @param request: DescribeRunningQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRunningQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_duration_ms):
            query['QueryDurationMs'] = request.query_duration_ms
        if not UtilClient.is_unset(request.query_id):
            query['QueryId'] = request.query_id
        if not UtilClient.is_unset(request.query_key_word):
            query['QueryKeyWord'] = request.query_key_word
        if not UtilClient.is_unset(request.query_user):
            query['QueryUser'] = request.query_user
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRunningQuery',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DescribeRunningQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_running_query(
        self,
        request: clickhouse_20220101_models.DescribeRunningQueryRequest,
    ) -> clickhouse_20220101_models.DescribeRunningQueryResponse:
        """
        @summary 查看计算组正在运行查询列表
        
        @param request: DescribeRunningQueryRequest
        @return: DescribeRunningQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_running_query_with_options(request, runtime)

    async def describe_running_query_async(
        self,
        request: clickhouse_20220101_models.DescribeRunningQueryRequest,
    ) -> clickhouse_20220101_models.DescribeRunningQueryResponse:
        """
        @summary 查看计算组正在运行查询列表
        
        @param request: DescribeRunningQueryRequest
        @return: DescribeRunningQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_running_query_with_options_async(request, runtime)

    def describe_slow_query_with_options(
        self,
        request: clickhouse_20220101_models.DescribeSlowQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DescribeSlowQueryResponse:
        """
        @summary 查看计算组慢查询详情
        
        @param request: DescribeSlowQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_duration_ms):
            query['QueryDurationMs'] = request.query_duration_ms
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowQuery',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DescribeSlowQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_query_with_options_async(
        self,
        request: clickhouse_20220101_models.DescribeSlowQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DescribeSlowQueryResponse:
        """
        @summary 查看计算组慢查询详情
        
        @param request: DescribeSlowQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_duration_ms):
            query['QueryDurationMs'] = request.query_duration_ms
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowQuery',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DescribeSlowQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slow_query(
        self,
        request: clickhouse_20220101_models.DescribeSlowQueryRequest,
    ) -> clickhouse_20220101_models.DescribeSlowQueryResponse:
        """
        @summary 查看计算组慢查询详情
        
        @param request: DescribeSlowQueryRequest
        @return: DescribeSlowQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_query_with_options(request, runtime)

    async def describe_slow_query_async(
        self,
        request: clickhouse_20220101_models.DescribeSlowQueryRequest,
    ) -> clickhouse_20220101_models.DescribeSlowQueryResponse:
        """
        @summary 查看计算组慢查询详情
        
        @param request: DescribeSlowQueryRequest
        @return: DescribeSlowQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_query_with_options_async(request, runtime)

    def describe_slow_query_trend_with_options(
        self,
        request: clickhouse_20220101_models.DescribeSlowQueryTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DescribeSlowQueryTrendResponse:
        """
        @summary 查看计算组慢查询趋势 以1分钟为间隔统计
        
        @param request: DescribeSlowQueryTrendRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowQueryTrendResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.query_duration_ms):
            query['QueryDurationMs'] = request.query_duration_ms
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowQueryTrend',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DescribeSlowQueryTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_query_trend_with_options_async(
        self,
        request: clickhouse_20220101_models.DescribeSlowQueryTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DescribeSlowQueryTrendResponse:
        """
        @summary 查看计算组慢查询趋势 以1分钟为间隔统计
        
        @param request: DescribeSlowQueryTrendRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowQueryTrendResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.query_duration_ms):
            query['QueryDurationMs'] = request.query_duration_ms
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowQueryTrend',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DescribeSlowQueryTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slow_query_trend(
        self,
        request: clickhouse_20220101_models.DescribeSlowQueryTrendRequest,
    ) -> clickhouse_20220101_models.DescribeSlowQueryTrendResponse:
        """
        @summary 查看计算组慢查询趋势 以1分钟为间隔统计
        
        @param request: DescribeSlowQueryTrendRequest
        @return: DescribeSlowQueryTrendResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_query_trend_with_options(request, runtime)

    async def describe_slow_query_trend_async(
        self,
        request: clickhouse_20220101_models.DescribeSlowQueryTrendRequest,
    ) -> clickhouse_20220101_models.DescribeSlowQueryTrendResponse:
        """
        @summary 查看计算组慢查询趋势 以1分钟为间隔统计
        
        @param request: DescribeSlowQueryTrendRequest
        @return: DescribeSlowQueryTrendResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_query_trend_with_options_async(request, runtime)

    def describe_virtual_ware_house_with_options(
        self,
        request: clickhouse_20220101_models.DescribeVirtualWareHouseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DescribeVirtualWareHouseResponse:
        """
        @summary 查看计算组详情
        
        @param request: DescribeVirtualWareHouseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVirtualWareHouseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVirtualWareHouse',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DescribeVirtualWareHouseResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_virtual_ware_house_with_options_async(
        self,
        request: clickhouse_20220101_models.DescribeVirtualWareHouseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DescribeVirtualWareHouseResponse:
        """
        @summary 查看计算组详情
        
        @param request: DescribeVirtualWareHouseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVirtualWareHouseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVirtualWareHouse',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DescribeVirtualWareHouseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_virtual_ware_house(
        self,
        request: clickhouse_20220101_models.DescribeVirtualWareHouseRequest,
    ) -> clickhouse_20220101_models.DescribeVirtualWareHouseResponse:
        """
        @summary 查看计算组详情
        
        @param request: DescribeVirtualWareHouseRequest
        @return: DescribeVirtualWareHouseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_virtual_ware_house_with_options(request, runtime)

    async def describe_virtual_ware_house_async(
        self,
        request: clickhouse_20220101_models.DescribeVirtualWareHouseRequest,
    ) -> clickhouse_20220101_models.DescribeVirtualWareHouseResponse:
        """
        @summary 查看计算组详情
        
        @param request: DescribeVirtualWareHouseRequest
        @return: DescribeVirtualWareHouseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_virtual_ware_house_with_options_async(request, runtime)

    def describe_virtual_ware_house_class_set_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DescribeVirtualWareHouseClassSetResponse:
        """
        @summary 查看计算组规格码集合
        
        @param request: DescribeVirtualWareHouseClassSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVirtualWareHouseClassSetResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeVirtualWareHouseClassSet',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DescribeVirtualWareHouseClassSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_virtual_ware_house_class_set_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DescribeVirtualWareHouseClassSetResponse:
        """
        @summary 查看计算组规格码集合
        
        @param request: DescribeVirtualWareHouseClassSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVirtualWareHouseClassSetResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeVirtualWareHouseClassSet',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DescribeVirtualWareHouseClassSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_virtual_ware_house_class_set(self) -> clickhouse_20220101_models.DescribeVirtualWareHouseClassSetResponse:
        """
        @summary 查看计算组规格码集合
        
        @return: DescribeVirtualWareHouseClassSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_virtual_ware_house_class_set_with_options(runtime)

    async def describe_virtual_ware_house_class_set_async(self) -> clickhouse_20220101_models.DescribeVirtualWareHouseClassSetResponse:
        """
        @summary 查看计算组规格码集合
        
        @return: DescribeVirtualWareHouseClassSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_virtual_ware_house_class_set_with_options_async(runtime)

    def describe_virtual_ware_house_endpoint_info_with_options(
        self,
        request: clickhouse_20220101_models.DescribeVirtualWareHouseEndpointInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DescribeVirtualWareHouseEndpointInfoResponse:
        """
        @summary 查看计算组链接信息
        
        @param request: DescribeVirtualWareHouseEndpointInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVirtualWareHouseEndpointInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVirtualWareHouseEndpointInfo',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DescribeVirtualWareHouseEndpointInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_virtual_ware_house_endpoint_info_with_options_async(
        self,
        request: clickhouse_20220101_models.DescribeVirtualWareHouseEndpointInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DescribeVirtualWareHouseEndpointInfoResponse:
        """
        @summary 查看计算组链接信息
        
        @param request: DescribeVirtualWareHouseEndpointInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVirtualWareHouseEndpointInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVirtualWareHouseEndpointInfo',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DescribeVirtualWareHouseEndpointInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_virtual_ware_house_endpoint_info(
        self,
        request: clickhouse_20220101_models.DescribeVirtualWareHouseEndpointInfoRequest,
    ) -> clickhouse_20220101_models.DescribeVirtualWareHouseEndpointInfoResponse:
        """
        @summary 查看计算组链接信息
        
        @param request: DescribeVirtualWareHouseEndpointInfoRequest
        @return: DescribeVirtualWareHouseEndpointInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_virtual_ware_house_endpoint_info_with_options(request, runtime)

    async def describe_virtual_ware_house_endpoint_info_async(
        self,
        request: clickhouse_20220101_models.DescribeVirtualWareHouseEndpointInfoRequest,
    ) -> clickhouse_20220101_models.DescribeVirtualWareHouseEndpointInfoResponse:
        """
        @summary 查看计算组链接信息
        
        @param request: DescribeVirtualWareHouseEndpointInfoRequest
        @return: DescribeVirtualWareHouseEndpointInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_virtual_ware_house_endpoint_info_with_options_async(request, runtime)

    def describe_virtual_ware_house_status_set_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DescribeVirtualWareHouseStatusSetResponse:
        """
        @summary 查看计算组状态集合
        
        @param request: DescribeVirtualWareHouseStatusSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVirtualWareHouseStatusSetResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeVirtualWareHouseStatusSet',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DescribeVirtualWareHouseStatusSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_virtual_ware_house_status_set_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.DescribeVirtualWareHouseStatusSetResponse:
        """
        @summary 查看计算组状态集合
        
        @param request: DescribeVirtualWareHouseStatusSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVirtualWareHouseStatusSetResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeVirtualWareHouseStatusSet',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.DescribeVirtualWareHouseStatusSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_virtual_ware_house_status_set(self) -> clickhouse_20220101_models.DescribeVirtualWareHouseStatusSetResponse:
        """
        @summary 查看计算组状态集合
        
        @return: DescribeVirtualWareHouseStatusSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_virtual_ware_house_status_set_with_options(runtime)

    async def describe_virtual_ware_house_status_set_async(self) -> clickhouse_20220101_models.DescribeVirtualWareHouseStatusSetResponse:
        """
        @summary 查看计算组状态集合
        
        @return: DescribeVirtualWareHouseStatusSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_virtual_ware_house_status_set_with_options_async(runtime)

    def get_distributed_tables_buffer_size_with_options(
        self,
        request: clickhouse_20220101_models.GetDistributedTablesBufferSizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.GetDistributedTablesBufferSizeResponse:
        """
        @summary 查询分布式表缓存大小
        
        @param request: GetDistributedTablesBufferSizeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDistributedTablesBufferSizeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDistributedTablesBufferSize',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.GetDistributedTablesBufferSizeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_distributed_tables_buffer_size_with_options_async(
        self,
        request: clickhouse_20220101_models.GetDistributedTablesBufferSizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.GetDistributedTablesBufferSizeResponse:
        """
        @summary 查询分布式表缓存大小
        
        @param request: GetDistributedTablesBufferSizeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDistributedTablesBufferSizeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDistributedTablesBufferSize',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.GetDistributedTablesBufferSizeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_distributed_tables_buffer_size(
        self,
        request: clickhouse_20220101_models.GetDistributedTablesBufferSizeRequest,
    ) -> clickhouse_20220101_models.GetDistributedTablesBufferSizeResponse:
        """
        @summary 查询分布式表缓存大小
        
        @param request: GetDistributedTablesBufferSizeRequest
        @return: GetDistributedTablesBufferSizeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_distributed_tables_buffer_size_with_options(request, runtime)

    async def get_distributed_tables_buffer_size_async(
        self,
        request: clickhouse_20220101_models.GetDistributedTablesBufferSizeRequest,
    ) -> clickhouse_20220101_models.GetDistributedTablesBufferSizeResponse:
        """
        @summary 查询分布式表缓存大小
        
        @param request: GetDistributedTablesBufferSizeRequest
        @return: GetDistributedTablesBufferSizeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_distributed_tables_buffer_size_with_options_async(request, runtime)

    def kill_query_with_options(
        self,
        request: clickhouse_20220101_models.KillQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.KillQueryResponse:
        """
        @summary Kill计算组查询
        
        @param request: KillQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: KillQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.query_ids):
            query['QueryIds'] = request.query_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='KillQuery',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.KillQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def kill_query_with_options_async(
        self,
        request: clickhouse_20220101_models.KillQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.KillQueryResponse:
        """
        @summary Kill计算组查询
        
        @param request: KillQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: KillQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.query_ids):
            query['QueryIds'] = request.query_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='KillQuery',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.KillQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kill_query(
        self,
        request: clickhouse_20220101_models.KillQueryRequest,
    ) -> clickhouse_20220101_models.KillQueryResponse:
        """
        @summary Kill计算组查询
        
        @param request: KillQueryRequest
        @return: KillQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.kill_query_with_options(request, runtime)

    async def kill_query_async(
        self,
        request: clickhouse_20220101_models.KillQueryRequest,
    ) -> clickhouse_20220101_models.KillQueryResponse:
        """
        @summary Kill计算组查询
        
        @param request: KillQueryRequest
        @return: KillQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.kill_query_with_options_async(request, runtime)

    def list_accounts_with_options(
        self,
        request: clickhouse_20220101_models.ListAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.ListAccountsResponse:
        """
        @summary 查看实例账户详情列表
        
        @param request: ListAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccounts',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.ListAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_accounts_with_options_async(
        self,
        request: clickhouse_20220101_models.ListAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.ListAccountsResponse:
        """
        @summary 查看实例账户详情列表
        
        @param request: ListAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccounts',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.ListAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_accounts(
        self,
        request: clickhouse_20220101_models.ListAccountsRequest,
    ) -> clickhouse_20220101_models.ListAccountsResponse:
        """
        @summary 查看实例账户详情列表
        
        @param request: ListAccountsRequest
        @return: ListAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_accounts_with_options(request, runtime)

    async def list_accounts_async(
        self,
        request: clickhouse_20220101_models.ListAccountsRequest,
    ) -> clickhouse_20220101_models.ListAccountsResponse:
        """
        @summary 查看实例账户详情列表
        
        @param request: ListAccountsRequest
        @return: ListAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_accounts_with_options_async(request, runtime)

    def list_clusters_with_options(
        self,
        request: clickhouse_20220101_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.ListClustersResponse:
        """
        @summary 查看实例详情列表
        
        @param request: ListClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbcluster_status):
            query['DBClusterStatus'] = request.dbcluster_status
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.ListClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_clusters_with_options_async(
        self,
        request: clickhouse_20220101_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.ListClustersResponse:
        """
        @summary 查看实例详情列表
        
        @param request: ListClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbcluster_status):
            query['DBClusterStatus'] = request.dbcluster_status
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.ListClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_clusters(
        self,
        request: clickhouse_20220101_models.ListClustersRequest,
    ) -> clickhouse_20220101_models.ListClustersResponse:
        """
        @summary 查看实例详情列表
        
        @param request: ListClustersRequest
        @return: ListClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_clusters_with_options(request, runtime)

    async def list_clusters_async(
        self,
        request: clickhouse_20220101_models.ListClustersRequest,
    ) -> clickhouse_20220101_models.ListClustersResponse:
        """
        @summary 查看实例详情列表
        
        @param request: ListClustersRequest
        @return: ListClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_clusters_with_options_async(request, runtime)

    def list_virtual_ware_house_configs_with_options(
        self,
        request: clickhouse_20220101_models.ListVirtualWareHouseConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.ListVirtualWareHouseConfigsResponse:
        """
        @summary 查看计算组参数配置列表
        
        @param request: ListVirtualWareHouseConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVirtualWareHouseConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVirtualWareHouseConfigs',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.ListVirtualWareHouseConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_virtual_ware_house_configs_with_options_async(
        self,
        request: clickhouse_20220101_models.ListVirtualWareHouseConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.ListVirtualWareHouseConfigsResponse:
        """
        @summary 查看计算组参数配置列表
        
        @param request: ListVirtualWareHouseConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVirtualWareHouseConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVirtualWareHouseConfigs',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.ListVirtualWareHouseConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_virtual_ware_house_configs(
        self,
        request: clickhouse_20220101_models.ListVirtualWareHouseConfigsRequest,
    ) -> clickhouse_20220101_models.ListVirtualWareHouseConfigsResponse:
        """
        @summary 查看计算组参数配置列表
        
        @param request: ListVirtualWareHouseConfigsRequest
        @return: ListVirtualWareHouseConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_virtual_ware_house_configs_with_options(request, runtime)

    async def list_virtual_ware_house_configs_async(
        self,
        request: clickhouse_20220101_models.ListVirtualWareHouseConfigsRequest,
    ) -> clickhouse_20220101_models.ListVirtualWareHouseConfigsResponse:
        """
        @summary 查看计算组参数配置列表
        
        @param request: ListVirtualWareHouseConfigsRequest
        @return: ListVirtualWareHouseConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_virtual_ware_house_configs_with_options_async(request, runtime)

    def list_virtual_ware_houses_with_options(
        self,
        request: clickhouse_20220101_models.ListVirtualWareHousesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.ListVirtualWareHousesResponse:
        """
        @summary 查看计算组详情列表
        
        @param request: ListVirtualWareHousesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVirtualWareHousesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVirtualWareHouses',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.ListVirtualWareHousesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_virtual_ware_houses_with_options_async(
        self,
        request: clickhouse_20220101_models.ListVirtualWareHousesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.ListVirtualWareHousesResponse:
        """
        @summary 查看计算组详情列表
        
        @param request: ListVirtualWareHousesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVirtualWareHousesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVirtualWareHouses',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.ListVirtualWareHousesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_virtual_ware_houses(
        self,
        request: clickhouse_20220101_models.ListVirtualWareHousesRequest,
    ) -> clickhouse_20220101_models.ListVirtualWareHousesResponse:
        """
        @summary 查看计算组详情列表
        
        @param request: ListVirtualWareHousesRequest
        @return: ListVirtualWareHousesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_virtual_ware_houses_with_options(request, runtime)

    async def list_virtual_ware_houses_async(
        self,
        request: clickhouse_20220101_models.ListVirtualWareHousesRequest,
    ) -> clickhouse_20220101_models.ListVirtualWareHousesResponse:
        """
        @summary 查看计算组详情列表
        
        @param request: ListVirtualWareHousesRequest
        @return: ListVirtualWareHousesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_virtual_ware_houses_with_options_async(request, runtime)

    def modify_account_description_with_options(
        self,
        request: clickhouse_20220101_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.ModifyAccountDescriptionResponse:
        """
        @summary 修改实例账户备注
        
        @param request: ModifyAccountDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.ModifyAccountDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_description_with_options_async(
        self,
        request: clickhouse_20220101_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.ModifyAccountDescriptionResponse:
        """
        @summary 修改实例账户备注
        
        @param request: ModifyAccountDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.ModifyAccountDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_description(
        self,
        request: clickhouse_20220101_models.ModifyAccountDescriptionRequest,
    ) -> clickhouse_20220101_models.ModifyAccountDescriptionResponse:
        """
        @summary 修改实例账户备注
        
        @param request: ModifyAccountDescriptionRequest
        @return: ModifyAccountDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    async def modify_account_description_async(
        self,
        request: clickhouse_20220101_models.ModifyAccountDescriptionRequest,
    ) -> clickhouse_20220101_models.ModifyAccountDescriptionResponse:
        """
        @summary 修改实例账户备注
        
        @param request: ModifyAccountDescriptionRequest
        @return: ModifyAccountDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_description_with_options_async(request, runtime)

    def modify_account_privilege_with_options(
        self,
        request: clickhouse_20220101_models.ModifyAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.ModifyAccountPrivilegeResponse:
        """
        @summary 修改实例账户权限级别
        
        @param request: ModifyAccountPrivilegeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountPrivilegeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.privilege_type):
            query['PrivilegeType'] = request.privilege_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountPrivilege',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.ModifyAccountPrivilegeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_privilege_with_options_async(
        self,
        request: clickhouse_20220101_models.ModifyAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.ModifyAccountPrivilegeResponse:
        """
        @summary 修改实例账户权限级别
        
        @param request: ModifyAccountPrivilegeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountPrivilegeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.privilege_type):
            query['PrivilegeType'] = request.privilege_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountPrivilege',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.ModifyAccountPrivilegeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_privilege(
        self,
        request: clickhouse_20220101_models.ModifyAccountPrivilegeRequest,
    ) -> clickhouse_20220101_models.ModifyAccountPrivilegeResponse:
        """
        @summary 修改实例账户权限级别
        
        @param request: ModifyAccountPrivilegeRequest
        @return: ModifyAccountPrivilegeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_account_privilege_with_options(request, runtime)

    async def modify_account_privilege_async(
        self,
        request: clickhouse_20220101_models.ModifyAccountPrivilegeRequest,
    ) -> clickhouse_20220101_models.ModifyAccountPrivilegeResponse:
        """
        @summary 修改实例账户权限级别
        
        @param request: ModifyAccountPrivilegeRequest
        @return: ModifyAccountPrivilegeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_privilege_with_options_async(request, runtime)

    def modify_cluster_description_with_options(
        self,
        request: clickhouse_20220101_models.ModifyClusterDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.ModifyClusterDescriptionResponse:
        """
        @summary 修改实例描述信息
        
        @param request: ModifyClusterDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClusterDescription',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.ModifyClusterDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_description_with_options_async(
        self,
        request: clickhouse_20220101_models.ModifyClusterDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.ModifyClusterDescriptionResponse:
        """
        @summary 修改实例描述信息
        
        @param request: ModifyClusterDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClusterDescription',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.ModifyClusterDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cluster_description(
        self,
        request: clickhouse_20220101_models.ModifyClusterDescriptionRequest,
    ) -> clickhouse_20220101_models.ModifyClusterDescriptionResponse:
        """
        @summary 修改实例描述信息
        
        @param request: ModifyClusterDescriptionRequest
        @return: ModifyClusterDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_description_with_options(request, runtime)

    async def modify_cluster_description_async(
        self,
        request: clickhouse_20220101_models.ModifyClusterDescriptionRequest,
    ) -> clickhouse_20220101_models.ModifyClusterDescriptionResponse:
        """
        @summary 修改实例描述信息
        
        @param request: ModifyClusterDescriptionRequest
        @return: ModifyClusterDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_cluster_description_with_options_async(request, runtime)

    def modify_virtual_ware_house_config_with_options(
        self,
        tmp_req: clickhouse_20220101_models.ModifyVirtualWareHouseConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.ModifyVirtualWareHouseConfigResponse:
        """
        @summary 修改计算组参数配置
        
        @param tmp_req: ModifyVirtualWareHouseConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyVirtualWareHouseConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = clickhouse_20220101_models.ModifyVirtualWareHouseConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config_changes):
            request.config_changes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config_changes, 'ConfigChanges', 'json')
        query = {}
        if not UtilClient.is_unset(request.config_changes_shrink):
            query['ConfigChanges'] = request.config_changes_shrink
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVirtualWareHouseConfig',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.ModifyVirtualWareHouseConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_virtual_ware_house_config_with_options_async(
        self,
        tmp_req: clickhouse_20220101_models.ModifyVirtualWareHouseConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.ModifyVirtualWareHouseConfigResponse:
        """
        @summary 修改计算组参数配置
        
        @param tmp_req: ModifyVirtualWareHouseConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyVirtualWareHouseConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = clickhouse_20220101_models.ModifyVirtualWareHouseConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config_changes):
            request.config_changes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config_changes, 'ConfigChanges', 'json')
        query = {}
        if not UtilClient.is_unset(request.config_changes_shrink):
            query['ConfigChanges'] = request.config_changes_shrink
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVirtualWareHouseConfig',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.ModifyVirtualWareHouseConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_virtual_ware_house_config(
        self,
        request: clickhouse_20220101_models.ModifyVirtualWareHouseConfigRequest,
    ) -> clickhouse_20220101_models.ModifyVirtualWareHouseConfigResponse:
        """
        @summary 修改计算组参数配置
        
        @param request: ModifyVirtualWareHouseConfigRequest
        @return: ModifyVirtualWareHouseConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_virtual_ware_house_config_with_options(request, runtime)

    async def modify_virtual_ware_house_config_async(
        self,
        request: clickhouse_20220101_models.ModifyVirtualWareHouseConfigRequest,
    ) -> clickhouse_20220101_models.ModifyVirtualWareHouseConfigResponse:
        """
        @summary 修改计算组参数配置
        
        @param request: ModifyVirtualWareHouseConfigRequest
        @return: ModifyVirtualWareHouseConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_virtual_ware_house_config_with_options_async(request, runtime)

    def modify_virtual_ware_house_description_with_options(
        self,
        request: clickhouse_20220101_models.ModifyVirtualWareHouseDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.ModifyVirtualWareHouseDescriptionResponse:
        """
        @summary 修改计算组描述信息
        
        @param request: ModifyVirtualWareHouseDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyVirtualWareHouseDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_description):
            query['VirtualWareHouseDescription'] = request.virtual_ware_house_description
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVirtualWareHouseDescription',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.ModifyVirtualWareHouseDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_virtual_ware_house_description_with_options_async(
        self,
        request: clickhouse_20220101_models.ModifyVirtualWareHouseDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.ModifyVirtualWareHouseDescriptionResponse:
        """
        @summary 修改计算组描述信息
        
        @param request: ModifyVirtualWareHouseDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyVirtualWareHouseDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_description):
            query['VirtualWareHouseDescription'] = request.virtual_ware_house_description
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVirtualWareHouseDescription',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.ModifyVirtualWareHouseDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_virtual_ware_house_description(
        self,
        request: clickhouse_20220101_models.ModifyVirtualWareHouseDescriptionRequest,
    ) -> clickhouse_20220101_models.ModifyVirtualWareHouseDescriptionResponse:
        """
        @summary 修改计算组描述信息
        
        @param request: ModifyVirtualWareHouseDescriptionRequest
        @return: ModifyVirtualWareHouseDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_virtual_ware_house_description_with_options(request, runtime)

    async def modify_virtual_ware_house_description_async(
        self,
        request: clickhouse_20220101_models.ModifyVirtualWareHouseDescriptionRequest,
    ) -> clickhouse_20220101_models.ModifyVirtualWareHouseDescriptionResponse:
        """
        @summary 修改计算组描述信息
        
        @param request: ModifyVirtualWareHouseDescriptionRequest
        @return: ModifyVirtualWareHouseDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_virtual_ware_house_description_with_options_async(request, runtime)

    def modify_virtual_ware_house_resource_with_options(
        self,
        request: clickhouse_20220101_models.ModifyVirtualWareHouseResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.ModifyVirtualWareHouseResourceResponse:
        """
        @summary 计算组变配
        
        @param request: ModifyVirtualWareHouseResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyVirtualWareHouseResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_cache_storage):
            query['VirtualWareHouseCacheStorage'] = request.virtual_ware_house_cache_storage
        if not UtilClient.is_unset(request.virtual_ware_house_class):
            query['VirtualWareHouseClass'] = request.virtual_ware_house_class
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVirtualWareHouseResource',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.ModifyVirtualWareHouseResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_virtual_ware_house_resource_with_options_async(
        self,
        request: clickhouse_20220101_models.ModifyVirtualWareHouseResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.ModifyVirtualWareHouseResourceResponse:
        """
        @summary 计算组变配
        
        @param request: ModifyVirtualWareHouseResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyVirtualWareHouseResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_cache_storage):
            query['VirtualWareHouseCacheStorage'] = request.virtual_ware_house_cache_storage
        if not UtilClient.is_unset(request.virtual_ware_house_class):
            query['VirtualWareHouseClass'] = request.virtual_ware_house_class
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVirtualWareHouseResource',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.ModifyVirtualWareHouseResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_virtual_ware_house_resource(
        self,
        request: clickhouse_20220101_models.ModifyVirtualWareHouseResourceRequest,
    ) -> clickhouse_20220101_models.ModifyVirtualWareHouseResourceResponse:
        """
        @summary 计算组变配
        
        @param request: ModifyVirtualWareHouseResourceRequest
        @return: ModifyVirtualWareHouseResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_virtual_ware_house_resource_with_options(request, runtime)

    async def modify_virtual_ware_house_resource_async(
        self,
        request: clickhouse_20220101_models.ModifyVirtualWareHouseResourceRequest,
    ) -> clickhouse_20220101_models.ModifyVirtualWareHouseResourceResponse:
        """
        @summary 计算组变配
        
        @param request: ModifyVirtualWareHouseResourceRequest
        @return: ModifyVirtualWareHouseResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_virtual_ware_house_resource_with_options_async(request, runtime)

    def patch_cluster_security_ipgroup_with_options(
        self,
        request: clickhouse_20220101_models.PatchClusterSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.PatchClusterSecurityIPGroupResponse:
        """
        @summary 实例IP白名单组添加IP
        
        @param request: PatchClusterSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PatchClusterSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_ips):
            query['SecurityIps'] = request.security_ips
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PatchClusterSecurityIPGroup',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.PatchClusterSecurityIPGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def patch_cluster_security_ipgroup_with_options_async(
        self,
        request: clickhouse_20220101_models.PatchClusterSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.PatchClusterSecurityIPGroupResponse:
        """
        @summary 实例IP白名单组添加IP
        
        @param request: PatchClusterSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PatchClusterSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_ips):
            query['SecurityIps'] = request.security_ips
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PatchClusterSecurityIPGroup',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.PatchClusterSecurityIPGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def patch_cluster_security_ipgroup(
        self,
        request: clickhouse_20220101_models.PatchClusterSecurityIPGroupRequest,
    ) -> clickhouse_20220101_models.PatchClusterSecurityIPGroupResponse:
        """
        @summary 实例IP白名单组添加IP
        
        @param request: PatchClusterSecurityIPGroupRequest
        @return: PatchClusterSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.patch_cluster_security_ipgroup_with_options(request, runtime)

    async def patch_cluster_security_ipgroup_async(
        self,
        request: clickhouse_20220101_models.PatchClusterSecurityIPGroupRequest,
    ) -> clickhouse_20220101_models.PatchClusterSecurityIPGroupResponse:
        """
        @summary 实例IP白名单组添加IP
        
        @param request: PatchClusterSecurityIPGroupRequest
        @return: PatchClusterSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.patch_cluster_security_ipgroup_with_options_async(request, runtime)

    def release_virtual_ware_house_public_connection_with_options(
        self,
        request: clickhouse_20220101_models.ReleaseVirtualWareHousePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.ReleaseVirtualWareHousePublicConnectionResponse:
        """
        @summary 释放计算组公网SLB
        
        @param request: ReleaseVirtualWareHousePublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseVirtualWareHousePublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseVirtualWareHousePublicConnection',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.ReleaseVirtualWareHousePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_virtual_ware_house_public_connection_with_options_async(
        self,
        request: clickhouse_20220101_models.ReleaseVirtualWareHousePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.ReleaseVirtualWareHousePublicConnectionResponse:
        """
        @summary 释放计算组公网SLB
        
        @param request: ReleaseVirtualWareHousePublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseVirtualWareHousePublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseVirtualWareHousePublicConnection',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.ReleaseVirtualWareHousePublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_virtual_ware_house_public_connection(
        self,
        request: clickhouse_20220101_models.ReleaseVirtualWareHousePublicConnectionRequest,
    ) -> clickhouse_20220101_models.ReleaseVirtualWareHousePublicConnectionResponse:
        """
        @summary 释放计算组公网SLB
        
        @param request: ReleaseVirtualWareHousePublicConnectionRequest
        @return: ReleaseVirtualWareHousePublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_virtual_ware_house_public_connection_with_options(request, runtime)

    async def release_virtual_ware_house_public_connection_async(
        self,
        request: clickhouse_20220101_models.ReleaseVirtualWareHousePublicConnectionRequest,
    ) -> clickhouse_20220101_models.ReleaseVirtualWareHousePublicConnectionResponse:
        """
        @summary 释放计算组公网SLB
        
        @param request: ReleaseVirtualWareHousePublicConnectionRequest
        @return: ReleaseVirtualWareHousePublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_virtual_ware_house_public_connection_with_options_async(request, runtime)

    def reset_account_password_with_options(
        self,
        request: clickhouse_20220101_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.ResetAccountPasswordResponse:
        """
        @summary 重置实例账户密码
        
        @param request: ResetAccountPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAccountPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_sha_256hex):
            query['PasswordSha256Hex'] = request.password_sha_256hex
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.ResetAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_account_password_with_options_async(
        self,
        request: clickhouse_20220101_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.ResetAccountPasswordResponse:
        """
        @summary 重置实例账户密码
        
        @param request: ResetAccountPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAccountPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_sha_256hex):
            query['PasswordSha256Hex'] = request.password_sha_256hex
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.ResetAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_account_password(
        self,
        request: clickhouse_20220101_models.ResetAccountPasswordRequest,
    ) -> clickhouse_20220101_models.ResetAccountPasswordResponse:
        """
        @summary 重置实例账户密码
        
        @param request: ResetAccountPasswordRequest
        @return: ResetAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    async def reset_account_password_async(
        self,
        request: clickhouse_20220101_models.ResetAccountPasswordRequest,
    ) -> clickhouse_20220101_models.ResetAccountPasswordResponse:
        """
        @summary 重置实例账户密码
        
        @param request: ResetAccountPasswordRequest
        @return: ResetAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_account_password_with_options_async(request, runtime)

    def restart_virtual_ware_house_with_options(
        self,
        request: clickhouse_20220101_models.RestartVirtualWareHouseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.RestartVirtualWareHouseResponse:
        """
        @summary 重启计算组
        
        @param request: RestartVirtualWareHouseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartVirtualWareHouseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartVirtualWareHouse',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.RestartVirtualWareHouseResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_virtual_ware_house_with_options_async(
        self,
        request: clickhouse_20220101_models.RestartVirtualWareHouseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.RestartVirtualWareHouseResponse:
        """
        @summary 重启计算组
        
        @param request: RestartVirtualWareHouseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartVirtualWareHouseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_ware_house_id):
            query['VirtualWareHouseId'] = request.virtual_ware_house_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartVirtualWareHouse',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.RestartVirtualWareHouseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_virtual_ware_house(
        self,
        request: clickhouse_20220101_models.RestartVirtualWareHouseRequest,
    ) -> clickhouse_20220101_models.RestartVirtualWareHouseResponse:
        """
        @summary 重启计算组
        
        @param request: RestartVirtualWareHouseRequest
        @return: RestartVirtualWareHouseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restart_virtual_ware_house_with_options(request, runtime)

    async def restart_virtual_ware_house_async(
        self,
        request: clickhouse_20220101_models.RestartVirtualWareHouseRequest,
    ) -> clickhouse_20220101_models.RestartVirtualWareHouseResponse:
        """
        @summary 重启计算组
        
        @param request: RestartVirtualWareHouseRequest
        @return: RestartVirtualWareHouseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restart_virtual_ware_house_with_options_async(request, runtime)

    def upgrade_cluster_with_options(
        self,
        request: clickhouse_20220101_models.UpgradeClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.UpgradeClusterResponse:
        """
        @summary 实例小版本升级(内核向前兼容)
        
        @param request: UpgradeClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeCluster',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.UpgradeClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_cluster_with_options_async(
        self,
        request: clickhouse_20220101_models.UpgradeClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.UpgradeClusterResponse:
        """
        @summary 实例小版本升级(内核向前兼容)
        
        @param request: UpgradeClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeCluster',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.UpgradeClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_cluster(
        self,
        request: clickhouse_20220101_models.UpgradeClusterRequest,
    ) -> clickhouse_20220101_models.UpgradeClusterResponse:
        """
        @summary 实例小版本升级(内核向前兼容)
        
        @param request: UpgradeClusterRequest
        @return: UpgradeClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_cluster_with_options(request, runtime)

    async def upgrade_cluster_async(
        self,
        request: clickhouse_20220101_models.UpgradeClusterRequest,
    ) -> clickhouse_20220101_models.UpgradeClusterResponse:
        """
        @summary 实例小版本升级(内核向前兼容)
        
        @param request: UpgradeClusterRequest
        @return: UpgradeClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_cluster_with_options_async(request, runtime)

    def upsert_cluster_security_ipgroup_with_options(
        self,
        request: clickhouse_20220101_models.UpsertClusterSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.UpsertClusterSecurityIPGroupResponse:
        """
        @summary 重置实例IP白名单组IP列表
        
        @param request: UpsertClusterSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpsertClusterSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_ips):
            query['SecurityIps'] = request.security_ips
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpsertClusterSecurityIPGroup',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.UpsertClusterSecurityIPGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def upsert_cluster_security_ipgroup_with_options_async(
        self,
        request: clickhouse_20220101_models.UpsertClusterSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20220101_models.UpsertClusterSecurityIPGroupResponse:
        """
        @summary 重置实例IP白名单组IP列表
        
        @param request: UpsertClusterSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpsertClusterSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_ips):
            query['SecurityIps'] = request.security_ips
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpsertClusterSecurityIPGroup',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20220101_models.UpsertClusterSecurityIPGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upsert_cluster_security_ipgroup(
        self,
        request: clickhouse_20220101_models.UpsertClusterSecurityIPGroupRequest,
    ) -> clickhouse_20220101_models.UpsertClusterSecurityIPGroupResponse:
        """
        @summary 重置实例IP白名单组IP列表
        
        @param request: UpsertClusterSecurityIPGroupRequest
        @return: UpsertClusterSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upsert_cluster_security_ipgroup_with_options(request, runtime)

    async def upsert_cluster_security_ipgroup_async(
        self,
        request: clickhouse_20220101_models.UpsertClusterSecurityIPGroupRequest,
    ) -> clickhouse_20220101_models.UpsertClusterSecurityIPGroupResponse:
        """
        @summary 重置实例IP白名单组IP列表
        
        @param request: UpsertClusterSecurityIPGroupRequest
        @return: UpsertClusterSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upsert_cluster_security_ipgroup_with_options_async(request, runtime)
