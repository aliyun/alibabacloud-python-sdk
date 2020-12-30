# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_hbase20190101 import models as hbase_20190101_models
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.AddUserHdfsInfoResponse().from_map(
            self.do_rpcrequest('AddUserHdfsInfo', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_user_hdfs_info_with_options_async(
        self,
        request: hbase_20190101_models.AddUserHdfsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.AddUserHdfsInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.AddUserHdfsInfoResponse().from_map(
            await self.do_rpcrequest_async('AddUserHdfsInfo', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.AllocatePublicNetworkAddressResponse().from_map(
            self.do_rpcrequest('AllocatePublicNetworkAddress', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def allocate_public_network_address_with_options_async(
        self,
        request: hbase_20190101_models.AllocatePublicNetworkAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.AllocatePublicNetworkAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.AllocatePublicNetworkAddressResponse().from_map(
            await self.do_rpcrequest_async('AllocatePublicNetworkAddress', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.CheckComponentsVersionResponse().from_map(
            self.do_rpcrequest('CheckComponentsVersion', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_components_version_with_options_async(
        self,
        request: hbase_20190101_models.CheckComponentsVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CheckComponentsVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.CheckComponentsVersionResponse().from_map(
            await self.do_rpcrequest_async('CheckComponentsVersion', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.CloseBackupResponse().from_map(
            self.do_rpcrequest('CloseBackup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def close_backup_with_options_async(
        self,
        request: hbase_20190101_models.CloseBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CloseBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.CloseBackupResponse().from_map(
            await self.do_rpcrequest_async('CloseBackup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ConvertInstanceResponse().from_map(
            self.do_rpcrequest('ConvertInstance', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def convert_instance_with_options_async(
        self,
        request: hbase_20190101_models.ConvertInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ConvertInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ConvertInstanceResponse().from_map(
            await self.do_rpcrequest_async('ConvertInstance', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.CreateBackupPlanResponse().from_map(
            self.do_rpcrequest('CreateBackupPlan', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_backup_plan_with_options_async(
        self,
        request: hbase_20190101_models.CreateBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CreateBackupPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.CreateBackupPlanResponse().from_map(
            await self.do_rpcrequest_async('CreateBackupPlan', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.CreateClusterResponse().from_map(
            self.do_rpcrequest('CreateCluster', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cluster_with_options_async(
        self,
        request: hbase_20190101_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CreateClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.CreateClusterResponse().from_map(
            await self.do_rpcrequest_async('CreateCluster', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.CreateGlobalResourceResponse().from_map(
            self.do_rpcrequest('CreateGlobalResource', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_global_resource_with_options_async(
        self,
        request: hbase_20190101_models.CreateGlobalResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CreateGlobalResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.CreateGlobalResourceResponse().from_map(
            await self.do_rpcrequest_async('CreateGlobalResource', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_hbase_ha_slb_with_options(
        self,
        request: hbase_20190101_models.CreateHbaseHaSlbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CreateHbaseHaSlbResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.CreateHbaseHaSlbResponse().from_map(
            self.do_rpcrequest('CreateHbaseHaSlb', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_hbase_ha_slb_with_options_async(
        self,
        request: hbase_20190101_models.CreateHbaseHaSlbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CreateHbaseHaSlbResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.CreateHbaseHaSlbResponse().from_map(
            await self.do_rpcrequest_async('CreateHbaseHaSlb', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_hbase_slb_server_with_options(
        self,
        request: hbase_20190101_models.CreateHBaseSlbServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CreateHBaseSlbServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.CreateHBaseSlbServerResponse().from_map(
            self.do_rpcrequest('CreateHBaseSlbServer', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_hbase_slb_server_with_options_async(
        self,
        request: hbase_20190101_models.CreateHBaseSlbServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CreateHBaseSlbServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.CreateHBaseSlbServerResponse().from_map(
            await self.do_rpcrequest_async('CreateHBaseSlbServer', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_multi_zone_cluster_with_options(
        self,
        request: hbase_20190101_models.CreateMultiZoneClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CreateMultiZoneClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.CreateMultiZoneClusterResponse().from_map(
            self.do_rpcrequest('CreateMultiZoneCluster', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_multi_zone_cluster_with_options_async(
        self,
        request: hbase_20190101_models.CreateMultiZoneClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CreateMultiZoneClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.CreateMultiZoneClusterResponse().from_map(
            await self.do_rpcrequest_async('CreateMultiZoneCluster', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.CreateRestorePlanResponse().from_map(
            self.do_rpcrequest('CreateRestorePlan', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_restore_plan_with_options_async(
        self,
        request: hbase_20190101_models.CreateRestorePlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CreateRestorePlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.CreateRestorePlanResponse().from_map(
            await self.do_rpcrequest_async('CreateRestorePlan', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.CreateServerlessClusterResponse().from_map(
            self.do_rpcrequest('CreateServerlessCluster', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_serverless_cluster_with_options_async(
        self,
        request: hbase_20190101_models.CreateServerlessClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.CreateServerlessClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.CreateServerlessClusterResponse().from_map(
            await self.do_rpcrequest_async('CreateServerlessCluster', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DeleteGlobalResourceResponse().from_map(
            self.do_rpcrequest('DeleteGlobalResource', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_global_resource_with_options_async(
        self,
        request: hbase_20190101_models.DeleteGlobalResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DeleteGlobalResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DeleteGlobalResourceResponse().from_map(
            await self.do_rpcrequest_async('DeleteGlobalResource', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DeleteHBaseHaDBResponse().from_map(
            self.do_rpcrequest('DeleteHBaseHaDB', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_hbase_ha_dbwith_options_async(
        self,
        request: hbase_20190101_models.DeleteHBaseHaDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DeleteHBaseHaDBResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DeleteHBaseHaDBResponse().from_map(
            await self.do_rpcrequest_async('DeleteHBaseHaDB', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_hbase_ha_slb_with_options(
        self,
        request: hbase_20190101_models.DeleteHbaseHaSlbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DeleteHbaseHaSlbResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DeleteHbaseHaSlbResponse().from_map(
            self.do_rpcrequest('DeleteHbaseHaSlb', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_hbase_ha_slb_with_options_async(
        self,
        request: hbase_20190101_models.DeleteHbaseHaSlbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DeleteHbaseHaSlbResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DeleteHbaseHaSlbResponse().from_map(
            await self.do_rpcrequest_async('DeleteHbaseHaSlb', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_hbase_slb_server_with_options(
        self,
        request: hbase_20190101_models.DeleteHBaseSlbServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DeleteHBaseSlbServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DeleteHBaseSlbServerResponse().from_map(
            self.do_rpcrequest('DeleteHBaseSlbServer', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_hbase_slb_server_with_options_async(
        self,
        request: hbase_20190101_models.DeleteHBaseSlbServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DeleteHBaseSlbServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DeleteHBaseSlbServerResponse().from_map(
            await self.do_rpcrequest_async('DeleteHBaseSlbServer', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_instance_with_options(
        self,
        request: hbase_20190101_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DeleteInstanceResponse().from_map(
            self.do_rpcrequest('DeleteInstance', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: hbase_20190101_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DeleteInstanceResponse().from_map(
            await self.do_rpcrequest_async('DeleteInstance', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DeleteMultiZoneClusterResponse().from_map(
            self.do_rpcrequest('DeleteMultiZoneCluster', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_multi_zone_cluster_with_options_async(
        self,
        request: hbase_20190101_models.DeleteMultiZoneClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DeleteMultiZoneClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DeleteMultiZoneClusterResponse().from_map(
            await self.do_rpcrequest_async('DeleteMultiZoneCluster', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DeleteServerlessClusterResponse().from_map(
            self.do_rpcrequest('DeleteServerlessCluster', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_serverless_cluster_with_options_async(
        self,
        request: hbase_20190101_models.DeleteServerlessClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DeleteServerlessClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DeleteServerlessClusterResponse().from_map(
            await self.do_rpcrequest_async('DeleteServerlessCluster', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DeleteUserHdfsInfoResponse().from_map(
            self.do_rpcrequest('DeleteUserHdfsInfo', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_user_hdfs_info_with_options_async(
        self,
        request: hbase_20190101_models.DeleteUserHdfsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DeleteUserHdfsInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DeleteUserHdfsInfoResponse().from_map(
            await self.do_rpcrequest_async('DeleteUserHdfsInfo', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeAvailableResourceResponse().from_map(
            self.do_rpcrequest('DescribeAvailableResource', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_available_resource_with_options_async(
        self,
        request: hbase_20190101_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeAvailableResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeAvailableResourceResponse().from_map(
            await self.do_rpcrequest_async('DescribeAvailableResource', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeBackupPlanConfigResponse().from_map(
            self.do_rpcrequest('DescribeBackupPlanConfig', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_plan_config_with_options_async(
        self,
        request: hbase_20190101_models.DescribeBackupPlanConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeBackupPlanConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeBackupPlanConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeBackupPlanConfig', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeBackupPolicyResponse().from_map(
            self.do_rpcrequest('DescribeBackupPolicy', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_policy_with_options_async(
        self,
        request: hbase_20190101_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeBackupPolicyResponse().from_map(
            await self.do_rpcrequest_async('DescribeBackupPolicy', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_backups_with_options(
        self,
        request: hbase_20190101_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeBackupsResponse().from_map(
            self.do_rpcrequest('DescribeBackups', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backups_with_options_async(
        self,
        request: hbase_20190101_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeBackupsResponse().from_map(
            await self.do_rpcrequest_async('DescribeBackups', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_backup_status_with_options(
        self,
        request: hbase_20190101_models.DescribeBackupStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeBackupStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeBackupStatusResponse().from_map(
            self.do_rpcrequest('DescribeBackupStatus', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_status_with_options_async(
        self,
        request: hbase_20190101_models.DescribeBackupStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeBackupStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeBackupStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeBackupStatus', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeBackupSummaryResponse().from_map(
            self.do_rpcrequest('DescribeBackupSummary', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_summary_with_options_async(
        self,
        request: hbase_20190101_models.DescribeBackupSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeBackupSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeBackupSummaryResponse().from_map(
            await self.do_rpcrequest_async('DescribeBackupSummary', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeBackupTablesResponse().from_map(
            self.do_rpcrequest('DescribeBackupTables', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_tables_with_options_async(
        self,
        request: hbase_20190101_models.DescribeBackupTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeBackupTablesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeBackupTablesResponse().from_map(
            await self.do_rpcrequest_async('DescribeBackupTables', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_cluster_connection_with_options(
        self,
        request: hbase_20190101_models.DescribeClusterConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeClusterConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeClusterConnectionResponse().from_map(
            self.do_rpcrequest('DescribeClusterConnection', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cluster_connection_with_options_async(
        self,
        request: hbase_20190101_models.DescribeClusterConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeClusterConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeClusterConnectionResponse().from_map(
            await self.do_rpcrequest_async('DescribeClusterConnection', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeColdStorageResponse().from_map(
            self.do_rpcrequest('DescribeColdStorage', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cold_storage_with_options_async(
        self,
        request: hbase_20190101_models.DescribeColdStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeColdStorageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeColdStorageResponse().from_map(
            await self.do_rpcrequest_async('DescribeColdStorage', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeDBInstanceUsageResponse().from_map(
            self.do_rpcrequest('DescribeDBInstanceUsage', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_usage_with_options_async(
        self,
        request: hbase_20190101_models.DescribeDBInstanceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeDBInstanceUsageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeDBInstanceUsageResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBInstanceUsage', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeDeletedInstancesResponse().from_map(
            self.do_rpcrequest('DescribeDeletedInstances', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_deleted_instances_with_options_async(
        self,
        request: hbase_20190101_models.DescribeDeletedInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeDeletedInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeDeletedInstancesResponse().from_map(
            await self.do_rpcrequest_async('DescribeDeletedInstances', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeDiskWarningLineResponse().from_map(
            self.do_rpcrequest('DescribeDiskWarningLine', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_disk_warning_line_with_options_async(
        self,
        request: hbase_20190101_models.DescribeDiskWarningLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeDiskWarningLineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeDiskWarningLineResponse().from_map(
            await self.do_rpcrequest_async('DescribeDiskWarningLine', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeEndpointsResponse().from_map(
            self.do_rpcrequest('DescribeEndpoints', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_endpoints_with_options_async(
        self,
        request: hbase_20190101_models.DescribeEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeEndpointsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeEndpointsResponse().from_map(
            await self.do_rpcrequest_async('DescribeEndpoints', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeInstanceResponse().from_map(
            self.do_rpcrequest('DescribeInstance', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_with_options_async(
        self,
        request: hbase_20190101_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeInstanceResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstance', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_instances_with_options(
        self,
        request: hbase_20190101_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeInstancesResponse().from_map(
            self.do_rpcrequest('DescribeInstances', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: hbase_20190101_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeInstancesResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstances', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_instance_type_with_options(
        self,
        request: hbase_20190101_models.DescribeInstanceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeInstanceTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeInstanceTypeResponse().from_map(
            self.do_rpcrequest('DescribeInstanceType', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_type_with_options_async(
        self,
        request: hbase_20190101_models.DescribeInstanceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeInstanceTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeInstanceTypeResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceType', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_ip_whitelist_with_options(
        self,
        request: hbase_20190101_models.DescribeIpWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeIpWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeIpWhitelistResponse().from_map(
            self.do_rpcrequest('DescribeIpWhitelist', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ip_whitelist_with_options_async(
        self,
        request: hbase_20190101_models.DescribeIpWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeIpWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeIpWhitelistResponse().from_map(
            await self.do_rpcrequest_async('DescribeIpWhitelist', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeMultiZoneAvailableRegionsResponse().from_map(
            self.do_rpcrequest('DescribeMultiZoneAvailableRegions', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_multi_zone_available_regions_with_options_async(
        self,
        request: hbase_20190101_models.DescribeMultiZoneAvailableRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeMultiZoneAvailableRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeMultiZoneAvailableRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeMultiZoneAvailableRegions', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeMultiZoneAvailableResourceResponse().from_map(
            self.do_rpcrequest('DescribeMultiZoneAvailableResource', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_multi_zone_available_resource_with_options_async(
        self,
        request: hbase_20190101_models.DescribeMultiZoneAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeMultiZoneAvailableResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeMultiZoneAvailableResourceResponse().from_map(
            await self.do_rpcrequest_async('DescribeMultiZoneAvailableResource', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeMultiZoneClusterResponse().from_map(
            self.do_rpcrequest('DescribeMultiZoneCluster', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_multi_zone_cluster_with_options_async(
        self,
        request: hbase_20190101_models.DescribeMultiZoneClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeMultiZoneClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeMultiZoneClusterResponse().from_map(
            await self.do_rpcrequest_async('DescribeMultiZoneCluster', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeRecoverableTimeRangeResponse().from_map(
            self.do_rpcrequest('DescribeRecoverableTimeRange', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_recoverable_time_range_with_options_async(
        self,
        request: hbase_20190101_models.DescribeRecoverableTimeRangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeRecoverableTimeRangeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeRecoverableTimeRangeResponse().from_map(
            await self.do_rpcrequest_async('DescribeRecoverableTimeRange', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: hbase_20190101_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRegions', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeRestoreFullDetailsResponse().from_map(
            self.do_rpcrequest('DescribeRestoreFullDetails', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_restore_full_details_with_options_async(
        self,
        request: hbase_20190101_models.DescribeRestoreFullDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeRestoreFullDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeRestoreFullDetailsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRestoreFullDetails', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeRestoreIncrDetailResponse().from_map(
            self.do_rpcrequest('DescribeRestoreIncrDetail', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_restore_incr_detail_with_options_async(
        self,
        request: hbase_20190101_models.DescribeRestoreIncrDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeRestoreIncrDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeRestoreIncrDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribeRestoreIncrDetail', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeRestoreSchemaDetailsResponse().from_map(
            self.do_rpcrequest('DescribeRestoreSchemaDetails', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_restore_schema_details_with_options_async(
        self,
        request: hbase_20190101_models.DescribeRestoreSchemaDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeRestoreSchemaDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeRestoreSchemaDetailsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRestoreSchemaDetails', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeRestoreSummaryResponse().from_map(
            self.do_rpcrequest('DescribeRestoreSummary', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_restore_summary_with_options_async(
        self,
        request: hbase_20190101_models.DescribeRestoreSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeRestoreSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeRestoreSummaryResponse().from_map(
            await self.do_rpcrequest_async('DescribeRestoreSummary', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeRestoreTablesResponse().from_map(
            self.do_rpcrequest('DescribeRestoreTables', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_restore_tables_with_options_async(
        self,
        request: hbase_20190101_models.DescribeRestoreTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeRestoreTablesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeRestoreTablesResponse().from_map(
            await self.do_rpcrequest_async('DescribeRestoreTables', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeSecurityGroupsResponse().from_map(
            self.do_rpcrequest('DescribeSecurityGroups', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_security_groups_with_options_async(
        self,
        request: hbase_20190101_models.DescribeSecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeSecurityGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeSecurityGroupsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSecurityGroups', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_sub_domain_with_options(
        self,
        request: hbase_20190101_models.DescribeSubDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeSubDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeSubDomainResponse().from_map(
            self.do_rpcrequest('DescribeSubDomain', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sub_domain_with_options_async(
        self,
        request: hbase_20190101_models.DescribeSubDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.DescribeSubDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.DescribeSubDomainResponse().from_map(
            await self.do_rpcrequest_async('DescribeSubDomain', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.EnableHBaseueBackupResponse().from_map(
            self.do_rpcrequest('EnableHBaseueBackup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_hbaseue_backup_with_options_async(
        self,
        request: hbase_20190101_models.EnableHBaseueBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.EnableHBaseueBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.EnableHBaseueBackupResponse().from_map(
            await self.do_rpcrequest_async('EnableHBaseueBackup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.EnableHBaseueModuleResponse().from_map(
            self.do_rpcrequest('EnableHBaseueModule', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_hbaseue_module_with_options_async(
        self,
        request: hbase_20190101_models.EnableHBaseueModuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.EnableHBaseueModuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.EnableHBaseueModuleResponse().from_map(
            await self.do_rpcrequest_async('EnableHBaseueModule', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.EvaluateMultiZoneResourceResponse().from_map(
            self.do_rpcrequest('EvaluateMultiZoneResource', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def evaluate_multi_zone_resource_with_options_async(
        self,
        request: hbase_20190101_models.EvaluateMultiZoneResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.EvaluateMultiZoneResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.EvaluateMultiZoneResourceResponse().from_map(
            await self.do_rpcrequest_async('EvaluateMultiZoneResource', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.GetMultimodeCmsUrlResponse().from_map(
            self.do_rpcrequest('GetMultimodeCmsUrl', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_multimode_cms_url_with_options_async(
        self,
        request: hbase_20190101_models.GetMultimodeCmsUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.GetMultimodeCmsUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.GetMultimodeCmsUrlResponse().from_map(
            await self.do_rpcrequest_async('GetMultimodeCmsUrl', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ListHBaseInstancesResponse().from_map(
            self.do_rpcrequest('ListHBaseInstances', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_hbase_instances_with_options_async(
        self,
        request: hbase_20190101_models.ListHBaseInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ListHBaseInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ListHBaseInstancesResponse().from_map(
            await self.do_rpcrequest_async('ListHBaseInstances', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ListInstanceServiceConfigHistoriesResponse().from_map(
            self.do_rpcrequest('ListInstanceServiceConfigHistories', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_instance_service_config_histories_with_options_async(
        self,
        request: hbase_20190101_models.ListInstanceServiceConfigHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ListInstanceServiceConfigHistoriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ListInstanceServiceConfigHistoriesResponse().from_map(
            await self.do_rpcrequest_async('ListInstanceServiceConfigHistories', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ListInstanceServiceConfigurationsResponse().from_map(
            self.do_rpcrequest('ListInstanceServiceConfigurations', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_instance_service_configurations_with_options_async(
        self,
        request: hbase_20190101_models.ListInstanceServiceConfigurationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ListInstanceServiceConfigurationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ListInstanceServiceConfigurationsResponse().from_map(
            await self.do_rpcrequest_async('ListInstanceServiceConfigurations', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ListTagResourcesResponse().from_map(
            self.do_rpcrequest('ListTagResources', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: hbase_20190101_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ListTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('ListTagResources', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ListTagsResponse().from_map(
            self.do_rpcrequest('ListTags', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tags_with_options_async(
        self,
        request: hbase_20190101_models.ListTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ListTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ListTagsResponse().from_map(
            await self.do_rpcrequest_async('ListTags', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ModifyBackupPlanConfigResponse().from_map(
            self.do_rpcrequest('ModifyBackupPlanConfig', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_backup_plan_config_with_options_async(
        self,
        request: hbase_20190101_models.ModifyBackupPlanConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyBackupPlanConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ModifyBackupPlanConfigResponse().from_map(
            await self.do_rpcrequest_async('ModifyBackupPlanConfig', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ModifyBackupPolicyResponse().from_map(
            self.do_rpcrequest('ModifyBackupPolicy', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_backup_policy_with_options_async(
        self,
        request: hbase_20190101_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ModifyBackupPolicyResponse().from_map(
            await self.do_rpcrequest_async('ModifyBackupPolicy', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ModifyClusterDeletionProtectionResponse().from_map(
            self.do_rpcrequest('ModifyClusterDeletionProtection', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_cluster_deletion_protection_with_options_async(
        self,
        request: hbase_20190101_models.ModifyClusterDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyClusterDeletionProtectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ModifyClusterDeletionProtectionResponse().from_map(
            await self.do_rpcrequest_async('ModifyClusterDeletionProtection', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ModifyDiskWarningLineResponse().from_map(
            self.do_rpcrequest('ModifyDiskWarningLine', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_disk_warning_line_with_options_async(
        self,
        request: hbase_20190101_models.ModifyDiskWarningLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyDiskWarningLineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ModifyDiskWarningLineResponse().from_map(
            await self.do_rpcrequest_async('ModifyDiskWarningLine', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ModifyInstanceMaintainTimeResponse().from_map(
            self.do_rpcrequest('ModifyInstanceMaintainTime', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_maintain_time_with_options_async(
        self,
        request: hbase_20190101_models.ModifyInstanceMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyInstanceMaintainTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ModifyInstanceMaintainTimeResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceMaintainTime', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ModifyInstanceNameResponse().from_map(
            self.do_rpcrequest('ModifyInstanceName', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_name_with_options_async(
        self,
        request: hbase_20190101_models.ModifyInstanceNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyInstanceNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ModifyInstanceNameResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceName', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ModifyInstanceServiceConfigResponse().from_map(
            self.do_rpcrequest('ModifyInstanceServiceConfig', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_service_config_with_options_async(
        self,
        request: hbase_20190101_models.ModifyInstanceServiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyInstanceServiceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ModifyInstanceServiceConfigResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceServiceConfig', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ModifyInstanceTypeResponse().from_map(
            self.do_rpcrequest('ModifyInstanceType', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_type_with_options_async(
        self,
        request: hbase_20190101_models.ModifyInstanceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyInstanceTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ModifyInstanceTypeResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceType', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ModifyIpWhitelistResponse().from_map(
            self.do_rpcrequest('ModifyIpWhitelist', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_ip_whitelist_with_options_async(
        self,
        request: hbase_20190101_models.ModifyIpWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyIpWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ModifyIpWhitelistResponse().from_map(
            await self.do_rpcrequest_async('ModifyIpWhitelist', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ModifyMultiZoneClusterNodeTypeResponse().from_map(
            self.do_rpcrequest('ModifyMultiZoneClusterNodeType', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_multi_zone_cluster_node_type_with_options_async(
        self,
        request: hbase_20190101_models.ModifyMultiZoneClusterNodeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyMultiZoneClusterNodeTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ModifyMultiZoneClusterNodeTypeResponse().from_map(
            await self.do_rpcrequest_async('ModifyMultiZoneClusterNodeType', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ModifySecurityGroupsResponse().from_map(
            self.do_rpcrequest('ModifySecurityGroups', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_security_groups_with_options_async(
        self,
        request: hbase_20190101_models.ModifySecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifySecurityGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ModifySecurityGroupsResponse().from_map(
            await self.do_rpcrequest_async('ModifySecurityGroups', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ModifyUIAccountPasswordResponse().from_map(
            self.do_rpcrequest('ModifyUIAccountPassword', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_uiaccount_password_with_options_async(
        self,
        request: hbase_20190101_models.ModifyUIAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ModifyUIAccountPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ModifyUIAccountPasswordResponse().from_map(
            await self.do_rpcrequest_async('ModifyUIAccountPassword', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.MoveResourceGroupResponse().from_map(
            self.do_rpcrequest('MoveResourceGroup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: hbase_20190101_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.MoveResourceGroupResponse().from_map(
            await self.do_rpcrequest_async('MoveResourceGroup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.OpenBackupResponse().from_map(
            self.do_rpcrequest('OpenBackup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def open_backup_with_options_async(
        self,
        request: hbase_20190101_models.OpenBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.OpenBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.OpenBackupResponse().from_map(
            await self.do_rpcrequest_async('OpenBackup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.PurgeInstanceResponse().from_map(
            self.do_rpcrequest('PurgeInstance', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def purge_instance_with_options_async(
        self,
        request: hbase_20190101_models.PurgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.PurgeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.PurgeInstanceResponse().from_map(
            await self.do_rpcrequest_async('PurgeInstance', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.QueryHBaseHaDBResponse().from_map(
            self.do_rpcrequest('QueryHBaseHaDB', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_hbase_ha_dbwith_options_async(
        self,
        request: hbase_20190101_models.QueryHBaseHaDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.QueryHBaseHaDBResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.QueryHBaseHaDBResponse().from_map(
            await self.do_rpcrequest_async('QueryHBaseHaDB', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.QueryXpackRelateDBResponse().from_map(
            self.do_rpcrequest('QueryXpackRelateDB', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_xpack_relate_dbwith_options_async(
        self,
        request: hbase_20190101_models.QueryXpackRelateDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.QueryXpackRelateDBResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.QueryXpackRelateDBResponse().from_map(
            await self.do_rpcrequest_async('QueryXpackRelateDB', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.RelateDbForHBaseHaResponse().from_map(
            self.do_rpcrequest('RelateDbForHBaseHa', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def relate_db_for_hbase_ha_with_options_async(
        self,
        request: hbase_20190101_models.RelateDbForHBaseHaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.RelateDbForHBaseHaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.RelateDbForHBaseHaResponse().from_map(
            await self.do_rpcrequest_async('RelateDbForHBaseHa', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ReleasePublicNetworkAddressResponse().from_map(
            self.do_rpcrequest('ReleasePublicNetworkAddress', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_public_network_address_with_options_async(
        self,
        request: hbase_20190101_models.ReleasePublicNetworkAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ReleasePublicNetworkAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ReleasePublicNetworkAddressResponse().from_map(
            await self.do_rpcrequest_async('ReleasePublicNetworkAddress', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.RenewInstanceResponse().from_map(
            self.do_rpcrequest('RenewInstance', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        request: hbase_20190101_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.RenewInstanceResponse().from_map(
            await self.do_rpcrequest_async('RenewInstance', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ResizeColdStorageSizeResponse().from_map(
            self.do_rpcrequest('ResizeColdStorageSize', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def resize_cold_storage_size_with_options_async(
        self,
        request: hbase_20190101_models.ResizeColdStorageSizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ResizeColdStorageSizeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ResizeColdStorageSizeResponse().from_map(
            await self.do_rpcrequest_async('ResizeColdStorageSize', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ResizeDiskSizeResponse().from_map(
            self.do_rpcrequest('ResizeDiskSize', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def resize_disk_size_with_options_async(
        self,
        request: hbase_20190101_models.ResizeDiskSizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ResizeDiskSizeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ResizeDiskSizeResponse().from_map(
            await self.do_rpcrequest_async('ResizeDiskSize', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ResizeMultiZoneClusterDiskSizeResponse().from_map(
            self.do_rpcrequest('ResizeMultiZoneClusterDiskSize', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def resize_multi_zone_cluster_disk_size_with_options_async(
        self,
        request: hbase_20190101_models.ResizeMultiZoneClusterDiskSizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ResizeMultiZoneClusterDiskSizeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ResizeMultiZoneClusterDiskSizeResponse().from_map(
            await self.do_rpcrequest_async('ResizeMultiZoneClusterDiskSize', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ResizeMultiZoneClusterNodeCountResponse().from_map(
            self.do_rpcrequest('ResizeMultiZoneClusterNodeCount', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def resize_multi_zone_cluster_node_count_with_options_async(
        self,
        request: hbase_20190101_models.ResizeMultiZoneClusterNodeCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ResizeMultiZoneClusterNodeCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ResizeMultiZoneClusterNodeCountResponse().from_map(
            await self.do_rpcrequest_async('ResizeMultiZoneClusterNodeCount', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ResizeNodeCountResponse().from_map(
            self.do_rpcrequest('ResizeNodeCount', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def resize_node_count_with_options_async(
        self,
        request: hbase_20190101_models.ResizeNodeCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.ResizeNodeCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.ResizeNodeCountResponse().from_map(
            await self.do_rpcrequest_async('ResizeNodeCount', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.RestartInstanceResponse().from_map(
            self.do_rpcrequest('RestartInstance', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def restart_instance_with_options_async(
        self,
        request: hbase_20190101_models.RestartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.RestartInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.RestartInstanceResponse().from_map(
            await self.do_rpcrequest_async('RestartInstance', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.SwitchHbaseHaSlbResponse().from_map(
            self.do_rpcrequest('SwitchHbaseHaSlb', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def switch_hbase_ha_slb_with_options_async(
        self,
        request: hbase_20190101_models.SwitchHbaseHaSlbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.SwitchHbaseHaSlbResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.SwitchHbaseHaSlbResponse().from_map(
            await self.do_rpcrequest_async('SwitchHbaseHaSlb', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.TagResourcesResponse().from_map(
            self.do_rpcrequest('TagResources', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: hbase_20190101_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.TagResourcesResponse().from_map(
            await self.do_rpcrequest_async('TagResources', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.UnTagResourcesResponse().from_map(
            self.do_rpcrequest('UnTagResources', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def un_tag_resources_with_options_async(
        self,
        request: hbase_20190101_models.UnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.UnTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.UnTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('UnTagResources', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.UpgradeMinorVersionResponse().from_map(
            self.do_rpcrequest('UpgradeMinorVersion', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_minor_version_with_options_async(
        self,
        request: hbase_20190101_models.UpgradeMinorVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.UpgradeMinorVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.UpgradeMinorVersionResponse().from_map(
            await self.do_rpcrequest_async('UpgradeMinorVersion', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.UpgradeMultiZoneClusterResponse().from_map(
            self.do_rpcrequest('UpgradeMultiZoneCluster', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_multi_zone_cluster_with_options_async(
        self,
        request: hbase_20190101_models.UpgradeMultiZoneClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.UpgradeMultiZoneClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.UpgradeMultiZoneClusterResponse().from_map(
            await self.do_rpcrequest_async('UpgradeMultiZoneCluster', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.XpackRelateDBResponse().from_map(
            self.do_rpcrequest('XpackRelateDB', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def xpack_relate_dbwith_options_async(
        self,
        request: hbase_20190101_models.XpackRelateDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hbase_20190101_models.XpackRelateDBResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hbase_20190101_models.XpackRelateDBResponse().from_map(
            await self.do_rpcrequest_async('XpackRelateDB', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
