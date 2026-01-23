# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_datahub20240620 import models as main_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('datahub', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_connector_with_options(
        self,
        request: main_models.GetConnectorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConnectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConnector',
            version = '2024-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_connector_with_options_async(
        self,
        request: main_models.GetConnectorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConnectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConnector',
            version = '2024-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConnectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_connector(
        self,
        request: main_models.GetConnectorRequest,
    ) -> main_models.GetConnectorResponse:
        runtime = RuntimeOptions()
        return self.get_connector_with_options(request, runtime)

    async def get_connector_async(
        self,
        request: main_models.GetConnectorRequest,
    ) -> main_models.GetConnectorResponse:
        runtime = RuntimeOptions()
        return await self.get_connector_with_options_async(request, runtime)

    def get_group_with_options(
        self,
        request: main_models.GetGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGroup',
            version = '2024-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_group_with_options_async(
        self,
        request: main_models.GetGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGroup',
            version = '2024-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_group(
        self,
        request: main_models.GetGroupRequest,
    ) -> main_models.GetGroupResponse:
        runtime = RuntimeOptions()
        return self.get_group_with_options(request, runtime)

    async def get_group_async(
        self,
        request: main_models.GetGroupRequest,
    ) -> main_models.GetGroupResponse:
        runtime = RuntimeOptions()
        return await self.get_group_with_options_async(request, runtime)

    def get_project_with_options(
        self,
        request: main_models.GetProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProject',
            version = '2024-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_with_options_async(
        self,
        request: main_models.GetProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProject',
            version = '2024-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project(
        self,
        request: main_models.GetProjectRequest,
    ) -> main_models.GetProjectResponse:
        runtime = RuntimeOptions()
        return self.get_project_with_options(request, runtime)

    async def get_project_async(
        self,
        request: main_models.GetProjectRequest,
    ) -> main_models.GetProjectResponse:
        runtime = RuntimeOptions()
        return await self.get_project_with_options_async(request, runtime)

    def get_records_with_options(
        self,
        request: main_models.GetRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.shard_id):
            query['ShardId'] = request.shard_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRecords',
            version = '2024-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_records_with_options_async(
        self,
        request: main_models.GetRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.shard_id):
            query['ShardId'] = request.shard_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRecords',
            version = '2024-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_records(
        self,
        request: main_models.GetRecordsRequest,
    ) -> main_models.GetRecordsResponse:
        runtime = RuntimeOptions()
        return self.get_records_with_options(request, runtime)

    async def get_records_async(
        self,
        request: main_models.GetRecordsRequest,
    ) -> main_models.GetRecordsResponse:
        runtime = RuntimeOptions()
        return await self.get_records_with_options_async(request, runtime)

    def get_schema_with_options(
        self,
        request: main_models.GetSchemaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSchemaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSchema',
            version = '2024-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_schema_with_options_async(
        self,
        request: main_models.GetSchemaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSchemaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSchema',
            version = '2024-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_schema(
        self,
        request: main_models.GetSchemaRequest,
    ) -> main_models.GetSchemaResponse:
        runtime = RuntimeOptions()
        return self.get_schema_with_options(request, runtime)

    async def get_schema_async(
        self,
        request: main_models.GetSchemaRequest,
    ) -> main_models.GetSchemaResponse:
        runtime = RuntimeOptions()
        return await self.get_schema_with_options_async(request, runtime)

    def get_subscription_with_options(
        self,
        request: main_models.GetSubscriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSubscriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.subscription_id):
            query['SubscriptionId'] = request.subscription_id
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSubscription',
            version = '2024-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_subscription_with_options_async(
        self,
        request: main_models.GetSubscriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSubscriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.subscription_id):
            query['SubscriptionId'] = request.subscription_id
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSubscription',
            version = '2024-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_subscription(
        self,
        request: main_models.GetSubscriptionRequest,
    ) -> main_models.GetSubscriptionResponse:
        runtime = RuntimeOptions()
        return self.get_subscription_with_options(request, runtime)

    async def get_subscription_async(
        self,
        request: main_models.GetSubscriptionRequest,
    ) -> main_models.GetSubscriptionResponse:
        runtime = RuntimeOptions()
        return await self.get_subscription_with_options_async(request, runtime)

    def get_topic_with_options(
        self,
        request: main_models.GetTopicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTopicResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTopic',
            version = '2024-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_topic_with_options_async(
        self,
        request: main_models.GetTopicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTopicResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTopic',
            version = '2024-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_topic(
        self,
        request: main_models.GetTopicRequest,
    ) -> main_models.GetTopicResponse:
        runtime = RuntimeOptions()
        return self.get_topic_with_options(request, runtime)

    async def get_topic_async(
        self,
        request: main_models.GetTopicRequest,
    ) -> main_models.GetTopicResponse:
        runtime = RuntimeOptions()
        return await self.get_topic_with_options_async(request, runtime)

    def list_connectors_with_options(
        self,
        request: main_models.ListConnectorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConnectorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.pure):
            query['Pure'] = request.pure
        if not DaraCore.is_null(request.skip):
            query['Skip'] = request.skip
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConnectors',
            version = '2024-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConnectorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_connectors_with_options_async(
        self,
        request: main_models.ListConnectorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConnectorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.pure):
            query['Pure'] = request.pure
        if not DaraCore.is_null(request.skip):
            query['Skip'] = request.skip
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConnectors',
            version = '2024-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConnectorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_connectors(
        self,
        request: main_models.ListConnectorsRequest,
    ) -> main_models.ListConnectorsResponse:
        runtime = RuntimeOptions()
        return self.list_connectors_with_options(request, runtime)

    async def list_connectors_async(
        self,
        request: main_models.ListConnectorsRequest,
    ) -> main_models.ListConnectorsResponse:
        runtime = RuntimeOptions()
        return await self.list_connectors_with_options_async(request, runtime)

    def list_groups_with_options(
        self,
        request: main_models.ListGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.pure):
            query['Pure'] = request.pure
        if not DaraCore.is_null(request.skip):
            query['Skip'] = request.skip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroups',
            version = '2024-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_groups_with_options_async(
        self,
        request: main_models.ListGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.pure):
            query['Pure'] = request.pure
        if not DaraCore.is_null(request.skip):
            query['Skip'] = request.skip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroups',
            version = '2024-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_groups(
        self,
        request: main_models.ListGroupsRequest,
    ) -> main_models.ListGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_groups_with_options(request, runtime)

    async def list_groups_async(
        self,
        request: main_models.ListGroupsRequest,
    ) -> main_models.ListGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_groups_with_options_async(request, runtime)

    def list_projects_with_options(
        self,
        request: main_models.ListProjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.pure):
            query['Pure'] = request.pure
        if not DaraCore.is_null(request.skip):
            query['Skip'] = request.skip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProjects',
            version = '2024-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_projects_with_options_async(
        self,
        request: main_models.ListProjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.pure):
            query['Pure'] = request.pure
        if not DaraCore.is_null(request.skip):
            query['Skip'] = request.skip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProjects',
            version = '2024-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_projects(
        self,
        request: main_models.ListProjectsRequest,
    ) -> main_models.ListProjectsResponse:
        runtime = RuntimeOptions()
        return self.list_projects_with_options(request, runtime)

    async def list_projects_async(
        self,
        request: main_models.ListProjectsRequest,
    ) -> main_models.ListProjectsResponse:
        runtime = RuntimeOptions()
        return await self.list_projects_with_options_async(request, runtime)

    def list_schemas_with_options(
        self,
        request: main_models.ListSchemasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSchemasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.skip):
            query['Skip'] = request.skip
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSchemas',
            version = '2024-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_schemas_with_options_async(
        self,
        request: main_models.ListSchemasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSchemasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.skip):
            query['Skip'] = request.skip
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSchemas',
            version = '2024-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSchemasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_schemas(
        self,
        request: main_models.ListSchemasRequest,
    ) -> main_models.ListSchemasResponse:
        runtime = RuntimeOptions()
        return self.list_schemas_with_options(request, runtime)

    async def list_schemas_async(
        self,
        request: main_models.ListSchemasRequest,
    ) -> main_models.ListSchemasResponse:
        runtime = RuntimeOptions()
        return await self.list_schemas_with_options_async(request, runtime)

    def list_subscriptions_with_options(
        self,
        request: main_models.ListSubscriptionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSubscriptionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.skip):
            query['Skip'] = request.skip
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSubscriptions',
            version = '2024-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubscriptionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_subscriptions_with_options_async(
        self,
        request: main_models.ListSubscriptionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSubscriptionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.skip):
            query['Skip'] = request.skip
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSubscriptions',
            version = '2024-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubscriptionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_subscriptions(
        self,
        request: main_models.ListSubscriptionsRequest,
    ) -> main_models.ListSubscriptionsResponse:
        runtime = RuntimeOptions()
        return self.list_subscriptions_with_options(request, runtime)

    async def list_subscriptions_async(
        self,
        request: main_models.ListSubscriptionsRequest,
    ) -> main_models.ListSubscriptionsResponse:
        runtime = RuntimeOptions()
        return await self.list_subscriptions_with_options_async(request, runtime)

    def list_topics_with_options(
        self,
        request: main_models.ListTopicsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTopicsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.pure):
            query['Pure'] = request.pure
        if not DaraCore.is_null(request.skip):
            query['Skip'] = request.skip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTopics',
            version = '2024-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTopicsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_topics_with_options_async(
        self,
        request: main_models.ListTopicsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTopicsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.pure):
            query['Pure'] = request.pure
        if not DaraCore.is_null(request.skip):
            query['Skip'] = request.skip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTopics',
            version = '2024-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTopicsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_topics(
        self,
        request: main_models.ListTopicsRequest,
    ) -> main_models.ListTopicsResponse:
        runtime = RuntimeOptions()
        return self.list_topics_with_options(request, runtime)

    async def list_topics_async(
        self,
        request: main_models.ListTopicsRequest,
    ) -> main_models.ListTopicsResponse:
        runtime = RuntimeOptions()
        return await self.list_topics_with_options_async(request, runtime)

    def put_records_with_options(
        self,
        tmp_req: main_models.PutRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutRecordsResponse:
        tmp_req.validate()
        request = main_models.PutRecordsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.records):
            request.records_shrink = Utils.array_to_string_with_specified_style(tmp_req.records, 'Records', 'json')
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.records_shrink):
            query['Records'] = request.records_shrink
        if not DaraCore.is_null(request.shard_id):
            query['ShardId'] = request.shard_id
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutRecords',
            version = '2024-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_records_with_options_async(
        self,
        tmp_req: main_models.PutRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutRecordsResponse:
        tmp_req.validate()
        request = main_models.PutRecordsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.records):
            request.records_shrink = Utils.array_to_string_with_specified_style(tmp_req.records, 'Records', 'json')
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.records_shrink):
            query['Records'] = request.records_shrink
        if not DaraCore.is_null(request.shard_id):
            query['ShardId'] = request.shard_id
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutRecords',
            version = '2024-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_records(
        self,
        request: main_models.PutRecordsRequest,
    ) -> main_models.PutRecordsResponse:
        runtime = RuntimeOptions()
        return self.put_records_with_options(request, runtime)

    async def put_records_async(
        self,
        request: main_models.PutRecordsRequest,
    ) -> main_models.PutRecordsResponse:
        runtime = RuntimeOptions()
        return await self.put_records_with_options_async(request, runtime)
