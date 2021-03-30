# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_openanalytics_open20200928 import models as openanalytics_open_20200928_models
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
        self._endpoint_rule = 'central'
        self._endpoint_map = {
            'cn-beijing': 'openanalytics.cn-beijing.aliyuncs.com',
            'cn-zhangjiakou': 'openanalytics.cn-zhangjiakou.aliyuncs.com',
            'cn-hangzhou': 'openanalytics.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'openanalytics.cn-shanghai.aliyuncs.com',
            'cn-shenzhen': 'openanalytics.cn-shenzhen.aliyuncs.com',
            'cn-hongkong': 'openanalytics.cn-hongkong.aliyuncs.com',
            'ap-southeast-1': 'openanalytics.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'datalakeanalytics.ap-southeast-2.aliyuncs.com',
            'ap-southeast-3': 'openanalytics.ap-southeast-3.aliyuncs.com',
            'ap-northeast-1': 'datalakeanalytics.ap-northeast-1.aliyuncs.com',
            'eu-west-1': 'openanalytics.eu-west-1.aliyuncs.com',
            'us-west-1': 'openanalytics.us-west-1.aliyuncs.com',
            'us-east-1': 'datalakeanalytics.us-east-1.aliyuncs.com',
            'eu-central-1': 'datalakeanalytics.eu-central-1.aliyuncs.com',
            'ap-south-1': 'openanalytics.ap-south-1.aliyuncs.com',
            'ap-northeast-2-pop': 'openanalytics.ap-northeast-1.aliyuncs.com',
            'ap-southeast-5': 'openanalytics.ap-southeast-5.aliyuncs.com',
            'cn-beijing-finance-1': 'openanalytics.aliyuncs.com',
            'cn-beijing-finance-pop': 'openanalytics.aliyuncs.com',
            'cn-beijing-gov-1': 'openanalytics.aliyuncs.com',
            'cn-beijing-nu16-b01': 'openanalytics.aliyuncs.com',
            'cn-chengdu': 'openanalytics.aliyuncs.com',
            'cn-edge-1': 'openanalytics.aliyuncs.com',
            'cn-fujian': 'openanalytics.aliyuncs.com',
            'cn-haidian-cm12-c01': 'openanalytics.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'openanalytics.aliyuncs.com',
            'cn-hangzhou-finance': 'openanalytics.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'openanalytics.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'openanalytics.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'openanalytics.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'openanalytics.aliyuncs.com',
            'cn-hangzhou-test-306': 'openanalytics.aliyuncs.com',
            'cn-hongkong-finance-pop': 'openanalytics.aliyuncs.com',
            'cn-huhehaote': 'openanalytics.cn-huhehaote.aliyuncs.com',
            'cn-north-2-gov-1': 'openanalytics.aliyuncs.com',
            'cn-qingdao': 'openanalytics.cn-qingdao.aliyuncs.com',
            'cn-qingdao-nebula': 'openanalytics.aliyuncs.com',
            'cn-shanghai-et15-b01': 'openanalytics.aliyuncs.com',
            'cn-shanghai-et2-b01': 'openanalytics.aliyuncs.com',
            'cn-shanghai-finance-1': 'openanalytics.aliyuncs.com',
            'cn-shanghai-inner': 'openanalytics.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'openanalytics.aliyuncs.com',
            'cn-shenzhen-finance-1': 'openanalytics.aliyuncs.com',
            'cn-shenzhen-inner': 'openanalytics.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'openanalytics.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'openanalytics.aliyuncs.com',
            'cn-wuhan': 'openanalytics.aliyuncs.com',
            'cn-yushanfang': 'openanalytics.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'openanalytics.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'openanalytics.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'openanalytics.aliyuncs.com',
            'eu-west-1-oxs': 'openanalytics.ap-northeast-1.aliyuncs.com',
            'me-east-1': 'openanalytics.me-east-1.aliyuncs.com',
            'rus-west-1-pop': 'openanalytics.ap-northeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('openanalytics-open', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_partitions_with_options(
        self,
        tmp_req: openanalytics_open_20200928_models.AddPartitionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.AddPartitionsResponse:
        UtilClient.validate_model(tmp_req)
        request = openanalytics_open_20200928_models.AddPartitionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.partition):
            request.partition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.partition, 'Partition', 'json')
        query = {}
        query['Partition'] = request.partition_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddPartitions',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.AddPartitionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_partitions_with_options_async(
        self,
        tmp_req: openanalytics_open_20200928_models.AddPartitionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.AddPartitionsResponse:
        UtilClient.validate_model(tmp_req)
        request = openanalytics_open_20200928_models.AddPartitionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.partition):
            request.partition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.partition, 'Partition', 'json')
        query = {}
        query['Partition'] = request.partition_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddPartitions',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.AddPartitionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_partitions(
        self,
        request: openanalytics_open_20200928_models.AddPartitionsRequest,
    ) -> openanalytics_open_20200928_models.AddPartitionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_partitions_with_options(request, runtime)

    async def add_partitions_async(
        self,
        request: openanalytics_open_20200928_models.AddPartitionsRequest,
    ) -> openanalytics_open_20200928_models.AddPartitionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_partitions_with_options_async(request, runtime)

    def alter_database_with_options(
        self,
        tmp_req: openanalytics_open_20200928_models.AlterDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.AlterDatabaseResponse:
        UtilClient.validate_model(tmp_req)
        request = openanalytics_open_20200928_models.AlterDatabaseShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        query['Name'] = request.name
        query['Description'] = request.description
        query['LocationUri'] = request.location_uri
        query['OldDbName'] = request.old_db_name
        query['Parameters'] = request.parameters_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AlterDatabase',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.AlterDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def alter_database_with_options_async(
        self,
        tmp_req: openanalytics_open_20200928_models.AlterDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.AlterDatabaseResponse:
        UtilClient.validate_model(tmp_req)
        request = openanalytics_open_20200928_models.AlterDatabaseShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        query['Name'] = request.name
        query['Description'] = request.description
        query['LocationUri'] = request.location_uri
        query['OldDbName'] = request.old_db_name
        query['Parameters'] = request.parameters_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AlterDatabase',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.AlterDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def alter_database(
        self,
        request: openanalytics_open_20200928_models.AlterDatabaseRequest,
    ) -> openanalytics_open_20200928_models.AlterDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.alter_database_with_options(request, runtime)

    async def alter_database_async(
        self,
        request: openanalytics_open_20200928_models.AlterDatabaseRequest,
    ) -> openanalytics_open_20200928_models.AlterDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.alter_database_with_options_async(request, runtime)

    def alter_table_with_options(
        self,
        tmp_req: openanalytics_open_20200928_models.AlterTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.AlterTableResponse:
        UtilClient.validate_model(tmp_req)
        request = openanalytics_open_20200928_models.AlterTableShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        if not UtilClient.is_unset(tmp_req.col):
            request.col_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.col, 'Col', 'json')
        query = {}
        query['OldDbName'] = request.old_db_name
        query['OldTableName'] = request.old_table_name
        query['NewDbName'] = request.new_db_name
        query['NewTableName'] = request.new_table_name
        query['Parameters'] = request.parameters_shrink
        query['Col'] = request.col_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AlterTable',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.AlterTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def alter_table_with_options_async(
        self,
        tmp_req: openanalytics_open_20200928_models.AlterTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.AlterTableResponse:
        UtilClient.validate_model(tmp_req)
        request = openanalytics_open_20200928_models.AlterTableShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        if not UtilClient.is_unset(tmp_req.col):
            request.col_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.col, 'Col', 'json')
        query = {}
        query['OldDbName'] = request.old_db_name
        query['OldTableName'] = request.old_table_name
        query['NewDbName'] = request.new_db_name
        query['NewTableName'] = request.new_table_name
        query['Parameters'] = request.parameters_shrink
        query['Col'] = request.col_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AlterTable',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.AlterTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def alter_table(
        self,
        request: openanalytics_open_20200928_models.AlterTableRequest,
    ) -> openanalytics_open_20200928_models.AlterTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.alter_table_with_options(request, runtime)

    async def alter_table_async(
        self,
        request: openanalytics_open_20200928_models.AlterTableRequest,
    ) -> openanalytics_open_20200928_models.AlterTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.alter_table_with_options_async(request, runtime)

    def create_database_with_options(
        self,
        tmp_req: openanalytics_open_20200928_models.CreateDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.CreateDatabaseResponse:
        UtilClient.validate_model(tmp_req)
        request = openanalytics_open_20200928_models.CreateDatabaseShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        query['Name'] = request.name
        query['Description'] = request.description
        query['LocationUri'] = request.location_uri
        query['Parameters'] = request.parameters_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDatabase',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.CreateDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_database_with_options_async(
        self,
        tmp_req: openanalytics_open_20200928_models.CreateDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.CreateDatabaseResponse:
        UtilClient.validate_model(tmp_req)
        request = openanalytics_open_20200928_models.CreateDatabaseShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        query['Name'] = request.name
        query['Description'] = request.description
        query['LocationUri'] = request.location_uri
        query['Parameters'] = request.parameters_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDatabase',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.CreateDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_database(
        self,
        request: openanalytics_open_20200928_models.CreateDatabaseRequest,
    ) -> openanalytics_open_20200928_models.CreateDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_database_with_options(request, runtime)

    async def create_database_async(
        self,
        request: openanalytics_open_20200928_models.CreateDatabaseRequest,
    ) -> openanalytics_open_20200928_models.CreateDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_database_with_options_async(request, runtime)

    def create_table_with_options(
        self,
        tmp_req: openanalytics_open_20200928_models.CreateTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.CreateTableResponse:
        UtilClient.validate_model(tmp_req)
        request = openanalytics_open_20200928_models.CreateTableShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.partition_keys):
            request.partition_keys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.partition_keys, 'PartitionKeys', 'json')
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        if not UtilClient.is_unset(tmp_req.storage_descriptor):
            request.storage_descriptor_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.storage_descriptor), 'StorageDescriptor', 'json')
        query = {}
        query['DbName'] = request.db_name
        query['TableName'] = request.table_name
        query['PartitionKeys'] = request.partition_keys_shrink
        query['Parameters'] = request.parameters_shrink
        query['StorageDescriptor'] = request.storage_descriptor_shrink
        query['ViewOriginalText'] = request.view_original_text
        query['ViewExpandedText'] = request.view_expanded_text
        query['TableType'] = request.table_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateTable',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.CreateTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_table_with_options_async(
        self,
        tmp_req: openanalytics_open_20200928_models.CreateTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.CreateTableResponse:
        UtilClient.validate_model(tmp_req)
        request = openanalytics_open_20200928_models.CreateTableShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.partition_keys):
            request.partition_keys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.partition_keys, 'PartitionKeys', 'json')
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        if not UtilClient.is_unset(tmp_req.storage_descriptor):
            request.storage_descriptor_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.storage_descriptor), 'StorageDescriptor', 'json')
        query = {}
        query['DbName'] = request.db_name
        query['TableName'] = request.table_name
        query['PartitionKeys'] = request.partition_keys_shrink
        query['Parameters'] = request.parameters_shrink
        query['StorageDescriptor'] = request.storage_descriptor_shrink
        query['ViewOriginalText'] = request.view_original_text
        query['ViewExpandedText'] = request.view_expanded_text
        query['TableType'] = request.table_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateTable',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.CreateTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_table(
        self,
        request: openanalytics_open_20200928_models.CreateTableRequest,
    ) -> openanalytics_open_20200928_models.CreateTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_table_with_options(request, runtime)

    async def create_table_async(
        self,
        request: openanalytics_open_20200928_models.CreateTableRequest,
    ) -> openanalytics_open_20200928_models.CreateTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_table_with_options_async(request, runtime)

    def drop_database_with_options(
        self,
        request: openanalytics_open_20200928_models.DropDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.DropDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['Cascade'] = request.cascade
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DropDatabase',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.DropDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def drop_database_with_options_async(
        self,
        request: openanalytics_open_20200928_models.DropDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.DropDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['Cascade'] = request.cascade
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DropDatabase',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.DropDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def drop_database(
        self,
        request: openanalytics_open_20200928_models.DropDatabaseRequest,
    ) -> openanalytics_open_20200928_models.DropDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.drop_database_with_options(request, runtime)

    async def drop_database_async(
        self,
        request: openanalytics_open_20200928_models.DropDatabaseRequest,
    ) -> openanalytics_open_20200928_models.DropDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.drop_database_with_options_async(request, runtime)

    def drop_partition_with_options(
        self,
        tmp_req: openanalytics_open_20200928_models.DropPartitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.DropPartitionResponse:
        UtilClient.validate_model(tmp_req)
        request = openanalytics_open_20200928_models.DropPartitionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.part_values):
            request.part_values_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.part_values, 'PartValues', 'json')
        query = {}
        query['DbName'] = request.db_name
        query['TableName'] = request.table_name
        query['PartValues'] = request.part_values_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DropPartition',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.DropPartitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def drop_partition_with_options_async(
        self,
        tmp_req: openanalytics_open_20200928_models.DropPartitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.DropPartitionResponse:
        UtilClient.validate_model(tmp_req)
        request = openanalytics_open_20200928_models.DropPartitionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.part_values):
            request.part_values_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.part_values, 'PartValues', 'json')
        query = {}
        query['DbName'] = request.db_name
        query['TableName'] = request.table_name
        query['PartValues'] = request.part_values_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DropPartition',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.DropPartitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def drop_partition(
        self,
        request: openanalytics_open_20200928_models.DropPartitionRequest,
    ) -> openanalytics_open_20200928_models.DropPartitionResponse:
        runtime = util_models.RuntimeOptions()
        return self.drop_partition_with_options(request, runtime)

    async def drop_partition_async(
        self,
        request: openanalytics_open_20200928_models.DropPartitionRequest,
    ) -> openanalytics_open_20200928_models.DropPartitionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.drop_partition_with_options_async(request, runtime)

    def drop_table_with_options(
        self,
        request: openanalytics_open_20200928_models.DropTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.DropTableResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DropTable',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.DropTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def drop_table_with_options_async(
        self,
        request: openanalytics_open_20200928_models.DropTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.DropTableResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DropTable',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.DropTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def drop_table(
        self,
        request: openanalytics_open_20200928_models.DropTableRequest,
    ) -> openanalytics_open_20200928_models.DropTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.drop_table_with_options(request, runtime)

    async def drop_table_async(
        self,
        request: openanalytics_open_20200928_models.DropTableRequest,
    ) -> openanalytics_open_20200928_models.DropTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.drop_table_with_options_async(request, runtime)

    def get_all_databases_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.GetAllDatabasesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAllDatabases',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.GetAllDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_all_databases_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.GetAllDatabasesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAllDatabases',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.GetAllDatabasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_all_databases(self) -> openanalytics_open_20200928_models.GetAllDatabasesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_all_databases_with_options(runtime)

    async def get_all_databases_async(self) -> openanalytics_open_20200928_models.GetAllDatabasesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_all_databases_with_options_async(runtime)

    def get_all_tables_with_options(
        self,
        request: openanalytics_open_20200928_models.GetAllTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.GetAllTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAllTables',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.GetAllTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_all_tables_with_options_async(
        self,
        request: openanalytics_open_20200928_models.GetAllTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.GetAllTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAllTables',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.GetAllTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_all_tables(
        self,
        request: openanalytics_open_20200928_models.GetAllTablesRequest,
    ) -> openanalytics_open_20200928_models.GetAllTablesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_all_tables_with_options(request, runtime)

    async def get_all_tables_async(
        self,
        request: openanalytics_open_20200928_models.GetAllTablesRequest,
    ) -> openanalytics_open_20200928_models.GetAllTablesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_all_tables_with_options_async(request, runtime)

    def get_database_with_options(
        self,
        request: openanalytics_open_20200928_models.GetDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.GetDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDatabase',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.GetDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_database_with_options_async(
        self,
        request: openanalytics_open_20200928_models.GetDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.GetDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDatabase',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.GetDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_database(
        self,
        request: openanalytics_open_20200928_models.GetDatabaseRequest,
    ) -> openanalytics_open_20200928_models.GetDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_database_with_options(request, runtime)

    async def get_database_async(
        self,
        request: openanalytics_open_20200928_models.GetDatabaseRequest,
    ) -> openanalytics_open_20200928_models.GetDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_database_with_options_async(request, runtime)

    def get_partition_with_options(
        self,
        tmp_req: openanalytics_open_20200928_models.GetPartitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.GetPartitionResponse:
        UtilClient.validate_model(tmp_req)
        request = openanalytics_open_20200928_models.GetPartitionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.values):
            request.values_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.values, 'Values', 'json')
        query = {}
        query['DbName'] = request.db_name
        query['TableName'] = request.table_name
        query['Values'] = request.values_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetPartition',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.GetPartitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_partition_with_options_async(
        self,
        tmp_req: openanalytics_open_20200928_models.GetPartitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.GetPartitionResponse:
        UtilClient.validate_model(tmp_req)
        request = openanalytics_open_20200928_models.GetPartitionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.values):
            request.values_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.values, 'Values', 'json')
        query = {}
        query['DbName'] = request.db_name
        query['TableName'] = request.table_name
        query['Values'] = request.values_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetPartition',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.GetPartitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_partition(
        self,
        request: openanalytics_open_20200928_models.GetPartitionRequest,
    ) -> openanalytics_open_20200928_models.GetPartitionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_partition_with_options(request, runtime)

    async def get_partition_async(
        self,
        request: openanalytics_open_20200928_models.GetPartitionRequest,
    ) -> openanalytics_open_20200928_models.GetPartitionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_partition_with_options_async(request, runtime)

    def get_partitions_with_options(
        self,
        request: openanalytics_open_20200928_models.GetPartitionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.GetPartitionsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['TableName'] = request.table_name
        query['MaxParts'] = request.max_parts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetPartitions',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.GetPartitionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_partitions_with_options_async(
        self,
        request: openanalytics_open_20200928_models.GetPartitionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.GetPartitionsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['TableName'] = request.table_name
        query['MaxParts'] = request.max_parts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetPartitions',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.GetPartitionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_partitions(
        self,
        request: openanalytics_open_20200928_models.GetPartitionsRequest,
    ) -> openanalytics_open_20200928_models.GetPartitionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_partitions_with_options(request, runtime)

    async def get_partitions_async(
        self,
        request: openanalytics_open_20200928_models.GetPartitionsRequest,
    ) -> openanalytics_open_20200928_models.GetPartitionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_partitions_with_options_async(request, runtime)

    def get_table_with_options(
        self,
        request: openanalytics_open_20200928_models.GetTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.GetTableResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetTable',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.GetTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_with_options_async(
        self,
        request: openanalytics_open_20200928_models.GetTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.GetTableResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetTable',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.GetTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table(
        self,
        request: openanalytics_open_20200928_models.GetTableRequest,
    ) -> openanalytics_open_20200928_models.GetTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_table_with_options(request, runtime)

    async def get_table_async(
        self,
        request: openanalytics_open_20200928_models.GetTableRequest,
    ) -> openanalytics_open_20200928_models.GetTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_table_with_options_async(request, runtime)

    def grant_privileges_with_options(
        self,
        tmp_req: openanalytics_open_20200928_models.GrantPrivilegesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.GrantPrivilegesResponse:
        UtilClient.validate_model(tmp_req)
        request = openanalytics_open_20200928_models.GrantPrivilegesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.privilege_bag):
            request.privilege_bag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.privilege_bag), 'PrivilegeBag', 'json')
        query = {}
        query['PrivilegeBag'] = request.privilege_bag_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GrantPrivileges',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.GrantPrivilegesResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_privileges_with_options_async(
        self,
        tmp_req: openanalytics_open_20200928_models.GrantPrivilegesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.GrantPrivilegesResponse:
        UtilClient.validate_model(tmp_req)
        request = openanalytics_open_20200928_models.GrantPrivilegesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.privilege_bag):
            request.privilege_bag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.privilege_bag), 'PrivilegeBag', 'json')
        query = {}
        query['PrivilegeBag'] = request.privilege_bag_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GrantPrivileges',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.GrantPrivilegesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_privileges(
        self,
        request: openanalytics_open_20200928_models.GrantPrivilegesRequest,
    ) -> openanalytics_open_20200928_models.GrantPrivilegesResponse:
        runtime = util_models.RuntimeOptions()
        return self.grant_privileges_with_options(request, runtime)

    async def grant_privileges_async(
        self,
        request: openanalytics_open_20200928_models.GrantPrivilegesRequest,
    ) -> openanalytics_open_20200928_models.GrantPrivilegesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.grant_privileges_with_options_async(request, runtime)

    def revoke_privileges_with_options(
        self,
        tmp_req: openanalytics_open_20200928_models.RevokePrivilegesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.RevokePrivilegesResponse:
        UtilClient.validate_model(tmp_req)
        request = openanalytics_open_20200928_models.RevokePrivilegesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.privilege_bag):
            request.privilege_bag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.privilege_bag), 'PrivilegeBag', 'json')
        query = {}
        query['PrivilegeBag'] = request.privilege_bag_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RevokePrivileges',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.RevokePrivilegesResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_privileges_with_options_async(
        self,
        tmp_req: openanalytics_open_20200928_models.RevokePrivilegesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20200928_models.RevokePrivilegesResponse:
        UtilClient.validate_model(tmp_req)
        request = openanalytics_open_20200928_models.RevokePrivilegesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.privilege_bag):
            request.privilege_bag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.privilege_bag), 'PrivilegeBag', 'json')
        query = {}
        query['PrivilegeBag'] = request.privilege_bag_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RevokePrivileges',
            version='2020-09-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20200928_models.RevokePrivilegesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_privileges(
        self,
        request: openanalytics_open_20200928_models.RevokePrivilegesRequest,
    ) -> openanalytics_open_20200928_models.RevokePrivilegesResponse:
        runtime = util_models.RuntimeOptions()
        return self.revoke_privileges_with_options(request, runtime)

    async def revoke_privileges_async(
        self,
        request: openanalytics_open_20200928_models.RevokePrivilegesRequest,
    ) -> openanalytics_open_20200928_models.RevokePrivilegesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revoke_privileges_with_options_async(request, runtime)
