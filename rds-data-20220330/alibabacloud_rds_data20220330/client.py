# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_rds_data20220330 import models as rds_data_20220330_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('rds-data', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def batch_execute_statement_with_options(
        self,
        tmp_req: rds_data_20220330_models.BatchExecuteStatementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_data_20220330_models.BatchExecuteStatementResponse:
        UtilClient.validate_model(tmp_req)
        request = rds_data_20220330_models.BatchExecuteStatementShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameter_sets):
            request.parameter_sets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameter_sets, 'ParameterSets', 'json')
        body = {}
        if not UtilClient.is_unset(request.database):
            body['Database'] = request.database
        if not UtilClient.is_unset(request.parameter_sets_shrink):
            body['ParameterSets'] = request.parameter_sets_shrink
        if not UtilClient.is_unset(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.secret_arn):
            body['SecretArn'] = request.secret_arn
        if not UtilClient.is_unset(request.sql):
            body['Sql'] = request.sql
        if not UtilClient.is_unset(request.transaction_id):
            body['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchExecuteStatement',
            version='2022-03-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_data_20220330_models.BatchExecuteStatementResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_execute_statement_with_options_async(
        self,
        tmp_req: rds_data_20220330_models.BatchExecuteStatementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_data_20220330_models.BatchExecuteStatementResponse:
        UtilClient.validate_model(tmp_req)
        request = rds_data_20220330_models.BatchExecuteStatementShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameter_sets):
            request.parameter_sets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameter_sets, 'ParameterSets', 'json')
        body = {}
        if not UtilClient.is_unset(request.database):
            body['Database'] = request.database
        if not UtilClient.is_unset(request.parameter_sets_shrink):
            body['ParameterSets'] = request.parameter_sets_shrink
        if not UtilClient.is_unset(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.secret_arn):
            body['SecretArn'] = request.secret_arn
        if not UtilClient.is_unset(request.sql):
            body['Sql'] = request.sql
        if not UtilClient.is_unset(request.transaction_id):
            body['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchExecuteStatement',
            version='2022-03-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_data_20220330_models.BatchExecuteStatementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_execute_statement(
        self,
        request: rds_data_20220330_models.BatchExecuteStatementRequest,
    ) -> rds_data_20220330_models.BatchExecuteStatementResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_execute_statement_with_options(request, runtime)

    async def batch_execute_statement_async(
        self,
        request: rds_data_20220330_models.BatchExecuteStatementRequest,
    ) -> rds_data_20220330_models.BatchExecuteStatementResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_execute_statement_with_options_async(request, runtime)

    def begin_transaction_with_options(
        self,
        request: rds_data_20220330_models.BeginTransactionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_data_20220330_models.BeginTransactionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.database):
            body['Database'] = request.database
        if not UtilClient.is_unset(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.secret_arn):
            body['SecretArn'] = request.secret_arn
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BeginTransaction',
            version='2022-03-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_data_20220330_models.BeginTransactionResponse(),
            self.call_api(params, req, runtime)
        )

    async def begin_transaction_with_options_async(
        self,
        request: rds_data_20220330_models.BeginTransactionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_data_20220330_models.BeginTransactionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.database):
            body['Database'] = request.database
        if not UtilClient.is_unset(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.secret_arn):
            body['SecretArn'] = request.secret_arn
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BeginTransaction',
            version='2022-03-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_data_20220330_models.BeginTransactionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def begin_transaction(
        self,
        request: rds_data_20220330_models.BeginTransactionRequest,
    ) -> rds_data_20220330_models.BeginTransactionResponse:
        runtime = util_models.RuntimeOptions()
        return self.begin_transaction_with_options(request, runtime)

    async def begin_transaction_async(
        self,
        request: rds_data_20220330_models.BeginTransactionRequest,
    ) -> rds_data_20220330_models.BeginTransactionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.begin_transaction_with_options_async(request, runtime)

    def commit_transaction_with_options(
        self,
        request: rds_data_20220330_models.CommitTransactionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_data_20220330_models.CommitTransactionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.secret_arn):
            body['SecretArn'] = request.secret_arn
        if not UtilClient.is_unset(request.transaction_id):
            body['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CommitTransaction',
            version='2022-03-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_data_20220330_models.CommitTransactionResponse(),
            self.call_api(params, req, runtime)
        )

    async def commit_transaction_with_options_async(
        self,
        request: rds_data_20220330_models.CommitTransactionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_data_20220330_models.CommitTransactionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.secret_arn):
            body['SecretArn'] = request.secret_arn
        if not UtilClient.is_unset(request.transaction_id):
            body['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CommitTransaction',
            version='2022-03-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_data_20220330_models.CommitTransactionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def commit_transaction(
        self,
        request: rds_data_20220330_models.CommitTransactionRequest,
    ) -> rds_data_20220330_models.CommitTransactionResponse:
        runtime = util_models.RuntimeOptions()
        return self.commit_transaction_with_options(request, runtime)

    async def commit_transaction_async(
        self,
        request: rds_data_20220330_models.CommitTransactionRequest,
    ) -> rds_data_20220330_models.CommitTransactionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.commit_transaction_with_options_async(request, runtime)

    def delete_with_options(
        self,
        tmp_req: rds_data_20220330_models.DeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_data_20220330_models.DeleteResponse:
        UtilClient.validate_model(tmp_req)
        request = rds_data_20220330_models.DeleteShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        body = {}
        if not UtilClient.is_unset(request.database):
            body['Database'] = request.database
        if not UtilClient.is_unset(request.filter_shrink):
            body['Filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.secret_arn):
            body['SecretArn'] = request.secret_arn
        if not UtilClient.is_unset(request.table):
            body['Table'] = request.table
        if not UtilClient.is_unset(request.transaction_id):
            body['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Delete',
            version='2022-03-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_data_20220330_models.DeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_with_options_async(
        self,
        tmp_req: rds_data_20220330_models.DeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_data_20220330_models.DeleteResponse:
        UtilClient.validate_model(tmp_req)
        request = rds_data_20220330_models.DeleteShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        body = {}
        if not UtilClient.is_unset(request.database):
            body['Database'] = request.database
        if not UtilClient.is_unset(request.filter_shrink):
            body['Filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.secret_arn):
            body['SecretArn'] = request.secret_arn
        if not UtilClient.is_unset(request.table):
            body['Table'] = request.table
        if not UtilClient.is_unset(request.transaction_id):
            body['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Delete',
            version='2022-03-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_data_20220330_models.DeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete(
        self,
        request: rds_data_20220330_models.DeleteRequest,
    ) -> rds_data_20220330_models.DeleteResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_with_options(request, runtime)

    async def delete_async(
        self,
        request: rds_data_20220330_models.DeleteRequest,
    ) -> rds_data_20220330_models.DeleteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_with_options_async(request, runtime)

    def execute_statement_with_options(
        self,
        tmp_req: rds_data_20220330_models.ExecuteStatementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_data_20220330_models.ExecuteStatementResponse:
        UtilClient.validate_model(tmp_req)
        request = rds_data_20220330_models.ExecuteStatementShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        if not UtilClient.is_unset(tmp_req.result_set_options):
            request.result_set_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.result_set_options, 'ResultSetOptions', 'json')
        body = {}
        if not UtilClient.is_unset(request.continue_after_timeout):
            body['ContinueAfterTimeout'] = request.continue_after_timeout
        if not UtilClient.is_unset(request.database):
            body['Database'] = request.database
        if not UtilClient.is_unset(request.format_records_as):
            body['FormatRecordsAs'] = request.format_records_as
        if not UtilClient.is_unset(request.include_result_metadata):
            body['IncludeResultMetadata'] = request.include_result_metadata
        if not UtilClient.is_unset(request.parameters_shrink):
            body['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.result_set_options_shrink):
            body['ResultSetOptions'] = request.result_set_options_shrink
        if not UtilClient.is_unset(request.secret_arn):
            body['SecretArn'] = request.secret_arn
        if not UtilClient.is_unset(request.sql):
            body['Sql'] = request.sql
        if not UtilClient.is_unset(request.transaction_id):
            body['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteStatement',
            version='2022-03-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_data_20220330_models.ExecuteStatementResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_statement_with_options_async(
        self,
        tmp_req: rds_data_20220330_models.ExecuteStatementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_data_20220330_models.ExecuteStatementResponse:
        UtilClient.validate_model(tmp_req)
        request = rds_data_20220330_models.ExecuteStatementShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        if not UtilClient.is_unset(tmp_req.result_set_options):
            request.result_set_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.result_set_options, 'ResultSetOptions', 'json')
        body = {}
        if not UtilClient.is_unset(request.continue_after_timeout):
            body['ContinueAfterTimeout'] = request.continue_after_timeout
        if not UtilClient.is_unset(request.database):
            body['Database'] = request.database
        if not UtilClient.is_unset(request.format_records_as):
            body['FormatRecordsAs'] = request.format_records_as
        if not UtilClient.is_unset(request.include_result_metadata):
            body['IncludeResultMetadata'] = request.include_result_metadata
        if not UtilClient.is_unset(request.parameters_shrink):
            body['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.result_set_options_shrink):
            body['ResultSetOptions'] = request.result_set_options_shrink
        if not UtilClient.is_unset(request.secret_arn):
            body['SecretArn'] = request.secret_arn
        if not UtilClient.is_unset(request.sql):
            body['Sql'] = request.sql
        if not UtilClient.is_unset(request.transaction_id):
            body['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteStatement',
            version='2022-03-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_data_20220330_models.ExecuteStatementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_statement(
        self,
        request: rds_data_20220330_models.ExecuteStatementRequest,
    ) -> rds_data_20220330_models.ExecuteStatementResponse:
        runtime = util_models.RuntimeOptions()
        return self.execute_statement_with_options(request, runtime)

    async def execute_statement_async(
        self,
        request: rds_data_20220330_models.ExecuteStatementRequest,
    ) -> rds_data_20220330_models.ExecuteStatementResponse:
        runtime = util_models.RuntimeOptions()
        return await self.execute_statement_with_options_async(request, runtime)

    def insert_with_options(
        self,
        tmp_req: rds_data_20220330_models.InsertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_data_20220330_models.InsertResponse:
        UtilClient.validate_model(tmp_req)
        request = rds_data_20220330_models.InsertShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.record):
            request.record_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.record, 'Record', 'json')
        body = {}
        if not UtilClient.is_unset(request.database):
            body['Database'] = request.database
        if not UtilClient.is_unset(request.record_shrink):
            body['Record'] = request.record_shrink
        if not UtilClient.is_unset(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.secret_arn):
            body['SecretArn'] = request.secret_arn
        if not UtilClient.is_unset(request.table):
            body['Table'] = request.table
        if not UtilClient.is_unset(request.transaction_id):
            body['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Insert',
            version='2022-03-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_data_20220330_models.InsertResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_with_options_async(
        self,
        tmp_req: rds_data_20220330_models.InsertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_data_20220330_models.InsertResponse:
        UtilClient.validate_model(tmp_req)
        request = rds_data_20220330_models.InsertShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.record):
            request.record_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.record, 'Record', 'json')
        body = {}
        if not UtilClient.is_unset(request.database):
            body['Database'] = request.database
        if not UtilClient.is_unset(request.record_shrink):
            body['Record'] = request.record_shrink
        if not UtilClient.is_unset(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.secret_arn):
            body['SecretArn'] = request.secret_arn
        if not UtilClient.is_unset(request.table):
            body['Table'] = request.table
        if not UtilClient.is_unset(request.transaction_id):
            body['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Insert',
            version='2022-03-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_data_20220330_models.InsertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert(
        self,
        request: rds_data_20220330_models.InsertRequest,
    ) -> rds_data_20220330_models.InsertResponse:
        runtime = util_models.RuntimeOptions()
        return self.insert_with_options(request, runtime)

    async def insert_async(
        self,
        request: rds_data_20220330_models.InsertRequest,
    ) -> rds_data_20220330_models.InsertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.insert_with_options_async(request, runtime)

    def insert_list_with_options(
        self,
        tmp_req: rds_data_20220330_models.InsertListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_data_20220330_models.InsertListResponse:
        UtilClient.validate_model(tmp_req)
        request = rds_data_20220330_models.InsertListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.records):
            request.records_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.records, 'Records', 'json')
        body = {}
        if not UtilClient.is_unset(request.database):
            body['Database'] = request.database
        if not UtilClient.is_unset(request.records_shrink):
            body['Records'] = request.records_shrink
        if not UtilClient.is_unset(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.secret_arn):
            body['SecretArn'] = request.secret_arn
        if not UtilClient.is_unset(request.table):
            body['Table'] = request.table
        if not UtilClient.is_unset(request.transaction_id):
            body['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InsertList',
            version='2022-03-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_data_20220330_models.InsertListResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_list_with_options_async(
        self,
        tmp_req: rds_data_20220330_models.InsertListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_data_20220330_models.InsertListResponse:
        UtilClient.validate_model(tmp_req)
        request = rds_data_20220330_models.InsertListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.records):
            request.records_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.records, 'Records', 'json')
        body = {}
        if not UtilClient.is_unset(request.database):
            body['Database'] = request.database
        if not UtilClient.is_unset(request.records_shrink):
            body['Records'] = request.records_shrink
        if not UtilClient.is_unset(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.secret_arn):
            body['SecretArn'] = request.secret_arn
        if not UtilClient.is_unset(request.table):
            body['Table'] = request.table
        if not UtilClient.is_unset(request.transaction_id):
            body['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InsertList',
            version='2022-03-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_data_20220330_models.InsertListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_list(
        self,
        request: rds_data_20220330_models.InsertListRequest,
    ) -> rds_data_20220330_models.InsertListResponse:
        runtime = util_models.RuntimeOptions()
        return self.insert_list_with_options(request, runtime)

    async def insert_list_async(
        self,
        request: rds_data_20220330_models.InsertListRequest,
    ) -> rds_data_20220330_models.InsertListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.insert_list_with_options_async(request, runtime)

    def rollback_transaction_with_options(
        self,
        request: rds_data_20220330_models.RollbackTransactionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_data_20220330_models.RollbackTransactionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.secret_arn):
            body['SecretArn'] = request.secret_arn
        if not UtilClient.is_unset(request.transaction_id):
            body['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RollbackTransaction',
            version='2022-03-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_data_20220330_models.RollbackTransactionResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_transaction_with_options_async(
        self,
        request: rds_data_20220330_models.RollbackTransactionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_data_20220330_models.RollbackTransactionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.secret_arn):
            body['SecretArn'] = request.secret_arn
        if not UtilClient.is_unset(request.transaction_id):
            body['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RollbackTransaction',
            version='2022-03-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_data_20220330_models.RollbackTransactionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_transaction(
        self,
        request: rds_data_20220330_models.RollbackTransactionRequest,
    ) -> rds_data_20220330_models.RollbackTransactionResponse:
        runtime = util_models.RuntimeOptions()
        return self.rollback_transaction_with_options(request, runtime)

    async def rollback_transaction_async(
        self,
        request: rds_data_20220330_models.RollbackTransactionRequest,
    ) -> rds_data_20220330_models.RollbackTransactionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rollback_transaction_with_options_async(request, runtime)

    def select_with_options(
        self,
        tmp_req: rds_data_20220330_models.SelectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_data_20220330_models.SelectResponse:
        UtilClient.validate_model(tmp_req)
        request = rds_data_20220330_models.SelectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        body = {}
        if not UtilClient.is_unset(request.database):
            body['Database'] = request.database
        if not UtilClient.is_unset(request.filter_shrink):
            body['Filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.secret_arn):
            body['SecretArn'] = request.secret_arn
        if not UtilClient.is_unset(request.table):
            body['Table'] = request.table
        if not UtilClient.is_unset(request.transaction_id):
            body['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Select',
            version='2022-03-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_data_20220330_models.SelectResponse(),
            self.call_api(params, req, runtime)
        )

    async def select_with_options_async(
        self,
        tmp_req: rds_data_20220330_models.SelectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_data_20220330_models.SelectResponse:
        UtilClient.validate_model(tmp_req)
        request = rds_data_20220330_models.SelectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        body = {}
        if not UtilClient.is_unset(request.database):
            body['Database'] = request.database
        if not UtilClient.is_unset(request.filter_shrink):
            body['Filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.secret_arn):
            body['SecretArn'] = request.secret_arn
        if not UtilClient.is_unset(request.table):
            body['Table'] = request.table
        if not UtilClient.is_unset(request.transaction_id):
            body['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Select',
            version='2022-03-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_data_20220330_models.SelectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def select(
        self,
        request: rds_data_20220330_models.SelectRequest,
    ) -> rds_data_20220330_models.SelectResponse:
        runtime = util_models.RuntimeOptions()
        return self.select_with_options(request, runtime)

    async def select_async(
        self,
        request: rds_data_20220330_models.SelectRequest,
    ) -> rds_data_20220330_models.SelectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.select_with_options_async(request, runtime)

    def update_with_options(
        self,
        tmp_req: rds_data_20220330_models.UpdateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_data_20220330_models.UpdateResponse:
        UtilClient.validate_model(tmp_req)
        request = rds_data_20220330_models.UpdateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        if not UtilClient.is_unset(tmp_req.record):
            request.record_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.record, 'Record', 'json')
        body = {}
        if not UtilClient.is_unset(request.database):
            body['Database'] = request.database
        if not UtilClient.is_unset(request.filter_shrink):
            body['Filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.record_shrink):
            body['Record'] = request.record_shrink
        if not UtilClient.is_unset(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.secret_arn):
            body['SecretArn'] = request.secret_arn
        if not UtilClient.is_unset(request.table):
            body['Table'] = request.table
        if not UtilClient.is_unset(request.transaction_id):
            body['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Update',
            version='2022-03-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_data_20220330_models.UpdateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_with_options_async(
        self,
        tmp_req: rds_data_20220330_models.UpdateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_data_20220330_models.UpdateResponse:
        UtilClient.validate_model(tmp_req)
        request = rds_data_20220330_models.UpdateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        if not UtilClient.is_unset(tmp_req.record):
            request.record_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.record, 'Record', 'json')
        body = {}
        if not UtilClient.is_unset(request.database):
            body['Database'] = request.database
        if not UtilClient.is_unset(request.filter_shrink):
            body['Filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.record_shrink):
            body['Record'] = request.record_shrink
        if not UtilClient.is_unset(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.secret_arn):
            body['SecretArn'] = request.secret_arn
        if not UtilClient.is_unset(request.table):
            body['Table'] = request.table
        if not UtilClient.is_unset(request.transaction_id):
            body['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Update',
            version='2022-03-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_data_20220330_models.UpdateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update(
        self,
        request: rds_data_20220330_models.UpdateRequest,
    ) -> rds_data_20220330_models.UpdateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_with_options(request, runtime)

    async def update_async(
        self,
        request: rds_data_20220330_models.UpdateRequest,
    ) -> rds_data_20220330_models.UpdateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_with_options_async(request, runtime)
