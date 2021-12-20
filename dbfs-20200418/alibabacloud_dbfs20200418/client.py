# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dbfs20200418 import models as dbfs20200418_models
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
            'ap-northeast-2-pop': 'dbfs.aliyuncs.com',
            'cn-beijing-finance-1': 'dbfs.aliyuncs.com',
            'cn-beijing-finance-pop': 'dbfs.aliyuncs.com',
            'cn-beijing-gov-1': 'dbfs.aliyuncs.com',
            'cn-beijing-nu16-b01': 'dbfs.aliyuncs.com',
            'cn-edge-1': 'dbfs.aliyuncs.com',
            'cn-fujian': 'dbfs.aliyuncs.com',
            'cn-haidian-cm12-c01': 'dbfs.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'dbfs.aliyuncs.com',
            'cn-hangzhou-finance': 'dbfs.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'dbfs.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'dbfs.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'dbfs.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'dbfs.aliyuncs.com',
            'cn-hangzhou-test-306': 'dbfs.aliyuncs.com',
            'cn-hongkong-finance-pop': 'dbfs.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'dbfs.aliyuncs.com',
            'cn-north-2-gov-1': 'dbfs.aliyuncs.com',
            'cn-qingdao-nebula': 'dbfs.aliyuncs.com',
            'cn-shanghai-et15-b01': 'dbfs.aliyuncs.com',
            'cn-shanghai-et2-b01': 'dbfs.aliyuncs.com',
            'cn-shanghai-finance-1': 'dbfs.aliyuncs.com',
            'cn-shanghai-inner': 'dbfs.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'dbfs.aliyuncs.com',
            'cn-shenzhen-finance-1': 'dbfs.aliyuncs.com',
            'cn-shenzhen-inner': 'dbfs.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'dbfs.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'dbfs.aliyuncs.com',
            'cn-wuhan': 'dbfs.aliyuncs.com',
            'cn-wulanchabu': 'dbfs.aliyuncs.com',
            'cn-yushanfang': 'dbfs.aliyuncs.com',
            'cn-zhangbei': 'dbfs.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'dbfs.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'dbfs.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'dbfs.aliyuncs.com',
            'eu-west-1-oxs': 'dbfs.aliyuncs.com',
            'rus-west-1-pop': 'dbfs.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dbfs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_tags_batch_with_options(
        self,
        request: dbfs20200418_models.AddTagsBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.AddTagsBatchResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['DbfsList'] = request.dbfs_list
        query['RegionId'] = request.region_id
        query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTagsBatch',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.AddTagsBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_tags_batch_with_options_async(
        self,
        request: dbfs20200418_models.AddTagsBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.AddTagsBatchResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['DbfsList'] = request.dbfs_list
        query['RegionId'] = request.region_id
        query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTagsBatch',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.AddTagsBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_tags_batch(
        self,
        request: dbfs20200418_models.AddTagsBatchRequest,
    ) -> dbfs20200418_models.AddTagsBatchResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_tags_batch_with_options(request, runtime)

    async def add_tags_batch_async(
        self,
        request: dbfs20200418_models.AddTagsBatchRequest,
    ) -> dbfs20200418_models.AddTagsBatchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_tags_batch_with_options_async(request, runtime)

    def attach_dbfs_with_options(
        self,
        request: dbfs20200418_models.AttachDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.AttachDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AttachMode'] = request.attach_mode
        query['AttachPoint'] = request.attach_point
        query['ECSInstanceId'] = request.ecsinstance_id
        query['FsId'] = request.fs_id
        query['RegionId'] = request.region_id
        query['ServerUrl'] = request.server_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.AttachDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.AttachDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.AttachDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AttachMode'] = request.attach_mode
        query['AttachPoint'] = request.attach_point
        query['ECSInstanceId'] = request.ecsinstance_id
        query['FsId'] = request.fs_id
        query['RegionId'] = request.region_id
        query['ServerUrl'] = request.server_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.AttachDbfsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_dbfs(
        self,
        request: dbfs20200418_models.AttachDbfsRequest,
    ) -> dbfs20200418_models.AttachDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_dbfs_with_options(request, runtime)

    async def attach_dbfs_async(
        self,
        request: dbfs20200418_models.AttachDbfsRequest,
    ) -> dbfs20200418_models.AttachDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_dbfs_with_options_async(request, runtime)

    def create_dbfs_with_options(
        self,
        request: dbfs20200418_models.CreateDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.CreateDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Category'] = request.category
        query['ClientToken'] = request.client_token
        query['DeleteSnapshot'] = request.delete_snapshot
        query['EnableRaid'] = request.enable_raid
        query['Encryption'] = request.encryption
        query['FsName'] = request.fs_name
        query['InstanceType'] = request.instance_type
        query['KMSKeyId'] = request.kmskey_id
        query['PerformanceLevel'] = request.performance_level
        query['RaidStripeUnitNumber'] = request.raid_stripe_unit_number
        query['RegionId'] = request.region_id
        query['SizeG'] = request.size_g
        query['SnapshotId'] = request.snapshot_id
        query['UsedScene'] = request.used_scene
        query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.CreateDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.CreateDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.CreateDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Category'] = request.category
        query['ClientToken'] = request.client_token
        query['DeleteSnapshot'] = request.delete_snapshot
        query['EnableRaid'] = request.enable_raid
        query['Encryption'] = request.encryption
        query['FsName'] = request.fs_name
        query['InstanceType'] = request.instance_type
        query['KMSKeyId'] = request.kmskey_id
        query['PerformanceLevel'] = request.performance_level
        query['RaidStripeUnitNumber'] = request.raid_stripe_unit_number
        query['RegionId'] = request.region_id
        query['SizeG'] = request.size_g
        query['SnapshotId'] = request.snapshot_id
        query['UsedScene'] = request.used_scene
        query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.CreateDbfsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbfs(
        self,
        request: dbfs20200418_models.CreateDbfsRequest,
    ) -> dbfs20200418_models.CreateDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dbfs_with_options(request, runtime)

    async def create_dbfs_async(
        self,
        request: dbfs20200418_models.CreateDbfsRequest,
    ) -> dbfs20200418_models.CreateDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dbfs_with_options_async(request, runtime)

    def create_service_linked_role_with_options(
        self,
        request: dbfs20200418_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.CreateServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRole',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.CreateServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_linked_role_with_options_async(
        self,
        request: dbfs20200418_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.CreateServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRole',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.CreateServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_linked_role(
        self,
        request: dbfs20200418_models.CreateServiceLinkedRoleRequest,
    ) -> dbfs20200418_models.CreateServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    async def create_service_linked_role_async(
        self,
        request: dbfs20200418_models.CreateServiceLinkedRoleRequest,
    ) -> dbfs20200418_models.CreateServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_service_linked_role_with_options_async(request, runtime)

    def create_snapshot_with_options(
        self,
        request: dbfs20200418_models.CreateSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.CreateSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['Description'] = request.description
        query['FsId'] = request.fs_id
        query['RegionId'] = request.region_id
        query['RetentionDays'] = request.retention_days
        query['SnapshotName'] = request.snapshot_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSnapshot',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.CreateSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_snapshot_with_options_async(
        self,
        request: dbfs20200418_models.CreateSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.CreateSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['Description'] = request.description
        query['FsId'] = request.fs_id
        query['RegionId'] = request.region_id
        query['RetentionDays'] = request.retention_days
        query['SnapshotName'] = request.snapshot_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSnapshot',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.CreateSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_snapshot(
        self,
        request: dbfs20200418_models.CreateSnapshotRequest,
    ) -> dbfs20200418_models.CreateSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_snapshot_with_options(request, runtime)

    async def create_snapshot_async(
        self,
        request: dbfs20200418_models.CreateSnapshotRequest,
    ) -> dbfs20200418_models.CreateSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_snapshot_with_options_async(request, runtime)

    def delete_dbfs_with_options(
        self,
        request: dbfs20200418_models.DeleteDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DeleteDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FsId'] = request.fs_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DeleteDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.DeleteDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DeleteDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FsId'] = request.fs_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DeleteDbfsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbfs(
        self,
        request: dbfs20200418_models.DeleteDbfsRequest,
    ) -> dbfs20200418_models.DeleteDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dbfs_with_options(request, runtime)

    async def delete_dbfs_async(
        self,
        request: dbfs20200418_models.DeleteDbfsRequest,
    ) -> dbfs20200418_models.DeleteDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbfs_with_options_async(request, runtime)

    def delete_snapshot_with_options(
        self,
        request: dbfs20200418_models.DeleteSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DeleteSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Force'] = request.force
        query['RegionId'] = request.region_id
        query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshot',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DeleteSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_snapshot_with_options_async(
        self,
        request: dbfs20200418_models.DeleteSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DeleteSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Force'] = request.force
        query['RegionId'] = request.region_id
        query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshot',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DeleteSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_snapshot(
        self,
        request: dbfs20200418_models.DeleteSnapshotRequest,
    ) -> dbfs20200418_models.DeleteSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshot_with_options(request, runtime)

    async def delete_snapshot_async(
        self,
        request: dbfs20200418_models.DeleteSnapshotRequest,
    ) -> dbfs20200418_models.DeleteSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_snapshot_with_options_async(request, runtime)

    def delete_tags_batch_with_options(
        self,
        request: dbfs20200418_models.DeleteTagsBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DeleteTagsBatchResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbfsList'] = request.dbfs_list
        query['RegionId'] = request.region_id
        query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTagsBatch',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DeleteTagsBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tags_batch_with_options_async(
        self,
        request: dbfs20200418_models.DeleteTagsBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DeleteTagsBatchResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbfsList'] = request.dbfs_list
        query['RegionId'] = request.region_id
        query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTagsBatch',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DeleteTagsBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tags_batch(
        self,
        request: dbfs20200418_models.DeleteTagsBatchRequest,
    ) -> dbfs20200418_models.DeleteTagsBatchResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_tags_batch_with_options(request, runtime)

    async def delete_tags_batch_async(
        self,
        request: dbfs20200418_models.DeleteTagsBatchRequest,
    ) -> dbfs20200418_models.DeleteTagsBatchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_tags_batch_with_options_async(request, runtime)

    def describe_dbfs_specifications_with_options(
        self,
        request: dbfs20200418_models.DescribeDbfsSpecificationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DescribeDbfsSpecificationsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Category'] = request.category
        query['EcsInstanceType'] = request.ecs_instance_type
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDbfsSpecifications',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DescribeDbfsSpecificationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbfs_specifications_with_options_async(
        self,
        request: dbfs20200418_models.DescribeDbfsSpecificationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DescribeDbfsSpecificationsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Category'] = request.category
        query['EcsInstanceType'] = request.ecs_instance_type
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDbfsSpecifications',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DescribeDbfsSpecificationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbfs_specifications(
        self,
        request: dbfs20200418_models.DescribeDbfsSpecificationsRequest,
    ) -> dbfs20200418_models.DescribeDbfsSpecificationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbfs_specifications_with_options(request, runtime)

    async def describe_dbfs_specifications_async(
        self,
        request: dbfs20200418_models.DescribeDbfsSpecificationsRequest,
    ) -> dbfs20200418_models.DescribeDbfsSpecificationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbfs_specifications_with_options_async(request, runtime)

    def describe_instance_types_with_options(
        self,
        request: dbfs20200418_models.DescribeInstanceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DescribeInstanceTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceTypes',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DescribeInstanceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_types_with_options_async(
        self,
        request: dbfs20200418_models.DescribeInstanceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DescribeInstanceTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceTypes',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DescribeInstanceTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_types(
        self,
        request: dbfs20200418_models.DescribeInstanceTypesRequest,
    ) -> dbfs20200418_models.DescribeInstanceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_types_with_options(request, runtime)

    async def describe_instance_types_async(
        self,
        request: dbfs20200418_models.DescribeInstanceTypesRequest,
    ) -> dbfs20200418_models.DescribeInstanceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_types_with_options_async(request, runtime)

    def detach_dbfs_with_options(
        self,
        request: dbfs20200418_models.DetachDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DetachDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ECSInstanceId'] = request.ecsinstance_id
        query['FsId'] = request.fs_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DetachDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.DetachDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DetachDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ECSInstanceId'] = request.ecsinstance_id
        query['FsId'] = request.fs_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DetachDbfsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_dbfs(
        self,
        request: dbfs20200418_models.DetachDbfsRequest,
    ) -> dbfs20200418_models.DetachDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_dbfs_with_options(request, runtime)

    async def detach_dbfs_async(
        self,
        request: dbfs20200418_models.DetachDbfsRequest,
    ) -> dbfs20200418_models.DetachDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_dbfs_with_options_async(request, runtime)

    def get_dbfs_with_options(
        self,
        request: dbfs20200418_models.GetDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.GetDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FsId'] = request.fs_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.GetDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.GetDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.GetDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FsId'] = request.fs_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.GetDbfsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dbfs(
        self,
        request: dbfs20200418_models.GetDbfsRequest,
    ) -> dbfs20200418_models.GetDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_dbfs_with_options(request, runtime)

    async def get_dbfs_async(
        self,
        request: dbfs20200418_models.GetDbfsRequest,
    ) -> dbfs20200418_models.GetDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_dbfs_with_options_async(request, runtime)

    def get_service_linked_role_with_options(
        self,
        request: dbfs20200418_models.GetServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.GetServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceLinkedRole',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.GetServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_linked_role_with_options_async(
        self,
        request: dbfs20200418_models.GetServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.GetServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceLinkedRole',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.GetServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_linked_role(
        self,
        request: dbfs20200418_models.GetServiceLinkedRoleRequest,
    ) -> dbfs20200418_models.GetServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_service_linked_role_with_options(request, runtime)

    async def get_service_linked_role_async(
        self,
        request: dbfs20200418_models.GetServiceLinkedRoleRequest,
    ) -> dbfs20200418_models.GetServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_service_linked_role_with_options_async(request, runtime)

    def list_dbfs_with_options(
        self,
        request: dbfs20200418_models.ListDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FilterKey'] = request.filter_key
        query['FilterValue'] = request.filter_value
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['SortKey'] = request.sort_key
        query['SortType'] = request.sort_type
        query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.ListDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FilterKey'] = request.filter_key
        query['FilterValue'] = request.filter_value
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['SortKey'] = request.sort_key
        query['SortType'] = request.sort_type
        query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListDbfsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dbfs(
        self,
        request: dbfs20200418_models.ListDbfsRequest,
    ) -> dbfs20200418_models.ListDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dbfs_with_options(request, runtime)

    async def list_dbfs_async(
        self,
        request: dbfs20200418_models.ListDbfsRequest,
    ) -> dbfs20200418_models.ListDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dbfs_with_options_async(request, runtime)

    def list_dbfs_attachable_ecs_instances_with_options(
        self,
        request: dbfs20200418_models.ListDbfsAttachableEcsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListDbfsAttachableEcsInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDbfsAttachableEcsInstances',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListDbfsAttachableEcsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dbfs_attachable_ecs_instances_with_options_async(
        self,
        request: dbfs20200418_models.ListDbfsAttachableEcsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListDbfsAttachableEcsInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDbfsAttachableEcsInstances',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListDbfsAttachableEcsInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dbfs_attachable_ecs_instances(
        self,
        request: dbfs20200418_models.ListDbfsAttachableEcsInstancesRequest,
    ) -> dbfs20200418_models.ListDbfsAttachableEcsInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dbfs_attachable_ecs_instances_with_options(request, runtime)

    async def list_dbfs_attachable_ecs_instances_async(
        self,
        request: dbfs20200418_models.ListDbfsAttachableEcsInstancesRequest,
    ) -> dbfs20200418_models.ListDbfsAttachableEcsInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dbfs_attachable_ecs_instances_with_options_async(request, runtime)

    def list_dbfs_attached_ecs_instances_with_options(
        self,
        request: dbfs20200418_models.ListDbfsAttachedEcsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListDbfsAttachedEcsInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FsId'] = request.fs_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDbfsAttachedEcsInstances',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListDbfsAttachedEcsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dbfs_attached_ecs_instances_with_options_async(
        self,
        request: dbfs20200418_models.ListDbfsAttachedEcsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListDbfsAttachedEcsInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FsId'] = request.fs_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDbfsAttachedEcsInstances',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListDbfsAttachedEcsInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dbfs_attached_ecs_instances(
        self,
        request: dbfs20200418_models.ListDbfsAttachedEcsInstancesRequest,
    ) -> dbfs20200418_models.ListDbfsAttachedEcsInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dbfs_attached_ecs_instances_with_options(request, runtime)

    async def list_dbfs_attached_ecs_instances_async(
        self,
        request: dbfs20200418_models.ListDbfsAttachedEcsInstancesRequest,
    ) -> dbfs20200418_models.ListDbfsAttachedEcsInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dbfs_attached_ecs_instances_with_options_async(request, runtime)

    def list_snapshot_with_options(
        self,
        request: dbfs20200418_models.ListSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FilterKey'] = request.filter_key
        query['FilterValue'] = request.filter_value
        query['FsId'] = request.fs_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['SnapshotIds'] = request.snapshot_ids
        query['SnapshotName'] = request.snapshot_name
        query['SnapshotType'] = request.snapshot_type
        query['SortKey'] = request.sort_key
        query['SortType'] = request.sort_type
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSnapshot',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_snapshot_with_options_async(
        self,
        request: dbfs20200418_models.ListSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FilterKey'] = request.filter_key
        query['FilterValue'] = request.filter_value
        query['FsId'] = request.fs_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['SnapshotIds'] = request.snapshot_ids
        query['SnapshotName'] = request.snapshot_name
        query['SnapshotType'] = request.snapshot_type
        query['SortKey'] = request.sort_key
        query['SortType'] = request.sort_type
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSnapshot',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_snapshot(
        self,
        request: dbfs20200418_models.ListSnapshotRequest,
    ) -> dbfs20200418_models.ListSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_snapshot_with_options(request, runtime)

    async def list_snapshot_async(
        self,
        request: dbfs20200418_models.ListSnapshotRequest,
    ) -> dbfs20200418_models.ListSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_snapshot_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: dbfs20200418_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: dbfs20200418_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_keys(
        self,
        request: dbfs20200418_models.ListTagKeysRequest,
    ) -> dbfs20200418_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: dbfs20200418_models.ListTagKeysRequest,
    ) -> dbfs20200418_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: dbfs20200418_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: dbfs20200418_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_values(
        self,
        request: dbfs20200418_models.ListTagValuesRequest,
    ) -> dbfs20200418_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: dbfs20200418_models.ListTagValuesRequest,
    ) -> dbfs20200418_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def rename_dbfs_with_options(
        self,
        request: dbfs20200418_models.RenameDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.RenameDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FsId'] = request.fs_id
        query['FsName'] = request.fs_name
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenameDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.RenameDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    async def rename_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.RenameDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.RenameDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FsId'] = request.fs_id
        query['FsName'] = request.fs_name
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenameDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.RenameDbfsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rename_dbfs(
        self,
        request: dbfs20200418_models.RenameDbfsRequest,
    ) -> dbfs20200418_models.RenameDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return self.rename_dbfs_with_options(request, runtime)

    async def rename_dbfs_async(
        self,
        request: dbfs20200418_models.RenameDbfsRequest,
    ) -> dbfs20200418_models.RenameDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rename_dbfs_with_options_async(request, runtime)

    def reset_dbfs_with_options(
        self,
        request: dbfs20200418_models.ResetDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ResetDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FsId'] = request.fs_id
        query['RegionId'] = request.region_id
        query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ResetDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.ResetDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ResetDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FsId'] = request.fs_id
        query['RegionId'] = request.region_id
        query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ResetDbfsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_dbfs(
        self,
        request: dbfs20200418_models.ResetDbfsRequest,
    ) -> dbfs20200418_models.ResetDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_dbfs_with_options(request, runtime)

    async def reset_dbfs_async(
        self,
        request: dbfs20200418_models.ResetDbfsRequest,
    ) -> dbfs20200418_models.ResetDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_dbfs_with_options_async(request, runtime)

    def resize_dbfs_with_options(
        self,
        request: dbfs20200418_models.ResizeDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ResizeDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FsId'] = request.fs_id
        query['NewSizeG'] = request.new_size_g
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResizeDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ResizeDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    async def resize_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.ResizeDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ResizeDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FsId'] = request.fs_id
        query['NewSizeG'] = request.new_size_g
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResizeDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ResizeDbfsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resize_dbfs(
        self,
        request: dbfs20200418_models.ResizeDbfsRequest,
    ) -> dbfs20200418_models.ResizeDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return self.resize_dbfs_with_options(request, runtime)

    async def resize_dbfs_async(
        self,
        request: dbfs20200418_models.ResizeDbfsRequest,
    ) -> dbfs20200418_models.ResizeDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resize_dbfs_with_options_async(request, runtime)

    def tag_dbfs_with_options(
        self,
        request: dbfs20200418_models.TagDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.TagDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbfsId'] = request.dbfs_id
        query['RegionId'] = request.region_id
        query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.TagDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.TagDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.TagDbfsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbfsId'] = request.dbfs_id
        query['RegionId'] = request.region_id
        query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.TagDbfsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_dbfs(
        self,
        request: dbfs20200418_models.TagDbfsRequest,
    ) -> dbfs20200418_models.TagDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_dbfs_with_options(request, runtime)

    async def tag_dbfs_async(
        self,
        request: dbfs20200418_models.TagDbfsRequest,
    ) -> dbfs20200418_models.TagDbfsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_dbfs_with_options_async(request, runtime)
