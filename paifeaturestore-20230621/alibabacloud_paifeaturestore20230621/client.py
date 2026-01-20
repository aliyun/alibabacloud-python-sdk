# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_paifeaturestore20230621 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions
from darabonba.url import Url as DaraURL

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
        self._endpoint = self.get_endpoint('paifeaturestore', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def check_instance_datasource_with_options(
        self,
        instance_id: str,
        request: main_models.CheckInstanceDatasourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckInstanceDatasourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.uri):
            body['Uri'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckInstanceDatasource',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/action/checkdatasource',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckInstanceDatasourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_instance_datasource_with_options_async(
        self,
        instance_id: str,
        request: main_models.CheckInstanceDatasourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckInstanceDatasourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.uri):
            body['Uri'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckInstanceDatasource',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/action/checkdatasource',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckInstanceDatasourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_instance_datasource(
        self,
        instance_id: str,
        request: main_models.CheckInstanceDatasourceRequest,
    ) -> main_models.CheckInstanceDatasourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.check_instance_datasource_with_options(instance_id, request, headers, runtime)

    async def check_instance_datasource_async(
        self,
        instance_id: str,
        request: main_models.CheckInstanceDatasourceRequest,
    ) -> main_models.CheckInstanceDatasourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.check_instance_datasource_with_options_async(instance_id, request, headers, runtime)

    def check_model_feature_fgfeature_with_options(
        self,
        instance_id: str,
        model_feature_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckModelFeatureFGFeatureResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CheckModelFeatureFGFeature',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/modelfeatures/{DaraURL.percent_encode(model_feature_id)}/action/checkfgfeature',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckModelFeatureFGFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_model_feature_fgfeature_with_options_async(
        self,
        instance_id: str,
        model_feature_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckModelFeatureFGFeatureResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CheckModelFeatureFGFeature',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/modelfeatures/{DaraURL.percent_encode(model_feature_id)}/action/checkfgfeature',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckModelFeatureFGFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_model_feature_fgfeature(
        self,
        instance_id: str,
        model_feature_id: str,
    ) -> main_models.CheckModelFeatureFGFeatureResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.check_model_feature_fgfeature_with_options(instance_id, model_feature_id, headers, runtime)

    async def check_model_feature_fgfeature_async(
        self,
        instance_id: str,
        model_feature_id: str,
    ) -> main_models.CheckModelFeatureFGFeatureResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.check_model_feature_fgfeature_with_options_async(instance_id, model_feature_id, headers, runtime)

    def create_datasource_with_options(
        self,
        instance_id: str,
        request: main_models.CreateDatasourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.uri):
            body['Uri'] = request.uri
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDatasource',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/datasources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_datasource_with_options_async(
        self,
        instance_id: str,
        request: main_models.CreateDatasourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.uri):
            body['Uri'] = request.uri
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDatasource',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/datasources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_datasource(
        self,
        instance_id: str,
        request: main_models.CreateDatasourceRequest,
    ) -> main_models.CreateDatasourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_datasource_with_options(instance_id, request, headers, runtime)

    async def create_datasource_async(
        self,
        instance_id: str,
        request: main_models.CreateDatasourceRequest,
    ) -> main_models.CreateDatasourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_datasource_with_options_async(instance_id, request, headers, runtime)

    def create_feature_entity_with_options(
        self,
        instance_id: str,
        request: main_models.CreateFeatureEntityRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateFeatureEntityResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.join_id):
            body['JoinId'] = request.join_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.parent_feature_entity_id):
            body['ParentFeatureEntityId'] = request.parent_feature_entity_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFeatureEntity',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/featureentities',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFeatureEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_feature_entity_with_options_async(
        self,
        instance_id: str,
        request: main_models.CreateFeatureEntityRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateFeatureEntityResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.join_id):
            body['JoinId'] = request.join_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.parent_feature_entity_id):
            body['ParentFeatureEntityId'] = request.parent_feature_entity_id
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFeatureEntity',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/featureentities',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFeatureEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_feature_entity(
        self,
        instance_id: str,
        request: main_models.CreateFeatureEntityRequest,
    ) -> main_models.CreateFeatureEntityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_feature_entity_with_options(instance_id, request, headers, runtime)

    async def create_feature_entity_async(
        self,
        instance_id: str,
        request: main_models.CreateFeatureEntityRequest,
    ) -> main_models.CreateFeatureEntityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_feature_entity_with_options_async(instance_id, request, headers, runtime)

    def create_feature_view_with_options(
        self,
        instance_id: str,
        request: main_models.CreateFeatureViewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateFeatureViewResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.feature_entity_id):
            body['FeatureEntityId'] = request.feature_entity_id
        if not DaraCore.is_null(request.fields):
            body['Fields'] = request.fields
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.register_datasource_id):
            body['RegisterDatasourceId'] = request.register_datasource_id
        if not DaraCore.is_null(request.register_table):
            body['RegisterTable'] = request.register_table
        if not DaraCore.is_null(request.sync_online_table):
            body['SyncOnlineTable'] = request.sync_online_table
        if not DaraCore.is_null(request.ttl):
            body['TTL'] = request.ttl
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.write_method):
            body['WriteMethod'] = request.write_method
        if not DaraCore.is_null(request.write_to_feature_db):
            body['WriteToFeatureDB'] = request.write_to_feature_db
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFeatureView',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/featureviews',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFeatureViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_feature_view_with_options_async(
        self,
        instance_id: str,
        request: main_models.CreateFeatureViewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateFeatureViewResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.feature_entity_id):
            body['FeatureEntityId'] = request.feature_entity_id
        if not DaraCore.is_null(request.fields):
            body['Fields'] = request.fields
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.register_datasource_id):
            body['RegisterDatasourceId'] = request.register_datasource_id
        if not DaraCore.is_null(request.register_table):
            body['RegisterTable'] = request.register_table
        if not DaraCore.is_null(request.sync_online_table):
            body['SyncOnlineTable'] = request.sync_online_table
        if not DaraCore.is_null(request.ttl):
            body['TTL'] = request.ttl
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.write_method):
            body['WriteMethod'] = request.write_method
        if not DaraCore.is_null(request.write_to_feature_db):
            body['WriteToFeatureDB'] = request.write_to_feature_db
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFeatureView',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/featureviews',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFeatureViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_feature_view(
        self,
        instance_id: str,
        request: main_models.CreateFeatureViewRequest,
    ) -> main_models.CreateFeatureViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_feature_view_with_options(instance_id, request, headers, runtime)

    async def create_feature_view_async(
        self,
        instance_id: str,
        request: main_models.CreateFeatureViewRequest,
    ) -> main_models.CreateFeatureViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_feature_view_with_options_async(instance_id, request, headers, runtime)

    def create_instance_with_options(
        self,
        request: main_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: main_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_instance_with_options(request, headers, runtime)

    async def create_instance_async(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_instance_with_options_async(request, headers, runtime)

    def create_llmconfig_with_options(
        self,
        instance_id: str,
        request: main_models.CreateLLMConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLLMConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['ApiKey'] = request.api_key
        if not DaraCore.is_null(request.base_url):
            body['BaseUrl'] = request.base_url
        if not DaraCore.is_null(request.batch_size):
            body['BatchSize'] = request.batch_size
        if not DaraCore.is_null(request.max_tokens):
            body['MaxTokens'] = request.max_tokens
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.rps):
            body['Rps'] = request.rps
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLLMConfig',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/llmconfigs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLLMConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_llmconfig_with_options_async(
        self,
        instance_id: str,
        request: main_models.CreateLLMConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLLMConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['ApiKey'] = request.api_key
        if not DaraCore.is_null(request.base_url):
            body['BaseUrl'] = request.base_url
        if not DaraCore.is_null(request.batch_size):
            body['BatchSize'] = request.batch_size
        if not DaraCore.is_null(request.max_tokens):
            body['MaxTokens'] = request.max_tokens
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.rps):
            body['Rps'] = request.rps
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLLMConfig',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/llmconfigs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLLMConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_llmconfig(
        self,
        instance_id: str,
        request: main_models.CreateLLMConfigRequest,
    ) -> main_models.CreateLLMConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_llmconfig_with_options(instance_id, request, headers, runtime)

    async def create_llmconfig_async(
        self,
        instance_id: str,
        request: main_models.CreateLLMConfigRequest,
    ) -> main_models.CreateLLMConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_llmconfig_with_options_async(instance_id, request, headers, runtime)

    def create_label_table_with_options(
        self,
        instance_id: str,
        request: main_models.CreateLabelTableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLabelTableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.datasource_id):
            body['DatasourceId'] = request.datasource_id
        if not DaraCore.is_null(request.fields):
            body['Fields'] = request.fields
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLabelTable',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/labeltables',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLabelTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_label_table_with_options_async(
        self,
        instance_id: str,
        request: main_models.CreateLabelTableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLabelTableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.datasource_id):
            body['DatasourceId'] = request.datasource_id
        if not DaraCore.is_null(request.fields):
            body['Fields'] = request.fields
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLabelTable',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/labeltables',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLabelTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_label_table(
        self,
        instance_id: str,
        request: main_models.CreateLabelTableRequest,
    ) -> main_models.CreateLabelTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_label_table_with_options(instance_id, request, headers, runtime)

    async def create_label_table_async(
        self,
        instance_id: str,
        request: main_models.CreateLabelTableRequest,
    ) -> main_models.CreateLabelTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_label_table_with_options_async(instance_id, request, headers, runtime)

    def create_model_feature_with_options(
        self,
        instance_id: str,
        request: main_models.CreateModelFeatureRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelFeatureResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.features):
            body['Features'] = request.features
        if not DaraCore.is_null(request.label_priority_level):
            body['LabelPriorityLevel'] = request.label_priority_level
        if not DaraCore.is_null(request.label_table_id):
            body['LabelTableId'] = request.label_table_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sequence_feature_view_ids):
            body['SequenceFeatureViewIds'] = request.sequence_feature_view_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModelFeature',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/modelfeatures',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_model_feature_with_options_async(
        self,
        instance_id: str,
        request: main_models.CreateModelFeatureRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateModelFeatureResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.features):
            body['Features'] = request.features
        if not DaraCore.is_null(request.label_priority_level):
            body['LabelPriorityLevel'] = request.label_priority_level
        if not DaraCore.is_null(request.label_table_id):
            body['LabelTableId'] = request.label_table_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            body['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sequence_feature_view_ids):
            body['SequenceFeatureViewIds'] = request.sequence_feature_view_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModelFeature',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/modelfeatures',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModelFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_model_feature(
        self,
        instance_id: str,
        request: main_models.CreateModelFeatureRequest,
    ) -> main_models.CreateModelFeatureResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_model_feature_with_options(instance_id, request, headers, runtime)

    async def create_model_feature_async(
        self,
        instance_id: str,
        request: main_models.CreateModelFeatureRequest,
    ) -> main_models.CreateModelFeatureResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_model_feature_with_options_async(instance_id, request, headers, runtime)

    def create_project_with_options(
        self,
        instance_id: str,
        request: main_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.offline_datasource_id):
            body['OfflineDatasourceId'] = request.offline_datasource_id
        if not DaraCore.is_null(request.offline_life_cycle):
            body['OfflineLifeCycle'] = request.offline_life_cycle
        if not DaraCore.is_null(request.online_datasource_id):
            body['OnlineDatasourceId'] = request.online_datasource_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProject',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/projects',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_with_options_async(
        self,
        instance_id: str,
        request: main_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.offline_datasource_id):
            body['OfflineDatasourceId'] = request.offline_datasource_id
        if not DaraCore.is_null(request.offline_life_cycle):
            body['OfflineLifeCycle'] = request.offline_life_cycle
        if not DaraCore.is_null(request.online_datasource_id):
            body['OnlineDatasourceId'] = request.online_datasource_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProject',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/projects',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project(
        self,
        instance_id: str,
        request: main_models.CreateProjectRequest,
    ) -> main_models.CreateProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_project_with_options(instance_id, request, headers, runtime)

    async def create_project_async(
        self,
        instance_id: str,
        request: main_models.CreateProjectRequest,
    ) -> main_models.CreateProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_project_with_options_async(instance_id, request, headers, runtime)

    def create_service_identity_role_with_options(
        self,
        request: main_models.CreateServiceIdentityRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceIdentityRoleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.role_name):
            body['RoleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceIdentityRole',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/serviceidentityroles',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceIdentityRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_identity_role_with_options_async(
        self,
        request: main_models.CreateServiceIdentityRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceIdentityRoleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.role_name):
            body['RoleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceIdentityRole',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/serviceidentityroles',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceIdentityRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_identity_role(
        self,
        request: main_models.CreateServiceIdentityRoleRequest,
    ) -> main_models.CreateServiceIdentityRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_service_identity_role_with_options(request, headers, runtime)

    async def create_service_identity_role_async(
        self,
        request: main_models.CreateServiceIdentityRoleRequest,
    ) -> main_models.CreateServiceIdentityRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_service_identity_role_with_options_async(request, headers, runtime)

    def delete_datasource_with_options(
        self,
        instance_id: str,
        datasource_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDatasource',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/datasources/{DaraURL.percent_encode(datasource_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_datasource_with_options_async(
        self,
        instance_id: str,
        datasource_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDatasource',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/datasources/{DaraURL.percent_encode(datasource_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_datasource(
        self,
        instance_id: str,
        datasource_id: str,
    ) -> main_models.DeleteDatasourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_datasource_with_options(instance_id, datasource_id, headers, runtime)

    async def delete_datasource_async(
        self,
        instance_id: str,
        datasource_id: str,
    ) -> main_models.DeleteDatasourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_datasource_with_options_async(instance_id, datasource_id, headers, runtime)

    def delete_feature_entity_with_options(
        self,
        instance_id: str,
        feature_entity_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFeatureEntityResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteFeatureEntity',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/featureentities/{DaraURL.percent_encode(feature_entity_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFeatureEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_feature_entity_with_options_async(
        self,
        instance_id: str,
        feature_entity_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFeatureEntityResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteFeatureEntity',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/featureentities/{DaraURL.percent_encode(feature_entity_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFeatureEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_feature_entity(
        self,
        instance_id: str,
        feature_entity_id: str,
    ) -> main_models.DeleteFeatureEntityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_feature_entity_with_options(instance_id, feature_entity_id, headers, runtime)

    async def delete_feature_entity_async(
        self,
        instance_id: str,
        feature_entity_id: str,
    ) -> main_models.DeleteFeatureEntityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_feature_entity_with_options_async(instance_id, feature_entity_id, headers, runtime)

    def delete_feature_view_with_options(
        self,
        instance_id: str,
        feature_view_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFeatureViewResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteFeatureView',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/featureviews/{DaraURL.percent_encode(feature_view_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFeatureViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_feature_view_with_options_async(
        self,
        instance_id: str,
        feature_view_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFeatureViewResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteFeatureView',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/featureviews/{DaraURL.percent_encode(feature_view_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFeatureViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_feature_view(
        self,
        instance_id: str,
        feature_view_id: str,
    ) -> main_models.DeleteFeatureViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_feature_view_with_options(instance_id, feature_view_id, headers, runtime)

    async def delete_feature_view_async(
        self,
        instance_id: str,
        feature_view_id: str,
    ) -> main_models.DeleteFeatureViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_feature_view_with_options_async(instance_id, feature_view_id, headers, runtime)

    def delete_llmconfig_with_options(
        self,
        instance_id: str,
        llmconfig_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLLMConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteLLMConfig',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/llmconfigs/{DaraURL.percent_encode(llmconfig_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLLMConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_llmconfig_with_options_async(
        self,
        instance_id: str,
        llmconfig_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLLMConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteLLMConfig',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/llmconfigs/{DaraURL.percent_encode(llmconfig_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLLMConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_llmconfig(
        self,
        instance_id: str,
        llmconfig_id: str,
    ) -> main_models.DeleteLLMConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_llmconfig_with_options(instance_id, llmconfig_id, headers, runtime)

    async def delete_llmconfig_async(
        self,
        instance_id: str,
        llmconfig_id: str,
    ) -> main_models.DeleteLLMConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_llmconfig_with_options_async(instance_id, llmconfig_id, headers, runtime)

    def delete_label_table_with_options(
        self,
        instance_id: str,
        label_table_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLabelTableResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteLabelTable',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/labeltables/{DaraURL.percent_encode(label_table_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLabelTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_label_table_with_options_async(
        self,
        instance_id: str,
        label_table_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLabelTableResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteLabelTable',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/labeltables/{DaraURL.percent_encode(label_table_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLabelTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_label_table(
        self,
        instance_id: str,
        label_table_id: str,
    ) -> main_models.DeleteLabelTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_label_table_with_options(instance_id, label_table_id, headers, runtime)

    async def delete_label_table_async(
        self,
        instance_id: str,
        label_table_id: str,
    ) -> main_models.DeleteLabelTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_label_table_with_options_async(instance_id, label_table_id, headers, runtime)

    def delete_model_feature_with_options(
        self,
        instance_id: str,
        model_feature_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelFeatureResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteModelFeature',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/modelfeatures/{DaraURL.percent_encode(model_feature_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_model_feature_with_options_async(
        self,
        instance_id: str,
        model_feature_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModelFeatureResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteModelFeature',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/modelfeatures/{DaraURL.percent_encode(model_feature_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModelFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_model_feature(
        self,
        instance_id: str,
        model_feature_id: str,
    ) -> main_models.DeleteModelFeatureResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_model_feature_with_options(instance_id, model_feature_id, headers, runtime)

    async def delete_model_feature_async(
        self,
        instance_id: str,
        model_feature_id: str,
    ) -> main_models.DeleteModelFeatureResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_model_feature_with_options_async(instance_id, model_feature_id, headers, runtime)

    def delete_project_with_options(
        self,
        instance_id: str,
        project_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProjectResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteProject',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/projects/{DaraURL.percent_encode(project_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        instance_id: str,
        project_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProjectResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteProject',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/projects/{DaraURL.percent_encode(project_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_project(
        self,
        instance_id: str,
        project_id: str,
    ) -> main_models.DeleteProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_project_with_options(instance_id, project_id, headers, runtime)

    async def delete_project_async(
        self,
        instance_id: str,
        project_id: str,
    ) -> main_models.DeleteProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_project_with_options_async(instance_id, project_id, headers, runtime)

    def export_model_feature_training_set_table_with_options(
        self,
        instance_id: str,
        model_feature_id: str,
        request: main_models.ExportModelFeatureTrainingSetTableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExportModelFeatureTrainingSetTableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.feature_view_config):
            body['FeatureViewConfig'] = request.feature_view_config
        if not DaraCore.is_null(request.label_input_config):
            body['LabelInputConfig'] = request.label_input_config
        if not DaraCore.is_null(request.real_time_iterate_interval):
            body['RealTimeIterateInterval'] = request.real_time_iterate_interval
        if not DaraCore.is_null(request.real_time_partition_count_value):
            body['RealTimePartitionCountValue'] = request.real_time_partition_count_value
        if not DaraCore.is_null(request.training_set_config):
            body['TrainingSetConfig'] = request.training_set_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportModelFeatureTrainingSetTable',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/modelfeatures/{DaraURL.percent_encode(model_feature_id)}/action/exporttrainingsettable',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportModelFeatureTrainingSetTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_model_feature_training_set_table_with_options_async(
        self,
        instance_id: str,
        model_feature_id: str,
        request: main_models.ExportModelFeatureTrainingSetTableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExportModelFeatureTrainingSetTableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.feature_view_config):
            body['FeatureViewConfig'] = request.feature_view_config
        if not DaraCore.is_null(request.label_input_config):
            body['LabelInputConfig'] = request.label_input_config
        if not DaraCore.is_null(request.real_time_iterate_interval):
            body['RealTimeIterateInterval'] = request.real_time_iterate_interval
        if not DaraCore.is_null(request.real_time_partition_count_value):
            body['RealTimePartitionCountValue'] = request.real_time_partition_count_value
        if not DaraCore.is_null(request.training_set_config):
            body['TrainingSetConfig'] = request.training_set_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportModelFeatureTrainingSetTable',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/modelfeatures/{DaraURL.percent_encode(model_feature_id)}/action/exporttrainingsettable',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportModelFeatureTrainingSetTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_model_feature_training_set_table(
        self,
        instance_id: str,
        model_feature_id: str,
        request: main_models.ExportModelFeatureTrainingSetTableRequest,
    ) -> main_models.ExportModelFeatureTrainingSetTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.export_model_feature_training_set_table_with_options(instance_id, model_feature_id, request, headers, runtime)

    async def export_model_feature_training_set_table_async(
        self,
        instance_id: str,
        model_feature_id: str,
        request: main_models.ExportModelFeatureTrainingSetTableRequest,
    ) -> main_models.ExportModelFeatureTrainingSetTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.export_model_feature_training_set_table_with_options_async(instance_id, model_feature_id, request, headers, runtime)

    def get_datasource_with_options(
        self,
        instance_id: str,
        datasource_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDatasource',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/datasources/{DaraURL.percent_encode(datasource_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_datasource_with_options_async(
        self,
        instance_id: str,
        datasource_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDatasource',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/datasources/{DaraURL.percent_encode(datasource_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_datasource(
        self,
        instance_id: str,
        datasource_id: str,
    ) -> main_models.GetDatasourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_datasource_with_options(instance_id, datasource_id, headers, runtime)

    async def get_datasource_async(
        self,
        instance_id: str,
        datasource_id: str,
    ) -> main_models.GetDatasourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_datasource_with_options_async(instance_id, datasource_id, headers, runtime)

    def get_datasource_table_with_options(
        self,
        instance_id: str,
        datasource_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasourceTableResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDatasourceTable',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/datasources/{DaraURL.percent_encode(datasource_id)}/tables/{DaraURL.percent_encode(table_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasourceTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_datasource_table_with_options_async(
        self,
        instance_id: str,
        datasource_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasourceTableResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDatasourceTable',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/datasources/{DaraURL.percent_encode(datasource_id)}/tables/{DaraURL.percent_encode(table_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasourceTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_datasource_table(
        self,
        instance_id: str,
        datasource_id: str,
        table_name: str,
    ) -> main_models.GetDatasourceTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_datasource_table_with_options(instance_id, datasource_id, table_name, headers, runtime)

    async def get_datasource_table_async(
        self,
        instance_id: str,
        datasource_id: str,
        table_name: str,
    ) -> main_models.GetDatasourceTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_datasource_table_with_options_async(instance_id, datasource_id, table_name, headers, runtime)

    def get_feature_entity_with_options(
        self,
        instance_id: str,
        feature_entity_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFeatureEntityResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetFeatureEntity',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/featureentities/{DaraURL.percent_encode(feature_entity_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFeatureEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_feature_entity_with_options_async(
        self,
        instance_id: str,
        feature_entity_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFeatureEntityResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetFeatureEntity',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/featureentities/{DaraURL.percent_encode(feature_entity_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFeatureEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_feature_entity(
        self,
        instance_id: str,
        feature_entity_id: str,
    ) -> main_models.GetFeatureEntityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_feature_entity_with_options(instance_id, feature_entity_id, headers, runtime)

    async def get_feature_entity_async(
        self,
        instance_id: str,
        feature_entity_id: str,
    ) -> main_models.GetFeatureEntityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_feature_entity_with_options_async(instance_id, feature_entity_id, headers, runtime)

    def get_feature_view_with_options(
        self,
        instance_id: str,
        feature_view_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFeatureViewResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetFeatureView',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/featureviews/{DaraURL.percent_encode(feature_view_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFeatureViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_feature_view_with_options_async(
        self,
        instance_id: str,
        feature_view_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFeatureViewResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetFeatureView',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/featureviews/{DaraURL.percent_encode(feature_view_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFeatureViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_feature_view(
        self,
        instance_id: str,
        feature_view_id: str,
    ) -> main_models.GetFeatureViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_feature_view_with_options(instance_id, feature_view_id, headers, runtime)

    async def get_feature_view_async(
        self,
        instance_id: str,
        feature_view_id: str,
    ) -> main_models.GetFeatureViewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_feature_view_with_options_async(instance_id, feature_view_id, headers, runtime)

    def get_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetInstance',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetInstance',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        instance_id: str,
    ) -> main_models.GetInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(instance_id, headers, runtime)

    async def get_instance_async(
        self,
        instance_id: str,
    ) -> main_models.GetInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_instance_with_options_async(instance_id, headers, runtime)

    def get_llmconfig_with_options(
        self,
        instance_id: str,
        llmconfig_id: str,
        region_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLLMConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLLMConfig',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/llmconfigs/{DaraURL.percent_encode(llmconfig_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLLMConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_llmconfig_with_options_async(
        self,
        instance_id: str,
        llmconfig_id: str,
        region_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLLMConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLLMConfig',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/llmconfigs/{DaraURL.percent_encode(llmconfig_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLLMConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_llmconfig(
        self,
        instance_id: str,
        llmconfig_id: str,
        region_id: str,
    ) -> main_models.GetLLMConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_llmconfig_with_options(instance_id, llmconfig_id, region_id, headers, runtime)

    async def get_llmconfig_async(
        self,
        instance_id: str,
        llmconfig_id: str,
        region_id: str,
    ) -> main_models.GetLLMConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_llmconfig_with_options_async(instance_id, llmconfig_id, region_id, headers, runtime)

    def get_label_table_with_options(
        self,
        instance_id: str,
        label_table_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLabelTableResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLabelTable',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/labeltables/{DaraURL.percent_encode(label_table_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLabelTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_label_table_with_options_async(
        self,
        instance_id: str,
        label_table_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLabelTableResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLabelTable',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/labeltables/{DaraURL.percent_encode(label_table_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLabelTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_label_table(
        self,
        instance_id: str,
        label_table_id: str,
    ) -> main_models.GetLabelTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_label_table_with_options(instance_id, label_table_id, headers, runtime)

    async def get_label_table_async(
        self,
        instance_id: str,
        label_table_id: str,
    ) -> main_models.GetLabelTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_label_table_with_options_async(instance_id, label_table_id, headers, runtime)

    def get_model_feature_with_options(
        self,
        instance_id: str,
        model_feature_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetModelFeatureResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetModelFeature',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/modelfeatures/{DaraURL.percent_encode(model_feature_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModelFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_model_feature_with_options_async(
        self,
        instance_id: str,
        model_feature_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetModelFeatureResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetModelFeature',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/modelfeatures/{DaraURL.percent_encode(model_feature_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModelFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_model_feature(
        self,
        instance_id: str,
        model_feature_id: str,
    ) -> main_models.GetModelFeatureResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_model_feature_with_options(instance_id, model_feature_id, headers, runtime)

    async def get_model_feature_async(
        self,
        instance_id: str,
        model_feature_id: str,
    ) -> main_models.GetModelFeatureResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_model_feature_with_options_async(instance_id, model_feature_id, headers, runtime)

    def get_model_feature_fgfeature_with_options(
        self,
        instance_id: str,
        model_feature_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetModelFeatureFGFeatureResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetModelFeatureFGFeature',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/modelfeatures/{DaraURL.percent_encode(model_feature_id)}/fgfeature',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModelFeatureFGFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_model_feature_fgfeature_with_options_async(
        self,
        instance_id: str,
        model_feature_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetModelFeatureFGFeatureResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetModelFeatureFGFeature',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/modelfeatures/{DaraURL.percent_encode(model_feature_id)}/fgfeature',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModelFeatureFGFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_model_feature_fgfeature(
        self,
        instance_id: str,
        model_feature_id: str,
    ) -> main_models.GetModelFeatureFGFeatureResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_model_feature_fgfeature_with_options(instance_id, model_feature_id, headers, runtime)

    async def get_model_feature_fgfeature_async(
        self,
        instance_id: str,
        model_feature_id: str,
    ) -> main_models.GetModelFeatureFGFeatureResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_model_feature_fgfeature_with_options_async(instance_id, model_feature_id, headers, runtime)

    def get_model_feature_fginfo_with_options(
        self,
        instance_id: str,
        model_feature_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetModelFeatureFGInfoResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetModelFeatureFGInfo',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/modelfeatures/{DaraURL.percent_encode(model_feature_id)}/fginfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModelFeatureFGInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_model_feature_fginfo_with_options_async(
        self,
        instance_id: str,
        model_feature_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetModelFeatureFGInfoResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetModelFeatureFGInfo',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/modelfeatures/{DaraURL.percent_encode(model_feature_id)}/fginfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModelFeatureFGInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_model_feature_fginfo(
        self,
        instance_id: str,
        model_feature_id: str,
    ) -> main_models.GetModelFeatureFGInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_model_feature_fginfo_with_options(instance_id, model_feature_id, headers, runtime)

    async def get_model_feature_fginfo_async(
        self,
        instance_id: str,
        model_feature_id: str,
    ) -> main_models.GetModelFeatureFGInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_model_feature_fginfo_with_options_async(instance_id, model_feature_id, headers, runtime)

    def get_project_with_options(
        self,
        instance_id: str,
        project_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetProject',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/projects/{DaraURL.percent_encode(project_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_with_options_async(
        self,
        instance_id: str,
        project_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetProject',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/projects/{DaraURL.percent_encode(project_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project(
        self,
        instance_id: str,
        project_id: str,
    ) -> main_models.GetProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_project_with_options(instance_id, project_id, headers, runtime)

    async def get_project_async(
        self,
        instance_id: str,
        project_id: str,
    ) -> main_models.GetProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_project_with_options_async(instance_id, project_id, headers, runtime)

    def get_project_feature_entity_with_options(
        self,
        instance_id: str,
        project_id: str,
        feature_entity_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectFeatureEntityResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetProjectFeatureEntity',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/projects/{DaraURL.percent_encode(project_id)}/featureentities/{DaraURL.percent_encode(feature_entity_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectFeatureEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_feature_entity_with_options_async(
        self,
        instance_id: str,
        project_id: str,
        feature_entity_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectFeatureEntityResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetProjectFeatureEntity',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/projects/{DaraURL.percent_encode(project_id)}/featureentities/{DaraURL.percent_encode(feature_entity_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectFeatureEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project_feature_entity(
        self,
        instance_id: str,
        project_id: str,
        feature_entity_name: str,
    ) -> main_models.GetProjectFeatureEntityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_project_feature_entity_with_options(instance_id, project_id, feature_entity_name, headers, runtime)

    async def get_project_feature_entity_async(
        self,
        instance_id: str,
        project_id: str,
        feature_entity_name: str,
    ) -> main_models.GetProjectFeatureEntityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_project_feature_entity_with_options_async(instance_id, project_id, feature_entity_name, headers, runtime)

    def get_service_identity_role_with_options(
        self,
        role_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceIdentityRoleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetServiceIdentityRole',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/serviceidentityroles/{DaraURL.percent_encode(role_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceIdentityRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_identity_role_with_options_async(
        self,
        role_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceIdentityRoleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetServiceIdentityRole',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/serviceidentityroles/{DaraURL.percent_encode(role_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceIdentityRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_identity_role(
        self,
        role_name: str,
    ) -> main_models.GetServiceIdentityRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_service_identity_role_with_options(role_name, headers, runtime)

    async def get_service_identity_role_async(
        self,
        role_name: str,
    ) -> main_models.GetServiceIdentityRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_service_identity_role_with_options_async(role_name, headers, runtime)

    def get_task_with_options(
        self,
        instance_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTask',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/tasks/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_with_options_async(
        self,
        instance_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTask',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/tasks/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task(
        self,
        instance_id: str,
        task_id: str,
    ) -> main_models.GetTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_task_with_options(instance_id, task_id, headers, runtime)

    async def get_task_async(
        self,
        instance_id: str,
        task_id: str,
    ) -> main_models.GetTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_task_with_options_async(instance_id, task_id, headers, runtime)

    def list_datasource_feature_views_with_options(
        self,
        instance_id: str,
        datasource_id: str,
        request: main_models.ListDatasourceFeatureViewsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasourceFeatureViewsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.show_storage_usage):
            query['ShowStorageUsage'] = request.show_storage_usage
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasourceFeatureViews',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/datasources/{DaraURL.percent_encode(datasource_id)}/featureviews',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasourceFeatureViewsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_datasource_feature_views_with_options_async(
        self,
        instance_id: str,
        datasource_id: str,
        request: main_models.ListDatasourceFeatureViewsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasourceFeatureViewsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.show_storage_usage):
            query['ShowStorageUsage'] = request.show_storage_usage
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasourceFeatureViews',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/datasources/{DaraURL.percent_encode(datasource_id)}/featureviews',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasourceFeatureViewsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_datasource_feature_views(
        self,
        instance_id: str,
        datasource_id: str,
        request: main_models.ListDatasourceFeatureViewsRequest,
    ) -> main_models.ListDatasourceFeatureViewsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_datasource_feature_views_with_options(instance_id, datasource_id, request, headers, runtime)

    async def list_datasource_feature_views_async(
        self,
        instance_id: str,
        datasource_id: str,
        request: main_models.ListDatasourceFeatureViewsRequest,
    ) -> main_models.ListDatasourceFeatureViewsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_datasource_feature_views_with_options_async(instance_id, datasource_id, request, headers, runtime)

    def list_datasource_tables_with_options(
        self,
        instance_id: str,
        datasource_id: str,
        request: main_models.ListDatasourceTablesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasourceTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasourceTables',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/datasources/{DaraURL.percent_encode(datasource_id)}/tables',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasourceTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_datasource_tables_with_options_async(
        self,
        instance_id: str,
        datasource_id: str,
        request: main_models.ListDatasourceTablesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasourceTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasourceTables',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/datasources/{DaraURL.percent_encode(datasource_id)}/tables',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasourceTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_datasource_tables(
        self,
        instance_id: str,
        datasource_id: str,
        request: main_models.ListDatasourceTablesRequest,
    ) -> main_models.ListDatasourceTablesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_datasource_tables_with_options(instance_id, datasource_id, request, headers, runtime)

    async def list_datasource_tables_async(
        self,
        instance_id: str,
        datasource_id: str,
        request: main_models.ListDatasourceTablesRequest,
    ) -> main_models.ListDatasourceTablesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_datasource_tables_with_options_async(instance_id, datasource_id, request, headers, runtime)

    def list_datasources_with_options(
        self,
        instance_id: str,
        request: main_models.ListDatasourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasources',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/datasources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_datasources_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListDatasourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasources',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/datasources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_datasources(
        self,
        instance_id: str,
        request: main_models.ListDatasourcesRequest,
    ) -> main_models.ListDatasourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_datasources_with_options(instance_id, request, headers, runtime)

    async def list_datasources_async(
        self,
        instance_id: str,
        request: main_models.ListDatasourcesRequest,
    ) -> main_models.ListDatasourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_datasources_with_options_async(instance_id, request, headers, runtime)

    def list_feature_entities_with_options(
        self,
        instance_id: str,
        tmp_req: main_models.ListFeatureEntitiesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFeatureEntitiesResponse:
        tmp_req.validate()
        request = main_models.ListFeatureEntitiesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.feature_entity_ids):
            request.feature_entity_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.feature_entity_ids, 'FeatureEntityIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.feature_entity_ids_shrink):
            query['FeatureEntityIds'] = request.feature_entity_ids_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_feature_entity_id):
            query['ParentFeatureEntityId'] = request.parent_feature_entity_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFeatureEntities',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/featureentities',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFeatureEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_feature_entities_with_options_async(
        self,
        instance_id: str,
        tmp_req: main_models.ListFeatureEntitiesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFeatureEntitiesResponse:
        tmp_req.validate()
        request = main_models.ListFeatureEntitiesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.feature_entity_ids):
            request.feature_entity_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.feature_entity_ids, 'FeatureEntityIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.feature_entity_ids_shrink):
            query['FeatureEntityIds'] = request.feature_entity_ids_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_feature_entity_id):
            query['ParentFeatureEntityId'] = request.parent_feature_entity_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFeatureEntities',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/featureentities',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFeatureEntitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_feature_entities(
        self,
        instance_id: str,
        request: main_models.ListFeatureEntitiesRequest,
    ) -> main_models.ListFeatureEntitiesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_feature_entities_with_options(instance_id, request, headers, runtime)

    async def list_feature_entities_async(
        self,
        instance_id: str,
        request: main_models.ListFeatureEntitiesRequest,
    ) -> main_models.ListFeatureEntitiesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_feature_entities_with_options_async(instance_id, request, headers, runtime)

    def list_feature_view_field_relationships_with_options(
        self,
        instance_id: str,
        feature_view_id: str,
        field_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFeatureViewFieldRelationshipsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListFeatureViewFieldRelationships',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/featureviews/{DaraURL.percent_encode(feature_view_id)}/fields/{DaraURL.percent_encode(field_name)}/relationships',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFeatureViewFieldRelationshipsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_feature_view_field_relationships_with_options_async(
        self,
        instance_id: str,
        feature_view_id: str,
        field_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFeatureViewFieldRelationshipsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListFeatureViewFieldRelationships',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/featureviews/{DaraURL.percent_encode(feature_view_id)}/fields/{DaraURL.percent_encode(field_name)}/relationships',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFeatureViewFieldRelationshipsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_feature_view_field_relationships(
        self,
        instance_id: str,
        feature_view_id: str,
        field_name: str,
    ) -> main_models.ListFeatureViewFieldRelationshipsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_feature_view_field_relationships_with_options(instance_id, feature_view_id, field_name, headers, runtime)

    async def list_feature_view_field_relationships_async(
        self,
        instance_id: str,
        feature_view_id: str,
        field_name: str,
    ) -> main_models.ListFeatureViewFieldRelationshipsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_feature_view_field_relationships_with_options_async(instance_id, feature_view_id, field_name, headers, runtime)

    def list_feature_view_online_features_with_options(
        self,
        instance_id: str,
        feature_view_id: str,
        tmp_req: main_models.ListFeatureViewOnlineFeaturesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFeatureViewOnlineFeaturesResponse:
        tmp_req.validate()
        request = main_models.ListFeatureViewOnlineFeaturesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.join_ids):
            request.join_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.join_ids, 'JoinIds', 'json')
        query = {}
        if not DaraCore.is_null(request.join_ids_shrink):
            query['JoinIds'] = request.join_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFeatureViewOnlineFeatures',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/featureviews/{DaraURL.percent_encode(feature_view_id)}/onlinefeatures',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFeatureViewOnlineFeaturesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_feature_view_online_features_with_options_async(
        self,
        instance_id: str,
        feature_view_id: str,
        tmp_req: main_models.ListFeatureViewOnlineFeaturesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFeatureViewOnlineFeaturesResponse:
        tmp_req.validate()
        request = main_models.ListFeatureViewOnlineFeaturesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.join_ids):
            request.join_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.join_ids, 'JoinIds', 'json')
        query = {}
        if not DaraCore.is_null(request.join_ids_shrink):
            query['JoinIds'] = request.join_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFeatureViewOnlineFeatures',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/featureviews/{DaraURL.percent_encode(feature_view_id)}/onlinefeatures',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFeatureViewOnlineFeaturesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_feature_view_online_features(
        self,
        instance_id: str,
        feature_view_id: str,
        request: main_models.ListFeatureViewOnlineFeaturesRequest,
    ) -> main_models.ListFeatureViewOnlineFeaturesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_feature_view_online_features_with_options(instance_id, feature_view_id, request, headers, runtime)

    async def list_feature_view_online_features_async(
        self,
        instance_id: str,
        feature_view_id: str,
        request: main_models.ListFeatureViewOnlineFeaturesRequest,
    ) -> main_models.ListFeatureViewOnlineFeaturesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_feature_view_online_features_with_options_async(instance_id, feature_view_id, request, headers, runtime)

    def list_feature_view_relationships_with_options(
        self,
        instance_id: str,
        feature_view_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFeatureViewRelationshipsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListFeatureViewRelationships',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/featureviews/{DaraURL.percent_encode(feature_view_id)}/relationships',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFeatureViewRelationshipsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_feature_view_relationships_with_options_async(
        self,
        instance_id: str,
        feature_view_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFeatureViewRelationshipsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListFeatureViewRelationships',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/featureviews/{DaraURL.percent_encode(feature_view_id)}/relationships',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFeatureViewRelationshipsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_feature_view_relationships(
        self,
        instance_id: str,
        feature_view_id: str,
    ) -> main_models.ListFeatureViewRelationshipsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_feature_view_relationships_with_options(instance_id, feature_view_id, headers, runtime)

    async def list_feature_view_relationships_async(
        self,
        instance_id: str,
        feature_view_id: str,
    ) -> main_models.ListFeatureViewRelationshipsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_feature_view_relationships_with_options_async(instance_id, feature_view_id, headers, runtime)

    def list_feature_views_with_options(
        self,
        instance_id: str,
        tmp_req: main_models.ListFeatureViewsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFeatureViewsResponse:
        tmp_req.validate()
        request = main_models.ListFeatureViewsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.feature_view_ids):
            request.feature_view_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.feature_view_ids, 'FeatureViewIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not DaraCore.is_null(request.feature_view_ids_shrink):
            query['FeatureViewIds'] = request.feature_view_ids_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFeatureViews',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/featureviews',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFeatureViewsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_feature_views_with_options_async(
        self,
        instance_id: str,
        tmp_req: main_models.ListFeatureViewsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFeatureViewsResponse:
        tmp_req.validate()
        request = main_models.ListFeatureViewsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.feature_view_ids):
            request.feature_view_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.feature_view_ids, 'FeatureViewIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not DaraCore.is_null(request.feature_view_ids_shrink):
            query['FeatureViewIds'] = request.feature_view_ids_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFeatureViews',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/featureviews',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFeatureViewsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_feature_views(
        self,
        instance_id: str,
        request: main_models.ListFeatureViewsRequest,
    ) -> main_models.ListFeatureViewsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_feature_views_with_options(instance_id, request, headers, runtime)

    async def list_feature_views_async(
        self,
        instance_id: str,
        request: main_models.ListFeatureViewsRequest,
    ) -> main_models.ListFeatureViewsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_feature_views_with_options_async(instance_id, request, headers, runtime)

    def list_instances_with_options(
        self,
        request: main_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: main_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: main_models.ListInstancesRequest,
    ) -> main_models.ListInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    async def list_instances_async(
        self,
        request: main_models.ListInstancesRequest,
    ) -> main_models.ListInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_instances_with_options_async(request, headers, runtime)

    def list_llmconfigs_with_options(
        self,
        instance_id: str,
        request: main_models.ListLLMConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLLMConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLLMConfigs',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/llmconfigs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLLMConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_llmconfigs_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListLLMConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLLMConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLLMConfigs',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/llmconfigs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLLMConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_llmconfigs(
        self,
        instance_id: str,
        request: main_models.ListLLMConfigsRequest,
    ) -> main_models.ListLLMConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_llmconfigs_with_options(instance_id, request, headers, runtime)

    async def list_llmconfigs_async(
        self,
        instance_id: str,
        request: main_models.ListLLMConfigsRequest,
    ) -> main_models.ListLLMConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_llmconfigs_with_options_async(instance_id, request, headers, runtime)

    def list_label_tables_with_options(
        self,
        instance_id: str,
        tmp_req: main_models.ListLabelTablesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLabelTablesResponse:
        tmp_req.validate()
        request = main_models.ListLabelTablesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.label_table_ids):
            request.label_table_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.label_table_ids, 'LabelTableIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.label_table_ids_shrink):
            query['LabelTableIds'] = request.label_table_ids_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLabelTables',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/labeltables',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLabelTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_label_tables_with_options_async(
        self,
        instance_id: str,
        tmp_req: main_models.ListLabelTablesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLabelTablesResponse:
        tmp_req.validate()
        request = main_models.ListLabelTablesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.label_table_ids):
            request.label_table_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.label_table_ids, 'LabelTableIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.label_table_ids_shrink):
            query['LabelTableIds'] = request.label_table_ids_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLabelTables',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/labeltables',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLabelTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_label_tables(
        self,
        instance_id: str,
        request: main_models.ListLabelTablesRequest,
    ) -> main_models.ListLabelTablesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_label_tables_with_options(instance_id, request, headers, runtime)

    async def list_label_tables_async(
        self,
        instance_id: str,
        request: main_models.ListLabelTablesRequest,
    ) -> main_models.ListLabelTablesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_label_tables_with_options_async(instance_id, request, headers, runtime)

    def list_model_feature_available_features_with_options(
        self,
        instance_id: str,
        model_feature_id: str,
        request: main_models.ListModelFeatureAvailableFeaturesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModelFeatureAvailableFeaturesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_name):
            query['FeatureName'] = request.feature_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModelFeatureAvailableFeatures',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/modelfeatures/{DaraURL.percent_encode(model_feature_id)}/availablefeatures',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelFeatureAvailableFeaturesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_model_feature_available_features_with_options_async(
        self,
        instance_id: str,
        model_feature_id: str,
        request: main_models.ListModelFeatureAvailableFeaturesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModelFeatureAvailableFeaturesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_name):
            query['FeatureName'] = request.feature_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModelFeatureAvailableFeatures',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/modelfeatures/{DaraURL.percent_encode(model_feature_id)}/availablefeatures',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelFeatureAvailableFeaturesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_model_feature_available_features(
        self,
        instance_id: str,
        model_feature_id: str,
        request: main_models.ListModelFeatureAvailableFeaturesRequest,
    ) -> main_models.ListModelFeatureAvailableFeaturesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_model_feature_available_features_with_options(instance_id, model_feature_id, request, headers, runtime)

    async def list_model_feature_available_features_async(
        self,
        instance_id: str,
        model_feature_id: str,
        request: main_models.ListModelFeatureAvailableFeaturesRequest,
    ) -> main_models.ListModelFeatureAvailableFeaturesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_model_feature_available_features_with_options_async(instance_id, model_feature_id, request, headers, runtime)

    def list_model_features_with_options(
        self,
        instance_id: str,
        tmp_req: main_models.ListModelFeaturesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModelFeaturesResponse:
        tmp_req.validate()
        request = main_models.ListModelFeaturesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.model_feature_ids):
            request.model_feature_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.model_feature_ids, 'ModelFeatureIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.model_feature_ids_shrink):
            query['ModelFeatureIds'] = request.model_feature_ids_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModelFeatures',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/modelfeatures',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelFeaturesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_model_features_with_options_async(
        self,
        instance_id: str,
        tmp_req: main_models.ListModelFeaturesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModelFeaturesResponse:
        tmp_req.validate()
        request = main_models.ListModelFeaturesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.model_feature_ids):
            request.model_feature_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.model_feature_ids, 'ModelFeatureIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.model_feature_ids_shrink):
            query['ModelFeatureIds'] = request.model_feature_ids_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModelFeatures',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/modelfeatures',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelFeaturesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_model_features(
        self,
        instance_id: str,
        request: main_models.ListModelFeaturesRequest,
    ) -> main_models.ListModelFeaturesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_model_features_with_options(instance_id, request, headers, runtime)

    async def list_model_features_async(
        self,
        instance_id: str,
        request: main_models.ListModelFeaturesRequest,
    ) -> main_models.ListModelFeaturesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_model_features_with_options_async(instance_id, request, headers, runtime)

    def list_project_feature_views_with_options(
        self,
        instance_id: str,
        project_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectFeatureViewsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListProjectFeatureViews',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/projects/{DaraURL.percent_encode(project_id)}/featureviews',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectFeatureViewsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_feature_views_with_options_async(
        self,
        instance_id: str,
        project_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectFeatureViewsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListProjectFeatureViews',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/projects/{DaraURL.percent_encode(project_id)}/featureviews',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectFeatureViewsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project_feature_views(
        self,
        instance_id: str,
        project_id: str,
    ) -> main_models.ListProjectFeatureViewsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_project_feature_views_with_options(instance_id, project_id, headers, runtime)

    async def list_project_feature_views_async(
        self,
        instance_id: str,
        project_id: str,
    ) -> main_models.ListProjectFeatureViewsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_project_feature_views_with_options_async(instance_id, project_id, headers, runtime)

    def list_project_features_with_options(
        self,
        instance_id: str,
        project_id: str,
        request: main_models.ListProjectFeaturesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectFeaturesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alias_name):
            query['AliasName'] = request.alias_name
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProjectFeatures',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/projects/{DaraURL.percent_encode(project_id)}/features',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectFeaturesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_features_with_options_async(
        self,
        instance_id: str,
        project_id: str,
        request: main_models.ListProjectFeaturesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectFeaturesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alias_name):
            query['AliasName'] = request.alias_name
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProjectFeatures',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/projects/{DaraURL.percent_encode(project_id)}/features',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectFeaturesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project_features(
        self,
        instance_id: str,
        project_id: str,
        request: main_models.ListProjectFeaturesRequest,
    ) -> main_models.ListProjectFeaturesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_project_features_with_options(instance_id, project_id, request, headers, runtime)

    async def list_project_features_async(
        self,
        instance_id: str,
        project_id: str,
        request: main_models.ListProjectFeaturesRequest,
    ) -> main_models.ListProjectFeaturesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_project_features_with_options_async(instance_id, project_id, request, headers, runtime)

    def list_projects_with_options(
        self,
        instance_id: str,
        tmp_req: main_models.ListProjectsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectsResponse:
        tmp_req.validate()
        request = main_models.ListProjectsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.project_ids):
            request.project_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.project_ids, 'ProjectIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_ids_shrink):
            query['ProjectIds'] = request.project_ids_shrink
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProjects',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/projects',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_projects_with_options_async(
        self,
        instance_id: str,
        tmp_req: main_models.ListProjectsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectsResponse:
        tmp_req.validate()
        request = main_models.ListProjectsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.project_ids):
            request.project_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.project_ids, 'ProjectIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_ids_shrink):
            query['ProjectIds'] = request.project_ids_shrink
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProjects',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/projects',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_projects(
        self,
        instance_id: str,
        request: main_models.ListProjectsRequest,
    ) -> main_models.ListProjectsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_projects_with_options(instance_id, request, headers, runtime)

    async def list_projects_async(
        self,
        instance_id: str,
        request: main_models.ListProjectsRequest,
    ) -> main_models.ListProjectsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_projects_with_options_async(instance_id, request, headers, runtime)

    def list_task_logs_with_options(
        self,
        instance_id: str,
        task_id: str,
        request: main_models.ListTaskLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTaskLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTaskLogs',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/tasks/{DaraURL.percent_encode(task_id)}/logs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTaskLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_task_logs_with_options_async(
        self,
        instance_id: str,
        task_id: str,
        request: main_models.ListTaskLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTaskLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTaskLogs',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/tasks/{DaraURL.percent_encode(task_id)}/logs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTaskLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_task_logs(
        self,
        instance_id: str,
        task_id: str,
        request: main_models.ListTaskLogsRequest,
    ) -> main_models.ListTaskLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_task_logs_with_options(instance_id, task_id, request, headers, runtime)

    async def list_task_logs_async(
        self,
        instance_id: str,
        task_id: str,
        request: main_models.ListTaskLogsRequest,
    ) -> main_models.ListTaskLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_task_logs_with_options_async(instance_id, task_id, request, headers, runtime)

    def list_tasks_with_options(
        self,
        instance_id: str,
        tmp_req: main_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTasksResponse:
        tmp_req.validate()
        request = main_models.ListTasksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_ids):
            request.task_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.object_id):
            query['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.object_type):
            query['ObjectType'] = request.object_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_ids_shrink):
            query['TaskIds'] = request.task_ids_shrink
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTasks',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tasks_with_options_async(
        self,
        instance_id: str,
        tmp_req: main_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTasksResponse:
        tmp_req.validate()
        request = main_models.ListTasksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_ids):
            request.task_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.object_id):
            query['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.object_type):
            query['ObjectType'] = request.object_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_ids_shrink):
            query['TaskIds'] = request.task_ids_shrink
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTasks',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tasks(
        self,
        instance_id: str,
        request: main_models.ListTasksRequest,
    ) -> main_models.ListTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_tasks_with_options(instance_id, request, headers, runtime)

    async def list_tasks_async(
        self,
        instance_id: str,
        request: main_models.ListTasksRequest,
    ) -> main_models.ListTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_tasks_with_options_async(instance_id, request, headers, runtime)

    def publish_feature_view_table_with_options(
        self,
        instance_id: str,
        feature_view_id: str,
        request: main_models.PublishFeatureViewTableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PublishFeatureViewTableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.event_time):
            body['EventTime'] = request.event_time
        if not DaraCore.is_null(request.mode):
            body['Mode'] = request.mode
        if not DaraCore.is_null(request.offline_to_online):
            body['OfflineToOnline'] = request.offline_to_online
        if not DaraCore.is_null(request.partitions):
            body['Partitions'] = request.partitions
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PublishFeatureViewTable',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/featureviews/{DaraURL.percent_encode(feature_view_id)}/action/publishtable',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishFeatureViewTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_feature_view_table_with_options_async(
        self,
        instance_id: str,
        feature_view_id: str,
        request: main_models.PublishFeatureViewTableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PublishFeatureViewTableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.event_time):
            body['EventTime'] = request.event_time
        if not DaraCore.is_null(request.mode):
            body['Mode'] = request.mode
        if not DaraCore.is_null(request.offline_to_online):
            body['OfflineToOnline'] = request.offline_to_online
        if not DaraCore.is_null(request.partitions):
            body['Partitions'] = request.partitions
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PublishFeatureViewTable',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/featureviews/{DaraURL.percent_encode(feature_view_id)}/action/publishtable',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishFeatureViewTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_feature_view_table(
        self,
        instance_id: str,
        feature_view_id: str,
        request: main_models.PublishFeatureViewTableRequest,
    ) -> main_models.PublishFeatureViewTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.publish_feature_view_table_with_options(instance_id, feature_view_id, request, headers, runtime)

    async def publish_feature_view_table_async(
        self,
        instance_id: str,
        feature_view_id: str,
        request: main_models.PublishFeatureViewTableRequest,
    ) -> main_models.PublishFeatureViewTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.publish_feature_view_table_with_options_async(instance_id, feature_view_id, request, headers, runtime)

    def stop_task_with_options(
        self,
        instance_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopTask',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/tasks/{DaraURL.percent_encode(task_id)}/action/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_task_with_options_async(
        self,
        instance_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopTask',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/tasks/{DaraURL.percent_encode(task_id)}/action/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_task(
        self,
        instance_id: str,
        task_id: str,
    ) -> main_models.StopTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_task_with_options(instance_id, task_id, headers, runtime)

    async def stop_task_async(
        self,
        instance_id: str,
        task_id: str,
    ) -> main_models.StopTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_task_with_options_async(instance_id, task_id, headers, runtime)

    def update_datasource_with_options(
        self,
        instance_id: str,
        datasource_id: str,
        request: main_models.UpdateDatasourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDatasourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.uri):
            body['Uri'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDatasource',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/datasources/{DaraURL.percent_encode(datasource_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDatasourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_datasource_with_options_async(
        self,
        instance_id: str,
        datasource_id: str,
        request: main_models.UpdateDatasourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDatasourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.uri):
            body['Uri'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDatasource',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/datasources/{DaraURL.percent_encode(datasource_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDatasourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_datasource(
        self,
        instance_id: str,
        datasource_id: str,
        request: main_models.UpdateDatasourceRequest,
    ) -> main_models.UpdateDatasourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_datasource_with_options(instance_id, datasource_id, request, headers, runtime)

    async def update_datasource_async(
        self,
        instance_id: str,
        datasource_id: str,
        request: main_models.UpdateDatasourceRequest,
    ) -> main_models.UpdateDatasourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_datasource_with_options_async(instance_id, datasource_id, request, headers, runtime)

    def update_llmconfig_with_options(
        self,
        instance_id: str,
        llmconfig_id: str,
        request: main_models.UpdateLLMConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLLMConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['ApiKey'] = request.api_key
        if not DaraCore.is_null(request.base_url):
            body['BaseUrl'] = request.base_url
        if not DaraCore.is_null(request.batch_size):
            body['BatchSize'] = request.batch_size
        if not DaraCore.is_null(request.max_tokens):
            body['MaxTokens'] = request.max_tokens
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.rps):
            body['Rps'] = request.rps
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLLMConfig',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/llmconfigs/{DaraURL.percent_encode(llmconfig_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLLMConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_llmconfig_with_options_async(
        self,
        instance_id: str,
        llmconfig_id: str,
        request: main_models.UpdateLLMConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLLMConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['ApiKey'] = request.api_key
        if not DaraCore.is_null(request.base_url):
            body['BaseUrl'] = request.base_url
        if not DaraCore.is_null(request.batch_size):
            body['BatchSize'] = request.batch_size
        if not DaraCore.is_null(request.max_tokens):
            body['MaxTokens'] = request.max_tokens
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.rps):
            body['Rps'] = request.rps
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLLMConfig',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/llmconfigs/{DaraURL.percent_encode(llmconfig_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLLMConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_llmconfig(
        self,
        instance_id: str,
        llmconfig_id: str,
        request: main_models.UpdateLLMConfigRequest,
    ) -> main_models.UpdateLLMConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_llmconfig_with_options(instance_id, llmconfig_id, request, headers, runtime)

    async def update_llmconfig_async(
        self,
        instance_id: str,
        llmconfig_id: str,
        request: main_models.UpdateLLMConfigRequest,
    ) -> main_models.UpdateLLMConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_llmconfig_with_options_async(instance_id, llmconfig_id, request, headers, runtime)

    def update_label_table_with_options(
        self,
        instance_id: str,
        label_table_id: str,
        request: main_models.UpdateLabelTableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLabelTableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.datasource_id):
            body['DatasourceId'] = request.datasource_id
        if not DaraCore.is_null(request.fields):
            body['Fields'] = request.fields
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLabelTable',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/labeltables/{DaraURL.percent_encode(label_table_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLabelTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_label_table_with_options_async(
        self,
        instance_id: str,
        label_table_id: str,
        request: main_models.UpdateLabelTableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLabelTableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.datasource_id):
            body['DatasourceId'] = request.datasource_id
        if not DaraCore.is_null(request.fields):
            body['Fields'] = request.fields
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLabelTable',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/labeltables/{DaraURL.percent_encode(label_table_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLabelTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_label_table(
        self,
        instance_id: str,
        label_table_id: str,
        request: main_models.UpdateLabelTableRequest,
    ) -> main_models.UpdateLabelTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_label_table_with_options(instance_id, label_table_id, request, headers, runtime)

    async def update_label_table_async(
        self,
        instance_id: str,
        label_table_id: str,
        request: main_models.UpdateLabelTableRequest,
    ) -> main_models.UpdateLabelTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_label_table_with_options_async(instance_id, label_table_id, request, headers, runtime)

    def update_model_feature_with_options(
        self,
        instance_id: str,
        model_feature_id: str,
        request: main_models.UpdateModelFeatureRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateModelFeatureResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.features):
            body['Features'] = request.features
        if not DaraCore.is_null(request.label_priority_level):
            body['LabelPriorityLevel'] = request.label_priority_level
        if not DaraCore.is_null(request.label_table_id):
            body['LabelTableId'] = request.label_table_id
        if not DaraCore.is_null(request.sequence_feature_view_ids):
            body['SequenceFeatureViewIds'] = request.sequence_feature_view_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateModelFeature',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/modelfeatures/{DaraURL.percent_encode(model_feature_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateModelFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_model_feature_with_options_async(
        self,
        instance_id: str,
        model_feature_id: str,
        request: main_models.UpdateModelFeatureRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateModelFeatureResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.features):
            body['Features'] = request.features
        if not DaraCore.is_null(request.label_priority_level):
            body['LabelPriorityLevel'] = request.label_priority_level
        if not DaraCore.is_null(request.label_table_id):
            body['LabelTableId'] = request.label_table_id
        if not DaraCore.is_null(request.sequence_feature_view_ids):
            body['SequenceFeatureViewIds'] = request.sequence_feature_view_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateModelFeature',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/modelfeatures/{DaraURL.percent_encode(model_feature_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateModelFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_model_feature(
        self,
        instance_id: str,
        model_feature_id: str,
        request: main_models.UpdateModelFeatureRequest,
    ) -> main_models.UpdateModelFeatureResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_model_feature_with_options(instance_id, model_feature_id, request, headers, runtime)

    async def update_model_feature_async(
        self,
        instance_id: str,
        model_feature_id: str,
        request: main_models.UpdateModelFeatureRequest,
    ) -> main_models.UpdateModelFeatureResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_model_feature_with_options_async(instance_id, model_feature_id, request, headers, runtime)

    def update_model_feature_fgfeature_with_options(
        self,
        instance_id: str,
        model_feature_id: str,
        request: main_models.UpdateModelFeatureFGFeatureRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateModelFeatureFGFeatureResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lookup_features):
            body['LookupFeatures'] = request.lookup_features
        if not DaraCore.is_null(request.raw_features):
            body['RawFeatures'] = request.raw_features
        if not DaraCore.is_null(request.reserves):
            body['Reserves'] = request.reserves
        if not DaraCore.is_null(request.sequence_features):
            body['SequenceFeatures'] = request.sequence_features
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateModelFeatureFGFeature',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/modelfeatures/{DaraURL.percent_encode(model_feature_id)}/fgfeature',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateModelFeatureFGFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_model_feature_fgfeature_with_options_async(
        self,
        instance_id: str,
        model_feature_id: str,
        request: main_models.UpdateModelFeatureFGFeatureRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateModelFeatureFGFeatureResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lookup_features):
            body['LookupFeatures'] = request.lookup_features
        if not DaraCore.is_null(request.raw_features):
            body['RawFeatures'] = request.raw_features
        if not DaraCore.is_null(request.reserves):
            body['Reserves'] = request.reserves
        if not DaraCore.is_null(request.sequence_features):
            body['SequenceFeatures'] = request.sequence_features
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateModelFeatureFGFeature',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/modelfeatures/{DaraURL.percent_encode(model_feature_id)}/fgfeature',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateModelFeatureFGFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_model_feature_fgfeature(
        self,
        instance_id: str,
        model_feature_id: str,
        request: main_models.UpdateModelFeatureFGFeatureRequest,
    ) -> main_models.UpdateModelFeatureFGFeatureResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_model_feature_fgfeature_with_options(instance_id, model_feature_id, request, headers, runtime)

    async def update_model_feature_fgfeature_async(
        self,
        instance_id: str,
        model_feature_id: str,
        request: main_models.UpdateModelFeatureFGFeatureRequest,
    ) -> main_models.UpdateModelFeatureFGFeatureResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_model_feature_fgfeature_with_options_async(instance_id, model_feature_id, request, headers, runtime)

    def update_project_with_options(
        self,
        instance_id: str,
        project_id: str,
        request: main_models.UpdateProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProject',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/projects/{DaraURL.percent_encode(project_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_with_options_async(
        self,
        instance_id: str,
        project_id: str,
        request: main_models.UpdateProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProject',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/projects/{DaraURL.percent_encode(project_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project(
        self,
        instance_id: str,
        project_id: str,
        request: main_models.UpdateProjectRequest,
    ) -> main_models.UpdateProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_project_with_options(instance_id, project_id, request, headers, runtime)

    async def update_project_async(
        self,
        instance_id: str,
        project_id: str,
        request: main_models.UpdateProjectRequest,
    ) -> main_models.UpdateProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_project_with_options_async(instance_id, project_id, request, headers, runtime)

    def write_feature_view_table_with_options(
        self,
        instance_id: str,
        feature_view_id: str,
        request: main_models.WriteFeatureViewTableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.WriteFeatureViewTableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.mode):
            body['Mode'] = request.mode
        if not DaraCore.is_null(request.partitions):
            body['Partitions'] = request.partitions
        if not DaraCore.is_null(request.url_datasource):
            body['UrlDatasource'] = request.url_datasource
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'WriteFeatureViewTable',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/featureviews/{DaraURL.percent_encode(feature_view_id)}/action/writetable',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WriteFeatureViewTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def write_feature_view_table_with_options_async(
        self,
        instance_id: str,
        feature_view_id: str,
        request: main_models.WriteFeatureViewTableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.WriteFeatureViewTableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.mode):
            body['Mode'] = request.mode
        if not DaraCore.is_null(request.partitions):
            body['Partitions'] = request.partitions
        if not DaraCore.is_null(request.url_datasource):
            body['UrlDatasource'] = request.url_datasource
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'WriteFeatureViewTable',
            version = '2023-06-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/featureviews/{DaraURL.percent_encode(feature_view_id)}/action/writetable',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WriteFeatureViewTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def write_feature_view_table(
        self,
        instance_id: str,
        feature_view_id: str,
        request: main_models.WriteFeatureViewTableRequest,
    ) -> main_models.WriteFeatureViewTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.write_feature_view_table_with_options(instance_id, feature_view_id, request, headers, runtime)

    async def write_feature_view_table_async(
        self,
        instance_id: str,
        feature_view_id: str,
        request: main_models.WriteFeatureViewTableRequest,
    ) -> main_models.WriteFeatureViewTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.write_feature_view_table_with_options_async(instance_id, feature_view_id, request, headers, runtime)
