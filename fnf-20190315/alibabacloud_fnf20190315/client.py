# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_fnf20190315 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._signature_algorithm = 'v2'
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-beijing': 'cn-beijing.fnf.aliyuncs.com',
            'cn-hangzhou': 'cn-hangzhou.fnf.aliyuncs.com',
            'cn-shanghai': 'cn-shanghai.fnf.aliyuncs.com',
            'cn-shenzhen': 'cn-shenzhen.fnf.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('fnf', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_flow_with_options(
        self,
        tmp_req: main_models.CreateFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFlowResponse:
        tmp_req.validate()
        request = main_models.CreateFlowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.environment):
            request.environment_shrink = Utils.array_to_string_with_specified_style(tmp_req.environment, 'Environment', 'json')
        body = {}
        if not DaraCore.is_null(request.definition):
            body['Definition'] = request.definition
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.environment_shrink):
            body['Environment'] = request.environment_shrink
        if not DaraCore.is_null(request.execution_mode):
            body['ExecutionMode'] = request.execution_mode
        if not DaraCore.is_null(request.external_storage_location):
            body['ExternalStorageLocation'] = request.external_storage_location
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.role_arn):
            body['RoleArn'] = request.role_arn
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFlow',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_with_options_async(
        self,
        tmp_req: main_models.CreateFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFlowResponse:
        tmp_req.validate()
        request = main_models.CreateFlowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.environment):
            request.environment_shrink = Utils.array_to_string_with_specified_style(tmp_req.environment, 'Environment', 'json')
        body = {}
        if not DaraCore.is_null(request.definition):
            body['Definition'] = request.definition
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.environment_shrink):
            body['Environment'] = request.environment_shrink
        if not DaraCore.is_null(request.execution_mode):
            body['ExecutionMode'] = request.execution_mode
        if not DaraCore.is_null(request.external_storage_location):
            body['ExternalStorageLocation'] = request.external_storage_location
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.role_arn):
            body['RoleArn'] = request.role_arn
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFlow',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_flow(
        self,
        request: main_models.CreateFlowRequest,
    ) -> main_models.CreateFlowResponse:
        runtime = RuntimeOptions()
        return self.create_flow_with_options(request, runtime)

    async def create_flow_async(
        self,
        request: main_models.CreateFlowRequest,
    ) -> main_models.CreateFlowResponse:
        runtime = RuntimeOptions()
        return await self.create_flow_with_options_async(request, runtime)

    def create_flow_alias_with_options(
        self,
        tmp_req: main_models.CreateFlowAliasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFlowAliasResponse:
        tmp_req.validate()
        request = main_models.CreateFlowAliasShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.routing_configurations):
            request.routing_configurations_shrink = Utils.array_to_string_with_specified_style(tmp_req.routing_configurations, 'RoutingConfigurations', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.flow_name):
            body['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.routing_configurations_shrink):
            body['RoutingConfigurations'] = request.routing_configurations_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFlowAlias',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFlowAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_alias_with_options_async(
        self,
        tmp_req: main_models.CreateFlowAliasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFlowAliasResponse:
        tmp_req.validate()
        request = main_models.CreateFlowAliasShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.routing_configurations):
            request.routing_configurations_shrink = Utils.array_to_string_with_specified_style(tmp_req.routing_configurations, 'RoutingConfigurations', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.flow_name):
            body['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.routing_configurations_shrink):
            body['RoutingConfigurations'] = request.routing_configurations_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFlowAlias',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFlowAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_flow_alias(
        self,
        request: main_models.CreateFlowAliasRequest,
    ) -> main_models.CreateFlowAliasResponse:
        runtime = RuntimeOptions()
        return self.create_flow_alias_with_options(request, runtime)

    async def create_flow_alias_async(
        self,
        request: main_models.CreateFlowAliasRequest,
    ) -> main_models.CreateFlowAliasResponse:
        runtime = RuntimeOptions()
        return await self.create_flow_alias_with_options_async(request, runtime)

    def create_schedule_with_options(
        self,
        request: main_models.CreateScheduleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScheduleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.signature_version):
            query['SignatureVersion'] = request.signature_version
        body = {}
        if not DaraCore.is_null(request.cron_expression):
            body['CronExpression'] = request.cron_expression
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.enable):
            body['Enable'] = request.enable
        if not DaraCore.is_null(request.flow_name):
            body['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.payload):
            body['Payload'] = request.payload
        if not DaraCore.is_null(request.schedule_name):
            body['ScheduleName'] = request.schedule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSchedule',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_schedule_with_options_async(
        self,
        request: main_models.CreateScheduleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScheduleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.signature_version):
            query['SignatureVersion'] = request.signature_version
        body = {}
        if not DaraCore.is_null(request.cron_expression):
            body['CronExpression'] = request.cron_expression
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.enable):
            body['Enable'] = request.enable
        if not DaraCore.is_null(request.flow_name):
            body['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.payload):
            body['Payload'] = request.payload
        if not DaraCore.is_null(request.schedule_name):
            body['ScheduleName'] = request.schedule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSchedule',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_schedule(
        self,
        request: main_models.CreateScheduleRequest,
    ) -> main_models.CreateScheduleResponse:
        runtime = RuntimeOptions()
        return self.create_schedule_with_options(request, runtime)

    async def create_schedule_async(
        self,
        request: main_models.CreateScheduleRequest,
    ) -> main_models.CreateScheduleResponse:
        runtime = RuntimeOptions()
        return await self.create_schedule_with_options_async(request, runtime)

    def delete_flow_with_options(
        self,
        request: main_models.DeleteFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFlowResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFlow',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_with_options_async(
        self,
        request: main_models.DeleteFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFlowResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFlow',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_flow(
        self,
        request: main_models.DeleteFlowRequest,
    ) -> main_models.DeleteFlowResponse:
        runtime = RuntimeOptions()
        return self.delete_flow_with_options(request, runtime)

    async def delete_flow_async(
        self,
        request: main_models.DeleteFlowRequest,
    ) -> main_models.DeleteFlowResponse:
        runtime = RuntimeOptions()
        return await self.delete_flow_with_options_async(request, runtime)

    def delete_flow_alias_with_options(
        self,
        request: main_models.DeleteFlowAliasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFlowAliasResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.flow_name):
            body['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFlowAlias',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFlowAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_alias_with_options_async(
        self,
        request: main_models.DeleteFlowAliasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFlowAliasResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.flow_name):
            body['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFlowAlias',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFlowAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_flow_alias(
        self,
        request: main_models.DeleteFlowAliasRequest,
    ) -> main_models.DeleteFlowAliasResponse:
        runtime = RuntimeOptions()
        return self.delete_flow_alias_with_options(request, runtime)

    async def delete_flow_alias_async(
        self,
        request: main_models.DeleteFlowAliasRequest,
    ) -> main_models.DeleteFlowAliasResponse:
        runtime = RuntimeOptions()
        return await self.delete_flow_alias_with_options_async(request, runtime)

    def delete_flow_version_with_options(
        self,
        request: main_models.DeleteFlowVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFlowVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.flow_name):
            body['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.flow_version):
            body['FlowVersion'] = request.flow_version
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFlowVersion',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFlowVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_version_with_options_async(
        self,
        request: main_models.DeleteFlowVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFlowVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.flow_name):
            body['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.flow_version):
            body['FlowVersion'] = request.flow_version
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFlowVersion',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFlowVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_flow_version(
        self,
        request: main_models.DeleteFlowVersionRequest,
    ) -> main_models.DeleteFlowVersionResponse:
        runtime = RuntimeOptions()
        return self.delete_flow_version_with_options(request, runtime)

    async def delete_flow_version_async(
        self,
        request: main_models.DeleteFlowVersionRequest,
    ) -> main_models.DeleteFlowVersionResponse:
        runtime = RuntimeOptions()
        return await self.delete_flow_version_with_options_async(request, runtime)

    def delete_schedule_with_options(
        self,
        request: main_models.DeleteScheduleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScheduleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.flow_name):
            body['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.schedule_name):
            body['ScheduleName'] = request.schedule_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSchedule',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_schedule_with_options_async(
        self,
        request: main_models.DeleteScheduleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScheduleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.flow_name):
            body['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.schedule_name):
            body['ScheduleName'] = request.schedule_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSchedule',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_schedule(
        self,
        request: main_models.DeleteScheduleRequest,
    ) -> main_models.DeleteScheduleResponse:
        runtime = RuntimeOptions()
        return self.delete_schedule_with_options(request, runtime)

    async def delete_schedule_async(
        self,
        request: main_models.DeleteScheduleRequest,
    ) -> main_models.DeleteScheduleResponse:
        runtime = RuntimeOptions()
        return await self.delete_schedule_with_options_async(request, runtime)

    def describe_execution_with_options(
        self,
        request: main_models.DescribeExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExecutionResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExecution',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_execution_with_options_async(
        self,
        request: main_models.DescribeExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExecutionResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExecution',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_execution(
        self,
        request: main_models.DescribeExecutionRequest,
    ) -> main_models.DescribeExecutionResponse:
        runtime = RuntimeOptions()
        return self.describe_execution_with_options(request, runtime)

    async def describe_execution_async(
        self,
        request: main_models.DescribeExecutionRequest,
    ) -> main_models.DescribeExecutionResponse:
        runtime = RuntimeOptions()
        return await self.describe_execution_with_options_async(request, runtime)

    def describe_flow_with_options(
        self,
        request: main_models.DescribeFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFlowResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFlow',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_with_options_async(
        self,
        request: main_models.DescribeFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFlowResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFlow',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_flow(
        self,
        request: main_models.DescribeFlowRequest,
    ) -> main_models.DescribeFlowResponse:
        runtime = RuntimeOptions()
        return self.describe_flow_with_options(request, runtime)

    async def describe_flow_async(
        self,
        request: main_models.DescribeFlowRequest,
    ) -> main_models.DescribeFlowResponse:
        runtime = RuntimeOptions()
        return await self.describe_flow_with_options_async(request, runtime)

    def describe_flow_alias_with_options(
        self,
        request: main_models.DescribeFlowAliasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFlowAliasResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFlowAlias',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFlowAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_alias_with_options_async(
        self,
        request: main_models.DescribeFlowAliasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFlowAliasResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFlowAlias',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFlowAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_flow_alias(
        self,
        request: main_models.DescribeFlowAliasRequest,
    ) -> main_models.DescribeFlowAliasResponse:
        runtime = RuntimeOptions()
        return self.describe_flow_alias_with_options(request, runtime)

    async def describe_flow_alias_async(
        self,
        request: main_models.DescribeFlowAliasRequest,
    ) -> main_models.DescribeFlowAliasResponse:
        runtime = RuntimeOptions()
        return await self.describe_flow_alias_with_options_async(request, runtime)

    def describe_map_run_with_options(
        self,
        request: main_models.DescribeMapRunRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMapRunResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMapRun',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMapRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_map_run_with_options_async(
        self,
        request: main_models.DescribeMapRunRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMapRunResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMapRun',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMapRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_map_run(
        self,
        request: main_models.DescribeMapRunRequest,
    ) -> main_models.DescribeMapRunResponse:
        runtime = RuntimeOptions()
        return self.describe_map_run_with_options(request, runtime)

    async def describe_map_run_async(
        self,
        request: main_models.DescribeMapRunRequest,
    ) -> main_models.DescribeMapRunResponse:
        runtime = RuntimeOptions()
        return await self.describe_map_run_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_schedule_with_options(
        self,
        request: main_models.DescribeScheduleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScheduleResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSchedule',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_schedule_with_options_async(
        self,
        request: main_models.DescribeScheduleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScheduleResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSchedule',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_schedule(
        self,
        request: main_models.DescribeScheduleRequest,
    ) -> main_models.DescribeScheduleResponse:
        runtime = RuntimeOptions()
        return self.describe_schedule_with_options(request, runtime)

    async def describe_schedule_async(
        self,
        request: main_models.DescribeScheduleRequest,
    ) -> main_models.DescribeScheduleResponse:
        runtime = RuntimeOptions()
        return await self.describe_schedule_with_options_async(request, runtime)

    def get_execution_history_with_options(
        self,
        request: main_models.GetExecutionHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetExecutionHistoryResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExecutionHistory',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExecutionHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_execution_history_with_options_async(
        self,
        request: main_models.GetExecutionHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetExecutionHistoryResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExecutionHistory',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExecutionHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_execution_history(
        self,
        request: main_models.GetExecutionHistoryRequest,
    ) -> main_models.GetExecutionHistoryResponse:
        runtime = RuntimeOptions()
        return self.get_execution_history_with_options(request, runtime)

    async def get_execution_history_async(
        self,
        request: main_models.GetExecutionHistoryRequest,
    ) -> main_models.GetExecutionHistoryResponse:
        runtime = RuntimeOptions()
        return await self.get_execution_history_with_options_async(request, runtime)

    def list_executions_with_options(
        self,
        request: main_models.ListExecutionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExecutionsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExecutions',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExecutionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_executions_with_options_async(
        self,
        request: main_models.ListExecutionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExecutionsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExecutions',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExecutionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_executions(
        self,
        request: main_models.ListExecutionsRequest,
    ) -> main_models.ListExecutionsResponse:
        runtime = RuntimeOptions()
        return self.list_executions_with_options(request, runtime)

    async def list_executions_async(
        self,
        request: main_models.ListExecutionsRequest,
    ) -> main_models.ListExecutionsResponse:
        runtime = RuntimeOptions()
        return await self.list_executions_with_options_async(request, runtime)

    def list_flow_aliases_with_options(
        self,
        request: main_models.ListFlowAliasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFlowAliasesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFlowAliases',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFlowAliasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_aliases_with_options_async(
        self,
        request: main_models.ListFlowAliasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFlowAliasesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFlowAliases',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFlowAliasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flow_aliases(
        self,
        request: main_models.ListFlowAliasesRequest,
    ) -> main_models.ListFlowAliasesResponse:
        runtime = RuntimeOptions()
        return self.list_flow_aliases_with_options(request, runtime)

    async def list_flow_aliases_async(
        self,
        request: main_models.ListFlowAliasesRequest,
    ) -> main_models.ListFlowAliasesResponse:
        runtime = RuntimeOptions()
        return await self.list_flow_aliases_with_options_async(request, runtime)

    def list_flow_versions_with_options(
        self,
        request: main_models.ListFlowVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFlowVersionsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFlowVersions',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFlowVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_versions_with_options_async(
        self,
        request: main_models.ListFlowVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFlowVersionsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFlowVersions',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFlowVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flow_versions(
        self,
        request: main_models.ListFlowVersionsRequest,
    ) -> main_models.ListFlowVersionsResponse:
        runtime = RuntimeOptions()
        return self.list_flow_versions_with_options(request, runtime)

    async def list_flow_versions_async(
        self,
        request: main_models.ListFlowVersionsRequest,
    ) -> main_models.ListFlowVersionsResponse:
        runtime = RuntimeOptions()
        return await self.list_flow_versions_with_options_async(request, runtime)

    def list_flows_with_options(
        self,
        request: main_models.ListFlowsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFlowsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFlows',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFlowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flows_with_options_async(
        self,
        request: main_models.ListFlowsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFlowsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFlows',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFlowsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flows(
        self,
        request: main_models.ListFlowsRequest,
    ) -> main_models.ListFlowsResponse:
        runtime = RuntimeOptions()
        return self.list_flows_with_options(request, runtime)

    async def list_flows_async(
        self,
        request: main_models.ListFlowsRequest,
    ) -> main_models.ListFlowsResponse:
        runtime = RuntimeOptions()
        return await self.list_flows_with_options_async(request, runtime)

    def list_schedules_with_options(
        self,
        request: main_models.ListSchedulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSchedulesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSchedules',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSchedulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_schedules_with_options_async(
        self,
        request: main_models.ListSchedulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSchedulesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSchedules',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSchedulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_schedules(
        self,
        request: main_models.ListSchedulesRequest,
    ) -> main_models.ListSchedulesResponse:
        runtime = RuntimeOptions()
        return self.list_schedules_with_options(request, runtime)

    async def list_schedules_async(
        self,
        request: main_models.ListSchedulesRequest,
    ) -> main_models.ListSchedulesResponse:
        runtime = RuntimeOptions()
        return await self.list_schedules_with_options_async(request, runtime)

    def publish_flow_version_with_options(
        self,
        request: main_models.PublishFlowVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishFlowVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.flow_name):
            body['FlowName'] = request.flow_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PublishFlowVersion',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishFlowVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_flow_version_with_options_async(
        self,
        request: main_models.PublishFlowVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishFlowVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.flow_name):
            body['FlowName'] = request.flow_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PublishFlowVersion',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishFlowVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_flow_version(
        self,
        request: main_models.PublishFlowVersionRequest,
    ) -> main_models.PublishFlowVersionResponse:
        runtime = RuntimeOptions()
        return self.publish_flow_version_with_options(request, runtime)

    async def publish_flow_version_async(
        self,
        request: main_models.PublishFlowVersionRequest,
    ) -> main_models.PublishFlowVersionResponse:
        runtime = RuntimeOptions()
        return await self.publish_flow_version_with_options_async(request, runtime)

    def report_task_failed_with_options(
        self,
        request: main_models.ReportTaskFailedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReportTaskFailedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_token):
            query['TaskToken'] = request.task_token
        body = {}
        if not DaraCore.is_null(request.cause):
            body['Cause'] = request.cause
        if not DaraCore.is_null(request.error):
            body['Error'] = request.error
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReportTaskFailed',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReportTaskFailedResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_task_failed_with_options_async(
        self,
        request: main_models.ReportTaskFailedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReportTaskFailedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_token):
            query['TaskToken'] = request.task_token
        body = {}
        if not DaraCore.is_null(request.cause):
            body['Cause'] = request.cause
        if not DaraCore.is_null(request.error):
            body['Error'] = request.error
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReportTaskFailed',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReportTaskFailedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_task_failed(
        self,
        request: main_models.ReportTaskFailedRequest,
    ) -> main_models.ReportTaskFailedResponse:
        runtime = RuntimeOptions()
        return self.report_task_failed_with_options(request, runtime)

    async def report_task_failed_async(
        self,
        request: main_models.ReportTaskFailedRequest,
    ) -> main_models.ReportTaskFailedResponse:
        runtime = RuntimeOptions()
        return await self.report_task_failed_with_options_async(request, runtime)

    def report_task_succeeded_with_options(
        self,
        request: main_models.ReportTaskSucceededRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReportTaskSucceededResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_token):
            query['TaskToken'] = request.task_token
        body = {}
        if not DaraCore.is_null(request.output):
            body['Output'] = request.output
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReportTaskSucceeded',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReportTaskSucceededResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_task_succeeded_with_options_async(
        self,
        request: main_models.ReportTaskSucceededRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReportTaskSucceededResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_token):
            query['TaskToken'] = request.task_token
        body = {}
        if not DaraCore.is_null(request.output):
            body['Output'] = request.output
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReportTaskSucceeded',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReportTaskSucceededResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_task_succeeded(
        self,
        request: main_models.ReportTaskSucceededRequest,
    ) -> main_models.ReportTaskSucceededResponse:
        runtime = RuntimeOptions()
        return self.report_task_succeeded_with_options(request, runtime)

    async def report_task_succeeded_async(
        self,
        request: main_models.ReportTaskSucceededRequest,
    ) -> main_models.ReportTaskSucceededResponse:
        runtime = RuntimeOptions()
        return await self.report_task_succeeded_with_options_async(request, runtime)

    def start_execution_with_options(
        self,
        request: main_models.StartExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartExecutionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.callback_fn_ftask_token):
            body['CallbackFnFTaskToken'] = request.callback_fn_ftask_token
        if not DaraCore.is_null(request.execution_name):
            body['ExecutionName'] = request.execution_name
        if not DaraCore.is_null(request.flow_name):
            body['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.input):
            body['Input'] = request.input
        if not DaraCore.is_null(request.qualifier):
            body['Qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartExecution',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_execution_with_options_async(
        self,
        request: main_models.StartExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartExecutionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.callback_fn_ftask_token):
            body['CallbackFnFTaskToken'] = request.callback_fn_ftask_token
        if not DaraCore.is_null(request.execution_name):
            body['ExecutionName'] = request.execution_name
        if not DaraCore.is_null(request.flow_name):
            body['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.input):
            body['Input'] = request.input
        if not DaraCore.is_null(request.qualifier):
            body['Qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartExecution',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_execution(
        self,
        request: main_models.StartExecutionRequest,
    ) -> main_models.StartExecutionResponse:
        runtime = RuntimeOptions()
        return self.start_execution_with_options(request, runtime)

    async def start_execution_async(
        self,
        request: main_models.StartExecutionRequest,
    ) -> main_models.StartExecutionResponse:
        runtime = RuntimeOptions()
        return await self.start_execution_with_options_async(request, runtime)

    def start_sync_execution_with_options(
        self,
        request: main_models.StartSyncExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartSyncExecutionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.execution_name):
            body['ExecutionName'] = request.execution_name
        if not DaraCore.is_null(request.flow_name):
            body['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.input):
            body['Input'] = request.input
        if not DaraCore.is_null(request.qualifier):
            body['Qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartSyncExecution',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartSyncExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_sync_execution_with_options_async(
        self,
        request: main_models.StartSyncExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartSyncExecutionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.execution_name):
            body['ExecutionName'] = request.execution_name
        if not DaraCore.is_null(request.flow_name):
            body['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.input):
            body['Input'] = request.input
        if not DaraCore.is_null(request.qualifier):
            body['Qualifier'] = request.qualifier
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartSyncExecution',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartSyncExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_sync_execution(
        self,
        request: main_models.StartSyncExecutionRequest,
    ) -> main_models.StartSyncExecutionResponse:
        runtime = RuntimeOptions()
        return self.start_sync_execution_with_options(request, runtime)

    async def start_sync_execution_async(
        self,
        request: main_models.StartSyncExecutionRequest,
    ) -> main_models.StartSyncExecutionResponse:
        runtime = RuntimeOptions()
        return await self.start_sync_execution_with_options_async(request, runtime)

    def stop_execution_with_options(
        self,
        request: main_models.StopExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopExecutionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cause):
            body['Cause'] = request.cause
        if not DaraCore.is_null(request.error):
            body['Error'] = request.error
        if not DaraCore.is_null(request.execution_name):
            body['ExecutionName'] = request.execution_name
        if not DaraCore.is_null(request.flow_name):
            body['FlowName'] = request.flow_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopExecution',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_execution_with_options_async(
        self,
        request: main_models.StopExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopExecutionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cause):
            body['Cause'] = request.cause
        if not DaraCore.is_null(request.error):
            body['Error'] = request.error
        if not DaraCore.is_null(request.execution_name):
            body['ExecutionName'] = request.execution_name
        if not DaraCore.is_null(request.flow_name):
            body['FlowName'] = request.flow_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopExecution',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_execution(
        self,
        request: main_models.StopExecutionRequest,
    ) -> main_models.StopExecutionResponse:
        runtime = RuntimeOptions()
        return self.stop_execution_with_options(request, runtime)

    async def stop_execution_async(
        self,
        request: main_models.StopExecutionRequest,
    ) -> main_models.StopExecutionResponse:
        runtime = RuntimeOptions()
        return await self.stop_execution_with_options_async(request, runtime)

    def update_flow_with_options(
        self,
        tmp_req: main_models.UpdateFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFlowResponse:
        tmp_req.validate()
        request = main_models.UpdateFlowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.environment):
            request.environment_shrink = Utils.array_to_string_with_specified_style(tmp_req.environment, 'Environment', 'json')
        body = {}
        if not DaraCore.is_null(request.definition):
            body['Definition'] = request.definition
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.environment_shrink):
            body['Environment'] = request.environment_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.role_arn):
            body['RoleArn'] = request.role_arn
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFlow',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_flow_with_options_async(
        self,
        tmp_req: main_models.UpdateFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFlowResponse:
        tmp_req.validate()
        request = main_models.UpdateFlowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.environment):
            request.environment_shrink = Utils.array_to_string_with_specified_style(tmp_req.environment, 'Environment', 'json')
        body = {}
        if not DaraCore.is_null(request.definition):
            body['Definition'] = request.definition
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.environment_shrink):
            body['Environment'] = request.environment_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.role_arn):
            body['RoleArn'] = request.role_arn
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFlow',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_flow(
        self,
        request: main_models.UpdateFlowRequest,
    ) -> main_models.UpdateFlowResponse:
        runtime = RuntimeOptions()
        return self.update_flow_with_options(request, runtime)

    async def update_flow_async(
        self,
        request: main_models.UpdateFlowRequest,
    ) -> main_models.UpdateFlowResponse:
        runtime = RuntimeOptions()
        return await self.update_flow_with_options_async(request, runtime)

    def update_flow_alias_with_options(
        self,
        tmp_req: main_models.UpdateFlowAliasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFlowAliasResponse:
        tmp_req.validate()
        request = main_models.UpdateFlowAliasShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.routing_configurations):
            request.routing_configurations_shrink = Utils.array_to_string_with_specified_style(tmp_req.routing_configurations, 'RoutingConfigurations', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.flow_name):
            body['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.routing_configurations_shrink):
            body['RoutingConfigurations'] = request.routing_configurations_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFlowAlias',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFlowAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_flow_alias_with_options_async(
        self,
        tmp_req: main_models.UpdateFlowAliasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFlowAliasResponse:
        tmp_req.validate()
        request = main_models.UpdateFlowAliasShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.routing_configurations):
            request.routing_configurations_shrink = Utils.array_to_string_with_specified_style(tmp_req.routing_configurations, 'RoutingConfigurations', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.flow_name):
            body['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.routing_configurations_shrink):
            body['RoutingConfigurations'] = request.routing_configurations_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFlowAlias',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFlowAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_flow_alias(
        self,
        request: main_models.UpdateFlowAliasRequest,
    ) -> main_models.UpdateFlowAliasResponse:
        runtime = RuntimeOptions()
        return self.update_flow_alias_with_options(request, runtime)

    async def update_flow_alias_async(
        self,
        request: main_models.UpdateFlowAliasRequest,
    ) -> main_models.UpdateFlowAliasResponse:
        runtime = RuntimeOptions()
        return await self.update_flow_alias_with_options_async(request, runtime)

    def update_map_run_with_options(
        self,
        request: main_models.UpdateMapRunRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMapRunResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMapRun',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMapRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_map_run_with_options_async(
        self,
        request: main_models.UpdateMapRunRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMapRunResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMapRun',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMapRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_map_run(
        self,
        request: main_models.UpdateMapRunRequest,
    ) -> main_models.UpdateMapRunResponse:
        runtime = RuntimeOptions()
        return self.update_map_run_with_options(request, runtime)

    async def update_map_run_async(
        self,
        request: main_models.UpdateMapRunRequest,
    ) -> main_models.UpdateMapRunResponse:
        runtime = RuntimeOptions()
        return await self.update_map_run_with_options_async(request, runtime)

    def update_schedule_with_options(
        self,
        request: main_models.UpdateScheduleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateScheduleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cron_expression):
            body['CronExpression'] = request.cron_expression
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.enable):
            body['Enable'] = request.enable
        if not DaraCore.is_null(request.flow_name):
            body['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.payload):
            body['Payload'] = request.payload
        if not DaraCore.is_null(request.schedule_name):
            body['ScheduleName'] = request.schedule_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSchedule',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_schedule_with_options_async(
        self,
        request: main_models.UpdateScheduleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateScheduleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cron_expression):
            body['CronExpression'] = request.cron_expression
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.enable):
            body['Enable'] = request.enable
        if not DaraCore.is_null(request.flow_name):
            body['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.payload):
            body['Payload'] = request.payload
        if not DaraCore.is_null(request.schedule_name):
            body['ScheduleName'] = request.schedule_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSchedule',
            version = '2019-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_schedule(
        self,
        request: main_models.UpdateScheduleRequest,
    ) -> main_models.UpdateScheduleResponse:
        runtime = RuntimeOptions()
        return self.update_schedule_with_options(request, runtime)

    async def update_schedule_async(
        self,
        request: main_models.UpdateScheduleRequest,
    ) -> main_models.UpdateScheduleResponse:
        runtime = RuntimeOptions()
        return await self.update_schedule_with_options_async(request, runtime)
