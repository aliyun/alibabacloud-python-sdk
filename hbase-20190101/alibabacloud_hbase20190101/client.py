# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_hbase20190101 import models as hbase_20190101_models
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
            'ap-southeast-1': 'hbase.aliyuncs.com',
            'cn-beijing': 'hbase.aliyuncs.com',
            'cn-beijing-finance-1': 'hbase.aliyuncs.com',
            'cn-beijing-finance-pop': 'hbase.aliyuncs.com',
            'cn-beijing-gov-1': 'hbase.aliyuncs.com',
            'cn-beijing-nu16-b01': 'hbase.aliyuncs.com',
            'cn-edge-1': 'hbase.aliyuncs.com',
            'cn-fujian': 'hbase.aliyuncs.com',
            'cn-haidian-cm12-c01': 'hbase.aliyuncs.com',
            'cn-hangzhou': 'hbase.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'hbase.aliyuncs.com',
            'cn-hangzhou-finance': 'hbase.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'hbase.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'hbase.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'hbase.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'hbase.aliyuncs.com',
            'cn-hangzhou-test-306': 'hbase.aliyuncs.com',
            'cn-hongkong': 'hbase.aliyuncs.com',
            'cn-hongkong-finance-pop': 'hbase.aliyuncs.com',
            'cn-north-2-gov-1': 'hbase.aliyuncs.com',
            'cn-qingdao': 'hbase.aliyuncs.com',
            'cn-qingdao-nebula': 'hbase.aliyuncs.com',
            'cn-shanghai': 'hbase.aliyuncs.com',
            'cn-shanghai-et15-b01': 'hbase.aliyuncs.com',
            'cn-shanghai-et2-b01': 'hbase.aliyuncs.com',
            'cn-shanghai-finance-1': 'hbase.aliyuncs.com',
            'cn-shanghai-inner': 'hbase.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'hbase.aliyuncs.com',
            'cn-shenzhen': 'hbase.aliyuncs.com',
            'cn-shenzhen-finance-1': 'hbase.aliyuncs.com',
            'cn-shenzhen-inner': 'hbase.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'hbase.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'hbase.aliyuncs.com',
            'cn-wuhan': 'hbase.aliyuncs.com',
            'cn-yushanfang': 'hbase.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'hbase.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'hbase.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'hbase.aliyuncs.com',
            'eu-west-1-oxs': 'hbase.ap-northeast-1.aliyuncs.com',
            'rus-west-1-pop': 'hbase.ap-northeast-1.aliyuncs.com',
            'us-east-1': 'hbase.aliyuncs.com',
            'us-west-1': 'hbase.aliyuncs.com'
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
        request: hbase_20190101_models.AddUserHdfsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.AddUserHdfsInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.ext_info):
            query['ExtInfo'] = request.ext_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserHdfsInfo',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.AddUserHdfsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_hdfs_info_with_options_async(
        self,
        request: hbase_20190101_models.AddUserHdfsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.AddUserHdfsInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.ext_info):
            query['ExtInfo'] = request.ext_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserHdfsInfo',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.AddUserHdfsInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user_hdfs_info(
        self,
        request: hbase_20190101_models.AddUserHdfsInfoRequest,
    ) -> hbase_20190101_models.AddUserHdfsInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_user_hdfs_info_with_options(request, runtime)

    async def add_user_hdfs_info_async(
        self,
        request: hbase_20190101_models.AddUserHdfsInfoRequest,
    ) -> hbase_20190101_models.AddUserHdfsInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_user_hdfs_info_with_options_async(request, runtime)

    def allocate_public_network_address_with_options(
        self,
        request: hbase_20190101_models.AllocatePublicNetworkAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.AllocatePublicNetworkAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocatePublicNetworkAddress',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.AllocatePublicNetworkAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_public_network_address_with_options_async(
        self,
        request: hbase_20190101_models.AllocatePublicNetworkAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.AllocatePublicNetworkAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocatePublicNetworkAddress',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.AllocatePublicNetworkAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_public_network_address(
        self,
        request: hbase_20190101_models.AllocatePublicNetworkAddressRequest,
    ) -> hbase_20190101_models.AllocatePublicNetworkAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_public_network_address_with_options(request, runtime)

    async def allocate_public_network_address_async(
        self,
        request: hbase_20190101_models.AllocatePublicNetworkAddressRequest,
    ) -> hbase_20190101_models.AllocatePublicNetworkAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_public_network_address_with_options_async(request, runtime)

    def check_components_version_with_options(
        self,
        request: hbase_20190101_models.CheckComponentsVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CheckComponentsVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.components):
            query['Components'] = request.components
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckComponentsVersion',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.CheckComponentsVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_components_version_with_options_async(
        self,
        request: hbase_20190101_models.CheckComponentsVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CheckComponentsVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.components):
            query['Components'] = request.components
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckComponentsVersion',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.CheckComponentsVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_components_version(
        self,
        request: hbase_20190101_models.CheckComponentsVersionRequest,
    ) -> hbase_20190101_models.CheckComponentsVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_components_version_with_options(request, runtime)

    async def check_components_version_async(
        self,
        request: hbase_20190101_models.CheckComponentsVersionRequest,
    ) -> hbase_20190101_models.CheckComponentsVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_components_version_with_options_async(request, runtime)

    def close_backup_with_options(
        self,
        request: hbase_20190101_models.CloseBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CloseBackupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseBackup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.CloseBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_backup_with_options_async(
        self,
        request: hbase_20190101_models.CloseBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CloseBackupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseBackup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.CloseBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_backup(
        self,
        request: hbase_20190101_models.CloseBackupRequest,
    ) -> hbase_20190101_models.CloseBackupResponse:
        runtime = util_models.RuntimeOptions()
        return self.close_backup_with_options(request, runtime)

    async def close_backup_async(
        self,
        request: hbase_20190101_models.CloseBackupRequest,
    ) -> hbase_20190101_models.CloseBackupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.close_backup_with_options_async(request, runtime)

    def convert_instance_with_options(
        self,
        request: hbase_20190101_models.ConvertInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ConvertInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConvertInstance',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ConvertInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def convert_instance_with_options_async(
        self,
        request: hbase_20190101_models.ConvertInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ConvertInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConvertInstance',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ConvertInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def convert_instance(
        self,
        request: hbase_20190101_models.ConvertInstanceRequest,
    ) -> hbase_20190101_models.ConvertInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.convert_instance_with_options(request, runtime)

    async def convert_instance_async(
        self,
        request: hbase_20190101_models.ConvertInstanceRequest,
    ) -> hbase_20190101_models.ConvertInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.convert_instance_with_options_async(request, runtime)

    def create_backup_plan_with_options(
        self,
        request: hbase_20190101_models.CreateBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CreateBackupPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBackupPlan',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.CreateBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_backup_plan_with_options_async(
        self,
        request: hbase_20190101_models.CreateBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CreateBackupPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBackupPlan',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.CreateBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_backup_plan(
        self,
        request: hbase_20190101_models.CreateBackupPlanRequest,
    ) -> hbase_20190101_models.CreateBackupPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_backup_plan_with_options(request, runtime)

    async def create_backup_plan_async(
        self,
        request: hbase_20190101_models.CreateBackupPlanRequest,
    ) -> hbase_20190101_models.CreateBackupPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_backup_plan_with_options_async(request, runtime)

    def create_cluster_with_options(
        self,
        request: hbase_20190101_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CreateClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.cold_storage_size):
            query['ColdStorageSize'] = request.cold_storage_size
        if not UtilClient.is_unset(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not UtilClient.is_unset(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.master_instance_type):
            query['MasterInstanceType'] = request.master_instance_type
        if not UtilClient.is_unset(request.node_count):
            query['NodeCount'] = request.node_count
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
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
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_with_options_async(
        self,
        request: hbase_20190101_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CreateClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.cold_storage_size):
            query['ColdStorageSize'] = request.cold_storage_size
        if not UtilClient.is_unset(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not UtilClient.is_unset(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.master_instance_type):
            query['MasterInstanceType'] = request.master_instance_type
        if not UtilClient.is_unset(request.node_count):
            query['NodeCount'] = request.node_count
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
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
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.CreateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster(
        self,
        request: hbase_20190101_models.CreateClusterRequest,
    ) -> hbase_20190101_models.CreateClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    async def create_cluster_async(
        self,
        request: hbase_20190101_models.CreateClusterRequest,
    ) -> hbase_20190101_models.CreateClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_with_options_async(request, runtime)

    def create_global_resource_with_options(
        self,
        request: hbase_20190101_models.CreateGlobalResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CreateGlobalResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGlobalResource',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.CreateGlobalResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_global_resource_with_options_async(
        self,
        request: hbase_20190101_models.CreateGlobalResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CreateGlobalResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGlobalResource',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.CreateGlobalResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_global_resource(
        self,
        request: hbase_20190101_models.CreateGlobalResourceRequest,
    ) -> hbase_20190101_models.CreateGlobalResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_global_resource_with_options(request, runtime)

    async def create_global_resource_async(
        self,
        request: hbase_20190101_models.CreateGlobalResourceRequest,
    ) -> hbase_20190101_models.CreateGlobalResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_global_resource_with_options_async(request, runtime)

    def create_hbase_slb_server_with_options(
        self,
        request: hbase_20190101_models.CreateHBaseSlbServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CreateHBaseSlbServerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.slb_server):
            query['SlbServer'] = request.slb_server
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHBaseSlbServer',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.CreateHBaseSlbServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_hbase_slb_server_with_options_async(
        self,
        request: hbase_20190101_models.CreateHBaseSlbServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CreateHBaseSlbServerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.slb_server):
            query['SlbServer'] = request.slb_server
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHBaseSlbServer',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.CreateHBaseSlbServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_hbase_slb_server(
        self,
        request: hbase_20190101_models.CreateHBaseSlbServerRequest,
    ) -> hbase_20190101_models.CreateHBaseSlbServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_hbase_slb_server_with_options(request, runtime)

    async def create_hbase_slb_server_async(
        self,
        request: hbase_20190101_models.CreateHBaseSlbServerRequest,
    ) -> hbase_20190101_models.CreateHBaseSlbServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_hbase_slb_server_with_options_async(request, runtime)

    def create_hbase_ha_slb_with_options(
        self,
        request: hbase_20190101_models.CreateHbaseHaSlbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CreateHbaseHaSlbResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bds_id):
            query['BdsId'] = request.bds_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.ha_id):
            query['HaId'] = request.ha_id
        if not UtilClient.is_unset(request.ha_types):
            query['HaTypes'] = request.ha_types
        if not UtilClient.is_unset(request.hbase_type):
            query['HbaseType'] = request.hbase_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHbaseHaSlb',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.CreateHbaseHaSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_hbase_ha_slb_with_options_async(
        self,
        request: hbase_20190101_models.CreateHbaseHaSlbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CreateHbaseHaSlbResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bds_id):
            query['BdsId'] = request.bds_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.ha_id):
            query['HaId'] = request.ha_id
        if not UtilClient.is_unset(request.ha_types):
            query['HaTypes'] = request.ha_types
        if not UtilClient.is_unset(request.hbase_type):
            query['HbaseType'] = request.hbase_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHbaseHaSlb',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.CreateHbaseHaSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_hbase_ha_slb(
        self,
        request: hbase_20190101_models.CreateHbaseHaSlbRequest,
    ) -> hbase_20190101_models.CreateHbaseHaSlbResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_hbase_ha_slb_with_options(request, runtime)

    async def create_hbase_ha_slb_async(
        self,
        request: hbase_20190101_models.CreateHbaseHaSlbRequest,
    ) -> hbase_20190101_models.CreateHbaseHaSlbResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_hbase_ha_slb_with_options_async(request, runtime)

    def create_multi_zone_cluster_with_options(
        self,
        request: hbase_20190101_models.CreateMultiZoneClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CreateMultiZoneClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.arbiter_vswitch_id):
            query['ArbiterVSwitchId'] = request.arbiter_vswitch_id
        if not UtilClient.is_unset(request.arbiter_zone_id):
            query['ArbiterZoneId'] = request.arbiter_zone_id
        if not UtilClient.is_unset(request.arch_version):
            query['ArchVersion'] = request.arch_version
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.core_disk_size):
            query['CoreDiskSize'] = request.core_disk_size
        if not UtilClient.is_unset(request.core_disk_type):
            query['CoreDiskType'] = request.core_disk_type
        if not UtilClient.is_unset(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not UtilClient.is_unset(request.core_node_count):
            query['CoreNodeCount'] = request.core_node_count
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.log_disk_size):
            query['LogDiskSize'] = request.log_disk_size
        if not UtilClient.is_unset(request.log_disk_type):
            query['LogDiskType'] = request.log_disk_type
        if not UtilClient.is_unset(request.log_instance_type):
            query['LogInstanceType'] = request.log_instance_type
        if not UtilClient.is_unset(request.log_node_count):
            query['LogNodeCount'] = request.log_node_count
        if not UtilClient.is_unset(request.master_instance_type):
            query['MasterInstanceType'] = request.master_instance_type
        if not UtilClient.is_unset(request.multi_zone_combination):
            query['MultiZoneCombination'] = request.multi_zone_combination
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.primary_vswitch_id):
            query['PrimaryVSwitchId'] = request.primary_vswitch_id
        if not UtilClient.is_unset(request.primary_zone_id):
            query['PrimaryZoneId'] = request.primary_zone_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not UtilClient.is_unset(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        if not UtilClient.is_unset(request.standby_zone_id):
            query['StandbyZoneId'] = request.standby_zone_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMultiZoneCluster',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.CreateMultiZoneClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_multi_zone_cluster_with_options_async(
        self,
        request: hbase_20190101_models.CreateMultiZoneClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CreateMultiZoneClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.arbiter_vswitch_id):
            query['ArbiterVSwitchId'] = request.arbiter_vswitch_id
        if not UtilClient.is_unset(request.arbiter_zone_id):
            query['ArbiterZoneId'] = request.arbiter_zone_id
        if not UtilClient.is_unset(request.arch_version):
            query['ArchVersion'] = request.arch_version
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.core_disk_size):
            query['CoreDiskSize'] = request.core_disk_size
        if not UtilClient.is_unset(request.core_disk_type):
            query['CoreDiskType'] = request.core_disk_type
        if not UtilClient.is_unset(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not UtilClient.is_unset(request.core_node_count):
            query['CoreNodeCount'] = request.core_node_count
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.log_disk_size):
            query['LogDiskSize'] = request.log_disk_size
        if not UtilClient.is_unset(request.log_disk_type):
            query['LogDiskType'] = request.log_disk_type
        if not UtilClient.is_unset(request.log_instance_type):
            query['LogInstanceType'] = request.log_instance_type
        if not UtilClient.is_unset(request.log_node_count):
            query['LogNodeCount'] = request.log_node_count
        if not UtilClient.is_unset(request.master_instance_type):
            query['MasterInstanceType'] = request.master_instance_type
        if not UtilClient.is_unset(request.multi_zone_combination):
            query['MultiZoneCombination'] = request.multi_zone_combination
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.primary_vswitch_id):
            query['PrimaryVSwitchId'] = request.primary_vswitch_id
        if not UtilClient.is_unset(request.primary_zone_id):
            query['PrimaryZoneId'] = request.primary_zone_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not UtilClient.is_unset(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        if not UtilClient.is_unset(request.standby_zone_id):
            query['StandbyZoneId'] = request.standby_zone_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMultiZoneCluster',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.CreateMultiZoneClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_multi_zone_cluster(
        self,
        request: hbase_20190101_models.CreateMultiZoneClusterRequest,
    ) -> hbase_20190101_models.CreateMultiZoneClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_multi_zone_cluster_with_options(request, runtime)

    async def create_multi_zone_cluster_async(
        self,
        request: hbase_20190101_models.CreateMultiZoneClusterRequest,
    ) -> hbase_20190101_models.CreateMultiZoneClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_multi_zone_cluster_with_options_async(request, runtime)

    def create_restore_plan_with_options(
        self,
        request: hbase_20190101_models.CreateRestorePlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CreateRestorePlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.restore_all_table):
            query['RestoreAllTable'] = request.restore_all_table
        if not UtilClient.is_unset(request.restore_by_copy):
            query['RestoreByCopy'] = request.restore_by_copy
        if not UtilClient.is_unset(request.restore_to_date):
            query['RestoreToDate'] = request.restore_to_date
        if not UtilClient.is_unset(request.tables):
            query['Tables'] = request.tables
        if not UtilClient.is_unset(request.target_cluster_id):
            query['TargetClusterId'] = request.target_cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRestorePlan',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.CreateRestorePlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_restore_plan_with_options_async(
        self,
        request: hbase_20190101_models.CreateRestorePlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CreateRestorePlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.restore_all_table):
            query['RestoreAllTable'] = request.restore_all_table
        if not UtilClient.is_unset(request.restore_by_copy):
            query['RestoreByCopy'] = request.restore_by_copy
        if not UtilClient.is_unset(request.restore_to_date):
            query['RestoreToDate'] = request.restore_to_date
        if not UtilClient.is_unset(request.tables):
            query['Tables'] = request.tables
        if not UtilClient.is_unset(request.target_cluster_id):
            query['TargetClusterId'] = request.target_cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRestorePlan',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.CreateRestorePlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_restore_plan(
        self,
        request: hbase_20190101_models.CreateRestorePlanRequest,
    ) -> hbase_20190101_models.CreateRestorePlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_restore_plan_with_options(request, runtime)

    async def create_restore_plan_async(
        self,
        request: hbase_20190101_models.CreateRestorePlanRequest,
    ) -> hbase_20190101_models.CreateRestorePlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_restore_plan_with_options_async(request, runtime)

    def create_serverless_cluster_with_options(
        self,
        request: hbase_20190101_models.CreateServerlessClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CreateServerlessClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.serverless_capability):
            query['ServerlessCapability'] = request.serverless_capability
        if not UtilClient.is_unset(request.serverless_spec):
            query['ServerlessSpec'] = request.serverless_spec
        if not UtilClient.is_unset(request.serverless_storage):
            query['ServerlessStorage'] = request.serverless_storage
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
            action='CreateServerlessCluster',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.CreateServerlessClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_serverless_cluster_with_options_async(
        self,
        request: hbase_20190101_models.CreateServerlessClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CreateServerlessClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.serverless_capability):
            query['ServerlessCapability'] = request.serverless_capability
        if not UtilClient.is_unset(request.serverless_spec):
            query['ServerlessSpec'] = request.serverless_spec
        if not UtilClient.is_unset(request.serverless_storage):
            query['ServerlessStorage'] = request.serverless_storage
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
            action='CreateServerlessCluster',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.CreateServerlessClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_serverless_cluster(
        self,
        request: hbase_20190101_models.CreateServerlessClusterRequest,
    ) -> hbase_20190101_models.CreateServerlessClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_serverless_cluster_with_options(request, runtime)

    async def create_serverless_cluster_async(
        self,
        request: hbase_20190101_models.CreateServerlessClusterRequest,
    ) -> hbase_20190101_models.CreateServerlessClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_serverless_cluster_with_options_async(request, runtime)

    def delete_global_resource_with_options(
        self,
        request: hbase_20190101_models.DeleteGlobalResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DeleteGlobalResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGlobalResource',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DeleteGlobalResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_global_resource_with_options_async(
        self,
        request: hbase_20190101_models.DeleteGlobalResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DeleteGlobalResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGlobalResource',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DeleteGlobalResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_global_resource(
        self,
        request: hbase_20190101_models.DeleteGlobalResourceRequest,
    ) -> hbase_20190101_models.DeleteGlobalResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_global_resource_with_options(request, runtime)

    async def delete_global_resource_async(
        self,
        request: hbase_20190101_models.DeleteGlobalResourceRequest,
    ) -> hbase_20190101_models.DeleteGlobalResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_global_resource_with_options_async(request, runtime)

    def delete_hbase_ha_dbwith_options(
        self,
        request: hbase_20190101_models.DeleteHBaseHaDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DeleteHBaseHaDBResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bds_id):
            query['BdsId'] = request.bds_id
        if not UtilClient.is_unset(request.ha_id):
            query['HaId'] = request.ha_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHBaseHaDB',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DeleteHBaseHaDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hbase_ha_dbwith_options_async(
        self,
        request: hbase_20190101_models.DeleteHBaseHaDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DeleteHBaseHaDBResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bds_id):
            query['BdsId'] = request.bds_id
        if not UtilClient.is_unset(request.ha_id):
            query['HaId'] = request.ha_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHBaseHaDB',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DeleteHBaseHaDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hbase_ha_db(
        self,
        request: hbase_20190101_models.DeleteHBaseHaDBRequest,
    ) -> hbase_20190101_models.DeleteHBaseHaDBResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_hbase_ha_dbwith_options(request, runtime)

    async def delete_hbase_ha_db_async(
        self,
        request: hbase_20190101_models.DeleteHBaseHaDBRequest,
    ) -> hbase_20190101_models.DeleteHBaseHaDBResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_hbase_ha_dbwith_options_async(request, runtime)

    def delete_hbase_slb_server_with_options(
        self,
        request: hbase_20190101_models.DeleteHBaseSlbServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DeleteHBaseSlbServerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.slb_server):
            query['SlbServer'] = request.slb_server
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHBaseSlbServer',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DeleteHBaseSlbServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hbase_slb_server_with_options_async(
        self,
        request: hbase_20190101_models.DeleteHBaseSlbServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DeleteHBaseSlbServerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.slb_server):
            query['SlbServer'] = request.slb_server
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHBaseSlbServer',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DeleteHBaseSlbServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hbase_slb_server(
        self,
        request: hbase_20190101_models.DeleteHBaseSlbServerRequest,
    ) -> hbase_20190101_models.DeleteHBaseSlbServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_hbase_slb_server_with_options(request, runtime)

    async def delete_hbase_slb_server_async(
        self,
        request: hbase_20190101_models.DeleteHBaseSlbServerRequest,
    ) -> hbase_20190101_models.DeleteHBaseSlbServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_hbase_slb_server_with_options_async(request, runtime)

    def delete_hbase_ha_slb_with_options(
        self,
        request: hbase_20190101_models.DeleteHbaseHaSlbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DeleteHbaseHaSlbResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bds_id):
            query['BdsId'] = request.bds_id
        if not UtilClient.is_unset(request.ha_id):
            query['HaId'] = request.ha_id
        if not UtilClient.is_unset(request.ha_types):
            query['HaTypes'] = request.ha_types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHbaseHaSlb',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DeleteHbaseHaSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hbase_ha_slb_with_options_async(
        self,
        request: hbase_20190101_models.DeleteHbaseHaSlbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DeleteHbaseHaSlbResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bds_id):
            query['BdsId'] = request.bds_id
        if not UtilClient.is_unset(request.ha_id):
            query['HaId'] = request.ha_id
        if not UtilClient.is_unset(request.ha_types):
            query['HaTypes'] = request.ha_types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHbaseHaSlb',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DeleteHbaseHaSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hbase_ha_slb(
        self,
        request: hbase_20190101_models.DeleteHbaseHaSlbRequest,
    ) -> hbase_20190101_models.DeleteHbaseHaSlbResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_hbase_ha_slb_with_options(request, runtime)

    async def delete_hbase_ha_slb_async(
        self,
        request: hbase_20190101_models.DeleteHbaseHaSlbRequest,
    ) -> hbase_20190101_models.DeleteHbaseHaSlbResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_hbase_ha_slb_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: hbase_20190101_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.immediate_delete_flag):
            query['ImmediateDeleteFlag'] = request.immediate_delete_flag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: hbase_20190101_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.immediate_delete_flag):
            query['ImmediateDeleteFlag'] = request.immediate_delete_flag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        request: hbase_20190101_models.DeleteInstanceRequest,
    ) -> hbase_20190101_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: hbase_20190101_models.DeleteInstanceRequest,
    ) -> hbase_20190101_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_multi_zone_cluster_with_options(
        self,
        request: hbase_20190101_models.DeleteMultiZoneClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DeleteMultiZoneClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.immediate_delete_flag):
            query['ImmediateDeleteFlag'] = request.immediate_delete_flag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMultiZoneCluster',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DeleteMultiZoneClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_multi_zone_cluster_with_options_async(
        self,
        request: hbase_20190101_models.DeleteMultiZoneClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DeleteMultiZoneClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.immediate_delete_flag):
            query['ImmediateDeleteFlag'] = request.immediate_delete_flag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMultiZoneCluster',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DeleteMultiZoneClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_multi_zone_cluster(
        self,
        request: hbase_20190101_models.DeleteMultiZoneClusterRequest,
    ) -> hbase_20190101_models.DeleteMultiZoneClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_multi_zone_cluster_with_options(request, runtime)

    async def delete_multi_zone_cluster_async(
        self,
        request: hbase_20190101_models.DeleteMultiZoneClusterRequest,
    ) -> hbase_20190101_models.DeleteMultiZoneClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_multi_zone_cluster_with_options_async(request, runtime)

    def delete_serverless_cluster_with_options(
        self,
        request: hbase_20190101_models.DeleteServerlessClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DeleteServerlessClusterResponse:
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
            action='DeleteServerlessCluster',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DeleteServerlessClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_serverless_cluster_with_options_async(
        self,
        request: hbase_20190101_models.DeleteServerlessClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DeleteServerlessClusterResponse:
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
            action='DeleteServerlessCluster',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DeleteServerlessClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_serverless_cluster(
        self,
        request: hbase_20190101_models.DeleteServerlessClusterRequest,
    ) -> hbase_20190101_models.DeleteServerlessClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_serverless_cluster_with_options(request, runtime)

    async def delete_serverless_cluster_async(
        self,
        request: hbase_20190101_models.DeleteServerlessClusterRequest,
    ) -> hbase_20190101_models.DeleteServerlessClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_serverless_cluster_with_options_async(request, runtime)

    def delete_user_hdfs_info_with_options(
        self,
        request: hbase_20190101_models.DeleteUserHdfsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DeleteUserHdfsInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.name_service):
            query['NameService'] = request.name_service
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserHdfsInfo',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DeleteUserHdfsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_hdfs_info_with_options_async(
        self,
        request: hbase_20190101_models.DeleteUserHdfsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DeleteUserHdfsInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.name_service):
            query['NameService'] = request.name_service
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserHdfsInfo',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DeleteUserHdfsInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_hdfs_info(
        self,
        request: hbase_20190101_models.DeleteUserHdfsInfoRequest,
    ) -> hbase_20190101_models.DeleteUserHdfsInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_hdfs_info_with_options(request, runtime)

    async def delete_user_hdfs_info_async(
        self,
        request: hbase_20190101_models.DeleteUserHdfsInfoRequest,
    ) -> hbase_20190101_models.DeleteUserHdfsInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_hdfs_info_with_options_async(request, runtime)

    def describe_available_resource_with_options(
        self,
        request: hbase_20190101_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeAvailableResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableResource',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeAvailableResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_resource_with_options_async(
        self,
        request: hbase_20190101_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeAvailableResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableResource',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeAvailableResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_resource(
        self,
        request: hbase_20190101_models.DescribeAvailableResourceRequest,
    ) -> hbase_20190101_models.DescribeAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    async def describe_available_resource_async(
        self,
        request: hbase_20190101_models.DescribeAvailableResourceRequest,
    ) -> hbase_20190101_models.DescribeAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_resource_with_options_async(request, runtime)

    def describe_backup_plan_config_with_options(
        self,
        request: hbase_20190101_models.DescribeBackupPlanConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeBackupPlanConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPlanConfig',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeBackupPlanConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_plan_config_with_options_async(
        self,
        request: hbase_20190101_models.DescribeBackupPlanConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeBackupPlanConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPlanConfig',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeBackupPlanConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_plan_config(
        self,
        request: hbase_20190101_models.DescribeBackupPlanConfigRequest,
    ) -> hbase_20190101_models.DescribeBackupPlanConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_plan_config_with_options(request, runtime)

    async def describe_backup_plan_config_async(
        self,
        request: hbase_20190101_models.DescribeBackupPlanConfigRequest,
    ) -> hbase_20190101_models.DescribeBackupPlanConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_plan_config_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: hbase_20190101_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_policy_with_options_async(
        self,
        request: hbase_20190101_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_policy(
        self,
        request: hbase_20190101_models.DescribeBackupPolicyRequest,
    ) -> hbase_20190101_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: hbase_20190101_models.DescribeBackupPolicyRequest,
    ) -> hbase_20190101_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_backup_status_with_options(
        self,
        request: hbase_20190101_models.DescribeBackupStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeBackupStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupStatus',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeBackupStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_status_with_options_async(
        self,
        request: hbase_20190101_models.DescribeBackupStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeBackupStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupStatus',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeBackupStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_status(
        self,
        request: hbase_20190101_models.DescribeBackupStatusRequest,
    ) -> hbase_20190101_models.DescribeBackupStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_status_with_options(request, runtime)

    async def describe_backup_status_async(
        self,
        request: hbase_20190101_models.DescribeBackupStatusRequest,
    ) -> hbase_20190101_models.DescribeBackupStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_status_with_options_async(request, runtime)

    def describe_backup_summary_with_options(
        self,
        request: hbase_20190101_models.DescribeBackupSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeBackupSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupSummary',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeBackupSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_summary_with_options_async(
        self,
        request: hbase_20190101_models.DescribeBackupSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeBackupSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupSummary',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeBackupSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_summary(
        self,
        request: hbase_20190101_models.DescribeBackupSummaryRequest,
    ) -> hbase_20190101_models.DescribeBackupSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_summary_with_options(request, runtime)

    async def describe_backup_summary_async(
        self,
        request: hbase_20190101_models.DescribeBackupSummaryRequest,
    ) -> hbase_20190101_models.DescribeBackupSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_summary_with_options_async(request, runtime)

    def describe_backup_tables_with_options(
        self,
        request: hbase_20190101_models.DescribeBackupTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeBackupTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_record_id):
            query['BackupRecordId'] = request.backup_record_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupTables',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeBackupTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_tables_with_options_async(
        self,
        request: hbase_20190101_models.DescribeBackupTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeBackupTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_record_id):
            query['BackupRecordId'] = request.backup_record_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupTables',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeBackupTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_tables(
        self,
        request: hbase_20190101_models.DescribeBackupTablesRequest,
    ) -> hbase_20190101_models.DescribeBackupTablesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_tables_with_options(request, runtime)

    async def describe_backup_tables_async(
        self,
        request: hbase_20190101_models.DescribeBackupTablesRequest,
    ) -> hbase_20190101_models.DescribeBackupTablesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_tables_with_options_async(request, runtime)

    def describe_backups_with_options(
        self,
        request: hbase_20190101_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeBackupsResponse:
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
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.start_time_utc):
            query['StartTimeUTC'] = request.start_time_utc
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackups',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backups_with_options_async(
        self,
        request: hbase_20190101_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeBackupsResponse:
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
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.start_time_utc):
            query['StartTimeUTC'] = request.start_time_utc
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackups',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeBackupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backups(
        self,
        request: hbase_20190101_models.DescribeBackupsRequest,
    ) -> hbase_20190101_models.DescribeBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    async def describe_backups_async(
        self,
        request: hbase_20190101_models.DescribeBackupsRequest,
    ) -> hbase_20190101_models.DescribeBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backups_with_options_async(request, runtime)

    def describe_cluster_connection_with_options(
        self,
        request: hbase_20190101_models.DescribeClusterConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeClusterConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterConnection',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeClusterConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_connection_with_options_async(
        self,
        request: hbase_20190101_models.DescribeClusterConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeClusterConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterConnection',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeClusterConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_connection(
        self,
        request: hbase_20190101_models.DescribeClusterConnectionRequest,
    ) -> hbase_20190101_models.DescribeClusterConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_connection_with_options(request, runtime)

    async def describe_cluster_connection_async(
        self,
        request: hbase_20190101_models.DescribeClusterConnectionRequest,
    ) -> hbase_20190101_models.DescribeClusterConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_connection_with_options_async(request, runtime)

    def describe_cold_storage_with_options(
        self,
        request: hbase_20190101_models.DescribeColdStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeColdStorageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeColdStorage',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeColdStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cold_storage_with_options_async(
        self,
        request: hbase_20190101_models.DescribeColdStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeColdStorageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeColdStorage',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeColdStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cold_storage(
        self,
        request: hbase_20190101_models.DescribeColdStorageRequest,
    ) -> hbase_20190101_models.DescribeColdStorageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cold_storage_with_options(request, runtime)

    async def describe_cold_storage_async(
        self,
        request: hbase_20190101_models.DescribeColdStorageRequest,
    ) -> hbase_20190101_models.DescribeColdStorageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cold_storage_with_options_async(request, runtime)

    def describe_dbinstance_usage_with_options(
        self,
        request: hbase_20190101_models.DescribeDBInstanceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeDBInstanceUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceUsage',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeDBInstanceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_usage_with_options_async(
        self,
        request: hbase_20190101_models.DescribeDBInstanceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeDBInstanceUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceUsage',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeDBInstanceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_usage(
        self,
        request: hbase_20190101_models.DescribeDBInstanceUsageRequest,
    ) -> hbase_20190101_models.DescribeDBInstanceUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_usage_with_options(request, runtime)

    async def describe_dbinstance_usage_async(
        self,
        request: hbase_20190101_models.DescribeDBInstanceUsageRequest,
    ) -> hbase_20190101_models.DescribeDBInstanceUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_usage_with_options_async(request, runtime)

    def describe_deleted_instances_with_options(
        self,
        request: hbase_20190101_models.DescribeDeletedInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeDeletedInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
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
            action='DescribeDeletedInstances',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeDeletedInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_deleted_instances_with_options_async(
        self,
        request: hbase_20190101_models.DescribeDeletedInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeDeletedInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
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
            action='DescribeDeletedInstances',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeDeletedInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_deleted_instances(
        self,
        request: hbase_20190101_models.DescribeDeletedInstancesRequest,
    ) -> hbase_20190101_models.DescribeDeletedInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_deleted_instances_with_options(request, runtime)

    async def describe_deleted_instances_async(
        self,
        request: hbase_20190101_models.DescribeDeletedInstancesRequest,
    ) -> hbase_20190101_models.DescribeDeletedInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_deleted_instances_with_options_async(request, runtime)

    def describe_disk_warning_line_with_options(
        self,
        request: hbase_20190101_models.DescribeDiskWarningLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeDiskWarningLineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiskWarningLine',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeDiskWarningLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_disk_warning_line_with_options_async(
        self,
        request: hbase_20190101_models.DescribeDiskWarningLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeDiskWarningLineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiskWarningLine',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeDiskWarningLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_disk_warning_line(
        self,
        request: hbase_20190101_models.DescribeDiskWarningLineRequest,
    ) -> hbase_20190101_models.DescribeDiskWarningLineResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_disk_warning_line_with_options(request, runtime)

    async def describe_disk_warning_line_async(
        self,
        request: hbase_20190101_models.DescribeDiskWarningLineRequest,
    ) -> hbase_20190101_models.DescribeDiskWarningLineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_disk_warning_line_with_options_async(request, runtime)

    def describe_endpoints_with_options(
        self,
        request: hbase_20190101_models.DescribeEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeEndpointsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEndpoints',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_endpoints_with_options_async(
        self,
        request: hbase_20190101_models.DescribeEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeEndpointsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEndpoints',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_endpoints(
        self,
        request: hbase_20190101_models.DescribeEndpointsRequest,
    ) -> hbase_20190101_models.DescribeEndpointsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_endpoints_with_options(request, runtime)

    async def describe_endpoints_async(
        self,
        request: hbase_20190101_models.DescribeEndpointsRequest,
    ) -> hbase_20190101_models.DescribeEndpointsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_endpoints_with_options_async(request, runtime)

    def describe_instance_with_options(
        self,
        request: hbase_20190101_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_with_options_async(
        self,
        request: hbase_20190101_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance(
        self,
        request: hbase_20190101_models.DescribeInstanceRequest,
    ) -> hbase_20190101_models.DescribeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_with_options(request, runtime)

    async def describe_instance_async(
        self,
        request: hbase_20190101_models.DescribeInstanceRequest,
    ) -> hbase_20190101_models.DescribeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_with_options_async(request, runtime)

    def describe_instance_type_with_options(
        self,
        request: hbase_20190101_models.DescribeInstanceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeInstanceTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceType',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeInstanceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_type_with_options_async(
        self,
        request: hbase_20190101_models.DescribeInstanceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeInstanceTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceType',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeInstanceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_type(
        self,
        request: hbase_20190101_models.DescribeInstanceTypeRequest,
    ) -> hbase_20190101_models.DescribeInstanceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_type_with_options(request, runtime)

    async def describe_instance_type_async(
        self,
        request: hbase_20190101_models.DescribeInstanceTypeRequest,
    ) -> hbase_20190101_models.DescribeInstanceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_type_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: hbase_20190101_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.db_type):
            query['DbType'] = request.db_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: hbase_20190101_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.db_type):
            query['DbType'] = request.db_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instances(
        self,
        request: hbase_20190101_models.DescribeInstancesRequest,
    ) -> hbase_20190101_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: hbase_20190101_models.DescribeInstancesRequest,
    ) -> hbase_20190101_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_ip_whitelist_with_options(
        self,
        request: hbase_20190101_models.DescribeIpWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeIpWhitelistResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIpWhitelist',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeIpWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ip_whitelist_with_options_async(
        self,
        request: hbase_20190101_models.DescribeIpWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeIpWhitelistResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIpWhitelist',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeIpWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ip_whitelist(
        self,
        request: hbase_20190101_models.DescribeIpWhitelistRequest,
    ) -> hbase_20190101_models.DescribeIpWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_whitelist_with_options(request, runtime)

    async def describe_ip_whitelist_async(
        self,
        request: hbase_20190101_models.DescribeIpWhitelistRequest,
    ) -> hbase_20190101_models.DescribeIpWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ip_whitelist_with_options_async(request, runtime)

    def describe_multi_zone_available_regions_with_options(
        self,
        request: hbase_20190101_models.DescribeMultiZoneAvailableRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeMultiZoneAvailableRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMultiZoneAvailableRegions',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeMultiZoneAvailableRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_multi_zone_available_regions_with_options_async(
        self,
        request: hbase_20190101_models.DescribeMultiZoneAvailableRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeMultiZoneAvailableRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMultiZoneAvailableRegions',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeMultiZoneAvailableRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_multi_zone_available_regions(
        self,
        request: hbase_20190101_models.DescribeMultiZoneAvailableRegionsRequest,
    ) -> hbase_20190101_models.DescribeMultiZoneAvailableRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_multi_zone_available_regions_with_options(request, runtime)

    async def describe_multi_zone_available_regions_async(
        self,
        request: hbase_20190101_models.DescribeMultiZoneAvailableRegionsRequest,
    ) -> hbase_20190101_models.DescribeMultiZoneAvailableRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_multi_zone_available_regions_with_options_async(request, runtime)

    def describe_multi_zone_available_resource_with_options(
        self,
        request: hbase_20190101_models.DescribeMultiZoneAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeMultiZoneAvailableResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.zone_combination):
            query['ZoneCombination'] = request.zone_combination
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMultiZoneAvailableResource',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeMultiZoneAvailableResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_multi_zone_available_resource_with_options_async(
        self,
        request: hbase_20190101_models.DescribeMultiZoneAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeMultiZoneAvailableResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.zone_combination):
            query['ZoneCombination'] = request.zone_combination
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMultiZoneAvailableResource',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeMultiZoneAvailableResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_multi_zone_available_resource(
        self,
        request: hbase_20190101_models.DescribeMultiZoneAvailableResourceRequest,
    ) -> hbase_20190101_models.DescribeMultiZoneAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_multi_zone_available_resource_with_options(request, runtime)

    async def describe_multi_zone_available_resource_async(
        self,
        request: hbase_20190101_models.DescribeMultiZoneAvailableResourceRequest,
    ) -> hbase_20190101_models.DescribeMultiZoneAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_multi_zone_available_resource_with_options_async(request, runtime)

    def describe_multi_zone_cluster_with_options(
        self,
        request: hbase_20190101_models.DescribeMultiZoneClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeMultiZoneClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMultiZoneCluster',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeMultiZoneClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_multi_zone_cluster_with_options_async(
        self,
        request: hbase_20190101_models.DescribeMultiZoneClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeMultiZoneClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMultiZoneCluster',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeMultiZoneClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_multi_zone_cluster(
        self,
        request: hbase_20190101_models.DescribeMultiZoneClusterRequest,
    ) -> hbase_20190101_models.DescribeMultiZoneClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_multi_zone_cluster_with_options(request, runtime)

    async def describe_multi_zone_cluster_async(
        self,
        request: hbase_20190101_models.DescribeMultiZoneClusterRequest,
    ) -> hbase_20190101_models.DescribeMultiZoneClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_multi_zone_cluster_with_options_async(request, runtime)

    def describe_recoverable_time_range_with_options(
        self,
        request: hbase_20190101_models.DescribeRecoverableTimeRangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeRecoverableTimeRangeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecoverableTimeRange',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeRecoverableTimeRangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_recoverable_time_range_with_options_async(
        self,
        request: hbase_20190101_models.DescribeRecoverableTimeRangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeRecoverableTimeRangeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecoverableTimeRange',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeRecoverableTimeRangeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_recoverable_time_range(
        self,
        request: hbase_20190101_models.DescribeRecoverableTimeRangeRequest,
    ) -> hbase_20190101_models.DescribeRecoverableTimeRangeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_recoverable_time_range_with_options(request, runtime)

    async def describe_recoverable_time_range_async(
        self,
        request: hbase_20190101_models.DescribeRecoverableTimeRangeRequest,
    ) -> hbase_20190101_models.DescribeRecoverableTimeRangeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_recoverable_time_range_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: hbase_20190101_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: hbase_20190101_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: hbase_20190101_models.DescribeRegionsRequest,
    ) -> hbase_20190101_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: hbase_20190101_models.DescribeRegionsRequest,
    ) -> hbase_20190101_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_restore_full_details_with_options(
        self,
        request: hbase_20190101_models.DescribeRestoreFullDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeRestoreFullDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.restore_record_id):
            query['RestoreRecordId'] = request.restore_record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRestoreFullDetails',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeRestoreFullDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_restore_full_details_with_options_async(
        self,
        request: hbase_20190101_models.DescribeRestoreFullDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeRestoreFullDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.restore_record_id):
            query['RestoreRecordId'] = request.restore_record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRestoreFullDetails',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeRestoreFullDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_restore_full_details(
        self,
        request: hbase_20190101_models.DescribeRestoreFullDetailsRequest,
    ) -> hbase_20190101_models.DescribeRestoreFullDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_restore_full_details_with_options(request, runtime)

    async def describe_restore_full_details_async(
        self,
        request: hbase_20190101_models.DescribeRestoreFullDetailsRequest,
    ) -> hbase_20190101_models.DescribeRestoreFullDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_restore_full_details_with_options_async(request, runtime)

    def describe_restore_incr_detail_with_options(
        self,
        request: hbase_20190101_models.DescribeRestoreIncrDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeRestoreIncrDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.restore_record_id):
            query['RestoreRecordId'] = request.restore_record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRestoreIncrDetail',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeRestoreIncrDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_restore_incr_detail_with_options_async(
        self,
        request: hbase_20190101_models.DescribeRestoreIncrDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeRestoreIncrDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.restore_record_id):
            query['RestoreRecordId'] = request.restore_record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRestoreIncrDetail',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeRestoreIncrDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_restore_incr_detail(
        self,
        request: hbase_20190101_models.DescribeRestoreIncrDetailRequest,
    ) -> hbase_20190101_models.DescribeRestoreIncrDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_restore_incr_detail_with_options(request, runtime)

    async def describe_restore_incr_detail_async(
        self,
        request: hbase_20190101_models.DescribeRestoreIncrDetailRequest,
    ) -> hbase_20190101_models.DescribeRestoreIncrDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_restore_incr_detail_with_options_async(request, runtime)

    def describe_restore_schema_details_with_options(
        self,
        request: hbase_20190101_models.DescribeRestoreSchemaDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeRestoreSchemaDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.restore_record_id):
            query['RestoreRecordId'] = request.restore_record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRestoreSchemaDetails',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeRestoreSchemaDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_restore_schema_details_with_options_async(
        self,
        request: hbase_20190101_models.DescribeRestoreSchemaDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeRestoreSchemaDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.restore_record_id):
            query['RestoreRecordId'] = request.restore_record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRestoreSchemaDetails',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeRestoreSchemaDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_restore_schema_details(
        self,
        request: hbase_20190101_models.DescribeRestoreSchemaDetailsRequest,
    ) -> hbase_20190101_models.DescribeRestoreSchemaDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_restore_schema_details_with_options(request, runtime)

    async def describe_restore_schema_details_async(
        self,
        request: hbase_20190101_models.DescribeRestoreSchemaDetailsRequest,
    ) -> hbase_20190101_models.DescribeRestoreSchemaDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_restore_schema_details_with_options_async(request, runtime)

    def describe_restore_summary_with_options(
        self,
        request: hbase_20190101_models.DescribeRestoreSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeRestoreSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRestoreSummary',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeRestoreSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_restore_summary_with_options_async(
        self,
        request: hbase_20190101_models.DescribeRestoreSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeRestoreSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRestoreSummary',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeRestoreSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_restore_summary(
        self,
        request: hbase_20190101_models.DescribeRestoreSummaryRequest,
    ) -> hbase_20190101_models.DescribeRestoreSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_restore_summary_with_options(request, runtime)

    async def describe_restore_summary_async(
        self,
        request: hbase_20190101_models.DescribeRestoreSummaryRequest,
    ) -> hbase_20190101_models.DescribeRestoreSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_restore_summary_with_options_async(request, runtime)

    def describe_restore_tables_with_options(
        self,
        request: hbase_20190101_models.DescribeRestoreTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeRestoreTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.restore_record_id):
            query['RestoreRecordId'] = request.restore_record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRestoreTables',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeRestoreTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_restore_tables_with_options_async(
        self,
        request: hbase_20190101_models.DescribeRestoreTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeRestoreTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.restore_record_id):
            query['RestoreRecordId'] = request.restore_record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRestoreTables',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeRestoreTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_restore_tables(
        self,
        request: hbase_20190101_models.DescribeRestoreTablesRequest,
    ) -> hbase_20190101_models.DescribeRestoreTablesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_restore_tables_with_options(request, runtime)

    async def describe_restore_tables_async(
        self,
        request: hbase_20190101_models.DescribeRestoreTablesRequest,
    ) -> hbase_20190101_models.DescribeRestoreTablesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_restore_tables_with_options_async(request, runtime)

    def describe_security_groups_with_options(
        self,
        request: hbase_20190101_models.DescribeSecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeSecurityGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityGroups',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeSecurityGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_groups_with_options_async(
        self,
        request: hbase_20190101_models.DescribeSecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeSecurityGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityGroups',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeSecurityGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_groups(
        self,
        request: hbase_20190101_models.DescribeSecurityGroupsRequest,
    ) -> hbase_20190101_models.DescribeSecurityGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_security_groups_with_options(request, runtime)

    async def describe_security_groups_async(
        self,
        request: hbase_20190101_models.DescribeSecurityGroupsRequest,
    ) -> hbase_20190101_models.DescribeSecurityGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_groups_with_options_async(request, runtime)

    def describe_serverless_cluster_with_options(
        self,
        request: hbase_20190101_models.DescribeServerlessClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeServerlessClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServerlessCluster',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeServerlessClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_serverless_cluster_with_options_async(
        self,
        request: hbase_20190101_models.DescribeServerlessClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeServerlessClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServerlessCluster',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeServerlessClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_serverless_cluster(
        self,
        request: hbase_20190101_models.DescribeServerlessClusterRequest,
    ) -> hbase_20190101_models.DescribeServerlessClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_serverless_cluster_with_options(request, runtime)

    async def describe_serverless_cluster_async(
        self,
        request: hbase_20190101_models.DescribeServerlessClusterRequest,
    ) -> hbase_20190101_models.DescribeServerlessClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_serverless_cluster_with_options_async(request, runtime)

    def describe_sub_domain_with_options(
        self,
        request: hbase_20190101_models.DescribeSubDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeSubDomainResponse:
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
            action='DescribeSubDomain',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeSubDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sub_domain_with_options_async(
        self,
        request: hbase_20190101_models.DescribeSubDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeSubDomainResponse:
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
            action='DescribeSubDomain',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.DescribeSubDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sub_domain(
        self,
        request: hbase_20190101_models.DescribeSubDomainRequest,
    ) -> hbase_20190101_models.DescribeSubDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sub_domain_with_options(request, runtime)

    async def describe_sub_domain_async(
        self,
        request: hbase_20190101_models.DescribeSubDomainRequest,
    ) -> hbase_20190101_models.DescribeSubDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sub_domain_with_options_async(request, runtime)

    def enable_hbaseue_backup_with_options(
        self,
        request: hbase_20190101_models.EnableHBaseueBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.EnableHBaseueBackupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cold_storage_size):
            query['ColdStorageSize'] = request.cold_storage_size
        if not UtilClient.is_unset(request.hbaseue_cluster_id):
            query['HbaseueClusterId'] = request.hbaseue_cluster_id
        if not UtilClient.is_unset(request.node_count):
            query['NodeCount'] = request.node_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableHBaseueBackup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.EnableHBaseueBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_hbaseue_backup_with_options_async(
        self,
        request: hbase_20190101_models.EnableHBaseueBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.EnableHBaseueBackupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cold_storage_size):
            query['ColdStorageSize'] = request.cold_storage_size
        if not UtilClient.is_unset(request.hbaseue_cluster_id):
            query['HbaseueClusterId'] = request.hbaseue_cluster_id
        if not UtilClient.is_unset(request.node_count):
            query['NodeCount'] = request.node_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableHBaseueBackup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.EnableHBaseueBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_hbaseue_backup(
        self,
        request: hbase_20190101_models.EnableHBaseueBackupRequest,
    ) -> hbase_20190101_models.EnableHBaseueBackupResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_hbaseue_backup_with_options(request, runtime)

    async def enable_hbaseue_backup_async(
        self,
        request: hbase_20190101_models.EnableHBaseueBackupRequest,
    ) -> hbase_20190101_models.EnableHBaseueBackupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_hbaseue_backup_with_options_async(request, runtime)

    def enable_hbaseue_module_with_options(
        self,
        request: hbase_20190101_models.EnableHBaseueModuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.EnableHBaseueModuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.bds_id):
            query['BdsId'] = request.bds_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not UtilClient.is_unset(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.hbaseue_cluster_id):
            query['HbaseueClusterId'] = request.hbaseue_cluster_id
        if not UtilClient.is_unset(request.master_instance_type):
            query['MasterInstanceType'] = request.master_instance_type
        if not UtilClient.is_unset(request.module_cluster_name):
            query['ModuleClusterName'] = request.module_cluster_name
        if not UtilClient.is_unset(request.module_type_name):
            query['ModuleTypeName'] = request.module_type_name
        if not UtilClient.is_unset(request.node_count):
            query['NodeCount'] = request.node_count
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='EnableHBaseueModule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.EnableHBaseueModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_hbaseue_module_with_options_async(
        self,
        request: hbase_20190101_models.EnableHBaseueModuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.EnableHBaseueModuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.bds_id):
            query['BdsId'] = request.bds_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not UtilClient.is_unset(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.hbaseue_cluster_id):
            query['HbaseueClusterId'] = request.hbaseue_cluster_id
        if not UtilClient.is_unset(request.master_instance_type):
            query['MasterInstanceType'] = request.master_instance_type
        if not UtilClient.is_unset(request.module_cluster_name):
            query['ModuleClusterName'] = request.module_cluster_name
        if not UtilClient.is_unset(request.module_type_name):
            query['ModuleTypeName'] = request.module_type_name
        if not UtilClient.is_unset(request.node_count):
            query['NodeCount'] = request.node_count
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='EnableHBaseueModule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.EnableHBaseueModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_hbaseue_module(
        self,
        request: hbase_20190101_models.EnableHBaseueModuleRequest,
    ) -> hbase_20190101_models.EnableHBaseueModuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_hbaseue_module_with_options(request, runtime)

    async def enable_hbaseue_module_async(
        self,
        request: hbase_20190101_models.EnableHBaseueModuleRequest,
    ) -> hbase_20190101_models.EnableHBaseueModuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_hbaseue_module_with_options_async(request, runtime)

    def evaluate_multi_zone_resource_with_options(
        self,
        request: hbase_20190101_models.EvaluateMultiZoneResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.EvaluateMultiZoneResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.arbiter_vswitch_id):
            query['ArbiterVSwitchId'] = request.arbiter_vswitch_id
        if not UtilClient.is_unset(request.arbiter_zone_id):
            query['ArbiterZoneId'] = request.arbiter_zone_id
        if not UtilClient.is_unset(request.arch_version):
            query['ArchVersion'] = request.arch_version
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.core_disk_size):
            query['CoreDiskSize'] = request.core_disk_size
        if not UtilClient.is_unset(request.core_disk_type):
            query['CoreDiskType'] = request.core_disk_type
        if not UtilClient.is_unset(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not UtilClient.is_unset(request.core_node_count):
            query['CoreNodeCount'] = request.core_node_count
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.log_disk_size):
            query['LogDiskSize'] = request.log_disk_size
        if not UtilClient.is_unset(request.log_disk_type):
            query['LogDiskType'] = request.log_disk_type
        if not UtilClient.is_unset(request.log_instance_type):
            query['LogInstanceType'] = request.log_instance_type
        if not UtilClient.is_unset(request.log_node_count):
            query['LogNodeCount'] = request.log_node_count
        if not UtilClient.is_unset(request.master_instance_type):
            query['MasterInstanceType'] = request.master_instance_type
        if not UtilClient.is_unset(request.multi_zone_combination):
            query['MultiZoneCombination'] = request.multi_zone_combination
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.primary_vswitch_id):
            query['PrimaryVSwitchId'] = request.primary_vswitch_id
        if not UtilClient.is_unset(request.primary_zone_id):
            query['PrimaryZoneId'] = request.primary_zone_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not UtilClient.is_unset(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        if not UtilClient.is_unset(request.standby_zone_id):
            query['StandbyZoneId'] = request.standby_zone_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EvaluateMultiZoneResource',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.EvaluateMultiZoneResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def evaluate_multi_zone_resource_with_options_async(
        self,
        request: hbase_20190101_models.EvaluateMultiZoneResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.EvaluateMultiZoneResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.arbiter_vswitch_id):
            query['ArbiterVSwitchId'] = request.arbiter_vswitch_id
        if not UtilClient.is_unset(request.arbiter_zone_id):
            query['ArbiterZoneId'] = request.arbiter_zone_id
        if not UtilClient.is_unset(request.arch_version):
            query['ArchVersion'] = request.arch_version
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.core_disk_size):
            query['CoreDiskSize'] = request.core_disk_size
        if not UtilClient.is_unset(request.core_disk_type):
            query['CoreDiskType'] = request.core_disk_type
        if not UtilClient.is_unset(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not UtilClient.is_unset(request.core_node_count):
            query['CoreNodeCount'] = request.core_node_count
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.log_disk_size):
            query['LogDiskSize'] = request.log_disk_size
        if not UtilClient.is_unset(request.log_disk_type):
            query['LogDiskType'] = request.log_disk_type
        if not UtilClient.is_unset(request.log_instance_type):
            query['LogInstanceType'] = request.log_instance_type
        if not UtilClient.is_unset(request.log_node_count):
            query['LogNodeCount'] = request.log_node_count
        if not UtilClient.is_unset(request.master_instance_type):
            query['MasterInstanceType'] = request.master_instance_type
        if not UtilClient.is_unset(request.multi_zone_combination):
            query['MultiZoneCombination'] = request.multi_zone_combination
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.primary_vswitch_id):
            query['PrimaryVSwitchId'] = request.primary_vswitch_id
        if not UtilClient.is_unset(request.primary_zone_id):
            query['PrimaryZoneId'] = request.primary_zone_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not UtilClient.is_unset(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        if not UtilClient.is_unset(request.standby_zone_id):
            query['StandbyZoneId'] = request.standby_zone_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EvaluateMultiZoneResource',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.EvaluateMultiZoneResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def evaluate_multi_zone_resource(
        self,
        request: hbase_20190101_models.EvaluateMultiZoneResourceRequest,
    ) -> hbase_20190101_models.EvaluateMultiZoneResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.evaluate_multi_zone_resource_with_options(request, runtime)

    async def evaluate_multi_zone_resource_async(
        self,
        request: hbase_20190101_models.EvaluateMultiZoneResourceRequest,
    ) -> hbase_20190101_models.EvaluateMultiZoneResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.evaluate_multi_zone_resource_with_options_async(request, runtime)

    def get_multimode_cms_url_with_options(
        self,
        request: hbase_20190101_models.GetMultimodeCmsUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.GetMultimodeCmsUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMultimodeCmsUrl',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.GetMultimodeCmsUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_multimode_cms_url_with_options_async(
        self,
        request: hbase_20190101_models.GetMultimodeCmsUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.GetMultimodeCmsUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMultimodeCmsUrl',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.GetMultimodeCmsUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_multimode_cms_url(
        self,
        request: hbase_20190101_models.GetMultimodeCmsUrlRequest,
    ) -> hbase_20190101_models.GetMultimodeCmsUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_multimode_cms_url_with_options(request, runtime)

    async def get_multimode_cms_url_async(
        self,
        request: hbase_20190101_models.GetMultimodeCmsUrlRequest,
    ) -> hbase_20190101_models.GetMultimodeCmsUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_multimode_cms_url_with_options_async(request, runtime)

    def list_hbase_instances_with_options(
        self,
        request: hbase_20190101_models.ListHBaseInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ListHBaseInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHBaseInstances',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ListHBaseInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hbase_instances_with_options_async(
        self,
        request: hbase_20190101_models.ListHBaseInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ListHBaseInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHBaseInstances',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ListHBaseInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hbase_instances(
        self,
        request: hbase_20190101_models.ListHBaseInstancesRequest,
    ) -> hbase_20190101_models.ListHBaseInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_hbase_instances_with_options(request, runtime)

    async def list_hbase_instances_async(
        self,
        request: hbase_20190101_models.ListHBaseInstancesRequest,
    ) -> hbase_20190101_models.ListHBaseInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_hbase_instances_with_options_async(request, runtime)

    def list_instance_service_config_histories_with_options(
        self,
        request: hbase_20190101_models.ListInstanceServiceConfigHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ListInstanceServiceConfigHistoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceServiceConfigHistories',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ListInstanceServiceConfigHistoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_service_config_histories_with_options_async(
        self,
        request: hbase_20190101_models.ListInstanceServiceConfigHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ListInstanceServiceConfigHistoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceServiceConfigHistories',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ListInstanceServiceConfigHistoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_service_config_histories(
        self,
        request: hbase_20190101_models.ListInstanceServiceConfigHistoriesRequest,
    ) -> hbase_20190101_models.ListInstanceServiceConfigHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_instance_service_config_histories_with_options(request, runtime)

    async def list_instance_service_config_histories_async(
        self,
        request: hbase_20190101_models.ListInstanceServiceConfigHistoriesRequest,
    ) -> hbase_20190101_models.ListInstanceServiceConfigHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_instance_service_config_histories_with_options_async(request, runtime)

    def list_instance_service_configurations_with_options(
        self,
        request: hbase_20190101_models.ListInstanceServiceConfigurationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ListInstanceServiceConfigurationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceServiceConfigurations',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ListInstanceServiceConfigurationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_service_configurations_with_options_async(
        self,
        request: hbase_20190101_models.ListInstanceServiceConfigurationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ListInstanceServiceConfigurationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceServiceConfigurations',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ListInstanceServiceConfigurationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_service_configurations(
        self,
        request: hbase_20190101_models.ListInstanceServiceConfigurationsRequest,
    ) -> hbase_20190101_models.ListInstanceServiceConfigurationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_instance_service_configurations_with_options(request, runtime)

    async def list_instance_service_configurations_async(
        self,
        request: hbase_20190101_models.ListInstanceServiceConfigurationsRequest,
    ) -> hbase_20190101_models.ListInstanceServiceConfigurationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_instance_service_configurations_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: hbase_20190101_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: hbase_20190101_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: hbase_20190101_models.ListTagResourcesRequest,
    ) -> hbase_20190101_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: hbase_20190101_models.ListTagResourcesRequest,
    ) -> hbase_20190101_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tags_with_options(
        self,
        request: hbase_20190101_models.ListTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ListTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTags',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ListTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tags_with_options_async(
        self,
        request: hbase_20190101_models.ListTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ListTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTags',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ListTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tags(
        self,
        request: hbase_20190101_models.ListTagsRequest,
    ) -> hbase_20190101_models.ListTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tags_with_options(request, runtime)

    async def list_tags_async(
        self,
        request: hbase_20190101_models.ListTagsRequest,
    ) -> hbase_20190101_models.ListTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tags_with_options_async(request, runtime)

    def modify_backup_plan_config_with_options(
        self,
        request: hbase_20190101_models.ModifyBackupPlanConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyBackupPlanConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.full_backup_cycle):
            query['FullBackupCycle'] = request.full_backup_cycle
        if not UtilClient.is_unset(request.min_hfile_backup_count):
            query['MinHFileBackupCount'] = request.min_hfile_backup_count
        if not UtilClient.is_unset(request.next_full_backup_date):
            query['NextFullBackupDate'] = request.next_full_backup_date
        if not UtilClient.is_unset(request.tables):
            query['Tables'] = request.tables
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPlanConfig',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ModifyBackupPlanConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_plan_config_with_options_async(
        self,
        request: hbase_20190101_models.ModifyBackupPlanConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyBackupPlanConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.full_backup_cycle):
            query['FullBackupCycle'] = request.full_backup_cycle
        if not UtilClient.is_unset(request.min_hfile_backup_count):
            query['MinHFileBackupCount'] = request.min_hfile_backup_count
        if not UtilClient.is_unset(request.next_full_backup_date):
            query['NextFullBackupDate'] = request.next_full_backup_date
        if not UtilClient.is_unset(request.tables):
            query['Tables'] = request.tables
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPlanConfig',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ModifyBackupPlanConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_plan_config(
        self,
        request: hbase_20190101_models.ModifyBackupPlanConfigRequest,
    ) -> hbase_20190101_models.ModifyBackupPlanConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_plan_config_with_options(request, runtime)

    async def modify_backup_plan_config_async(
        self,
        request: hbase_20190101_models.ModifyBackupPlanConfigRequest,
    ) -> hbase_20190101_models.ModifyBackupPlanConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_plan_config_with_options_async(request, runtime)

    def modify_backup_policy_with_options(
        self,
        request: hbase_20190101_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.preferred_backup_end_time_utc):
            query['PreferredBackupEndTimeUTC'] = request.preferred_backup_end_time_utc
        if not UtilClient.is_unset(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not UtilClient.is_unset(request.preferred_backup_start_time_utc):
            query['PreferredBackupStartTimeUTC'] = request.preferred_backup_start_time_utc
        if not UtilClient.is_unset(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicy',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ModifyBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_policy_with_options_async(
        self,
        request: hbase_20190101_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.preferred_backup_end_time_utc):
            query['PreferredBackupEndTimeUTC'] = request.preferred_backup_end_time_utc
        if not UtilClient.is_unset(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not UtilClient.is_unset(request.preferred_backup_start_time_utc):
            query['PreferredBackupStartTimeUTC'] = request.preferred_backup_start_time_utc
        if not UtilClient.is_unset(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicy',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ModifyBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_policy(
        self,
        request: hbase_20190101_models.ModifyBackupPolicyRequest,
    ) -> hbase_20190101_models.ModifyBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    async def modify_backup_policy_async(
        self,
        request: hbase_20190101_models.ModifyBackupPolicyRequest,
    ) -> hbase_20190101_models.ModifyBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_policy_with_options_async(request, runtime)

    def modify_cluster_deletion_protection_with_options(
        self,
        request: hbase_20190101_models.ModifyClusterDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyClusterDeletionProtectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.protection):
            query['Protection'] = request.protection
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClusterDeletionProtection',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ModifyClusterDeletionProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_deletion_protection_with_options_async(
        self,
        request: hbase_20190101_models.ModifyClusterDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyClusterDeletionProtectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.protection):
            query['Protection'] = request.protection
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClusterDeletionProtection',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ModifyClusterDeletionProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cluster_deletion_protection(
        self,
        request: hbase_20190101_models.ModifyClusterDeletionProtectionRequest,
    ) -> hbase_20190101_models.ModifyClusterDeletionProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_deletion_protection_with_options(request, runtime)

    async def modify_cluster_deletion_protection_async(
        self,
        request: hbase_20190101_models.ModifyClusterDeletionProtectionRequest,
    ) -> hbase_20190101_models.ModifyClusterDeletionProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cluster_deletion_protection_with_options_async(request, runtime)

    def modify_disk_warning_line_with_options(
        self,
        request: hbase_20190101_models.ModifyDiskWarningLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyDiskWarningLineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.warning_line):
            query['WarningLine'] = request.warning_line
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDiskWarningLine',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ModifyDiskWarningLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_disk_warning_line_with_options_async(
        self,
        request: hbase_20190101_models.ModifyDiskWarningLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyDiskWarningLineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.warning_line):
            query['WarningLine'] = request.warning_line
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDiskWarningLine',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ModifyDiskWarningLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_disk_warning_line(
        self,
        request: hbase_20190101_models.ModifyDiskWarningLineRequest,
    ) -> hbase_20190101_models.ModifyDiskWarningLineResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_disk_warning_line_with_options(request, runtime)

    async def modify_disk_warning_line_async(
        self,
        request: hbase_20190101_models.ModifyDiskWarningLineRequest,
    ) -> hbase_20190101_models.ModifyDiskWarningLineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_disk_warning_line_with_options_async(request, runtime)

    def modify_instance_maintain_time_with_options(
        self,
        request: hbase_20190101_models.ModifyInstanceMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyInstanceMaintainTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.maintain_end_time):
            query['MaintainEndTime'] = request.maintain_end_time
        if not UtilClient.is_unset(request.maintain_start_time):
            query['MaintainStartTime'] = request.maintain_start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceMaintainTime',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ModifyInstanceMaintainTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_maintain_time_with_options_async(
        self,
        request: hbase_20190101_models.ModifyInstanceMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyInstanceMaintainTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.maintain_end_time):
            query['MaintainEndTime'] = request.maintain_end_time
        if not UtilClient.is_unset(request.maintain_start_time):
            query['MaintainStartTime'] = request.maintain_start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceMaintainTime',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ModifyInstanceMaintainTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_maintain_time(
        self,
        request: hbase_20190101_models.ModifyInstanceMaintainTimeRequest,
    ) -> hbase_20190101_models.ModifyInstanceMaintainTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_maintain_time_with_options(request, runtime)

    async def modify_instance_maintain_time_async(
        self,
        request: hbase_20190101_models.ModifyInstanceMaintainTimeRequest,
    ) -> hbase_20190101_models.ModifyInstanceMaintainTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_maintain_time_with_options_async(request, runtime)

    def modify_instance_name_with_options(
        self,
        request: hbase_20190101_models.ModifyInstanceNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyInstanceNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceName',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ModifyInstanceNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_name_with_options_async(
        self,
        request: hbase_20190101_models.ModifyInstanceNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyInstanceNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceName',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ModifyInstanceNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_name(
        self,
        request: hbase_20190101_models.ModifyInstanceNameRequest,
    ) -> hbase_20190101_models.ModifyInstanceNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_name_with_options(request, runtime)

    async def modify_instance_name_async(
        self,
        request: hbase_20190101_models.ModifyInstanceNameRequest,
    ) -> hbase_20190101_models.ModifyInstanceNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_name_with_options_async(request, runtime)

    def modify_instance_service_config_with_options(
        self,
        request: hbase_20190101_models.ModifyInstanceServiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyInstanceServiceConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.configure_name):
            query['ConfigureName'] = request.configure_name
        if not UtilClient.is_unset(request.configure_value):
            query['ConfigureValue'] = request.configure_value
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.restart):
            query['Restart'] = request.restart
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceServiceConfig',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ModifyInstanceServiceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_service_config_with_options_async(
        self,
        request: hbase_20190101_models.ModifyInstanceServiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyInstanceServiceConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.configure_name):
            query['ConfigureName'] = request.configure_name
        if not UtilClient.is_unset(request.configure_value):
            query['ConfigureValue'] = request.configure_value
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.restart):
            query['Restart'] = request.restart
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceServiceConfig',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ModifyInstanceServiceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_service_config(
        self,
        request: hbase_20190101_models.ModifyInstanceServiceConfigRequest,
    ) -> hbase_20190101_models.ModifyInstanceServiceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_service_config_with_options(request, runtime)

    async def modify_instance_service_config_async(
        self,
        request: hbase_20190101_models.ModifyInstanceServiceConfigRequest,
    ) -> hbase_20190101_models.ModifyInstanceServiceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_service_config_with_options_async(request, runtime)

    def modify_instance_type_with_options(
        self,
        request: hbase_20190101_models.ModifyInstanceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyInstanceTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not UtilClient.is_unset(request.master_instance_type):
            query['MasterInstanceType'] = request.master_instance_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceType',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ModifyInstanceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_type_with_options_async(
        self,
        request: hbase_20190101_models.ModifyInstanceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyInstanceTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not UtilClient.is_unset(request.master_instance_type):
            query['MasterInstanceType'] = request.master_instance_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceType',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ModifyInstanceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_type(
        self,
        request: hbase_20190101_models.ModifyInstanceTypeRequest,
    ) -> hbase_20190101_models.ModifyInstanceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_type_with_options(request, runtime)

    async def modify_instance_type_async(
        self,
        request: hbase_20190101_models.ModifyInstanceTypeRequest,
    ) -> hbase_20190101_models.ModifyInstanceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_type_with_options_async(request, runtime)

    def modify_ip_whitelist_with_options(
        self,
        request: hbase_20190101_models.ModifyIpWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyIpWhitelistResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.ip_list):
            query['IpList'] = request.ip_list
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyIpWhitelist',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ModifyIpWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_ip_whitelist_with_options_async(
        self,
        request: hbase_20190101_models.ModifyIpWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyIpWhitelistResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.ip_list):
            query['IpList'] = request.ip_list
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyIpWhitelist',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ModifyIpWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_ip_whitelist(
        self,
        request: hbase_20190101_models.ModifyIpWhitelistRequest,
    ) -> hbase_20190101_models.ModifyIpWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ip_whitelist_with_options(request, runtime)

    async def modify_ip_whitelist_async(
        self,
        request: hbase_20190101_models.ModifyIpWhitelistRequest,
    ) -> hbase_20190101_models.ModifyIpWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ip_whitelist_with_options_async(request, runtime)

    def modify_multi_zone_cluster_node_type_with_options(
        self,
        request: hbase_20190101_models.ModifyMultiZoneClusterNodeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyMultiZoneClusterNodeTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not UtilClient.is_unset(request.log_instance_type):
            query['LogInstanceType'] = request.log_instance_type
        if not UtilClient.is_unset(request.master_instance_type):
            query['MasterInstanceType'] = request.master_instance_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMultiZoneClusterNodeType',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ModifyMultiZoneClusterNodeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_multi_zone_cluster_node_type_with_options_async(
        self,
        request: hbase_20190101_models.ModifyMultiZoneClusterNodeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyMultiZoneClusterNodeTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not UtilClient.is_unset(request.log_instance_type):
            query['LogInstanceType'] = request.log_instance_type
        if not UtilClient.is_unset(request.master_instance_type):
            query['MasterInstanceType'] = request.master_instance_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMultiZoneClusterNodeType',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ModifyMultiZoneClusterNodeTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_multi_zone_cluster_node_type(
        self,
        request: hbase_20190101_models.ModifyMultiZoneClusterNodeTypeRequest,
    ) -> hbase_20190101_models.ModifyMultiZoneClusterNodeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_multi_zone_cluster_node_type_with_options(request, runtime)

    async def modify_multi_zone_cluster_node_type_async(
        self,
        request: hbase_20190101_models.ModifyMultiZoneClusterNodeTypeRequest,
    ) -> hbase_20190101_models.ModifyMultiZoneClusterNodeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_multi_zone_cluster_node_type_with_options_async(request, runtime)

    def modify_security_groups_with_options(
        self,
        request: hbase_20190101_models.ModifySecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifySecurityGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityGroups',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ModifySecurityGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_security_groups_with_options_async(
        self,
        request: hbase_20190101_models.ModifySecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifySecurityGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityGroups',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ModifySecurityGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_security_groups(
        self,
        request: hbase_20190101_models.ModifySecurityGroupsRequest,
    ) -> hbase_20190101_models.ModifySecurityGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_security_groups_with_options(request, runtime)

    async def modify_security_groups_async(
        self,
        request: hbase_20190101_models.ModifySecurityGroupsRequest,
    ) -> hbase_20190101_models.ModifySecurityGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_groups_with_options_async(request, runtime)

    def modify_uiaccount_password_with_options(
        self,
        request: hbase_20190101_models.ModifyUIAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyUIAccountPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUIAccountPassword',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ModifyUIAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_uiaccount_password_with_options_async(
        self,
        request: hbase_20190101_models.ModifyUIAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyUIAccountPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUIAccountPassword',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ModifyUIAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_uiaccount_password(
        self,
        request: hbase_20190101_models.ModifyUIAccountPasswordRequest,
    ) -> hbase_20190101_models.ModifyUIAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_uiaccount_password_with_options(request, runtime)

    async def modify_uiaccount_password_async(
        self,
        request: hbase_20190101_models.ModifyUIAccountPasswordRequest,
    ) -> hbase_20190101_models.ModifyUIAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_uiaccount_password_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: hbase_20190101_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: hbase_20190101_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.MoveResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_resource_group(
        self,
        request: hbase_20190101_models.MoveResourceGroupRequest,
    ) -> hbase_20190101_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: hbase_20190101_models.MoveResourceGroupRequest,
    ) -> hbase_20190101_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def open_backup_with_options(
        self,
        request: hbase_20190101_models.OpenBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.OpenBackupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenBackup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.OpenBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_backup_with_options_async(
        self,
        request: hbase_20190101_models.OpenBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.OpenBackupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenBackup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.OpenBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_backup(
        self,
        request: hbase_20190101_models.OpenBackupRequest,
    ) -> hbase_20190101_models.OpenBackupResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_backup_with_options(request, runtime)

    async def open_backup_async(
        self,
        request: hbase_20190101_models.OpenBackupRequest,
    ) -> hbase_20190101_models.OpenBackupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_backup_with_options_async(request, runtime)

    def purge_instance_with_options(
        self,
        request: hbase_20190101_models.PurgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.PurgeInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PurgeInstance',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.PurgeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def purge_instance_with_options_async(
        self,
        request: hbase_20190101_models.PurgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.PurgeInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PurgeInstance',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.PurgeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def purge_instance(
        self,
        request: hbase_20190101_models.PurgeInstanceRequest,
    ) -> hbase_20190101_models.PurgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.purge_instance_with_options(request, runtime)

    async def purge_instance_async(
        self,
        request: hbase_20190101_models.PurgeInstanceRequest,
    ) -> hbase_20190101_models.PurgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.purge_instance_with_options_async(request, runtime)

    def query_hbase_ha_dbwith_options(
        self,
        request: hbase_20190101_models.QueryHBaseHaDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.QueryHBaseHaDBResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bds_id):
            query['BdsId'] = request.bds_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryHBaseHaDB',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.QueryHBaseHaDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_hbase_ha_dbwith_options_async(
        self,
        request: hbase_20190101_models.QueryHBaseHaDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.QueryHBaseHaDBResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bds_id):
            query['BdsId'] = request.bds_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryHBaseHaDB',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.QueryHBaseHaDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_hbase_ha_db(
        self,
        request: hbase_20190101_models.QueryHBaseHaDBRequest,
    ) -> hbase_20190101_models.QueryHBaseHaDBResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_hbase_ha_dbwith_options(request, runtime)

    async def query_hbase_ha_db_async(
        self,
        request: hbase_20190101_models.QueryHBaseHaDBRequest,
    ) -> hbase_20190101_models.QueryHBaseHaDBResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_hbase_ha_dbwith_options_async(request, runtime)

    def query_xpack_relate_dbwith_options(
        self,
        request: hbase_20190101_models.QueryXpackRelateDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.QueryXpackRelateDBResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.has_single_node):
            query['HasSingleNode'] = request.has_single_node
        if not UtilClient.is_unset(request.relate_db_type):
            query['RelateDbType'] = request.relate_db_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryXpackRelateDB',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.QueryXpackRelateDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_xpack_relate_dbwith_options_async(
        self,
        request: hbase_20190101_models.QueryXpackRelateDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.QueryXpackRelateDBResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.has_single_node):
            query['HasSingleNode'] = request.has_single_node
        if not UtilClient.is_unset(request.relate_db_type):
            query['RelateDbType'] = request.relate_db_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryXpackRelateDB',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.QueryXpackRelateDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_xpack_relate_db(
        self,
        request: hbase_20190101_models.QueryXpackRelateDBRequest,
    ) -> hbase_20190101_models.QueryXpackRelateDBResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_xpack_relate_dbwith_options(request, runtime)

    async def query_xpack_relate_db_async(
        self,
        request: hbase_20190101_models.QueryXpackRelateDBRequest,
    ) -> hbase_20190101_models.QueryXpackRelateDBResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_xpack_relate_dbwith_options_async(request, runtime)

    def relate_db_for_hbase_ha_with_options(
        self,
        request: hbase_20190101_models.RelateDbForHBaseHaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.RelateDbForHBaseHaResponse:
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RelateDbForHBaseHa',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.RelateDbForHBaseHaResponse(),
            self.call_api(params, req, runtime)
        )

    async def relate_db_for_hbase_ha_with_options_async(
        self,
        request: hbase_20190101_models.RelateDbForHBaseHaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.RelateDbForHBaseHaResponse:
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RelateDbForHBaseHa',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.RelateDbForHBaseHaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def relate_db_for_hbase_ha(
        self,
        request: hbase_20190101_models.RelateDbForHBaseHaRequest,
    ) -> hbase_20190101_models.RelateDbForHBaseHaResponse:
        runtime = util_models.RuntimeOptions()
        return self.relate_db_for_hbase_ha_with_options(request, runtime)

    async def relate_db_for_hbase_ha_async(
        self,
        request: hbase_20190101_models.RelateDbForHBaseHaRequest,
    ) -> hbase_20190101_models.RelateDbForHBaseHaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.relate_db_for_hbase_ha_with_options_async(request, runtime)

    def release_public_network_address_with_options(
        self,
        request: hbase_20190101_models.ReleasePublicNetworkAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ReleasePublicNetworkAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleasePublicNetworkAddress',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ReleasePublicNetworkAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_public_network_address_with_options_async(
        self,
        request: hbase_20190101_models.ReleasePublicNetworkAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ReleasePublicNetworkAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleasePublicNetworkAddress',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ReleasePublicNetworkAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_public_network_address(
        self,
        request: hbase_20190101_models.ReleasePublicNetworkAddressRequest,
    ) -> hbase_20190101_models.ReleasePublicNetworkAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_public_network_address_with_options(request, runtime)

    async def release_public_network_address_async(
        self,
        request: hbase_20190101_models.ReleasePublicNetworkAddressRequest,
    ) -> hbase_20190101_models.ReleasePublicNetworkAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_public_network_address_with_options_async(request, runtime)

    def renew_instance_with_options(
        self,
        request: hbase_20190101_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.RenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        request: hbase_20190101_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.RenewInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_instance(
        self,
        request: hbase_20190101_models.RenewInstanceRequest,
    ) -> hbase_20190101_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    async def renew_instance_async(
        self,
        request: hbase_20190101_models.RenewInstanceRequest,
    ) -> hbase_20190101_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_instance_with_options_async(request, runtime)

    def resize_cold_storage_size_with_options(
        self,
        request: hbase_20190101_models.ResizeColdStorageSizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ResizeColdStorageSizeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cold_storage_size):
            query['ColdStorageSize'] = request.cold_storage_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResizeColdStorageSize',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ResizeColdStorageSizeResponse(),
            self.call_api(params, req, runtime)
        )

    async def resize_cold_storage_size_with_options_async(
        self,
        request: hbase_20190101_models.ResizeColdStorageSizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ResizeColdStorageSizeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cold_storage_size):
            query['ColdStorageSize'] = request.cold_storage_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResizeColdStorageSize',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ResizeColdStorageSizeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resize_cold_storage_size(
        self,
        request: hbase_20190101_models.ResizeColdStorageSizeRequest,
    ) -> hbase_20190101_models.ResizeColdStorageSizeResponse:
        runtime = util_models.RuntimeOptions()
        return self.resize_cold_storage_size_with_options(request, runtime)

    async def resize_cold_storage_size_async(
        self,
        request: hbase_20190101_models.ResizeColdStorageSizeRequest,
    ) -> hbase_20190101_models.ResizeColdStorageSizeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resize_cold_storage_size_with_options_async(request, runtime)

    def resize_disk_size_with_options(
        self,
        request: hbase_20190101_models.ResizeDiskSizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ResizeDiskSizeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.node_disk_size):
            query['NodeDiskSize'] = request.node_disk_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResizeDiskSize',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ResizeDiskSizeResponse(),
            self.call_api(params, req, runtime)
        )

    async def resize_disk_size_with_options_async(
        self,
        request: hbase_20190101_models.ResizeDiskSizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ResizeDiskSizeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.node_disk_size):
            query['NodeDiskSize'] = request.node_disk_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResizeDiskSize',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ResizeDiskSizeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resize_disk_size(
        self,
        request: hbase_20190101_models.ResizeDiskSizeRequest,
    ) -> hbase_20190101_models.ResizeDiskSizeResponse:
        runtime = util_models.RuntimeOptions()
        return self.resize_disk_size_with_options(request, runtime)

    async def resize_disk_size_async(
        self,
        request: hbase_20190101_models.ResizeDiskSizeRequest,
    ) -> hbase_20190101_models.ResizeDiskSizeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resize_disk_size_with_options_async(request, runtime)

    def resize_multi_zone_cluster_disk_size_with_options(
        self,
        request: hbase_20190101_models.ResizeMultiZoneClusterDiskSizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ResizeMultiZoneClusterDiskSizeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.core_disk_size):
            query['CoreDiskSize'] = request.core_disk_size
        if not UtilClient.is_unset(request.log_disk_size):
            query['LogDiskSize'] = request.log_disk_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResizeMultiZoneClusterDiskSize',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ResizeMultiZoneClusterDiskSizeResponse(),
            self.call_api(params, req, runtime)
        )

    async def resize_multi_zone_cluster_disk_size_with_options_async(
        self,
        request: hbase_20190101_models.ResizeMultiZoneClusterDiskSizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ResizeMultiZoneClusterDiskSizeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.core_disk_size):
            query['CoreDiskSize'] = request.core_disk_size
        if not UtilClient.is_unset(request.log_disk_size):
            query['LogDiskSize'] = request.log_disk_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResizeMultiZoneClusterDiskSize',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ResizeMultiZoneClusterDiskSizeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resize_multi_zone_cluster_disk_size(
        self,
        request: hbase_20190101_models.ResizeMultiZoneClusterDiskSizeRequest,
    ) -> hbase_20190101_models.ResizeMultiZoneClusterDiskSizeResponse:
        runtime = util_models.RuntimeOptions()
        return self.resize_multi_zone_cluster_disk_size_with_options(request, runtime)

    async def resize_multi_zone_cluster_disk_size_async(
        self,
        request: hbase_20190101_models.ResizeMultiZoneClusterDiskSizeRequest,
    ) -> hbase_20190101_models.ResizeMultiZoneClusterDiskSizeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resize_multi_zone_cluster_disk_size_with_options_async(request, runtime)

    def resize_multi_zone_cluster_node_count_with_options(
        self,
        request: hbase_20190101_models.ResizeMultiZoneClusterNodeCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ResizeMultiZoneClusterNodeCountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.arbiter_vswitch_id):
            query['ArbiterVSwitchId'] = request.arbiter_vswitch_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.core_node_count):
            query['CoreNodeCount'] = request.core_node_count
        if not UtilClient.is_unset(request.log_node_count):
            query['LogNodeCount'] = request.log_node_count
        if not UtilClient.is_unset(request.primary_core_node_count):
            query['PrimaryCoreNodeCount'] = request.primary_core_node_count
        if not UtilClient.is_unset(request.primary_vswitch_id):
            query['PrimaryVSwitchId'] = request.primary_vswitch_id
        if not UtilClient.is_unset(request.standby_core_node_count):
            query['StandbyCoreNodeCount'] = request.standby_core_node_count
        if not UtilClient.is_unset(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResizeMultiZoneClusterNodeCount',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ResizeMultiZoneClusterNodeCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def resize_multi_zone_cluster_node_count_with_options_async(
        self,
        request: hbase_20190101_models.ResizeMultiZoneClusterNodeCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ResizeMultiZoneClusterNodeCountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.arbiter_vswitch_id):
            query['ArbiterVSwitchId'] = request.arbiter_vswitch_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.core_node_count):
            query['CoreNodeCount'] = request.core_node_count
        if not UtilClient.is_unset(request.log_node_count):
            query['LogNodeCount'] = request.log_node_count
        if not UtilClient.is_unset(request.primary_core_node_count):
            query['PrimaryCoreNodeCount'] = request.primary_core_node_count
        if not UtilClient.is_unset(request.primary_vswitch_id):
            query['PrimaryVSwitchId'] = request.primary_vswitch_id
        if not UtilClient.is_unset(request.standby_core_node_count):
            query['StandbyCoreNodeCount'] = request.standby_core_node_count
        if not UtilClient.is_unset(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResizeMultiZoneClusterNodeCount',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ResizeMultiZoneClusterNodeCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resize_multi_zone_cluster_node_count(
        self,
        request: hbase_20190101_models.ResizeMultiZoneClusterNodeCountRequest,
    ) -> hbase_20190101_models.ResizeMultiZoneClusterNodeCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.resize_multi_zone_cluster_node_count_with_options(request, runtime)

    async def resize_multi_zone_cluster_node_count_async(
        self,
        request: hbase_20190101_models.ResizeMultiZoneClusterNodeCountRequest,
    ) -> hbase_20190101_models.ResizeMultiZoneClusterNodeCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resize_multi_zone_cluster_node_count_with_options_async(request, runtime)

    def resize_node_count_with_options(
        self,
        request: hbase_20190101_models.ResizeNodeCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ResizeNodeCountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.node_count):
            query['NodeCount'] = request.node_count
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResizeNodeCount',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ResizeNodeCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def resize_node_count_with_options_async(
        self,
        request: hbase_20190101_models.ResizeNodeCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ResizeNodeCountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.node_count):
            query['NodeCount'] = request.node_count
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResizeNodeCount',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.ResizeNodeCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resize_node_count(
        self,
        request: hbase_20190101_models.ResizeNodeCountRequest,
    ) -> hbase_20190101_models.ResizeNodeCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.resize_node_count_with_options(request, runtime)

    async def resize_node_count_async(
        self,
        request: hbase_20190101_models.ResizeNodeCountRequest,
    ) -> hbase_20190101_models.ResizeNodeCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resize_node_count_with_options_async(request, runtime)

    def restart_instance_with_options(
        self,
        request: hbase_20190101_models.RestartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.RestartInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.components):
            query['Components'] = request.components
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartInstance',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.RestartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_instance_with_options_async(
        self,
        request: hbase_20190101_models.RestartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.RestartInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.components):
            query['Components'] = request.components
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartInstance',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.RestartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_instance(
        self,
        request: hbase_20190101_models.RestartInstanceRequest,
    ) -> hbase_20190101_models.RestartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_instance_with_options(request, runtime)

    async def restart_instance_async(
        self,
        request: hbase_20190101_models.RestartInstanceRequest,
    ) -> hbase_20190101_models.RestartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_instance_with_options_async(request, runtime)

    def switch_hbase_ha_slb_with_options(
        self,
        request: hbase_20190101_models.SwitchHbaseHaSlbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.SwitchHbaseHaSlbResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bds_id):
            query['BdsId'] = request.bds_id
        if not UtilClient.is_unset(request.ha_id):
            query['HaId'] = request.ha_id
        if not UtilClient.is_unset(request.ha_types):
            query['HaTypes'] = request.ha_types
        if not UtilClient.is_unset(request.hbase_type):
            query['HbaseType'] = request.hbase_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchHbaseHaSlb',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.SwitchHbaseHaSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_hbase_ha_slb_with_options_async(
        self,
        request: hbase_20190101_models.SwitchHbaseHaSlbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.SwitchHbaseHaSlbResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bds_id):
            query['BdsId'] = request.bds_id
        if not UtilClient.is_unset(request.ha_id):
            query['HaId'] = request.ha_id
        if not UtilClient.is_unset(request.ha_types):
            query['HaTypes'] = request.ha_types
        if not UtilClient.is_unset(request.hbase_type):
            query['HbaseType'] = request.hbase_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchHbaseHaSlb',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.SwitchHbaseHaSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_hbase_ha_slb(
        self,
        request: hbase_20190101_models.SwitchHbaseHaSlbRequest,
    ) -> hbase_20190101_models.SwitchHbaseHaSlbResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_hbase_ha_slb_with_options(request, runtime)

    async def switch_hbase_ha_slb_async(
        self,
        request: hbase_20190101_models.SwitchHbaseHaSlbRequest,
    ) -> hbase_20190101_models.SwitchHbaseHaSlbResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_hbase_ha_slb_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: hbase_20190101_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: hbase_20190101_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: hbase_20190101_models.TagResourcesRequest,
    ) -> hbase_20190101_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: hbase_20190101_models.TagResourcesRequest,
    ) -> hbase_20190101_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def un_tag_resources_with_options(
        self,
        request: hbase_20190101_models.UnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.UnTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnTagResources',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.UnTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_tag_resources_with_options_async(
        self,
        request: hbase_20190101_models.UnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.UnTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnTagResources',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.UnTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_tag_resources(
        self,
        request: hbase_20190101_models.UnTagResourcesRequest,
    ) -> hbase_20190101_models.UnTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.un_tag_resources_with_options(request, runtime)

    async def un_tag_resources_async(
        self,
        request: hbase_20190101_models.UnTagResourcesRequest,
    ) -> hbase_20190101_models.UnTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.un_tag_resources_with_options_async(request, runtime)

    def upgrade_minor_version_with_options(
        self,
        request: hbase_20190101_models.UpgradeMinorVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.UpgradeMinorVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.components):
            query['Components'] = request.components
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeMinorVersion',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.UpgradeMinorVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_minor_version_with_options_async(
        self,
        request: hbase_20190101_models.UpgradeMinorVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.UpgradeMinorVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.components):
            query['Components'] = request.components
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeMinorVersion',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.UpgradeMinorVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_minor_version(
        self,
        request: hbase_20190101_models.UpgradeMinorVersionRequest,
    ) -> hbase_20190101_models.UpgradeMinorVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_minor_version_with_options(request, runtime)

    async def upgrade_minor_version_async(
        self,
        request: hbase_20190101_models.UpgradeMinorVersionRequest,
    ) -> hbase_20190101_models.UpgradeMinorVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_minor_version_with_options_async(request, runtime)

    def upgrade_multi_zone_cluster_with_options(
        self,
        request: hbase_20190101_models.UpgradeMultiZoneClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.UpgradeMultiZoneClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.components):
            query['Components'] = request.components
        if not UtilClient.is_unset(request.restart_components):
            query['RestartComponents'] = request.restart_components
        if not UtilClient.is_unset(request.run_mode):
            query['RunMode'] = request.run_mode
        if not UtilClient.is_unset(request.upgrade_ins_name):
            query['UpgradeInsName'] = request.upgrade_ins_name
        if not UtilClient.is_unset(request.versions):
            query['Versions'] = request.versions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeMultiZoneCluster',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.UpgradeMultiZoneClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_multi_zone_cluster_with_options_async(
        self,
        request: hbase_20190101_models.UpgradeMultiZoneClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.UpgradeMultiZoneClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.components):
            query['Components'] = request.components
        if not UtilClient.is_unset(request.restart_components):
            query['RestartComponents'] = request.restart_components
        if not UtilClient.is_unset(request.run_mode):
            query['RunMode'] = request.run_mode
        if not UtilClient.is_unset(request.upgrade_ins_name):
            query['UpgradeInsName'] = request.upgrade_ins_name
        if not UtilClient.is_unset(request.versions):
            query['Versions'] = request.versions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeMultiZoneCluster',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.UpgradeMultiZoneClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_multi_zone_cluster(
        self,
        request: hbase_20190101_models.UpgradeMultiZoneClusterRequest,
    ) -> hbase_20190101_models.UpgradeMultiZoneClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_multi_zone_cluster_with_options(request, runtime)

    async def upgrade_multi_zone_cluster_async(
        self,
        request: hbase_20190101_models.UpgradeMultiZoneClusterRequest,
    ) -> hbase_20190101_models.UpgradeMultiZoneClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_multi_zone_cluster_with_options_async(request, runtime)

    def xpack_relate_dbwith_options(
        self,
        request: hbase_20190101_models.XpackRelateDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.XpackRelateDBResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.db_cluster_ids):
            query['DbClusterIds'] = request.db_cluster_ids
        if not UtilClient.is_unset(request.relate_db_type):
            query['RelateDbType'] = request.relate_db_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='XpackRelateDB',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.XpackRelateDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def xpack_relate_dbwith_options_async(
        self,
        request: hbase_20190101_models.XpackRelateDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.XpackRelateDBResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.db_cluster_ids):
            query['DbClusterIds'] = request.db_cluster_ids
        if not UtilClient.is_unset(request.relate_db_type):
            query['RelateDbType'] = request.relate_db_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='XpackRelateDB',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hbase_20190101_models.XpackRelateDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def xpack_relate_db(
        self,
        request: hbase_20190101_models.XpackRelateDBRequest,
    ) -> hbase_20190101_models.XpackRelateDBResponse:
        runtime = util_models.RuntimeOptions()
        return self.xpack_relate_dbwith_options(request, runtime)

    async def xpack_relate_db_async(
        self,
        request: hbase_20190101_models.XpackRelateDBRequest,
    ) -> hbase_20190101_models.XpackRelateDBResponse:
        runtime = util_models.RuntimeOptions()
        return await self.xpack_relate_dbwith_options_async(request, runtime)
