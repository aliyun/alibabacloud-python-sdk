# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_fnf20190315 import models as fnf_20190315_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_flow_with_options(
        self,
        tmp_req: fnf_20190315_models.CreateFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.CreateFlowResponse:
        """
        @summary Creates a flow.
        
        @description ## [](#)Usage notes
        The number of flows that each user can create is restricted by resources. For more information, see [Limits](https://help.aliyun.com/document_detail/122093.html). If you want to create more flows, submit a ticket.
        At the user level, flows are distinguished by name. The name of a flow within one account must be unique.
        
        @param tmp_req: CreateFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFlowResponse
        """
        UtilClient.validate_model(tmp_req)
        request = fnf_20190315_models.CreateFlowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.environment):
            request.environment_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.environment, 'Environment', 'json')
        body = {}
        if not UtilClient.is_unset(request.definition):
            body['Definition'] = request.definition
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.environment_shrink):
            body['Environment'] = request.environment_shrink
        if not UtilClient.is_unset(request.execution_mode):
            body['ExecutionMode'] = request.execution_mode
        if not UtilClient.is_unset(request.external_storage_location):
            body['ExternalStorageLocation'] = request.external_storage_location
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.role_arn):
            body['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFlow',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.CreateFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_with_options_async(
        self,
        tmp_req: fnf_20190315_models.CreateFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.CreateFlowResponse:
        """
        @summary Creates a flow.
        
        @description ## [](#)Usage notes
        The number of flows that each user can create is restricted by resources. For more information, see [Limits](https://help.aliyun.com/document_detail/122093.html). If you want to create more flows, submit a ticket.
        At the user level, flows are distinguished by name. The name of a flow within one account must be unique.
        
        @param tmp_req: CreateFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFlowResponse
        """
        UtilClient.validate_model(tmp_req)
        request = fnf_20190315_models.CreateFlowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.environment):
            request.environment_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.environment, 'Environment', 'json')
        body = {}
        if not UtilClient.is_unset(request.definition):
            body['Definition'] = request.definition
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.environment_shrink):
            body['Environment'] = request.environment_shrink
        if not UtilClient.is_unset(request.execution_mode):
            body['ExecutionMode'] = request.execution_mode
        if not UtilClient.is_unset(request.external_storage_location):
            body['ExternalStorageLocation'] = request.external_storage_location
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.role_arn):
            body['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFlow',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.CreateFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_flow(
        self,
        request: fnf_20190315_models.CreateFlowRequest,
    ) -> fnf_20190315_models.CreateFlowResponse:
        """
        @summary Creates a flow.
        
        @description ## [](#)Usage notes
        The number of flows that each user can create is restricted by resources. For more information, see [Limits](https://help.aliyun.com/document_detail/122093.html). If you want to create more flows, submit a ticket.
        At the user level, flows are distinguished by name. The name of a flow within one account must be unique.
        
        @param request: CreateFlowRequest
        @return: CreateFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_flow_with_options(request, runtime)

    async def create_flow_async(
        self,
        request: fnf_20190315_models.CreateFlowRequest,
    ) -> fnf_20190315_models.CreateFlowResponse:
        """
        @summary Creates a flow.
        
        @description ## [](#)Usage notes
        The number of flows that each user can create is restricted by resources. For more information, see [Limits](https://help.aliyun.com/document_detail/122093.html). If you want to create more flows, submit a ticket.
        At the user level, flows are distinguished by name. The name of a flow within one account must be unique.
        
        @param request: CreateFlowRequest
        @return: CreateFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_flow_with_options_async(request, runtime)

    def create_flow_alias_with_options(
        self,
        tmp_req: fnf_20190315_models.CreateFlowAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.CreateFlowAliasResponse:
        """
        @summary 创建流程版本别名
        
        @param tmp_req: CreateFlowAliasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFlowAliasResponse
        """
        UtilClient.validate_model(tmp_req)
        request = fnf_20190315_models.CreateFlowAliasShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.routing_configurations):
            request.routing_configurations_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.routing_configurations, 'RoutingConfigurations', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.routing_configurations_shrink):
            body['RoutingConfigurations'] = request.routing_configurations_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFlowAlias',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.CreateFlowAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_alias_with_options_async(
        self,
        tmp_req: fnf_20190315_models.CreateFlowAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.CreateFlowAliasResponse:
        """
        @summary 创建流程版本别名
        
        @param tmp_req: CreateFlowAliasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFlowAliasResponse
        """
        UtilClient.validate_model(tmp_req)
        request = fnf_20190315_models.CreateFlowAliasShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.routing_configurations):
            request.routing_configurations_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.routing_configurations, 'RoutingConfigurations', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.routing_configurations_shrink):
            body['RoutingConfigurations'] = request.routing_configurations_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFlowAlias',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.CreateFlowAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_flow_alias(
        self,
        request: fnf_20190315_models.CreateFlowAliasRequest,
    ) -> fnf_20190315_models.CreateFlowAliasResponse:
        """
        @summary 创建流程版本别名
        
        @param request: CreateFlowAliasRequest
        @return: CreateFlowAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_flow_alias_with_options(request, runtime)

    async def create_flow_alias_async(
        self,
        request: fnf_20190315_models.CreateFlowAliasRequest,
    ) -> fnf_20190315_models.CreateFlowAliasResponse:
        """
        @summary 创建流程版本别名
        
        @param request: CreateFlowAliasRequest
        @return: CreateFlowAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_flow_alias_with_options_async(request, runtime)

    def create_schedule_with_options(
        self,
        request: fnf_20190315_models.CreateScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.CreateScheduleResponse:
        """
        @summary Creates a time-based schedule.
        
        @param request: CreateScheduleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScheduleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.signature_version):
            query['SignatureVersion'] = request.signature_version
        body = {}
        if not UtilClient.is_unset(request.cron_expression):
            body['CronExpression'] = request.cron_expression
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.payload):
            body['Payload'] = request.payload
        if not UtilClient.is_unset(request.schedule_name):
            body['ScheduleName'] = request.schedule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSchedule',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.CreateScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_schedule_with_options_async(
        self,
        request: fnf_20190315_models.CreateScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.CreateScheduleResponse:
        """
        @summary Creates a time-based schedule.
        
        @param request: CreateScheduleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScheduleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.signature_version):
            query['SignatureVersion'] = request.signature_version
        body = {}
        if not UtilClient.is_unset(request.cron_expression):
            body['CronExpression'] = request.cron_expression
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.payload):
            body['Payload'] = request.payload
        if not UtilClient.is_unset(request.schedule_name):
            body['ScheduleName'] = request.schedule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSchedule',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.CreateScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_schedule(
        self,
        request: fnf_20190315_models.CreateScheduleRequest,
    ) -> fnf_20190315_models.CreateScheduleResponse:
        """
        @summary Creates a time-based schedule.
        
        @param request: CreateScheduleRequest
        @return: CreateScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_schedule_with_options(request, runtime)

    async def create_schedule_async(
        self,
        request: fnf_20190315_models.CreateScheduleRequest,
    ) -> fnf_20190315_models.CreateScheduleResponse:
        """
        @summary Creates a time-based schedule.
        
        @param request: CreateScheduleRequest
        @return: CreateScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_schedule_with_options_async(request, runtime)

    def delete_flow_with_options(
        self,
        request: fnf_20190315_models.DeleteFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DeleteFlowResponse:
        """
        @summary Deletes an existing flow.
        
        @description ## [](#)Usage notes
        A delete operation is asynchronous. If this operation is successful, the system returns a successful response. If an existing flow is pending to be deleted, a new flow of the same name will not be affected by the existing one. After you delete a flow, you cannot query its historical executions. All executions in progress will stop after their most recent steps are complete.
        
        @param request: DeleteFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFlowResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFlow',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.DeleteFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_with_options_async(
        self,
        request: fnf_20190315_models.DeleteFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DeleteFlowResponse:
        """
        @summary Deletes an existing flow.
        
        @description ## [](#)Usage notes
        A delete operation is asynchronous. If this operation is successful, the system returns a successful response. If an existing flow is pending to be deleted, a new flow of the same name will not be affected by the existing one. After you delete a flow, you cannot query its historical executions. All executions in progress will stop after their most recent steps are complete.
        
        @param request: DeleteFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFlowResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFlow',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.DeleteFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_flow(
        self,
        request: fnf_20190315_models.DeleteFlowRequest,
    ) -> fnf_20190315_models.DeleteFlowResponse:
        """
        @summary Deletes an existing flow.
        
        @description ## [](#)Usage notes
        A delete operation is asynchronous. If this operation is successful, the system returns a successful response. If an existing flow is pending to be deleted, a new flow of the same name will not be affected by the existing one. After you delete a flow, you cannot query its historical executions. All executions in progress will stop after their most recent steps are complete.
        
        @param request: DeleteFlowRequest
        @return: DeleteFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_with_options(request, runtime)

    async def delete_flow_async(
        self,
        request: fnf_20190315_models.DeleteFlowRequest,
    ) -> fnf_20190315_models.DeleteFlowResponse:
        """
        @summary Deletes an existing flow.
        
        @description ## [](#)Usage notes
        A delete operation is asynchronous. If this operation is successful, the system returns a successful response. If an existing flow is pending to be deleted, a new flow of the same name will not be affected by the existing one. After you delete a flow, you cannot query its historical executions. All executions in progress will stop after their most recent steps are complete.
        
        @param request: DeleteFlowRequest
        @return: DeleteFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_flow_with_options_async(request, runtime)

    def delete_flow_alias_with_options(
        self,
        request: fnf_20190315_models.DeleteFlowAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DeleteFlowAliasResponse:
        """
        @summary 删除流程别名
        
        @param request: DeleteFlowAliasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFlowAliasResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFlowAlias',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.DeleteFlowAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_alias_with_options_async(
        self,
        request: fnf_20190315_models.DeleteFlowAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DeleteFlowAliasResponse:
        """
        @summary 删除流程别名
        
        @param request: DeleteFlowAliasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFlowAliasResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFlowAlias',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.DeleteFlowAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_flow_alias(
        self,
        request: fnf_20190315_models.DeleteFlowAliasRequest,
    ) -> fnf_20190315_models.DeleteFlowAliasResponse:
        """
        @summary 删除流程别名
        
        @param request: DeleteFlowAliasRequest
        @return: DeleteFlowAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_alias_with_options(request, runtime)

    async def delete_flow_alias_async(
        self,
        request: fnf_20190315_models.DeleteFlowAliasRequest,
    ) -> fnf_20190315_models.DeleteFlowAliasResponse:
        """
        @summary 删除流程别名
        
        @param request: DeleteFlowAliasRequest
        @return: DeleteFlowAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_flow_alias_with_options_async(request, runtime)

    def delete_flow_version_with_options(
        self,
        request: fnf_20190315_models.DeleteFlowVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DeleteFlowVersionResponse:
        """
        @summary 删除流程版本
        
        @param request: DeleteFlowVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFlowVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.flow_version):
            body['FlowVersion'] = request.flow_version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFlowVersion',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.DeleteFlowVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_version_with_options_async(
        self,
        request: fnf_20190315_models.DeleteFlowVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DeleteFlowVersionResponse:
        """
        @summary 删除流程版本
        
        @param request: DeleteFlowVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFlowVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.flow_version):
            body['FlowVersion'] = request.flow_version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFlowVersion',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.DeleteFlowVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_flow_version(
        self,
        request: fnf_20190315_models.DeleteFlowVersionRequest,
    ) -> fnf_20190315_models.DeleteFlowVersionResponse:
        """
        @summary 删除流程版本
        
        @param request: DeleteFlowVersionRequest
        @return: DeleteFlowVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_version_with_options(request, runtime)

    async def delete_flow_version_async(
        self,
        request: fnf_20190315_models.DeleteFlowVersionRequest,
    ) -> fnf_20190315_models.DeleteFlowVersionResponse:
        """
        @summary 删除流程版本
        
        @param request: DeleteFlowVersionRequest
        @return: DeleteFlowVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_flow_version_with_options_async(request, runtime)

    def delete_schedule_with_options(
        self,
        request: fnf_20190315_models.DeleteScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DeleteScheduleResponse:
        """
        @summary Deletes a time-based scheduling task.
        
        @param request: DeleteScheduleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScheduleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.schedule_name):
            body['ScheduleName'] = request.schedule_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSchedule',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.DeleteScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_schedule_with_options_async(
        self,
        request: fnf_20190315_models.DeleteScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DeleteScheduleResponse:
        """
        @summary Deletes a time-based scheduling task.
        
        @param request: DeleteScheduleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScheduleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.schedule_name):
            body['ScheduleName'] = request.schedule_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSchedule',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.DeleteScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_schedule(
        self,
        request: fnf_20190315_models.DeleteScheduleRequest,
    ) -> fnf_20190315_models.DeleteScheduleResponse:
        """
        @summary Deletes a time-based scheduling task.
        
        @param request: DeleteScheduleRequest
        @return: DeleteScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_schedule_with_options(request, runtime)

    async def delete_schedule_async(
        self,
        request: fnf_20190315_models.DeleteScheduleRequest,
    ) -> fnf_20190315_models.DeleteScheduleResponse:
        """
        @summary Deletes a time-based scheduling task.
        
        @param request: DeleteScheduleRequest
        @return: DeleteScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_schedule_with_options_async(request, runtime)

    def describe_execution_with_options(
        self,
        request: fnf_20190315_models.DescribeExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DescribeExecutionResponse:
        """
        @summary Queries an execution in a flow. The long polling mode is supported. The maximum waiting period for long polling depends on the value of the WaitTimeSeconds parameter.
        
        @param request: DescribeExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeExecutionResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExecution',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.DescribeExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_execution_with_options_async(
        self,
        request: fnf_20190315_models.DescribeExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DescribeExecutionResponse:
        """
        @summary Queries an execution in a flow. The long polling mode is supported. The maximum waiting period for long polling depends on the value of the WaitTimeSeconds parameter.
        
        @param request: DescribeExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeExecutionResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExecution',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.DescribeExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_execution(
        self,
        request: fnf_20190315_models.DescribeExecutionRequest,
    ) -> fnf_20190315_models.DescribeExecutionResponse:
        """
        @summary Queries an execution in a flow. The long polling mode is supported. The maximum waiting period for long polling depends on the value of the WaitTimeSeconds parameter.
        
        @param request: DescribeExecutionRequest
        @return: DescribeExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_execution_with_options(request, runtime)

    async def describe_execution_async(
        self,
        request: fnf_20190315_models.DescribeExecutionRequest,
    ) -> fnf_20190315_models.DescribeExecutionResponse:
        """
        @summary Queries an execution in a flow. The long polling mode is supported. The maximum waiting period for long polling depends on the value of the WaitTimeSeconds parameter.
        
        @param request: DescribeExecutionRequest
        @return: DescribeExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_execution_with_options_async(request, runtime)

    def describe_flow_with_options(
        self,
        request: fnf_20190315_models.DescribeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DescribeFlowResponse:
        """
        @summary Queries the information about a flow.
        
        @param request: DescribeFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFlowResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlow',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.DescribeFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_with_options_async(
        self,
        request: fnf_20190315_models.DescribeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DescribeFlowResponse:
        """
        @summary Queries the information about a flow.
        
        @param request: DescribeFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFlowResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlow',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.DescribeFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_flow(
        self,
        request: fnf_20190315_models.DescribeFlowRequest,
    ) -> fnf_20190315_models.DescribeFlowResponse:
        """
        @summary Queries the information about a flow.
        
        @param request: DescribeFlowRequest
        @return: DescribeFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_with_options(request, runtime)

    async def describe_flow_async(
        self,
        request: fnf_20190315_models.DescribeFlowRequest,
    ) -> fnf_20190315_models.DescribeFlowResponse:
        """
        @summary Queries the information about a flow.
        
        @param request: DescribeFlowRequest
        @return: DescribeFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_with_options_async(request, runtime)

    def describe_flow_alias_with_options(
        self,
        request: fnf_20190315_models.DescribeFlowAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DescribeFlowAliasResponse:
        """
        @summary 查询流程版本别名详情
        
        @param request: DescribeFlowAliasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFlowAliasResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowAlias',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.DescribeFlowAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_alias_with_options_async(
        self,
        request: fnf_20190315_models.DescribeFlowAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DescribeFlowAliasResponse:
        """
        @summary 查询流程版本别名详情
        
        @param request: DescribeFlowAliasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFlowAliasResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowAlias',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.DescribeFlowAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_flow_alias(
        self,
        request: fnf_20190315_models.DescribeFlowAliasRequest,
    ) -> fnf_20190315_models.DescribeFlowAliasResponse:
        """
        @summary 查询流程版本别名详情
        
        @param request: DescribeFlowAliasRequest
        @return: DescribeFlowAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_alias_with_options(request, runtime)

    async def describe_flow_alias_async(
        self,
        request: fnf_20190315_models.DescribeFlowAliasRequest,
    ) -> fnf_20190315_models.DescribeFlowAliasResponse:
        """
        @summary 查询流程版本别名详情
        
        @param request: DescribeFlowAliasRequest
        @return: DescribeFlowAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_alias_with_options_async(request, runtime)

    def describe_map_run_with_options(
        self,
        request: fnf_20190315_models.DescribeMapRunRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DescribeMapRunResponse:
        """
        @summary 查询 MapRun 详情
        
        @param request: DescribeMapRunRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMapRunResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMapRun',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.DescribeMapRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_map_run_with_options_async(
        self,
        request: fnf_20190315_models.DescribeMapRunRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DescribeMapRunResponse:
        """
        @summary 查询 MapRun 详情
        
        @param request: DescribeMapRunRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMapRunResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMapRun',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.DescribeMapRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_map_run(
        self,
        request: fnf_20190315_models.DescribeMapRunRequest,
    ) -> fnf_20190315_models.DescribeMapRunResponse:
        """
        @summary 查询 MapRun 详情
        
        @param request: DescribeMapRunRequest
        @return: DescribeMapRunResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_map_run_with_options(request, runtime)

    async def describe_map_run_async(
        self,
        request: fnf_20190315_models.DescribeMapRunRequest,
    ) -> fnf_20190315_models.DescribeMapRunResponse:
        """
        @summary 查询 MapRun 详情
        
        @param request: DescribeMapRunRequest
        @return: DescribeMapRunResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_map_run_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: fnf_20190315_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DescribeRegionsResponse:
        """
        @summary 查询地域信息列表
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: fnf_20190315_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DescribeRegionsResponse:
        """
        @summary 查询地域信息列表
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: fnf_20190315_models.DescribeRegionsRequest,
    ) -> fnf_20190315_models.DescribeRegionsResponse:
        """
        @summary 查询地域信息列表
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: fnf_20190315_models.DescribeRegionsRequest,
    ) -> fnf_20190315_models.DescribeRegionsResponse:
        """
        @summary 查询地域信息列表
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_schedule_with_options(
        self,
        request: fnf_20190315_models.DescribeScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DescribeScheduleResponse:
        """
        @summary Queries the detailed information about a time-based schedule.
        
        @param request: DescribeScheduleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScheduleResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSchedule',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.DescribeScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_schedule_with_options_async(
        self,
        request: fnf_20190315_models.DescribeScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.DescribeScheduleResponse:
        """
        @summary Queries the detailed information about a time-based schedule.
        
        @param request: DescribeScheduleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScheduleResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSchedule',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.DescribeScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_schedule(
        self,
        request: fnf_20190315_models.DescribeScheduleRequest,
    ) -> fnf_20190315_models.DescribeScheduleResponse:
        """
        @summary Queries the detailed information about a time-based schedule.
        
        @param request: DescribeScheduleRequest
        @return: DescribeScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_schedule_with_options(request, runtime)

    async def describe_schedule_async(
        self,
        request: fnf_20190315_models.DescribeScheduleRequest,
    ) -> fnf_20190315_models.DescribeScheduleResponse:
        """
        @summary Queries the detailed information about a time-based schedule.
        
        @param request: DescribeScheduleRequest
        @return: DescribeScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_schedule_with_options_async(request, runtime)

    def get_execution_history_with_options(
        self,
        request: fnf_20190315_models.GetExecutionHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.GetExecutionHistoryResponse:
        """
        @summary Queries the details about each step in an execution process.
        
        @param request: GetExecutionHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExecutionHistoryResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExecutionHistory',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.GetExecutionHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_execution_history_with_options_async(
        self,
        request: fnf_20190315_models.GetExecutionHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.GetExecutionHistoryResponse:
        """
        @summary Queries the details about each step in an execution process.
        
        @param request: GetExecutionHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExecutionHistoryResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExecutionHistory',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.GetExecutionHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_execution_history(
        self,
        request: fnf_20190315_models.GetExecutionHistoryRequest,
    ) -> fnf_20190315_models.GetExecutionHistoryResponse:
        """
        @summary Queries the details about each step in an execution process.
        
        @param request: GetExecutionHistoryRequest
        @return: GetExecutionHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_execution_history_with_options(request, runtime)

    async def get_execution_history_async(
        self,
        request: fnf_20190315_models.GetExecutionHistoryRequest,
    ) -> fnf_20190315_models.GetExecutionHistoryResponse:
        """
        @summary Queries the details about each step in an execution process.
        
        @param request: GetExecutionHistoryRequest
        @return: GetExecutionHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_execution_history_with_options_async(request, runtime)

    def list_executions_with_options(
        self,
        request: fnf_20190315_models.ListExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.ListExecutionsResponse:
        """
        @summary Queries all historical executions of a flow.
        
        @description ## [](#)Usage notes
        After you delete a flow, you cannot query its historical executions, even if you create a flow of the same name.
        
        @param request: ListExecutionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExecutionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExecutions',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.ListExecutionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_executions_with_options_async(
        self,
        request: fnf_20190315_models.ListExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.ListExecutionsResponse:
        """
        @summary Queries all historical executions of a flow.
        
        @description ## [](#)Usage notes
        After you delete a flow, you cannot query its historical executions, even if you create a flow of the same name.
        
        @param request: ListExecutionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExecutionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExecutions',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.ListExecutionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_executions(
        self,
        request: fnf_20190315_models.ListExecutionsRequest,
    ) -> fnf_20190315_models.ListExecutionsResponse:
        """
        @summary Queries all historical executions of a flow.
        
        @description ## [](#)Usage notes
        After you delete a flow, you cannot query its historical executions, even if you create a flow of the same name.
        
        @param request: ListExecutionsRequest
        @return: ListExecutionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_executions_with_options(request, runtime)

    async def list_executions_async(
        self,
        request: fnf_20190315_models.ListExecutionsRequest,
    ) -> fnf_20190315_models.ListExecutionsResponse:
        """
        @summary Queries all historical executions of a flow.
        
        @description ## [](#)Usage notes
        After you delete a flow, you cannot query its historical executions, even if you create a flow of the same name.
        
        @param request: ListExecutionsRequest
        @return: ListExecutionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_executions_with_options_async(request, runtime)

    def list_flow_aliases_with_options(
        self,
        request: fnf_20190315_models.ListFlowAliasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.ListFlowAliasesResponse:
        """
        @summary 查询流程版本别名列表
        
        @param request: ListFlowAliasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFlowAliasesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowAliases',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.ListFlowAliasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_aliases_with_options_async(
        self,
        request: fnf_20190315_models.ListFlowAliasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.ListFlowAliasesResponse:
        """
        @summary 查询流程版本别名列表
        
        @param request: ListFlowAliasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFlowAliasesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowAliases',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.ListFlowAliasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flow_aliases(
        self,
        request: fnf_20190315_models.ListFlowAliasesRequest,
    ) -> fnf_20190315_models.ListFlowAliasesResponse:
        """
        @summary 查询流程版本别名列表
        
        @param request: ListFlowAliasesRequest
        @return: ListFlowAliasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_flow_aliases_with_options(request, runtime)

    async def list_flow_aliases_async(
        self,
        request: fnf_20190315_models.ListFlowAliasesRequest,
    ) -> fnf_20190315_models.ListFlowAliasesResponse:
        """
        @summary 查询流程版本别名列表
        
        @param request: ListFlowAliasesRequest
        @return: ListFlowAliasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_aliases_with_options_async(request, runtime)

    def list_flow_versions_with_options(
        self,
        request: fnf_20190315_models.ListFlowVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.ListFlowVersionsResponse:
        """
        @summary 查询流程版本列表
        
        @param request: ListFlowVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFlowVersionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowVersions',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.ListFlowVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_versions_with_options_async(
        self,
        request: fnf_20190315_models.ListFlowVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.ListFlowVersionsResponse:
        """
        @summary 查询流程版本列表
        
        @param request: ListFlowVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFlowVersionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowVersions',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.ListFlowVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flow_versions(
        self,
        request: fnf_20190315_models.ListFlowVersionsRequest,
    ) -> fnf_20190315_models.ListFlowVersionsResponse:
        """
        @summary 查询流程版本列表
        
        @param request: ListFlowVersionsRequest
        @return: ListFlowVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_flow_versions_with_options(request, runtime)

    async def list_flow_versions_async(
        self,
        request: fnf_20190315_models.ListFlowVersionsRequest,
    ) -> fnf_20190315_models.ListFlowVersionsResponse:
        """
        @summary 查询流程版本列表
        
        @param request: ListFlowVersionsRequest
        @return: ListFlowVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_versions_with_options_async(request, runtime)

    def list_flows_with_options(
        self,
        request: fnf_20190315_models.ListFlowsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.ListFlowsResponse:
        """
        @summary Queries a list of flows.
        
        @param request: ListFlowsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFlowsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlows',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.ListFlowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flows_with_options_async(
        self,
        request: fnf_20190315_models.ListFlowsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.ListFlowsResponse:
        """
        @summary Queries a list of flows.
        
        @param request: ListFlowsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFlowsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlows',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.ListFlowsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flows(
        self,
        request: fnf_20190315_models.ListFlowsRequest,
    ) -> fnf_20190315_models.ListFlowsResponse:
        """
        @summary Queries a list of flows.
        
        @param request: ListFlowsRequest
        @return: ListFlowsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_flows_with_options(request, runtime)

    async def list_flows_async(
        self,
        request: fnf_20190315_models.ListFlowsRequest,
    ) -> fnf_20190315_models.ListFlowsResponse:
        """
        @summary Queries a list of flows.
        
        @param request: ListFlowsRequest
        @return: ListFlowsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_flows_with_options_async(request, runtime)

    def list_schedules_with_options(
        self,
        request: fnf_20190315_models.ListSchedulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.ListSchedulesResponse:
        """
        @summary Queries time-based schedules in a flow.
        
        @param request: ListSchedulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSchedulesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSchedules',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.ListSchedulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_schedules_with_options_async(
        self,
        request: fnf_20190315_models.ListSchedulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.ListSchedulesResponse:
        """
        @summary Queries time-based schedules in a flow.
        
        @param request: ListSchedulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSchedulesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSchedules',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.ListSchedulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_schedules(
        self,
        request: fnf_20190315_models.ListSchedulesRequest,
    ) -> fnf_20190315_models.ListSchedulesResponse:
        """
        @summary Queries time-based schedules in a flow.
        
        @param request: ListSchedulesRequest
        @return: ListSchedulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_schedules_with_options(request, runtime)

    async def list_schedules_async(
        self,
        request: fnf_20190315_models.ListSchedulesRequest,
    ) -> fnf_20190315_models.ListSchedulesResponse:
        """
        @summary Queries time-based schedules in a flow.
        
        @param request: ListSchedulesRequest
        @return: ListSchedulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_schedules_with_options_async(request, runtime)

    def publish_flow_version_with_options(
        self,
        request: fnf_20190315_models.PublishFlowVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.PublishFlowVersionResponse:
        """
        @summary 发布流程版本
        
        @param request: PublishFlowVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishFlowVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishFlowVersion',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.PublishFlowVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_flow_version_with_options_async(
        self,
        request: fnf_20190315_models.PublishFlowVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.PublishFlowVersionResponse:
        """
        @summary 发布流程版本
        
        @param request: PublishFlowVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishFlowVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishFlowVersion',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.PublishFlowVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_flow_version(
        self,
        request: fnf_20190315_models.PublishFlowVersionRequest,
    ) -> fnf_20190315_models.PublishFlowVersionResponse:
        """
        @summary 发布流程版本
        
        @param request: PublishFlowVersionRequest
        @return: PublishFlowVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.publish_flow_version_with_options(request, runtime)

    async def publish_flow_version_async(
        self,
        request: fnf_20190315_models.PublishFlowVersionRequest,
    ) -> fnf_20190315_models.PublishFlowVersionResponse:
        """
        @summary 发布流程版本
        
        @param request: PublishFlowVersionRequest
        @return: PublishFlowVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.publish_flow_version_with_options_async(request, runtime)

    def report_task_failed_with_options(
        self,
        request: fnf_20190315_models.ReportTaskFailedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.ReportTaskFailedResponse:
        """
        @summary Reports a failed task.
        
        @description ## [](#)Usage notes
        In the previous service (Serverless Workflow), the task step that ReportTaskFailed is used to call back `pattern: waitForCallback` indicates that the current task fails to be executed.
        In the new service (CloudFlow), the task step that ReportTaskFailed is used to call back `TaskMode: WaitForCustomCallback` indicates that the current task fails to be executed.
        
        @param request: ReportTaskFailedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReportTaskFailedResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_token):
            query['TaskToken'] = request.task_token
        body = {}
        if not UtilClient.is_unset(request.cause):
            body['Cause'] = request.cause
        if not UtilClient.is_unset(request.error):
            body['Error'] = request.error
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReportTaskFailed',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.ReportTaskFailedResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_task_failed_with_options_async(
        self,
        request: fnf_20190315_models.ReportTaskFailedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.ReportTaskFailedResponse:
        """
        @summary Reports a failed task.
        
        @description ## [](#)Usage notes
        In the previous service (Serverless Workflow), the task step that ReportTaskFailed is used to call back `pattern: waitForCallback` indicates that the current task fails to be executed.
        In the new service (CloudFlow), the task step that ReportTaskFailed is used to call back `TaskMode: WaitForCustomCallback` indicates that the current task fails to be executed.
        
        @param request: ReportTaskFailedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReportTaskFailedResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_token):
            query['TaskToken'] = request.task_token
        body = {}
        if not UtilClient.is_unset(request.cause):
            body['Cause'] = request.cause
        if not UtilClient.is_unset(request.error):
            body['Error'] = request.error
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReportTaskFailed',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.ReportTaskFailedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_task_failed(
        self,
        request: fnf_20190315_models.ReportTaskFailedRequest,
    ) -> fnf_20190315_models.ReportTaskFailedResponse:
        """
        @summary Reports a failed task.
        
        @description ## [](#)Usage notes
        In the previous service (Serverless Workflow), the task step that ReportTaskFailed is used to call back `pattern: waitForCallback` indicates that the current task fails to be executed.
        In the new service (CloudFlow), the task step that ReportTaskFailed is used to call back `TaskMode: WaitForCustomCallback` indicates that the current task fails to be executed.
        
        @param request: ReportTaskFailedRequest
        @return: ReportTaskFailedResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.report_task_failed_with_options(request, runtime)

    async def report_task_failed_async(
        self,
        request: fnf_20190315_models.ReportTaskFailedRequest,
    ) -> fnf_20190315_models.ReportTaskFailedResponse:
        """
        @summary Reports a failed task.
        
        @description ## [](#)Usage notes
        In the previous service (Serverless Workflow), the task step that ReportTaskFailed is used to call back `pattern: waitForCallback` indicates that the current task fails to be executed.
        In the new service (CloudFlow), the task step that ReportTaskFailed is used to call back `TaskMode: WaitForCustomCallback` indicates that the current task fails to be executed.
        
        @param request: ReportTaskFailedRequest
        @return: ReportTaskFailedResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.report_task_failed_with_options_async(request, runtime)

    def report_task_succeeded_with_options(
        self,
        request: fnf_20190315_models.ReportTaskSucceededRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.ReportTaskSucceededResponse:
        """
        @summary Reports a successful task.
        
        @description ## [](#)Usage notes
        In the previous service (Serverless Workflow), the task step that ReportTaskSucceeded is used to call back pattern: waitForCallback indicates that the current task is successfully executed.
        In the new service (CloudFlow), the task step that ReportTaskSucceeded is used to call back TaskMode: WaitForCustomCallback indicates that the current task is successfully executed.
        
        @param request: ReportTaskSucceededRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReportTaskSucceededResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_token):
            query['TaskToken'] = request.task_token
        body = {}
        if not UtilClient.is_unset(request.output):
            body['Output'] = request.output
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReportTaskSucceeded',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.ReportTaskSucceededResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_task_succeeded_with_options_async(
        self,
        request: fnf_20190315_models.ReportTaskSucceededRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.ReportTaskSucceededResponse:
        """
        @summary Reports a successful task.
        
        @description ## [](#)Usage notes
        In the previous service (Serverless Workflow), the task step that ReportTaskSucceeded is used to call back pattern: waitForCallback indicates that the current task is successfully executed.
        In the new service (CloudFlow), the task step that ReportTaskSucceeded is used to call back TaskMode: WaitForCustomCallback indicates that the current task is successfully executed.
        
        @param request: ReportTaskSucceededRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReportTaskSucceededResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_token):
            query['TaskToken'] = request.task_token
        body = {}
        if not UtilClient.is_unset(request.output):
            body['Output'] = request.output
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReportTaskSucceeded',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.ReportTaskSucceededResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_task_succeeded(
        self,
        request: fnf_20190315_models.ReportTaskSucceededRequest,
    ) -> fnf_20190315_models.ReportTaskSucceededResponse:
        """
        @summary Reports a successful task.
        
        @description ## [](#)Usage notes
        In the previous service (Serverless Workflow), the task step that ReportTaskSucceeded is used to call back pattern: waitForCallback indicates that the current task is successfully executed.
        In the new service (CloudFlow), the task step that ReportTaskSucceeded is used to call back TaskMode: WaitForCustomCallback indicates that the current task is successfully executed.
        
        @param request: ReportTaskSucceededRequest
        @return: ReportTaskSucceededResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.report_task_succeeded_with_options(request, runtime)

    async def report_task_succeeded_async(
        self,
        request: fnf_20190315_models.ReportTaskSucceededRequest,
    ) -> fnf_20190315_models.ReportTaskSucceededResponse:
        """
        @summary Reports a successful task.
        
        @description ## [](#)Usage notes
        In the previous service (Serverless Workflow), the task step that ReportTaskSucceeded is used to call back pattern: waitForCallback indicates that the current task is successfully executed.
        In the new service (CloudFlow), the task step that ReportTaskSucceeded is used to call back TaskMode: WaitForCustomCallback indicates that the current task is successfully executed.
        
        @param request: ReportTaskSucceededRequest
        @return: ReportTaskSucceededResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.report_task_succeeded_with_options_async(request, runtime)

    def start_execution_with_options(
        self,
        request: fnf_20190315_models.StartExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.StartExecutionResponse:
        """
        @summary Starts the execution of a workflow.
        
        @description ## [](#)Usage notes
        The flow is created. A flow only in standard mode is supported.
        If you do not specify an execution, the system automatically generates an execution and starts the execution.
        If an ongoing execution has the same name as that of the execution to be started, the system directly returns the ongoing execution.
        If the ongoing execution with the same name has ended (succeeded or failed), `ExecutionAlreadyExists` is returned.
        If no execution with the same name exists, the system starts a new execution.
        
        @param request: StartExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartExecutionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.callback_fn_ftask_token):
            body['CallbackFnFTaskToken'] = request.callback_fn_ftask_token
        if not UtilClient.is_unset(request.execution_name):
            body['ExecutionName'] = request.execution_name
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.input):
            body['Input'] = request.input
        if not UtilClient.is_unset(request.qualifier):
            body['Qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartExecution',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.StartExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_execution_with_options_async(
        self,
        request: fnf_20190315_models.StartExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.StartExecutionResponse:
        """
        @summary Starts the execution of a workflow.
        
        @description ## [](#)Usage notes
        The flow is created. A flow only in standard mode is supported.
        If you do not specify an execution, the system automatically generates an execution and starts the execution.
        If an ongoing execution has the same name as that of the execution to be started, the system directly returns the ongoing execution.
        If the ongoing execution with the same name has ended (succeeded or failed), `ExecutionAlreadyExists` is returned.
        If no execution with the same name exists, the system starts a new execution.
        
        @param request: StartExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartExecutionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.callback_fn_ftask_token):
            body['CallbackFnFTaskToken'] = request.callback_fn_ftask_token
        if not UtilClient.is_unset(request.execution_name):
            body['ExecutionName'] = request.execution_name
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.input):
            body['Input'] = request.input
        if not UtilClient.is_unset(request.qualifier):
            body['Qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartExecution',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.StartExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_execution(
        self,
        request: fnf_20190315_models.StartExecutionRequest,
    ) -> fnf_20190315_models.StartExecutionResponse:
        """
        @summary Starts the execution of a workflow.
        
        @description ## [](#)Usage notes
        The flow is created. A flow only in standard mode is supported.
        If you do not specify an execution, the system automatically generates an execution and starts the execution.
        If an ongoing execution has the same name as that of the execution to be started, the system directly returns the ongoing execution.
        If the ongoing execution with the same name has ended (succeeded or failed), `ExecutionAlreadyExists` is returned.
        If no execution with the same name exists, the system starts a new execution.
        
        @param request: StartExecutionRequest
        @return: StartExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_execution_with_options(request, runtime)

    async def start_execution_async(
        self,
        request: fnf_20190315_models.StartExecutionRequest,
    ) -> fnf_20190315_models.StartExecutionResponse:
        """
        @summary Starts the execution of a workflow.
        
        @description ## [](#)Usage notes
        The flow is created. A flow only in standard mode is supported.
        If you do not specify an execution, the system automatically generates an execution and starts the execution.
        If an ongoing execution has the same name as that of the execution to be started, the system directly returns the ongoing execution.
        If the ongoing execution with the same name has ended (succeeded or failed), `ExecutionAlreadyExists` is returned.
        If no execution with the same name exists, the system starts a new execution.
        
        @param request: StartExecutionRequest
        @return: StartExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_execution_with_options_async(request, runtime)

    def start_sync_execution_with_options(
        self,
        request: fnf_20190315_models.StartSyncExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.StartSyncExecutionResponse:
        """
        @summary Synchronously starts an execution in a flow.
        
        @description    Only flows of the express execution mode are supported.
        
        @param request: StartSyncExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartSyncExecutionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.execution_name):
            body['ExecutionName'] = request.execution_name
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.input):
            body['Input'] = request.input
        if not UtilClient.is_unset(request.qualifier):
            body['Qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartSyncExecution',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.StartSyncExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_sync_execution_with_options_async(
        self,
        request: fnf_20190315_models.StartSyncExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.StartSyncExecutionResponse:
        """
        @summary Synchronously starts an execution in a flow.
        
        @description    Only flows of the express execution mode are supported.
        
        @param request: StartSyncExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartSyncExecutionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.execution_name):
            body['ExecutionName'] = request.execution_name
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.input):
            body['Input'] = request.input
        if not UtilClient.is_unset(request.qualifier):
            body['Qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartSyncExecution',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.StartSyncExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_sync_execution(
        self,
        request: fnf_20190315_models.StartSyncExecutionRequest,
    ) -> fnf_20190315_models.StartSyncExecutionResponse:
        """
        @summary Synchronously starts an execution in a flow.
        
        @description    Only flows of the express execution mode are supported.
        
        @param request: StartSyncExecutionRequest
        @return: StartSyncExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_sync_execution_with_options(request, runtime)

    async def start_sync_execution_async(
        self,
        request: fnf_20190315_models.StartSyncExecutionRequest,
    ) -> fnf_20190315_models.StartSyncExecutionResponse:
        """
        @summary Synchronously starts an execution in a flow.
        
        @description    Only flows of the express execution mode are supported.
        
        @param request: StartSyncExecutionRequest
        @return: StartSyncExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_sync_execution_with_options_async(request, runtime)

    def stop_execution_with_options(
        self,
        request: fnf_20190315_models.StopExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.StopExecutionResponse:
        """
        @summary Stops an execution that is in progress in a flow.
        
        @description ## [](#)Usage notes
        The flow must be in progress.
        
        @param request: StopExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopExecutionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cause):
            body['Cause'] = request.cause
        if not UtilClient.is_unset(request.error):
            body['Error'] = request.error
        if not UtilClient.is_unset(request.execution_name):
            body['ExecutionName'] = request.execution_name
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopExecution',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.StopExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_execution_with_options_async(
        self,
        request: fnf_20190315_models.StopExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.StopExecutionResponse:
        """
        @summary Stops an execution that is in progress in a flow.
        
        @description ## [](#)Usage notes
        The flow must be in progress.
        
        @param request: StopExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopExecutionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cause):
            body['Cause'] = request.cause
        if not UtilClient.is_unset(request.error):
            body['Error'] = request.error
        if not UtilClient.is_unset(request.execution_name):
            body['ExecutionName'] = request.execution_name
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopExecution',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.StopExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_execution(
        self,
        request: fnf_20190315_models.StopExecutionRequest,
    ) -> fnf_20190315_models.StopExecutionResponse:
        """
        @summary Stops an execution that is in progress in a flow.
        
        @description ## [](#)Usage notes
        The flow must be in progress.
        
        @param request: StopExecutionRequest
        @return: StopExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_execution_with_options(request, runtime)

    async def stop_execution_async(
        self,
        request: fnf_20190315_models.StopExecutionRequest,
    ) -> fnf_20190315_models.StopExecutionResponse:
        """
        @summary Stops an execution that is in progress in a flow.
        
        @description ## [](#)Usage notes
        The flow must be in progress.
        
        @param request: StopExecutionRequest
        @return: StopExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_execution_with_options_async(request, runtime)

    def update_flow_with_options(
        self,
        tmp_req: fnf_20190315_models.UpdateFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.UpdateFlowResponse:
        """
        @summary Updates a flow.
        
        @param tmp_req: UpdateFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFlowResponse
        """
        UtilClient.validate_model(tmp_req)
        request = fnf_20190315_models.UpdateFlowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.environment):
            request.environment_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.environment, 'Environment', 'json')
        body = {}
        if not UtilClient.is_unset(request.definition):
            body['Definition'] = request.definition
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.environment_shrink):
            body['Environment'] = request.environment_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.role_arn):
            body['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFlow',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.UpdateFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_flow_with_options_async(
        self,
        tmp_req: fnf_20190315_models.UpdateFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.UpdateFlowResponse:
        """
        @summary Updates a flow.
        
        @param tmp_req: UpdateFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFlowResponse
        """
        UtilClient.validate_model(tmp_req)
        request = fnf_20190315_models.UpdateFlowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.environment):
            request.environment_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.environment, 'Environment', 'json')
        body = {}
        if not UtilClient.is_unset(request.definition):
            body['Definition'] = request.definition
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.environment_shrink):
            body['Environment'] = request.environment_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.role_arn):
            body['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFlow',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.UpdateFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_flow(
        self,
        request: fnf_20190315_models.UpdateFlowRequest,
    ) -> fnf_20190315_models.UpdateFlowResponse:
        """
        @summary Updates a flow.
        
        @param request: UpdateFlowRequest
        @return: UpdateFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_flow_with_options(request, runtime)

    async def update_flow_async(
        self,
        request: fnf_20190315_models.UpdateFlowRequest,
    ) -> fnf_20190315_models.UpdateFlowResponse:
        """
        @summary Updates a flow.
        
        @param request: UpdateFlowRequest
        @return: UpdateFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_flow_with_options_async(request, runtime)

    def update_flow_alias_with_options(
        self,
        tmp_req: fnf_20190315_models.UpdateFlowAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.UpdateFlowAliasResponse:
        """
        @summary 更新流程版本别名配置
        
        @param tmp_req: UpdateFlowAliasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFlowAliasResponse
        """
        UtilClient.validate_model(tmp_req)
        request = fnf_20190315_models.UpdateFlowAliasShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.routing_configurations):
            request.routing_configurations_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.routing_configurations, 'RoutingConfigurations', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.routing_configurations_shrink):
            body['RoutingConfigurations'] = request.routing_configurations_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFlowAlias',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.UpdateFlowAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_flow_alias_with_options_async(
        self,
        tmp_req: fnf_20190315_models.UpdateFlowAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.UpdateFlowAliasResponse:
        """
        @summary 更新流程版本别名配置
        
        @param tmp_req: UpdateFlowAliasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFlowAliasResponse
        """
        UtilClient.validate_model(tmp_req)
        request = fnf_20190315_models.UpdateFlowAliasShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.routing_configurations):
            request.routing_configurations_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.routing_configurations, 'RoutingConfigurations', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.routing_configurations_shrink):
            body['RoutingConfigurations'] = request.routing_configurations_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFlowAlias',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.UpdateFlowAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_flow_alias(
        self,
        request: fnf_20190315_models.UpdateFlowAliasRequest,
    ) -> fnf_20190315_models.UpdateFlowAliasResponse:
        """
        @summary 更新流程版本别名配置
        
        @param request: UpdateFlowAliasRequest
        @return: UpdateFlowAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_flow_alias_with_options(request, runtime)

    async def update_flow_alias_async(
        self,
        request: fnf_20190315_models.UpdateFlowAliasRequest,
    ) -> fnf_20190315_models.UpdateFlowAliasResponse:
        """
        @summary 更新流程版本别名配置
        
        @param request: UpdateFlowAliasRequest
        @return: UpdateFlowAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_flow_alias_with_options_async(request, runtime)

    def update_map_run_with_options(
        self,
        request: fnf_20190315_models.UpdateMapRunRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.UpdateMapRunResponse:
        """
        @summary 更新 MapRun 配置
        
        @param request: UpdateMapRunRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMapRunResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMapRun',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.UpdateMapRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_map_run_with_options_async(
        self,
        request: fnf_20190315_models.UpdateMapRunRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.UpdateMapRunResponse:
        """
        @summary 更新 MapRun 配置
        
        @param request: UpdateMapRunRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMapRunResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMapRun',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.UpdateMapRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_map_run(
        self,
        request: fnf_20190315_models.UpdateMapRunRequest,
    ) -> fnf_20190315_models.UpdateMapRunResponse:
        """
        @summary 更新 MapRun 配置
        
        @param request: UpdateMapRunRequest
        @return: UpdateMapRunResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_map_run_with_options(request, runtime)

    async def update_map_run_async(
        self,
        request: fnf_20190315_models.UpdateMapRunRequest,
    ) -> fnf_20190315_models.UpdateMapRunResponse:
        """
        @summary 更新 MapRun 配置
        
        @param request: UpdateMapRunRequest
        @return: UpdateMapRunResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_map_run_with_options_async(request, runtime)

    def update_schedule_with_options(
        self,
        request: fnf_20190315_models.UpdateScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.UpdateScheduleResponse:
        """
        @summary Updates a time-based schedule.
        
        @param request: UpdateScheduleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateScheduleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cron_expression):
            body['CronExpression'] = request.cron_expression
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.payload):
            body['Payload'] = request.payload
        if not UtilClient.is_unset(request.schedule_name):
            body['ScheduleName'] = request.schedule_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSchedule',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.UpdateScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_schedule_with_options_async(
        self,
        request: fnf_20190315_models.UpdateScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> fnf_20190315_models.UpdateScheduleResponse:
        """
        @summary Updates a time-based schedule.
        
        @param request: UpdateScheduleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateScheduleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cron_expression):
            body['CronExpression'] = request.cron_expression
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.enable):
            body['Enable'] = request.enable
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.payload):
            body['Payload'] = request.payload
        if not UtilClient.is_unset(request.schedule_name):
            body['ScheduleName'] = request.schedule_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSchedule',
            version='2019-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fnf_20190315_models.UpdateScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_schedule(
        self,
        request: fnf_20190315_models.UpdateScheduleRequest,
    ) -> fnf_20190315_models.UpdateScheduleResponse:
        """
        @summary Updates a time-based schedule.
        
        @param request: UpdateScheduleRequest
        @return: UpdateScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_schedule_with_options(request, runtime)

    async def update_schedule_async(
        self,
        request: fnf_20190315_models.UpdateScheduleRequest,
    ) -> fnf_20190315_models.UpdateScheduleResponse:
        """
        @summary Updates a time-based schedule.
        
        @param request: UpdateScheduleRequest
        @return: UpdateScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_schedule_with_options_async(request, runtime)
