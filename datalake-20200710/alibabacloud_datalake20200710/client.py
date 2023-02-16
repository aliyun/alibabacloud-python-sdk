# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_datalake20200710 import models as data_lake_20200710_models
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
            'ap-northeast-1': 'datalake-daily.aliyuncs.com',
            'ap-northeast-2-pop': 'datalake-daily.aliyuncs.com',
            'ap-south-1': 'datalake-daily.aliyuncs.com',
            'ap-southeast-1': 'datalake-daily.aliyuncs.com',
            'ap-southeast-2': 'datalake-daily.aliyuncs.com',
            'ap-southeast-3': 'datalake-daily.aliyuncs.com',
            'ap-southeast-5': 'datalake-daily.aliyuncs.com',
            'cn-beijing': 'dlf.cn-beijing.aliyuncs.com',
            'cn-beijing-finance-1': 'datalake-daily.aliyuncs.com',
            'cn-beijing-finance-pop': 'datalake-daily.aliyuncs.com',
            'cn-beijing-gov-1': 'datalake-daily.aliyuncs.com',
            'cn-beijing-nu16-b01': 'datalake-daily.aliyuncs.com',
            'cn-chengdu': 'datalake-daily.aliyuncs.com',
            'cn-edge-1': 'datalake-daily.aliyuncs.com',
            'cn-fujian': 'datalake-daily.aliyuncs.com',
            'cn-haidian-cm12-c01': 'datalake-daily.aliyuncs.com',
            'cn-hangzhou': 'dlf.cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'datalake-daily.aliyuncs.com',
            'cn-hangzhou-finance': 'datalake-daily.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'datalake-daily.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'datalake-daily.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'datalake-daily.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'datalake-daily.aliyuncs.com',
            'cn-hangzhou-test-306': 'datalake-daily.aliyuncs.com',
            'cn-hongkong': 'datalake-daily.aliyuncs.com',
            'cn-hongkong-finance-pop': 'datalake-daily.aliyuncs.com',
            'cn-huhehaote': 'datalake-daily.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'datalake-daily.aliyuncs.com',
            'cn-north-2-gov-1': 'datalake-daily.aliyuncs.com',
            'cn-qingdao': 'datalake-daily.aliyuncs.com',
            'cn-qingdao-nebula': 'datalake-daily.aliyuncs.com',
            'cn-shanghai': 'dlf.cn-shanghai.aliyuncs.com',
            'cn-shanghai-et15-b01': 'datalake-daily.aliyuncs.com',
            'cn-shanghai-et2-b01': 'datalake-daily.aliyuncs.com',
            'cn-shanghai-finance-1': 'datalake-daily.aliyuncs.com',
            'cn-shanghai-inner': 'datalake-daily.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'datalake-daily.aliyuncs.com',
            'cn-shenzhen': 'dlf.cn-shenzhen.aliyuncs.com',
            'cn-shenzhen-finance-1': 'datalake-daily.aliyuncs.com',
            'cn-shenzhen-inner': 'datalake-daily.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'datalake-daily.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'datalake-daily.aliyuncs.com',
            'cn-wuhan': 'datalake-daily.aliyuncs.com',
            'cn-wulanchabu': 'datalake-daily.aliyuncs.com',
            'cn-yushanfang': 'datalake-daily.aliyuncs.com',
            'cn-zhangbei': 'datalake-daily.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'datalake-daily.aliyuncs.com',
            'cn-zhangjiakou': 'datalake-daily.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'datalake-daily.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'datalake-daily.aliyuncs.com',
            'eu-central-1': 'datalake-daily.aliyuncs.com',
            'eu-west-1': 'datalake-daily.aliyuncs.com',
            'eu-west-1-oxs': 'datalake-daily.aliyuncs.com',
            'me-east-1': 'datalake-daily.aliyuncs.com',
            'rus-west-1-pop': 'datalake-daily.aliyuncs.com',
            'us-east-1': 'datalake-daily.aliyuncs.com',
            'us-west-1': 'datalake-daily.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('datalake', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def abort_lock_with_options(
        self,
        request: data_lake_20200710_models.AbortLockRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.AbortLockResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lock_id):
            query['LockId'] = request.lock_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortLock',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/locks/abort',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.AbortLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def abort_lock_with_options_async(
        self,
        request: data_lake_20200710_models.AbortLockRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.AbortLockResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lock_id):
            query['LockId'] = request.lock_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortLock',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/locks/abort',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.AbortLockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def abort_lock(
        self,
        request: data_lake_20200710_models.AbortLockRequest,
    ) -> data_lake_20200710_models.AbortLockResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.abort_lock_with_options(request, headers, runtime)

    async def abort_lock_async(
        self,
        request: data_lake_20200710_models.AbortLockRequest,
    ) -> data_lake_20200710_models.AbortLockResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.abort_lock_with_options_async(request, headers, runtime)

    def batch_create_partitions_with_options(
        self,
        request: data_lake_20200710_models.BatchCreatePartitionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.BatchCreatePartitionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.if_not_exists):
            body['IfNotExists'] = request.if_not_exists
        if not UtilClient.is_unset(request.need_result):
            body['NeedResult'] = request.need_result
        if not UtilClient.is_unset(request.partition_inputs):
            body['PartitionInputs'] = request.partition_inputs
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchCreatePartitions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/batchcreate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchCreatePartitionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_create_partitions_with_options_async(
        self,
        request: data_lake_20200710_models.BatchCreatePartitionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.BatchCreatePartitionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.if_not_exists):
            body['IfNotExists'] = request.if_not_exists
        if not UtilClient.is_unset(request.need_result):
            body['NeedResult'] = request.need_result
        if not UtilClient.is_unset(request.partition_inputs):
            body['PartitionInputs'] = request.partition_inputs
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchCreatePartitions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/batchcreate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchCreatePartitionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_create_partitions(
        self,
        request: data_lake_20200710_models.BatchCreatePartitionsRequest,
    ) -> data_lake_20200710_models.BatchCreatePartitionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_create_partitions_with_options(request, headers, runtime)

    async def batch_create_partitions_async(
        self,
        request: data_lake_20200710_models.BatchCreatePartitionsRequest,
    ) -> data_lake_20200710_models.BatchCreatePartitionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_create_partitions_with_options_async(request, headers, runtime)

    def batch_create_tables_with_options(
        self,
        request: data_lake_20200710_models.BatchCreateTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.BatchCreateTablesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.if_not_exists):
            body['IfNotExists'] = request.if_not_exists
        if not UtilClient.is_unset(request.table_inputs):
            body['TableInputs'] = request.table_inputs
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchCreateTables',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/batchcreate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchCreateTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_create_tables_with_options_async(
        self,
        request: data_lake_20200710_models.BatchCreateTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.BatchCreateTablesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.if_not_exists):
            body['IfNotExists'] = request.if_not_exists
        if not UtilClient.is_unset(request.table_inputs):
            body['TableInputs'] = request.table_inputs
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchCreateTables',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/batchcreate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchCreateTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_create_tables(
        self,
        request: data_lake_20200710_models.BatchCreateTablesRequest,
    ) -> data_lake_20200710_models.BatchCreateTablesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_create_tables_with_options(request, headers, runtime)

    async def batch_create_tables_async(
        self,
        request: data_lake_20200710_models.BatchCreateTablesRequest,
    ) -> data_lake_20200710_models.BatchCreateTablesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_create_tables_with_options_async(request, headers, runtime)

    def batch_delete_partitions_with_options(
        self,
        request: data_lake_20200710_models.BatchDeletePartitionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.BatchDeletePartitionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.if_exists):
            body['IfExists'] = request.if_exists
        if not UtilClient.is_unset(request.partition_value_list):
            body['PartitionValueList'] = request.partition_value_list
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeletePartitions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/batchdelete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchDeletePartitionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_partitions_with_options_async(
        self,
        request: data_lake_20200710_models.BatchDeletePartitionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.BatchDeletePartitionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.if_exists):
            body['IfExists'] = request.if_exists
        if not UtilClient.is_unset(request.partition_value_list):
            body['PartitionValueList'] = request.partition_value_list
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeletePartitions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/batchdelete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchDeletePartitionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_partitions(
        self,
        request: data_lake_20200710_models.BatchDeletePartitionsRequest,
    ) -> data_lake_20200710_models.BatchDeletePartitionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_delete_partitions_with_options(request, headers, runtime)

    async def batch_delete_partitions_async(
        self,
        request: data_lake_20200710_models.BatchDeletePartitionsRequest,
    ) -> data_lake_20200710_models.BatchDeletePartitionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_delete_partitions_with_options_async(request, headers, runtime)

    def batch_delete_table_versions_with_options(
        self,
        request: data_lake_20200710_models.BatchDeleteTableVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.BatchDeleteTableVersionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        if not UtilClient.is_unset(request.version_ids):
            body['VersionIds'] = request.version_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeleteTableVersions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/versions/batchdelete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchDeleteTableVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_table_versions_with_options_async(
        self,
        request: data_lake_20200710_models.BatchDeleteTableVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.BatchDeleteTableVersionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        if not UtilClient.is_unset(request.version_ids):
            body['VersionIds'] = request.version_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeleteTableVersions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/versions/batchdelete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchDeleteTableVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_table_versions(
        self,
        request: data_lake_20200710_models.BatchDeleteTableVersionsRequest,
    ) -> data_lake_20200710_models.BatchDeleteTableVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_delete_table_versions_with_options(request, headers, runtime)

    async def batch_delete_table_versions_async(
        self,
        request: data_lake_20200710_models.BatchDeleteTableVersionsRequest,
    ) -> data_lake_20200710_models.BatchDeleteTableVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_delete_table_versions_with_options_async(request, headers, runtime)

    def batch_delete_tables_with_options(
        self,
        request: data_lake_20200710_models.BatchDeleteTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.BatchDeleteTablesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.if_exists):
            body['IfExists'] = request.if_exists
        if not UtilClient.is_unset(request.table_names):
            body['TableNames'] = request.table_names
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeleteTables',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/batchdelete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchDeleteTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_tables_with_options_async(
        self,
        request: data_lake_20200710_models.BatchDeleteTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.BatchDeleteTablesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.if_exists):
            body['IfExists'] = request.if_exists
        if not UtilClient.is_unset(request.table_names):
            body['TableNames'] = request.table_names
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeleteTables',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/batchdelete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchDeleteTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_tables(
        self,
        request: data_lake_20200710_models.BatchDeleteTablesRequest,
    ) -> data_lake_20200710_models.BatchDeleteTablesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_delete_tables_with_options(request, headers, runtime)

    async def batch_delete_tables_async(
        self,
        request: data_lake_20200710_models.BatchDeleteTablesRequest,
    ) -> data_lake_20200710_models.BatchDeleteTablesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_delete_tables_with_options_async(request, headers, runtime)

    def batch_get_partition_column_statistics_with_options(
        self,
        request: data_lake_20200710_models.BatchGetPartitionColumnStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.BatchGetPartitionColumnStatisticsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.column_names):
            body['ColumnNames'] = request.column_names
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.partition_names):
            body['PartitionNames'] = request.partition_names
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchGetPartitionColumnStatistics',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/columnstatistics/batchget',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchGetPartitionColumnStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_get_partition_column_statistics_with_options_async(
        self,
        request: data_lake_20200710_models.BatchGetPartitionColumnStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.BatchGetPartitionColumnStatisticsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.column_names):
            body['ColumnNames'] = request.column_names
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.partition_names):
            body['PartitionNames'] = request.partition_names
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchGetPartitionColumnStatistics',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/columnstatistics/batchget',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchGetPartitionColumnStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_get_partition_column_statistics(
        self,
        request: data_lake_20200710_models.BatchGetPartitionColumnStatisticsRequest,
    ) -> data_lake_20200710_models.BatchGetPartitionColumnStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_get_partition_column_statistics_with_options(request, headers, runtime)

    async def batch_get_partition_column_statistics_async(
        self,
        request: data_lake_20200710_models.BatchGetPartitionColumnStatisticsRequest,
    ) -> data_lake_20200710_models.BatchGetPartitionColumnStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_get_partition_column_statistics_with_options_async(request, headers, runtime)

    def batch_get_partitions_with_options(
        self,
        request: data_lake_20200710_models.BatchGetPartitionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.BatchGetPartitionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.is_share_sd):
            body['IsShareSd'] = request.is_share_sd
        if not UtilClient.is_unset(request.partition_value_list):
            body['PartitionValueList'] = request.partition_value_list
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchGetPartitions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/batchget',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchGetPartitionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_get_partitions_with_options_async(
        self,
        request: data_lake_20200710_models.BatchGetPartitionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.BatchGetPartitionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.is_share_sd):
            body['IsShareSd'] = request.is_share_sd
        if not UtilClient.is_unset(request.partition_value_list):
            body['PartitionValueList'] = request.partition_value_list
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchGetPartitions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/batchget',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchGetPartitionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_get_partitions(
        self,
        request: data_lake_20200710_models.BatchGetPartitionsRequest,
    ) -> data_lake_20200710_models.BatchGetPartitionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_get_partitions_with_options(request, headers, runtime)

    async def batch_get_partitions_async(
        self,
        request: data_lake_20200710_models.BatchGetPartitionsRequest,
    ) -> data_lake_20200710_models.BatchGetPartitionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_get_partitions_with_options_async(request, headers, runtime)

    def batch_get_tables_with_options(
        self,
        request: data_lake_20200710_models.BatchGetTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.BatchGetTablesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_names):
            body['TableNames'] = request.table_names
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchGetTables',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/batchget',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchGetTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_get_tables_with_options_async(
        self,
        request: data_lake_20200710_models.BatchGetTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.BatchGetTablesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_names):
            body['TableNames'] = request.table_names
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchGetTables',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/batchget',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchGetTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_get_tables(
        self,
        request: data_lake_20200710_models.BatchGetTablesRequest,
    ) -> data_lake_20200710_models.BatchGetTablesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_get_tables_with_options(request, headers, runtime)

    async def batch_get_tables_async(
        self,
        request: data_lake_20200710_models.BatchGetTablesRequest,
    ) -> data_lake_20200710_models.BatchGetTablesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_get_tables_with_options_async(request, headers, runtime)

    def batch_grant_permissions_with_options(
        self,
        request: data_lake_20200710_models.BatchGrantPermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.BatchGrantPermissionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.grant_revoke_entries):
            body['GrantRevokeEntries'] = request.grant_revoke_entries
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchGrantPermissions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/permissions/batchgrant',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchGrantPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_grant_permissions_with_options_async(
        self,
        request: data_lake_20200710_models.BatchGrantPermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.BatchGrantPermissionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.grant_revoke_entries):
            body['GrantRevokeEntries'] = request.grant_revoke_entries
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchGrantPermissions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/permissions/batchgrant',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchGrantPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_grant_permissions(
        self,
        request: data_lake_20200710_models.BatchGrantPermissionsRequest,
    ) -> data_lake_20200710_models.BatchGrantPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_grant_permissions_with_options(request, headers, runtime)

    async def batch_grant_permissions_async(
        self,
        request: data_lake_20200710_models.BatchGrantPermissionsRequest,
    ) -> data_lake_20200710_models.BatchGrantPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_grant_permissions_with_options_async(request, headers, runtime)

    def batch_revoke_permissions_with_options(
        self,
        request: data_lake_20200710_models.BatchRevokePermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.BatchRevokePermissionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.grant_revoke_entries):
            body['GrantRevokeEntries'] = request.grant_revoke_entries
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchRevokePermissions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/permissions/batchrevoke',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchRevokePermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_revoke_permissions_with_options_async(
        self,
        request: data_lake_20200710_models.BatchRevokePermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.BatchRevokePermissionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.grant_revoke_entries):
            body['GrantRevokeEntries'] = request.grant_revoke_entries
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchRevokePermissions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/permissions/batchrevoke',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchRevokePermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_revoke_permissions(
        self,
        request: data_lake_20200710_models.BatchRevokePermissionsRequest,
    ) -> data_lake_20200710_models.BatchRevokePermissionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_revoke_permissions_with_options(request, headers, runtime)

    async def batch_revoke_permissions_async(
        self,
        request: data_lake_20200710_models.BatchRevokePermissionsRequest,
    ) -> data_lake_20200710_models.BatchRevokePermissionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_revoke_permissions_with_options_async(request, headers, runtime)

    def batch_update_partitions_with_options(
        self,
        request: data_lake_20200710_models.BatchUpdatePartitionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.BatchUpdatePartitionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.partition_inputs):
            body['PartitionInputs'] = request.partition_inputs
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchUpdatePartitions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/batchupdate',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchUpdatePartitionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_update_partitions_with_options_async(
        self,
        request: data_lake_20200710_models.BatchUpdatePartitionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.BatchUpdatePartitionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.partition_inputs):
            body['PartitionInputs'] = request.partition_inputs
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchUpdatePartitions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/batchupdate',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchUpdatePartitionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_update_partitions(
        self,
        request: data_lake_20200710_models.BatchUpdatePartitionsRequest,
    ) -> data_lake_20200710_models.BatchUpdatePartitionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_update_partitions_with_options(request, headers, runtime)

    async def batch_update_partitions_async(
        self,
        request: data_lake_20200710_models.BatchUpdatePartitionsRequest,
    ) -> data_lake_20200710_models.BatchUpdatePartitionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_update_partitions_with_options_async(request, headers, runtime)

    def batch_update_tables_with_options(
        self,
        request: data_lake_20200710_models.BatchUpdateTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.BatchUpdateTablesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.is_async):
            body['IsAsync'] = request.is_async
        if not UtilClient.is_unset(request.table_inputs):
            body['TableInputs'] = request.table_inputs
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchUpdateTables',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/batchupdate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchUpdateTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_update_tables_with_options_async(
        self,
        request: data_lake_20200710_models.BatchUpdateTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.BatchUpdateTablesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.is_async):
            body['IsAsync'] = request.is_async
        if not UtilClient.is_unset(request.table_inputs):
            body['TableInputs'] = request.table_inputs
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchUpdateTables',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/batchupdate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.BatchUpdateTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_update_tables(
        self,
        request: data_lake_20200710_models.BatchUpdateTablesRequest,
    ) -> data_lake_20200710_models.BatchUpdateTablesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_update_tables_with_options(request, headers, runtime)

    async def batch_update_tables_async(
        self,
        request: data_lake_20200710_models.BatchUpdateTablesRequest,
    ) -> data_lake_20200710_models.BatchUpdateTablesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_update_tables_with_options_async(request, headers, runtime)

    def cancel_query_with_options(
        self,
        request: data_lake_20200710_models.CancelQueryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.CancelQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelQuery',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/webapi/query/cancelQuery',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.CancelQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_query_with_options_async(
        self,
        request: data_lake_20200710_models.CancelQueryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.CancelQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelQuery',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/webapi/query/cancelQuery',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.CancelQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_query(
        self,
        request: data_lake_20200710_models.CancelQueryRequest,
    ) -> data_lake_20200710_models.CancelQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_query_with_options(request, headers, runtime)

    async def cancel_query_async(
        self,
        request: data_lake_20200710_models.CancelQueryRequest,
    ) -> data_lake_20200710_models.CancelQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_query_with_options_async(request, headers, runtime)

    def check_permissions_with_options(
        self,
        request: data_lake_20200710_models.CheckPermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.CheckPermissionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CheckPermissions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/permissions/check',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.CheckPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_permissions_with_options_async(
        self,
        request: data_lake_20200710_models.CheckPermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.CheckPermissionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CheckPermissions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/permissions/check',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.CheckPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_permissions(
        self,
        request: data_lake_20200710_models.CheckPermissionsRequest,
    ) -> data_lake_20200710_models.CheckPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_permissions_with_options(request, headers, runtime)

    async def check_permissions_async(
        self,
        request: data_lake_20200710_models.CheckPermissionsRequest,
    ) -> data_lake_20200710_models.CheckPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.check_permissions_with_options_async(request, headers, runtime)

    def create_catalog_with_options(
        self,
        request: data_lake_20200710_models.CreateCatalogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.CreateCatalogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_input):
            body['CatalogInput'] = request.catalog_input
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCatalog',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.CreateCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_catalog_with_options_async(
        self,
        request: data_lake_20200710_models.CreateCatalogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.CreateCatalogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_input):
            body['CatalogInput'] = request.catalog_input
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCatalog',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.CreateCatalogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_catalog(
        self,
        request: data_lake_20200710_models.CreateCatalogRequest,
    ) -> data_lake_20200710_models.CreateCatalogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_catalog_with_options(request, headers, runtime)

    async def create_catalog_async(
        self,
        request: data_lake_20200710_models.CreateCatalogRequest,
    ) -> data_lake_20200710_models.CreateCatalogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_catalog_with_options_async(request, headers, runtime)

    def create_database_with_options(
        self,
        request: data_lake_20200710_models.CreateDatabaseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.CreateDatabaseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_input):
            body['DatabaseInput'] = request.database_input
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDatabase',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.CreateDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_database_with_options_async(
        self,
        request: data_lake_20200710_models.CreateDatabaseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.CreateDatabaseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_input):
            body['DatabaseInput'] = request.database_input
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDatabase',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.CreateDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_database(
        self,
        request: data_lake_20200710_models.CreateDatabaseRequest,
    ) -> data_lake_20200710_models.CreateDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_database_with_options(request, headers, runtime)

    async def create_database_async(
        self,
        request: data_lake_20200710_models.CreateDatabaseRequest,
    ) -> data_lake_20200710_models.CreateDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_database_with_options_async(request, headers, runtime)

    def create_function_with_options(
        self,
        request: data_lake_20200710_models.CreateFunctionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.CreateFunctionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.function_input):
            body['FunctionInput'] = request.function_input
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFunction',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/functions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.CreateFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_function_with_options_async(
        self,
        request: data_lake_20200710_models.CreateFunctionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.CreateFunctionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.function_input):
            body['FunctionInput'] = request.function_input
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFunction',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/functions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.CreateFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_function(
        self,
        request: data_lake_20200710_models.CreateFunctionRequest,
    ) -> data_lake_20200710_models.CreateFunctionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_function_with_options(request, headers, runtime)

    async def create_function_async(
        self,
        request: data_lake_20200710_models.CreateFunctionRequest,
    ) -> data_lake_20200710_models.CreateFunctionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_function_with_options_async(request, headers, runtime)

    def create_lock_with_options(
        self,
        request: data_lake_20200710_models.CreateLockRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.CreateLockResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lock_obj_list):
            body['LockObjList'] = request.lock_obj_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLock',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/locks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.CreateLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_lock_with_options_async(
        self,
        request: data_lake_20200710_models.CreateLockRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.CreateLockResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lock_obj_list):
            body['LockObjList'] = request.lock_obj_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLock',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/locks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.CreateLockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_lock(
        self,
        request: data_lake_20200710_models.CreateLockRequest,
    ) -> data_lake_20200710_models.CreateLockResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_lock_with_options(request, headers, runtime)

    async def create_lock_async(
        self,
        request: data_lake_20200710_models.CreateLockRequest,
    ) -> data_lake_20200710_models.CreateLockResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_lock_with_options_async(request, headers, runtime)

    def create_partition_with_options(
        self,
        request: data_lake_20200710_models.CreatePartitionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.CreatePartitionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.if_not_exists):
            body['IfNotExists'] = request.if_not_exists
        if not UtilClient.is_unset(request.need_result):
            body['NeedResult'] = request.need_result
        if not UtilClient.is_unset(request.partition_input):
            body['PartitionInput'] = request.partition_input
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePartition',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.CreatePartitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_partition_with_options_async(
        self,
        request: data_lake_20200710_models.CreatePartitionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.CreatePartitionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.if_not_exists):
            body['IfNotExists'] = request.if_not_exists
        if not UtilClient.is_unset(request.need_result):
            body['NeedResult'] = request.need_result
        if not UtilClient.is_unset(request.partition_input):
            body['PartitionInput'] = request.partition_input
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePartition',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.CreatePartitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_partition(
        self,
        request: data_lake_20200710_models.CreatePartitionRequest,
    ) -> data_lake_20200710_models.CreatePartitionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_partition_with_options(request, headers, runtime)

    async def create_partition_async(
        self,
        request: data_lake_20200710_models.CreatePartitionRequest,
    ) -> data_lake_20200710_models.CreatePartitionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_partition_with_options_async(request, headers, runtime)

    def create_role_with_options(
        self,
        request: data_lake_20200710_models.CreateRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.CreateRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateRole',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/roles',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.CreateRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_role_with_options_async(
        self,
        request: data_lake_20200710_models.CreateRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.CreateRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateRole',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/roles',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.CreateRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_role(
        self,
        request: data_lake_20200710_models.CreateRoleRequest,
    ) -> data_lake_20200710_models.CreateRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_role_with_options(request, headers, runtime)

    async def create_role_async(
        self,
        request: data_lake_20200710_models.CreateRoleRequest,
    ) -> data_lake_20200710_models.CreateRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_role_with_options_async(request, headers, runtime)

    def create_table_with_options(
        self,
        request: data_lake_20200710_models.CreateTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.CreateTableResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_input):
            body['TableInput'] = request.table_input
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTable',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.CreateTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_table_with_options_async(
        self,
        request: data_lake_20200710_models.CreateTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.CreateTableResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_input):
            body['TableInput'] = request.table_input
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTable',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.CreateTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_table(
        self,
        request: data_lake_20200710_models.CreateTableRequest,
    ) -> data_lake_20200710_models.CreateTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_table_with_options(request, headers, runtime)

    async def create_table_async(
        self,
        request: data_lake_20200710_models.CreateTableRequest,
    ) -> data_lake_20200710_models.CreateTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_table_with_options_async(request, headers, runtime)

    def delete_catalog_with_options(
        self,
        request: data_lake_20200710_models.DeleteCatalogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.DeleteCatalogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.is_async):
            query['IsAsync'] = request.is_async
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCatalog',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeleteCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_catalog_with_options_async(
        self,
        request: data_lake_20200710_models.DeleteCatalogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.DeleteCatalogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.is_async):
            query['IsAsync'] = request.is_async
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCatalog',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeleteCatalogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_catalog(
        self,
        request: data_lake_20200710_models.DeleteCatalogRequest,
    ) -> data_lake_20200710_models.DeleteCatalogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_catalog_with_options(request, headers, runtime)

    async def delete_catalog_async(
        self,
        request: data_lake_20200710_models.DeleteCatalogRequest,
    ) -> data_lake_20200710_models.DeleteCatalogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_catalog_with_options_async(request, headers, runtime)

    def delete_database_with_options(
        self,
        request: data_lake_20200710_models.DeleteDatabaseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.DeleteDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cascade):
            query['Cascade'] = request.cascade
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDatabase',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeleteDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_database_with_options_async(
        self,
        request: data_lake_20200710_models.DeleteDatabaseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.DeleteDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cascade):
            query['Cascade'] = request.cascade
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDatabase',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeleteDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_database(
        self,
        request: data_lake_20200710_models.DeleteDatabaseRequest,
    ) -> data_lake_20200710_models.DeleteDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_database_with_options(request, headers, runtime)

    async def delete_database_async(
        self,
        request: data_lake_20200710_models.DeleteDatabaseRequest,
    ) -> data_lake_20200710_models.DeleteDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_database_with_options_async(request, headers, runtime)

    def delete_function_with_options(
        self,
        request: data_lake_20200710_models.DeleteFunctionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.DeleteFunctionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFunction',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/functions',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeleteFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_function_with_options_async(
        self,
        request: data_lake_20200710_models.DeleteFunctionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.DeleteFunctionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFunction',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/functions',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeleteFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_function(
        self,
        request: data_lake_20200710_models.DeleteFunctionRequest,
    ) -> data_lake_20200710_models.DeleteFunctionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_function_with_options(request, headers, runtime)

    async def delete_function_async(
        self,
        request: data_lake_20200710_models.DeleteFunctionRequest,
    ) -> data_lake_20200710_models.DeleteFunctionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_function_with_options_async(request, headers, runtime)

    def delete_partition_with_options(
        self,
        request: data_lake_20200710_models.DeletePartitionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.DeletePartitionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.if_exists):
            body['IfExists'] = request.if_exists
        if not UtilClient.is_unset(request.partition_values):
            body['PartitionValues'] = request.partition_values
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePartition',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeletePartitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_partition_with_options_async(
        self,
        request: data_lake_20200710_models.DeletePartitionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.DeletePartitionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.if_exists):
            body['IfExists'] = request.if_exists
        if not UtilClient.is_unset(request.partition_values):
            body['PartitionValues'] = request.partition_values
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePartition',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeletePartitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_partition(
        self,
        request: data_lake_20200710_models.DeletePartitionRequest,
    ) -> data_lake_20200710_models.DeletePartitionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_partition_with_options(request, headers, runtime)

    async def delete_partition_async(
        self,
        request: data_lake_20200710_models.DeletePartitionRequest,
    ) -> data_lake_20200710_models.DeletePartitionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_partition_with_options_async(request, headers, runtime)

    def delete_partition_column_statistics_with_options(
        self,
        tmp_req: data_lake_20200710_models.DeletePartitionColumnStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.DeletePartitionColumnStatisticsResponse:
        UtilClient.validate_model(tmp_req)
        request = data_lake_20200710_models.DeletePartitionColumnStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.column_names):
            request.column_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.column_names, 'ColumnNames', 'json')
        if not UtilClient.is_unset(tmp_req.partition_names):
            request.partition_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.partition_names, 'PartitionNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.column_names_shrink):
            query['ColumnNames'] = request.column_names_shrink
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.partition_names_shrink):
            query['PartitionNames'] = request.partition_names_shrink
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePartitionColumnStatistics',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/columnstatistics',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeletePartitionColumnStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_partition_column_statistics_with_options_async(
        self,
        tmp_req: data_lake_20200710_models.DeletePartitionColumnStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.DeletePartitionColumnStatisticsResponse:
        UtilClient.validate_model(tmp_req)
        request = data_lake_20200710_models.DeletePartitionColumnStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.column_names):
            request.column_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.column_names, 'ColumnNames', 'json')
        if not UtilClient.is_unset(tmp_req.partition_names):
            request.partition_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.partition_names, 'PartitionNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.column_names_shrink):
            query['ColumnNames'] = request.column_names_shrink
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.partition_names_shrink):
            query['PartitionNames'] = request.partition_names_shrink
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePartitionColumnStatistics',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/columnstatistics',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeletePartitionColumnStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_partition_column_statistics(
        self,
        request: data_lake_20200710_models.DeletePartitionColumnStatisticsRequest,
    ) -> data_lake_20200710_models.DeletePartitionColumnStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_partition_column_statistics_with_options(request, headers, runtime)

    async def delete_partition_column_statistics_async(
        self,
        request: data_lake_20200710_models.DeletePartitionColumnStatisticsRequest,
    ) -> data_lake_20200710_models.DeletePartitionColumnStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_partition_column_statistics_with_options_async(request, headers, runtime)

    def delete_role_with_options(
        self,
        request: data_lake_20200710_models.DeleteRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.DeleteRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRole',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/roles',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeleteRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_role_with_options_async(
        self,
        request: data_lake_20200710_models.DeleteRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.DeleteRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRole',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/roles',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeleteRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_role(
        self,
        request: data_lake_20200710_models.DeleteRoleRequest,
    ) -> data_lake_20200710_models.DeleteRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_role_with_options(request, headers, runtime)

    async def delete_role_async(
        self,
        request: data_lake_20200710_models.DeleteRoleRequest,
    ) -> data_lake_20200710_models.DeleteRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_role_with_options_async(request, headers, runtime)

    def delete_table_with_options(
        self,
        request: data_lake_20200710_models.DeleteTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.DeleteTableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTable',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeleteTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_table_with_options_async(
        self,
        request: data_lake_20200710_models.DeleteTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.DeleteTableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTable',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeleteTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_table(
        self,
        request: data_lake_20200710_models.DeleteTableRequest,
    ) -> data_lake_20200710_models.DeleteTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_table_with_options(request, headers, runtime)

    async def delete_table_async(
        self,
        request: data_lake_20200710_models.DeleteTableRequest,
    ) -> data_lake_20200710_models.DeleteTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_table_with_options_async(request, headers, runtime)

    def delete_table_column_statistics_with_options(
        self,
        tmp_req: data_lake_20200710_models.DeleteTableColumnStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.DeleteTableColumnStatisticsResponse:
        UtilClient.validate_model(tmp_req)
        request = data_lake_20200710_models.DeleteTableColumnStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.column_names):
            request.column_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.column_names, 'ColumnNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.column_names_shrink):
            query['ColumnNames'] = request.column_names_shrink
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTableColumnStatistics',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/columnstatistics',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeleteTableColumnStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_table_column_statistics_with_options_async(
        self,
        tmp_req: data_lake_20200710_models.DeleteTableColumnStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.DeleteTableColumnStatisticsResponse:
        UtilClient.validate_model(tmp_req)
        request = data_lake_20200710_models.DeleteTableColumnStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.column_names):
            request.column_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.column_names, 'ColumnNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.column_names_shrink):
            query['ColumnNames'] = request.column_names_shrink
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTableColumnStatistics',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/columnstatistics',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeleteTableColumnStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_table_column_statistics(
        self,
        request: data_lake_20200710_models.DeleteTableColumnStatisticsRequest,
    ) -> data_lake_20200710_models.DeleteTableColumnStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_table_column_statistics_with_options(request, headers, runtime)

    async def delete_table_column_statistics_async(
        self,
        request: data_lake_20200710_models.DeleteTableColumnStatisticsRequest,
    ) -> data_lake_20200710_models.DeleteTableColumnStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_table_column_statistics_with_options_async(request, headers, runtime)

    def delete_table_version_with_options(
        self,
        request: data_lake_20200710_models.DeleteTableVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.DeleteTableVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTableVersion',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/versions',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeleteTableVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_table_version_with_options_async(
        self,
        request: data_lake_20200710_models.DeleteTableVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.DeleteTableVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTableVersion',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/versions',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeleteTableVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_table_version(
        self,
        request: data_lake_20200710_models.DeleteTableVersionRequest,
    ) -> data_lake_20200710_models.DeleteTableVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_table_version_with_options(request, headers, runtime)

    async def delete_table_version_async(
        self,
        request: data_lake_20200710_models.DeleteTableVersionRequest,
    ) -> data_lake_20200710_models.DeleteTableVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_table_version_with_options_async(request, headers, runtime)

    def deregister_location_with_options(
        self,
        request: data_lake_20200710_models.DeregisterLocationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.DeregisterLocationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.location_id):
            query['LocationId'] = request.location_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeregisterLocation',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/webapi/locations',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeregisterLocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def deregister_location_with_options_async(
        self,
        request: data_lake_20200710_models.DeregisterLocationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.DeregisterLocationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.location_id):
            query['LocationId'] = request.location_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeregisterLocation',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/webapi/locations',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DeregisterLocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deregister_location(
        self,
        request: data_lake_20200710_models.DeregisterLocationRequest,
    ) -> data_lake_20200710_models.DeregisterLocationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.deregister_location_with_options(request, headers, runtime)

    async def deregister_location_async(
        self,
        request: data_lake_20200710_models.DeregisterLocationRequest,
    ) -> data_lake_20200710_models.DeregisterLocationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.deregister_location_with_options_async(request, headers, runtime)

    def describe_regions_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/webapi/service/describeRegions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/webapi/service/describeRegions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(self) -> data_lake_20200710_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(headers, runtime)

    async def describe_regions_async(self) -> data_lake_20200710_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_regions_with_options_async(headers, runtime)

    def get_async_task_status_with_options(
        self,
        request: data_lake_20200710_models.GetAsyncTaskStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetAsyncTaskStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsyncTaskStatus',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetAsyncTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_async_task_status_with_options_async(
        self,
        request: data_lake_20200710_models.GetAsyncTaskStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetAsyncTaskStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsyncTaskStatus',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetAsyncTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_async_task_status(
        self,
        request: data_lake_20200710_models.GetAsyncTaskStatusRequest,
    ) -> data_lake_20200710_models.GetAsyncTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_async_task_status_with_options(request, headers, runtime)

    async def get_async_task_status_async(
        self,
        request: data_lake_20200710_models.GetAsyncTaskStatusRequest,
    ) -> data_lake_20200710_models.GetAsyncTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_async_task_status_with_options_async(request, headers, runtime)

    def get_catalog_with_options(
        self,
        request: data_lake_20200710_models.GetCatalogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetCatalogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCatalog',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_catalog_with_options_async(
        self,
        request: data_lake_20200710_models.GetCatalogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetCatalogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCatalog',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetCatalogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_catalog(
        self,
        request: data_lake_20200710_models.GetCatalogRequest,
    ) -> data_lake_20200710_models.GetCatalogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_catalog_with_options(request, headers, runtime)

    async def get_catalog_async(
        self,
        request: data_lake_20200710_models.GetCatalogRequest,
    ) -> data_lake_20200710_models.GetCatalogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_catalog_with_options_async(request, headers, runtime)

    def get_catalog_settings_with_options(
        self,
        request: data_lake_20200710_models.GetCatalogSettingsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetCatalogSettingsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCatalogSettings',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/settings',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetCatalogSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_catalog_settings_with_options_async(
        self,
        request: data_lake_20200710_models.GetCatalogSettingsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetCatalogSettingsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCatalogSettings',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/settings',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetCatalogSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_catalog_settings(
        self,
        request: data_lake_20200710_models.GetCatalogSettingsRequest,
    ) -> data_lake_20200710_models.GetCatalogSettingsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_catalog_settings_with_options(request, headers, runtime)

    async def get_catalog_settings_async(
        self,
        request: data_lake_20200710_models.GetCatalogSettingsRequest,
    ) -> data_lake_20200710_models.GetCatalogSettingsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_catalog_settings_with_options_async(request, headers, runtime)

    def get_database_with_options(
        self,
        request: data_lake_20200710_models.GetDatabaseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDatabase',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_database_with_options_async(
        self,
        request: data_lake_20200710_models.GetDatabaseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDatabase',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_database(
        self,
        request: data_lake_20200710_models.GetDatabaseRequest,
    ) -> data_lake_20200710_models.GetDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_database_with_options(request, headers, runtime)

    async def get_database_async(
        self,
        request: data_lake_20200710_models.GetDatabaseRequest,
    ) -> data_lake_20200710_models.GetDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_database_with_options_async(request, headers, runtime)

    def get_function_with_options(
        self,
        request: data_lake_20200710_models.GetFunctionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetFunctionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFunction',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/functions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_function_with_options_async(
        self,
        request: data_lake_20200710_models.GetFunctionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetFunctionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFunction',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/functions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_function(
        self,
        request: data_lake_20200710_models.GetFunctionRequest,
    ) -> data_lake_20200710_models.GetFunctionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_function_with_options(request, headers, runtime)

    async def get_function_async(
        self,
        request: data_lake_20200710_models.GetFunctionRequest,
    ) -> data_lake_20200710_models.GetFunctionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_function_with_options_async(request, headers, runtime)

    def get_lock_with_options(
        self,
        request: data_lake_20200710_models.GetLockRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetLockResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lock_id):
            query['LockId'] = request.lock_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLock',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/locks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lock_with_options_async(
        self,
        request: data_lake_20200710_models.GetLockRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetLockResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lock_id):
            query['LockId'] = request.lock_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLock',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/locks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetLockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lock(
        self,
        request: data_lake_20200710_models.GetLockRequest,
    ) -> data_lake_20200710_models.GetLockResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_lock_with_options(request, headers, runtime)

    async def get_lock_async(
        self,
        request: data_lake_20200710_models.GetLockRequest,
    ) -> data_lake_20200710_models.GetLockResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_lock_with_options_async(request, headers, runtime)

    def get_partition_with_options(
        self,
        request: data_lake_20200710_models.GetPartitionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetPartitionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.partition_values):
            body['PartitionValues'] = request.partition_values
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPartition',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetPartitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_partition_with_options_async(
        self,
        request: data_lake_20200710_models.GetPartitionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetPartitionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.partition_values):
            body['PartitionValues'] = request.partition_values
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPartition',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetPartitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_partition(
        self,
        request: data_lake_20200710_models.GetPartitionRequest,
    ) -> data_lake_20200710_models.GetPartitionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_partition_with_options(request, headers, runtime)

    async def get_partition_async(
        self,
        request: data_lake_20200710_models.GetPartitionRequest,
    ) -> data_lake_20200710_models.GetPartitionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_partition_with_options_async(request, headers, runtime)

    def get_partition_column_statistics_with_options(
        self,
        tmp_req: data_lake_20200710_models.GetPartitionColumnStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetPartitionColumnStatisticsResponse:
        UtilClient.validate_model(tmp_req)
        request = data_lake_20200710_models.GetPartitionColumnStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.column_names):
            request.column_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.column_names, 'ColumnNames', 'json')
        if not UtilClient.is_unset(tmp_req.partition_names):
            request.partition_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.partition_names, 'PartitionNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.column_names_shrink):
            query['ColumnNames'] = request.column_names_shrink
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.partition_names_shrink):
            query['PartitionNames'] = request.partition_names_shrink
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPartitionColumnStatistics',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/columnstatistics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetPartitionColumnStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_partition_column_statistics_with_options_async(
        self,
        tmp_req: data_lake_20200710_models.GetPartitionColumnStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetPartitionColumnStatisticsResponse:
        UtilClient.validate_model(tmp_req)
        request = data_lake_20200710_models.GetPartitionColumnStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.column_names):
            request.column_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.column_names, 'ColumnNames', 'json')
        if not UtilClient.is_unset(tmp_req.partition_names):
            request.partition_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.partition_names, 'PartitionNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.column_names_shrink):
            query['ColumnNames'] = request.column_names_shrink
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.partition_names_shrink):
            query['PartitionNames'] = request.partition_names_shrink
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPartitionColumnStatistics',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/columnstatistics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetPartitionColumnStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_partition_column_statistics(
        self,
        request: data_lake_20200710_models.GetPartitionColumnStatisticsRequest,
    ) -> data_lake_20200710_models.GetPartitionColumnStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_partition_column_statistics_with_options(request, headers, runtime)

    async def get_partition_column_statistics_async(
        self,
        request: data_lake_20200710_models.GetPartitionColumnStatisticsRequest,
    ) -> data_lake_20200710_models.GetPartitionColumnStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_partition_column_statistics_with_options_async(request, headers, runtime)

    def get_query_result_with_options(
        self,
        request: data_lake_20200710_models.GetQueryResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetQueryResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueryResult',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/webapi/query/getQueryResult',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetQueryResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_query_result_with_options_async(
        self,
        request: data_lake_20200710_models.GetQueryResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetQueryResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueryResult',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/webapi/query/getQueryResult',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetQueryResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_query_result(
        self,
        request: data_lake_20200710_models.GetQueryResultRequest,
    ) -> data_lake_20200710_models.GetQueryResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_query_result_with_options(request, headers, runtime)

    async def get_query_result_async(
        self,
        request: data_lake_20200710_models.GetQueryResultRequest,
    ) -> data_lake_20200710_models.GetQueryResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_query_result_with_options_async(request, headers, runtime)

    def get_region_status_with_options(
        self,
        request: data_lake_20200710_models.GetRegionStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetRegionStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRegionStatus',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/webapi/service/getRegionStatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetRegionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_region_status_with_options_async(
        self,
        request: data_lake_20200710_models.GetRegionStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetRegionStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRegionStatus',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/webapi/service/getRegionStatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetRegionStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_region_status(
        self,
        request: data_lake_20200710_models.GetRegionStatusRequest,
    ) -> data_lake_20200710_models.GetRegionStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_region_status_with_options(request, headers, runtime)

    async def get_region_status_async(
        self,
        request: data_lake_20200710_models.GetRegionStatusRequest,
    ) -> data_lake_20200710_models.GetRegionStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_region_status_with_options_async(request, headers, runtime)

    def get_role_with_options(
        self,
        request: data_lake_20200710_models.GetRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRole',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/roles',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_role_with_options_async(
        self,
        request: data_lake_20200710_models.GetRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRole',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/roles',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_role(
        self,
        request: data_lake_20200710_models.GetRoleRequest,
    ) -> data_lake_20200710_models.GetRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_role_with_options(request, headers, runtime)

    async def get_role_async(
        self,
        request: data_lake_20200710_models.GetRoleRequest,
    ) -> data_lake_20200710_models.GetRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_role_with_options_async(request, headers, runtime)

    def get_service_status_with_options(
        self,
        request: data_lake_20200710_models.GetServiceStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetServiceStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceStatus',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/webapi/service/getServiceStatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_status_with_options_async(
        self,
        request: data_lake_20200710_models.GetServiceStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetServiceStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceStatus',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/webapi/service/getServiceStatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_status(
        self,
        request: data_lake_20200710_models.GetServiceStatusRequest,
    ) -> data_lake_20200710_models.GetServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_status_with_options(request, headers, runtime)

    async def get_service_status_async(
        self,
        request: data_lake_20200710_models.GetServiceStatusRequest,
    ) -> data_lake_20200710_models.GetServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_service_status_with_options_async(request, headers, runtime)

    def get_table_with_options(
        self,
        request: data_lake_20200710_models.GetTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetTableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTable',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_with_options_async(
        self,
        request: data_lake_20200710_models.GetTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetTableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTable',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table(
        self,
        request: data_lake_20200710_models.GetTableRequest,
    ) -> data_lake_20200710_models.GetTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_table_with_options(request, headers, runtime)

    async def get_table_async(
        self,
        request: data_lake_20200710_models.GetTableRequest,
    ) -> data_lake_20200710_models.GetTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_table_with_options_async(request, headers, runtime)

    def get_table_column_statistics_with_options(
        self,
        tmp_req: data_lake_20200710_models.GetTableColumnStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetTableColumnStatisticsResponse:
        UtilClient.validate_model(tmp_req)
        request = data_lake_20200710_models.GetTableColumnStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.column_names):
            request.column_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.column_names, 'ColumnNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.column_names_shrink):
            query['ColumnNames'] = request.column_names_shrink
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTableColumnStatistics',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/columnstatistics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetTableColumnStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_column_statistics_with_options_async(
        self,
        tmp_req: data_lake_20200710_models.GetTableColumnStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetTableColumnStatisticsResponse:
        UtilClient.validate_model(tmp_req)
        request = data_lake_20200710_models.GetTableColumnStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.column_names):
            request.column_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.column_names, 'ColumnNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.column_names_shrink):
            query['ColumnNames'] = request.column_names_shrink
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTableColumnStatistics',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/columnstatistics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetTableColumnStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_column_statistics(
        self,
        request: data_lake_20200710_models.GetTableColumnStatisticsRequest,
    ) -> data_lake_20200710_models.GetTableColumnStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_table_column_statistics_with_options(request, headers, runtime)

    async def get_table_column_statistics_async(
        self,
        request: data_lake_20200710_models.GetTableColumnStatisticsRequest,
    ) -> data_lake_20200710_models.GetTableColumnStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_table_column_statistics_with_options_async(request, headers, runtime)

    def get_table_profile_with_options(
        self,
        request: data_lake_20200710_models.GetTableProfileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetTableProfileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTableProfile',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/webapi/metastorehouse/catalog/database/tableprofile',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetTableProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_profile_with_options_async(
        self,
        request: data_lake_20200710_models.GetTableProfileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetTableProfileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTableProfile',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/webapi/metastorehouse/catalog/database/tableprofile',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetTableProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_profile(
        self,
        request: data_lake_20200710_models.GetTableProfileRequest,
    ) -> data_lake_20200710_models.GetTableProfileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_table_profile_with_options(request, headers, runtime)

    async def get_table_profile_async(
        self,
        request: data_lake_20200710_models.GetTableProfileRequest,
    ) -> data_lake_20200710_models.GetTableProfileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_table_profile_with_options_async(request, headers, runtime)

    def get_table_version_with_options(
        self,
        request: data_lake_20200710_models.GetTableVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetTableVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTableVersion',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetTableVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_version_with_options_async(
        self,
        request: data_lake_20200710_models.GetTableVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GetTableVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTableVersion',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GetTableVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_version(
        self,
        request: data_lake_20200710_models.GetTableVersionRequest,
    ) -> data_lake_20200710_models.GetTableVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_table_version_with_options(request, headers, runtime)

    async def get_table_version_async(
        self,
        request: data_lake_20200710_models.GetTableVersionRequest,
    ) -> data_lake_20200710_models.GetTableVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_table_version_with_options_async(request, headers, runtime)

    def grant_permissions_with_options(
        self,
        request: data_lake_20200710_models.GrantPermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GrantPermissionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accesses):
            body['Accesses'] = request.accesses
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.delegate_accesses):
            body['DelegateAccesses'] = request.delegate_accesses
        if not UtilClient.is_unset(request.meta_resource):
            body['MetaResource'] = request.meta_resource
        if not UtilClient.is_unset(request.principal):
            body['Principal'] = request.principal
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantPermissions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/permissions/grant',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GrantPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_permissions_with_options_async(
        self,
        request: data_lake_20200710_models.GrantPermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GrantPermissionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accesses):
            body['Accesses'] = request.accesses
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.delegate_accesses):
            body['DelegateAccesses'] = request.delegate_accesses
        if not UtilClient.is_unset(request.meta_resource):
            body['MetaResource'] = request.meta_resource
        if not UtilClient.is_unset(request.principal):
            body['Principal'] = request.principal
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantPermissions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/permissions/grant',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GrantPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_permissions(
        self,
        request: data_lake_20200710_models.GrantPermissionsRequest,
    ) -> data_lake_20200710_models.GrantPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.grant_permissions_with_options(request, headers, runtime)

    async def grant_permissions_async(
        self,
        request: data_lake_20200710_models.GrantPermissionsRequest,
    ) -> data_lake_20200710_models.GrantPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.grant_permissions_with_options_async(request, headers, runtime)

    def grant_role_to_users_with_options(
        self,
        request: data_lake_20200710_models.GrantRoleToUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GrantRoleToUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_name):
            body['RoleName'] = request.role_name
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantRoleToUsers',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/roles/grantusers',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GrantRoleToUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_role_to_users_with_options_async(
        self,
        request: data_lake_20200710_models.GrantRoleToUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GrantRoleToUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_name):
            body['RoleName'] = request.role_name
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantRoleToUsers',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/roles/grantusers',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GrantRoleToUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_role_to_users(
        self,
        request: data_lake_20200710_models.GrantRoleToUsersRequest,
    ) -> data_lake_20200710_models.GrantRoleToUsersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.grant_role_to_users_with_options(request, headers, runtime)

    async def grant_role_to_users_async(
        self,
        request: data_lake_20200710_models.GrantRoleToUsersRequest,
    ) -> data_lake_20200710_models.GrantRoleToUsersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.grant_role_to_users_with_options_async(request, headers, runtime)

    def grant_roles_to_user_with_options(
        self,
        request: data_lake_20200710_models.GrantRolesToUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GrantRolesToUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_names):
            body['RoleNames'] = request.role_names
        if not UtilClient.is_unset(request.user):
            body['User'] = request.user
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantRolesToUser',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/roles/grantroles',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GrantRolesToUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_roles_to_user_with_options_async(
        self,
        request: data_lake_20200710_models.GrantRolesToUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.GrantRolesToUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_names):
            body['RoleNames'] = request.role_names
        if not UtilClient.is_unset(request.user):
            body['User'] = request.user
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantRolesToUser',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/roles/grantroles',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.GrantRolesToUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_roles_to_user(
        self,
        request: data_lake_20200710_models.GrantRolesToUserRequest,
    ) -> data_lake_20200710_models.GrantRolesToUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.grant_roles_to_user_with_options(request, headers, runtime)

    async def grant_roles_to_user_async(
        self,
        request: data_lake_20200710_models.GrantRolesToUserRequest,
    ) -> data_lake_20200710_models.GrantRolesToUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.grant_roles_to_user_with_options_async(request, headers, runtime)

    def list_catalogs_with_options(
        self,
        request: data_lake_20200710_models.ListCatalogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListCatalogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id_pattern):
            query['IdPattern'] = request.id_pattern
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCatalogs',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListCatalogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_catalogs_with_options_async(
        self,
        request: data_lake_20200710_models.ListCatalogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListCatalogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id_pattern):
            query['IdPattern'] = request.id_pattern
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCatalogs',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListCatalogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_catalogs(
        self,
        request: data_lake_20200710_models.ListCatalogsRequest,
    ) -> data_lake_20200710_models.ListCatalogsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_catalogs_with_options(request, headers, runtime)

    async def list_catalogs_async(
        self,
        request: data_lake_20200710_models.ListCatalogsRequest,
    ) -> data_lake_20200710_models.ListCatalogsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_catalogs_with_options_async(request, headers, runtime)

    def list_databases_with_options(
        self,
        request: data_lake_20200710_models.ListDatabasesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListDatabasesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.name_pattern):
            query['NamePattern'] = request.name_pattern
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatabases',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_databases_with_options_async(
        self,
        request: data_lake_20200710_models.ListDatabasesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListDatabasesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.name_pattern):
            query['NamePattern'] = request.name_pattern
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatabases',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListDatabasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_databases(
        self,
        request: data_lake_20200710_models.ListDatabasesRequest,
    ) -> data_lake_20200710_models.ListDatabasesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_databases_with_options(request, headers, runtime)

    async def list_databases_async(
        self,
        request: data_lake_20200710_models.ListDatabasesRequest,
    ) -> data_lake_20200710_models.ListDatabasesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_databases_with_options_async(request, headers, runtime)

    def list_function_names_with_options(
        self,
        request: data_lake_20200710_models.ListFunctionNamesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListFunctionNamesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.function_name_pattern):
            query['FunctionNamePattern'] = request.function_name_pattern
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctionNames',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/functions/names',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListFunctionNamesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_function_names_with_options_async(
        self,
        request: data_lake_20200710_models.ListFunctionNamesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListFunctionNamesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.function_name_pattern):
            query['FunctionNamePattern'] = request.function_name_pattern
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctionNames',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/functions/names',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListFunctionNamesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_function_names(
        self,
        request: data_lake_20200710_models.ListFunctionNamesRequest,
    ) -> data_lake_20200710_models.ListFunctionNamesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_function_names_with_options(request, headers, runtime)

    async def list_function_names_async(
        self,
        request: data_lake_20200710_models.ListFunctionNamesRequest,
    ) -> data_lake_20200710_models.ListFunctionNamesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_function_names_with_options_async(request, headers, runtime)

    def list_functions_with_options(
        self,
        request: data_lake_20200710_models.ListFunctionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListFunctionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.function_name_pattern):
            query['FunctionNamePattern'] = request.function_name_pattern
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/functions/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListFunctionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_functions_with_options_async(
        self,
        request: data_lake_20200710_models.ListFunctionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListFunctionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.function_name_pattern):
            query['FunctionNamePattern'] = request.function_name_pattern
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/functions/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListFunctionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_functions(
        self,
        request: data_lake_20200710_models.ListFunctionsRequest,
    ) -> data_lake_20200710_models.ListFunctionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_functions_with_options(request, headers, runtime)

    async def list_functions_async(
        self,
        request: data_lake_20200710_models.ListFunctionsRequest,
    ) -> data_lake_20200710_models.ListFunctionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_functions_with_options_async(request, headers, runtime)

    def list_partition_names_with_options(
        self,
        request: data_lake_20200710_models.ListPartitionNamesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListPartitionNamesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.next_page_token):
            body['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.partial_part_values):
            body['PartialPartValues'] = request.partial_part_values
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPartitionNames',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/names',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListPartitionNamesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_partition_names_with_options_async(
        self,
        request: data_lake_20200710_models.ListPartitionNamesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListPartitionNamesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.next_page_token):
            body['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.partial_part_values):
            body['PartialPartValues'] = request.partial_part_values
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPartitionNames',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/names',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListPartitionNamesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_partition_names(
        self,
        request: data_lake_20200710_models.ListPartitionNamesRequest,
    ) -> data_lake_20200710_models.ListPartitionNamesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_partition_names_with_options(request, headers, runtime)

    async def list_partition_names_async(
        self,
        request: data_lake_20200710_models.ListPartitionNamesRequest,
    ) -> data_lake_20200710_models.ListPartitionNamesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_partition_names_with_options_async(request, headers, runtime)

    def list_partitions_with_options(
        self,
        request: data_lake_20200710_models.ListPartitionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListPartitionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.is_share_sd):
            body['IsShareSd'] = request.is_share_sd
        if not UtilClient.is_unset(request.next_page_token):
            body['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.partial_part_values):
            body['PartialPartValues'] = request.partial_part_values
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPartitions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListPartitionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_partitions_with_options_async(
        self,
        request: data_lake_20200710_models.ListPartitionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListPartitionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.is_share_sd):
            body['IsShareSd'] = request.is_share_sd
        if not UtilClient.is_unset(request.next_page_token):
            body['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.partial_part_values):
            body['PartialPartValues'] = request.partial_part_values
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPartitions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListPartitionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_partitions(
        self,
        request: data_lake_20200710_models.ListPartitionsRequest,
    ) -> data_lake_20200710_models.ListPartitionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_partitions_with_options(request, headers, runtime)

    async def list_partitions_async(
        self,
        request: data_lake_20200710_models.ListPartitionsRequest,
    ) -> data_lake_20200710_models.ListPartitionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_partitions_with_options_async(request, headers, runtime)

    def list_partitions_by_expr_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListPartitionsByExprResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListPartitionsByExpr',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/listbyexpr',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListPartitionsByExprResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_partitions_by_expr_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListPartitionsByExprResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListPartitionsByExpr',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/listbyexpr',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListPartitionsByExprResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_partitions_by_expr(self) -> data_lake_20200710_models.ListPartitionsByExprResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_partitions_by_expr_with_options(headers, runtime)

    async def list_partitions_by_expr_async(self) -> data_lake_20200710_models.ListPartitionsByExprResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_partitions_by_expr_with_options_async(headers, runtime)

    def list_partitions_by_filter_with_options(
        self,
        request: data_lake_20200710_models.ListPartitionsByFilterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListPartitionsByFilterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.is_share_sd):
            body['IsShareSd'] = request.is_share_sd
        if not UtilClient.is_unset(request.next_page_token):
            body['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPartitionsByFilter',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/listbyfilter',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListPartitionsByFilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_partitions_by_filter_with_options_async(
        self,
        request: data_lake_20200710_models.ListPartitionsByFilterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListPartitionsByFilterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.is_share_sd):
            body['IsShareSd'] = request.is_share_sd
        if not UtilClient.is_unset(request.next_page_token):
            body['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPartitionsByFilter',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/listbyfilter',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListPartitionsByFilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_partitions_by_filter(
        self,
        request: data_lake_20200710_models.ListPartitionsByFilterRequest,
    ) -> data_lake_20200710_models.ListPartitionsByFilterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_partitions_by_filter_with_options(request, headers, runtime)

    async def list_partitions_by_filter_async(
        self,
        request: data_lake_20200710_models.ListPartitionsByFilterRequest,
    ) -> data_lake_20200710_models.ListPartitionsByFilterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_partitions_by_filter_with_options_async(request, headers, runtime)

    def list_permissions_with_options(
        self,
        request: data_lake_20200710_models.ListPermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListPermissionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.is_list_user_role_permissions):
            body['IsListUserRolePermissions'] = request.is_list_user_role_permissions
        if not UtilClient.is_unset(request.meta_resource):
            body['MetaResource'] = request.meta_resource
        if not UtilClient.is_unset(request.meta_resource_type):
            body['MetaResourceType'] = request.meta_resource_type
        if not UtilClient.is_unset(request.next_page_token):
            body['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.principal):
            body['Principal'] = request.principal
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPermissions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/permissions/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_permissions_with_options_async(
        self,
        request: data_lake_20200710_models.ListPermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListPermissionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.is_list_user_role_permissions):
            body['IsListUserRolePermissions'] = request.is_list_user_role_permissions
        if not UtilClient.is_unset(request.meta_resource):
            body['MetaResource'] = request.meta_resource
        if not UtilClient.is_unset(request.meta_resource_type):
            body['MetaResourceType'] = request.meta_resource_type
        if not UtilClient.is_unset(request.next_page_token):
            body['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.principal):
            body['Principal'] = request.principal
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPermissions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/permissions/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_permissions(
        self,
        request: data_lake_20200710_models.ListPermissionsRequest,
    ) -> data_lake_20200710_models.ListPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_permissions_with_options(request, headers, runtime)

    async def list_permissions_async(
        self,
        request: data_lake_20200710_models.ListPermissionsRequest,
    ) -> data_lake_20200710_models.ListPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_permissions_with_options_async(request, headers, runtime)

    def list_role_users_with_options(
        self,
        request: data_lake_20200710_models.ListRoleUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListRoleUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        if not UtilClient.is_unset(request.user_name_pattern):
            query['UserNamePattern'] = request.user_name_pattern
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRoleUsers',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/roles/roleusers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListRoleUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_role_users_with_options_async(
        self,
        request: data_lake_20200710_models.ListRoleUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListRoleUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        if not UtilClient.is_unset(request.user_name_pattern):
            query['UserNamePattern'] = request.user_name_pattern
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRoleUsers',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/roles/roleusers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListRoleUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_role_users(
        self,
        request: data_lake_20200710_models.ListRoleUsersRequest,
    ) -> data_lake_20200710_models.ListRoleUsersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_role_users_with_options(request, headers, runtime)

    async def list_role_users_async(
        self,
        request: data_lake_20200710_models.ListRoleUsersRequest,
    ) -> data_lake_20200710_models.ListRoleUsersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_role_users_with_options_async(request, headers, runtime)

    def list_roles_with_options(
        self,
        request: data_lake_20200710_models.ListRolesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListRolesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.role_name_pattern):
            query['RoleNamePattern'] = request.role_name_pattern
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRoles',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/roles/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_roles_with_options_async(
        self,
        request: data_lake_20200710_models.ListRolesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListRolesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.role_name_pattern):
            query['RoleNamePattern'] = request.role_name_pattern
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRoles',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/roles/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_roles(
        self,
        request: data_lake_20200710_models.ListRolesRequest,
    ) -> data_lake_20200710_models.ListRolesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_roles_with_options(request, headers, runtime)

    async def list_roles_async(
        self,
        request: data_lake_20200710_models.ListRolesRequest,
    ) -> data_lake_20200710_models.ListRolesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_roles_with_options_async(request, headers, runtime)

    def list_table_names_with_options(
        self,
        request: data_lake_20200710_models.ListTableNamesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListTableNamesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.table_name_pattern):
            query['TableNamePattern'] = request.table_name_pattern
        if not UtilClient.is_unset(request.table_type):
            query['TableType'] = request.table_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTableNames',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/names',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListTableNamesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_table_names_with_options_async(
        self,
        request: data_lake_20200710_models.ListTableNamesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListTableNamesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.table_name_pattern):
            query['TableNamePattern'] = request.table_name_pattern
        if not UtilClient.is_unset(request.table_type):
            query['TableType'] = request.table_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTableNames',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/names',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListTableNamesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_table_names(
        self,
        request: data_lake_20200710_models.ListTableNamesRequest,
    ) -> data_lake_20200710_models.ListTableNamesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_table_names_with_options(request, headers, runtime)

    async def list_table_names_async(
        self,
        request: data_lake_20200710_models.ListTableNamesRequest,
    ) -> data_lake_20200710_models.ListTableNamesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_table_names_with_options_async(request, headers, runtime)

    def list_table_versions_with_options(
        self,
        request: data_lake_20200710_models.ListTableVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListTableVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTableVersions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/versions/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListTableVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_table_versions_with_options_async(
        self,
        request: data_lake_20200710_models.ListTableVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListTableVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTableVersions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/versions/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListTableVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_table_versions(
        self,
        request: data_lake_20200710_models.ListTableVersionsRequest,
    ) -> data_lake_20200710_models.ListTableVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_table_versions_with_options(request, headers, runtime)

    async def list_table_versions_async(
        self,
        request: data_lake_20200710_models.ListTableVersionsRequest,
    ) -> data_lake_20200710_models.ListTableVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_table_versions_with_options_async(request, headers, runtime)

    def list_tables_with_options(
        self,
        request: data_lake_20200710_models.ListTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.table_name_pattern):
            query['TableNamePattern'] = request.table_name_pattern
        if not UtilClient.is_unset(request.table_type):
            query['TableType'] = request.table_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTables',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/databases/tables/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tables_with_options_async(
        self,
        request: data_lake_20200710_models.ListTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.table_name_pattern):
            query['TableNamePattern'] = request.table_name_pattern
        if not UtilClient.is_unset(request.table_type):
            query['TableType'] = request.table_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTables',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/databases/tables/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tables(
        self,
        request: data_lake_20200710_models.ListTablesRequest,
    ) -> data_lake_20200710_models.ListTablesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tables_with_options(request, headers, runtime)

    async def list_tables_async(
        self,
        request: data_lake_20200710_models.ListTablesRequest,
    ) -> data_lake_20200710_models.ListTablesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tables_with_options_async(request, headers, runtime)

    def list_user_roles_with_options(
        self,
        request: data_lake_20200710_models.ListUserRolesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListUserRolesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.principal_arn):
            query['PrincipalArn'] = request.principal_arn
        if not UtilClient.is_unset(request.role_name_pattern):
            query['RoleNamePattern'] = request.role_name_pattern
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserRoles',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/roles/userroles',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListUserRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_roles_with_options_async(
        self,
        request: data_lake_20200710_models.ListUserRolesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.ListUserRolesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.principal_arn):
            query['PrincipalArn'] = request.principal_arn
        if not UtilClient.is_unset(request.role_name_pattern):
            query['RoleNamePattern'] = request.role_name_pattern
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserRoles',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/roles/userroles',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.ListUserRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_roles(
        self,
        request: data_lake_20200710_models.ListUserRolesRequest,
    ) -> data_lake_20200710_models.ListUserRolesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_user_roles_with_options(request, headers, runtime)

    async def list_user_roles_async(
        self,
        request: data_lake_20200710_models.ListUserRolesRequest,
    ) -> data_lake_20200710_models.ListUserRolesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_user_roles_with_options_async(request, headers, runtime)

    def refresh_lock_with_options(
        self,
        request: data_lake_20200710_models.RefreshLockRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.RefreshLockResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lock_id):
            query['LockId'] = request.lock_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshLock',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/locks',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.RefreshLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_lock_with_options_async(
        self,
        request: data_lake_20200710_models.RefreshLockRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.RefreshLockResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lock_id):
            query['LockId'] = request.lock_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshLock',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/locks',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.RefreshLockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_lock(
        self,
        request: data_lake_20200710_models.RefreshLockRequest,
    ) -> data_lake_20200710_models.RefreshLockResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.refresh_lock_with_options(request, headers, runtime)

    async def refresh_lock_async(
        self,
        request: data_lake_20200710_models.RefreshLockRequest,
    ) -> data_lake_20200710_models.RefreshLockResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.refresh_lock_with_options_async(request, headers, runtime)

    def register_location_with_options(
        self,
        request: data_lake_20200710_models.RegisterLocationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.RegisterLocationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.inventory_collect_enabled):
            body['InventoryCollectEnabled'] = request.inventory_collect_enabled
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.oss_log_collect_enabled):
            body['OssLogCollectEnabled'] = request.oss_log_collect_enabled
        if not UtilClient.is_unset(request.role_name):
            body['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RegisterLocation',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/webapi/locations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.RegisterLocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_location_with_options_async(
        self,
        request: data_lake_20200710_models.RegisterLocationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.RegisterLocationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.inventory_collect_enabled):
            body['InventoryCollectEnabled'] = request.inventory_collect_enabled
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.oss_log_collect_enabled):
            body['OssLogCollectEnabled'] = request.oss_log_collect_enabled
        if not UtilClient.is_unset(request.role_name):
            body['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RegisterLocation',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/webapi/locations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.RegisterLocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_location(
        self,
        request: data_lake_20200710_models.RegisterLocationRequest,
    ) -> data_lake_20200710_models.RegisterLocationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.register_location_with_options(request, headers, runtime)

    async def register_location_async(
        self,
        request: data_lake_20200710_models.RegisterLocationRequest,
    ) -> data_lake_20200710_models.RegisterLocationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.register_location_with_options_async(request, headers, runtime)

    def rename_partition_with_options(
        self,
        request: data_lake_20200710_models.RenamePartitionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.RenamePartitionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.partition_input):
            body['PartitionInput'] = request.partition_input
        if not UtilClient.is_unset(request.partition_values):
            body['PartitionValues'] = request.partition_values
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenamePartition',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/rename',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.RenamePartitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def rename_partition_with_options_async(
        self,
        request: data_lake_20200710_models.RenamePartitionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.RenamePartitionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.partition_input):
            body['PartitionInput'] = request.partition_input
        if not UtilClient.is_unset(request.partition_values):
            body['PartitionValues'] = request.partition_values
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenamePartition',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/rename',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.RenamePartitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rename_partition(
        self,
        request: data_lake_20200710_models.RenamePartitionRequest,
    ) -> data_lake_20200710_models.RenamePartitionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rename_partition_with_options(request, headers, runtime)

    async def rename_partition_async(
        self,
        request: data_lake_20200710_models.RenamePartitionRequest,
    ) -> data_lake_20200710_models.RenamePartitionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.rename_partition_with_options_async(request, headers, runtime)

    def rename_table_with_options(
        self,
        request: data_lake_20200710_models.RenameTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.RenameTableResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.is_async):
            body['IsAsync'] = request.is_async
        if not UtilClient.is_unset(request.table_input):
            body['TableInput'] = request.table_input
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenameTable',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/rename',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.RenameTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def rename_table_with_options_async(
        self,
        request: data_lake_20200710_models.RenameTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.RenameTableResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.is_async):
            body['IsAsync'] = request.is_async
        if not UtilClient.is_unset(request.table_input):
            body['TableInput'] = request.table_input
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenameTable',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/rename',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.RenameTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rename_table(
        self,
        request: data_lake_20200710_models.RenameTableRequest,
    ) -> data_lake_20200710_models.RenameTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rename_table_with_options(request, headers, runtime)

    async def rename_table_async(
        self,
        request: data_lake_20200710_models.RenameTableRequest,
    ) -> data_lake_20200710_models.RenameTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.rename_table_with_options_async(request, headers, runtime)

    def revoke_permissions_with_options(
        self,
        request: data_lake_20200710_models.RevokePermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.RevokePermissionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accesses):
            body['Accesses'] = request.accesses
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.delegate_accesses):
            body['DelegateAccesses'] = request.delegate_accesses
        if not UtilClient.is_unset(request.meta_resource):
            body['MetaResource'] = request.meta_resource
        if not UtilClient.is_unset(request.principal):
            body['Principal'] = request.principal
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokePermissions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/permissions/revoke',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.RevokePermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_permissions_with_options_async(
        self,
        request: data_lake_20200710_models.RevokePermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.RevokePermissionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accesses):
            body['Accesses'] = request.accesses
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.delegate_accesses):
            body['DelegateAccesses'] = request.delegate_accesses
        if not UtilClient.is_unset(request.meta_resource):
            body['MetaResource'] = request.meta_resource
        if not UtilClient.is_unset(request.principal):
            body['Principal'] = request.principal
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokePermissions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/permissions/revoke',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.RevokePermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_permissions(
        self,
        request: data_lake_20200710_models.RevokePermissionsRequest,
    ) -> data_lake_20200710_models.RevokePermissionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.revoke_permissions_with_options(request, headers, runtime)

    async def revoke_permissions_async(
        self,
        request: data_lake_20200710_models.RevokePermissionsRequest,
    ) -> data_lake_20200710_models.RevokePermissionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.revoke_permissions_with_options_async(request, headers, runtime)

    def revoke_role_from_users_with_options(
        self,
        request: data_lake_20200710_models.RevokeRoleFromUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.RevokeRoleFromUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_name):
            body['RoleName'] = request.role_name
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokeRoleFromUsers',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/roles/revokeusers',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.RevokeRoleFromUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_role_from_users_with_options_async(
        self,
        request: data_lake_20200710_models.RevokeRoleFromUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.RevokeRoleFromUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_name):
            body['RoleName'] = request.role_name
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokeRoleFromUsers',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/roles/revokeusers',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.RevokeRoleFromUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_role_from_users(
        self,
        request: data_lake_20200710_models.RevokeRoleFromUsersRequest,
    ) -> data_lake_20200710_models.RevokeRoleFromUsersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.revoke_role_from_users_with_options(request, headers, runtime)

    async def revoke_role_from_users_async(
        self,
        request: data_lake_20200710_models.RevokeRoleFromUsersRequest,
    ) -> data_lake_20200710_models.RevokeRoleFromUsersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.revoke_role_from_users_with_options_async(request, headers, runtime)

    def revoke_roles_from_user_with_options(
        self,
        request: data_lake_20200710_models.RevokeRolesFromUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.RevokeRolesFromUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_names):
            body['RoleNames'] = request.role_names
        if not UtilClient.is_unset(request.user):
            body['User'] = request.user
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokeRolesFromUser',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/roles/revokeroles',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.RevokeRolesFromUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_roles_from_user_with_options_async(
        self,
        request: data_lake_20200710_models.RevokeRolesFromUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.RevokeRolesFromUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_names):
            body['RoleNames'] = request.role_names
        if not UtilClient.is_unset(request.user):
            body['User'] = request.user
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokeRolesFromUser',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/roles/revokeroles',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.RevokeRolesFromUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_roles_from_user(
        self,
        request: data_lake_20200710_models.RevokeRolesFromUserRequest,
    ) -> data_lake_20200710_models.RevokeRolesFromUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.revoke_roles_from_user_with_options(request, headers, runtime)

    async def revoke_roles_from_user_async(
        self,
        request: data_lake_20200710_models.RevokeRolesFromUserRequest,
    ) -> data_lake_20200710_models.RevokeRolesFromUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.revoke_roles_from_user_with_options_async(request, headers, runtime)

    def run_migration_workflow_with_options(
        self,
        request: data_lake_20200710_models.RunMigrationWorkflowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.RunMigrationWorkflowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunMigrationWorkflow',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/webapi/migration/workflow/run',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.RunMigrationWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_migration_workflow_with_options_async(
        self,
        request: data_lake_20200710_models.RunMigrationWorkflowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.RunMigrationWorkflowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunMigrationWorkflow',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/webapi/migration/workflow/run',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.RunMigrationWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_migration_workflow(
        self,
        request: data_lake_20200710_models.RunMigrationWorkflowRequest,
    ) -> data_lake_20200710_models.RunMigrationWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_migration_workflow_with_options(request, headers, runtime)

    async def run_migration_workflow_async(
        self,
        request: data_lake_20200710_models.RunMigrationWorkflowRequest,
    ) -> data_lake_20200710_models.RunMigrationWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_migration_workflow_with_options_async(request, headers, runtime)

    def search_with_options(
        self,
        request: data_lake_20200710_models.SearchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.SearchResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_text):
            body['SearchText'] = request.search_text
        if not UtilClient.is_unset(request.search_type):
            body['SearchType'] = request.search_type
        if not UtilClient.is_unset(request.sort_criteria):
            body['SortCriteria'] = request.sort_criteria
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Search',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.SearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_with_options_async(
        self,
        request: data_lake_20200710_models.SearchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.SearchResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_text):
            body['SearchText'] = request.search_text
        if not UtilClient.is_unset(request.search_type):
            body['SearchType'] = request.search_type
        if not UtilClient.is_unset(request.sort_criteria):
            body['SortCriteria'] = request.sort_criteria
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Search',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.SearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search(
        self,
        request: data_lake_20200710_models.SearchRequest,
    ) -> data_lake_20200710_models.SearchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_with_options(request, headers, runtime)

    async def search_async(
        self,
        request: data_lake_20200710_models.SearchRequest,
    ) -> data_lake_20200710_models.SearchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.search_with_options_async(request, headers, runtime)

    def search_across_catalog_with_options(
        self,
        request: data_lake_20200710_models.SearchAcrossCatalogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.SearchAcrossCatalogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_ids):
            body['CatalogIds'] = request.catalog_ids
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_text):
            body['SearchText'] = request.search_text
        if not UtilClient.is_unset(request.search_types):
            body['SearchTypes'] = request.search_types
        if not UtilClient.is_unset(request.sort_criteria):
            body['SortCriteria'] = request.sort_criteria
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchAcrossCatalog',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/search/search-across-catalog',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.SearchAcrossCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_across_catalog_with_options_async(
        self,
        request: data_lake_20200710_models.SearchAcrossCatalogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.SearchAcrossCatalogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_ids):
            body['CatalogIds'] = request.catalog_ids
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_text):
            body['SearchText'] = request.search_text
        if not UtilClient.is_unset(request.search_types):
            body['SearchTypes'] = request.search_types
        if not UtilClient.is_unset(request.sort_criteria):
            body['SortCriteria'] = request.sort_criteria
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchAcrossCatalog',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/search/search-across-catalog',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.SearchAcrossCatalogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_across_catalog(
        self,
        request: data_lake_20200710_models.SearchAcrossCatalogRequest,
    ) -> data_lake_20200710_models.SearchAcrossCatalogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_across_catalog_with_options(request, headers, runtime)

    async def search_across_catalog_async(
        self,
        request: data_lake_20200710_models.SearchAcrossCatalogRequest,
    ) -> data_lake_20200710_models.SearchAcrossCatalogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.search_across_catalog_with_options_async(request, headers, runtime)

    def stop_migration_workflow_with_options(
        self,
        request: data_lake_20200710_models.StopMigrationWorkflowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.StopMigrationWorkflowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopMigrationWorkflow',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/webapi/migration/workflow/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.StopMigrationWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_migration_workflow_with_options_async(
        self,
        request: data_lake_20200710_models.StopMigrationWorkflowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.StopMigrationWorkflowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopMigrationWorkflow',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/webapi/migration/workflow/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.StopMigrationWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_migration_workflow(
        self,
        request: data_lake_20200710_models.StopMigrationWorkflowRequest,
    ) -> data_lake_20200710_models.StopMigrationWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_migration_workflow_with_options(request, headers, runtime)

    async def stop_migration_workflow_async(
        self,
        request: data_lake_20200710_models.StopMigrationWorkflowRequest,
    ) -> data_lake_20200710_models.StopMigrationWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_migration_workflow_with_options_async(request, headers, runtime)

    def submit_query_with_options(
        self,
        request: data_lake_20200710_models.SubmitQueryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.SubmitQueryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['catalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.sql):
            body['sql'] = request.sql
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitQuery',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/webapi/query/submitQueryRequestBody',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.SubmitQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_query_with_options_async(
        self,
        request: data_lake_20200710_models.SubmitQueryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.SubmitQueryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['catalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.sql):
            body['sql'] = request.sql
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitQuery',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/webapi/query/submitQueryRequestBody',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.SubmitQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_query(
        self,
        request: data_lake_20200710_models.SubmitQueryRequest,
    ) -> data_lake_20200710_models.SubmitQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_query_with_options(request, headers, runtime)

    async def submit_query_async(
        self,
        request: data_lake_20200710_models.SubmitQueryRequest,
    ) -> data_lake_20200710_models.SubmitQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.submit_query_with_options_async(request, headers, runtime)

    def un_lock_with_options(
        self,
        request: data_lake_20200710_models.UnLockRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.UnLockResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lock_id):
            query['LockId'] = request.lock_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnLock',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/locks',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UnLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_lock_with_options_async(
        self,
        request: data_lake_20200710_models.UnLockRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.UnLockResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lock_id):
            query['LockId'] = request.lock_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnLock',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/locks',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UnLockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_lock(
        self,
        request: data_lake_20200710_models.UnLockRequest,
    ) -> data_lake_20200710_models.UnLockResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.un_lock_with_options(request, headers, runtime)

    async def un_lock_async(
        self,
        request: data_lake_20200710_models.UnLockRequest,
    ) -> data_lake_20200710_models.UnLockResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.un_lock_with_options_async(request, headers, runtime)

    def update_catalog_with_options(
        self,
        request: data_lake_20200710_models.UpdateCatalogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.UpdateCatalogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_input):
            body['CatalogInput'] = request.catalog_input
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCatalog',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdateCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_catalog_with_options_async(
        self,
        request: data_lake_20200710_models.UpdateCatalogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.UpdateCatalogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_input):
            body['CatalogInput'] = request.catalog_input
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCatalog',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdateCatalogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_catalog(
        self,
        request: data_lake_20200710_models.UpdateCatalogRequest,
    ) -> data_lake_20200710_models.UpdateCatalogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_catalog_with_options(request, headers, runtime)

    async def update_catalog_async(
        self,
        request: data_lake_20200710_models.UpdateCatalogRequest,
    ) -> data_lake_20200710_models.UpdateCatalogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_catalog_with_options_async(request, headers, runtime)

    def update_catalog_settings_with_options(
        self,
        request: data_lake_20200710_models.UpdateCatalogSettingsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.UpdateCatalogSettingsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.catalog_settings):
            body['CatalogSettings'] = request.catalog_settings
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCatalogSettings',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/settings',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdateCatalogSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_catalog_settings_with_options_async(
        self,
        request: data_lake_20200710_models.UpdateCatalogSettingsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.UpdateCatalogSettingsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.catalog_settings):
            body['CatalogSettings'] = request.catalog_settings
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCatalogSettings',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/settings',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdateCatalogSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_catalog_settings(
        self,
        request: data_lake_20200710_models.UpdateCatalogSettingsRequest,
    ) -> data_lake_20200710_models.UpdateCatalogSettingsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_catalog_settings_with_options(request, headers, runtime)

    async def update_catalog_settings_async(
        self,
        request: data_lake_20200710_models.UpdateCatalogSettingsRequest,
    ) -> data_lake_20200710_models.UpdateCatalogSettingsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_catalog_settings_with_options_async(request, headers, runtime)

    def update_database_with_options(
        self,
        request: data_lake_20200710_models.UpdateDatabaseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.UpdateDatabaseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_input):
            body['DatabaseInput'] = request.database_input
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDatabase',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdateDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_database_with_options_async(
        self,
        request: data_lake_20200710_models.UpdateDatabaseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.UpdateDatabaseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_input):
            body['DatabaseInput'] = request.database_input
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDatabase',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdateDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_database(
        self,
        request: data_lake_20200710_models.UpdateDatabaseRequest,
    ) -> data_lake_20200710_models.UpdateDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_database_with_options(request, headers, runtime)

    async def update_database_async(
        self,
        request: data_lake_20200710_models.UpdateDatabaseRequest,
    ) -> data_lake_20200710_models.UpdateDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_database_with_options_async(request, headers, runtime)

    def update_function_with_options(
        self,
        request: data_lake_20200710_models.UpdateFunctionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.UpdateFunctionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.function_input):
            body['FunctionInput'] = request.function_input
        if not UtilClient.is_unset(request.function_name):
            body['FunctionName'] = request.function_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFunction',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/functions',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdateFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_function_with_options_async(
        self,
        request: data_lake_20200710_models.UpdateFunctionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.UpdateFunctionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.function_input):
            body['FunctionInput'] = request.function_input
        if not UtilClient.is_unset(request.function_name):
            body['FunctionName'] = request.function_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFunction',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/functions',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdateFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_function(
        self,
        request: data_lake_20200710_models.UpdateFunctionRequest,
    ) -> data_lake_20200710_models.UpdateFunctionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_function_with_options(request, headers, runtime)

    async def update_function_async(
        self,
        request: data_lake_20200710_models.UpdateFunctionRequest,
    ) -> data_lake_20200710_models.UpdateFunctionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_function_with_options_async(request, headers, runtime)

    def update_partition_column_statistics_with_options(
        self,
        request: data_lake_20200710_models.UpdatePartitionColumnStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.UpdatePartitionColumnStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.update_table_partition_column_statistics_request)
        )
        params = open_api_models.Params(
            action='UpdatePartitionColumnStatistics',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/columnstatistics',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdatePartitionColumnStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_partition_column_statistics_with_options_async(
        self,
        request: data_lake_20200710_models.UpdatePartitionColumnStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.UpdatePartitionColumnStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.update_table_partition_column_statistics_request)
        )
        params = open_api_models.Params(
            action='UpdatePartitionColumnStatistics',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/partitions/columnstatistics',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdatePartitionColumnStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_partition_column_statistics(
        self,
        request: data_lake_20200710_models.UpdatePartitionColumnStatisticsRequest,
    ) -> data_lake_20200710_models.UpdatePartitionColumnStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_partition_column_statistics_with_options(request, headers, runtime)

    async def update_partition_column_statistics_async(
        self,
        request: data_lake_20200710_models.UpdatePartitionColumnStatisticsRequest,
    ) -> data_lake_20200710_models.UpdatePartitionColumnStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_partition_column_statistics_with_options_async(request, headers, runtime)

    def update_permissions_with_options(
        self,
        request: data_lake_20200710_models.UpdatePermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.UpdatePermissionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accesses):
            body['Accesses'] = request.accesses
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.delegate_accesses):
            body['DelegateAccesses'] = request.delegate_accesses
        if not UtilClient.is_unset(request.meta_resource):
            body['MetaResource'] = request.meta_resource
        if not UtilClient.is_unset(request.principal):
            body['Principal'] = request.principal
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePermissions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/permissions/',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdatePermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_permissions_with_options_async(
        self,
        request: data_lake_20200710_models.UpdatePermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.UpdatePermissionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accesses):
            body['Accesses'] = request.accesses
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.delegate_accesses):
            body['DelegateAccesses'] = request.delegate_accesses
        if not UtilClient.is_unset(request.meta_resource):
            body['MetaResource'] = request.meta_resource
        if not UtilClient.is_unset(request.principal):
            body['Principal'] = request.principal
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePermissions',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/permissions/',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdatePermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_permissions(
        self,
        request: data_lake_20200710_models.UpdatePermissionsRequest,
    ) -> data_lake_20200710_models.UpdatePermissionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_permissions_with_options(request, headers, runtime)

    async def update_permissions_async(
        self,
        request: data_lake_20200710_models.UpdatePermissionsRequest,
    ) -> data_lake_20200710_models.UpdatePermissionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_permissions_with_options_async(request, headers, runtime)

    def update_registered_location_with_options(
        self,
        request: data_lake_20200710_models.UpdateRegisteredLocationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.UpdateRegisteredLocationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.inventory_collect_enabled):
            body['InventoryCollectEnabled'] = request.inventory_collect_enabled
        if not UtilClient.is_unset(request.location_id):
            body['LocationId'] = request.location_id
        if not UtilClient.is_unset(request.oss_log_collect_enabled):
            body['OssLogCollectEnabled'] = request.oss_log_collect_enabled
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRegisteredLocation',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/webapi/locations',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdateRegisteredLocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_registered_location_with_options_async(
        self,
        request: data_lake_20200710_models.UpdateRegisteredLocationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.UpdateRegisteredLocationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.inventory_collect_enabled):
            body['InventoryCollectEnabled'] = request.inventory_collect_enabled
        if not UtilClient.is_unset(request.location_id):
            body['LocationId'] = request.location_id
        if not UtilClient.is_unset(request.oss_log_collect_enabled):
            body['OssLogCollectEnabled'] = request.oss_log_collect_enabled
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRegisteredLocation',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/webapi/locations',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdateRegisteredLocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_registered_location(
        self,
        request: data_lake_20200710_models.UpdateRegisteredLocationRequest,
    ) -> data_lake_20200710_models.UpdateRegisteredLocationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_registered_location_with_options(request, headers, runtime)

    async def update_registered_location_async(
        self,
        request: data_lake_20200710_models.UpdateRegisteredLocationRequest,
    ) -> data_lake_20200710_models.UpdateRegisteredLocationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_registered_location_with_options_async(request, headers, runtime)

    def update_role_with_options(
        self,
        request: data_lake_20200710_models.UpdateRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.UpdateRoleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_input):
            body['RoleInput'] = request.role_input
        if not UtilClient.is_unset(request.role_name):
            body['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRole',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/roles',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdateRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_role_with_options_async(
        self,
        request: data_lake_20200710_models.UpdateRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.UpdateRoleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_input):
            body['RoleInput'] = request.role_input
        if not UtilClient.is_unset(request.role_name):
            body['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRole',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/roles',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdateRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_role(
        self,
        request: data_lake_20200710_models.UpdateRoleRequest,
    ) -> data_lake_20200710_models.UpdateRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_role_with_options(request, headers, runtime)

    async def update_role_async(
        self,
        request: data_lake_20200710_models.UpdateRoleRequest,
    ) -> data_lake_20200710_models.UpdateRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_role_with_options_async(request, headers, runtime)

    def update_role_users_with_options(
        self,
        request: data_lake_20200710_models.UpdateRoleUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.UpdateRoleUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_name):
            body['RoleName'] = request.role_name
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRoleUsers',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/updateroleusers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdateRoleUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_role_users_with_options_async(
        self,
        request: data_lake_20200710_models.UpdateRoleUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.UpdateRoleUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_name):
            body['RoleName'] = request.role_name
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRoleUsers',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/auth/updateroleusers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdateRoleUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_role_users(
        self,
        request: data_lake_20200710_models.UpdateRoleUsersRequest,
    ) -> data_lake_20200710_models.UpdateRoleUsersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_role_users_with_options(request, headers, runtime)

    async def update_role_users_async(
        self,
        request: data_lake_20200710_models.UpdateRoleUsersRequest,
    ) -> data_lake_20200710_models.UpdateRoleUsersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_role_users_with_options_async(request, headers, runtime)

    def update_table_with_options(
        self,
        request: data_lake_20200710_models.UpdateTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.UpdateTableResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.allow_partition_key_change):
            body['AllowPartitionKeyChange'] = request.allow_partition_key_change
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.is_async):
            body['IsAsync'] = request.is_async
        if not UtilClient.is_unset(request.skip_archive):
            body['SkipArchive'] = request.skip_archive
        if not UtilClient.is_unset(request.table_input):
            body['TableInput'] = request.table_input
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTable',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdateTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_table_with_options_async(
        self,
        request: data_lake_20200710_models.UpdateTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.UpdateTableResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.allow_partition_key_change):
            body['AllowPartitionKeyChange'] = request.allow_partition_key_change
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.is_async):
            body['IsAsync'] = request.is_async
        if not UtilClient.is_unset(request.skip_archive):
            body['SkipArchive'] = request.skip_archive
        if not UtilClient.is_unset(request.table_input):
            body['TableInput'] = request.table_input
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTable',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdateTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_table(
        self,
        request: data_lake_20200710_models.UpdateTableRequest,
    ) -> data_lake_20200710_models.UpdateTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_table_with_options(request, headers, runtime)

    async def update_table_async(
        self,
        request: data_lake_20200710_models.UpdateTableRequest,
    ) -> data_lake_20200710_models.UpdateTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_table_with_options_async(request, headers, runtime)

    def update_table_column_statistics_with_options(
        self,
        request: data_lake_20200710_models.UpdateTableColumnStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.UpdateTableColumnStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.update_table_partition_column_statistics_request)
        )
        params = open_api_models.Params(
            action='UpdateTableColumnStatistics',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/columnstatistics',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdateTableColumnStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_table_column_statistics_with_options_async(
        self,
        request: data_lake_20200710_models.UpdateTableColumnStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_lake_20200710_models.UpdateTableColumnStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.update_table_partition_column_statistics_request)
        )
        params = open_api_models.Params(
            action='UpdateTableColumnStatistics',
            version='2020-07-10',
            protocol='HTTPS',
            pathname=f'/api/metastore/catalogs/databases/tables/columnstatistics',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_lake_20200710_models.UpdateTableColumnStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_table_column_statistics(
        self,
        request: data_lake_20200710_models.UpdateTableColumnStatisticsRequest,
    ) -> data_lake_20200710_models.UpdateTableColumnStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_table_column_statistics_with_options(request, headers, runtime)

    async def update_table_column_statistics_async(
        self,
        request: data_lake_20200710_models.UpdateTableColumnStatisticsRequest,
    ) -> data_lake_20200710_models.UpdateTableColumnStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_table_column_statistics_with_options_async(request, headers, runtime)
