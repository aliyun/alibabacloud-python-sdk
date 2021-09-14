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

    def create_constants_with_options(
        self,
        request: dbfs20200418_models.CreateConstantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.CreateConstantsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.CreateConstantsResponse(),
            self.do_rpcrequest('CreateConstants', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_constants_with_options_async(
        self,
        request: dbfs20200418_models.CreateConstantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.CreateConstantsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.CreateConstantsResponse(),
            await self.do_rpcrequest_async('CreateConstants', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_constants(
        self,
        request: dbfs20200418_models.CreateConstantsRequest,
    ) -> dbfs20200418_models.CreateConstantsResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_constants_with_options(request, runtime)

    async def create_constants_async(
        self,
        request: dbfs20200418_models.CreateConstantsRequest,
    ) -> dbfs20200418_models.CreateConstantsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_constants_with_options_async(request, runtime)

    def delete_dbfs_with_options(
        self,
        request: dbfs20200418_models.DeleteDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DeleteDbfsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.DeleteDbfsResponse(),
            self.do_rpcrequest('DeleteDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.DeleteDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DeleteDbfsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.DeleteDbfsResponse(),
            await self.do_rpcrequest_async('DeleteDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_constants_with_options(
        self,
        request: dbfs20200418_models.DeleteConstantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DeleteConstantsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.DeleteConstantsResponse(),
            self.do_rpcrequest('DeleteConstants', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_constants_with_options_async(
        self,
        request: dbfs20200418_models.DeleteConstantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DeleteConstantsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.DeleteConstantsResponse(),
            await self.do_rpcrequest_async('DeleteConstants', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_constants(
        self,
        request: dbfs20200418_models.DeleteConstantsRequest,
    ) -> dbfs20200418_models.DeleteConstantsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_constants_with_options(request, runtime)

    async def delete_constants_async(
        self,
        request: dbfs20200418_models.DeleteConstantsRequest,
    ) -> dbfs20200418_models.DeleteConstantsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_constants_with_options_async(request, runtime)

    def create_service_linked_role_with_options(
        self,
        request: dbfs20200418_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.CreateServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.CreateServiceLinkedRoleResponse(),
            self.do_rpcrequest('CreateServiceLinkedRole', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_service_linked_role_with_options_async(
        self,
        request: dbfs20200418_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.CreateServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.CreateServiceLinkedRoleResponse(),
            await self.do_rpcrequest_async('CreateServiceLinkedRole', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def resize_dbfs_with_options(
        self,
        request: dbfs20200418_models.ResizeDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ResizeDbfsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.ResizeDbfsResponse(),
            self.do_rpcrequest('ResizeDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def resize_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.ResizeDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ResizeDbfsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.ResizeDbfsResponse(),
            await self.do_rpcrequest_async('ResizeDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def publish_upgrade_task_with_options(
        self,
        request: dbfs20200418_models.PublishUpgradeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.PublishUpgradeTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.PublishUpgradeTaskResponse(),
            self.do_rpcrequest('PublishUpgradeTask', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def publish_upgrade_task_with_options_async(
        self,
        request: dbfs20200418_models.PublishUpgradeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.PublishUpgradeTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.PublishUpgradeTaskResponse(),
            await self.do_rpcrequest_async('PublishUpgradeTask', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_upgrade_task(
        self,
        request: dbfs20200418_models.PublishUpgradeTaskRequest,
    ) -> dbfs20200418_models.PublishUpgradeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_upgrade_task_with_options(request, runtime)

    async def publish_upgrade_task_async(
        self,
        request: dbfs20200418_models.PublishUpgradeTaskRequest,
    ) -> dbfs20200418_models.PublishUpgradeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_upgrade_task_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: dbfs20200418_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListTagValuesResponse(),
            self.do_rpcrequest('ListTagValues', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: dbfs20200418_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListTagValuesResponse(),
            await self.do_rpcrequest_async('ListTagValues', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_snapshot_with_options(
        self,
        request: dbfs20200418_models.DeleteSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DeleteSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.DeleteSnapshotResponse(),
            self.do_rpcrequest('DeleteSnapshot', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_snapshot_with_options_async(
        self,
        request: dbfs20200418_models.DeleteSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DeleteSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.DeleteSnapshotResponse(),
            await self.do_rpcrequest_async('DeleteSnapshot', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def detach_dbfs_with_options(
        self,
        request: dbfs20200418_models.DetachDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DetachDbfsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.DetachDbfsResponse(),
            self.do_rpcrequest('DetachDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.DetachDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DetachDbfsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.DetachDbfsResponse(),
            await self.do_rpcrequest_async('DetachDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def generate_upgrade_record_with_options(
        self,
        request: dbfs20200418_models.GenerateUpgradeRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.GenerateUpgradeRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.GenerateUpgradeRecordResponse(),
            self.do_rpcrequest('GenerateUpgradeRecord', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_upgrade_record_with_options_async(
        self,
        request: dbfs20200418_models.GenerateUpgradeRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.GenerateUpgradeRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.GenerateUpgradeRecordResponse(),
            await self.do_rpcrequest_async('GenerateUpgradeRecord', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_upgrade_record(
        self,
        request: dbfs20200418_models.GenerateUpgradeRecordRequest,
    ) -> dbfs20200418_models.GenerateUpgradeRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_upgrade_record_with_options(request, runtime)

    async def generate_upgrade_record_async(
        self,
        request: dbfs20200418_models.GenerateUpgradeRecordRequest,
    ) -> dbfs20200418_models.GenerateUpgradeRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_upgrade_record_with_options_async(request, runtime)

    def reset_dbfs_with_options(
        self,
        request: dbfs20200418_models.ResetDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ResetDbfsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.ResetDbfsResponse(),
            self.do_rpcrequest('ResetDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.ResetDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ResetDbfsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.ResetDbfsResponse(),
            await self.do_rpcrequest_async('ResetDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_dbfs_with_options(
        self,
        request: dbfs20200418_models.GetDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.GetDbfsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.GetDbfsResponse(),
            self.do_rpcrequest('GetDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.GetDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.GetDbfsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.GetDbfsResponse(),
            await self.do_rpcrequest_async('GetDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def dbfs_record_with_options(
        self,
        request: dbfs20200418_models.DbfsRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DbfsRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.DbfsRecordResponse(),
            self.do_rpcrequest('DbfsRecord', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def dbfs_record_with_options_async(
        self,
        request: dbfs20200418_models.DbfsRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DbfsRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.DbfsRecordResponse(),
            await self.do_rpcrequest_async('DbfsRecord', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def dbfs_record(
        self,
        request: dbfs20200418_models.DbfsRecordRequest,
    ) -> dbfs20200418_models.DbfsRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.dbfs_record_with_options(request, runtime)

    async def dbfs_record_async(
        self,
        request: dbfs20200418_models.DbfsRecordRequest,
    ) -> dbfs20200418_models.DbfsRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dbfs_record_with_options_async(request, runtime)

    def stop_upgrade_task_with_options(
        self,
        request: dbfs20200418_models.StopUpgradeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.StopUpgradeTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.StopUpgradeTaskResponse(),
            self.do_rpcrequest('StopUpgradeTask', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_upgrade_task_with_options_async(
        self,
        request: dbfs20200418_models.StopUpgradeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.StopUpgradeTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.StopUpgradeTaskResponse(),
            await self.do_rpcrequest_async('StopUpgradeTask', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_upgrade_task(
        self,
        request: dbfs20200418_models.StopUpgradeTaskRequest,
    ) -> dbfs20200418_models.StopUpgradeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_upgrade_task_with_options(request, runtime)

    async def stop_upgrade_task_async(
        self,
        request: dbfs20200418_models.StopUpgradeTaskRequest,
    ) -> dbfs20200418_models.StopUpgradeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_upgrade_task_with_options_async(request, runtime)

    def create_dbfs_with_options(
        self,
        request: dbfs20200418_models.CreateDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.CreateDbfsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.CreateDbfsResponse(),
            self.do_rpcrequest('CreateDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.CreateDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.CreateDbfsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.CreateDbfsResponse(),
            await self.do_rpcrequest_async('CreateDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_task_with_options(
        self,
        request: dbfs20200418_models.UpdateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.UpdateTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.UpdateTaskResponse(),
            self.do_rpcrequest('UpdateTask', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_task_with_options_async(
        self,
        request: dbfs20200418_models.UpdateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.UpdateTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.UpdateTaskResponse(),
            await self.do_rpcrequest_async('UpdateTask', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_task(
        self,
        request: dbfs20200418_models.UpdateTaskRequest,
    ) -> dbfs20200418_models.UpdateTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_task_with_options(request, runtime)

    async def update_task_async(
        self,
        request: dbfs20200418_models.UpdateTaskRequest,
    ) -> dbfs20200418_models.UpdateTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_task_with_options_async(request, runtime)

    def delete_tags_batch_with_options(
        self,
        request: dbfs20200418_models.DeleteTagsBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DeleteTagsBatchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.DeleteTagsBatchResponse(),
            self.do_rpcrequest('DeleteTagsBatch', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_tags_batch_with_options_async(
        self,
        request: dbfs20200418_models.DeleteTagsBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DeleteTagsBatchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.DeleteTagsBatchResponse(),
            await self.do_rpcrequest_async('DeleteTagsBatch', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_service_linked_role_with_options(
        self,
        request: dbfs20200418_models.GetServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.GetServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.GetServiceLinkedRoleResponse(),
            self.do_rpcrequest('GetServiceLinkedRole', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_service_linked_role_with_options_async(
        self,
        request: dbfs20200418_models.GetServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.GetServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.GetServiceLinkedRoleResponse(),
            await self.do_rpcrequest_async('GetServiceLinkedRole', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_constants_with_options(
        self,
        request: dbfs20200418_models.UpdateConstantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.UpdateConstantsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.UpdateConstantsResponse(),
            self.do_rpcrequest('UpdateConstants', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_constants_with_options_async(
        self,
        request: dbfs20200418_models.UpdateConstantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.UpdateConstantsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.UpdateConstantsResponse(),
            await self.do_rpcrequest_async('UpdateConstants', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_constants(
        self,
        request: dbfs20200418_models.UpdateConstantsRequest,
    ) -> dbfs20200418_models.UpdateConstantsResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_constants_with_options(request, runtime)

    async def update_constants_async(
        self,
        request: dbfs20200418_models.UpdateConstantsRequest,
    ) -> dbfs20200418_models.UpdateConstantsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_constants_with_options_async(request, runtime)

    def insert_synchroniz_constants_with_options(
        self,
        request: dbfs20200418_models.InsertSynchronizConstantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.InsertSynchronizConstantsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.InsertSynchronizConstantsResponse(),
            self.do_rpcrequest('InsertSynchronizConstants', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def insert_synchroniz_constants_with_options_async(
        self,
        request: dbfs20200418_models.InsertSynchronizConstantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.InsertSynchronizConstantsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.InsertSynchronizConstantsResponse(),
            await self.do_rpcrequest_async('InsertSynchronizConstants', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def insert_synchroniz_constants(
        self,
        request: dbfs20200418_models.InsertSynchronizConstantsRequest,
    ) -> dbfs20200418_models.InsertSynchronizConstantsResponse:
        runtime = util_models.RuntimeOptions()
        return self.insert_synchroniz_constants_with_options(request, runtime)

    async def insert_synchroniz_constants_async(
        self,
        request: dbfs20200418_models.InsertSynchronizConstantsRequest,
    ) -> dbfs20200418_models.InsertSynchronizConstantsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.insert_synchroniz_constants_with_options_async(request, runtime)

    def attach_dbfs_with_options(
        self,
        request: dbfs20200418_models.AttachDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.AttachDbfsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.AttachDbfsResponse(),
            self.do_rpcrequest('AttachDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.AttachDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.AttachDbfsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.AttachDbfsResponse(),
            await self.do_rpcrequest_async('AttachDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_task_with_options(
        self,
        request: dbfs20200418_models.ListTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListTaskResponse(),
            self.do_rpcrequest('ListTask', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_task_with_options_async(
        self,
        request: dbfs20200418_models.ListTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListTaskResponse(),
            await self.do_rpcrequest_async('ListTask', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_task(
        self,
        request: dbfs20200418_models.ListTaskRequest,
    ) -> dbfs20200418_models.ListTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_task_with_options(request, runtime)

    async def list_task_async(
        self,
        request: dbfs20200418_models.ListTaskRequest,
    ) -> dbfs20200418_models.ListTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_task_with_options_async(request, runtime)

    def list_dbfs_with_options(
        self,
        request: dbfs20200418_models.ListDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListDbfsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListDbfsResponse(),
            self.do_rpcrequest('ListDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.ListDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListDbfsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListDbfsResponse(),
            await self.do_rpcrequest_async('ListDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def add_tags_batch_with_options(
        self,
        request: dbfs20200418_models.AddTagsBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.AddTagsBatchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.AddTagsBatchResponse(),
            self.do_rpcrequest('AddTagsBatch', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_tags_batch_with_options_async(
        self,
        request: dbfs20200418_models.AddTagsBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.AddTagsBatchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.AddTagsBatchResponse(),
            await self.do_rpcrequest_async('AddTagsBatch', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def tag_dbfs_with_options(
        self,
        request: dbfs20200418_models.TagDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.TagDbfsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.TagDbfsResponse(),
            self.do_rpcrequest('TagDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.TagDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.TagDbfsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.TagDbfsResponse(),
            await self.do_rpcrequest_async('TagDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_synchroniz_constants_with_options(
        self,
        request: dbfs20200418_models.GetSynchronizConstantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.GetSynchronizConstantsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.GetSynchronizConstantsResponse(),
            self.do_rpcrequest('GetSynchronizConstants', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_synchroniz_constants_with_options_async(
        self,
        request: dbfs20200418_models.GetSynchronizConstantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.GetSynchronizConstantsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.GetSynchronizConstantsResponse(),
            await self.do_rpcrequest_async('GetSynchronizConstants', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_synchroniz_constants(
        self,
        request: dbfs20200418_models.GetSynchronizConstantsRequest,
    ) -> dbfs20200418_models.GetSynchronizConstantsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_synchroniz_constants_with_options(request, runtime)

    async def get_synchroniz_constants_async(
        self,
        request: dbfs20200418_models.GetSynchronizConstantsRequest,
    ) -> dbfs20200418_models.GetSynchronizConstantsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_synchroniz_constants_with_options_async(request, runtime)

    def opreate_constants_with_options(
        self,
        request: dbfs20200418_models.OpreateConstantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.OpreateConstantsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.OpreateConstantsResponse(),
            self.do_rpcrequest('OpreateConstants', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def opreate_constants_with_options_async(
        self,
        request: dbfs20200418_models.OpreateConstantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.OpreateConstantsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.OpreateConstantsResponse(),
            await self.do_rpcrequest_async('OpreateConstants', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def opreate_constants(
        self,
        request: dbfs20200418_models.OpreateConstantsRequest,
    ) -> dbfs20200418_models.OpreateConstantsResponse:
        runtime = util_models.RuntimeOptions()
        return self.opreate_constants_with_options(request, runtime)

    async def opreate_constants_async(
        self,
        request: dbfs20200418_models.OpreateConstantsRequest,
    ) -> dbfs20200418_models.OpreateConstantsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.opreate_constants_with_options_async(request, runtime)

    def rename_dbfs_with_options(
        self,
        request: dbfs20200418_models.RenameDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.RenameDbfsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.RenameDbfsResponse(),
            self.do_rpcrequest('RenameDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def rename_dbfs_with_options_async(
        self,
        request: dbfs20200418_models.RenameDbfsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.RenameDbfsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.RenameDbfsResponse(),
            await self.do_rpcrequest_async('RenameDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_tag_keys_with_options(
        self,
        request: dbfs20200418_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListTagKeysResponse(),
            self.do_rpcrequest('ListTagKeys', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: dbfs20200418_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListTagKeysResponse(),
            await self.do_rpcrequest_async('ListTagKeys', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_constants_with_options(
        self,
        request: dbfs20200418_models.ListConstantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListConstantsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListConstantsResponse(),
            self.do_rpcrequest('ListConstants', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_constants_with_options_async(
        self,
        request: dbfs20200418_models.ListConstantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListConstantsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListConstantsResponse(),
            await self.do_rpcrequest_async('ListConstants', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_constants(
        self,
        request: dbfs20200418_models.ListConstantsRequest,
    ) -> dbfs20200418_models.ListConstantsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_constants_with_options(request, runtime)

    async def list_constants_async(
        self,
        request: dbfs20200418_models.ListConstantsRequest,
    ) -> dbfs20200418_models.ListConstantsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_constants_with_options_async(request, runtime)

    def list_snapshot_with_options(
        self,
        request: dbfs20200418_models.ListSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListSnapshotResponse(),
            self.do_rpcrequest('ListSnapshot', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_snapshot_with_options_async(
        self,
        request: dbfs20200418_models.ListSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.ListSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListSnapshotResponse(),
            await self.do_rpcrequest_async('ListSnapshot', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_dbfs_specifications_with_options(
        self,
        request: dbfs20200418_models.DescribeDbfsSpecificationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DescribeDbfsSpecificationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.DescribeDbfsSpecificationsResponse(),
            self.do_rpcrequest('DescribeDbfsSpecifications', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbfs_specifications_with_options_async(
        self,
        request: dbfs20200418_models.DescribeDbfsSpecificationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.DescribeDbfsSpecificationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.DescribeDbfsSpecificationsResponse(),
            await self.do_rpcrequest_async('DescribeDbfsSpecifications', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_snapshot_with_options(
        self,
        request: dbfs20200418_models.CreateSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.CreateSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.CreateSnapshotResponse(),
            self.do_rpcrequest('CreateSnapshot', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_snapshot_with_options_async(
        self,
        request: dbfs20200418_models.CreateSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbfs20200418_models.CreateSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.CreateSnapshotResponse(),
            await self.do_rpcrequest_async('CreateSnapshot', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
