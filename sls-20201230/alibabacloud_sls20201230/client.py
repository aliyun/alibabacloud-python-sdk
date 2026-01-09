# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_gateway_sls.client import Client as GatewayClientClient
from alibabacloud_sls20201230 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.core import DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._product_id = 'Sls'
        gateway_client = GatewayClientClient()
        self._spi = gateway_client
        self._endpoint_rule = 'central'

    def apply_config_to_machine_group_with_options(
        self,
        project: str,
        machine_group: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ApplyConfigToMachineGroupResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ApplyConfigToMachineGroup',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/machinegroups/{machine_group}/configs/{config_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.ApplyConfigToMachineGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def apply_config_to_machine_group_with_options_async(
        self,
        project: str,
        machine_group: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ApplyConfigToMachineGroupResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ApplyConfigToMachineGroup',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/machinegroups/{machine_group}/configs/{config_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.ApplyConfigToMachineGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def apply_config_to_machine_group(
        self,
        project: str,
        machine_group: str,
        config_name: str,
    ) -> main_models.ApplyConfigToMachineGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.apply_config_to_machine_group_with_options(project, machine_group, config_name, headers, runtime)

    async def apply_config_to_machine_group_async(
        self,
        project: str,
        machine_group: str,
        config_name: str,
    ) -> main_models.ApplyConfigToMachineGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.apply_config_to_machine_group_with_options_async(project, machine_group, config_name, headers, runtime)

    def call_ai_tools_with_options(
        self,
        request: main_models.CallAiToolsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CallAiToolsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.params):
            body['params'] = request.params
        if not DaraCore.is_null(request.region_id):
            body['regionId'] = request.region_id
        if not DaraCore.is_null(request.tool_name):
            body['toolName'] = request.tool_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CallAiTools',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/tool/call',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'string'
        )
        return DaraCore.from_map(
            main_models.CallAiToolsResponse(),
            self.execute(params, req, runtime)
        )

    async def call_ai_tools_with_options_async(
        self,
        request: main_models.CallAiToolsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CallAiToolsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.params):
            body['params'] = request.params
        if not DaraCore.is_null(request.region_id):
            body['regionId'] = request.region_id
        if not DaraCore.is_null(request.tool_name):
            body['toolName'] = request.tool_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CallAiTools',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/tool/call',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'string'
        )
        return DaraCore.from_map(
            main_models.CallAiToolsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def call_ai_tools(
        self,
        request: main_models.CallAiToolsRequest,
    ) -> main_models.CallAiToolsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.call_ai_tools_with_options(request, headers, runtime)

    async def call_ai_tools_async(
        self,
        request: main_models.CallAiToolsRequest,
    ) -> main_models.CallAiToolsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.call_ai_tools_with_options_async(request, headers, runtime)

    def change_resource_group_with_options(
        self,
        project: str,
        request: main_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            body['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/resourcegroup',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        project: str,
        request: main_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            body['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/resourcegroup',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        project: str,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.change_resource_group_with_options(project, request, headers, runtime)

    async def change_resource_group_async(
        self,
        project: str,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.change_resource_group_with_options_async(project, request, headers, runtime)

    def consumer_group_heart_beat_with_options(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: main_models.ConsumerGroupHeartBeatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ConsumerGroupHeartBeatResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.consumer):
            query['consumer'] = request.consumer
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'ConsumerGroupHeartBeat',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/consumergroups/{consumer_group}?type=heartbeat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.ConsumerGroupHeartBeatResponse(),
            self.execute(params, req, runtime)
        )

    async def consumer_group_heart_beat_with_options_async(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: main_models.ConsumerGroupHeartBeatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ConsumerGroupHeartBeatResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.consumer):
            query['consumer'] = request.consumer
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'ConsumerGroupHeartBeat',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/consumergroups/{consumer_group}?type=heartbeat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.ConsumerGroupHeartBeatResponse(),
            await self.execute_async(params, req, runtime)
        )

    def consumer_group_heart_beat(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: main_models.ConsumerGroupHeartBeatRequest,
    ) -> main_models.ConsumerGroupHeartBeatResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.consumer_group_heart_beat_with_options(project, logstore, consumer_group, request, headers, runtime)

    async def consumer_group_heart_beat_async(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: main_models.ConsumerGroupHeartBeatRequest,
    ) -> main_models.ConsumerGroupHeartBeatResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.consumer_group_heart_beat_with_options_async(project, logstore, consumer_group, request, headers, runtime)

    def consumer_group_update_check_point_with_options(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: main_models.ConsumerGroupUpdateCheckPointRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ConsumerGroupUpdateCheckPointResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.consumer):
            query['consumer'] = request.consumer
        if not DaraCore.is_null(request.force_success):
            query['forceSuccess'] = request.force_success
        body = {}
        if not DaraCore.is_null(request.checkpoint):
            body['checkpoint'] = request.checkpoint
        if not DaraCore.is_null(request.shard):
            body['shard'] = request.shard
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ConsumerGroupUpdateCheckPoint',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/consumergroups/{consumer_group}?type=checkpoint',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.ConsumerGroupUpdateCheckPointResponse(),
            self.execute(params, req, runtime)
        )

    async def consumer_group_update_check_point_with_options_async(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: main_models.ConsumerGroupUpdateCheckPointRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ConsumerGroupUpdateCheckPointResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.consumer):
            query['consumer'] = request.consumer
        if not DaraCore.is_null(request.force_success):
            query['forceSuccess'] = request.force_success
        body = {}
        if not DaraCore.is_null(request.checkpoint):
            body['checkpoint'] = request.checkpoint
        if not DaraCore.is_null(request.shard):
            body['shard'] = request.shard
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ConsumerGroupUpdateCheckPoint',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/consumergroups/{consumer_group}?type=checkpoint',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.ConsumerGroupUpdateCheckPointResponse(),
            await self.execute_async(params, req, runtime)
        )

    def consumer_group_update_check_point(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: main_models.ConsumerGroupUpdateCheckPointRequest,
    ) -> main_models.ConsumerGroupUpdateCheckPointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.consumer_group_update_check_point_with_options(project, logstore, consumer_group, request, headers, runtime)

    async def consumer_group_update_check_point_async(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: main_models.ConsumerGroupUpdateCheckPointRequest,
    ) -> main_models.ConsumerGroupUpdateCheckPointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.consumer_group_update_check_point_with_options_async(project, logstore, consumer_group, request, headers, runtime)

    def create_agent_instance_config_with_options(
        self,
        request: main_models.CreateAgentInstanceConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentInstanceConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attributes):
            body['attributes'] = request.attributes
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.config_type):
            body['configType'] = request.config_type
        if not DaraCore.is_null(request.gray_configs):
            body['grayConfigs'] = request.gray_configs
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgentInstanceConfig',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/agentinstanceconfigs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateAgentInstanceConfigResponse(),
            self.execute(params, req, runtime)
        )

    async def create_agent_instance_config_with_options_async(
        self,
        request: main_models.CreateAgentInstanceConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentInstanceConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attributes):
            body['attributes'] = request.attributes
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.config_type):
            body['configType'] = request.config_type
        if not DaraCore.is_null(request.gray_configs):
            body['grayConfigs'] = request.gray_configs
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgentInstanceConfig',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/agentinstanceconfigs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateAgentInstanceConfigResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_agent_instance_config(
        self,
        request: main_models.CreateAgentInstanceConfigRequest,
    ) -> main_models.CreateAgentInstanceConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_agent_instance_config_with_options(request, headers, runtime)

    async def create_agent_instance_config_async(
        self,
        request: main_models.CreateAgentInstanceConfigRequest,
    ) -> main_models.CreateAgentInstanceConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_agent_instance_config_with_options_async(request, headers, runtime)

    def create_alert_with_options(
        self,
        project: str,
        request: main_models.CreateAlertRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAlertResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.schedule):
            body['schedule'] = request.schedule
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAlert',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/alerts',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateAlertResponse(),
            self.execute(params, req, runtime)
        )

    async def create_alert_with_options_async(
        self,
        project: str,
        request: main_models.CreateAlertRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAlertResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.schedule):
            body['schedule'] = request.schedule
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAlert',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/alerts',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateAlertResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_alert(
        self,
        project: str,
        request: main_models.CreateAlertRequest,
    ) -> main_models.CreateAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_alert_with_options(project, request, headers, runtime)

    async def create_alert_async(
        self,
        project: str,
        request: main_models.CreateAlertRequest,
    ) -> main_models.CreateAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_alert_with_options_async(project, request, headers, runtime)

    def create_annotation_data_set_with_options(
        self,
        request: main_models.CreateAnnotationDataSetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAnnotationDataSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_id):
            query['datasetId'] = request.dataset_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAnnotationDataSet',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/annotationdataset',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateAnnotationDataSetResponse(),
            self.execute(params, req, runtime)
        )

    async def create_annotation_data_set_with_options_async(
        self,
        request: main_models.CreateAnnotationDataSetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAnnotationDataSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_id):
            query['datasetId'] = request.dataset_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAnnotationDataSet',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/annotationdataset',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateAnnotationDataSetResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_annotation_data_set(
        self,
        request: main_models.CreateAnnotationDataSetRequest,
    ) -> main_models.CreateAnnotationDataSetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_annotation_data_set_with_options(request, headers, runtime)

    async def create_annotation_data_set_async(
        self,
        request: main_models.CreateAnnotationDataSetRequest,
    ) -> main_models.CreateAnnotationDataSetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_annotation_data_set_with_options_async(request, headers, runtime)

    def create_annotation_label_with_options(
        self,
        request: main_models.CreateAnnotationLabelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAnnotationLabelResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAnnotationLabel',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/annotationlabel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateAnnotationLabelResponse(),
            self.execute(params, req, runtime)
        )

    async def create_annotation_label_with_options_async(
        self,
        request: main_models.CreateAnnotationLabelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAnnotationLabelResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAnnotationLabel',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/annotationlabel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateAnnotationLabelResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_annotation_label(
        self,
        request: main_models.CreateAnnotationLabelRequest,
    ) -> main_models.CreateAnnotationLabelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_annotation_label_with_options(request, headers, runtime)

    async def create_annotation_label_async(
        self,
        request: main_models.CreateAnnotationLabelRequest,
    ) -> main_models.CreateAnnotationLabelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_annotation_label_with_options_async(request, headers, runtime)

    def create_azure_blob_ingestion_with_options(
        self,
        project: str,
        request: main_models.CreateAzureBlobIngestionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAzureBlobIngestionResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.schedule):
            body['schedule'] = request.schedule
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAzureBlobIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/azureblobingestions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateAzureBlobIngestionResponse(),
            self.execute(params, req, runtime)
        )

    async def create_azure_blob_ingestion_with_options_async(
        self,
        project: str,
        request: main_models.CreateAzureBlobIngestionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAzureBlobIngestionResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.schedule):
            body['schedule'] = request.schedule
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAzureBlobIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/azureblobingestions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateAzureBlobIngestionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_azure_blob_ingestion(
        self,
        project: str,
        request: main_models.CreateAzureBlobIngestionRequest,
    ) -> main_models.CreateAzureBlobIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_azure_blob_ingestion_with_options(project, request, headers, runtime)

    async def create_azure_blob_ingestion_async(
        self,
        project: str,
        request: main_models.CreateAzureBlobIngestionRequest,
    ) -> main_models.CreateAzureBlobIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_azure_blob_ingestion_with_options_async(project, request, headers, runtime)

    def create_config_with_options(
        self,
        project: str,
        request: main_models.CreateConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConfigResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConfig',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/configs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateConfigResponse(),
            self.execute(params, req, runtime)
        )

    async def create_config_with_options_async(
        self,
        project: str,
        request: main_models.CreateConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConfigResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConfig',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/configs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateConfigResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_config(
        self,
        project: str,
        request: main_models.CreateConfigRequest,
    ) -> main_models.CreateConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_config_with_options(project, request, headers, runtime)

    async def create_config_async(
        self,
        project: str,
        request: main_models.CreateConfigRequest,
    ) -> main_models.CreateConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_config_with_options_async(project, request, headers, runtime)

    def create_consumer_group_with_options(
        self,
        project: str,
        logstore: str,
        request: main_models.CreateConsumerGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConsumerGroupResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.consumer_group):
            body['consumerGroup'] = request.consumer_group
        if not DaraCore.is_null(request.order):
            body['order'] = request.order
        if not DaraCore.is_null(request.timeout):
            body['timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConsumerGroup',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/consumergroups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateConsumerGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def create_consumer_group_with_options_async(
        self,
        project: str,
        logstore: str,
        request: main_models.CreateConsumerGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConsumerGroupResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.consumer_group):
            body['consumerGroup'] = request.consumer_group
        if not DaraCore.is_null(request.order):
            body['order'] = request.order
        if not DaraCore.is_null(request.timeout):
            body['timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConsumerGroup',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/consumergroups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateConsumerGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_consumer_group(
        self,
        project: str,
        logstore: str,
        request: main_models.CreateConsumerGroupRequest,
    ) -> main_models.CreateConsumerGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_consumer_group_with_options(project, logstore, request, headers, runtime)

    async def create_consumer_group_async(
        self,
        project: str,
        logstore: str,
        request: main_models.CreateConsumerGroupRequest,
    ) -> main_models.CreateConsumerGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_consumer_group_with_options_async(project, logstore, request, headers, runtime)

    def create_dashboard_with_options(
        self,
        project: str,
        request: main_models.CreateDashboardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDashboardResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDashboard',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/dashboards',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateDashboardResponse(),
            self.execute(params, req, runtime)
        )

    async def create_dashboard_with_options_async(
        self,
        project: str,
        request: main_models.CreateDashboardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDashboardResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDashboard',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/dashboards',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateDashboardResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_dashboard(
        self,
        project: str,
        request: main_models.CreateDashboardRequest,
    ) -> main_models.CreateDashboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_dashboard_with_options(project, request, headers, runtime)

    async def create_dashboard_async(
        self,
        project: str,
        request: main_models.CreateDashboardRequest,
    ) -> main_models.CreateDashboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_dashboard_with_options_async(project, request, headers, runtime)

    def create_domain_with_options(
        self,
        project: str,
        request: main_models.CreateDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDomainResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.domain_name):
            body['domainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDomain',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/domains',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateDomainResponse(),
            self.execute(params, req, runtime)
        )

    async def create_domain_with_options_async(
        self,
        project: str,
        request: main_models.CreateDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDomainResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.domain_name):
            body['domainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDomain',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/domains',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateDomainResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_domain(
        self,
        project: str,
        request: main_models.CreateDomainRequest,
    ) -> main_models.CreateDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_domain_with_options(project, request, headers, runtime)

    async def create_domain_async(
        self,
        project: str,
        request: main_models.CreateDomainRequest,
    ) -> main_models.CreateDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_domain_with_options_async(project, request, headers, runtime)

    def create_download_job_with_options(
        self,
        project: str,
        request: main_models.CreateDownloadJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDownloadJobResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDownloadJob',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/downloadjobs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateDownloadJobResponse(),
            self.execute(params, req, runtime)
        )

    async def create_download_job_with_options_async(
        self,
        project: str,
        request: main_models.CreateDownloadJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDownloadJobResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDownloadJob',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/downloadjobs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateDownloadJobResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_download_job(
        self,
        project: str,
        request: main_models.CreateDownloadJobRequest,
    ) -> main_models.CreateDownloadJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_download_job_with_options(project, request, headers, runtime)

    async def create_download_job_async(
        self,
        project: str,
        request: main_models.CreateDownloadJobRequest,
    ) -> main_models.CreateDownloadJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_download_job_with_options_async(project, request, headers, runtime)

    def create_etlwith_options(
        self,
        project: str,
        request: main_models.CreateETLRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateETLResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateETL',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/etls',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateETLResponse(),
            self.execute(params, req, runtime)
        )

    async def create_etlwith_options_async(
        self,
        project: str,
        request: main_models.CreateETLRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateETLResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateETL',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/etls',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateETLResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_etl(
        self,
        project: str,
        request: main_models.CreateETLRequest,
    ) -> main_models.CreateETLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_etlwith_options(project, request, headers, runtime)

    async def create_etl_async(
        self,
        project: str,
        request: main_models.CreateETLRequest,
    ) -> main_models.CreateETLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_etlwith_options_async(project, request, headers, runtime)

    def create_elasticsearch_ingestion_with_options(
        self,
        project: str,
        request: main_models.CreateElasticsearchIngestionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateElasticsearchIngestionResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.schedule):
            body['schedule'] = request.schedule
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateElasticsearchIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/elasticsearchingestions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateElasticsearchIngestionResponse(),
            self.execute(params, req, runtime)
        )

    async def create_elasticsearch_ingestion_with_options_async(
        self,
        project: str,
        request: main_models.CreateElasticsearchIngestionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateElasticsearchIngestionResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.schedule):
            body['schedule'] = request.schedule
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateElasticsearchIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/elasticsearchingestions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateElasticsearchIngestionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_elasticsearch_ingestion(
        self,
        project: str,
        request: main_models.CreateElasticsearchIngestionRequest,
    ) -> main_models.CreateElasticsearchIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_elasticsearch_ingestion_with_options(project, request, headers, runtime)

    async def create_elasticsearch_ingestion_async(
        self,
        project: str,
        request: main_models.CreateElasticsearchIngestionRequest,
    ) -> main_models.CreateElasticsearchIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_elasticsearch_ingestion_with_options_async(project, request, headers, runtime)

    def create_index_with_options(
        self,
        project: str,
        logstore: str,
        request: main_models.CreateIndexRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateIndexResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIndex',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/index',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateIndexResponse(),
            self.execute(params, req, runtime)
        )

    async def create_index_with_options_async(
        self,
        project: str,
        logstore: str,
        request: main_models.CreateIndexRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateIndexResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIndex',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/index',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateIndexResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_index(
        self,
        project: str,
        logstore: str,
        request: main_models.CreateIndexRequest,
    ) -> main_models.CreateIndexResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_index_with_options(project, logstore, request, headers, runtime)

    async def create_index_async(
        self,
        project: str,
        logstore: str,
        request: main_models.CreateIndexRequest,
    ) -> main_models.CreateIndexResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_index_with_options_async(project, logstore, request, headers, runtime)

    def create_log_store_with_options(
        self,
        project: str,
        request: main_models.CreateLogStoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLogStoreResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.append_meta):
            body['appendMeta'] = request.append_meta
        if not DaraCore.is_null(request.auto_split):
            body['autoSplit'] = request.auto_split
        if not DaraCore.is_null(request.enable_tracking):
            body['enable_tracking'] = request.enable_tracking
        if not DaraCore.is_null(request.encrypt_conf):
            body['encrypt_conf'] = request.encrypt_conf
        if not DaraCore.is_null(request.hot_ttl):
            body['hot_ttl'] = request.hot_ttl
        if not DaraCore.is_null(request.infrequent_access_ttl):
            body['infrequentAccessTTL'] = request.infrequent_access_ttl
        if not DaraCore.is_null(request.logstore_name):
            body['logstoreName'] = request.logstore_name
        if not DaraCore.is_null(request.max_split_shard):
            body['maxSplitShard'] = request.max_split_shard
        if not DaraCore.is_null(request.mode):
            body['mode'] = request.mode
        if not DaraCore.is_null(request.processor_id):
            body['processorId'] = request.processor_id
        if not DaraCore.is_null(request.shard_count):
            body['shardCount'] = request.shard_count
        if not DaraCore.is_null(request.sharding_policy):
            body['shardingPolicy'] = request.sharding_policy
        if not DaraCore.is_null(request.telemetry_type):
            body['telemetryType'] = request.telemetry_type
        if not DaraCore.is_null(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLogStore',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateLogStoreResponse(),
            self.execute(params, req, runtime)
        )

    async def create_log_store_with_options_async(
        self,
        project: str,
        request: main_models.CreateLogStoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLogStoreResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.append_meta):
            body['appendMeta'] = request.append_meta
        if not DaraCore.is_null(request.auto_split):
            body['autoSplit'] = request.auto_split
        if not DaraCore.is_null(request.enable_tracking):
            body['enable_tracking'] = request.enable_tracking
        if not DaraCore.is_null(request.encrypt_conf):
            body['encrypt_conf'] = request.encrypt_conf
        if not DaraCore.is_null(request.hot_ttl):
            body['hot_ttl'] = request.hot_ttl
        if not DaraCore.is_null(request.infrequent_access_ttl):
            body['infrequentAccessTTL'] = request.infrequent_access_ttl
        if not DaraCore.is_null(request.logstore_name):
            body['logstoreName'] = request.logstore_name
        if not DaraCore.is_null(request.max_split_shard):
            body['maxSplitShard'] = request.max_split_shard
        if not DaraCore.is_null(request.mode):
            body['mode'] = request.mode
        if not DaraCore.is_null(request.processor_id):
            body['processorId'] = request.processor_id
        if not DaraCore.is_null(request.shard_count):
            body['shardCount'] = request.shard_count
        if not DaraCore.is_null(request.sharding_policy):
            body['shardingPolicy'] = request.sharding_policy
        if not DaraCore.is_null(request.telemetry_type):
            body['telemetryType'] = request.telemetry_type
        if not DaraCore.is_null(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLogStore',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateLogStoreResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_log_store(
        self,
        project: str,
        request: main_models.CreateLogStoreRequest,
    ) -> main_models.CreateLogStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_log_store_with_options(project, request, headers, runtime)

    async def create_log_store_async(
        self,
        project: str,
        request: main_models.CreateLogStoreRequest,
    ) -> main_models.CreateLogStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_log_store_with_options_async(project, request, headers, runtime)

    def create_logging_with_options(
        self,
        project: str,
        request: main_models.CreateLoggingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLoggingResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.logging_details):
            body['loggingDetails'] = request.logging_details
        if not DaraCore.is_null(request.logging_project):
            body['loggingProject'] = request.logging_project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLogging',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logging',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateLoggingResponse(),
            self.execute(params, req, runtime)
        )

    async def create_logging_with_options_async(
        self,
        project: str,
        request: main_models.CreateLoggingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLoggingResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.logging_details):
            body['loggingDetails'] = request.logging_details
        if not DaraCore.is_null(request.logging_project):
            body['loggingProject'] = request.logging_project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLogging',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logging',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateLoggingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_logging(
        self,
        project: str,
        request: main_models.CreateLoggingRequest,
    ) -> main_models.CreateLoggingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_logging_with_options(project, request, headers, runtime)

    async def create_logging_async(
        self,
        project: str,
        request: main_models.CreateLoggingRequest,
    ) -> main_models.CreateLoggingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_logging_with_options_async(project, request, headers, runtime)

    def create_logtail_pipeline_config_with_options(
        self,
        project: str,
        request: main_models.CreateLogtailPipelineConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLogtailPipelineConfigResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.aggregators):
            body['aggregators'] = request.aggregators
        if not DaraCore.is_null(request.config_name):
            body['configName'] = request.config_name
        if not DaraCore.is_null(request.flushers):
            body['flushers'] = request.flushers
        if not DaraCore.is_null(request.global_):
            body['global'] = request.global_
        if not DaraCore.is_null(request.inputs):
            body['inputs'] = request.inputs
        if not DaraCore.is_null(request.log_sample):
            body['logSample'] = request.log_sample
        if not DaraCore.is_null(request.processors):
            body['processors'] = request.processors
        if not DaraCore.is_null(request.task):
            body['task'] = request.task
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLogtailPipelineConfig',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/pipelineconfigs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateLogtailPipelineConfigResponse(),
            self.execute(params, req, runtime)
        )

    async def create_logtail_pipeline_config_with_options_async(
        self,
        project: str,
        request: main_models.CreateLogtailPipelineConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLogtailPipelineConfigResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.aggregators):
            body['aggregators'] = request.aggregators
        if not DaraCore.is_null(request.config_name):
            body['configName'] = request.config_name
        if not DaraCore.is_null(request.flushers):
            body['flushers'] = request.flushers
        if not DaraCore.is_null(request.global_):
            body['global'] = request.global_
        if not DaraCore.is_null(request.inputs):
            body['inputs'] = request.inputs
        if not DaraCore.is_null(request.log_sample):
            body['logSample'] = request.log_sample
        if not DaraCore.is_null(request.processors):
            body['processors'] = request.processors
        if not DaraCore.is_null(request.task):
            body['task'] = request.task
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLogtailPipelineConfig',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/pipelineconfigs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateLogtailPipelineConfigResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_logtail_pipeline_config(
        self,
        project: str,
        request: main_models.CreateLogtailPipelineConfigRequest,
    ) -> main_models.CreateLogtailPipelineConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_logtail_pipeline_config_with_options(project, request, headers, runtime)

    async def create_logtail_pipeline_config_async(
        self,
        project: str,
        request: main_models.CreateLogtailPipelineConfigRequest,
    ) -> main_models.CreateLogtailPipelineConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_logtail_pipeline_config_with_options_async(project, request, headers, runtime)

    def create_machine_group_with_options(
        self,
        project: str,
        request: main_models.CreateMachineGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMachineGroupResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.group_attribute):
            body['groupAttribute'] = request.group_attribute
        if not DaraCore.is_null(request.group_name):
            body['groupName'] = request.group_name
        if not DaraCore.is_null(request.group_type):
            body['groupType'] = request.group_type
        if not DaraCore.is_null(request.machine_identify_type):
            body['machineIdentifyType'] = request.machine_identify_type
        if not DaraCore.is_null(request.machine_list):
            body['machineList'] = request.machine_list
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMachineGroup',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/machinegroups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateMachineGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def create_machine_group_with_options_async(
        self,
        project: str,
        request: main_models.CreateMachineGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMachineGroupResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.group_attribute):
            body['groupAttribute'] = request.group_attribute
        if not DaraCore.is_null(request.group_name):
            body['groupName'] = request.group_name
        if not DaraCore.is_null(request.group_type):
            body['groupType'] = request.group_type
        if not DaraCore.is_null(request.machine_identify_type):
            body['machineIdentifyType'] = request.machine_identify_type
        if not DaraCore.is_null(request.machine_list):
            body['machineList'] = request.machine_list
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMachineGroup',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/machinegroups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateMachineGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_machine_group(
        self,
        project: str,
        request: main_models.CreateMachineGroupRequest,
    ) -> main_models.CreateMachineGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_machine_group_with_options(project, request, headers, runtime)

    async def create_machine_group_async(
        self,
        project: str,
        request: main_models.CreateMachineGroupRequest,
    ) -> main_models.CreateMachineGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_machine_group_with_options_async(project, request, headers, runtime)

    def create_materialized_view_with_options(
        self,
        project: str,
        request: main_models.CreateMaterializedViewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMaterializedViewResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.agg_interval_mins):
            body['aggIntervalMins'] = request.agg_interval_mins
        if not DaraCore.is_null(request.logstore):
            body['logstore'] = request.logstore
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.original_sql):
            body['originalSql'] = request.original_sql
        if not DaraCore.is_null(request.start_time):
            body['startTime'] = request.start_time
        if not DaraCore.is_null(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMaterializedView',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/materializedviews',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateMaterializedViewResponse(),
            self.execute(params, req, runtime)
        )

    async def create_materialized_view_with_options_async(
        self,
        project: str,
        request: main_models.CreateMaterializedViewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMaterializedViewResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.agg_interval_mins):
            body['aggIntervalMins'] = request.agg_interval_mins
        if not DaraCore.is_null(request.logstore):
            body['logstore'] = request.logstore
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.original_sql):
            body['originalSql'] = request.original_sql
        if not DaraCore.is_null(request.start_time):
            body['startTime'] = request.start_time
        if not DaraCore.is_null(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMaterializedView',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/materializedviews',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateMaterializedViewResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_materialized_view(
        self,
        project: str,
        request: main_models.CreateMaterializedViewRequest,
    ) -> main_models.CreateMaterializedViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_materialized_view_with_options(project, request, headers, runtime)

    async def create_materialized_view_async(
        self,
        project: str,
        request: main_models.CreateMaterializedViewRequest,
    ) -> main_models.CreateMaterializedViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_materialized_view_with_options_async(project, request, headers, runtime)

    def create_max_compute_export_with_options(
        self,
        project: str,
        request: main_models.CreateMaxComputeExportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMaxComputeExportResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMaxComputeExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/maxcomputeexports',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateMaxComputeExportResponse(),
            self.execute(params, req, runtime)
        )

    async def create_max_compute_export_with_options_async(
        self,
        project: str,
        request: main_models.CreateMaxComputeExportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMaxComputeExportResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMaxComputeExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/maxcomputeexports',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateMaxComputeExportResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_max_compute_export(
        self,
        project: str,
        request: main_models.CreateMaxComputeExportRequest,
    ) -> main_models.CreateMaxComputeExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_max_compute_export_with_options(project, request, headers, runtime)

    async def create_max_compute_export_async(
        self,
        project: str,
        request: main_models.CreateMaxComputeExportRequest,
    ) -> main_models.CreateMaxComputeExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_max_compute_export_with_options_async(project, request, headers, runtime)

    def create_metric_store_with_options(
        self,
        project: str,
        request: main_models.CreateMetricStoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMetricStoreResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.append_meta):
            body['appendMeta'] = request.append_meta
        if not DaraCore.is_null(request.auto_split):
            body['autoSplit'] = request.auto_split
        if not DaraCore.is_null(request.hot_ttl):
            body['hot_ttl'] = request.hot_ttl
        if not DaraCore.is_null(request.infrequent_access_ttl):
            body['infrequentAccessTTL'] = request.infrequent_access_ttl
        if not DaraCore.is_null(request.max_split_shard):
            body['maxSplitShard'] = request.max_split_shard
        if not DaraCore.is_null(request.metric_type):
            body['metricType'] = request.metric_type
        if not DaraCore.is_null(request.mode):
            body['mode'] = request.mode
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.shard_count):
            body['shardCount'] = request.shard_count
        if not DaraCore.is_null(request.sharding_policy):
            body['shardingPolicy'] = request.sharding_policy
        if not DaraCore.is_null(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMetricStore',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/metricstores',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateMetricStoreResponse(),
            self.execute(params, req, runtime)
        )

    async def create_metric_store_with_options_async(
        self,
        project: str,
        request: main_models.CreateMetricStoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMetricStoreResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.append_meta):
            body['appendMeta'] = request.append_meta
        if not DaraCore.is_null(request.auto_split):
            body['autoSplit'] = request.auto_split
        if not DaraCore.is_null(request.hot_ttl):
            body['hot_ttl'] = request.hot_ttl
        if not DaraCore.is_null(request.infrequent_access_ttl):
            body['infrequentAccessTTL'] = request.infrequent_access_ttl
        if not DaraCore.is_null(request.max_split_shard):
            body['maxSplitShard'] = request.max_split_shard
        if not DaraCore.is_null(request.metric_type):
            body['metricType'] = request.metric_type
        if not DaraCore.is_null(request.mode):
            body['mode'] = request.mode
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.shard_count):
            body['shardCount'] = request.shard_count
        if not DaraCore.is_null(request.sharding_policy):
            body['shardingPolicy'] = request.sharding_policy
        if not DaraCore.is_null(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMetricStore',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/metricstores',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateMetricStoreResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_metric_store(
        self,
        project: str,
        request: main_models.CreateMetricStoreRequest,
    ) -> main_models.CreateMetricStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_metric_store_with_options(project, request, headers, runtime)

    async def create_metric_store_async(
        self,
        project: str,
        request: main_models.CreateMetricStoreRequest,
    ) -> main_models.CreateMetricStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_metric_store_with_options_async(project, request, headers, runtime)

    def create_ossexport_with_options(
        self,
        project: str,
        request: main_models.CreateOSSExportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateOSSExportResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOSSExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ossexports',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateOSSExportResponse(),
            self.execute(params, req, runtime)
        )

    async def create_ossexport_with_options_async(
        self,
        project: str,
        request: main_models.CreateOSSExportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateOSSExportResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOSSExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ossexports',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateOSSExportResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_ossexport(
        self,
        project: str,
        request: main_models.CreateOSSExportRequest,
    ) -> main_models.CreateOSSExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_ossexport_with_options(project, request, headers, runtime)

    async def create_ossexport_async(
        self,
        project: str,
        request: main_models.CreateOSSExportRequest,
    ) -> main_models.CreateOSSExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_ossexport_with_options_async(project, request, headers, runtime)

    def create_osshdfsexport_with_options(
        self,
        project: str,
        request: main_models.CreateOSSHDFSExportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateOSSHDFSExportResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOSSHDFSExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/osshdfsexports',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateOSSHDFSExportResponse(),
            self.execute(params, req, runtime)
        )

    async def create_osshdfsexport_with_options_async(
        self,
        project: str,
        request: main_models.CreateOSSHDFSExportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateOSSHDFSExportResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOSSHDFSExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/osshdfsexports',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateOSSHDFSExportResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_osshdfsexport(
        self,
        project: str,
        request: main_models.CreateOSSHDFSExportRequest,
    ) -> main_models.CreateOSSHDFSExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_osshdfsexport_with_options(project, request, headers, runtime)

    async def create_osshdfsexport_async(
        self,
        project: str,
        request: main_models.CreateOSSHDFSExportRequest,
    ) -> main_models.CreateOSSHDFSExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_osshdfsexport_with_options_async(project, request, headers, runtime)

    def create_ossingestion_with_options(
        self,
        project: str,
        request: main_models.CreateOSSIngestionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateOSSIngestionResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.schedule):
            body['schedule'] = request.schedule
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOSSIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ossingestions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateOSSIngestionResponse(),
            self.execute(params, req, runtime)
        )

    async def create_ossingestion_with_options_async(
        self,
        project: str,
        request: main_models.CreateOSSIngestionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateOSSIngestionResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.schedule):
            body['schedule'] = request.schedule
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOSSIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ossingestions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateOSSIngestionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_ossingestion(
        self,
        project: str,
        request: main_models.CreateOSSIngestionRequest,
    ) -> main_models.CreateOSSIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_ossingestion_with_options(project, request, headers, runtime)

    async def create_ossingestion_async(
        self,
        project: str,
        request: main_models.CreateOSSIngestionRequest,
    ) -> main_models.CreateOSSIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_ossingestion_with_options_async(project, request, headers, runtime)

    def create_project_with_options(
        self,
        request: main_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_redundancy_type):
            body['dataRedundancyType'] = request.data_redundancy_type
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.project_name):
            body['projectName'] = request.project_name
        if not DaraCore.is_null(request.recycle_bin_enabled):
            body['recycleBinEnabled'] = request.recycle_bin_enabled
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProject',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateProjectResponse(),
            self.execute(params, req, runtime)
        )

    async def create_project_with_options_async(
        self,
        request: main_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_redundancy_type):
            body['dataRedundancyType'] = request.data_redundancy_type
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.project_name):
            body['projectName'] = request.project_name
        if not DaraCore.is_null(request.recycle_bin_enabled):
            body['recycleBinEnabled'] = request.recycle_bin_enabled
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProject',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateProjectResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_project(
        self,
        request: main_models.CreateProjectRequest,
    ) -> main_models.CreateProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_project_with_options(request, headers, runtime)

    async def create_project_async(
        self,
        request: main_models.CreateProjectRequest,
    ) -> main_models.CreateProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_project_with_options_async(request, headers, runtime)

    def create_s3ingestion_with_options(
        self,
        project: str,
        request: main_models.CreateS3IngestionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateS3IngestionResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.schedule):
            body['schedule'] = request.schedule
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateS3Ingestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/s3ingestions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateS3IngestionResponse(),
            self.execute(params, req, runtime)
        )

    async def create_s3ingestion_with_options_async(
        self,
        project: str,
        request: main_models.CreateS3IngestionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateS3IngestionResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.schedule):
            body['schedule'] = request.schedule
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateS3Ingestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/s3ingestions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateS3IngestionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_s3ingestion(
        self,
        project: str,
        request: main_models.CreateS3IngestionRequest,
    ) -> main_models.CreateS3IngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_s3ingestion_with_options(project, request, headers, runtime)

    async def create_s3ingestion_async(
        self,
        project: str,
        request: main_models.CreateS3IngestionRequest,
    ) -> main_models.CreateS3IngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_s3ingestion_with_options_async(project, request, headers, runtime)

    def create_saved_search_with_options(
        self,
        project: str,
        request: main_models.CreateSavedSearchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSavedSearchResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.logstore):
            body['logstore'] = request.logstore
        if not DaraCore.is_null(request.savedsearch_name):
            body['savedsearchName'] = request.savedsearch_name
        if not DaraCore.is_null(request.search_query):
            body['searchQuery'] = request.search_query
        if not DaraCore.is_null(request.topic):
            body['topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSavedSearch',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/savedsearches',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateSavedSearchResponse(),
            self.execute(params, req, runtime)
        )

    async def create_saved_search_with_options_async(
        self,
        project: str,
        request: main_models.CreateSavedSearchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSavedSearchResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.logstore):
            body['logstore'] = request.logstore
        if not DaraCore.is_null(request.savedsearch_name):
            body['savedsearchName'] = request.savedsearch_name
        if not DaraCore.is_null(request.search_query):
            body['searchQuery'] = request.search_query
        if not DaraCore.is_null(request.topic):
            body['topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSavedSearch',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/savedsearches',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateSavedSearchResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_saved_search(
        self,
        project: str,
        request: main_models.CreateSavedSearchRequest,
    ) -> main_models.CreateSavedSearchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_saved_search_with_options(project, request, headers, runtime)

    async def create_saved_search_async(
        self,
        project: str,
        request: main_models.CreateSavedSearchRequest,
    ) -> main_models.CreateSavedSearchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_saved_search_with_options_async(project, request, headers, runtime)

    def create_scheduled_sqlwith_options(
        self,
        project: str,
        request: main_models.CreateScheduledSQLRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateScheduledSQLResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.schedule):
            body['schedule'] = request.schedule
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateScheduledSQL',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/scheduledsqls',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateScheduledSQLResponse(),
            self.execute(params, req, runtime)
        )

    async def create_scheduled_sqlwith_options_async(
        self,
        project: str,
        request: main_models.CreateScheduledSQLRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateScheduledSQLResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.schedule):
            body['schedule'] = request.schedule
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateScheduledSQL',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/scheduledsqls',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateScheduledSQLResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_scheduled_sql(
        self,
        project: str,
        request: main_models.CreateScheduledSQLRequest,
    ) -> main_models.CreateScheduledSQLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_scheduled_sqlwith_options(project, request, headers, runtime)

    async def create_scheduled_sql_async(
        self,
        project: str,
        request: main_models.CreateScheduledSQLRequest,
    ) -> main_models.CreateScheduledSQLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_scheduled_sqlwith_options_async(project, request, headers, runtime)

    def create_sql_instance_with_options(
        self,
        project: str,
        request: main_models.CreateSqlInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSqlInstanceResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.cu):
            body['cu'] = request.cu
        if not DaraCore.is_null(request.use_as_default):
            body['useAsDefault'] = request.use_as_default
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSqlInstance',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/sqlinstance',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateSqlInstanceResponse(),
            self.execute(params, req, runtime)
        )

    async def create_sql_instance_with_options_async(
        self,
        project: str,
        request: main_models.CreateSqlInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSqlInstanceResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.cu):
            body['cu'] = request.cu
        if not DaraCore.is_null(request.use_as_default):
            body['useAsDefault'] = request.use_as_default
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSqlInstance',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/sqlinstance',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateSqlInstanceResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_sql_instance(
        self,
        project: str,
        request: main_models.CreateSqlInstanceRequest,
    ) -> main_models.CreateSqlInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_sql_instance_with_options(project, request, headers, runtime)

    async def create_sql_instance_async(
        self,
        project: str,
        request: main_models.CreateSqlInstanceRequest,
    ) -> main_models.CreateSqlInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_sql_instance_with_options_async(project, request, headers, runtime)

    def create_store_view_with_options(
        self,
        project: str,
        request: main_models.CreateStoreViewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateStoreViewResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.store_type):
            body['storeType'] = request.store_type
        if not DaraCore.is_null(request.stores):
            body['stores'] = request.stores
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateStoreView',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/storeviews',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateStoreViewResponse(),
            self.execute(params, req, runtime)
        )

    async def create_store_view_with_options_async(
        self,
        project: str,
        request: main_models.CreateStoreViewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateStoreViewResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.store_type):
            body['storeType'] = request.store_type
        if not DaraCore.is_null(request.stores):
            body['stores'] = request.stores
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateStoreView',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/storeviews',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateStoreViewResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_store_view(
        self,
        project: str,
        request: main_models.CreateStoreViewRequest,
    ) -> main_models.CreateStoreViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_store_view_with_options(project, request, headers, runtime)

    async def create_store_view_async(
        self,
        project: str,
        request: main_models.CreateStoreViewRequest,
    ) -> main_models.CreateStoreViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_store_view_with_options_async(project, request, headers, runtime)

    def create_ticket_with_options(
        self,
        request: main_models.CreateTicketRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_token_expiration_time):
            query['accessTokenExpirationTime'] = request.access_token_expiration_time
        if not DaraCore.is_null(request.expiration_time):
            query['expirationTime'] = request.expiration_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTicket',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/tickets',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTicketResponse(),
            self.execute(params, req, runtime)
        )

    async def create_ticket_with_options_async(
        self,
        request: main_models.CreateTicketRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_token_expiration_time):
            query['accessTokenExpirationTime'] = request.access_token_expiration_time
        if not DaraCore.is_null(request.expiration_time):
            query['expirationTime'] = request.expiration_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTicket',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/tickets',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTicketResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_ticket(
        self,
        request: main_models.CreateTicketRequest,
    ) -> main_models.CreateTicketResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_ticket_with_options(request, headers, runtime)

    async def create_ticket_async(
        self,
        request: main_models.CreateTicketRequest,
    ) -> main_models.CreateTicketResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_ticket_with_options_async(request, headers, runtime)

    def delete_agent_instance_config_with_options(
        self,
        config_type: str,
        tmp_req: main_models.DeleteAgentInstanceConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentInstanceConfigResponse:
        tmp_req.validate()
        request = main_models.DeleteAgentInstanceConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.attributes):
            request.attributes_shrink = Utils.array_to_string_with_specified_style(tmp_req.attributes, 'attributes', 'json')
        query = {}
        if not DaraCore.is_null(request.attributes_shrink):
            query['attributes'] = request.attributes_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgentInstanceConfig',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/agentinstanceconfigs/{config_type}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentInstanceConfigResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_agent_instance_config_with_options_async(
        self,
        config_type: str,
        tmp_req: main_models.DeleteAgentInstanceConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentInstanceConfigResponse:
        tmp_req.validate()
        request = main_models.DeleteAgentInstanceConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.attributes):
            request.attributes_shrink = Utils.array_to_string_with_specified_style(tmp_req.attributes, 'attributes', 'json')
        query = {}
        if not DaraCore.is_null(request.attributes_shrink):
            query['attributes'] = request.attributes_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgentInstanceConfig',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/agentinstanceconfigs/{config_type}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentInstanceConfigResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_agent_instance_config(
        self,
        config_type: str,
        request: main_models.DeleteAgentInstanceConfigRequest,
    ) -> main_models.DeleteAgentInstanceConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_agent_instance_config_with_options(config_type, request, headers, runtime)

    async def delete_agent_instance_config_async(
        self,
        config_type: str,
        request: main_models.DeleteAgentInstanceConfigRequest,
    ) -> main_models.DeleteAgentInstanceConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_agent_instance_config_with_options_async(config_type, request, headers, runtime)

    def delete_alert_with_options(
        self,
        project: str,
        alert_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlertResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlert',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/alerts/{alert_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteAlertResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_alert_with_options_async(
        self,
        project: str,
        alert_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlertResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlert',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/alerts/{alert_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteAlertResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_alert(
        self,
        project: str,
        alert_name: str,
    ) -> main_models.DeleteAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_alert_with_options(project, alert_name, headers, runtime)

    async def delete_alert_async(
        self,
        project: str,
        alert_name: str,
    ) -> main_models.DeleteAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_alert_with_options_async(project, alert_name, headers, runtime)

    def delete_annotation_data_with_options(
        self,
        dataset_id: str,
        annotationdata_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAnnotationDataResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAnnotationData',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/annotationdataset/{dataset_id}/annotationdata/{annotationdata_id}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteAnnotationDataResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_annotation_data_with_options_async(
        self,
        dataset_id: str,
        annotationdata_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAnnotationDataResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAnnotationData',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/annotationdataset/{dataset_id}/annotationdata/{annotationdata_id}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteAnnotationDataResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_annotation_data(
        self,
        dataset_id: str,
        annotationdata_id: str,
    ) -> main_models.DeleteAnnotationDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_annotation_data_with_options(dataset_id, annotationdata_id, headers, runtime)

    async def delete_annotation_data_async(
        self,
        dataset_id: str,
        annotationdata_id: str,
    ) -> main_models.DeleteAnnotationDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_annotation_data_with_options_async(dataset_id, annotationdata_id, headers, runtime)

    def delete_annotation_data_set_with_options(
        self,
        dataset_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAnnotationDataSetResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAnnotationDataSet',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/annotationdataset/{dataset_id}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteAnnotationDataSetResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_annotation_data_set_with_options_async(
        self,
        dataset_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAnnotationDataSetResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAnnotationDataSet',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/annotationdataset/{dataset_id}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteAnnotationDataSetResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_annotation_data_set(
        self,
        dataset_id: str,
    ) -> main_models.DeleteAnnotationDataSetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_annotation_data_set_with_options(dataset_id, headers, runtime)

    async def delete_annotation_data_set_async(
        self,
        dataset_id: str,
    ) -> main_models.DeleteAnnotationDataSetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_annotation_data_set_with_options_async(dataset_id, headers, runtime)

    def delete_annotation_label_with_options(
        self,
        label_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAnnotationLabelResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAnnotationLabel',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/annotationlabel/{label_id}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteAnnotationLabelResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_annotation_label_with_options_async(
        self,
        label_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAnnotationLabelResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAnnotationLabel',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/annotationlabel/{label_id}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteAnnotationLabelResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_annotation_label(
        self,
        label_id: str,
    ) -> main_models.DeleteAnnotationLabelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_annotation_label_with_options(label_id, headers, runtime)

    async def delete_annotation_label_async(
        self,
        label_id: str,
    ) -> main_models.DeleteAnnotationLabelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_annotation_label_with_options_async(label_id, headers, runtime)

    def delete_azure_blob_ingestion_with_options(
        self,
        project: str,
        azure_blob_ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAzureBlobIngestionResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAzureBlobIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/azureblobingestions/{azure_blob_ingestion_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteAzureBlobIngestionResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_azure_blob_ingestion_with_options_async(
        self,
        project: str,
        azure_blob_ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAzureBlobIngestionResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAzureBlobIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/azureblobingestions/{azure_blob_ingestion_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteAzureBlobIngestionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_azure_blob_ingestion(
        self,
        project: str,
        azure_blob_ingestion_name: str,
    ) -> main_models.DeleteAzureBlobIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_azure_blob_ingestion_with_options(project, azure_blob_ingestion_name, headers, runtime)

    async def delete_azure_blob_ingestion_async(
        self,
        project: str,
        azure_blob_ingestion_name: str,
    ) -> main_models.DeleteAzureBlobIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_azure_blob_ingestion_with_options_async(project, azure_blob_ingestion_name, headers, runtime)

    def delete_collection_policy_with_options(
        self,
        policy_name: str,
        request: main_models.DeleteCollectionPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCollectionPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_code):
            query['dataCode'] = request.data_code
        if not DaraCore.is_null(request.product_code):
            query['productCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCollectionPolicy',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/collectionpolicy/{policy_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteCollectionPolicyResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_collection_policy_with_options_async(
        self,
        policy_name: str,
        request: main_models.DeleteCollectionPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCollectionPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_code):
            query['dataCode'] = request.data_code
        if not DaraCore.is_null(request.product_code):
            query['productCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCollectionPolicy',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/collectionpolicy/{policy_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteCollectionPolicyResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_collection_policy(
        self,
        policy_name: str,
        request: main_models.DeleteCollectionPolicyRequest,
    ) -> main_models.DeleteCollectionPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_collection_policy_with_options(policy_name, request, headers, runtime)

    async def delete_collection_policy_async(
        self,
        policy_name: str,
        request: main_models.DeleteCollectionPolicyRequest,
    ) -> main_models.DeleteCollectionPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_collection_policy_with_options_async(policy_name, request, headers, runtime)

    def delete_config_with_options(
        self,
        project: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConfigResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteConfig',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/configs/{config_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteConfigResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_config_with_options_async(
        self,
        project: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConfigResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteConfig',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/configs/{config_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteConfigResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_config(
        self,
        project: str,
        config_name: str,
    ) -> main_models.DeleteConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_config_with_options(project, config_name, headers, runtime)

    async def delete_config_async(
        self,
        project: str,
        config_name: str,
    ) -> main_models.DeleteConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_config_with_options_async(project, config_name, headers, runtime)

    def delete_consume_processor_with_options(
        self,
        project: str,
        processor_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConsumeProcessorResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteConsumeProcessor',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/consumeprocessors/{processor_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteConsumeProcessorResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_consume_processor_with_options_async(
        self,
        project: str,
        processor_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConsumeProcessorResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteConsumeProcessor',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/consumeprocessors/{processor_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteConsumeProcessorResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_consume_processor(
        self,
        project: str,
        processor_name: str,
    ) -> main_models.DeleteConsumeProcessorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_consume_processor_with_options(project, processor_name, headers, runtime)

    async def delete_consume_processor_async(
        self,
        project: str,
        processor_name: str,
    ) -> main_models.DeleteConsumeProcessorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_consume_processor_with_options_async(project, processor_name, headers, runtime)

    def delete_consumer_group_with_options(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConsumerGroupResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteConsumerGroup',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/consumergroups/{consumer_group}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteConsumerGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_consumer_group_with_options_async(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConsumerGroupResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteConsumerGroup',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/consumergroups/{consumer_group}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteConsumerGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_consumer_group(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
    ) -> main_models.DeleteConsumerGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_consumer_group_with_options(project, logstore, consumer_group, headers, runtime)

    async def delete_consumer_group_async(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
    ) -> main_models.DeleteConsumerGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_consumer_group_with_options_async(project, logstore, consumer_group, headers, runtime)

    def delete_dashboard_with_options(
        self,
        project: str,
        dashboard_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDashboardResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDashboard',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/dashboards/{dashboard_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteDashboardResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_dashboard_with_options_async(
        self,
        project: str,
        dashboard_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDashboardResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDashboard',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/dashboards/{dashboard_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteDashboardResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_dashboard(
        self,
        project: str,
        dashboard_name: str,
    ) -> main_models.DeleteDashboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_dashboard_with_options(project, dashboard_name, headers, runtime)

    async def delete_dashboard_async(
        self,
        project: str,
        dashboard_name: str,
    ) -> main_models.DeleteDashboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_dashboard_with_options_async(project, dashboard_name, headers, runtime)

    def delete_domain_with_options(
        self,
        project: str,
        domain_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomain',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/domains/{domain_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        project: str,
        domain_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomain',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/domains/{domain_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_domain(
        self,
        project: str,
        domain_name: str,
    ) -> main_models.DeleteDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_domain_with_options(project, domain_name, headers, runtime)

    async def delete_domain_async(
        self,
        project: str,
        domain_name: str,
    ) -> main_models.DeleteDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_domain_with_options_async(project, domain_name, headers, runtime)

    def delete_download_job_with_options(
        self,
        project: str,
        download_job_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDownloadJobResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDownloadJob',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/downloadjobs/{download_job_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteDownloadJobResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_download_job_with_options_async(
        self,
        project: str,
        download_job_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDownloadJobResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDownloadJob',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/downloadjobs/{download_job_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteDownloadJobResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_download_job(
        self,
        project: str,
        download_job_name: str,
    ) -> main_models.DeleteDownloadJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_download_job_with_options(project, download_job_name, headers, runtime)

    async def delete_download_job_async(
        self,
        project: str,
        download_job_name: str,
    ) -> main_models.DeleteDownloadJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_download_job_with_options_async(project, download_job_name, headers, runtime)

    def delete_etlwith_options(
        self,
        project: str,
        etl_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteETLResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteETL',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/etls/{etl_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteETLResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_etlwith_options_async(
        self,
        project: str,
        etl_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteETLResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteETL',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/etls/{etl_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteETLResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_etl(
        self,
        project: str,
        etl_name: str,
    ) -> main_models.DeleteETLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_etlwith_options(project, etl_name, headers, runtime)

    async def delete_etl_async(
        self,
        project: str,
        etl_name: str,
    ) -> main_models.DeleteETLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_etlwith_options_async(project, etl_name, headers, runtime)

    def delete_elasticsearch_ingestion_with_options(
        self,
        project: str,
        es_ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteElasticsearchIngestionResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteElasticsearchIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/elasticsearchingestions/{es_ingestion_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteElasticsearchIngestionResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_elasticsearch_ingestion_with_options_async(
        self,
        project: str,
        es_ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteElasticsearchIngestionResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteElasticsearchIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/elasticsearchingestions/{es_ingestion_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteElasticsearchIngestionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_elasticsearch_ingestion(
        self,
        project: str,
        es_ingestion_name: str,
    ) -> main_models.DeleteElasticsearchIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_elasticsearch_ingestion_with_options(project, es_ingestion_name, headers, runtime)

    async def delete_elasticsearch_ingestion_async(
        self,
        project: str,
        es_ingestion_name: str,
    ) -> main_models.DeleteElasticsearchIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_elasticsearch_ingestion_with_options_async(project, es_ingestion_name, headers, runtime)

    def delete_index_with_options(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIndexResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteIndex',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/index',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteIndexResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_index_with_options_async(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIndexResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteIndex',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/index',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteIndexResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_index(
        self,
        project: str,
        logstore: str,
    ) -> main_models.DeleteIndexResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_index_with_options(project, logstore, headers, runtime)

    async def delete_index_async(
        self,
        project: str,
        logstore: str,
    ) -> main_models.DeleteIndexResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_index_with_options_async(project, logstore, headers, runtime)

    def delete_ingest_processor_with_options(
        self,
        project: str,
        processor_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIngestProcessorResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteIngestProcessor',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ingestprocessors/{processor_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteIngestProcessorResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_ingest_processor_with_options_async(
        self,
        project: str,
        processor_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIngestProcessorResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteIngestProcessor',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ingestprocessors/{processor_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteIngestProcessorResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_ingest_processor(
        self,
        project: str,
        processor_name: str,
    ) -> main_models.DeleteIngestProcessorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_ingest_processor_with_options(project, processor_name, headers, runtime)

    async def delete_ingest_processor_async(
        self,
        project: str,
        processor_name: str,
    ) -> main_models.DeleteIngestProcessorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_ingest_processor_with_options_async(project, processor_name, headers, runtime)

    def delete_log_store_with_options(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLogStoreResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteLogStore',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteLogStoreResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_log_store_with_options_async(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLogStoreResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteLogStore',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteLogStoreResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_log_store(
        self,
        project: str,
        logstore: str,
    ) -> main_models.DeleteLogStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_log_store_with_options(project, logstore, headers, runtime)

    async def delete_log_store_async(
        self,
        project: str,
        logstore: str,
    ) -> main_models.DeleteLogStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_log_store_with_options_async(project, logstore, headers, runtime)

    def delete_logging_with_options(
        self,
        project: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLoggingResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteLogging',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logging',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteLoggingResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_logging_with_options_async(
        self,
        project: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLoggingResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteLogging',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logging',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteLoggingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_logging(
        self,
        project: str,
    ) -> main_models.DeleteLoggingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_logging_with_options(project, headers, runtime)

    async def delete_logging_async(
        self,
        project: str,
    ) -> main_models.DeleteLoggingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_logging_with_options_async(project, headers, runtime)

    def delete_logtail_pipeline_config_with_options(
        self,
        project: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLogtailPipelineConfigResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteLogtailPipelineConfig',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/pipelineconfigs/{config_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteLogtailPipelineConfigResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_logtail_pipeline_config_with_options_async(
        self,
        project: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLogtailPipelineConfigResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteLogtailPipelineConfig',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/pipelineconfigs/{config_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteLogtailPipelineConfigResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_logtail_pipeline_config(
        self,
        project: str,
        config_name: str,
    ) -> main_models.DeleteLogtailPipelineConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_logtail_pipeline_config_with_options(project, config_name, headers, runtime)

    async def delete_logtail_pipeline_config_async(
        self,
        project: str,
        config_name: str,
    ) -> main_models.DeleteLogtailPipelineConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_logtail_pipeline_config_with_options_async(project, config_name, headers, runtime)

    def delete_machine_group_with_options(
        self,
        project: str,
        machine_group: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMachineGroupResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMachineGroup',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/machinegroups/{machine_group}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteMachineGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_machine_group_with_options_async(
        self,
        project: str,
        machine_group: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMachineGroupResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMachineGroup',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/machinegroups/{machine_group}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteMachineGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_machine_group(
        self,
        project: str,
        machine_group: str,
    ) -> main_models.DeleteMachineGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_machine_group_with_options(project, machine_group, headers, runtime)

    async def delete_machine_group_async(
        self,
        project: str,
        machine_group: str,
    ) -> main_models.DeleteMachineGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_machine_group_with_options_async(project, machine_group, headers, runtime)

    def delete_materialized_view_with_options(
        self,
        project: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMaterializedViewResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMaterializedView',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/materializedviews/{name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteMaterializedViewResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_materialized_view_with_options_async(
        self,
        project: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMaterializedViewResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMaterializedView',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/materializedviews/{name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteMaterializedViewResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_materialized_view(
        self,
        project: str,
        name: str,
    ) -> main_models.DeleteMaterializedViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_materialized_view_with_options(project, name, headers, runtime)

    async def delete_materialized_view_async(
        self,
        project: str,
        name: str,
    ) -> main_models.DeleteMaterializedViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_materialized_view_with_options_async(project, name, headers, runtime)

    def delete_max_compute_export_with_options(
        self,
        project: str,
        mc_export_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMaxComputeExportResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMaxComputeExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/maxcomputeexports/{mc_export_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteMaxComputeExportResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_max_compute_export_with_options_async(
        self,
        project: str,
        mc_export_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMaxComputeExportResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMaxComputeExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/maxcomputeexports/{mc_export_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteMaxComputeExportResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_max_compute_export(
        self,
        project: str,
        mc_export_name: str,
    ) -> main_models.DeleteMaxComputeExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_max_compute_export_with_options(project, mc_export_name, headers, runtime)

    async def delete_max_compute_export_async(
        self,
        project: str,
        mc_export_name: str,
    ) -> main_models.DeleteMaxComputeExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_max_compute_export_with_options_async(project, mc_export_name, headers, runtime)

    def delete_metric_store_with_options(
        self,
        project: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMetricStoreResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMetricStore',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/metricstores/{name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'none',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteMetricStoreResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_metric_store_with_options_async(
        self,
        project: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMetricStoreResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMetricStore',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/metricstores/{name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'none',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteMetricStoreResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_metric_store(
        self,
        project: str,
        name: str,
    ) -> main_models.DeleteMetricStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_metric_store_with_options(project, name, headers, runtime)

    async def delete_metric_store_async(
        self,
        project: str,
        name: str,
    ) -> main_models.DeleteMetricStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_metric_store_with_options_async(project, name, headers, runtime)

    def delete_ossexport_with_options(
        self,
        project: str,
        oss_export_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOSSExportResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteOSSExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ossexports/{oss_export_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteOSSExportResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_ossexport_with_options_async(
        self,
        project: str,
        oss_export_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOSSExportResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteOSSExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ossexports/{oss_export_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteOSSExportResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_ossexport(
        self,
        project: str,
        oss_export_name: str,
    ) -> main_models.DeleteOSSExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_ossexport_with_options(project, oss_export_name, headers, runtime)

    async def delete_ossexport_async(
        self,
        project: str,
        oss_export_name: str,
    ) -> main_models.DeleteOSSExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_ossexport_with_options_async(project, oss_export_name, headers, runtime)

    def delete_osshdfsexport_with_options(
        self,
        project: str,
        oss_export_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOSSHDFSExportResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteOSSHDFSExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/osshdfsexports/{oss_export_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteOSSHDFSExportResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_osshdfsexport_with_options_async(
        self,
        project: str,
        oss_export_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOSSHDFSExportResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteOSSHDFSExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/osshdfsexports/{oss_export_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteOSSHDFSExportResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_osshdfsexport(
        self,
        project: str,
        oss_export_name: str,
    ) -> main_models.DeleteOSSHDFSExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_osshdfsexport_with_options(project, oss_export_name, headers, runtime)

    async def delete_osshdfsexport_async(
        self,
        project: str,
        oss_export_name: str,
    ) -> main_models.DeleteOSSHDFSExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_osshdfsexport_with_options_async(project, oss_export_name, headers, runtime)

    def delete_ossingestion_with_options(
        self,
        project: str,
        oss_ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOSSIngestionResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteOSSIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ossingestions/{oss_ingestion_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteOSSIngestionResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_ossingestion_with_options_async(
        self,
        project: str,
        oss_ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOSSIngestionResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteOSSIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ossingestions/{oss_ingestion_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteOSSIngestionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_ossingestion(
        self,
        project: str,
        oss_ingestion_name: str,
    ) -> main_models.DeleteOSSIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_ossingestion_with_options(project, oss_ingestion_name, headers, runtime)

    async def delete_ossingestion_async(
        self,
        project: str,
        oss_ingestion_name: str,
    ) -> main_models.DeleteOSSIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_ossingestion_with_options_async(project, oss_ingestion_name, headers, runtime)

    def delete_project_with_options(
        self,
        project: str,
        request: main_models.DeleteProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProjectResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.force_delete):
            query['forceDelete'] = request.force_delete
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProject',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteProjectResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        project: str,
        request: main_models.DeleteProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProjectResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.force_delete):
            query['forceDelete'] = request.force_delete
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProject',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteProjectResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_project(
        self,
        project: str,
        request: main_models.DeleteProjectRequest,
    ) -> main_models.DeleteProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_project_with_options(project, request, headers, runtime)

    async def delete_project_async(
        self,
        project: str,
        request: main_models.DeleteProjectRequest,
    ) -> main_models.DeleteProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_project_with_options_async(project, request, headers, runtime)

    def delete_project_policy_with_options(
        self,
        project: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProjectPolicyResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteProjectPolicy',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/policy',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteProjectPolicyResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_project_policy_with_options_async(
        self,
        project: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProjectPolicyResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteProjectPolicy',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/policy',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteProjectPolicyResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_project_policy(
        self,
        project: str,
    ) -> main_models.DeleteProjectPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_project_policy_with_options(project, headers, runtime)

    async def delete_project_policy_async(
        self,
        project: str,
    ) -> main_models.DeleteProjectPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_project_policy_with_options_async(project, headers, runtime)

    def delete_s3ingestion_with_options(
        self,
        project: str,
        s_3ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteS3IngestionResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteS3Ingestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/s3ingestions/{s_3ingestion_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteS3IngestionResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_s3ingestion_with_options_async(
        self,
        project: str,
        s_3ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteS3IngestionResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteS3Ingestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/s3ingestions/{s_3ingestion_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteS3IngestionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_s3ingestion(
        self,
        project: str,
        s_3ingestion_name: str,
    ) -> main_models.DeleteS3IngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_s3ingestion_with_options(project, s_3ingestion_name, headers, runtime)

    async def delete_s3ingestion_async(
        self,
        project: str,
        s_3ingestion_name: str,
    ) -> main_models.DeleteS3IngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_s3ingestion_with_options_async(project, s_3ingestion_name, headers, runtime)

    def delete_saved_search_with_options(
        self,
        project: str,
        savedsearch_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSavedSearchResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteSavedSearch',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/savedsearches/{savedsearch_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteSavedSearchResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_saved_search_with_options_async(
        self,
        project: str,
        savedsearch_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSavedSearchResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteSavedSearch',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/savedsearches/{savedsearch_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteSavedSearchResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_saved_search(
        self,
        project: str,
        savedsearch_name: str,
    ) -> main_models.DeleteSavedSearchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_saved_search_with_options(project, savedsearch_name, headers, runtime)

    async def delete_saved_search_async(
        self,
        project: str,
        savedsearch_name: str,
    ) -> main_models.DeleteSavedSearchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_saved_search_with_options_async(project, savedsearch_name, headers, runtime)

    def delete_scheduled_sqlwith_options(
        self,
        project: str,
        scheduled_sqlname: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScheduledSQLResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteScheduledSQL',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/scheduledsqls/{scheduled_sqlname}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteScheduledSQLResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_scheduled_sqlwith_options_async(
        self,
        project: str,
        scheduled_sqlname: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScheduledSQLResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteScheduledSQL',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/scheduledsqls/{scheduled_sqlname}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteScheduledSQLResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_scheduled_sql(
        self,
        project: str,
        scheduled_sqlname: str,
    ) -> main_models.DeleteScheduledSQLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_scheduled_sqlwith_options(project, scheduled_sqlname, headers, runtime)

    async def delete_scheduled_sql_async(
        self,
        project: str,
        scheduled_sqlname: str,
    ) -> main_models.DeleteScheduledSQLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_scheduled_sqlwith_options_async(project, scheduled_sqlname, headers, runtime)

    def delete_store_view_with_options(
        self,
        project: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStoreViewResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteStoreView',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/storeviews/{name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteStoreViewResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_store_view_with_options_async(
        self,
        project: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStoreViewResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteStoreView',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/storeviews/{name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteStoreViewResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_store_view(
        self,
        project: str,
        name: str,
    ) -> main_models.DeleteStoreViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_store_view_with_options(project, name, headers, runtime)

    async def delete_store_view_async(
        self,
        project: str,
        name: str,
    ) -> main_models.DeleteStoreViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_store_view_with_options_async(project, name, headers, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['language'] = request.language
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/regions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.execute(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: main_models.DescribeRegionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['language'] = request.language
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/regions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(request, headers, runtime)

    async def describe_regions_async(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_regions_with_options_async(request, headers, runtime)

    def disable_alert_with_options(
        self,
        project: str,
        alert_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableAlertResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DisableAlert',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/alerts/{alert_name}?action=disable',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DisableAlertResponse(),
            self.execute(params, req, runtime)
        )

    async def disable_alert_with_options_async(
        self,
        project: str,
        alert_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableAlertResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DisableAlert',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/alerts/{alert_name}?action=disable',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DisableAlertResponse(),
            await self.execute_async(params, req, runtime)
        )

    def disable_alert(
        self,
        project: str,
        alert_name: str,
    ) -> main_models.DisableAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.disable_alert_with_options(project, alert_name, headers, runtime)

    async def disable_alert_async(
        self,
        project: str,
        alert_name: str,
    ) -> main_models.DisableAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.disable_alert_with_options_async(project, alert_name, headers, runtime)

    def disable_scheduled_sqlwith_options(
        self,
        project: str,
        scheduled_sqlname: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableScheduledSQLResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DisableScheduledSQL',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/scheduledsqls/{scheduled_sqlname}?action=disable',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DisableScheduledSQLResponse(),
            self.execute(params, req, runtime)
        )

    async def disable_scheduled_sqlwith_options_async(
        self,
        project: str,
        scheduled_sqlname: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableScheduledSQLResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DisableScheduledSQL',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/scheduledsqls/{scheduled_sqlname}?action=disable',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DisableScheduledSQLResponse(),
            await self.execute_async(params, req, runtime)
        )

    def disable_scheduled_sql(
        self,
        project: str,
        scheduled_sqlname: str,
    ) -> main_models.DisableScheduledSQLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.disable_scheduled_sqlwith_options(project, scheduled_sqlname, headers, runtime)

    async def disable_scheduled_sql_async(
        self,
        project: str,
        scheduled_sqlname: str,
    ) -> main_models.DisableScheduledSQLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.disable_scheduled_sqlwith_options_async(project, scheduled_sqlname, headers, runtime)

    def enable_alert_with_options(
        self,
        project: str,
        alert_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableAlertResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'EnableAlert',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/alerts/{alert_name}?action=enable',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.EnableAlertResponse(),
            self.execute(params, req, runtime)
        )

    async def enable_alert_with_options_async(
        self,
        project: str,
        alert_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableAlertResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'EnableAlert',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/alerts/{alert_name}?action=enable',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.EnableAlertResponse(),
            await self.execute_async(params, req, runtime)
        )

    def enable_alert(
        self,
        project: str,
        alert_name: str,
    ) -> main_models.EnableAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.enable_alert_with_options(project, alert_name, headers, runtime)

    async def enable_alert_async(
        self,
        project: str,
        alert_name: str,
    ) -> main_models.EnableAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.enable_alert_with_options_async(project, alert_name, headers, runtime)

    def enable_scheduled_sqlwith_options(
        self,
        project: str,
        scheduled_sqlname: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableScheduledSQLResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'EnableScheduledSQL',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/scheduledsqls/{scheduled_sqlname}?action=enable',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.EnableScheduledSQLResponse(),
            self.execute(params, req, runtime)
        )

    async def enable_scheduled_sqlwith_options_async(
        self,
        project: str,
        scheduled_sqlname: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableScheduledSQLResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'EnableScheduledSQL',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/scheduledsqls/{scheduled_sqlname}?action=enable',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.EnableScheduledSQLResponse(),
            await self.execute_async(params, req, runtime)
        )

    def enable_scheduled_sql(
        self,
        project: str,
        scheduled_sqlname: str,
    ) -> main_models.EnableScheduledSQLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.enable_scheduled_sqlwith_options(project, scheduled_sqlname, headers, runtime)

    async def enable_scheduled_sql_async(
        self,
        project: str,
        scheduled_sqlname: str,
    ) -> main_models.EnableScheduledSQLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.enable_scheduled_sqlwith_options_async(project, scheduled_sqlname, headers, runtime)

    def get_agent_instance_config_with_options(
        self,
        config_type: str,
        tmp_req: main_models.GetAgentInstanceConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentInstanceConfigResponse:
        tmp_req.validate()
        request = main_models.GetAgentInstanceConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.attributes):
            request.attributes_shrink = Utils.array_to_string_with_specified_style(tmp_req.attributes, 'attributes', 'json')
        query = {}
        if not DaraCore.is_null(request.attributes_shrink):
            query['attributes'] = request.attributes_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentInstanceConfig',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/agentinstanceconfigs/{config_type}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentInstanceConfigResponse(),
            self.execute(params, req, runtime)
        )

    async def get_agent_instance_config_with_options_async(
        self,
        config_type: str,
        tmp_req: main_models.GetAgentInstanceConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentInstanceConfigResponse:
        tmp_req.validate()
        request = main_models.GetAgentInstanceConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.attributes):
            request.attributes_shrink = Utils.array_to_string_with_specified_style(tmp_req.attributes, 'attributes', 'json')
        query = {}
        if not DaraCore.is_null(request.attributes_shrink):
            query['attributes'] = request.attributes_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentInstanceConfig',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/agentinstanceconfigs/{config_type}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentInstanceConfigResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_agent_instance_config(
        self,
        config_type: str,
        request: main_models.GetAgentInstanceConfigRequest,
    ) -> main_models.GetAgentInstanceConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_agent_instance_config_with_options(config_type, request, headers, runtime)

    async def get_agent_instance_config_async(
        self,
        config_type: str,
        request: main_models.GetAgentInstanceConfigRequest,
    ) -> main_models.GetAgentInstanceConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_agent_instance_config_with_options_async(config_type, request, headers, runtime)

    def get_alert_with_options(
        self,
        project: str,
        alert_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAlertResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAlert',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/alerts/{alert_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlertResponse(),
            self.execute(params, req, runtime)
        )

    async def get_alert_with_options_async(
        self,
        project: str,
        alert_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAlertResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAlert',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/alerts/{alert_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlertResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_alert(
        self,
        project: str,
        alert_name: str,
    ) -> main_models.GetAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_alert_with_options(project, alert_name, headers, runtime)

    async def get_alert_async(
        self,
        project: str,
        alert_name: str,
    ) -> main_models.GetAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_alert_with_options_async(project, alert_name, headers, runtime)

    def get_annotation_data_with_options(
        self,
        dataset_id: str,
        annotationdata_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAnnotationDataResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAnnotationData',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/annotationdataset/{dataset_id}/annotationdata/{annotationdata_id}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAnnotationDataResponse(),
            self.execute(params, req, runtime)
        )

    async def get_annotation_data_with_options_async(
        self,
        dataset_id: str,
        annotationdata_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAnnotationDataResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAnnotationData',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/annotationdataset/{dataset_id}/annotationdata/{annotationdata_id}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAnnotationDataResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_annotation_data(
        self,
        dataset_id: str,
        annotationdata_id: str,
    ) -> main_models.GetAnnotationDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_annotation_data_with_options(dataset_id, annotationdata_id, headers, runtime)

    async def get_annotation_data_async(
        self,
        dataset_id: str,
        annotationdata_id: str,
    ) -> main_models.GetAnnotationDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_annotation_data_with_options_async(dataset_id, annotationdata_id, headers, runtime)

    def get_annotation_data_set_with_options(
        self,
        dataset_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAnnotationDataSetResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAnnotationDataSet',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/annotationdataset/{dataset_id}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAnnotationDataSetResponse(),
            self.execute(params, req, runtime)
        )

    async def get_annotation_data_set_with_options_async(
        self,
        dataset_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAnnotationDataSetResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAnnotationDataSet',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/annotationdataset/{dataset_id}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAnnotationDataSetResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_annotation_data_set(
        self,
        dataset_id: str,
    ) -> main_models.GetAnnotationDataSetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_annotation_data_set_with_options(dataset_id, headers, runtime)

    async def get_annotation_data_set_async(
        self,
        dataset_id: str,
    ) -> main_models.GetAnnotationDataSetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_annotation_data_set_with_options_async(dataset_id, headers, runtime)

    def get_annotation_label_with_options(
        self,
        label_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAnnotationLabelResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAnnotationLabel',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/annotationlabel/{label_id}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAnnotationLabelResponse(),
            self.execute(params, req, runtime)
        )

    async def get_annotation_label_with_options_async(
        self,
        label_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAnnotationLabelResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAnnotationLabel',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/annotationlabel/{label_id}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAnnotationLabelResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_annotation_label(
        self,
        label_id: str,
    ) -> main_models.GetAnnotationLabelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_annotation_label_with_options(label_id, headers, runtime)

    async def get_annotation_label_async(
        self,
        label_id: str,
    ) -> main_models.GetAnnotationLabelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_annotation_label_with_options_async(label_id, headers, runtime)

    def get_applied_configs_with_options(
        self,
        project: str,
        machine_group: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAppliedConfigsResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAppliedConfigs',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/machinegroups/{machine_group}/configs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppliedConfigsResponse(),
            self.execute(params, req, runtime)
        )

    async def get_applied_configs_with_options_async(
        self,
        project: str,
        machine_group: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAppliedConfigsResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAppliedConfigs',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/machinegroups/{machine_group}/configs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppliedConfigsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_applied_configs(
        self,
        project: str,
        machine_group: str,
    ) -> main_models.GetAppliedConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_applied_configs_with_options(project, machine_group, headers, runtime)

    async def get_applied_configs_async(
        self,
        project: str,
        machine_group: str,
    ) -> main_models.GetAppliedConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_applied_configs_with_options_async(project, machine_group, headers, runtime)

    def get_applied_machine_groups_with_options(
        self,
        project: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAppliedMachineGroupsResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAppliedMachineGroups',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/configs/{config_name}/machinegroups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppliedMachineGroupsResponse(),
            self.execute(params, req, runtime)
        )

    async def get_applied_machine_groups_with_options_async(
        self,
        project: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAppliedMachineGroupsResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAppliedMachineGroups',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/configs/{config_name}/machinegroups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppliedMachineGroupsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_applied_machine_groups(
        self,
        project: str,
        config_name: str,
    ) -> main_models.GetAppliedMachineGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_applied_machine_groups_with_options(project, config_name, headers, runtime)

    async def get_applied_machine_groups_async(
        self,
        project: str,
        config_name: str,
    ) -> main_models.GetAppliedMachineGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_applied_machine_groups_with_options_async(project, config_name, headers, runtime)

    def get_async_sql_with_options(
        self,
        project: str,
        query_id: str,
        request: main_models.GetAsyncSqlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAsyncSqlResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.line):
            query['line'] = request.line
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAsyncSql',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/asyncsql/{query_id}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'none',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAsyncSqlResponse(),
            self.execute(params, req, runtime)
        )

    async def get_async_sql_with_options_async(
        self,
        project: str,
        query_id: str,
        request: main_models.GetAsyncSqlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAsyncSqlResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.line):
            query['line'] = request.line
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAsyncSql',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/asyncsql/{query_id}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'none',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAsyncSqlResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_async_sql(
        self,
        project: str,
        query_id: str,
        request: main_models.GetAsyncSqlRequest,
    ) -> main_models.GetAsyncSqlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_async_sql_with_options(project, query_id, request, headers, runtime)

    async def get_async_sql_async(
        self,
        project: str,
        query_id: str,
        request: main_models.GetAsyncSqlRequest,
    ) -> main_models.GetAsyncSqlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_async_sql_with_options_async(project, query_id, request, headers, runtime)

    def get_azure_blob_ingestion_with_options(
        self,
        project: str,
        azure_blob_ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAzureBlobIngestionResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAzureBlobIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/azureblobingestions/{azure_blob_ingestion_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAzureBlobIngestionResponse(),
            self.execute(params, req, runtime)
        )

    async def get_azure_blob_ingestion_with_options_async(
        self,
        project: str,
        azure_blob_ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAzureBlobIngestionResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAzureBlobIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/azureblobingestions/{azure_blob_ingestion_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAzureBlobIngestionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_azure_blob_ingestion(
        self,
        project: str,
        azure_blob_ingestion_name: str,
    ) -> main_models.GetAzureBlobIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_azure_blob_ingestion_with_options(project, azure_blob_ingestion_name, headers, runtime)

    async def get_azure_blob_ingestion_async(
        self,
        project: str,
        azure_blob_ingestion_name: str,
    ) -> main_models.GetAzureBlobIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_azure_blob_ingestion_with_options_async(project, azure_blob_ingestion_name, headers, runtime)

    def get_check_point_with_options(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: main_models.GetCheckPointRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCheckPointResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.shard):
            query['shard'] = request.shard
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCheckPoint',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/consumergroups/{consumer_group}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.GetCheckPointResponse(),
            self.execute(params, req, runtime)
        )

    async def get_check_point_with_options_async(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: main_models.GetCheckPointRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCheckPointResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.shard):
            query['shard'] = request.shard
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCheckPoint',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/consumergroups/{consumer_group}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.GetCheckPointResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_check_point(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: main_models.GetCheckPointRequest,
    ) -> main_models.GetCheckPointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_check_point_with_options(project, logstore, consumer_group, request, headers, runtime)

    async def get_check_point_async(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: main_models.GetCheckPointRequest,
    ) -> main_models.GetCheckPointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_check_point_with_options_async(project, logstore, consumer_group, request, headers, runtime)

    def get_collection_policy_with_options(
        self,
        policy_name: str,
        request: main_models.GetCollectionPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCollectionPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_code):
            query['dataCode'] = request.data_code
        if not DaraCore.is_null(request.product_code):
            query['productCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCollectionPolicy',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/collectionpolicy/{policy_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCollectionPolicyResponse(),
            self.execute(params, req, runtime)
        )

    async def get_collection_policy_with_options_async(
        self,
        policy_name: str,
        request: main_models.GetCollectionPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCollectionPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_code):
            query['dataCode'] = request.data_code
        if not DaraCore.is_null(request.product_code):
            query['productCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCollectionPolicy',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/collectionpolicy/{policy_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCollectionPolicyResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_collection_policy(
        self,
        policy_name: str,
        request: main_models.GetCollectionPolicyRequest,
    ) -> main_models.GetCollectionPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_collection_policy_with_options(policy_name, request, headers, runtime)

    async def get_collection_policy_async(
        self,
        policy_name: str,
        request: main_models.GetCollectionPolicyRequest,
    ) -> main_models.GetCollectionPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_collection_policy_with_options_async(policy_name, request, headers, runtime)

    def get_config_with_options(
        self,
        project: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConfigResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetConfig',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/configs/{config_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConfigResponse(),
            self.execute(params, req, runtime)
        )

    async def get_config_with_options_async(
        self,
        project: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConfigResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetConfig',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/configs/{config_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConfigResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_config(
        self,
        project: str,
        config_name: str,
    ) -> main_models.GetConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_config_with_options(project, config_name, headers, runtime)

    async def get_config_async(
        self,
        project: str,
        config_name: str,
    ) -> main_models.GetConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_config_with_options_async(project, config_name, headers, runtime)

    def get_consume_processor_with_options(
        self,
        project: str,
        processor_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConsumeProcessorResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetConsumeProcessor',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/consumeprocessors/{processor_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConsumeProcessorResponse(),
            self.execute(params, req, runtime)
        )

    async def get_consume_processor_with_options_async(
        self,
        project: str,
        processor_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConsumeProcessorResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetConsumeProcessor',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/consumeprocessors/{processor_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConsumeProcessorResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_consume_processor(
        self,
        project: str,
        processor_name: str,
    ) -> main_models.GetConsumeProcessorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_consume_processor_with_options(project, processor_name, headers, runtime)

    async def get_consume_processor_async(
        self,
        project: str,
        processor_name: str,
    ) -> main_models.GetConsumeProcessorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_consume_processor_with_options_async(project, processor_name, headers, runtime)

    def get_context_logs_with_options(
        self,
        project: str,
        logstore: str,
        request: main_models.GetContextLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetContextLogsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.back_lines):
            query['back_lines'] = request.back_lines
        if not DaraCore.is_null(request.forward_lines):
            query['forward_lines'] = request.forward_lines
        if not DaraCore.is_null(request.pack_id):
            query['pack_id'] = request.pack_id
        if not DaraCore.is_null(request.pack_meta):
            query['pack_meta'] = request.pack_meta
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetContextLogs',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}?type=context_log',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetContextLogsResponse(),
            self.execute(params, req, runtime)
        )

    async def get_context_logs_with_options_async(
        self,
        project: str,
        logstore: str,
        request: main_models.GetContextLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetContextLogsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.back_lines):
            query['back_lines'] = request.back_lines
        if not DaraCore.is_null(request.forward_lines):
            query['forward_lines'] = request.forward_lines
        if not DaraCore.is_null(request.pack_id):
            query['pack_id'] = request.pack_id
        if not DaraCore.is_null(request.pack_meta):
            query['pack_meta'] = request.pack_meta
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetContextLogs',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}?type=context_log',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetContextLogsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_context_logs(
        self,
        project: str,
        logstore: str,
        request: main_models.GetContextLogsRequest,
    ) -> main_models.GetContextLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_context_logs_with_options(project, logstore, request, headers, runtime)

    async def get_context_logs_async(
        self,
        project: str,
        logstore: str,
        request: main_models.GetContextLogsRequest,
    ) -> main_models.GetContextLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_context_logs_with_options_async(project, logstore, request, headers, runtime)

    def get_cursor_with_options(
        self,
        project: str,
        logstore: str,
        shard_id: str,
        request: main_models.GetCursorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCursorResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.from_):
            query['from'] = request.from_
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCursor',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/shards/{shard_id}?type=cursor',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCursorResponse(),
            self.execute(params, req, runtime)
        )

    async def get_cursor_with_options_async(
        self,
        project: str,
        logstore: str,
        shard_id: str,
        request: main_models.GetCursorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCursorResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.from_):
            query['from'] = request.from_
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCursor',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/shards/{shard_id}?type=cursor',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCursorResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_cursor(
        self,
        project: str,
        logstore: str,
        shard_id: str,
        request: main_models.GetCursorRequest,
    ) -> main_models.GetCursorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_cursor_with_options(project, logstore, shard_id, request, headers, runtime)

    async def get_cursor_async(
        self,
        project: str,
        logstore: str,
        shard_id: str,
        request: main_models.GetCursorRequest,
    ) -> main_models.GetCursorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_cursor_with_options_async(project, logstore, shard_id, request, headers, runtime)

    def get_cursor_time_with_options(
        self,
        project: str,
        logstore: str,
        shard_id: str,
        request: main_models.GetCursorTimeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCursorTimeResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.cursor):
            query['cursor'] = request.cursor
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCursorTime',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/shards/{shard_id}?type=cursor_time',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCursorTimeResponse(),
            self.execute(params, req, runtime)
        )

    async def get_cursor_time_with_options_async(
        self,
        project: str,
        logstore: str,
        shard_id: str,
        request: main_models.GetCursorTimeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCursorTimeResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.cursor):
            query['cursor'] = request.cursor
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCursorTime',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/shards/{shard_id}?type=cursor_time',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCursorTimeResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_cursor_time(
        self,
        project: str,
        logstore: str,
        shard_id: str,
        request: main_models.GetCursorTimeRequest,
    ) -> main_models.GetCursorTimeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_cursor_time_with_options(project, logstore, shard_id, request, headers, runtime)

    async def get_cursor_time_async(
        self,
        project: str,
        logstore: str,
        shard_id: str,
        request: main_models.GetCursorTimeRequest,
    ) -> main_models.GetCursorTimeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_cursor_time_with_options_async(project, logstore, shard_id, request, headers, runtime)

    def get_dashboard_with_options(
        self,
        project: str,
        dashboard_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDashboardResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDashboard',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/dashboards/{dashboard_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDashboardResponse(),
            self.execute(params, req, runtime)
        )

    async def get_dashboard_with_options_async(
        self,
        project: str,
        dashboard_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDashboardResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDashboard',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/dashboards/{dashboard_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDashboardResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_dashboard(
        self,
        project: str,
        dashboard_name: str,
    ) -> main_models.GetDashboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_dashboard_with_options(project, dashboard_name, headers, runtime)

    async def get_dashboard_async(
        self,
        project: str,
        dashboard_name: str,
    ) -> main_models.GetDashboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_dashboard_with_options_async(project, dashboard_name, headers, runtime)

    def get_download_job_with_options(
        self,
        project: str,
        download_job_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDownloadJobResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDownloadJob',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/downloadjobs/{download_job_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDownloadJobResponse(),
            self.execute(params, req, runtime)
        )

    async def get_download_job_with_options_async(
        self,
        project: str,
        download_job_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDownloadJobResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDownloadJob',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/downloadjobs/{download_job_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDownloadJobResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_download_job(
        self,
        project: str,
        download_job_name: str,
    ) -> main_models.GetDownloadJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_download_job_with_options(project, download_job_name, headers, runtime)

    async def get_download_job_async(
        self,
        project: str,
        download_job_name: str,
    ) -> main_models.GetDownloadJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_download_job_with_options_async(project, download_job_name, headers, runtime)

    def get_etlwith_options(
        self,
        project: str,
        etl_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetETLResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetETL',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/etls/{etl_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetETLResponse(),
            self.execute(params, req, runtime)
        )

    async def get_etlwith_options_async(
        self,
        project: str,
        etl_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetETLResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetETL',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/etls/{etl_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetETLResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_etl(
        self,
        project: str,
        etl_name: str,
    ) -> main_models.GetETLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_etlwith_options(project, etl_name, headers, runtime)

    async def get_etl_async(
        self,
        project: str,
        etl_name: str,
    ) -> main_models.GetETLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_etlwith_options_async(project, etl_name, headers, runtime)

    def get_elasticsearch_ingestion_with_options(
        self,
        project: str,
        es_ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetElasticsearchIngestionResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetElasticsearchIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/elasticsearchingestions/{es_ingestion_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetElasticsearchIngestionResponse(),
            self.execute(params, req, runtime)
        )

    async def get_elasticsearch_ingestion_with_options_async(
        self,
        project: str,
        es_ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetElasticsearchIngestionResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetElasticsearchIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/elasticsearchingestions/{es_ingestion_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetElasticsearchIngestionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_elasticsearch_ingestion(
        self,
        project: str,
        es_ingestion_name: str,
    ) -> main_models.GetElasticsearchIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_elasticsearch_ingestion_with_options(project, es_ingestion_name, headers, runtime)

    async def get_elasticsearch_ingestion_async(
        self,
        project: str,
        es_ingestion_name: str,
    ) -> main_models.GetElasticsearchIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_elasticsearch_ingestion_with_options_async(project, es_ingestion_name, headers, runtime)

    def get_histograms_with_options(
        self,
        project: str,
        logstore: str,
        request: main_models.GetHistogramsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHistogramsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.from_):
            query['from'] = request.from_
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.to):
            query['to'] = request.to
        if not DaraCore.is_null(request.topic):
            query['topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHistograms',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/index?type=histogram',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.GetHistogramsResponse(),
            self.execute(params, req, runtime)
        )

    async def get_histograms_with_options_async(
        self,
        project: str,
        logstore: str,
        request: main_models.GetHistogramsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHistogramsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.from_):
            query['from'] = request.from_
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.to):
            query['to'] = request.to
        if not DaraCore.is_null(request.topic):
            query['topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHistograms',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/index?type=histogram',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.GetHistogramsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_histograms(
        self,
        project: str,
        logstore: str,
        request: main_models.GetHistogramsRequest,
    ) -> main_models.GetHistogramsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_histograms_with_options(project, logstore, request, headers, runtime)

    async def get_histograms_async(
        self,
        project: str,
        logstore: str,
        request: main_models.GetHistogramsRequest,
    ) -> main_models.GetHistogramsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_histograms_with_options_async(project, logstore, request, headers, runtime)

    def get_index_with_options(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIndexResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetIndex',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/index',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIndexResponse(),
            self.execute(params, req, runtime)
        )

    async def get_index_with_options_async(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIndexResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetIndex',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/index',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIndexResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_index(
        self,
        project: str,
        logstore: str,
    ) -> main_models.GetIndexResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_index_with_options(project, logstore, headers, runtime)

    async def get_index_async(
        self,
        project: str,
        logstore: str,
    ) -> main_models.GetIndexResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_index_with_options_async(project, logstore, headers, runtime)

    def get_ingest_processor_with_options(
        self,
        project: str,
        processor_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIngestProcessorResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetIngestProcessor',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ingestprocessors/{processor_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIngestProcessorResponse(),
            self.execute(params, req, runtime)
        )

    async def get_ingest_processor_with_options_async(
        self,
        project: str,
        processor_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIngestProcessorResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetIngestProcessor',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ingestprocessors/{processor_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIngestProcessorResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_ingest_processor(
        self,
        project: str,
        processor_name: str,
    ) -> main_models.GetIngestProcessorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_ingest_processor_with_options(project, processor_name, headers, runtime)

    async def get_ingest_processor_async(
        self,
        project: str,
        processor_name: str,
    ) -> main_models.GetIngestProcessorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_ingest_processor_with_options_async(project, processor_name, headers, runtime)

    def get_log_store_with_options(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLogStoreResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLogStore',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLogStoreResponse(),
            self.execute(params, req, runtime)
        )

    async def get_log_store_with_options_async(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLogStoreResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLogStore',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLogStoreResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_log_store(
        self,
        project: str,
        logstore: str,
    ) -> main_models.GetLogStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_log_store_with_options(project, logstore, headers, runtime)

    async def get_log_store_async(
        self,
        project: str,
        logstore: str,
    ) -> main_models.GetLogStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_log_store_with_options_async(project, logstore, headers, runtime)

    def get_log_store_metering_mode_with_options(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLogStoreMeteringModeResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLogStoreMeteringMode',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/meteringmode',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLogStoreMeteringModeResponse(),
            self.execute(params, req, runtime)
        )

    async def get_log_store_metering_mode_with_options_async(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLogStoreMeteringModeResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLogStoreMeteringMode',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/meteringmode',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLogStoreMeteringModeResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_log_store_metering_mode(
        self,
        project: str,
        logstore: str,
    ) -> main_models.GetLogStoreMeteringModeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_log_store_metering_mode_with_options(project, logstore, headers, runtime)

    async def get_log_store_metering_mode_async(
        self,
        project: str,
        logstore: str,
    ) -> main_models.GetLogStoreMeteringModeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_log_store_metering_mode_with_options_async(project, logstore, headers, runtime)

    def get_logging_with_options(
        self,
        project: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLoggingResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLogging',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logging',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLoggingResponse(),
            self.execute(params, req, runtime)
        )

    async def get_logging_with_options_async(
        self,
        project: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLoggingResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLogging',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logging',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLoggingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_logging(
        self,
        project: str,
    ) -> main_models.GetLoggingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_logging_with_options(project, headers, runtime)

    async def get_logging_async(
        self,
        project: str,
    ) -> main_models.GetLoggingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_logging_with_options_async(project, headers, runtime)

    def get_logs_with_options(
        self,
        project: str,
        logstore: str,
        request: main_models.GetLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLogsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.from_):
            query['from'] = request.from_
        if not DaraCore.is_null(request.line):
            query['line'] = request.line
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.power_sql):
            query['powerSql'] = request.power_sql
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.reverse):
            query['reverse'] = request.reverse
        if not DaraCore.is_null(request.to):
            query['to'] = request.to
        if not DaraCore.is_null(request.topic):
            query['topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLogs',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}?type=log',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.GetLogsResponse(),
            self.execute(params, req, runtime)
        )

    async def get_logs_with_options_async(
        self,
        project: str,
        logstore: str,
        request: main_models.GetLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLogsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.from_):
            query['from'] = request.from_
        if not DaraCore.is_null(request.line):
            query['line'] = request.line
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.power_sql):
            query['powerSql'] = request.power_sql
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.reverse):
            query['reverse'] = request.reverse
        if not DaraCore.is_null(request.to):
            query['to'] = request.to
        if not DaraCore.is_null(request.topic):
            query['topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLogs',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}?type=log',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.GetLogsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_logs(
        self,
        project: str,
        logstore: str,
        request: main_models.GetLogsRequest,
    ) -> main_models.GetLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_logs_with_options(project, logstore, request, headers, runtime)

    async def get_logs_async(
        self,
        project: str,
        logstore: str,
        request: main_models.GetLogsRequest,
    ) -> main_models.GetLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_logs_with_options_async(project, logstore, request, headers, runtime)

    def get_logs_v2with_options(
        self,
        project: str,
        logstore: str,
        request: main_models.GetLogsV2Request,
        headers: main_models.GetLogsV2Headers,
        runtime: RuntimeOptions,
    ) -> main_models.GetLogsV2Response:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.forward):
            body['forward'] = request.forward
        if not DaraCore.is_null(request.from_):
            body['from'] = request.from_
        if not DaraCore.is_null(request.highlight):
            body['highlight'] = request.highlight
        if not DaraCore.is_null(request.line):
            body['line'] = request.line
        if not DaraCore.is_null(request.offset):
            body['offset'] = request.offset
        if not DaraCore.is_null(request.power_sql):
            body['powerSql'] = request.power_sql
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.reverse):
            body['reverse'] = request.reverse
        if not DaraCore.is_null(request.session):
            body['session'] = request.session
        if not DaraCore.is_null(request.to):
            body['to'] = request.to
        if not DaraCore.is_null(request.topic):
            body['topic'] = request.topic
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.accept_encoding):
            real_headers['Accept-Encoding'] = str(headers.accept_encoding)
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetLogsV2',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/logs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLogsV2Response(),
            self.execute(params, req, runtime)
        )

    async def get_logs_v2with_options_async(
        self,
        project: str,
        logstore: str,
        request: main_models.GetLogsV2Request,
        headers: main_models.GetLogsV2Headers,
        runtime: RuntimeOptions,
    ) -> main_models.GetLogsV2Response:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.forward):
            body['forward'] = request.forward
        if not DaraCore.is_null(request.from_):
            body['from'] = request.from_
        if not DaraCore.is_null(request.highlight):
            body['highlight'] = request.highlight
        if not DaraCore.is_null(request.line):
            body['line'] = request.line
        if not DaraCore.is_null(request.offset):
            body['offset'] = request.offset
        if not DaraCore.is_null(request.power_sql):
            body['powerSql'] = request.power_sql
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.reverse):
            body['reverse'] = request.reverse
        if not DaraCore.is_null(request.session):
            body['session'] = request.session
        if not DaraCore.is_null(request.to):
            body['to'] = request.to
        if not DaraCore.is_null(request.topic):
            body['topic'] = request.topic
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.accept_encoding):
            real_headers['Accept-Encoding'] = str(headers.accept_encoding)
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetLogsV2',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/logs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLogsV2Response(),
            await self.execute_async(params, req, runtime)
        )

    def get_logs_v2(
        self,
        project: str,
        logstore: str,
        request: main_models.GetLogsV2Request,
    ) -> main_models.GetLogsV2Response:
        runtime = RuntimeOptions()
        headers = main_models.GetLogsV2Headers()
        return self.get_logs_v2with_options(project, logstore, request, headers, runtime)

    async def get_logs_v2_async(
        self,
        project: str,
        logstore: str,
        request: main_models.GetLogsV2Request,
    ) -> main_models.GetLogsV2Response:
        runtime = RuntimeOptions()
        headers = main_models.GetLogsV2Headers()
        return await self.get_logs_v2with_options_async(project, logstore, request, headers, runtime)

    def get_logtail_pipeline_config_with_options(
        self,
        project: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLogtailPipelineConfigResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLogtailPipelineConfig',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/pipelineconfigs/{config_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLogtailPipelineConfigResponse(),
            self.execute(params, req, runtime)
        )

    async def get_logtail_pipeline_config_with_options_async(
        self,
        project: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLogtailPipelineConfigResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLogtailPipelineConfig',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/pipelineconfigs/{config_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLogtailPipelineConfigResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_logtail_pipeline_config(
        self,
        project: str,
        config_name: str,
    ) -> main_models.GetLogtailPipelineConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_logtail_pipeline_config_with_options(project, config_name, headers, runtime)

    async def get_logtail_pipeline_config_async(
        self,
        project: str,
        config_name: str,
    ) -> main_models.GetLogtailPipelineConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_logtail_pipeline_config_with_options_async(project, config_name, headers, runtime)

    def get_mlservice_results_with_options(
        self,
        service_name: str,
        request: main_models.GetMLServiceResultsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMLServiceResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_builtin):
            query['allowBuiltin'] = request.allow_builtin
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'GetMLServiceResults',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/service/{service_name}/analysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMLServiceResultsResponse(),
            self.execute(params, req, runtime)
        )

    async def get_mlservice_results_with_options_async(
        self,
        service_name: str,
        request: main_models.GetMLServiceResultsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMLServiceResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_builtin):
            query['allowBuiltin'] = request.allow_builtin
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'GetMLServiceResults',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/service/{service_name}/analysis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMLServiceResultsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_mlservice_results(
        self,
        service_name: str,
        request: main_models.GetMLServiceResultsRequest,
    ) -> main_models.GetMLServiceResultsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_mlservice_results_with_options(service_name, request, headers, runtime)

    async def get_mlservice_results_async(
        self,
        service_name: str,
        request: main_models.GetMLServiceResultsRequest,
    ) -> main_models.GetMLServiceResultsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_mlservice_results_with_options_async(service_name, request, headers, runtime)

    def get_machine_group_with_options(
        self,
        project: str,
        machine_group: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMachineGroupResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMachineGroup',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/machinegroups/{machine_group}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMachineGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def get_machine_group_with_options_async(
        self,
        project: str,
        machine_group: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMachineGroupResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMachineGroup',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/machinegroups/{machine_group}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMachineGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_machine_group(
        self,
        project: str,
        machine_group: str,
    ) -> main_models.GetMachineGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_machine_group_with_options(project, machine_group, headers, runtime)

    async def get_machine_group_async(
        self,
        project: str,
        machine_group: str,
    ) -> main_models.GetMachineGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_machine_group_with_options_async(project, machine_group, headers, runtime)

    def get_materialized_view_with_options(
        self,
        project: str,
        name: str,
        headers: main_models.GetMaterializedViewHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetMaterializedViewResponse:
        host_map = {}
        host_map['project'] = project
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.content_type):
            real_headers['Content-Type'] = str(headers.content_type)
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetMaterializedView',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/materializedviews/{name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMaterializedViewResponse(),
            self.execute(params, req, runtime)
        )

    async def get_materialized_view_with_options_async(
        self,
        project: str,
        name: str,
        headers: main_models.GetMaterializedViewHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetMaterializedViewResponse:
        host_map = {}
        host_map['project'] = project
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.content_type):
            real_headers['Content-Type'] = str(headers.content_type)
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetMaterializedView',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/materializedviews/{name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMaterializedViewResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_materialized_view(
        self,
        project: str,
        name: str,
    ) -> main_models.GetMaterializedViewResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetMaterializedViewHeaders()
        return self.get_materialized_view_with_options(project, name, headers, runtime)

    async def get_materialized_view_async(
        self,
        project: str,
        name: str,
    ) -> main_models.GetMaterializedViewResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetMaterializedViewHeaders()
        return await self.get_materialized_view_with_options_async(project, name, headers, runtime)

    def get_max_compute_export_with_options(
        self,
        project: str,
        mc_export_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMaxComputeExportResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMaxComputeExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/maxcomputeexports/{mc_export_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMaxComputeExportResponse(),
            self.execute(params, req, runtime)
        )

    async def get_max_compute_export_with_options_async(
        self,
        project: str,
        mc_export_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMaxComputeExportResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMaxComputeExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/maxcomputeexports/{mc_export_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMaxComputeExportResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_max_compute_export(
        self,
        project: str,
        mc_export_name: str,
    ) -> main_models.GetMaxComputeExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_max_compute_export_with_options(project, mc_export_name, headers, runtime)

    async def get_max_compute_export_async(
        self,
        project: str,
        mc_export_name: str,
    ) -> main_models.GetMaxComputeExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_max_compute_export_with_options_async(project, mc_export_name, headers, runtime)

    def get_metric_store_with_options(
        self,
        project: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMetricStoreResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMetricStore',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/metricstores/{name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'none',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMetricStoreResponse(),
            self.execute(params, req, runtime)
        )

    async def get_metric_store_with_options_async(
        self,
        project: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMetricStoreResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMetricStore',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/metricstores/{name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'none',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMetricStoreResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_metric_store(
        self,
        project: str,
        name: str,
    ) -> main_models.GetMetricStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_metric_store_with_options(project, name, headers, runtime)

    async def get_metric_store_async(
        self,
        project: str,
        name: str,
    ) -> main_models.GetMetricStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_metric_store_with_options_async(project, name, headers, runtime)

    def get_metric_store_metering_mode_with_options(
        self,
        project: str,
        metric_store: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMetricStoreMeteringModeResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMetricStoreMeteringMode',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/metricstores/{metric_store}/meteringmode',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMetricStoreMeteringModeResponse(),
            self.execute(params, req, runtime)
        )

    async def get_metric_store_metering_mode_with_options_async(
        self,
        project: str,
        metric_store: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMetricStoreMeteringModeResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMetricStoreMeteringMode',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/metricstores/{metric_store}/meteringmode',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMetricStoreMeteringModeResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_metric_store_metering_mode(
        self,
        project: str,
        metric_store: str,
    ) -> main_models.GetMetricStoreMeteringModeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_metric_store_metering_mode_with_options(project, metric_store, headers, runtime)

    async def get_metric_store_metering_mode_async(
        self,
        project: str,
        metric_store: str,
    ) -> main_models.GetMetricStoreMeteringModeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_metric_store_metering_mode_with_options_async(project, metric_store, headers, runtime)

    def get_ossexport_with_options(
        self,
        project: str,
        oss_export_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetOSSExportResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetOSSExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ossexports/{oss_export_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOSSExportResponse(),
            self.execute(params, req, runtime)
        )

    async def get_ossexport_with_options_async(
        self,
        project: str,
        oss_export_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetOSSExportResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetOSSExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ossexports/{oss_export_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOSSExportResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_ossexport(
        self,
        project: str,
        oss_export_name: str,
    ) -> main_models.GetOSSExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_ossexport_with_options(project, oss_export_name, headers, runtime)

    async def get_ossexport_async(
        self,
        project: str,
        oss_export_name: str,
    ) -> main_models.GetOSSExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_ossexport_with_options_async(project, oss_export_name, headers, runtime)

    def get_osshdfsexport_with_options(
        self,
        project: str,
        oss_export_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetOSSHDFSExportResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetOSSHDFSExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/osshdfsexports/{oss_export_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOSSHDFSExportResponse(),
            self.execute(params, req, runtime)
        )

    async def get_osshdfsexport_with_options_async(
        self,
        project: str,
        oss_export_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetOSSHDFSExportResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetOSSHDFSExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/osshdfsexports/{oss_export_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOSSHDFSExportResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_osshdfsexport(
        self,
        project: str,
        oss_export_name: str,
    ) -> main_models.GetOSSHDFSExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_osshdfsexport_with_options(project, oss_export_name, headers, runtime)

    async def get_osshdfsexport_async(
        self,
        project: str,
        oss_export_name: str,
    ) -> main_models.GetOSSHDFSExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_osshdfsexport_with_options_async(project, oss_export_name, headers, runtime)

    def get_ossingestion_with_options(
        self,
        project: str,
        oss_ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetOSSIngestionResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetOSSIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ossingestions/{oss_ingestion_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOSSIngestionResponse(),
            self.execute(params, req, runtime)
        )

    async def get_ossingestion_with_options_async(
        self,
        project: str,
        oss_ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetOSSIngestionResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetOSSIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ossingestions/{oss_ingestion_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOSSIngestionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_ossingestion(
        self,
        project: str,
        oss_ingestion_name: str,
    ) -> main_models.GetOSSIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_ossingestion_with_options(project, oss_ingestion_name, headers, runtime)

    async def get_ossingestion_async(
        self,
        project: str,
        oss_ingestion_name: str,
    ) -> main_models.GetOSSIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_ossingestion_with_options_async(project, oss_ingestion_name, headers, runtime)

    def get_project_with_options(
        self,
        project: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetProject',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectResponse(),
            self.execute(params, req, runtime)
        )

    async def get_project_with_options_async(
        self,
        project: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetProject',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_project(
        self,
        project: str,
    ) -> main_models.GetProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_project_with_options(project, headers, runtime)

    async def get_project_async(
        self,
        project: str,
    ) -> main_models.GetProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_project_with_options_async(project, headers, runtime)

    def get_project_logs_with_options(
        self,
        project: str,
        request: main_models.GetProjectLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectLogsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.power_sql):
            query['powerSql'] = request.power_sql
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProjectLogs',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.GetProjectLogsResponse(),
            self.execute(params, req, runtime)
        )

    async def get_project_logs_with_options_async(
        self,
        project: str,
        request: main_models.GetProjectLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectLogsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.power_sql):
            query['powerSql'] = request.power_sql
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProjectLogs',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.GetProjectLogsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_project_logs(
        self,
        project: str,
        request: main_models.GetProjectLogsRequest,
    ) -> main_models.GetProjectLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_project_logs_with_options(project, request, headers, runtime)

    async def get_project_logs_async(
        self,
        project: str,
        request: main_models.GetProjectLogsRequest,
    ) -> main_models.GetProjectLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_project_logs_with_options_async(project, request, headers, runtime)

    def get_project_policy_with_options(
        self,
        project: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectPolicyResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetProjectPolicy',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/policy',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'string'
        )
        return DaraCore.from_map(
            main_models.GetProjectPolicyResponse(),
            self.execute(params, req, runtime)
        )

    async def get_project_policy_with_options_async(
        self,
        project: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectPolicyResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetProjectPolicy',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/policy',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'string'
        )
        return DaraCore.from_map(
            main_models.GetProjectPolicyResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_project_policy(
        self,
        project: str,
    ) -> main_models.GetProjectPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_project_policy_with_options(project, headers, runtime)

    async def get_project_policy_async(
        self,
        project: str,
    ) -> main_models.GetProjectPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_project_policy_with_options_async(project, headers, runtime)

    def get_s3ingestion_with_options(
        self,
        project: str,
        s_3ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetS3IngestionResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetS3Ingestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/s3ingestions/{s_3ingestion_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetS3IngestionResponse(),
            self.execute(params, req, runtime)
        )

    async def get_s3ingestion_with_options_async(
        self,
        project: str,
        s_3ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetS3IngestionResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetS3Ingestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/s3ingestions/{s_3ingestion_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetS3IngestionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_s3ingestion(
        self,
        project: str,
        s_3ingestion_name: str,
    ) -> main_models.GetS3IngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_s3ingestion_with_options(project, s_3ingestion_name, headers, runtime)

    async def get_s3ingestion_async(
        self,
        project: str,
        s_3ingestion_name: str,
    ) -> main_models.GetS3IngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_s3ingestion_with_options_async(project, s_3ingestion_name, headers, runtime)

    def get_saved_search_with_options(
        self,
        project: str,
        savedsearch_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSavedSearchResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSavedSearch',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/savedsearches/{savedsearch_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSavedSearchResponse(),
            self.execute(params, req, runtime)
        )

    async def get_saved_search_with_options_async(
        self,
        project: str,
        savedsearch_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSavedSearchResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSavedSearch',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/savedsearches/{savedsearch_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSavedSearchResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_saved_search(
        self,
        project: str,
        savedsearch_name: str,
    ) -> main_models.GetSavedSearchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_saved_search_with_options(project, savedsearch_name, headers, runtime)

    async def get_saved_search_async(
        self,
        project: str,
        savedsearch_name: str,
    ) -> main_models.GetSavedSearchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_saved_search_with_options_async(project, savedsearch_name, headers, runtime)

    def get_scheduled_sqlwith_options(
        self,
        project: str,
        scheduled_sqlname: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetScheduledSQLResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetScheduledSQL',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/scheduledsqls/{scheduled_sqlname}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScheduledSQLResponse(),
            self.execute(params, req, runtime)
        )

    async def get_scheduled_sqlwith_options_async(
        self,
        project: str,
        scheduled_sqlname: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetScheduledSQLResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetScheduledSQL',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/scheduledsqls/{scheduled_sqlname}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScheduledSQLResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_scheduled_sql(
        self,
        project: str,
        scheduled_sqlname: str,
    ) -> main_models.GetScheduledSQLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_scheduled_sqlwith_options(project, scheduled_sqlname, headers, runtime)

    async def get_scheduled_sql_async(
        self,
        project: str,
        scheduled_sqlname: str,
    ) -> main_models.GetScheduledSQLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_scheduled_sqlwith_options_async(project, scheduled_sqlname, headers, runtime)

    def get_sls_service_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSlsServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSlsService',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/slsservice',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSlsServiceResponse(),
            self.execute(params, req, runtime)
        )

    async def get_sls_service_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSlsServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSlsService',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/slsservice',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSlsServiceResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_sls_service(self) -> main_models.GetSlsServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_sls_service_with_options(headers, runtime)

    async def get_sls_service_async(self) -> main_models.GetSlsServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_sls_service_with_options_async(headers, runtime)

    def get_sql_instance_with_options(
        self,
        project: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSqlInstanceResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSqlInstance',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/sqlinstance',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.GetSqlInstanceResponse(),
            self.execute(params, req, runtime)
        )

    async def get_sql_instance_with_options_async(
        self,
        project: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSqlInstanceResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSqlInstance',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/sqlinstance',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.GetSqlInstanceResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_sql_instance(
        self,
        project: str,
    ) -> main_models.GetSqlInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_sql_instance_with_options(project, headers, runtime)

    async def get_sql_instance_async(
        self,
        project: str,
    ) -> main_models.GetSqlInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_sql_instance_with_options_async(project, headers, runtime)

    def get_store_view_with_options(
        self,
        project: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetStoreViewResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetStoreView',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/storeviews/{name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStoreViewResponse(),
            self.execute(params, req, runtime)
        )

    async def get_store_view_with_options_async(
        self,
        project: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetStoreViewResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetStoreView',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/storeviews/{name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStoreViewResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_store_view(
        self,
        project: str,
        name: str,
    ) -> main_models.GetStoreViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_store_view_with_options(project, name, headers, runtime)

    async def get_store_view_async(
        self,
        project: str,
        name: str,
    ) -> main_models.GetStoreViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_store_view_with_options_async(project, name, headers, runtime)

    def get_store_view_index_with_options(
        self,
        project: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetStoreViewIndexResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetStoreViewIndex',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/storeviews/{name}/index',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStoreViewIndexResponse(),
            self.execute(params, req, runtime)
        )

    async def get_store_view_index_with_options_async(
        self,
        project: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetStoreViewIndexResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetStoreViewIndex',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/storeviews/{name}/index',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStoreViewIndexResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_store_view_index(
        self,
        project: str,
        name: str,
    ) -> main_models.GetStoreViewIndexResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_store_view_index_with_options(project, name, headers, runtime)

    async def get_store_view_index_async(
        self,
        project: str,
        name: str,
    ) -> main_models.GetStoreViewIndexResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_store_view_index_with_options_async(project, name, headers, runtime)

    def list_agent_instance_configs_with_options(
        self,
        request: main_models.ListAgentInstanceConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentInstanceConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_type):
            query['configType'] = request.config_type
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentInstanceConfigs',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/agentinstanceconfigs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentInstanceConfigsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_agent_instance_configs_with_options_async(
        self,
        request: main_models.ListAgentInstanceConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentInstanceConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_type):
            query['configType'] = request.config_type
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgentInstanceConfigs',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/agentinstanceconfigs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentInstanceConfigsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_agent_instance_configs(
        self,
        request: main_models.ListAgentInstanceConfigsRequest,
    ) -> main_models.ListAgentInstanceConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_agent_instance_configs_with_options(request, headers, runtime)

    async def list_agent_instance_configs_async(
        self,
        request: main_models.ListAgentInstanceConfigsRequest,
    ) -> main_models.ListAgentInstanceConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_agent_instance_configs_with_options_async(request, headers, runtime)

    def list_ai_tools_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAiToolsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListAiTools',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/tool/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.ListAiToolsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_ai_tools_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAiToolsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListAiTools',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/tool/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.ListAiToolsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_ai_tools(self) -> main_models.ListAiToolsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_ai_tools_with_options(headers, runtime)

    async def list_ai_tools_async(self) -> main_models.ListAiToolsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_ai_tools_with_options_async(headers, runtime)

    def list_alerts_with_options(
        self,
        project: str,
        request: main_models.ListAlertsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAlertsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.logstore):
            query['logstore'] = request.logstore
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAlerts',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/alerts',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlertsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_alerts_with_options_async(
        self,
        project: str,
        request: main_models.ListAlertsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAlertsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.logstore):
            query['logstore'] = request.logstore
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAlerts',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/alerts',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlertsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_alerts(
        self,
        project: str,
        request: main_models.ListAlertsRequest,
    ) -> main_models.ListAlertsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_alerts_with_options(project, request, headers, runtime)

    async def list_alerts_async(
        self,
        project: str,
        request: main_models.ListAlertsRequest,
    ) -> main_models.ListAlertsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_alerts_with_options_async(project, request, headers, runtime)

    def list_annotation_data_with_options(
        self,
        dataset_id: str,
        request: main_models.ListAnnotationDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAnnotationDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAnnotationData',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/annotationdataset/{dataset_id}/annotationdata',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAnnotationDataResponse(),
            self.execute(params, req, runtime)
        )

    async def list_annotation_data_with_options_async(
        self,
        dataset_id: str,
        request: main_models.ListAnnotationDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAnnotationDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAnnotationData',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/annotationdataset/{dataset_id}/annotationdata',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAnnotationDataResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_annotation_data(
        self,
        dataset_id: str,
        request: main_models.ListAnnotationDataRequest,
    ) -> main_models.ListAnnotationDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_annotation_data_with_options(dataset_id, request, headers, runtime)

    async def list_annotation_data_async(
        self,
        dataset_id: str,
        request: main_models.ListAnnotationDataRequest,
    ) -> main_models.ListAnnotationDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_annotation_data_with_options_async(dataset_id, request, headers, runtime)

    def list_annotation_data_sets_with_options(
        self,
        request: main_models.ListAnnotationDataSetsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAnnotationDataSetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAnnotationDataSets',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/annotationdataset',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAnnotationDataSetsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_annotation_data_sets_with_options_async(
        self,
        request: main_models.ListAnnotationDataSetsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAnnotationDataSetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAnnotationDataSets',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/annotationdataset',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAnnotationDataSetsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_annotation_data_sets(
        self,
        request: main_models.ListAnnotationDataSetsRequest,
    ) -> main_models.ListAnnotationDataSetsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_annotation_data_sets_with_options(request, headers, runtime)

    async def list_annotation_data_sets_async(
        self,
        request: main_models.ListAnnotationDataSetsRequest,
    ) -> main_models.ListAnnotationDataSetsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_annotation_data_sets_with_options_async(request, headers, runtime)

    def list_annotation_labels_with_options(
        self,
        request: main_models.ListAnnotationLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAnnotationLabelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAnnotationLabels',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/annotationlabel',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAnnotationLabelsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_annotation_labels_with_options_async(
        self,
        request: main_models.ListAnnotationLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAnnotationLabelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAnnotationLabels',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/annotationlabel',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAnnotationLabelsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_annotation_labels(
        self,
        request: main_models.ListAnnotationLabelsRequest,
    ) -> main_models.ListAnnotationLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_annotation_labels_with_options(request, headers, runtime)

    async def list_annotation_labels_async(
        self,
        request: main_models.ListAnnotationLabelsRequest,
    ) -> main_models.ListAnnotationLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_annotation_labels_with_options_async(request, headers, runtime)

    def list_azure_blob_ingestion_with_options(
        self,
        project: str,
        request: main_models.ListAzureBlobIngestionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAzureBlobIngestionResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.logstore):
            query['logstore'] = request.logstore
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAzureBlobIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/azureblobingestions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAzureBlobIngestionResponse(),
            self.execute(params, req, runtime)
        )

    async def list_azure_blob_ingestion_with_options_async(
        self,
        project: str,
        request: main_models.ListAzureBlobIngestionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAzureBlobIngestionResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.logstore):
            query['logstore'] = request.logstore
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAzureBlobIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/azureblobingestions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAzureBlobIngestionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_azure_blob_ingestion(
        self,
        project: str,
        request: main_models.ListAzureBlobIngestionRequest,
    ) -> main_models.ListAzureBlobIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_azure_blob_ingestion_with_options(project, request, headers, runtime)

    async def list_azure_blob_ingestion_async(
        self,
        project: str,
        request: main_models.ListAzureBlobIngestionRequest,
    ) -> main_models.ListAzureBlobIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_azure_blob_ingestion_with_options_async(project, request, headers, runtime)

    def list_collection_policies_with_options(
        self,
        request: main_models.ListCollectionPoliciesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCollectionPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.central_project):
            query['centralProject'] = request.central_project
        if not DaraCore.is_null(request.data_code):
            query['dataCode'] = request.data_code
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.policy_name):
            query['policyName'] = request.policy_name
        if not DaraCore.is_null(request.product_code):
            query['productCode'] = request.product_code
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCollectionPolicies',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/collectionpolicy',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCollectionPoliciesResponse(),
            self.execute(params, req, runtime)
        )

    async def list_collection_policies_with_options_async(
        self,
        request: main_models.ListCollectionPoliciesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCollectionPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.central_project):
            query['centralProject'] = request.central_project
        if not DaraCore.is_null(request.data_code):
            query['dataCode'] = request.data_code
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.policy_name):
            query['policyName'] = request.policy_name
        if not DaraCore.is_null(request.product_code):
            query['productCode'] = request.product_code
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCollectionPolicies',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/collectionpolicy',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCollectionPoliciesResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_collection_policies(
        self,
        request: main_models.ListCollectionPoliciesRequest,
    ) -> main_models.ListCollectionPoliciesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_collection_policies_with_options(request, headers, runtime)

    async def list_collection_policies_async(
        self,
        request: main_models.ListCollectionPoliciesRequest,
    ) -> main_models.ListCollectionPoliciesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_collection_policies_with_options_async(request, headers, runtime)

    def list_config_with_options(
        self,
        project: str,
        request: main_models.ListConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConfigResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.config_name):
            query['configName'] = request.config_name
        if not DaraCore.is_null(request.logstore_name):
            query['logstoreName'] = request.logstore_name
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConfig',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/configs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConfigResponse(),
            self.execute(params, req, runtime)
        )

    async def list_config_with_options_async(
        self,
        project: str,
        request: main_models.ListConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConfigResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.config_name):
            query['configName'] = request.config_name
        if not DaraCore.is_null(request.logstore_name):
            query['logstoreName'] = request.logstore_name
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConfig',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/configs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConfigResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_config(
        self,
        project: str,
        request: main_models.ListConfigRequest,
    ) -> main_models.ListConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_config_with_options(project, request, headers, runtime)

    async def list_config_async(
        self,
        project: str,
        request: main_models.ListConfigRequest,
    ) -> main_models.ListConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_config_with_options_async(project, request, headers, runtime)

    def list_consume_processors_with_options(
        self,
        project: str,
        request: main_models.ListConsumeProcessorsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConsumeProcessorsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.display_name):
            query['displayName'] = request.display_name
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.processor_name):
            query['processorName'] = request.processor_name
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConsumeProcessors',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/consumeprocessors',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConsumeProcessorsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_consume_processors_with_options_async(
        self,
        project: str,
        request: main_models.ListConsumeProcessorsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConsumeProcessorsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.display_name):
            query['displayName'] = request.display_name
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.processor_name):
            query['processorName'] = request.processor_name
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConsumeProcessors',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/consumeprocessors',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConsumeProcessorsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_consume_processors(
        self,
        project: str,
        request: main_models.ListConsumeProcessorsRequest,
    ) -> main_models.ListConsumeProcessorsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_consume_processors_with_options(project, request, headers, runtime)

    async def list_consume_processors_async(
        self,
        project: str,
        request: main_models.ListConsumeProcessorsRequest,
    ) -> main_models.ListConsumeProcessorsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_consume_processors_with_options_async(project, request, headers, runtime)

    def list_consumer_group_with_options(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConsumerGroupResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListConsumerGroup',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/consumergroups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.ListConsumerGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def list_consumer_group_with_options_async(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConsumerGroupResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListConsumerGroup',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/consumergroups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.ListConsumerGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_consumer_group(
        self,
        project: str,
        logstore: str,
    ) -> main_models.ListConsumerGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_consumer_group_with_options(project, logstore, headers, runtime)

    async def list_consumer_group_async(
        self,
        project: str,
        logstore: str,
    ) -> main_models.ListConsumerGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_consumer_group_with_options_async(project, logstore, headers, runtime)

    def list_dashboard_with_options(
        self,
        project: str,
        tmp_req: main_models.ListDashboardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDashboardResponse:
        tmp_req.validate()
        host_map = {}
        host_map['project'] = project
        request = main_models.ListDashboardShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not DaraCore.is_null(request.dashboard_name):
            query['dashboardName'] = request.dashboard_name
        if not DaraCore.is_null(request.display_name):
            query['displayName'] = request.display_name
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDashboard',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/dashboards',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDashboardResponse(),
            self.execute(params, req, runtime)
        )

    async def list_dashboard_with_options_async(
        self,
        project: str,
        tmp_req: main_models.ListDashboardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDashboardResponse:
        tmp_req.validate()
        host_map = {}
        host_map['project'] = project
        request = main_models.ListDashboardShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not DaraCore.is_null(request.dashboard_name):
            query['dashboardName'] = request.dashboard_name
        if not DaraCore.is_null(request.display_name):
            query['displayName'] = request.display_name
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDashboard',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/dashboards',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDashboardResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_dashboard(
        self,
        project: str,
        request: main_models.ListDashboardRequest,
    ) -> main_models.ListDashboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_dashboard_with_options(project, request, headers, runtime)

    async def list_dashboard_async(
        self,
        project: str,
        request: main_models.ListDashboardRequest,
    ) -> main_models.ListDashboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_dashboard_with_options_async(project, request, headers, runtime)

    def list_domains_with_options(
        self,
        project: str,
        request: main_models.ListDomainsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDomainsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['domainName'] = request.domain_name
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDomains',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/domains',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDomainsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_domains_with_options_async(
        self,
        project: str,
        request: main_models.ListDomainsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDomainsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['domainName'] = request.domain_name
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDomains',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/domains',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDomainsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_domains(
        self,
        project: str,
        request: main_models.ListDomainsRequest,
    ) -> main_models.ListDomainsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_domains_with_options(project, request, headers, runtime)

    async def list_domains_async(
        self,
        project: str,
        request: main_models.ListDomainsRequest,
    ) -> main_models.ListDomainsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_domains_with_options_async(project, request, headers, runtime)

    def list_download_jobs_with_options(
        self,
        project: str,
        request: main_models.ListDownloadJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDownloadJobsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.logstore):
            query['logstore'] = request.logstore
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDownloadJobs',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/downloadjobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDownloadJobsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_download_jobs_with_options_async(
        self,
        project: str,
        request: main_models.ListDownloadJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDownloadJobsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.logstore):
            query['logstore'] = request.logstore
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDownloadJobs',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/downloadjobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDownloadJobsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_download_jobs(
        self,
        project: str,
        request: main_models.ListDownloadJobsRequest,
    ) -> main_models.ListDownloadJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_download_jobs_with_options(project, request, headers, runtime)

    async def list_download_jobs_async(
        self,
        project: str,
        request: main_models.ListDownloadJobsRequest,
    ) -> main_models.ListDownloadJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_download_jobs_with_options_async(project, request, headers, runtime)

    def list_etls_with_options(
        self,
        project: str,
        request: main_models.ListETLsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListETLsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.logstore):
            query['logstore'] = request.logstore
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListETLs',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/etls',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListETLsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_etls_with_options_async(
        self,
        project: str,
        request: main_models.ListETLsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListETLsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.logstore):
            query['logstore'] = request.logstore
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListETLs',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/etls',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListETLsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_etls(
        self,
        project: str,
        request: main_models.ListETLsRequest,
    ) -> main_models.ListETLsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_etls_with_options(project, request, headers, runtime)

    async def list_etls_async(
        self,
        project: str,
        request: main_models.ListETLsRequest,
    ) -> main_models.ListETLsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_etls_with_options_async(project, request, headers, runtime)

    def list_elasticsearch_ingestions_with_options(
        self,
        project: str,
        request: main_models.ListElasticsearchIngestionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListElasticsearchIngestionsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.logstore):
            query['logstore'] = request.logstore
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListElasticsearchIngestions',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/elasticsearchingestions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListElasticsearchIngestionsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_elasticsearch_ingestions_with_options_async(
        self,
        project: str,
        request: main_models.ListElasticsearchIngestionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListElasticsearchIngestionsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.logstore):
            query['logstore'] = request.logstore
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListElasticsearchIngestions',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/elasticsearchingestions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListElasticsearchIngestionsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_elasticsearch_ingestions(
        self,
        project: str,
        request: main_models.ListElasticsearchIngestionsRequest,
    ) -> main_models.ListElasticsearchIngestionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_elasticsearch_ingestions_with_options(project, request, headers, runtime)

    async def list_elasticsearch_ingestions_async(
        self,
        project: str,
        request: main_models.ListElasticsearchIngestionsRequest,
    ) -> main_models.ListElasticsearchIngestionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_elasticsearch_ingestions_with_options_async(project, request, headers, runtime)

    def list_ingest_processors_with_options(
        self,
        project: str,
        request: main_models.ListIngestProcessorsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIngestProcessorsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.display_name):
            query['displayName'] = request.display_name
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.processor_name):
            query['processorName'] = request.processor_name
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIngestProcessors',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ingestprocessors',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIngestProcessorsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_ingest_processors_with_options_async(
        self,
        project: str,
        request: main_models.ListIngestProcessorsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIngestProcessorsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.display_name):
            query['displayName'] = request.display_name
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.processor_name):
            query['processorName'] = request.processor_name
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIngestProcessors',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ingestprocessors',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIngestProcessorsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_ingest_processors(
        self,
        project: str,
        request: main_models.ListIngestProcessorsRequest,
    ) -> main_models.ListIngestProcessorsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_ingest_processors_with_options(project, request, headers, runtime)

    async def list_ingest_processors_async(
        self,
        project: str,
        request: main_models.ListIngestProcessorsRequest,
    ) -> main_models.ListIngestProcessorsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_ingest_processors_with_options_async(project, request, headers, runtime)

    def list_log_stores_with_options(
        self,
        project: str,
        request: main_models.ListLogStoresRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLogStoresResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.logstore_name):
            query['logstoreName'] = request.logstore_name
        if not DaraCore.is_null(request.mode):
            query['mode'] = request.mode
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.telemetry_type):
            query['telemetryType'] = request.telemetry_type
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLogStores',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLogStoresResponse(),
            self.execute(params, req, runtime)
        )

    async def list_log_stores_with_options_async(
        self,
        project: str,
        request: main_models.ListLogStoresRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLogStoresResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.logstore_name):
            query['logstoreName'] = request.logstore_name
        if not DaraCore.is_null(request.mode):
            query['mode'] = request.mode
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.telemetry_type):
            query['telemetryType'] = request.telemetry_type
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLogStores',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLogStoresResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_log_stores(
        self,
        project: str,
        request: main_models.ListLogStoresRequest,
    ) -> main_models.ListLogStoresResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_log_stores_with_options(project, request, headers, runtime)

    async def list_log_stores_async(
        self,
        project: str,
        request: main_models.ListLogStoresRequest,
    ) -> main_models.ListLogStoresResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_log_stores_with_options_async(project, request, headers, runtime)

    def list_logtail_pipeline_config_with_options(
        self,
        project: str,
        request: main_models.ListLogtailPipelineConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLogtailPipelineConfigResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.config_name):
            query['configName'] = request.config_name
        if not DaraCore.is_null(request.config_type):
            query['configType'] = request.config_type
        if not DaraCore.is_null(request.logstore_name):
            query['logstoreName'] = request.logstore_name
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLogtailPipelineConfig',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/pipelineconfigs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLogtailPipelineConfigResponse(),
            self.execute(params, req, runtime)
        )

    async def list_logtail_pipeline_config_with_options_async(
        self,
        project: str,
        request: main_models.ListLogtailPipelineConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLogtailPipelineConfigResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.config_name):
            query['configName'] = request.config_name
        if not DaraCore.is_null(request.config_type):
            query['configType'] = request.config_type
        if not DaraCore.is_null(request.logstore_name):
            query['logstoreName'] = request.logstore_name
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLogtailPipelineConfig',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/pipelineconfigs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLogtailPipelineConfigResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_logtail_pipeline_config(
        self,
        project: str,
        request: main_models.ListLogtailPipelineConfigRequest,
    ) -> main_models.ListLogtailPipelineConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_logtail_pipeline_config_with_options(project, request, headers, runtime)

    async def list_logtail_pipeline_config_async(
        self,
        project: str,
        request: main_models.ListLogtailPipelineConfigRequest,
    ) -> main_models.ListLogtailPipelineConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_logtail_pipeline_config_with_options_async(project, request, headers, runtime)

    def list_machine_group_with_options(
        self,
        project: str,
        request: main_models.ListMachineGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMachineGroupResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['groupName'] = request.group_name
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMachineGroup',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/machinegroups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMachineGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def list_machine_group_with_options_async(
        self,
        project: str,
        request: main_models.ListMachineGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMachineGroupResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['groupName'] = request.group_name
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMachineGroup',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/machinegroups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMachineGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_machine_group(
        self,
        project: str,
        request: main_models.ListMachineGroupRequest,
    ) -> main_models.ListMachineGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_machine_group_with_options(project, request, headers, runtime)

    async def list_machine_group_async(
        self,
        project: str,
        request: main_models.ListMachineGroupRequest,
    ) -> main_models.ListMachineGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_machine_group_with_options_async(project, request, headers, runtime)

    def list_machines_with_options(
        self,
        project: str,
        machine_group: str,
        request: main_models.ListMachinesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMachinesResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMachines',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/machinegroups/{machine_group}/machines',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMachinesResponse(),
            self.execute(params, req, runtime)
        )

    async def list_machines_with_options_async(
        self,
        project: str,
        machine_group: str,
        request: main_models.ListMachinesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMachinesResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMachines',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/machinegroups/{machine_group}/machines',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMachinesResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_machines(
        self,
        project: str,
        machine_group: str,
        request: main_models.ListMachinesRequest,
    ) -> main_models.ListMachinesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_machines_with_options(project, machine_group, request, headers, runtime)

    async def list_machines_async(
        self,
        project: str,
        machine_group: str,
        request: main_models.ListMachinesRequest,
    ) -> main_models.ListMachinesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_machines_with_options_async(project, machine_group, request, headers, runtime)

    def list_materialized_view_with_options(
        self,
        project: str,
        request: main_models.ListMaterializedViewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMaterializedViewResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMaterializedView',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/materializedviews',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMaterializedViewResponse(),
            self.execute(params, req, runtime)
        )

    async def list_materialized_view_with_options_async(
        self,
        project: str,
        request: main_models.ListMaterializedViewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMaterializedViewResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMaterializedView',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/materializedviews',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMaterializedViewResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_materialized_view(
        self,
        project: str,
        request: main_models.ListMaterializedViewRequest,
    ) -> main_models.ListMaterializedViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_materialized_view_with_options(project, request, headers, runtime)

    async def list_materialized_view_async(
        self,
        project: str,
        request: main_models.ListMaterializedViewRequest,
    ) -> main_models.ListMaterializedViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_materialized_view_with_options_async(project, request, headers, runtime)

    def list_materialized_views_with_options(
        self,
        project: str,
        request: main_models.ListMaterializedViewsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMaterializedViewsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMaterializedViews',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/materializedviews',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMaterializedViewsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_materialized_views_with_options_async(
        self,
        project: str,
        request: main_models.ListMaterializedViewsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMaterializedViewsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMaterializedViews',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/materializedviews',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMaterializedViewsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_materialized_views(
        self,
        project: str,
        request: main_models.ListMaterializedViewsRequest,
    ) -> main_models.ListMaterializedViewsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_materialized_views_with_options(project, request, headers, runtime)

    async def list_materialized_views_async(
        self,
        project: str,
        request: main_models.ListMaterializedViewsRequest,
    ) -> main_models.ListMaterializedViewsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_materialized_views_with_options_async(project, request, headers, runtime)

    def list_max_compute_exports_with_options(
        self,
        project: str,
        request: main_models.ListMaxComputeExportsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMaxComputeExportsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.logstore):
            query['logstore'] = request.logstore
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMaxComputeExports',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/maxcomputeexports',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMaxComputeExportsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_max_compute_exports_with_options_async(
        self,
        project: str,
        request: main_models.ListMaxComputeExportsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMaxComputeExportsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.logstore):
            query['logstore'] = request.logstore
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMaxComputeExports',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/maxcomputeexports',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMaxComputeExportsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_max_compute_exports(
        self,
        project: str,
        request: main_models.ListMaxComputeExportsRequest,
    ) -> main_models.ListMaxComputeExportsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_max_compute_exports_with_options(project, request, headers, runtime)

    async def list_max_compute_exports_async(
        self,
        project: str,
        request: main_models.ListMaxComputeExportsRequest,
    ) -> main_models.ListMaxComputeExportsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_max_compute_exports_with_options_async(project, request, headers, runtime)

    def list_metric_stores_with_options(
        self,
        project: str,
        request: main_models.ListMetricStoresRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMetricStoresResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.mode):
            query['mode'] = request.mode
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMetricStores',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/metricstores',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'none',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMetricStoresResponse(),
            self.execute(params, req, runtime)
        )

    async def list_metric_stores_with_options_async(
        self,
        project: str,
        request: main_models.ListMetricStoresRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMetricStoresResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.mode):
            query['mode'] = request.mode
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMetricStores',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/metricstores',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'none',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMetricStoresResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_metric_stores(
        self,
        project: str,
        request: main_models.ListMetricStoresRequest,
    ) -> main_models.ListMetricStoresResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_metric_stores_with_options(project, request, headers, runtime)

    async def list_metric_stores_async(
        self,
        project: str,
        request: main_models.ListMetricStoresRequest,
    ) -> main_models.ListMetricStoresResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_metric_stores_with_options_async(project, request, headers, runtime)

    def list_ossexports_with_options(
        self,
        project: str,
        request: main_models.ListOSSExportsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListOSSExportsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.logstore):
            query['logstore'] = request.logstore
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOSSExports',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ossexports',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOSSExportsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_ossexports_with_options_async(
        self,
        project: str,
        request: main_models.ListOSSExportsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListOSSExportsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.logstore):
            query['logstore'] = request.logstore
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOSSExports',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ossexports',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOSSExportsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_ossexports(
        self,
        project: str,
        request: main_models.ListOSSExportsRequest,
    ) -> main_models.ListOSSExportsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_ossexports_with_options(project, request, headers, runtime)

    async def list_ossexports_async(
        self,
        project: str,
        request: main_models.ListOSSExportsRequest,
    ) -> main_models.ListOSSExportsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_ossexports_with_options_async(project, request, headers, runtime)

    def list_osshdfsexports_with_options(
        self,
        project: str,
        request: main_models.ListOSSHDFSExportsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListOSSHDFSExportsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.logstore):
            query['logstore'] = request.logstore
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOSSHDFSExports',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/osshdfsexports',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOSSHDFSExportsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_osshdfsexports_with_options_async(
        self,
        project: str,
        request: main_models.ListOSSHDFSExportsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListOSSHDFSExportsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.logstore):
            query['logstore'] = request.logstore
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOSSHDFSExports',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/osshdfsexports',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOSSHDFSExportsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_osshdfsexports(
        self,
        project: str,
        request: main_models.ListOSSHDFSExportsRequest,
    ) -> main_models.ListOSSHDFSExportsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_osshdfsexports_with_options(project, request, headers, runtime)

    async def list_osshdfsexports_async(
        self,
        project: str,
        request: main_models.ListOSSHDFSExportsRequest,
    ) -> main_models.ListOSSHDFSExportsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_osshdfsexports_with_options_async(project, request, headers, runtime)

    def list_ossingestions_with_options(
        self,
        project: str,
        request: main_models.ListOSSIngestionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListOSSIngestionsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.logstore):
            query['logstore'] = request.logstore
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOSSIngestions',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ossingestions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOSSIngestionsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_ossingestions_with_options_async(
        self,
        project: str,
        request: main_models.ListOSSIngestionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListOSSIngestionsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.logstore):
            query['logstore'] = request.logstore
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOSSIngestions',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ossingestions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOSSIngestionsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_ossingestions(
        self,
        project: str,
        request: main_models.ListOSSIngestionsRequest,
    ) -> main_models.ListOSSIngestionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_ossingestions_with_options(project, request, headers, runtime)

    async def list_ossingestions_async(
        self,
        project: str,
        request: main_models.ListOSSIngestionsRequest,
    ) -> main_models.ListOSSIngestionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_ossingestions_with_options_async(project, request, headers, runtime)

    def list_project_with_options(
        self,
        request: main_models.ListProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.fetch_quota):
            query['fetchQuota'] = request.fetch_quota
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.project_name):
            query['projectName'] = request.project_name
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProject',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectResponse(),
            self.execute(params, req, runtime)
        )

    async def list_project_with_options_async(
        self,
        request: main_models.ListProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.fetch_quota):
            query['fetchQuota'] = request.fetch_quota
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.project_name):
            query['projectName'] = request.project_name
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProject',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_project(
        self,
        request: main_models.ListProjectRequest,
    ) -> main_models.ListProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_project_with_options(request, headers, runtime)

    async def list_project_async(
        self,
        request: main_models.ListProjectRequest,
    ) -> main_models.ListProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_project_with_options_async(request, headers, runtime)

    def list_s3ingestions_with_options(
        self,
        project: str,
        request: main_models.ListS3IngestionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListS3IngestionsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.logstore):
            query['logstore'] = request.logstore
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListS3Ingestions',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/s3ingestions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListS3IngestionsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_s3ingestions_with_options_async(
        self,
        project: str,
        request: main_models.ListS3IngestionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListS3IngestionsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.logstore):
            query['logstore'] = request.logstore
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListS3Ingestions',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/s3ingestions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListS3IngestionsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_s3ingestions(
        self,
        project: str,
        request: main_models.ListS3IngestionsRequest,
    ) -> main_models.ListS3IngestionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_s3ingestions_with_options(project, request, headers, runtime)

    async def list_s3ingestions_async(
        self,
        project: str,
        request: main_models.ListS3IngestionsRequest,
    ) -> main_models.ListS3IngestionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_s3ingestions_with_options_async(project, request, headers, runtime)

    def list_saved_search_with_options(
        self,
        project: str,
        request: main_models.ListSavedSearchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSavedSearchResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSavedSearch',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/savedsearches',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSavedSearchResponse(),
            self.execute(params, req, runtime)
        )

    async def list_saved_search_with_options_async(
        self,
        project: str,
        request: main_models.ListSavedSearchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSavedSearchResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSavedSearch',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/savedsearches',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSavedSearchResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_saved_search(
        self,
        project: str,
        request: main_models.ListSavedSearchRequest,
    ) -> main_models.ListSavedSearchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_saved_search_with_options(project, request, headers, runtime)

    async def list_saved_search_async(
        self,
        project: str,
        request: main_models.ListSavedSearchRequest,
    ) -> main_models.ListSavedSearchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_saved_search_with_options_async(project, request, headers, runtime)

    def list_scheduled_sqls_with_options(
        self,
        project: str,
        request: main_models.ListScheduledSQLsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListScheduledSQLsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.logstore):
            query['logstore'] = request.logstore
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScheduledSQLs',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/scheduledsqls',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScheduledSQLsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_scheduled_sqls_with_options_async(
        self,
        project: str,
        request: main_models.ListScheduledSQLsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListScheduledSQLsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.logstore):
            query['logstore'] = request.logstore
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScheduledSQLs',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/scheduledsqls',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScheduledSQLsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_scheduled_sqls(
        self,
        project: str,
        request: main_models.ListScheduledSQLsRequest,
    ) -> main_models.ListScheduledSQLsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_scheduled_sqls_with_options(project, request, headers, runtime)

    async def list_scheduled_sqls_async(
        self,
        project: str,
        request: main_models.ListScheduledSQLsRequest,
    ) -> main_models.ListScheduledSQLsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_scheduled_sqls_with_options_async(project, request, headers, runtime)

    def list_shards_with_options(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListShardsResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListShards',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/shards',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.ListShardsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_shards_with_options_async(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListShardsResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListShards',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/shards',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.ListShardsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_shards(
        self,
        project: str,
        logstore: str,
    ) -> main_models.ListShardsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_shards_with_options(project, logstore, headers, runtime)

    async def list_shards_async(
        self,
        project: str,
        logstore: str,
    ) -> main_models.ListShardsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_shards_with_options_async(project, logstore, headers, runtime)

    def list_store_views_with_options(
        self,
        project: str,
        request: main_models.ListStoreViewsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListStoreViewsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.store_type):
            query['storeType'] = request.store_type
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStoreViews',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/storeviews',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStoreViewsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_store_views_with_options_async(
        self,
        project: str,
        request: main_models.ListStoreViewsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListStoreViewsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.offset):
            query['offset'] = request.offset
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.store_type):
            query['storeType'] = request.store_type
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStoreViews',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/storeviews',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStoreViewsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_store_views(
        self,
        project: str,
        request: main_models.ListStoreViewsRequest,
    ) -> main_models.ListStoreViewsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_store_views_with_options(project, request, headers, runtime)

    async def list_store_views_async(
        self,
        project: str,
        request: main_models.ListStoreViewsRequest,
    ) -> main_models.ListStoreViewsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_store_views_with_options_async(project, request, headers, runtime)

    def list_tag_resources_with_options(
        self,
        tmp_req: main_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        tmp_req.validate()
        request = main_models.ListTagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id):
            request.resource_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id, 'resourceId', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not DaraCore.is_null(request.resource_id_shrink):
            query['resourceId'] = request.resource_id_shrink
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/tags',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.execute(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        tmp_req: main_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        tmp_req.validate()
        request = main_models.ListTagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id):
            request.resource_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id, 'resourceId', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not DaraCore.is_null(request.resource_id_shrink):
            query['resourceId'] = request.resource_id_shrink
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/tags',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_tag_resources_with_options_async(request, headers, runtime)

    def merge_shard_with_options(
        self,
        project: str,
        logstore: str,
        shard: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.MergeShardResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'MergeShard',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/shards/{shard}?action=merge',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.MergeShardResponse(),
            self.execute(params, req, runtime)
        )

    async def merge_shard_with_options_async(
        self,
        project: str,
        logstore: str,
        shard: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.MergeShardResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'MergeShard',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/shards/{shard}?action=merge',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.MergeShardResponse(),
            await self.execute_async(params, req, runtime)
        )

    def merge_shard(
        self,
        project: str,
        logstore: str,
        shard: str,
    ) -> main_models.MergeShardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.merge_shard_with_options(project, logstore, shard, headers, runtime)

    async def merge_shard_async(
        self,
        project: str,
        logstore: str,
        shard: str,
    ) -> main_models.MergeShardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.merge_shard_with_options_async(project, logstore, shard, headers, runtime)

    def open_sls_service_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OpenSlsServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'OpenSlsService',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/slsservice',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.OpenSlsServiceResponse(),
            self.execute(params, req, runtime)
        )

    async def open_sls_service_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OpenSlsServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'OpenSlsService',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/slsservice',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.OpenSlsServiceResponse(),
            await self.execute_async(params, req, runtime)
        )

    def open_sls_service(self) -> main_models.OpenSlsServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.open_sls_service_with_options(headers, runtime)

    async def open_sls_service_async(self) -> main_models.OpenSlsServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.open_sls_service_with_options_async(headers, runtime)

    def pull_logs_with_options(
        self,
        project: str,
        log_store: str,
        shard_id: str,
        request: main_models.PullLogsRequest,
        headers: main_models.PullLogsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PullLogsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.count):
            query['count'] = request.count
        if not DaraCore.is_null(request.cursor):
            query['cursor'] = request.cursor
        if not DaraCore.is_null(request.end_cursor):
            query['end_cursor'] = request.end_cursor
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.accept_encoding):
            real_headers['Accept-Encoding'] = str(headers.accept_encoding)
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PullLogs',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{log_store}/shards/{shard_id}?type=log',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'none',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PullLogsResponse(),
            self.execute(params, req, runtime)
        )

    async def pull_logs_with_options_async(
        self,
        project: str,
        log_store: str,
        shard_id: str,
        request: main_models.PullLogsRequest,
        headers: main_models.PullLogsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PullLogsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.count):
            query['count'] = request.count
        if not DaraCore.is_null(request.cursor):
            query['cursor'] = request.cursor
        if not DaraCore.is_null(request.end_cursor):
            query['end_cursor'] = request.end_cursor
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.accept_encoding):
            real_headers['Accept-Encoding'] = str(headers.accept_encoding)
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PullLogs',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{log_store}/shards/{shard_id}?type=log',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'none',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PullLogsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def pull_logs(
        self,
        project: str,
        log_store: str,
        shard_id: str,
        request: main_models.PullLogsRequest,
    ) -> main_models.PullLogsResponse:
        runtime = RuntimeOptions()
        headers = main_models.PullLogsHeaders()
        return self.pull_logs_with_options(project, log_store, shard_id, request, headers, runtime)

    async def pull_logs_async(
        self,
        project: str,
        log_store: str,
        shard_id: str,
        request: main_models.PullLogsRequest,
    ) -> main_models.PullLogsResponse:
        runtime = RuntimeOptions()
        headers = main_models.PullLogsHeaders()
        return await self.pull_logs_with_options_async(project, log_store, shard_id, request, headers, runtime)

    def put_annotation_data_with_options(
        self,
        dataset_id: str,
        request: main_models.PutAnnotationDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PutAnnotationDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotationdata_id):
            query['annotationdataId'] = request.annotationdata_id
        body = {}
        if not DaraCore.is_null(request.ml_data_param):
            body['mlDataParam'] = request.ml_data_param
        if not DaraCore.is_null(request.raw_log):
            body['rawLog'] = request.raw_log
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PutAnnotationData',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/annotationdataset/{dataset_id}/annotationdata',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PutAnnotationDataResponse(),
            self.execute(params, req, runtime)
        )

    async def put_annotation_data_with_options_async(
        self,
        dataset_id: str,
        request: main_models.PutAnnotationDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PutAnnotationDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotationdata_id):
            query['annotationdataId'] = request.annotationdata_id
        body = {}
        if not DaraCore.is_null(request.ml_data_param):
            body['mlDataParam'] = request.ml_data_param
        if not DaraCore.is_null(request.raw_log):
            body['rawLog'] = request.raw_log
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PutAnnotationData',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/annotationdataset/{dataset_id}/annotationdata',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PutAnnotationDataResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_annotation_data(
        self,
        dataset_id: str,
        request: main_models.PutAnnotationDataRequest,
    ) -> main_models.PutAnnotationDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.put_annotation_data_with_options(dataset_id, request, headers, runtime)

    async def put_annotation_data_async(
        self,
        dataset_id: str,
        request: main_models.PutAnnotationDataRequest,
    ) -> main_models.PutAnnotationDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.put_annotation_data_with_options_async(dataset_id, request, headers, runtime)

    def put_consume_processor_with_options(
        self,
        project: str,
        processor_name: str,
        request: main_models.PutConsumeProcessorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PutConsumeProcessorResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PutConsumeProcessor',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/consumeprocessors/{processor_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PutConsumeProcessorResponse(),
            self.execute(params, req, runtime)
        )

    async def put_consume_processor_with_options_async(
        self,
        project: str,
        processor_name: str,
        request: main_models.PutConsumeProcessorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PutConsumeProcessorResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PutConsumeProcessor',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/consumeprocessors/{processor_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PutConsumeProcessorResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_consume_processor(
        self,
        project: str,
        processor_name: str,
        request: main_models.PutConsumeProcessorRequest,
    ) -> main_models.PutConsumeProcessorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.put_consume_processor_with_options(project, processor_name, request, headers, runtime)

    async def put_consume_processor_async(
        self,
        project: str,
        processor_name: str,
        request: main_models.PutConsumeProcessorRequest,
    ) -> main_models.PutConsumeProcessorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.put_consume_processor_with_options_async(project, processor_name, request, headers, runtime)

    def put_ingest_processor_with_options(
        self,
        project: str,
        processor_name: str,
        request: main_models.PutIngestProcessorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PutIngestProcessorResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PutIngestProcessor',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ingestprocessors/{processor_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PutIngestProcessorResponse(),
            self.execute(params, req, runtime)
        )

    async def put_ingest_processor_with_options_async(
        self,
        project: str,
        processor_name: str,
        request: main_models.PutIngestProcessorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PutIngestProcessorResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PutIngestProcessor',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ingestprocessors/{processor_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PutIngestProcessorResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_ingest_processor(
        self,
        project: str,
        processor_name: str,
        request: main_models.PutIngestProcessorRequest,
    ) -> main_models.PutIngestProcessorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.put_ingest_processor_with_options(project, processor_name, request, headers, runtime)

    async def put_ingest_processor_async(
        self,
        project: str,
        processor_name: str,
        request: main_models.PutIngestProcessorRequest,
    ) -> main_models.PutIngestProcessorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.put_ingest_processor_with_options_async(project, processor_name, request, headers, runtime)

    def put_logs_with_options(
        self,
        project: str,
        logstore: str,
        request: main_models.PutLogsRequest,
        headers: main_models.PutLogsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PutLogsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_log_compresstype):
            real_headers['x-log-compresstype'] = str(headers.x_log_compresstype)
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'PutLogs',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/shards/lb',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'protobuf',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PutLogsResponse(),
            self.execute(params, req, runtime)
        )

    async def put_logs_with_options_async(
        self,
        project: str,
        logstore: str,
        request: main_models.PutLogsRequest,
        headers: main_models.PutLogsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PutLogsResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.x_log_compresstype):
            real_headers['x-log-compresstype'] = str(headers.x_log_compresstype)
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'PutLogs',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/shards/lb',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'protobuf',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PutLogsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_logs(
        self,
        project: str,
        logstore: str,
        request: main_models.PutLogsRequest,
    ) -> main_models.PutLogsResponse:
        runtime = RuntimeOptions()
        headers = main_models.PutLogsHeaders()
        return self.put_logs_with_options(project, logstore, request, headers, runtime)

    async def put_logs_async(
        self,
        project: str,
        logstore: str,
        request: main_models.PutLogsRequest,
    ) -> main_models.PutLogsResponse:
        runtime = RuntimeOptions()
        headers = main_models.PutLogsHeaders()
        return await self.put_logs_with_options_async(project, logstore, request, headers, runtime)

    def put_project_policy_with_options(
        self,
        project: str,
        request: main_models.PutProjectPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PutProjectPolicyResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'PutProjectPolicy',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/policy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PutProjectPolicyResponse(),
            self.execute(params, req, runtime)
        )

    async def put_project_policy_with_options_async(
        self,
        project: str,
        request: main_models.PutProjectPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PutProjectPolicyResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'PutProjectPolicy',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/policy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PutProjectPolicyResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_project_policy(
        self,
        project: str,
        request: main_models.PutProjectPolicyRequest,
    ) -> main_models.PutProjectPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.put_project_policy_with_options(project, request, headers, runtime)

    async def put_project_policy_async(
        self,
        project: str,
        request: main_models.PutProjectPolicyRequest,
    ) -> main_models.PutProjectPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.put_project_policy_with_options_async(project, request, headers, runtime)

    def put_project_transfer_acceleration_with_options(
        self,
        project: str,
        request: main_models.PutProjectTransferAccelerationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PutProjectTransferAccelerationResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.enabled):
            body['enabled'] = request.enabled
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PutProjectTransferAcceleration',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/transferacceleration',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PutProjectTransferAccelerationResponse(),
            self.execute(params, req, runtime)
        )

    async def put_project_transfer_acceleration_with_options_async(
        self,
        project: str,
        request: main_models.PutProjectTransferAccelerationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PutProjectTransferAccelerationResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.enabled):
            body['enabled'] = request.enabled
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PutProjectTransferAcceleration',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/transferacceleration',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PutProjectTransferAccelerationResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_project_transfer_acceleration(
        self,
        project: str,
        request: main_models.PutProjectTransferAccelerationRequest,
    ) -> main_models.PutProjectTransferAccelerationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.put_project_transfer_acceleration_with_options(project, request, headers, runtime)

    async def put_project_transfer_acceleration_async(
        self,
        project: str,
        request: main_models.PutProjectTransferAccelerationRequest,
    ) -> main_models.PutProjectTransferAccelerationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.put_project_transfer_acceleration_with_options_async(project, request, headers, runtime)

    def put_webtracking_with_options(
        self,
        project: str,
        logstore_name: str,
        request: main_models.PutWebtrackingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PutWebtrackingResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.logs):
            body['__logs__'] = request.logs
        if not DaraCore.is_null(request.source):
            body['__source__'] = request.source
        if not DaraCore.is_null(request.tags):
            body['__tags__'] = request.tags
        if not DaraCore.is_null(request.topic):
            body['__topic__'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PutWebtracking',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore_name}/track',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PutWebtrackingResponse(),
            self.execute(params, req, runtime)
        )

    async def put_webtracking_with_options_async(
        self,
        project: str,
        logstore_name: str,
        request: main_models.PutWebtrackingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PutWebtrackingResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.logs):
            body['__logs__'] = request.logs
        if not DaraCore.is_null(request.source):
            body['__source__'] = request.source
        if not DaraCore.is_null(request.tags):
            body['__tags__'] = request.tags
        if not DaraCore.is_null(request.topic):
            body['__topic__'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PutWebtracking',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore_name}/track',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PutWebtrackingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_webtracking(
        self,
        project: str,
        logstore_name: str,
        request: main_models.PutWebtrackingRequest,
    ) -> main_models.PutWebtrackingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.put_webtracking_with_options(project, logstore_name, request, headers, runtime)

    async def put_webtracking_async(
        self,
        project: str,
        logstore_name: str,
        request: main_models.PutWebtrackingRequest,
    ) -> main_models.PutWebtrackingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.put_webtracking_with_options_async(project, logstore_name, request, headers, runtime)

    def refresh_token_with_options(
        self,
        request: main_models.RefreshTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RefreshTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_token_expiration_time):
            query['accessTokenExpirationTime'] = request.access_token_expiration_time
        if not DaraCore.is_null(request.ticket):
            query['ticket'] = request.ticket
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshToken',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/token/refresh',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshTokenResponse(),
            self.execute(params, req, runtime)
        )

    async def refresh_token_with_options_async(
        self,
        request: main_models.RefreshTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RefreshTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_token_expiration_time):
            query['accessTokenExpirationTime'] = request.access_token_expiration_time
        if not DaraCore.is_null(request.ticket):
            query['ticket'] = request.ticket
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshToken',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/token/refresh',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshTokenResponse(),
            await self.execute_async(params, req, runtime)
        )

    def refresh_token(
        self,
        request: main_models.RefreshTokenRequest,
    ) -> main_models.RefreshTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.refresh_token_with_options(request, headers, runtime)

    async def refresh_token_async(
        self,
        request: main_models.RefreshTokenRequest,
    ) -> main_models.RefreshTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.refresh_token_with_options_async(request, headers, runtime)

    def remove_config_from_machine_group_with_options(
        self,
        project: str,
        machine_group: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveConfigFromMachineGroupResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveConfigFromMachineGroup',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/machinegroups/{machine_group}/configs/{config_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.RemoveConfigFromMachineGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def remove_config_from_machine_group_with_options_async(
        self,
        project: str,
        machine_group: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveConfigFromMachineGroupResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveConfigFromMachineGroup',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/machinegroups/{machine_group}/configs/{config_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.RemoveConfigFromMachineGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def remove_config_from_machine_group(
        self,
        project: str,
        machine_group: str,
        config_name: str,
    ) -> main_models.RemoveConfigFromMachineGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.remove_config_from_machine_group_with_options(project, machine_group, config_name, headers, runtime)

    async def remove_config_from_machine_group_async(
        self,
        project: str,
        machine_group: str,
        config_name: str,
    ) -> main_models.RemoveConfigFromMachineGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.remove_config_from_machine_group_with_options_async(project, machine_group, config_name, headers, runtime)

    def split_shard_with_options(
        self,
        project: str,
        logstore: str,
        shard: str,
        request: main_models.SplitShardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SplitShardResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.key):
            query['key'] = request.key
        if not DaraCore.is_null(request.shard_count):
            query['shardCount'] = request.shard_count
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SplitShard',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/shards/{shard}?action=split',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.SplitShardResponse(),
            self.execute(params, req, runtime)
        )

    async def split_shard_with_options_async(
        self,
        project: str,
        logstore: str,
        shard: str,
        request: main_models.SplitShardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SplitShardResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.key):
            query['key'] = request.key
        if not DaraCore.is_null(request.shard_count):
            query['shardCount'] = request.shard_count
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SplitShard',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/shards/{shard}?action=split',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.SplitShardResponse(),
            await self.execute_async(params, req, runtime)
        )

    def split_shard(
        self,
        project: str,
        logstore: str,
        shard: str,
        request: main_models.SplitShardRequest,
    ) -> main_models.SplitShardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.split_shard_with_options(project, logstore, shard, request, headers, runtime)

    async def split_shard_async(
        self,
        project: str,
        logstore: str,
        shard: str,
        request: main_models.SplitShardRequest,
    ) -> main_models.SplitShardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.split_shard_with_options_async(project, logstore, shard, request, headers, runtime)

    def start_azure_blob_ingestion_with_options(
        self,
        project: str,
        azure_blob_ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartAzureBlobIngestionResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StartAzureBlobIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/azureblobingestions/{azure_blob_ingestion_name}?action=START',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StartAzureBlobIngestionResponse(),
            self.execute(params, req, runtime)
        )

    async def start_azure_blob_ingestion_with_options_async(
        self,
        project: str,
        azure_blob_ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartAzureBlobIngestionResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StartAzureBlobIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/azureblobingestions/{azure_blob_ingestion_name}?action=START',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StartAzureBlobIngestionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def start_azure_blob_ingestion(
        self,
        project: str,
        azure_blob_ingestion_name: str,
    ) -> main_models.StartAzureBlobIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_azure_blob_ingestion_with_options(project, azure_blob_ingestion_name, headers, runtime)

    async def start_azure_blob_ingestion_async(
        self,
        project: str,
        azure_blob_ingestion_name: str,
    ) -> main_models.StartAzureBlobIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_azure_blob_ingestion_with_options_async(project, azure_blob_ingestion_name, headers, runtime)

    def start_etlwith_options(
        self,
        project: str,
        etl_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartETLResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StartETL',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/etls/{etl_name}?action=START',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StartETLResponse(),
            self.execute(params, req, runtime)
        )

    async def start_etlwith_options_async(
        self,
        project: str,
        etl_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartETLResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StartETL',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/etls/{etl_name}?action=START',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StartETLResponse(),
            await self.execute_async(params, req, runtime)
        )

    def start_etl(
        self,
        project: str,
        etl_name: str,
    ) -> main_models.StartETLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_etlwith_options(project, etl_name, headers, runtime)

    async def start_etl_async(
        self,
        project: str,
        etl_name: str,
    ) -> main_models.StartETLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_etlwith_options_async(project, etl_name, headers, runtime)

    def start_elasticsearch_ingestion_with_options(
        self,
        project: str,
        elasticsearch_ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartElasticsearchIngestionResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StartElasticsearchIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/elasticsearchingestions/{elasticsearch_ingestion_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StartElasticsearchIngestionResponse(),
            self.execute(params, req, runtime)
        )

    async def start_elasticsearch_ingestion_with_options_async(
        self,
        project: str,
        elasticsearch_ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartElasticsearchIngestionResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StartElasticsearchIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/elasticsearchingestions/{elasticsearch_ingestion_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StartElasticsearchIngestionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def start_elasticsearch_ingestion(
        self,
        project: str,
        elasticsearch_ingestion_name: str,
    ) -> main_models.StartElasticsearchIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_elasticsearch_ingestion_with_options(project, elasticsearch_ingestion_name, headers, runtime)

    async def start_elasticsearch_ingestion_async(
        self,
        project: str,
        elasticsearch_ingestion_name: str,
    ) -> main_models.StartElasticsearchIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_elasticsearch_ingestion_with_options_async(project, elasticsearch_ingestion_name, headers, runtime)

    def start_max_compute_export_with_options(
        self,
        project: str,
        mc_export_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartMaxComputeExportResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StartMaxComputeExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/maxcomputeexports/{mc_export_name}?action=START',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StartMaxComputeExportResponse(),
            self.execute(params, req, runtime)
        )

    async def start_max_compute_export_with_options_async(
        self,
        project: str,
        mc_export_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartMaxComputeExportResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StartMaxComputeExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/maxcomputeexports/{mc_export_name}?action=START',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StartMaxComputeExportResponse(),
            await self.execute_async(params, req, runtime)
        )

    def start_max_compute_export(
        self,
        project: str,
        mc_export_name: str,
    ) -> main_models.StartMaxComputeExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_max_compute_export_with_options(project, mc_export_name, headers, runtime)

    async def start_max_compute_export_async(
        self,
        project: str,
        mc_export_name: str,
    ) -> main_models.StartMaxComputeExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_max_compute_export_with_options_async(project, mc_export_name, headers, runtime)

    def start_ossexport_with_options(
        self,
        project: str,
        oss_export_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartOSSExportResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StartOSSExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ossexports/{oss_export_name}?action=START',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StartOSSExportResponse(),
            self.execute(params, req, runtime)
        )

    async def start_ossexport_with_options_async(
        self,
        project: str,
        oss_export_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartOSSExportResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StartOSSExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ossexports/{oss_export_name}?action=START',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StartOSSExportResponse(),
            await self.execute_async(params, req, runtime)
        )

    def start_ossexport(
        self,
        project: str,
        oss_export_name: str,
    ) -> main_models.StartOSSExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_ossexport_with_options(project, oss_export_name, headers, runtime)

    async def start_ossexport_async(
        self,
        project: str,
        oss_export_name: str,
    ) -> main_models.StartOSSExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_ossexport_with_options_async(project, oss_export_name, headers, runtime)

    def start_osshdfsexport_with_options(
        self,
        project: str,
        oss_export_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartOSSHDFSExportResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StartOSSHDFSExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/osshdfsexports/{oss_export_name}?action=START',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StartOSSHDFSExportResponse(),
            self.execute(params, req, runtime)
        )

    async def start_osshdfsexport_with_options_async(
        self,
        project: str,
        oss_export_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartOSSHDFSExportResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StartOSSHDFSExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/osshdfsexports/{oss_export_name}?action=START',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StartOSSHDFSExportResponse(),
            await self.execute_async(params, req, runtime)
        )

    def start_osshdfsexport(
        self,
        project: str,
        oss_export_name: str,
    ) -> main_models.StartOSSHDFSExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_osshdfsexport_with_options(project, oss_export_name, headers, runtime)

    async def start_osshdfsexport_async(
        self,
        project: str,
        oss_export_name: str,
    ) -> main_models.StartOSSHDFSExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_osshdfsexport_with_options_async(project, oss_export_name, headers, runtime)

    def start_ossingestion_with_options(
        self,
        project: str,
        oss_ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartOSSIngestionResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StartOSSIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ossingestions/{oss_ingestion_name}?action=START',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StartOSSIngestionResponse(),
            self.execute(params, req, runtime)
        )

    async def start_ossingestion_with_options_async(
        self,
        project: str,
        oss_ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartOSSIngestionResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StartOSSIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ossingestions/{oss_ingestion_name}?action=START',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StartOSSIngestionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def start_ossingestion(
        self,
        project: str,
        oss_ingestion_name: str,
    ) -> main_models.StartOSSIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_ossingestion_with_options(project, oss_ingestion_name, headers, runtime)

    async def start_ossingestion_async(
        self,
        project: str,
        oss_ingestion_name: str,
    ) -> main_models.StartOSSIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_ossingestion_with_options_async(project, oss_ingestion_name, headers, runtime)

    def stop_azure_blob_ingestion_with_options(
        self,
        project: str,
        azure_blob_ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopAzureBlobIngestionResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopAzureBlobIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/azureblobingestions/{azure_blob_ingestion_name}?action=STOP',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StopAzureBlobIngestionResponse(),
            self.execute(params, req, runtime)
        )

    async def stop_azure_blob_ingestion_with_options_async(
        self,
        project: str,
        azure_blob_ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopAzureBlobIngestionResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopAzureBlobIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/azureblobingestions/{azure_blob_ingestion_name}?action=STOP',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StopAzureBlobIngestionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def stop_azure_blob_ingestion(
        self,
        project: str,
        azure_blob_ingestion_name: str,
    ) -> main_models.StopAzureBlobIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_azure_blob_ingestion_with_options(project, azure_blob_ingestion_name, headers, runtime)

    async def stop_azure_blob_ingestion_async(
        self,
        project: str,
        azure_blob_ingestion_name: str,
    ) -> main_models.StopAzureBlobIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_azure_blob_ingestion_with_options_async(project, azure_blob_ingestion_name, headers, runtime)

    def stop_etlwith_options(
        self,
        project: str,
        etl_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopETLResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopETL',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/etls/{etl_name}?action=STOP',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StopETLResponse(),
            self.execute(params, req, runtime)
        )

    async def stop_etlwith_options_async(
        self,
        project: str,
        etl_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopETLResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopETL',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/etls/{etl_name}?action=STOP',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StopETLResponse(),
            await self.execute_async(params, req, runtime)
        )

    def stop_etl(
        self,
        project: str,
        etl_name: str,
    ) -> main_models.StopETLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_etlwith_options(project, etl_name, headers, runtime)

    async def stop_etl_async(
        self,
        project: str,
        etl_name: str,
    ) -> main_models.StopETLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_etlwith_options_async(project, etl_name, headers, runtime)

    def stop_elasticsearch_ingestion_with_sse(
        self,
        project: str,
        elasticsearch_ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.StopElasticsearchIngestionResponse, None, None]:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopElasticsearchIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/elasticsearchingestion/{elasticsearch_ingestion_name}?action=STOP',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.StopElasticsearchIngestionResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def stop_elasticsearch_ingestion_with_sse_async(
        self,
        project: str,
        elasticsearch_ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.StopElasticsearchIngestionResponse, None, None]:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopElasticsearchIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/elasticsearchingestion/{elasticsearch_ingestion_name}?action=STOP',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.StopElasticsearchIngestionResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def stop_elasticsearch_ingestion_with_options(
        self,
        project: str,
        elasticsearch_ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopElasticsearchIngestionResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopElasticsearchIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/elasticsearchingestion/{elasticsearch_ingestion_name}?action=STOP',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StopElasticsearchIngestionResponse(),
            self.execute(params, req, runtime)
        )

    async def stop_elasticsearch_ingestion_with_options_async(
        self,
        project: str,
        elasticsearch_ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopElasticsearchIngestionResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopElasticsearchIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/elasticsearchingestion/{elasticsearch_ingestion_name}?action=STOP',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StopElasticsearchIngestionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def stop_elasticsearch_ingestion(
        self,
        project: str,
        elasticsearch_ingestion_name: str,
    ) -> main_models.StopElasticsearchIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_elasticsearch_ingestion_with_options(project, elasticsearch_ingestion_name, headers, runtime)

    async def stop_elasticsearch_ingestion_async(
        self,
        project: str,
        elasticsearch_ingestion_name: str,
    ) -> main_models.StopElasticsearchIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_elasticsearch_ingestion_with_options_async(project, elasticsearch_ingestion_name, headers, runtime)

    def stop_max_compute_export_with_options(
        self,
        project: str,
        mc_export_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopMaxComputeExportResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopMaxComputeExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/maxcomputeexports/{mc_export_name}?action=STOP',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StopMaxComputeExportResponse(),
            self.execute(params, req, runtime)
        )

    async def stop_max_compute_export_with_options_async(
        self,
        project: str,
        mc_export_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopMaxComputeExportResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopMaxComputeExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/maxcomputeexports/{mc_export_name}?action=STOP',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StopMaxComputeExportResponse(),
            await self.execute_async(params, req, runtime)
        )

    def stop_max_compute_export(
        self,
        project: str,
        mc_export_name: str,
    ) -> main_models.StopMaxComputeExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_max_compute_export_with_options(project, mc_export_name, headers, runtime)

    async def stop_max_compute_export_async(
        self,
        project: str,
        mc_export_name: str,
    ) -> main_models.StopMaxComputeExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_max_compute_export_with_options_async(project, mc_export_name, headers, runtime)

    def stop_ossexport_with_options(
        self,
        project: str,
        oss_export_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopOSSExportResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopOSSExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ossexports/{oss_export_name}?action=STOP',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StopOSSExportResponse(),
            self.execute(params, req, runtime)
        )

    async def stop_ossexport_with_options_async(
        self,
        project: str,
        oss_export_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopOSSExportResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopOSSExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ossexports/{oss_export_name}?action=STOP',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StopOSSExportResponse(),
            await self.execute_async(params, req, runtime)
        )

    def stop_ossexport(
        self,
        project: str,
        oss_export_name: str,
    ) -> main_models.StopOSSExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_ossexport_with_options(project, oss_export_name, headers, runtime)

    async def stop_ossexport_async(
        self,
        project: str,
        oss_export_name: str,
    ) -> main_models.StopOSSExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_ossexport_with_options_async(project, oss_export_name, headers, runtime)

    def stop_osshdfsexport_with_options(
        self,
        project: str,
        oss_export_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopOSSHDFSExportResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopOSSHDFSExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/osshdfsexports/{oss_export_name}?action=STOP',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StopOSSHDFSExportResponse(),
            self.execute(params, req, runtime)
        )

    async def stop_osshdfsexport_with_options_async(
        self,
        project: str,
        oss_export_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopOSSHDFSExportResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopOSSHDFSExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/osshdfsexports/{oss_export_name}?action=STOP',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StopOSSHDFSExportResponse(),
            await self.execute_async(params, req, runtime)
        )

    def stop_osshdfsexport(
        self,
        project: str,
        oss_export_name: str,
    ) -> main_models.StopOSSHDFSExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_osshdfsexport_with_options(project, oss_export_name, headers, runtime)

    async def stop_osshdfsexport_async(
        self,
        project: str,
        oss_export_name: str,
    ) -> main_models.StopOSSHDFSExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_osshdfsexport_with_options_async(project, oss_export_name, headers, runtime)

    def stop_ossingestion_with_options(
        self,
        project: str,
        oss_ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopOSSIngestionResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopOSSIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ossingestions/{oss_ingestion_name}?action=STOP',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StopOSSIngestionResponse(),
            self.execute(params, req, runtime)
        )

    async def stop_ossingestion_with_options_async(
        self,
        project: str,
        oss_ingestion_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopOSSIngestionResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopOSSIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ossingestions/{oss_ingestion_name}?action=STOP',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.StopOSSIngestionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def stop_ossingestion(
        self,
        project: str,
        oss_ingestion_name: str,
    ) -> main_models.StopOSSIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_ossingestion_with_options(project, oss_ingestion_name, headers, runtime)

    async def stop_ossingestion_async(
        self,
        project: str,
        oss_ingestion_name: str,
    ) -> main_models.StopOSSIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_ossingestion_with_options_async(project, oss_ingestion_name, headers, runtime)

    def submit_async_sql_with_options(
        self,
        project: str,
        request: main_models.SubmitAsyncSqlRequest,
        headers: main_models.SubmitAsyncSqlHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitAsyncSqlResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.accept):
            real_headers['Accept'] = str(headers.accept)
        if not DaraCore.is_null(headers.accept_encoding):
            real_headers['Accept-Encoding'] = str(headers.accept_encoding)
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitAsyncSql',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/asyncsql',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'none',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitAsyncSqlResponse(),
            self.execute(params, req, runtime)
        )

    async def submit_async_sql_with_options_async(
        self,
        project: str,
        request: main_models.SubmitAsyncSqlRequest,
        headers: main_models.SubmitAsyncSqlHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitAsyncSqlResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.accept):
            real_headers['Accept'] = str(headers.accept)
        if not DaraCore.is_null(headers.accept_encoding):
            real_headers['Accept-Encoding'] = str(headers.accept_encoding)
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = real_headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitAsyncSql',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/asyncsql',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'none',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitAsyncSqlResponse(),
            await self.execute_async(params, req, runtime)
        )

    def submit_async_sql(
        self,
        project: str,
        request: main_models.SubmitAsyncSqlRequest,
    ) -> main_models.SubmitAsyncSqlResponse:
        runtime = RuntimeOptions()
        headers = main_models.SubmitAsyncSqlHeaders()
        return self.submit_async_sql_with_options(project, request, headers, runtime)

    async def submit_async_sql_async(
        self,
        project: str,
        request: main_models.SubmitAsyncSqlRequest,
    ) -> main_models.SubmitAsyncSqlResponse:
        runtime = RuntimeOptions()
        headers = main_models.SubmitAsyncSqlHeaders()
        return await self.submit_async_sql_with_options_async(project, request, headers, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_id):
            body['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/tag',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.execute(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_id):
            body['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/tag',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.execute_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.tag_resources_with_options_async(request, headers, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.all):
            body['all'] = request.all
        if not DaraCore.is_null(request.resource_id):
            body['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/untag',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.execute(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: main_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.all):
            body['all'] = request.all
        if not DaraCore.is_null(request.resource_id):
            body['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/untag',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.execute_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.untag_resources_with_options(request, headers, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.untag_resources_with_options_async(request, headers, runtime)

    def update_agent_instance_config_with_options(
        self,
        config_type: str,
        tmp_req: main_models.UpdateAgentInstanceConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentInstanceConfigResponse:
        tmp_req.validate()
        request = main_models.UpdateAgentInstanceConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.attributes):
            request.attributes_shrink = Utils.array_to_string_with_specified_style(tmp_req.attributes, 'attributes', 'json')
        query = {}
        if not DaraCore.is_null(request.attributes_shrink):
            query['attributes'] = request.attributes_shrink
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.gray_configs):
            body['grayConfigs'] = request.gray_configs
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgentInstanceConfig',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/agentinstanceconfigs/{config_type}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentInstanceConfigResponse(),
            self.execute(params, req, runtime)
        )

    async def update_agent_instance_config_with_options_async(
        self,
        config_type: str,
        tmp_req: main_models.UpdateAgentInstanceConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentInstanceConfigResponse:
        tmp_req.validate()
        request = main_models.UpdateAgentInstanceConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.attributes):
            request.attributes_shrink = Utils.array_to_string_with_specified_style(tmp_req.attributes, 'attributes', 'json')
        query = {}
        if not DaraCore.is_null(request.attributes_shrink):
            query['attributes'] = request.attributes_shrink
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.gray_configs):
            body['grayConfigs'] = request.gray_configs
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgentInstanceConfig',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/agentinstanceconfigs/{config_type}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentInstanceConfigResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_agent_instance_config(
        self,
        config_type: str,
        request: main_models.UpdateAgentInstanceConfigRequest,
    ) -> main_models.UpdateAgentInstanceConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_agent_instance_config_with_options(config_type, request, headers, runtime)

    async def update_agent_instance_config_async(
        self,
        config_type: str,
        request: main_models.UpdateAgentInstanceConfigRequest,
    ) -> main_models.UpdateAgentInstanceConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_agent_instance_config_with_options_async(config_type, request, headers, runtime)

    def update_alert_with_options(
        self,
        project: str,
        alert_name: str,
        request: main_models.UpdateAlertRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAlertResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.schedule):
            body['schedule'] = request.schedule
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAlert',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/alerts/{alert_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateAlertResponse(),
            self.execute(params, req, runtime)
        )

    async def update_alert_with_options_async(
        self,
        project: str,
        alert_name: str,
        request: main_models.UpdateAlertRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAlertResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.schedule):
            body['schedule'] = request.schedule
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAlert',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/alerts/{alert_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateAlertResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_alert(
        self,
        project: str,
        alert_name: str,
        request: main_models.UpdateAlertRequest,
    ) -> main_models.UpdateAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_alert_with_options(project, alert_name, request, headers, runtime)

    async def update_alert_async(
        self,
        project: str,
        alert_name: str,
        request: main_models.UpdateAlertRequest,
    ) -> main_models.UpdateAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_alert_with_options_async(project, alert_name, request, headers, runtime)

    def update_annotation_data_set_with_options(
        self,
        dataset_id: str,
        request: main_models.UpdateAnnotationDataSetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAnnotationDataSetResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAnnotationDataSet',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/annotationdataset/{dataset_id}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateAnnotationDataSetResponse(),
            self.execute(params, req, runtime)
        )

    async def update_annotation_data_set_with_options_async(
        self,
        dataset_id: str,
        request: main_models.UpdateAnnotationDataSetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAnnotationDataSetResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAnnotationDataSet',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/annotationdataset/{dataset_id}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateAnnotationDataSetResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_annotation_data_set(
        self,
        dataset_id: str,
        request: main_models.UpdateAnnotationDataSetRequest,
    ) -> main_models.UpdateAnnotationDataSetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_annotation_data_set_with_options(dataset_id, request, headers, runtime)

    async def update_annotation_data_set_async(
        self,
        dataset_id: str,
        request: main_models.UpdateAnnotationDataSetRequest,
    ) -> main_models.UpdateAnnotationDataSetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_annotation_data_set_with_options_async(dataset_id, request, headers, runtime)

    def update_annotation_label_with_options(
        self,
        request: main_models.UpdateAnnotationLabelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAnnotationLabelResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAnnotationLabel',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/annotationlabel',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateAnnotationLabelResponse(),
            self.execute(params, req, runtime)
        )

    async def update_annotation_label_with_options_async(
        self,
        request: main_models.UpdateAnnotationLabelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAnnotationLabelResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAnnotationLabel',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ml/annotationlabel',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateAnnotationLabelResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_annotation_label(
        self,
        request: main_models.UpdateAnnotationLabelRequest,
    ) -> main_models.UpdateAnnotationLabelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_annotation_label_with_options(request, headers, runtime)

    async def update_annotation_label_async(
        self,
        request: main_models.UpdateAnnotationLabelRequest,
    ) -> main_models.UpdateAnnotationLabelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_annotation_label_with_options_async(request, headers, runtime)

    def update_azure_blob_ingestion_with_options(
        self,
        project: str,
        azure_blob_ingestion_name: str,
        request: main_models.UpdateAzureBlobIngestionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAzureBlobIngestionResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.schedule):
            body['schedule'] = request.schedule
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAzureBlobIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/azureblobingestions/{azure_blob_ingestion_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateAzureBlobIngestionResponse(),
            self.execute(params, req, runtime)
        )

    async def update_azure_blob_ingestion_with_options_async(
        self,
        project: str,
        azure_blob_ingestion_name: str,
        request: main_models.UpdateAzureBlobIngestionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAzureBlobIngestionResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.schedule):
            body['schedule'] = request.schedule
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAzureBlobIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/azureblobingestions/{azure_blob_ingestion_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateAzureBlobIngestionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_azure_blob_ingestion(
        self,
        project: str,
        azure_blob_ingestion_name: str,
        request: main_models.UpdateAzureBlobIngestionRequest,
    ) -> main_models.UpdateAzureBlobIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_azure_blob_ingestion_with_options(project, azure_blob_ingestion_name, request, headers, runtime)

    async def update_azure_blob_ingestion_async(
        self,
        project: str,
        azure_blob_ingestion_name: str,
        request: main_models.UpdateAzureBlobIngestionRequest,
    ) -> main_models.UpdateAzureBlobIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_azure_blob_ingestion_with_options_async(project, azure_blob_ingestion_name, request, headers, runtime)

    def update_config_with_options(
        self,
        project: str,
        config_name: str,
        request: main_models.UpdateConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConfigResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConfig',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/configs/{config_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateConfigResponse(),
            self.execute(params, req, runtime)
        )

    async def update_config_with_options_async(
        self,
        project: str,
        config_name: str,
        request: main_models.UpdateConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConfigResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConfig',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/configs/{config_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateConfigResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_config(
        self,
        project: str,
        config_name: str,
        request: main_models.UpdateConfigRequest,
    ) -> main_models.UpdateConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_config_with_options(project, config_name, request, headers, runtime)

    async def update_config_async(
        self,
        project: str,
        config_name: str,
        request: main_models.UpdateConfigRequest,
    ) -> main_models.UpdateConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_config_with_options_async(project, config_name, request, headers, runtime)

    def update_consumer_group_with_options(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: main_models.UpdateConsumerGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConsumerGroupResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.order):
            body['order'] = request.order
        if not DaraCore.is_null(request.timeout):
            body['timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConsumerGroup',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/consumergroups/{consumer_group}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateConsumerGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def update_consumer_group_with_options_async(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: main_models.UpdateConsumerGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConsumerGroupResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.order):
            body['order'] = request.order
        if not DaraCore.is_null(request.timeout):
            body['timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConsumerGroup',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/consumergroups/{consumer_group}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateConsumerGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_consumer_group(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: main_models.UpdateConsumerGroupRequest,
    ) -> main_models.UpdateConsumerGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_consumer_group_with_options(project, logstore, consumer_group, request, headers, runtime)

    async def update_consumer_group_async(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: main_models.UpdateConsumerGroupRequest,
    ) -> main_models.UpdateConsumerGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_consumer_group_with_options_async(project, logstore, consumer_group, request, headers, runtime)

    def update_dashboard_with_options(
        self,
        project: str,
        dashboard_name: str,
        request: main_models.UpdateDashboardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDashboardResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.attribute):
            body['attribute'] = request.attribute
        if not DaraCore.is_null(request.charts):
            body['charts'] = request.charts
        if not DaraCore.is_null(request.dashboard_name):
            body['dashboardName'] = request.dashboard_name
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDashboard',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/dashboards/{dashboard_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateDashboardResponse(),
            self.execute(params, req, runtime)
        )

    async def update_dashboard_with_options_async(
        self,
        project: str,
        dashboard_name: str,
        request: main_models.UpdateDashboardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDashboardResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.attribute):
            body['attribute'] = request.attribute
        if not DaraCore.is_null(request.charts):
            body['charts'] = request.charts
        if not DaraCore.is_null(request.dashboard_name):
            body['dashboardName'] = request.dashboard_name
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDashboard',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/dashboards/{dashboard_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateDashboardResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_dashboard(
        self,
        project: str,
        dashboard_name: str,
        request: main_models.UpdateDashboardRequest,
    ) -> main_models.UpdateDashboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_dashboard_with_options(project, dashboard_name, request, headers, runtime)

    async def update_dashboard_async(
        self,
        project: str,
        dashboard_name: str,
        request: main_models.UpdateDashboardRequest,
    ) -> main_models.UpdateDashboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_dashboard_with_options_async(project, dashboard_name, request, headers, runtime)

    def update_etlwith_options(
        self,
        project: str,
        etl_name: str,
        request: main_models.UpdateETLRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateETLResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateETL',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/etls/{etl_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateETLResponse(),
            self.execute(params, req, runtime)
        )

    async def update_etlwith_options_async(
        self,
        project: str,
        etl_name: str,
        request: main_models.UpdateETLRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateETLResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateETL',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/etls/{etl_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateETLResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_etl(
        self,
        project: str,
        etl_name: str,
        request: main_models.UpdateETLRequest,
    ) -> main_models.UpdateETLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_etlwith_options(project, etl_name, request, headers, runtime)

    async def update_etl_async(
        self,
        project: str,
        etl_name: str,
        request: main_models.UpdateETLRequest,
    ) -> main_models.UpdateETLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_etlwith_options_async(project, etl_name, request, headers, runtime)

    def update_elasticsearch_ingestion_with_options(
        self,
        project: str,
        elasticsearch_ingestion_name: str,
        request: main_models.UpdateElasticsearchIngestionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateElasticsearchIngestionResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.schedule):
            body['schedule'] = request.schedule
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateElasticsearchIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/elasticsearchingestions/{elasticsearch_ingestion_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateElasticsearchIngestionResponse(),
            self.execute(params, req, runtime)
        )

    async def update_elasticsearch_ingestion_with_options_async(
        self,
        project: str,
        elasticsearch_ingestion_name: str,
        request: main_models.UpdateElasticsearchIngestionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateElasticsearchIngestionResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.schedule):
            body['schedule'] = request.schedule
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateElasticsearchIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/elasticsearchingestions/{elasticsearch_ingestion_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateElasticsearchIngestionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_elasticsearch_ingestion(
        self,
        project: str,
        elasticsearch_ingestion_name: str,
        request: main_models.UpdateElasticsearchIngestionRequest,
    ) -> main_models.UpdateElasticsearchIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_elasticsearch_ingestion_with_options(project, elasticsearch_ingestion_name, request, headers, runtime)

    async def update_elasticsearch_ingestion_async(
        self,
        project: str,
        elasticsearch_ingestion_name: str,
        request: main_models.UpdateElasticsearchIngestionRequest,
    ) -> main_models.UpdateElasticsearchIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_elasticsearch_ingestion_with_options_async(project, elasticsearch_ingestion_name, request, headers, runtime)

    def update_index_with_options(
        self,
        project: str,
        logstore: str,
        request: main_models.UpdateIndexRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIndexResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIndex',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/index',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateIndexResponse(),
            self.execute(params, req, runtime)
        )

    async def update_index_with_options_async(
        self,
        project: str,
        logstore: str,
        request: main_models.UpdateIndexRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIndexResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIndex',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/index',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateIndexResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_index(
        self,
        project: str,
        logstore: str,
        request: main_models.UpdateIndexRequest,
    ) -> main_models.UpdateIndexResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_index_with_options(project, logstore, request, headers, runtime)

    async def update_index_async(
        self,
        project: str,
        logstore: str,
        request: main_models.UpdateIndexRequest,
    ) -> main_models.UpdateIndexResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_index_with_options_async(project, logstore, request, headers, runtime)

    def update_log_store_with_options(
        self,
        project: str,
        logstore: str,
        request: main_models.UpdateLogStoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLogStoreResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.append_meta):
            body['appendMeta'] = request.append_meta
        if not DaraCore.is_null(request.auto_split):
            body['autoSplit'] = request.auto_split
        if not DaraCore.is_null(request.enable_tracking):
            body['enable_tracking'] = request.enable_tracking
        if not DaraCore.is_null(request.encrypt_conf):
            body['encrypt_conf'] = request.encrypt_conf
        if not DaraCore.is_null(request.hot_ttl):
            body['hot_ttl'] = request.hot_ttl
        if not DaraCore.is_null(request.infrequent_access_ttl):
            body['infrequentAccessTTL'] = request.infrequent_access_ttl
        if not DaraCore.is_null(request.logstore_name):
            body['logstoreName'] = request.logstore_name
        if not DaraCore.is_null(request.max_split_shard):
            body['maxSplitShard'] = request.max_split_shard
        if not DaraCore.is_null(request.mode):
            body['mode'] = request.mode
        if not DaraCore.is_null(request.shard_count):
            body['shardCount'] = request.shard_count
        if not DaraCore.is_null(request.sharding_policy):
            body['shardingPolicy'] = request.sharding_policy
        if not DaraCore.is_null(request.telemetry_type):
            body['telemetryType'] = request.telemetry_type
        if not DaraCore.is_null(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLogStore',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateLogStoreResponse(),
            self.execute(params, req, runtime)
        )

    async def update_log_store_with_options_async(
        self,
        project: str,
        logstore: str,
        request: main_models.UpdateLogStoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLogStoreResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.append_meta):
            body['appendMeta'] = request.append_meta
        if not DaraCore.is_null(request.auto_split):
            body['autoSplit'] = request.auto_split
        if not DaraCore.is_null(request.enable_tracking):
            body['enable_tracking'] = request.enable_tracking
        if not DaraCore.is_null(request.encrypt_conf):
            body['encrypt_conf'] = request.encrypt_conf
        if not DaraCore.is_null(request.hot_ttl):
            body['hot_ttl'] = request.hot_ttl
        if not DaraCore.is_null(request.infrequent_access_ttl):
            body['infrequentAccessTTL'] = request.infrequent_access_ttl
        if not DaraCore.is_null(request.logstore_name):
            body['logstoreName'] = request.logstore_name
        if not DaraCore.is_null(request.max_split_shard):
            body['maxSplitShard'] = request.max_split_shard
        if not DaraCore.is_null(request.mode):
            body['mode'] = request.mode
        if not DaraCore.is_null(request.shard_count):
            body['shardCount'] = request.shard_count
        if not DaraCore.is_null(request.sharding_policy):
            body['shardingPolicy'] = request.sharding_policy
        if not DaraCore.is_null(request.telemetry_type):
            body['telemetryType'] = request.telemetry_type
        if not DaraCore.is_null(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLogStore',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateLogStoreResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_log_store(
        self,
        project: str,
        logstore: str,
        request: main_models.UpdateLogStoreRequest,
    ) -> main_models.UpdateLogStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_log_store_with_options(project, logstore, request, headers, runtime)

    async def update_log_store_async(
        self,
        project: str,
        logstore: str,
        request: main_models.UpdateLogStoreRequest,
    ) -> main_models.UpdateLogStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_log_store_with_options_async(project, logstore, request, headers, runtime)

    def update_log_store_encryption_with_options(
        self,
        project: str,
        logstore: str,
        request: main_models.UpdateLogStoreEncryptionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLogStoreEncryptionResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.encrypt_type):
            body['encryptType'] = request.encrypt_type
        if not DaraCore.is_null(request.user_cmk_info):
            body['userCmkInfo'] = request.user_cmk_info
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLogStoreEncryption',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/encryption',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateLogStoreEncryptionResponse(),
            self.execute(params, req, runtime)
        )

    async def update_log_store_encryption_with_options_async(
        self,
        project: str,
        logstore: str,
        request: main_models.UpdateLogStoreEncryptionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLogStoreEncryptionResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.encrypt_type):
            body['encryptType'] = request.encrypt_type
        if not DaraCore.is_null(request.user_cmk_info):
            body['userCmkInfo'] = request.user_cmk_info
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLogStoreEncryption',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/encryption',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateLogStoreEncryptionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_log_store_encryption(
        self,
        project: str,
        logstore: str,
        request: main_models.UpdateLogStoreEncryptionRequest,
    ) -> main_models.UpdateLogStoreEncryptionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_log_store_encryption_with_options(project, logstore, request, headers, runtime)

    async def update_log_store_encryption_async(
        self,
        project: str,
        logstore: str,
        request: main_models.UpdateLogStoreEncryptionRequest,
    ) -> main_models.UpdateLogStoreEncryptionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_log_store_encryption_with_options_async(project, logstore, request, headers, runtime)

    def update_log_store_metering_mode_with_options(
        self,
        project: str,
        logstore: str,
        request: main_models.UpdateLogStoreMeteringModeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLogStoreMeteringModeResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.metering_mode):
            body['meteringMode'] = request.metering_mode
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLogStoreMeteringMode',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/meteringmode',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateLogStoreMeteringModeResponse(),
            self.execute(params, req, runtime)
        )

    async def update_log_store_metering_mode_with_options_async(
        self,
        project: str,
        logstore: str,
        request: main_models.UpdateLogStoreMeteringModeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLogStoreMeteringModeResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.metering_mode):
            body['meteringMode'] = request.metering_mode
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLogStoreMeteringMode',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/meteringmode',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateLogStoreMeteringModeResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_log_store_metering_mode(
        self,
        project: str,
        logstore: str,
        request: main_models.UpdateLogStoreMeteringModeRequest,
    ) -> main_models.UpdateLogStoreMeteringModeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_log_store_metering_mode_with_options(project, logstore, request, headers, runtime)

    async def update_log_store_metering_mode_async(
        self,
        project: str,
        logstore: str,
        request: main_models.UpdateLogStoreMeteringModeRequest,
    ) -> main_models.UpdateLogStoreMeteringModeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_log_store_metering_mode_with_options_async(project, logstore, request, headers, runtime)

    def update_log_store_processor_with_options(
        self,
        project: str,
        logstore: str,
        request: main_models.UpdateLogStoreProcessorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLogStoreProcessorResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.processor_name):
            body['processorName'] = request.processor_name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLogStoreProcessor',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/processor',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateLogStoreProcessorResponse(),
            self.execute(params, req, runtime)
        )

    async def update_log_store_processor_with_options_async(
        self,
        project: str,
        logstore: str,
        request: main_models.UpdateLogStoreProcessorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLogStoreProcessorResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.processor_name):
            body['processorName'] = request.processor_name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLogStoreProcessor',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logstores/{logstore}/processor',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateLogStoreProcessorResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_log_store_processor(
        self,
        project: str,
        logstore: str,
        request: main_models.UpdateLogStoreProcessorRequest,
    ) -> main_models.UpdateLogStoreProcessorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_log_store_processor_with_options(project, logstore, request, headers, runtime)

    async def update_log_store_processor_async(
        self,
        project: str,
        logstore: str,
        request: main_models.UpdateLogStoreProcessorRequest,
    ) -> main_models.UpdateLogStoreProcessorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_log_store_processor_with_options_async(project, logstore, request, headers, runtime)

    def update_logging_with_options(
        self,
        project: str,
        request: main_models.UpdateLoggingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLoggingResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.logging_details):
            body['loggingDetails'] = request.logging_details
        if not DaraCore.is_null(request.logging_project):
            body['loggingProject'] = request.logging_project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLogging',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logging',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateLoggingResponse(),
            self.execute(params, req, runtime)
        )

    async def update_logging_with_options_async(
        self,
        project: str,
        request: main_models.UpdateLoggingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLoggingResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.logging_details):
            body['loggingDetails'] = request.logging_details
        if not DaraCore.is_null(request.logging_project):
            body['loggingProject'] = request.logging_project
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLogging',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/logging',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateLoggingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_logging(
        self,
        project: str,
        request: main_models.UpdateLoggingRequest,
    ) -> main_models.UpdateLoggingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_logging_with_options(project, request, headers, runtime)

    async def update_logging_async(
        self,
        project: str,
        request: main_models.UpdateLoggingRequest,
    ) -> main_models.UpdateLoggingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_logging_with_options_async(project, request, headers, runtime)

    def update_logtail_pipeline_config_with_options(
        self,
        project: str,
        config_name: str,
        request: main_models.UpdateLogtailPipelineConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLogtailPipelineConfigResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.aggregators):
            body['aggregators'] = request.aggregators
        if not DaraCore.is_null(request.config_name):
            body['configName'] = request.config_name
        if not DaraCore.is_null(request.flushers):
            body['flushers'] = request.flushers
        if not DaraCore.is_null(request.global_):
            body['global'] = request.global_
        if not DaraCore.is_null(request.inputs):
            body['inputs'] = request.inputs
        if not DaraCore.is_null(request.log_sample):
            body['logSample'] = request.log_sample
        if not DaraCore.is_null(request.processors):
            body['processors'] = request.processors
        if not DaraCore.is_null(request.task):
            body['task'] = request.task
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLogtailPipelineConfig',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/pipelineconfigs/{config_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateLogtailPipelineConfigResponse(),
            self.execute(params, req, runtime)
        )

    async def update_logtail_pipeline_config_with_options_async(
        self,
        project: str,
        config_name: str,
        request: main_models.UpdateLogtailPipelineConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLogtailPipelineConfigResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.aggregators):
            body['aggregators'] = request.aggregators
        if not DaraCore.is_null(request.config_name):
            body['configName'] = request.config_name
        if not DaraCore.is_null(request.flushers):
            body['flushers'] = request.flushers
        if not DaraCore.is_null(request.global_):
            body['global'] = request.global_
        if not DaraCore.is_null(request.inputs):
            body['inputs'] = request.inputs
        if not DaraCore.is_null(request.log_sample):
            body['logSample'] = request.log_sample
        if not DaraCore.is_null(request.processors):
            body['processors'] = request.processors
        if not DaraCore.is_null(request.task):
            body['task'] = request.task
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLogtailPipelineConfig',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/pipelineconfigs/{config_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateLogtailPipelineConfigResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_logtail_pipeline_config(
        self,
        project: str,
        config_name: str,
        request: main_models.UpdateLogtailPipelineConfigRequest,
    ) -> main_models.UpdateLogtailPipelineConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_logtail_pipeline_config_with_options(project, config_name, request, headers, runtime)

    async def update_logtail_pipeline_config_async(
        self,
        project: str,
        config_name: str,
        request: main_models.UpdateLogtailPipelineConfigRequest,
    ) -> main_models.UpdateLogtailPipelineConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_logtail_pipeline_config_with_options_async(project, config_name, request, headers, runtime)

    def update_machine_group_with_options(
        self,
        project: str,
        group_name: str,
        request: main_models.UpdateMachineGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMachineGroupResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.group_attribute):
            body['groupAttribute'] = request.group_attribute
        if not DaraCore.is_null(request.group_name):
            body['groupName'] = request.group_name
        if not DaraCore.is_null(request.group_type):
            body['groupType'] = request.group_type
        if not DaraCore.is_null(request.machine_identify_type):
            body['machineIdentifyType'] = request.machine_identify_type
        if not DaraCore.is_null(request.machine_list):
            body['machineList'] = request.machine_list
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMachineGroup',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/machinegroups/{group_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateMachineGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def update_machine_group_with_options_async(
        self,
        project: str,
        group_name: str,
        request: main_models.UpdateMachineGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMachineGroupResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.group_attribute):
            body['groupAttribute'] = request.group_attribute
        if not DaraCore.is_null(request.group_name):
            body['groupName'] = request.group_name
        if not DaraCore.is_null(request.group_type):
            body['groupType'] = request.group_type
        if not DaraCore.is_null(request.machine_identify_type):
            body['machineIdentifyType'] = request.machine_identify_type
        if not DaraCore.is_null(request.machine_list):
            body['machineList'] = request.machine_list
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMachineGroup',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/machinegroups/{group_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateMachineGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_machine_group(
        self,
        project: str,
        group_name: str,
        request: main_models.UpdateMachineGroupRequest,
    ) -> main_models.UpdateMachineGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_machine_group_with_options(project, group_name, request, headers, runtime)

    async def update_machine_group_async(
        self,
        project: str,
        group_name: str,
        request: main_models.UpdateMachineGroupRequest,
    ) -> main_models.UpdateMachineGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_machine_group_with_options_async(project, group_name, request, headers, runtime)

    def update_machine_group_machine_with_options(
        self,
        project: str,
        machine_group: str,
        request: main_models.UpdateMachineGroupMachineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMachineGroupMachineResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.action):
            query['action'] = request.action
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateMachineGroupMachine',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/machinegroups/{machine_group}/machines',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateMachineGroupMachineResponse(),
            self.execute(params, req, runtime)
        )

    async def update_machine_group_machine_with_options_async(
        self,
        project: str,
        machine_group: str,
        request: main_models.UpdateMachineGroupMachineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMachineGroupMachineResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        query = {}
        if not DaraCore.is_null(request.action):
            query['action'] = request.action
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateMachineGroupMachine',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/machinegroups/{machine_group}/machines',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateMachineGroupMachineResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_machine_group_machine(
        self,
        project: str,
        machine_group: str,
        request: main_models.UpdateMachineGroupMachineRequest,
    ) -> main_models.UpdateMachineGroupMachineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_machine_group_machine_with_options(project, machine_group, request, headers, runtime)

    async def update_machine_group_machine_async(
        self,
        project: str,
        machine_group: str,
        request: main_models.UpdateMachineGroupMachineRequest,
    ) -> main_models.UpdateMachineGroupMachineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_machine_group_machine_with_options_async(project, machine_group, request, headers, runtime)

    def update_materialized_view_with_options(
        self,
        project: str,
        name: str,
        request: main_models.UpdateMaterializedViewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMaterializedViewResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.agg_interval_mins):
            body['aggIntervalMins'] = request.agg_interval_mins
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.original_sql):
            body['originalSql'] = request.original_sql
        if not DaraCore.is_null(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMaterializedView',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/materializedviews/{name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateMaterializedViewResponse(),
            self.execute(params, req, runtime)
        )

    async def update_materialized_view_with_options_async(
        self,
        project: str,
        name: str,
        request: main_models.UpdateMaterializedViewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMaterializedViewResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.agg_interval_mins):
            body['aggIntervalMins'] = request.agg_interval_mins
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.original_sql):
            body['originalSql'] = request.original_sql
        if not DaraCore.is_null(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMaterializedView',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/materializedviews/{name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateMaterializedViewResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_materialized_view(
        self,
        project: str,
        name: str,
        request: main_models.UpdateMaterializedViewRequest,
    ) -> main_models.UpdateMaterializedViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_materialized_view_with_options(project, name, request, headers, runtime)

    async def update_materialized_view_async(
        self,
        project: str,
        name: str,
        request: main_models.UpdateMaterializedViewRequest,
    ) -> main_models.UpdateMaterializedViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_materialized_view_with_options_async(project, name, request, headers, runtime)

    def update_max_compute_export_with_options(
        self,
        project: str,
        mc_export_name: str,
        request: main_models.UpdateMaxComputeExportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMaxComputeExportResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMaxComputeExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/maxcomputeexports/{mc_export_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateMaxComputeExportResponse(),
            self.execute(params, req, runtime)
        )

    async def update_max_compute_export_with_options_async(
        self,
        project: str,
        mc_export_name: str,
        request: main_models.UpdateMaxComputeExportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMaxComputeExportResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMaxComputeExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/maxcomputeexports/{mc_export_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateMaxComputeExportResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_max_compute_export(
        self,
        project: str,
        mc_export_name: str,
        request: main_models.UpdateMaxComputeExportRequest,
    ) -> main_models.UpdateMaxComputeExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_max_compute_export_with_options(project, mc_export_name, request, headers, runtime)

    async def update_max_compute_export_async(
        self,
        project: str,
        mc_export_name: str,
        request: main_models.UpdateMaxComputeExportRequest,
    ) -> main_models.UpdateMaxComputeExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_max_compute_export_with_options_async(project, mc_export_name, request, headers, runtime)

    def update_metric_store_with_options(
        self,
        project: str,
        name: str,
        request: main_models.UpdateMetricStoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMetricStoreResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.append_meta):
            body['appendMeta'] = request.append_meta
        if not DaraCore.is_null(request.auto_split):
            body['autoSplit'] = request.auto_split
        if not DaraCore.is_null(request.hot_ttl):
            body['hot_ttl'] = request.hot_ttl
        if not DaraCore.is_null(request.infrequent_access_ttl):
            body['infrequentAccessTTL'] = request.infrequent_access_ttl
        if not DaraCore.is_null(request.max_split_shard):
            body['maxSplitShard'] = request.max_split_shard
        if not DaraCore.is_null(request.mode):
            body['mode'] = request.mode
        if not DaraCore.is_null(request.sharding_policy):
            body['shardingPolicy'] = request.sharding_policy
        if not DaraCore.is_null(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMetricStore',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/metricstores/{name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateMetricStoreResponse(),
            self.execute(params, req, runtime)
        )

    async def update_metric_store_with_options_async(
        self,
        project: str,
        name: str,
        request: main_models.UpdateMetricStoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMetricStoreResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.append_meta):
            body['appendMeta'] = request.append_meta
        if not DaraCore.is_null(request.auto_split):
            body['autoSplit'] = request.auto_split
        if not DaraCore.is_null(request.hot_ttl):
            body['hot_ttl'] = request.hot_ttl
        if not DaraCore.is_null(request.infrequent_access_ttl):
            body['infrequentAccessTTL'] = request.infrequent_access_ttl
        if not DaraCore.is_null(request.max_split_shard):
            body['maxSplitShard'] = request.max_split_shard
        if not DaraCore.is_null(request.mode):
            body['mode'] = request.mode
        if not DaraCore.is_null(request.sharding_policy):
            body['shardingPolicy'] = request.sharding_policy
        if not DaraCore.is_null(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMetricStore',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/metricstores/{name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateMetricStoreResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_metric_store(
        self,
        project: str,
        name: str,
        request: main_models.UpdateMetricStoreRequest,
    ) -> main_models.UpdateMetricStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_metric_store_with_options(project, name, request, headers, runtime)

    async def update_metric_store_async(
        self,
        project: str,
        name: str,
        request: main_models.UpdateMetricStoreRequest,
    ) -> main_models.UpdateMetricStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_metric_store_with_options_async(project, name, request, headers, runtime)

    def update_metric_store_metering_mode_with_options(
        self,
        project: str,
        metric_store: str,
        request: main_models.UpdateMetricStoreMeteringModeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMetricStoreMeteringModeResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.metering_mode):
            body['meteringMode'] = request.metering_mode
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMetricStoreMeteringMode',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/metricstores/{metric_store}/meteringmode',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateMetricStoreMeteringModeResponse(),
            self.execute(params, req, runtime)
        )

    async def update_metric_store_metering_mode_with_options_async(
        self,
        project: str,
        metric_store: str,
        request: main_models.UpdateMetricStoreMeteringModeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMetricStoreMeteringModeResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.metering_mode):
            body['meteringMode'] = request.metering_mode
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMetricStoreMeteringMode',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/metricstores/{metric_store}/meteringmode',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateMetricStoreMeteringModeResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_metric_store_metering_mode(
        self,
        project: str,
        metric_store: str,
        request: main_models.UpdateMetricStoreMeteringModeRequest,
    ) -> main_models.UpdateMetricStoreMeteringModeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_metric_store_metering_mode_with_options(project, metric_store, request, headers, runtime)

    async def update_metric_store_metering_mode_async(
        self,
        project: str,
        metric_store: str,
        request: main_models.UpdateMetricStoreMeteringModeRequest,
    ) -> main_models.UpdateMetricStoreMeteringModeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_metric_store_metering_mode_with_options_async(project, metric_store, request, headers, runtime)

    def update_metric_store_processor_with_options(
        self,
        project: str,
        metricstore: str,
        request: main_models.UpdateMetricStoreProcessorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMetricStoreProcessorResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.processor_name):
            body['processorName'] = request.processor_name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMetricStoreProcessor',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/metricstores/{metricstore}/processor',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateMetricStoreProcessorResponse(),
            self.execute(params, req, runtime)
        )

    async def update_metric_store_processor_with_options_async(
        self,
        project: str,
        metricstore: str,
        request: main_models.UpdateMetricStoreProcessorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMetricStoreProcessorResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.processor_name):
            body['processorName'] = request.processor_name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMetricStoreProcessor',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/metricstores/{metricstore}/processor',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateMetricStoreProcessorResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_metric_store_processor(
        self,
        project: str,
        metricstore: str,
        request: main_models.UpdateMetricStoreProcessorRequest,
    ) -> main_models.UpdateMetricStoreProcessorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_metric_store_processor_with_options(project, metricstore, request, headers, runtime)

    async def update_metric_store_processor_async(
        self,
        project: str,
        metricstore: str,
        request: main_models.UpdateMetricStoreProcessorRequest,
    ) -> main_models.UpdateMetricStoreProcessorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_metric_store_processor_with_options_async(project, metricstore, request, headers, runtime)

    def update_ossexport_with_options(
        self,
        project: str,
        oss_export_name: str,
        request: main_models.UpdateOSSExportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOSSExportResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOSSExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ossexports/{oss_export_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateOSSExportResponse(),
            self.execute(params, req, runtime)
        )

    async def update_ossexport_with_options_async(
        self,
        project: str,
        oss_export_name: str,
        request: main_models.UpdateOSSExportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOSSExportResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOSSExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ossexports/{oss_export_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateOSSExportResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_ossexport(
        self,
        project: str,
        oss_export_name: str,
        request: main_models.UpdateOSSExportRequest,
    ) -> main_models.UpdateOSSExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_ossexport_with_options(project, oss_export_name, request, headers, runtime)

    async def update_ossexport_async(
        self,
        project: str,
        oss_export_name: str,
        request: main_models.UpdateOSSExportRequest,
    ) -> main_models.UpdateOSSExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_ossexport_with_options_async(project, oss_export_name, request, headers, runtime)

    def update_osshdfsexport_with_options(
        self,
        project: str,
        oss_export_name: str,
        request: main_models.UpdateOSSHDFSExportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOSSHDFSExportResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOSSHDFSExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/osshdfsexports/{oss_export_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateOSSHDFSExportResponse(),
            self.execute(params, req, runtime)
        )

    async def update_osshdfsexport_with_options_async(
        self,
        project: str,
        oss_export_name: str,
        request: main_models.UpdateOSSHDFSExportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOSSHDFSExportResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOSSHDFSExport',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/osshdfsexports/{oss_export_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateOSSHDFSExportResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_osshdfsexport(
        self,
        project: str,
        oss_export_name: str,
        request: main_models.UpdateOSSHDFSExportRequest,
    ) -> main_models.UpdateOSSHDFSExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_osshdfsexport_with_options(project, oss_export_name, request, headers, runtime)

    async def update_osshdfsexport_async(
        self,
        project: str,
        oss_export_name: str,
        request: main_models.UpdateOSSHDFSExportRequest,
    ) -> main_models.UpdateOSSHDFSExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_osshdfsexport_with_options_async(project, oss_export_name, request, headers, runtime)

    def update_ossingestion_with_options(
        self,
        project: str,
        oss_ingestion_name: str,
        request: main_models.UpdateOSSIngestionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOSSIngestionResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.schedule):
            body['schedule'] = request.schedule
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOSSIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ossingestions/{oss_ingestion_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateOSSIngestionResponse(),
            self.execute(params, req, runtime)
        )

    async def update_ossingestion_with_options_async(
        self,
        project: str,
        oss_ingestion_name: str,
        request: main_models.UpdateOSSIngestionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOSSIngestionResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.schedule):
            body['schedule'] = request.schedule
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOSSIngestion',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/ossingestions/{oss_ingestion_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateOSSIngestionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_ossingestion(
        self,
        project: str,
        oss_ingestion_name: str,
        request: main_models.UpdateOSSIngestionRequest,
    ) -> main_models.UpdateOSSIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_ossingestion_with_options(project, oss_ingestion_name, request, headers, runtime)

    async def update_ossingestion_async(
        self,
        project: str,
        oss_ingestion_name: str,
        request: main_models.UpdateOSSIngestionRequest,
    ) -> main_models.UpdateOSSIngestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_ossingestion_with_options_async(project, oss_ingestion_name, request, headers, runtime)

    def update_project_with_options(
        self,
        project: str,
        request: main_models.UpdateProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProjectResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.recycle_bin_enabled):
            body['recycleBinEnabled'] = request.recycle_bin_enabled
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProject',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateProjectResponse(),
            self.execute(params, req, runtime)
        )

    async def update_project_with_options_async(
        self,
        project: str,
        request: main_models.UpdateProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProjectResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.recycle_bin_enabled):
            body['recycleBinEnabled'] = request.recycle_bin_enabled
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProject',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateProjectResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_project(
        self,
        project: str,
        request: main_models.UpdateProjectRequest,
    ) -> main_models.UpdateProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_project_with_options(project, request, headers, runtime)

    async def update_project_async(
        self,
        project: str,
        request: main_models.UpdateProjectRequest,
    ) -> main_models.UpdateProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_project_with_options_async(project, request, headers, runtime)

    def update_saved_search_with_options(
        self,
        project: str,
        savedsearch_name: str,
        request: main_models.UpdateSavedSearchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSavedSearchResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.logstore):
            body['logstore'] = request.logstore
        if not DaraCore.is_null(request.savedsearch_name):
            body['savedsearchName'] = request.savedsearch_name
        if not DaraCore.is_null(request.search_query):
            body['searchQuery'] = request.search_query
        if not DaraCore.is_null(request.topic):
            body['topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSavedSearch',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/savedsearches/{savedsearch_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateSavedSearchResponse(),
            self.execute(params, req, runtime)
        )

    async def update_saved_search_with_options_async(
        self,
        project: str,
        savedsearch_name: str,
        request: main_models.UpdateSavedSearchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSavedSearchResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.logstore):
            body['logstore'] = request.logstore
        if not DaraCore.is_null(request.savedsearch_name):
            body['savedsearchName'] = request.savedsearch_name
        if not DaraCore.is_null(request.search_query):
            body['searchQuery'] = request.search_query
        if not DaraCore.is_null(request.topic):
            body['topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSavedSearch',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/savedsearches/{savedsearch_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateSavedSearchResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_saved_search(
        self,
        project: str,
        savedsearch_name: str,
        request: main_models.UpdateSavedSearchRequest,
    ) -> main_models.UpdateSavedSearchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_saved_search_with_options(project, savedsearch_name, request, headers, runtime)

    async def update_saved_search_async(
        self,
        project: str,
        savedsearch_name: str,
        request: main_models.UpdateSavedSearchRequest,
    ) -> main_models.UpdateSavedSearchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_saved_search_with_options_async(project, savedsearch_name, request, headers, runtime)

    def update_scheduled_sqlwith_options(
        self,
        project: str,
        scheduled_sqlname: str,
        request: main_models.UpdateScheduledSQLRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateScheduledSQLResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.schedule):
            body['schedule'] = request.schedule
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateScheduledSQL',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/scheduledsqls/{scheduled_sqlname}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateScheduledSQLResponse(),
            self.execute(params, req, runtime)
        )

    async def update_scheduled_sqlwith_options_async(
        self,
        project: str,
        scheduled_sqlname: str,
        request: main_models.UpdateScheduledSQLRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateScheduledSQLResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.schedule):
            body['schedule'] = request.schedule
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateScheduledSQL',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/scheduledsqls/{scheduled_sqlname}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateScheduledSQLResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_scheduled_sql(
        self,
        project: str,
        scheduled_sqlname: str,
        request: main_models.UpdateScheduledSQLRequest,
    ) -> main_models.UpdateScheduledSQLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_scheduled_sqlwith_options(project, scheduled_sqlname, request, headers, runtime)

    async def update_scheduled_sql_async(
        self,
        project: str,
        scheduled_sqlname: str,
        request: main_models.UpdateScheduledSQLRequest,
    ) -> main_models.UpdateScheduledSQLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_scheduled_sqlwith_options_async(project, scheduled_sqlname, request, headers, runtime)

    def update_sql_instance_with_options(
        self,
        project: str,
        request: main_models.UpdateSqlInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSqlInstanceResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.cu):
            body['cu'] = request.cu
        if not DaraCore.is_null(request.use_as_default):
            body['useAsDefault'] = request.use_as_default
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSqlInstance',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/sqlinstance',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateSqlInstanceResponse(),
            self.execute(params, req, runtime)
        )

    async def update_sql_instance_with_options_async(
        self,
        project: str,
        request: main_models.UpdateSqlInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSqlInstanceResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.cu):
            body['cu'] = request.cu
        if not DaraCore.is_null(request.use_as_default):
            body['useAsDefault'] = request.use_as_default
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSqlInstance',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/sqlinstance',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateSqlInstanceResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_sql_instance(
        self,
        project: str,
        request: main_models.UpdateSqlInstanceRequest,
    ) -> main_models.UpdateSqlInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_sql_instance_with_options(project, request, headers, runtime)

    async def update_sql_instance_async(
        self,
        project: str,
        request: main_models.UpdateSqlInstanceRequest,
    ) -> main_models.UpdateSqlInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_sql_instance_with_options_async(project, request, headers, runtime)

    def update_store_view_with_options(
        self,
        project: str,
        name: str,
        request: main_models.UpdateStoreViewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStoreViewResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.store_type):
            body['storeType'] = request.store_type
        if not DaraCore.is_null(request.stores):
            body['stores'] = request.stores
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStoreView',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/storeviews/{name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateStoreViewResponse(),
            self.execute(params, req, runtime)
        )

    async def update_store_view_with_options_async(
        self,
        project: str,
        name: str,
        request: main_models.UpdateStoreViewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStoreViewResponse:
        request.validate()
        host_map = {}
        host_map['project'] = project
        body = {}
        if not DaraCore.is_null(request.store_type):
            body['storeType'] = request.store_type
        if not DaraCore.is_null(request.stores):
            body['stores'] = request.stores
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStoreView',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/storeviews/{name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateStoreViewResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_store_view(
        self,
        project: str,
        name: str,
        request: main_models.UpdateStoreViewRequest,
    ) -> main_models.UpdateStoreViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_store_view_with_options(project, name, request, headers, runtime)

    async def update_store_view_async(
        self,
        project: str,
        name: str,
        request: main_models.UpdateStoreViewRequest,
    ) -> main_models.UpdateStoreViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_store_view_with_options_async(project, name, request, headers, runtime)

    def upsert_collection_policy_with_options(
        self,
        request: main_models.UpsertCollectionPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpsertCollectionPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.centralize_config):
            body['centralizeConfig'] = request.centralize_config
        if not DaraCore.is_null(request.centralize_enabled):
            body['centralizeEnabled'] = request.centralize_enabled
        if not DaraCore.is_null(request.data_code):
            body['dataCode'] = request.data_code
        if not DaraCore.is_null(request.data_config):
            body['dataConfig'] = request.data_config
        if not DaraCore.is_null(request.enabled):
            body['enabled'] = request.enabled
        if not DaraCore.is_null(request.policy_config):
            body['policyConfig'] = request.policy_config
        if not DaraCore.is_null(request.policy_name):
            body['policyName'] = request.policy_name
        if not DaraCore.is_null(request.product_code):
            body['productCode'] = request.product_code
        if not DaraCore.is_null(request.resource_directory):
            body['resourceDirectory'] = request.resource_directory
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpsertCollectionPolicy',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/collectionpolicy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpsertCollectionPolicyResponse(),
            self.execute(params, req, runtime)
        )

    async def upsert_collection_policy_with_options_async(
        self,
        request: main_models.UpsertCollectionPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpsertCollectionPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.centralize_config):
            body['centralizeConfig'] = request.centralize_config
        if not DaraCore.is_null(request.centralize_enabled):
            body['centralizeEnabled'] = request.centralize_enabled
        if not DaraCore.is_null(request.data_code):
            body['dataCode'] = request.data_code
        if not DaraCore.is_null(request.data_config):
            body['dataConfig'] = request.data_config
        if not DaraCore.is_null(request.enabled):
            body['enabled'] = request.enabled
        if not DaraCore.is_null(request.policy_config):
            body['policyConfig'] = request.policy_config
        if not DaraCore.is_null(request.policy_name):
            body['policyName'] = request.policy_name
        if not DaraCore.is_null(request.product_code):
            body['productCode'] = request.product_code
        if not DaraCore.is_null(request.resource_directory):
            body['resourceDirectory'] = request.resource_directory
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpsertCollectionPolicy',
            version = '2020-12-30',
            protocol = 'HTTPS',
            pathname = f'/collectionpolicy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpsertCollectionPolicyResponse(),
            await self.execute_async(params, req, runtime)
        )

    def upsert_collection_policy(
        self,
        request: main_models.UpsertCollectionPolicyRequest,
    ) -> main_models.UpsertCollectionPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.upsert_collection_policy_with_options(request, headers, runtime)

    async def upsert_collection_policy_async(
        self,
        request: main_models.UpsertCollectionPolicyRequest,
    ) -> main_models.UpsertCollectionPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.upsert_collection_policy_with_options_async(request, headers, runtime)
