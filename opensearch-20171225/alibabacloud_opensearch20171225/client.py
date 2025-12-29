# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_opensearch20171225 import models as main_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('opensearch', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def bind_esuser_analyzer_with_options(
        self,
        app_group_identity: str,
        es_instance_id: str,
        request: main_models.BindESUserAnalyzerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BindESUserAnalyzerResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'BindESUserAnalyzer',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/es/{DaraURL.percent_encode(es_instance_id)}/actions/bind-analyzer',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindESUserAnalyzerResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_esuser_analyzer_with_options_async(
        self,
        app_group_identity: str,
        es_instance_id: str,
        request: main_models.BindESUserAnalyzerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BindESUserAnalyzerResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'BindESUserAnalyzer',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/es/{DaraURL.percent_encode(es_instance_id)}/actions/bind-analyzer',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindESUserAnalyzerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_esuser_analyzer(
        self,
        app_group_identity: str,
        es_instance_id: str,
        request: main_models.BindESUserAnalyzerRequest,
    ) -> main_models.BindESUserAnalyzerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.bind_esuser_analyzer_with_options(app_group_identity, es_instance_id, request, headers, runtime)

    async def bind_esuser_analyzer_async(
        self,
        app_group_identity: str,
        es_instance_id: str,
        request: main_models.BindESUserAnalyzerRequest,
    ) -> main_models.BindESUserAnalyzerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.bind_esuser_analyzer_with_options_async(app_group_identity, es_instance_id, request, headers, runtime)

    def bind_es_instance_with_options(
        self,
        app_group_identity: str,
        request: main_models.BindEsInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BindEsInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.body):
            body['body'] = request.body
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BindEsInstance',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/actions/bind-es-instance',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindEsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_es_instance_with_options_async(
        self,
        app_group_identity: str,
        request: main_models.BindEsInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BindEsInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.body):
            body['body'] = request.body
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BindEsInstance',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/actions/bind-es-instance',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindEsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_es_instance(
        self,
        app_group_identity: str,
        request: main_models.BindEsInstanceRequest,
    ) -> main_models.BindEsInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.bind_es_instance_with_options(app_group_identity, request, headers, runtime)

    async def bind_es_instance_async(
        self,
        app_group_identity: str,
        request: main_models.BindEsInstanceRequest,
    ) -> main_models.BindEsInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.bind_es_instance_with_options_async(app_group_identity, request, headers, runtime)

    def compile_sort_script_with_options(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CompileSortScriptResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CompileSortScript',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_version_id)}/sort-scripts/{DaraURL.percent_encode(script_name)}/actions/compiling',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompileSortScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def compile_sort_script_with_options_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CompileSortScriptResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CompileSortScript',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_version_id)}/sort-scripts/{DaraURL.percent_encode(script_name)}/actions/compiling',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompileSortScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def compile_sort_script(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
    ) -> main_models.CompileSortScriptResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.compile_sort_script_with_options(app_group_identity, script_name, app_version_id, headers, runtime)

    async def compile_sort_script_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
    ) -> main_models.CompileSortScriptResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.compile_sort_script_with_options_async(app_group_identity, script_name, app_version_id, headers, runtime)

    def create_abtest_experiment_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        request: main_models.CreateABTestExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateABTestExperimentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateABTestExperiment',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}/groups/{DaraURL.percent_encode(group_id)}/experiments',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateABTestExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_abtest_experiment_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        request: main_models.CreateABTestExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateABTestExperimentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateABTestExperiment',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}/groups/{DaraURL.percent_encode(group_id)}/experiments',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateABTestExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_abtest_experiment(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        request: main_models.CreateABTestExperimentRequest,
    ) -> main_models.CreateABTestExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_abtest_experiment_with_options(app_group_identity, scene_id, group_id, request, headers, runtime)

    async def create_abtest_experiment_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        request: main_models.CreateABTestExperimentRequest,
    ) -> main_models.CreateABTestExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_abtest_experiment_with_options_async(app_group_identity, scene_id, group_id, request, headers, runtime)

    def create_abtest_group_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        request: main_models.CreateABTestGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateABTestGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateABTestGroup',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}/groups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateABTestGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_abtest_group_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        request: main_models.CreateABTestGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateABTestGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateABTestGroup',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}/groups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateABTestGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_abtest_group(
        self,
        app_group_identity: str,
        scene_id: str,
        request: main_models.CreateABTestGroupRequest,
    ) -> main_models.CreateABTestGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_abtest_group_with_options(app_group_identity, scene_id, request, headers, runtime)

    async def create_abtest_group_async(
        self,
        app_group_identity: str,
        scene_id: str,
        request: main_models.CreateABTestGroupRequest,
    ) -> main_models.CreateABTestGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_abtest_group_with_options_async(app_group_identity, scene_id, request, headers, runtime)

    def create_abtest_scene_with_options(
        self,
        app_group_identity: str,
        request: main_models.CreateABTestSceneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateABTestSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateABTestScene',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateABTestSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_abtest_scene_with_options_async(
        self,
        app_group_identity: str,
        request: main_models.CreateABTestSceneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateABTestSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateABTestScene',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateABTestSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_abtest_scene(
        self,
        app_group_identity: str,
        request: main_models.CreateABTestSceneRequest,
    ) -> main_models.CreateABTestSceneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_abtest_scene_with_options(app_group_identity, request, headers, runtime)

    async def create_abtest_scene_async(
        self,
        app_group_identity: str,
        request: main_models.CreateABTestSceneRequest,
    ) -> main_models.CreateABTestSceneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_abtest_scene_with_options_async(app_group_identity, request, headers, runtime)

    def create_app_with_options(
        self,
        app_group_identity: str,
        request: main_models.CreateAppRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.auto_switch):
            body['autoSwitch'] = request.auto_switch
        if not DaraCore.is_null(request.cluster):
            body['cluster'] = request.cluster
        if not DaraCore.is_null(request.config_items):
            body['configItems'] = request.config_items
        if not DaraCore.is_null(request.data_sources):
            body['dataSources'] = request.data_sources
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.domain):
            body['domain'] = request.domain
        if not DaraCore.is_null(request.fetch_fields):
            body['fetchFields'] = request.fetch_fields
        if not DaraCore.is_null(request.first_ranks):
            body['firstRanks'] = request.first_ranks
        if not DaraCore.is_null(request.interpretations):
            body['interpretations'] = request.interpretations
        if not DaraCore.is_null(request.network_type):
            body['networkType'] = request.network_type
        if not DaraCore.is_null(request.prompts):
            body['prompts'] = request.prompts
        if not DaraCore.is_null(request.query_processors):
            body['queryProcessors'] = request.query_processors
        if not DaraCore.is_null(request.realtime_shared):
            body['realtimeShared'] = request.realtime_shared
        if not DaraCore.is_null(request.schema):
            body['schema'] = request.schema
        if not DaraCore.is_null(request.schemas):
            body['schemas'] = request.schemas
        if not DaraCore.is_null(request.second_ranks):
            body['secondRanks'] = request.second_ranks
        if not DaraCore.is_null(request.summaries):
            body['summaries'] = request.summaries
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateApp',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_with_options_async(
        self,
        app_group_identity: str,
        request: main_models.CreateAppRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.auto_switch):
            body['autoSwitch'] = request.auto_switch
        if not DaraCore.is_null(request.cluster):
            body['cluster'] = request.cluster
        if not DaraCore.is_null(request.config_items):
            body['configItems'] = request.config_items
        if not DaraCore.is_null(request.data_sources):
            body['dataSources'] = request.data_sources
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.domain):
            body['domain'] = request.domain
        if not DaraCore.is_null(request.fetch_fields):
            body['fetchFields'] = request.fetch_fields
        if not DaraCore.is_null(request.first_ranks):
            body['firstRanks'] = request.first_ranks
        if not DaraCore.is_null(request.interpretations):
            body['interpretations'] = request.interpretations
        if not DaraCore.is_null(request.network_type):
            body['networkType'] = request.network_type
        if not DaraCore.is_null(request.prompts):
            body['prompts'] = request.prompts
        if not DaraCore.is_null(request.query_processors):
            body['queryProcessors'] = request.query_processors
        if not DaraCore.is_null(request.realtime_shared):
            body['realtimeShared'] = request.realtime_shared
        if not DaraCore.is_null(request.schema):
            body['schema'] = request.schema
        if not DaraCore.is_null(request.schemas):
            body['schemas'] = request.schemas
        if not DaraCore.is_null(request.second_ranks):
            body['secondRanks'] = request.second_ranks
        if not DaraCore.is_null(request.summaries):
            body['summaries'] = request.summaries
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateApp',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app(
        self,
        app_group_identity: str,
        request: main_models.CreateAppRequest,
    ) -> main_models.CreateAppResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_app_with_options(app_group_identity, request, headers, runtime)

    async def create_app_async(
        self,
        app_group_identity: str,
        request: main_models.CreateAppRequest,
    ) -> main_models.CreateAppResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_app_with_options_async(app_group_identity, request, headers, runtime)

    def create_app_group_with_options(
        self,
        request: main_models.CreateAppGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.charge_type):
            body['chargeType'] = request.charge_type
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.quota):
            body['quota'] = request.quota
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppGroup',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_group_with_options_async(
        self,
        request: main_models.CreateAppGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.charge_type):
            body['chargeType'] = request.charge_type
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.quota):
            body['quota'] = request.quota
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppGroup',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_group(
        self,
        request: main_models.CreateAppGroupRequest,
    ) -> main_models.CreateAppGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_app_group_with_options(request, headers, runtime)

    async def create_app_group_async(
        self,
        request: main_models.CreateAppGroupRequest,
    ) -> main_models.CreateAppGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_app_group_with_options_async(request, headers, runtime)

    def create_app_group_credentials_with_options(
        self,
        app_group_identity: str,
        request: main_models.CreateAppGroupCredentialsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppGroupCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppGroupCredentials',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/credentials',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppGroupCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_group_credentials_with_options_async(
        self,
        app_group_identity: str,
        request: main_models.CreateAppGroupCredentialsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppGroupCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppGroupCredentials',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/credentials',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppGroupCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_group_credentials(
        self,
        app_group_identity: str,
        request: main_models.CreateAppGroupCredentialsRequest,
    ) -> main_models.CreateAppGroupCredentialsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_app_group_credentials_with_options(app_group_identity, request, headers, runtime)

    async def create_app_group_credentials_async(
        self,
        app_group_identity: str,
        request: main_models.CreateAppGroupCredentialsRequest,
    ) -> main_models.CreateAppGroupCredentialsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_app_group_credentials_with_options_async(app_group_identity, request, headers, runtime)

    def create_first_rank_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        request: main_models.CreateFirstRankRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateFirstRankResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFirstRank',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/first-ranks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFirstRankResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_first_rank_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: main_models.CreateFirstRankRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateFirstRankResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFirstRank',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/first-ranks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFirstRankResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_first_rank(
        self,
        app_group_identity: str,
        app_id: str,
        request: main_models.CreateFirstRankRequest,
    ) -> main_models.CreateFirstRankResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_first_rank_with_options(app_group_identity, app_id, request, headers, runtime)

    async def create_first_rank_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: main_models.CreateFirstRankRequest,
    ) -> main_models.CreateFirstRankResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_first_rank_with_options_async(app_group_identity, app_id, request, headers, runtime)

    def create_function_instance_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        request: main_models.CreateFunctionInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateFunctionInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.create_parameters):
            body['createParameters'] = request.create_parameters
        if not DaraCore.is_null(request.cron):
            body['cron'] = request.cron
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.function_type):
            body['functionType'] = request.function_type
        if not DaraCore.is_null(request.instance_name):
            body['instanceName'] = request.instance_name
        if not DaraCore.is_null(request.model_type):
            body['modelType'] = request.model_type
        if not DaraCore.is_null(request.usage_parameters):
            body['usageParameters'] = request.usage_parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFunctionInstance',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/instances',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFunctionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_function_instance_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        request: main_models.CreateFunctionInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateFunctionInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.create_parameters):
            body['createParameters'] = request.create_parameters
        if not DaraCore.is_null(request.cron):
            body['cron'] = request.cron
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.function_type):
            body['functionType'] = request.function_type
        if not DaraCore.is_null(request.instance_name):
            body['instanceName'] = request.instance_name
        if not DaraCore.is_null(request.model_type):
            body['modelType'] = request.model_type
        if not DaraCore.is_null(request.usage_parameters):
            body['usageParameters'] = request.usage_parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFunctionInstance',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/instances',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFunctionInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_function_instance(
        self,
        app_group_identity: str,
        function_name: str,
        request: main_models.CreateFunctionInstanceRequest,
    ) -> main_models.CreateFunctionInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_function_instance_with_options(app_group_identity, function_name, request, headers, runtime)

    async def create_function_instance_async(
        self,
        app_group_identity: str,
        function_name: str,
        request: main_models.CreateFunctionInstanceRequest,
    ) -> main_models.CreateFunctionInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_function_instance_with_options_async(app_group_identity, function_name, request, headers, runtime)

    def create_function_resource_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        request: main_models.CreateFunctionResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateFunctionResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.resource_name):
            body['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFunctionResource',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/resources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFunctionResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_function_resource_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        request: main_models.CreateFunctionResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateFunctionResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.resource_name):
            body['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFunctionResource',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/resources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFunctionResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_function_resource(
        self,
        app_group_identity: str,
        function_name: str,
        request: main_models.CreateFunctionResourceRequest,
    ) -> main_models.CreateFunctionResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_function_resource_with_options(app_group_identity, function_name, request, headers, runtime)

    async def create_function_resource_async(
        self,
        app_group_identity: str,
        function_name: str,
        request: main_models.CreateFunctionResourceRequest,
    ) -> main_models.CreateFunctionResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_function_resource_with_options_async(app_group_identity, function_name, request, headers, runtime)

    def create_function_task_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateFunctionTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CreateFunctionTask',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/instances/{DaraURL.percent_encode(instance_name)}/tasks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFunctionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_function_task_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateFunctionTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CreateFunctionTask',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/instances/{DaraURL.percent_encode(instance_name)}/tasks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFunctionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_function_task(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
    ) -> main_models.CreateFunctionTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_function_task_with_options(app_group_identity, function_name, instance_name, headers, runtime)

    async def create_function_task_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
    ) -> main_models.CreateFunctionTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_function_task_with_options_async(app_group_identity, function_name, instance_name, headers, runtime)

    def create_intervention_dictionary_with_options(
        self,
        request: main_models.CreateInterventionDictionaryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInterventionDictionaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.analyzer_type):
            body['analyzerType'] = request.analyzer_type
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInterventionDictionary',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/intervention-dictionaries',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInterventionDictionaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_intervention_dictionary_with_options_async(
        self,
        request: main_models.CreateInterventionDictionaryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInterventionDictionaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.analyzer_type):
            body['analyzerType'] = request.analyzer_type
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInterventionDictionary',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/intervention-dictionaries',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInterventionDictionaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_intervention_dictionary(
        self,
        request: main_models.CreateInterventionDictionaryRequest,
    ) -> main_models.CreateInterventionDictionaryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_intervention_dictionary_with_options(request, headers, runtime)

    async def create_intervention_dictionary_async(
        self,
        request: main_models.CreateInterventionDictionaryRequest,
    ) -> main_models.CreateInterventionDictionaryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_intervention_dictionary_with_options_async(request, headers, runtime)

    def create_query_processor_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        request: main_models.CreateQueryProcessorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateQueryProcessorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'CreateQueryProcessor',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/query-processors',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQueryProcessorResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_query_processor_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: main_models.CreateQueryProcessorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateQueryProcessorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'CreateQueryProcessor',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/query-processors',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQueryProcessorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_query_processor(
        self,
        app_group_identity: str,
        app_id: str,
        request: main_models.CreateQueryProcessorRequest,
    ) -> main_models.CreateQueryProcessorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_query_processor_with_options(app_group_identity, app_id, request, headers, runtime)

    async def create_query_processor_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: main_models.CreateQueryProcessorRequest,
    ) -> main_models.CreateQueryProcessorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_query_processor_with_options_async(app_group_identity, app_id, request, headers, runtime)

    def create_scheduled_task_with_options(
        self,
        app_group_identity: str,
        request: main_models.CreateScheduledTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateScheduledTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateScheduledTask',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scheduled-tasks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scheduled_task_with_options_async(
        self,
        app_group_identity: str,
        request: main_models.CreateScheduledTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateScheduledTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateScheduledTask',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scheduled-tasks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScheduledTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scheduled_task(
        self,
        app_group_identity: str,
        request: main_models.CreateScheduledTaskRequest,
    ) -> main_models.CreateScheduledTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_scheduled_task_with_options(app_group_identity, request, headers, runtime)

    async def create_scheduled_task_async(
        self,
        app_group_identity: str,
        request: main_models.CreateScheduledTaskRequest,
    ) -> main_models.CreateScheduledTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_scheduled_task_with_options_async(app_group_identity, request, headers, runtime)

    def create_search_strategy_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        request: main_models.CreateSearchStrategyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSearchStrategyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSearchStrategy',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/search-strategies',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSearchStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_search_strategy_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: main_models.CreateSearchStrategyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSearchStrategyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSearchStrategy',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/search-strategies',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSearchStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_search_strategy(
        self,
        app_group_identity: str,
        app_id: str,
        request: main_models.CreateSearchStrategyRequest,
    ) -> main_models.CreateSearchStrategyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_search_strategy_with_options(app_group_identity, app_id, request, headers, runtime)

    async def create_search_strategy_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: main_models.CreateSearchStrategyRequest,
    ) -> main_models.CreateSearchStrategyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_search_strategy_with_options_async(app_group_identity, app_id, request, headers, runtime)

    def create_second_rank_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        request: main_models.CreateSecondRankRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSecondRankResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecondRank',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/second-ranks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSecondRankResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_second_rank_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: main_models.CreateSecondRankRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSecondRankResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecondRank',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/second-ranks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSecondRankResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_second_rank(
        self,
        app_group_identity: str,
        app_id: str,
        request: main_models.CreateSecondRankRequest,
    ) -> main_models.CreateSecondRankResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_second_rank_with_options(app_group_identity, app_id, request, headers, runtime)

    async def create_second_rank_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: main_models.CreateSecondRankRequest,
    ) -> main_models.CreateSecondRankResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_second_rank_with_options_async(app_group_identity, app_id, request, headers, runtime)

    def create_sort_script_with_options(
        self,
        app_group_identity: str,
        app_version_id: str,
        request: main_models.CreateSortScriptRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSortScriptResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.scope):
            body['scope'] = request.scope
        if not DaraCore.is_null(request.script_name):
            body['scriptName'] = request.script_name
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSortScript',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_version_id)}/sort-scripts',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSortScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sort_script_with_options_async(
        self,
        app_group_identity: str,
        app_version_id: str,
        request: main_models.CreateSortScriptRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSortScriptResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.scope):
            body['scope'] = request.scope
        if not DaraCore.is_null(request.script_name):
            body['scriptName'] = request.script_name
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSortScript',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_version_id)}/sort-scripts',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSortScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sort_script(
        self,
        app_group_identity: str,
        app_version_id: str,
        request: main_models.CreateSortScriptRequest,
    ) -> main_models.CreateSortScriptResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_sort_script_with_options(app_group_identity, app_version_id, request, headers, runtime)

    async def create_sort_script_async(
        self,
        app_group_identity: str,
        app_version_id: str,
        request: main_models.CreateSortScriptRequest,
    ) -> main_models.CreateSortScriptResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_sort_script_with_options_async(app_group_identity, app_version_id, request, headers, runtime)

    def create_user_analyzer_with_options(
        self,
        request: main_models.CreateUserAnalyzerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserAnalyzerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.business):
            body['business'] = request.business
        if not DaraCore.is_null(request.business_app_group_id):
            body['businessAppGroupId'] = request.business_app_group_id
        if not DaraCore.is_null(request.business_type):
            body['businessType'] = request.business_type
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUserAnalyzer',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/user-analyzers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserAnalyzerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_analyzer_with_options_async(
        self,
        request: main_models.CreateUserAnalyzerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserAnalyzerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.business):
            body['business'] = request.business
        if not DaraCore.is_null(request.business_app_group_id):
            body['businessAppGroupId'] = request.business_app_group_id
        if not DaraCore.is_null(request.business_type):
            body['businessType'] = request.business_type
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUserAnalyzer',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/user-analyzers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserAnalyzerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_analyzer(
        self,
        request: main_models.CreateUserAnalyzerRequest,
    ) -> main_models.CreateUserAnalyzerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_user_analyzer_with_options(request, headers, runtime)

    async def create_user_analyzer_async(
        self,
        request: main_models.CreateUserAnalyzerRequest,
    ) -> main_models.CreateUserAnalyzerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_user_analyzer_with_options_async(request, headers, runtime)

    def delete_abtest_experiment_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteABTestExperimentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteABTestExperiment',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}/groups/{DaraURL.percent_encode(group_id)}/experiments/{DaraURL.percent_encode(experiment_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteABTestExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_abtest_experiment_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteABTestExperimentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteABTestExperiment',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}/groups/{DaraURL.percent_encode(group_id)}/experiments/{DaraURL.percent_encode(experiment_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteABTestExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_abtest_experiment(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
    ) -> main_models.DeleteABTestExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_abtest_experiment_with_options(app_group_identity, scene_id, group_id, experiment_id, headers, runtime)

    async def delete_abtest_experiment_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
    ) -> main_models.DeleteABTestExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_abtest_experiment_with_options_async(app_group_identity, scene_id, group_id, experiment_id, headers, runtime)

    def delete_abtest_group_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteABTestGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteABTestGroup',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}/groups/{DaraURL.percent_encode(group_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteABTestGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_abtest_group_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteABTestGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteABTestGroup',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}/groups/{DaraURL.percent_encode(group_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteABTestGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_abtest_group(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
    ) -> main_models.DeleteABTestGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_abtest_group_with_options(app_group_identity, scene_id, group_id, headers, runtime)

    async def delete_abtest_group_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
    ) -> main_models.DeleteABTestGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_abtest_group_with_options_async(app_group_identity, scene_id, group_id, headers, runtime)

    def delete_abtest_scene_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteABTestSceneResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteABTestScene',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteABTestSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_abtest_scene_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteABTestSceneResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteABTestScene',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteABTestSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_abtest_scene(
        self,
        app_group_identity: str,
        scene_id: str,
    ) -> main_models.DeleteABTestSceneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_abtest_scene_with_options(app_group_identity, scene_id, headers, runtime)

    async def delete_abtest_scene_async(
        self,
        app_group_identity: str,
        scene_id: str,
    ) -> main_models.DeleteABTestSceneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_abtest_scene_with_options_async(app_group_identity, scene_id, headers, runtime)

    def delete_function_instance_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFunctionInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteFunctionInstance',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/instances/{DaraURL.percent_encode(instance_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFunctionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_function_instance_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFunctionInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteFunctionInstance',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/instances/{DaraURL.percent_encode(instance_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFunctionInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_function_instance(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
    ) -> main_models.DeleteFunctionInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_function_instance_with_options(app_group_identity, function_name, instance_name, headers, runtime)

    async def delete_function_instance_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
    ) -> main_models.DeleteFunctionInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_function_instance_with_options_async(app_group_identity, function_name, instance_name, headers, runtime)

    def delete_function_resource_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        resource_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFunctionResourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteFunctionResource',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/resources/{DaraURL.percent_encode(resource_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFunctionResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_function_resource_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        resource_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFunctionResourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteFunctionResource',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/resources/{DaraURL.percent_encode(resource_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFunctionResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_function_resource(
        self,
        app_group_identity: str,
        function_name: str,
        resource_name: str,
    ) -> main_models.DeleteFunctionResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_function_resource_with_options(app_group_identity, function_name, resource_name, headers, runtime)

    async def delete_function_resource_async(
        self,
        app_group_identity: str,
        function_name: str,
        resource_name: str,
    ) -> main_models.DeleteFunctionResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_function_resource_with_options_async(app_group_identity, function_name, resource_name, headers, runtime)

    def delete_function_task_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        generation: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFunctionTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteFunctionTask',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/instances/{DaraURL.percent_encode(instance_name)}/tasks/{DaraURL.percent_encode(generation)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFunctionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_function_task_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        generation: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFunctionTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteFunctionTask',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/instances/{DaraURL.percent_encode(instance_name)}/tasks/{DaraURL.percent_encode(generation)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFunctionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_function_task(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        generation: str,
    ) -> main_models.DeleteFunctionTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_function_task_with_options(app_group_identity, function_name, instance_name, generation, headers, runtime)

    async def delete_function_task_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        generation: str,
    ) -> main_models.DeleteFunctionTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_function_task_with_options_async(app_group_identity, function_name, instance_name, generation, headers, runtime)

    def delete_sort_script_with_options(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSortScriptResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteSortScript',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_version_id)}/sort-scripts/{DaraURL.percent_encode(script_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSortScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sort_script_with_options_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSortScriptResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteSortScript',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_version_id)}/sort-scripts/{DaraURL.percent_encode(script_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSortScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sort_script(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
    ) -> main_models.DeleteSortScriptResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_sort_script_with_options(app_group_identity, script_name, app_version_id, headers, runtime)

    async def delete_sort_script_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
    ) -> main_models.DeleteSortScriptResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_sort_script_with_options_async(app_group_identity, script_name, app_version_id, headers, runtime)

    def delete_sort_script_file_with_options(
        self,
        app_group_identity: str,
        app_version_id: str,
        script_name: str,
        file_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSortScriptFileResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteSortScriptFile',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_version_id)}/sort-scripts/{DaraURL.percent_encode(script_name)}/files/src/{DaraURL.percent_encode(file_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSortScriptFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sort_script_file_with_options_async(
        self,
        app_group_identity: str,
        app_version_id: str,
        script_name: str,
        file_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSortScriptFileResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteSortScriptFile',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_version_id)}/sort-scripts/{DaraURL.percent_encode(script_name)}/files/src/{DaraURL.percent_encode(file_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSortScriptFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sort_script_file(
        self,
        app_group_identity: str,
        app_version_id: str,
        script_name: str,
        file_name: str,
    ) -> main_models.DeleteSortScriptFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_sort_script_file_with_options(app_group_identity, app_version_id, script_name, file_name, headers, runtime)

    async def delete_sort_script_file_async(
        self,
        app_group_identity: str,
        app_version_id: str,
        script_name: str,
        file_name: str,
    ) -> main_models.DeleteSortScriptFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_sort_script_file_with_options_async(app_group_identity, app_version_id, script_name, file_name, headers, runtime)

    def describe_abtest_experiment_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeABTestExperimentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeABTestExperiment',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}/groups/{DaraURL.percent_encode(group_id)}/experiments/{DaraURL.percent_encode(experiment_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeABTestExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_abtest_experiment_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeABTestExperimentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeABTestExperiment',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}/groups/{DaraURL.percent_encode(group_id)}/experiments/{DaraURL.percent_encode(experiment_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeABTestExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_abtest_experiment(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
    ) -> main_models.DescribeABTestExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_abtest_experiment_with_options(app_group_identity, scene_id, group_id, experiment_id, headers, runtime)

    async def describe_abtest_experiment_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
    ) -> main_models.DescribeABTestExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_abtest_experiment_with_options_async(app_group_identity, scene_id, group_id, experiment_id, headers, runtime)

    def describe_abtest_group_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeABTestGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeABTestGroup',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}/groups/{DaraURL.percent_encode(group_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeABTestGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_abtest_group_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeABTestGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeABTestGroup',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}/groups/{DaraURL.percent_encode(group_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeABTestGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_abtest_group(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
    ) -> main_models.DescribeABTestGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_abtest_group_with_options(app_group_identity, scene_id, group_id, headers, runtime)

    async def describe_abtest_group_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
    ) -> main_models.DescribeABTestGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_abtest_group_with_options_async(app_group_identity, scene_id, group_id, headers, runtime)

    def describe_abtest_scene_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeABTestSceneResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeABTestScene',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeABTestSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_abtest_scene_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeABTestSceneResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeABTestScene',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeABTestSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_abtest_scene(
        self,
        app_group_identity: str,
        scene_id: str,
    ) -> main_models.DescribeABTestSceneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_abtest_scene_with_options(app_group_identity, scene_id, headers, runtime)

    async def describe_abtest_scene_async(
        self,
        app_group_identity: str,
        scene_id: str,
    ) -> main_models.DescribeABTestSceneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_abtest_scene_with_options_async(app_group_identity, scene_id, headers, runtime)

    def describe_app_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeApp',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeApp',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> main_models.DescribeAppResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_app_with_options(app_group_identity, app_id, headers, runtime)

    async def describe_app_async(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> main_models.DescribeAppResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_app_with_options_async(app_group_identity, app_id, headers, runtime)

    def describe_app_group_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppGroup',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_group_with_options_async(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppGroup',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_group(
        self,
        app_group_identity: str,
    ) -> main_models.DescribeAppGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_app_group_with_options(app_group_identity, headers, runtime)

    async def describe_app_group_async(
        self,
        app_group_identity: str,
    ) -> main_models.DescribeAppGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_app_group_with_options_async(app_group_identity, headers, runtime)

    def describe_app_statistics_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppStatisticsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppStatistics',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/statistics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_statistics_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppStatisticsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppStatistics',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/statistics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_statistics(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> main_models.DescribeAppStatisticsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_app_statistics_with_options(app_group_identity, app_id, headers, runtime)

    async def describe_app_statistics_async(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> main_models.DescribeAppStatisticsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_app_statistics_with_options_async(app_group_identity, app_id, headers, runtime)

    def describe_apps_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeApps',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apps_with_options_async(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeApps',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apps(
        self,
        app_group_identity: str,
    ) -> main_models.DescribeAppsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_apps_with_options(app_group_identity, headers, runtime)

    async def describe_apps_async(
        self,
        app_group_identity: str,
    ) -> main_models.DescribeAppsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_apps_with_options_async(app_group_identity, headers, runtime)

    def describe_data_collction_with_options(
        self,
        app_group_identity: str,
        data_collection_identity: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataCollctionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataCollction',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/data-collections/{DaraURL.percent_encode(data_collection_identity)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataCollctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_collction_with_options_async(
        self,
        app_group_identity: str,
        data_collection_identity: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataCollctionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataCollction',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/data-collections/{DaraURL.percent_encode(data_collection_identity)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataCollctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_collction(
        self,
        app_group_identity: str,
        data_collection_identity: str,
    ) -> main_models.DescribeDataCollctionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_data_collction_with_options(app_group_identity, data_collection_identity, headers, runtime)

    async def describe_data_collction_async(
        self,
        app_group_identity: str,
        data_collection_identity: str,
    ) -> main_models.DescribeDataCollctionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_data_collction_with_options_async(app_group_identity, data_collection_identity, headers, runtime)

    def describe_first_rank_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFirstRankResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeFirstRank',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/first-ranks/{DaraURL.percent_encode(name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFirstRankResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_first_rank_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFirstRankResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeFirstRank',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/first-ranks/{DaraURL.percent_encode(name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFirstRankResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_first_rank(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> main_models.DescribeFirstRankResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_first_rank_with_options(app_group_identity, app_id, name, headers, runtime)

    async def describe_first_rank_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> main_models.DescribeFirstRankResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_first_rank_with_options_async(app_group_identity, app_id, name, headers, runtime)

    def describe_intervention_dictionary_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInterventionDictionaryResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeInterventionDictionary',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/intervention-dictionaries/{DaraURL.percent_encode(name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInterventionDictionaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_intervention_dictionary_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInterventionDictionaryResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeInterventionDictionary',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/intervention-dictionaries/{DaraURL.percent_encode(name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInterventionDictionaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_intervention_dictionary(
        self,
        name: str,
    ) -> main_models.DescribeInterventionDictionaryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_intervention_dictionary_with_options(name, headers, runtime)

    async def describe_intervention_dictionary_async(
        self,
        name: str,
    ) -> main_models.DescribeInterventionDictionaryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_intervention_dictionary_with_options_async(name, headers, runtime)

    def describe_query_processor_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeQueryProcessorResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeQueryProcessor',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/query-processors/{DaraURL.percent_encode(name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeQueryProcessorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_query_processor_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeQueryProcessorResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeQueryProcessor',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/query-processors/{DaraURL.percent_encode(name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeQueryProcessorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_query_processor(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> main_models.DescribeQueryProcessorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_query_processor_with_options(app_group_identity, app_id, name, headers, runtime)

    async def describe_query_processor_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> main_models.DescribeQueryProcessorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_query_processor_with_options_async(app_group_identity, app_id, name, headers, runtime)

    def describe_regions_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/regions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/regions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(self) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(headers, runtime)

    async def describe_regions_async(self) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_regions_with_options_async(headers, runtime)

    def describe_scheduled_task_with_options(
        self,
        app_group_identity: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScheduledTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeScheduledTask',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scheduled-tasks/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scheduled_task_with_options_async(
        self,
        app_group_identity: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScheduledTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeScheduledTask',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scheduled-tasks/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScheduledTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scheduled_task(
        self,
        app_group_identity: str,
        task_id: str,
    ) -> main_models.DescribeScheduledTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_scheduled_task_with_options(app_group_identity, task_id, headers, runtime)

    async def describe_scheduled_task_async(
        self,
        app_group_identity: str,
        task_id: str,
    ) -> main_models.DescribeScheduledTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_scheduled_task_with_options_async(app_group_identity, task_id, headers, runtime)

    def describe_second_rank_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecondRankResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecondRank',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/second-ranks/{DaraURL.percent_encode(name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecondRankResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_second_rank_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecondRankResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecondRank',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/second-ranks/{DaraURL.percent_encode(name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecondRankResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_second_rank(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> main_models.DescribeSecondRankResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_second_rank_with_options(app_group_identity, app_id, name, headers, runtime)

    async def describe_second_rank_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> main_models.DescribeSecondRankResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_second_rank_with_options_async(app_group_identity, app_id, name, headers, runtime)

    def describe_slow_query_status_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlowQueryStatusResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlowQueryStatus',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/optimizers/slow-query',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlowQueryStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_query_status_with_options_async(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlowQueryStatusResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlowQueryStatus',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/optimizers/slow-query',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlowQueryStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slow_query_status(
        self,
        app_group_identity: str,
    ) -> main_models.DescribeSlowQueryStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_slow_query_status_with_options(app_group_identity, headers, runtime)

    async def describe_slow_query_status_async(
        self,
        app_group_identity: str,
    ) -> main_models.DescribeSlowQueryStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_slow_query_status_with_options_async(app_group_identity, headers, runtime)

    def describe_user_analyzer_with_options(
        self,
        name: str,
        request: main_models.DescribeUserAnalyzerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserAnalyzerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.with_):
            query['with'] = request.with_
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserAnalyzer',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/user-analyzers/{DaraURL.percent_encode(name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserAnalyzerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_analyzer_with_options_async(
        self,
        name: str,
        request: main_models.DescribeUserAnalyzerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserAnalyzerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.with_):
            query['with'] = request.with_
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserAnalyzer',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/user-analyzers/{DaraURL.percent_encode(name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserAnalyzerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_analyzer(
        self,
        name: str,
        request: main_models.DescribeUserAnalyzerRequest,
    ) -> main_models.DescribeUserAnalyzerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_user_analyzer_with_options(name, request, headers, runtime)

    async def describe_user_analyzer_async(
        self,
        name: str,
        request: main_models.DescribeUserAnalyzerRequest,
    ) -> main_models.DescribeUserAnalyzerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_user_analyzer_with_options_async(name, request, headers, runtime)

    def disable_slow_query_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableSlowQueryResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DisableSlowQuery',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/optimizers/slow-query/actions/disable',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableSlowQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_slow_query_with_options_async(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableSlowQueryResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DisableSlowQuery',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/optimizers/slow-query/actions/disable',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableSlowQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_slow_query(
        self,
        app_group_identity: str,
    ) -> main_models.DisableSlowQueryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.disable_slow_query_with_options(app_group_identity, headers, runtime)

    async def disable_slow_query_async(
        self,
        app_group_identity: str,
    ) -> main_models.DisableSlowQueryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.disable_slow_query_with_options_async(app_group_identity, headers, runtime)

    def enable_slow_query_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableSlowQueryResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'EnableSlowQuery',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/optimizers/slow-query/actions/enable',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableSlowQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_slow_query_with_options_async(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableSlowQueryResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'EnableSlowQuery',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/optimizers/slow-query/actions/enable',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableSlowQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_slow_query(
        self,
        app_group_identity: str,
    ) -> main_models.EnableSlowQueryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.enable_slow_query_with_options(app_group_identity, headers, runtime)

    async def enable_slow_query_async(
        self,
        app_group_identity: str,
    ) -> main_models.EnableSlowQueryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.enable_slow_query_with_options_async(app_group_identity, headers, runtime)

    def generate_merged_table_with_options(
        self,
        request: main_models.GenerateMergedTableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateMergedTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.spec):
            query['spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateMergedTable',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/assist/schema/actions/merge',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateMergedTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_merged_table_with_options_async(
        self,
        request: main_models.GenerateMergedTableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateMergedTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.spec):
            query['spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateMergedTable',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/assist/schema/actions/merge',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateMergedTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_merged_table(
        self,
        request: main_models.GenerateMergedTableRequest,
    ) -> main_models.GenerateMergedTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.generate_merged_table_with_options(request, headers, runtime)

    async def generate_merged_table_async(
        self,
        request: main_models.GenerateMergedTableRequest,
    ) -> main_models.GenerateMergedTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.generate_merged_table_with_options_async(request, headers, runtime)

    def get_domain_with_options(
        self,
        domain_name: str,
        request: main_models.GetDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_group_identity):
            query['appGroupIdentity'] = request.app_group_identity
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDomain',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/domains/{DaraURL.percent_encode(domain_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_domain_with_options_async(
        self,
        domain_name: str,
        request: main_models.GetDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_group_identity):
            query['appGroupIdentity'] = request.app_group_identity
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDomain',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/domains/{DaraURL.percent_encode(domain_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_domain(
        self,
        domain_name: str,
        request: main_models.GetDomainRequest,
    ) -> main_models.GetDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_domain_with_options(domain_name, request, headers, runtime)

    async def get_domain_async(
        self,
        domain_name: str,
        request: main_models.GetDomainRequest,
    ) -> main_models.GetDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_domain_with_options_async(domain_name, request, headers, runtime)

    def get_function_current_version_with_options(
        self,
        function_name: str,
        request: main_models.GetFunctionCurrentVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFunctionCurrentVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['category'] = request.category
        if not DaraCore.is_null(request.domain):
            query['domain'] = request.domain
        if not DaraCore.is_null(request.function_type):
            query['functionType'] = request.function_type
        if not DaraCore.is_null(request.model_type):
            query['modelType'] = request.model_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFunctionCurrentVersion',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/functions/{DaraURL.percent_encode(function_name)}/current-version',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFunctionCurrentVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_function_current_version_with_options_async(
        self,
        function_name: str,
        request: main_models.GetFunctionCurrentVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFunctionCurrentVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['category'] = request.category
        if not DaraCore.is_null(request.domain):
            query['domain'] = request.domain
        if not DaraCore.is_null(request.function_type):
            query['functionType'] = request.function_type
        if not DaraCore.is_null(request.model_type):
            query['modelType'] = request.model_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFunctionCurrentVersion',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/functions/{DaraURL.percent_encode(function_name)}/current-version',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFunctionCurrentVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_function_current_version(
        self,
        function_name: str,
        request: main_models.GetFunctionCurrentVersionRequest,
    ) -> main_models.GetFunctionCurrentVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_function_current_version_with_options(function_name, request, headers, runtime)

    async def get_function_current_version_async(
        self,
        function_name: str,
        request: main_models.GetFunctionCurrentVersionRequest,
    ) -> main_models.GetFunctionCurrentVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_function_current_version_with_options_async(function_name, request, headers, runtime)

    def get_function_default_instance_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFunctionDefaultInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetFunctionDefaultInstance',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/default-instance',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFunctionDefaultInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_function_default_instance_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFunctionDefaultInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetFunctionDefaultInstance',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/default-instance',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFunctionDefaultInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_function_default_instance(
        self,
        app_group_identity: str,
        function_name: str,
    ) -> main_models.GetFunctionDefaultInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_function_default_instance_with_options(app_group_identity, function_name, headers, runtime)

    async def get_function_default_instance_async(
        self,
        app_group_identity: str,
        function_name: str,
    ) -> main_models.GetFunctionDefaultInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_function_default_instance_with_options_async(app_group_identity, function_name, headers, runtime)

    def get_function_instance_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        request: main_models.GetFunctionInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFunctionInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.output):
            query['output'] = request.output
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFunctionInstance',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/instances/{DaraURL.percent_encode(instance_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFunctionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_function_instance_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        request: main_models.GetFunctionInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFunctionInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.output):
            query['output'] = request.output
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFunctionInstance',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/instances/{DaraURL.percent_encode(instance_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFunctionInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_function_instance(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        request: main_models.GetFunctionInstanceRequest,
    ) -> main_models.GetFunctionInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_function_instance_with_options(app_group_identity, function_name, instance_name, request, headers, runtime)

    async def get_function_instance_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        request: main_models.GetFunctionInstanceRequest,
    ) -> main_models.GetFunctionInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_function_instance_with_options_async(app_group_identity, function_name, instance_name, request, headers, runtime)

    def get_function_resource_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        resource_name: str,
        request: main_models.GetFunctionResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFunctionResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.output):
            query['output'] = request.output
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFunctionResource',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/resources/{DaraURL.percent_encode(resource_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFunctionResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_function_resource_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        resource_name: str,
        request: main_models.GetFunctionResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFunctionResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.output):
            query['output'] = request.output
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFunctionResource',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/resources/{DaraURL.percent_encode(resource_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFunctionResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_function_resource(
        self,
        app_group_identity: str,
        function_name: str,
        resource_name: str,
        request: main_models.GetFunctionResourceRequest,
    ) -> main_models.GetFunctionResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_function_resource_with_options(app_group_identity, function_name, resource_name, request, headers, runtime)

    async def get_function_resource_async(
        self,
        app_group_identity: str,
        function_name: str,
        resource_name: str,
        request: main_models.GetFunctionResourceRequest,
    ) -> main_models.GetFunctionResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_function_resource_with_options_async(app_group_identity, function_name, resource_name, request, headers, runtime)

    def get_function_task_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        generation: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFunctionTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetFunctionTask',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/instances/{DaraURL.percent_encode(instance_name)}/tasks/{DaraURL.percent_encode(generation)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFunctionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_function_task_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        generation: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFunctionTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetFunctionTask',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/instances/{DaraURL.percent_encode(instance_name)}/tasks/{DaraURL.percent_encode(generation)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFunctionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_function_task(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        generation: str,
    ) -> main_models.GetFunctionTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_function_task_with_options(app_group_identity, function_name, instance_name, generation, headers, runtime)

    async def get_function_task_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        generation: str,
    ) -> main_models.GetFunctionTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_function_task_with_options_async(app_group_identity, function_name, instance_name, generation, headers, runtime)

    def get_function_version_with_options(
        self,
        function_name: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFunctionVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetFunctionVersion',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/functions/{DaraURL.percent_encode(function_name)}/versions/{DaraURL.percent_encode(version_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFunctionVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_function_version_with_options_async(
        self,
        function_name: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFunctionVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetFunctionVersion',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/functions/{DaraURL.percent_encode(function_name)}/versions/{DaraURL.percent_encode(version_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFunctionVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_function_version(
        self,
        function_name: str,
        version_id: str,
    ) -> main_models.GetFunctionVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_function_version_with_options(function_name, version_id, headers, runtime)

    async def get_function_version_async(
        self,
        function_name: str,
        version_id: str,
    ) -> main_models.GetFunctionVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_function_version_with_options_async(function_name, version_id, headers, runtime)

    def get_script_file_names_with_options(
        self,
        app_group_identity: str,
        app_version_id: str,
        script_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetScriptFileNamesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetScriptFileNames',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_version_id)}/sort-scripts/{DaraURL.percent_encode(script_name)}/file-names',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScriptFileNamesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_script_file_names_with_options_async(
        self,
        app_group_identity: str,
        app_version_id: str,
        script_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetScriptFileNamesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetScriptFileNames',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_version_id)}/sort-scripts/{DaraURL.percent_encode(script_name)}/file-names',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScriptFileNamesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_script_file_names(
        self,
        app_group_identity: str,
        app_version_id: str,
        script_name: str,
    ) -> main_models.GetScriptFileNamesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_script_file_names_with_options(app_group_identity, app_version_id, script_name, headers, runtime)

    async def get_script_file_names_async(
        self,
        app_group_identity: str,
        app_version_id: str,
        script_name: str,
    ) -> main_models.GetScriptFileNamesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_script_file_names_with_options_async(app_group_identity, app_version_id, script_name, headers, runtime)

    def get_search_strategy_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        strategy_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSearchStrategyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSearchStrategy',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/search-strategies/{DaraURL.percent_encode(strategy_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSearchStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_search_strategy_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        strategy_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSearchStrategyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSearchStrategy',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/search-strategies/{DaraURL.percent_encode(strategy_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSearchStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_search_strategy(
        self,
        app_group_identity: str,
        app_id: str,
        strategy_name: str,
    ) -> main_models.GetSearchStrategyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_search_strategy_with_options(app_group_identity, app_id, strategy_name, headers, runtime)

    async def get_search_strategy_async(
        self,
        app_group_identity: str,
        app_id: str,
        strategy_name: str,
    ) -> main_models.GetSearchStrategyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_search_strategy_with_options_async(app_group_identity, app_id, strategy_name, headers, runtime)

    def get_sort_script_with_options(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSortScriptResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSortScript',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_version_id)}/sort-scripts/{DaraURL.percent_encode(script_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSortScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sort_script_with_options_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSortScriptResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSortScript',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_version_id)}/sort-scripts/{DaraURL.percent_encode(script_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSortScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sort_script(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
    ) -> main_models.GetSortScriptResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_sort_script_with_options(app_group_identity, script_name, app_version_id, headers, runtime)

    async def get_sort_script_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
    ) -> main_models.GetSortScriptResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_sort_script_with_options_async(app_group_identity, script_name, app_version_id, headers, runtime)

    def get_sort_script_file_with_options(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        file_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSortScriptFileResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSortScriptFile',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_version_id)}/sort-scripts/{DaraURL.percent_encode(script_name)}/files/src/{DaraURL.percent_encode(file_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSortScriptFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sort_script_file_with_options_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        file_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSortScriptFileResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSortScriptFile',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_version_id)}/sort-scripts/{DaraURL.percent_encode(script_name)}/files/src/{DaraURL.percent_encode(file_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSortScriptFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sort_script_file(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        file_name: str,
    ) -> main_models.GetSortScriptFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_sort_script_file_with_options(app_group_identity, script_name, app_version_id, file_name, headers, runtime)

    async def get_sort_script_file_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        file_name: str,
    ) -> main_models.GetSortScriptFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_sort_script_file_with_options_async(app_group_identity, script_name, app_version_id, file_name, headers, runtime)

    def list_abtest_experiments_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListABTestExperimentsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListABTestExperiments',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}/groups/{DaraURL.percent_encode(group_id)}/experiments',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListABTestExperimentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_abtest_experiments_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListABTestExperimentsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListABTestExperiments',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}/groups/{DaraURL.percent_encode(group_id)}/experiments',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListABTestExperimentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_abtest_experiments(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
    ) -> main_models.ListABTestExperimentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_abtest_experiments_with_options(app_group_identity, scene_id, group_id, headers, runtime)

    async def list_abtest_experiments_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
    ) -> main_models.ListABTestExperimentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_abtest_experiments_with_options_async(app_group_identity, scene_id, group_id, headers, runtime)

    def list_abtest_fixed_flow_dividers_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListABTestFixedFlowDividersResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListABTestFixedFlowDividers',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}/groups/{DaraURL.percent_encode(group_id)}/experiments/{DaraURL.percent_encode(experiment_id)}/fixed-flow-dividers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListABTestFixedFlowDividersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_abtest_fixed_flow_dividers_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListABTestFixedFlowDividersResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListABTestFixedFlowDividers',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}/groups/{DaraURL.percent_encode(group_id)}/experiments/{DaraURL.percent_encode(experiment_id)}/fixed-flow-dividers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListABTestFixedFlowDividersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_abtest_fixed_flow_dividers(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
    ) -> main_models.ListABTestFixedFlowDividersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_abtest_fixed_flow_dividers_with_options(app_group_identity, scene_id, group_id, experiment_id, headers, runtime)

    async def list_abtest_fixed_flow_dividers_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
    ) -> main_models.ListABTestFixedFlowDividersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_abtest_fixed_flow_dividers_with_options_async(app_group_identity, scene_id, group_id, experiment_id, headers, runtime)

    def list_abtest_groups_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListABTestGroupsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListABTestGroups',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}/groups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListABTestGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_abtest_groups_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListABTestGroupsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListABTestGroups',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}/groups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListABTestGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_abtest_groups(
        self,
        app_group_identity: str,
        scene_id: str,
    ) -> main_models.ListABTestGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_abtest_groups_with_options(app_group_identity, scene_id, headers, runtime)

    async def list_abtest_groups_async(
        self,
        app_group_identity: str,
        scene_id: str,
    ) -> main_models.ListABTestGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_abtest_groups_with_options_async(app_group_identity, scene_id, headers, runtime)

    def list_abtest_scenes_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListABTestScenesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListABTestScenes',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListABTestScenesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_abtest_scenes_with_options_async(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListABTestScenesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListABTestScenes',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListABTestScenesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_abtest_scenes(
        self,
        app_group_identity: str,
    ) -> main_models.ListABTestScenesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_abtest_scenes_with_options(app_group_identity, headers, runtime)

    async def list_abtest_scenes_async(
        self,
        app_group_identity: str,
    ) -> main_models.ListABTestScenesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_abtest_scenes_with_options_async(app_group_identity, headers, runtime)

    def list_app_groups_with_options(
        self,
        tmp_req: main_models.ListAppGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAppGroupsResponse:
        tmp_req.validate()
        request = main_models.ListAppGroupsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.sort_by):
            query['sortBy'] = request.sort_by
        if not DaraCore.is_null(request.tags_shrink):
            query['tags'] = request.tags_shrink
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppGroups',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_groups_with_options_async(
        self,
        tmp_req: main_models.ListAppGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAppGroupsResponse:
        tmp_req.validate()
        request = main_models.ListAppGroupsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.sort_by):
            query['sortBy'] = request.sort_by
        if not DaraCore.is_null(request.tags_shrink):
            query['tags'] = request.tags_shrink
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppGroups',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_groups(
        self,
        request: main_models.ListAppGroupsRequest,
    ) -> main_models.ListAppGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_app_groups_with_options(request, headers, runtime)

    async def list_app_groups_async(
        self,
        request: main_models.ListAppGroupsRequest,
    ) -> main_models.ListAppGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_app_groups_with_options_async(request, headers, runtime)

    def list_data_collections_with_options(
        self,
        app_group_identity: str,
        request: main_models.ListDataCollectionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataCollectionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataCollections',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/data-collections',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataCollectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_collections_with_options_async(
        self,
        app_group_identity: str,
        request: main_models.ListDataCollectionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataCollectionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataCollections',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/data-collections',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataCollectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_collections(
        self,
        app_group_identity: str,
        request: main_models.ListDataCollectionsRequest,
    ) -> main_models.ListDataCollectionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_data_collections_with_options(app_group_identity, request, headers, runtime)

    async def list_data_collections_async(
        self,
        app_group_identity: str,
        request: main_models.ListDataCollectionsRequest,
    ) -> main_models.ListDataCollectionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_data_collections_with_options_async(app_group_identity, request, headers, runtime)

    def list_data_source_table_fields_with_options(
        self,
        data_source_type: str,
        request: main_models.ListDataSourceTableFieldsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSourceTableFieldsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.params):
            query['params'] = request.params
        if not DaraCore.is_null(request.raw_type):
            query['rawType'] = request.raw_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSourceTableFields',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/assist/data-sources/{DaraURL.percent_encode(data_source_type)}/fields',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSourceTableFieldsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_source_table_fields_with_options_async(
        self,
        data_source_type: str,
        request: main_models.ListDataSourceTableFieldsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSourceTableFieldsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.params):
            query['params'] = request.params
        if not DaraCore.is_null(request.raw_type):
            query['rawType'] = request.raw_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSourceTableFields',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/assist/data-sources/{DaraURL.percent_encode(data_source_type)}/fields',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSourceTableFieldsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_source_table_fields(
        self,
        data_source_type: str,
        request: main_models.ListDataSourceTableFieldsRequest,
    ) -> main_models.ListDataSourceTableFieldsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_data_source_table_fields_with_options(data_source_type, request, headers, runtime)

    async def list_data_source_table_fields_async(
        self,
        data_source_type: str,
        request: main_models.ListDataSourceTableFieldsRequest,
    ) -> main_models.ListDataSourceTableFieldsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_data_source_table_fields_with_options_async(data_source_type, request, headers, runtime)

    def list_data_source_tables_with_options(
        self,
        data_source_type: str,
        request: main_models.ListDataSourceTablesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSourceTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.params):
            query['params'] = request.params
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSourceTables',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/assist/data-sources/{DaraURL.percent_encode(data_source_type)}/tables',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSourceTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_source_tables_with_options_async(
        self,
        data_source_type: str,
        request: main_models.ListDataSourceTablesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSourceTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.params):
            query['params'] = request.params
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSourceTables',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/assist/data-sources/{DaraURL.percent_encode(data_source_type)}/tables',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSourceTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_source_tables(
        self,
        data_source_type: str,
        request: main_models.ListDataSourceTablesRequest,
    ) -> main_models.ListDataSourceTablesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_data_source_tables_with_options(data_source_type, request, headers, runtime)

    async def list_data_source_tables_async(
        self,
        data_source_type: str,
        request: main_models.ListDataSourceTablesRequest,
    ) -> main_models.ListDataSourceTablesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_data_source_tables_with_options_async(data_source_type, request, headers, runtime)

    def list_first_ranks_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFirstRanksResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListFirstRanks',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/first-ranks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFirstRanksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_first_ranks_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFirstRanksResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListFirstRanks',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/first-ranks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFirstRanksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_first_ranks(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> main_models.ListFirstRanksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_first_ranks_with_options(app_group_identity, app_id, headers, runtime)

    async def list_first_ranks_async(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> main_models.ListFirstRanksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_first_ranks_with_options_async(app_group_identity, app_id, headers, runtime)

    def list_function_instances_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        request: main_models.ListFunctionInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFunctionInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.function_type):
            query['functionType'] = request.function_type
        if not DaraCore.is_null(request.model_type):
            query['modelType'] = request.model_type
        if not DaraCore.is_null(request.output):
            query['output'] = request.output
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFunctionInstances',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFunctionInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_function_instances_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        request: main_models.ListFunctionInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFunctionInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.function_type):
            query['functionType'] = request.function_type
        if not DaraCore.is_null(request.model_type):
            query['modelType'] = request.model_type
        if not DaraCore.is_null(request.output):
            query['output'] = request.output
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFunctionInstances',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFunctionInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_function_instances(
        self,
        app_group_identity: str,
        function_name: str,
        request: main_models.ListFunctionInstancesRequest,
    ) -> main_models.ListFunctionInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_function_instances_with_options(app_group_identity, function_name, request, headers, runtime)

    async def list_function_instances_async(
        self,
        app_group_identity: str,
        function_name: str,
        request: main_models.ListFunctionInstancesRequest,
    ) -> main_models.ListFunctionInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_function_instances_with_options_async(app_group_identity, function_name, request, headers, runtime)

    def list_function_resources_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        request: main_models.ListFunctionResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFunctionResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.output):
            query['output'] = request.output
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFunctionResources',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/resources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFunctionResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_function_resources_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        request: main_models.ListFunctionResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFunctionResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.output):
            query['output'] = request.output
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFunctionResources',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/resources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFunctionResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_function_resources(
        self,
        app_group_identity: str,
        function_name: str,
        request: main_models.ListFunctionResourcesRequest,
    ) -> main_models.ListFunctionResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_function_resources_with_options(app_group_identity, function_name, request, headers, runtime)

    async def list_function_resources_async(
        self,
        app_group_identity: str,
        function_name: str,
        request: main_models.ListFunctionResourcesRequest,
    ) -> main_models.ListFunctionResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_function_resources_with_options_async(app_group_identity, function_name, request, headers, runtime)

    def list_function_tasks_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        request: main_models.ListFunctionTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFunctionTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFunctionTasks',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/instances/{DaraURL.percent_encode(instance_name)}/tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFunctionTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_function_tasks_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        request: main_models.ListFunctionTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFunctionTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFunctionTasks',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/instances/{DaraURL.percent_encode(instance_name)}/tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFunctionTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_function_tasks(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        request: main_models.ListFunctionTasksRequest,
    ) -> main_models.ListFunctionTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_function_tasks_with_options(app_group_identity, function_name, instance_name, request, headers, runtime)

    async def list_function_tasks_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        request: main_models.ListFunctionTasksRequest,
    ) -> main_models.ListFunctionTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_function_tasks_with_options_async(app_group_identity, function_name, instance_name, request, headers, runtime)

    def list_intervention_dictionaries_with_options(
        self,
        request: main_models.ListInterventionDictionariesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInterventionDictionariesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.types):
            query['types'] = request.types
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInterventionDictionaries',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/intervention-dictionaries',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInterventionDictionariesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_intervention_dictionaries_with_options_async(
        self,
        request: main_models.ListInterventionDictionariesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInterventionDictionariesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.types):
            query['types'] = request.types
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInterventionDictionaries',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/intervention-dictionaries',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInterventionDictionariesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_intervention_dictionaries(
        self,
        request: main_models.ListInterventionDictionariesRequest,
    ) -> main_models.ListInterventionDictionariesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_intervention_dictionaries_with_options(request, headers, runtime)

    async def list_intervention_dictionaries_async(
        self,
        request: main_models.ListInterventionDictionariesRequest,
    ) -> main_models.ListInterventionDictionariesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_intervention_dictionaries_with_options_async(request, headers, runtime)

    def list_intervention_dictionary_entries_with_options(
        self,
        name: str,
        request: main_models.ListInterventionDictionaryEntriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInterventionDictionaryEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.word):
            query['word'] = request.word
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInterventionDictionaryEntries',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/intervention-dictionaries/{DaraURL.percent_encode(name)}/entries',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInterventionDictionaryEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_intervention_dictionary_entries_with_options_async(
        self,
        name: str,
        request: main_models.ListInterventionDictionaryEntriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInterventionDictionaryEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.word):
            query['word'] = request.word
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInterventionDictionaryEntries',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/intervention-dictionaries/{DaraURL.percent_encode(name)}/entries',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInterventionDictionaryEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_intervention_dictionary_entries(
        self,
        name: str,
        request: main_models.ListInterventionDictionaryEntriesRequest,
    ) -> main_models.ListInterventionDictionaryEntriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_intervention_dictionary_entries_with_options(name, request, headers, runtime)

    async def list_intervention_dictionary_entries_async(
        self,
        name: str,
        request: main_models.ListInterventionDictionaryEntriesRequest,
    ) -> main_models.ListInterventionDictionaryEntriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_intervention_dictionary_entries_with_options_async(name, request, headers, runtime)

    def list_intervention_dictionary_ner_results_with_options(
        self,
        name: str,
        request: main_models.ListInterventionDictionaryNerResultsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInterventionDictionaryNerResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInterventionDictionaryNerResults',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/intervention-dictionaries/{DaraURL.percent_encode(name)}/ner-results',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInterventionDictionaryNerResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_intervention_dictionary_ner_results_with_options_async(
        self,
        name: str,
        request: main_models.ListInterventionDictionaryNerResultsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInterventionDictionaryNerResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInterventionDictionaryNerResults',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/intervention-dictionaries/{DaraURL.percent_encode(name)}/ner-results',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInterventionDictionaryNerResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_intervention_dictionary_ner_results(
        self,
        name: str,
        request: main_models.ListInterventionDictionaryNerResultsRequest,
    ) -> main_models.ListInterventionDictionaryNerResultsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_intervention_dictionary_ner_results_with_options(name, request, headers, runtime)

    async def list_intervention_dictionary_ner_results_async(
        self,
        name: str,
        request: main_models.ListInterventionDictionaryNerResultsRequest,
    ) -> main_models.ListInterventionDictionaryNerResultsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_intervention_dictionary_ner_results_with_options_async(name, request, headers, runtime)

    def list_intervention_dictionary_related_entities_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInterventionDictionaryRelatedEntitiesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListInterventionDictionaryRelatedEntities',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/intervention-dictionaries/{DaraURL.percent_encode(name)}/related',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInterventionDictionaryRelatedEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_intervention_dictionary_related_entities_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInterventionDictionaryRelatedEntitiesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListInterventionDictionaryRelatedEntities',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/intervention-dictionaries/{DaraURL.percent_encode(name)}/related',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInterventionDictionaryRelatedEntitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_intervention_dictionary_related_entities(
        self,
        name: str,
    ) -> main_models.ListInterventionDictionaryRelatedEntitiesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_intervention_dictionary_related_entities_with_options(name, headers, runtime)

    async def list_intervention_dictionary_related_entities_async(
        self,
        name: str,
    ) -> main_models.ListInterventionDictionaryRelatedEntitiesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_intervention_dictionary_related_entities_with_options_async(name, headers, runtime)

    def list_proceedings_with_options(
        self,
        app_group_identity: str,
        request: main_models.ListProceedingsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProceedingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter_finished):
            query['filterFinished'] = request.filter_finished
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProceedings',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/proceedings',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProceedingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_proceedings_with_options_async(
        self,
        app_group_identity: str,
        request: main_models.ListProceedingsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProceedingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter_finished):
            query['filterFinished'] = request.filter_finished
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProceedings',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/proceedings',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProceedingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_proceedings(
        self,
        app_group_identity: str,
        request: main_models.ListProceedingsRequest,
    ) -> main_models.ListProceedingsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_proceedings_with_options(app_group_identity, request, headers, runtime)

    async def list_proceedings_async(
        self,
        app_group_identity: str,
        request: main_models.ListProceedingsRequest,
    ) -> main_models.ListProceedingsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_proceedings_with_options_async(app_group_identity, request, headers, runtime)

    def list_query_processor_analyzer_results_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: main_models.ListQueryProcessorAnalyzerResultsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListQueryProcessorAnalyzerResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.text):
            query['text'] = request.text
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQueryProcessorAnalyzerResults',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/query-processors/{DaraURL.percent_encode(name)}/analyze',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQueryProcessorAnalyzerResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_query_processor_analyzer_results_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: main_models.ListQueryProcessorAnalyzerResultsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListQueryProcessorAnalyzerResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.text):
            query['text'] = request.text
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQueryProcessorAnalyzerResults',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/query-processors/{DaraURL.percent_encode(name)}/analyze',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQueryProcessorAnalyzerResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_query_processor_analyzer_results(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: main_models.ListQueryProcessorAnalyzerResultsRequest,
    ) -> main_models.ListQueryProcessorAnalyzerResultsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_query_processor_analyzer_results_with_options(app_group_identity, app_id, name, request, headers, runtime)

    async def list_query_processor_analyzer_results_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: main_models.ListQueryProcessorAnalyzerResultsRequest,
    ) -> main_models.ListQueryProcessorAnalyzerResultsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_query_processor_analyzer_results_with_options_async(app_group_identity, app_id, name, request, headers, runtime)

    def list_query_processor_ners_with_options(
        self,
        request: main_models.ListQueryProcessorNersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListQueryProcessorNersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['domain'] = request.domain
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQueryProcessorNers',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/query-processor/ner/default-priorities',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQueryProcessorNersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_query_processor_ners_with_options_async(
        self,
        request: main_models.ListQueryProcessorNersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListQueryProcessorNersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['domain'] = request.domain
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQueryProcessorNers',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/query-processor/ner/default-priorities',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQueryProcessorNersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_query_processor_ners(
        self,
        request: main_models.ListQueryProcessorNersRequest,
    ) -> main_models.ListQueryProcessorNersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_query_processor_ners_with_options(request, headers, runtime)

    async def list_query_processor_ners_async(
        self,
        request: main_models.ListQueryProcessorNersRequest,
    ) -> main_models.ListQueryProcessorNersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_query_processor_ners_with_options_async(request, headers, runtime)

    def list_query_processors_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        request: main_models.ListQueryProcessorsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListQueryProcessorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_active):
            query['isActive'] = request.is_active
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQueryProcessors',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/query-processors',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQueryProcessorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_query_processors_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: main_models.ListQueryProcessorsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListQueryProcessorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_active):
            query['isActive'] = request.is_active
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQueryProcessors',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/query-processors',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQueryProcessorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_query_processors(
        self,
        app_group_identity: str,
        app_id: str,
        request: main_models.ListQueryProcessorsRequest,
    ) -> main_models.ListQueryProcessorsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_query_processors_with_options(app_group_identity, app_id, request, headers, runtime)

    async def list_query_processors_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: main_models.ListQueryProcessorsRequest,
    ) -> main_models.ListQueryProcessorsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_query_processors_with_options_async(app_group_identity, app_id, request, headers, runtime)

    def list_quota_review_tasks_with_options(
        self,
        app_group_identity: str,
        request: main_models.ListQuotaReviewTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListQuotaReviewTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQuotaReviewTasks',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/quota-review-tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQuotaReviewTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quota_review_tasks_with_options_async(
        self,
        app_group_identity: str,
        request: main_models.ListQuotaReviewTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListQuotaReviewTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQuotaReviewTasks',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/quota-review-tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQuotaReviewTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quota_review_tasks(
        self,
        app_group_identity: str,
        request: main_models.ListQuotaReviewTasksRequest,
    ) -> main_models.ListQuotaReviewTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_quota_review_tasks_with_options(app_group_identity, request, headers, runtime)

    async def list_quota_review_tasks_async(
        self,
        app_group_identity: str,
        request: main_models.ListQuotaReviewTasksRequest,
    ) -> main_models.ListQuotaReviewTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_quota_review_tasks_with_options_async(app_group_identity, request, headers, runtime)

    def list_scheduled_tasks_with_options(
        self,
        app_group_identity: str,
        request: main_models.ListScheduledTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListScheduledTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScheduledTasks',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scheduled-tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScheduledTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scheduled_tasks_with_options_async(
        self,
        app_group_identity: str,
        request: main_models.ListScheduledTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListScheduledTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScheduledTasks',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scheduled-tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScheduledTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scheduled_tasks(
        self,
        app_group_identity: str,
        request: main_models.ListScheduledTasksRequest,
    ) -> main_models.ListScheduledTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_scheduled_tasks_with_options(app_group_identity, request, headers, runtime)

    async def list_scheduled_tasks_async(
        self,
        app_group_identity: str,
        request: main_models.ListScheduledTasksRequest,
    ) -> main_models.ListScheduledTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_scheduled_tasks_with_options_async(app_group_identity, request, headers, runtime)

    def list_search_strategies_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSearchStrategiesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListSearchStrategies',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/search-strategies',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSearchStrategiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_search_strategies_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSearchStrategiesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListSearchStrategies',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/search-strategies',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSearchStrategiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_search_strategies(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> main_models.ListSearchStrategiesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_search_strategies_with_options(app_group_identity, app_id, headers, runtime)

    async def list_search_strategies_async(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> main_models.ListSearchStrategiesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_search_strategies_with_options_async(app_group_identity, app_id, headers, runtime)

    def list_second_ranks_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSecondRanksResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListSecondRanks',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/second-ranks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecondRanksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_second_ranks_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSecondRanksResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListSecondRanks',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/second-ranks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecondRanksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_second_ranks(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> main_models.ListSecondRanksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_second_ranks_with_options(app_group_identity, app_id, headers, runtime)

    async def list_second_ranks_async(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> main_models.ListSecondRanksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_second_ranks_with_options_async(app_group_identity, app_id, headers, runtime)

    def list_slow_query_categories_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSlowQueryCategoriesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListSlowQueryCategories',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/optimizers/slow-query/categories',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSlowQueryCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_slow_query_categories_with_options_async(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSlowQueryCategoriesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListSlowQueryCategories',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/optimizers/slow-query/categories',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSlowQueryCategoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_slow_query_categories(
        self,
        app_group_identity: str,
    ) -> main_models.ListSlowQueryCategoriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_slow_query_categories_with_options(app_group_identity, headers, runtime)

    async def list_slow_query_categories_async(
        self,
        app_group_identity: str,
    ) -> main_models.ListSlowQueryCategoriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_slow_query_categories_with_options_async(app_group_identity, headers, runtime)

    def list_slow_query_queries_with_options(
        self,
        app_group_identity: str,
        category_index: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSlowQueryQueriesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListSlowQueryQueries',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/optimizers/slow-query/categories/{DaraURL.percent_encode(category_index)}/queries',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSlowQueryQueriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_slow_query_queries_with_options_async(
        self,
        app_group_identity: str,
        category_index: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSlowQueryQueriesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListSlowQueryQueries',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/optimizers/slow-query/categories/{DaraURL.percent_encode(category_index)}/queries',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSlowQueryQueriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_slow_query_queries(
        self,
        app_group_identity: str,
        category_index: str,
    ) -> main_models.ListSlowQueryQueriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_slow_query_queries_with_options(app_group_identity, category_index, headers, runtime)

    async def list_slow_query_queries_async(
        self,
        app_group_identity: str,
        category_index: str,
    ) -> main_models.ListSlowQueryQueriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_slow_query_queries_with_options_async(app_group_identity, category_index, headers, runtime)

    def list_sort_expressions_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSortExpressionsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListSortExpressions',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/sort-expressions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSortExpressionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sort_expressions_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSortExpressionsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListSortExpressions',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/sort-expressions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSortExpressionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sort_expressions(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> main_models.ListSortExpressionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_sort_expressions_with_options(app_group_identity, app_id, headers, runtime)

    async def list_sort_expressions_async(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> main_models.ListSortExpressionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_sort_expressions_with_options_async(app_group_identity, app_id, headers, runtime)

    def list_sort_scripts_with_options(
        self,
        app_group_identity: str,
        app_version_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSortScriptsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListSortScripts',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_version_id)}/sort-scripts',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSortScriptsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sort_scripts_with_options_async(
        self,
        app_group_identity: str,
        app_version_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSortScriptsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListSortScripts',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_version_id)}/sort-scripts',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSortScriptsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sort_scripts(
        self,
        app_group_identity: str,
        app_version_id: str,
    ) -> main_models.ListSortScriptsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_sort_scripts_with_options(app_group_identity, app_version_id, headers, runtime)

    async def list_sort_scripts_async(
        self,
        app_group_identity: str,
        app_version_id: str,
    ) -> main_models.ListSortScriptsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_sort_scripts_with_options_async(app_group_identity, app_version_id, headers, runtime)

    def list_statistic_logs_with_options(
        self,
        app_group_identity: str,
        module_name: str,
        request: main_models.ListStatisticLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListStatisticLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.columns):
            query['columns'] = request.columns
        if not DaraCore.is_null(request.distinct):
            query['distinct'] = request.distinct
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.sort_by):
            query['sortBy'] = request.sort_by
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.stop_time):
            query['stopTime'] = request.stop_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStatisticLogs',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/statistic-logs/{DaraURL.percent_encode(module_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStatisticLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_statistic_logs_with_options_async(
        self,
        app_group_identity: str,
        module_name: str,
        request: main_models.ListStatisticLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListStatisticLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.columns):
            query['columns'] = request.columns
        if not DaraCore.is_null(request.distinct):
            query['distinct'] = request.distinct
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.sort_by):
            query['sortBy'] = request.sort_by
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.stop_time):
            query['stopTime'] = request.stop_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStatisticLogs',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/statistic-logs/{DaraURL.percent_encode(module_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStatisticLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_statistic_logs(
        self,
        app_group_identity: str,
        module_name: str,
        request: main_models.ListStatisticLogsRequest,
    ) -> main_models.ListStatisticLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_statistic_logs_with_options(app_group_identity, module_name, request, headers, runtime)

    async def list_statistic_logs_async(
        self,
        app_group_identity: str,
        module_name: str,
        request: main_models.ListStatisticLogsRequest,
    ) -> main_models.ListStatisticLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_statistic_logs_with_options_async(app_group_identity, module_name, request, headers, runtime)

    def list_statistic_report_with_options(
        self,
        app_group_identity: str,
        module_name: str,
        request: main_models.ListStatisticReportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListStatisticReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.columns):
            query['columns'] = request.columns
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStatisticReport',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/statistic-report/{DaraURL.percent_encode(module_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStatisticReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_statistic_report_with_options_async(
        self,
        app_group_identity: str,
        module_name: str,
        request: main_models.ListStatisticReportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListStatisticReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.columns):
            query['columns'] = request.columns
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStatisticReport',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/statistic-report/{DaraURL.percent_encode(module_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStatisticReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_statistic_report(
        self,
        app_group_identity: str,
        module_name: str,
        request: main_models.ListStatisticReportRequest,
    ) -> main_models.ListStatisticReportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_statistic_report_with_options(app_group_identity, module_name, request, headers, runtime)

    async def list_statistic_report_async(
        self,
        app_group_identity: str,
        module_name: str,
        request: main_models.ListStatisticReportRequest,
    ) -> main_models.ListStatisticReportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_statistic_report_with_options_async(app_group_identity, module_name, request, headers, runtime)

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
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id_shrink):
            query['resourceId'] = request.resource_id_shrink
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/resource-tags',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
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
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id_shrink):
            query['resourceId'] = request.resource_id_shrink
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/resource-tags',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_user_analyzer_entries_with_options(
        self,
        name: str,
        request: main_models.ListUserAnalyzerEntriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUserAnalyzerEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.word):
            query['word'] = request.word
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserAnalyzerEntries',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/user-analyzers/{DaraURL.percent_encode(name)}/entries',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserAnalyzerEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_analyzer_entries_with_options_async(
        self,
        name: str,
        request: main_models.ListUserAnalyzerEntriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUserAnalyzerEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.word):
            query['word'] = request.word
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserAnalyzerEntries',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/user-analyzers/{DaraURL.percent_encode(name)}/entries',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserAnalyzerEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_analyzer_entries(
        self,
        name: str,
        request: main_models.ListUserAnalyzerEntriesRequest,
    ) -> main_models.ListUserAnalyzerEntriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_user_analyzer_entries_with_options(name, request, headers, runtime)

    async def list_user_analyzer_entries_async(
        self,
        name: str,
        request: main_models.ListUserAnalyzerEntriesRequest,
    ) -> main_models.ListUserAnalyzerEntriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_user_analyzer_entries_with_options_async(name, request, headers, runtime)

    def list_user_analyzers_with_options(
        self,
        request: main_models.ListUserAnalyzersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUserAnalyzersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserAnalyzers',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/user-analyzers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserAnalyzersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_analyzers_with_options_async(
        self,
        request: main_models.ListUserAnalyzersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUserAnalyzersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserAnalyzers',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/user-analyzers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserAnalyzersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_analyzers(
        self,
        request: main_models.ListUserAnalyzersRequest,
    ) -> main_models.ListUserAnalyzersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_user_analyzers_with_options(request, headers, runtime)

    async def list_user_analyzers_async(
        self,
        request: main_models.ListUserAnalyzersRequest,
    ) -> main_models.ListUserAnalyzersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_user_analyzers_with_options_async(request, headers, runtime)

    def modify_app_group_with_options(
        self,
        app_group_identity: str,
        request: main_models.ModifyAppGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.current_version):
            body['currentVersion'] = request.current_version
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.domain):
            body['domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppGroup',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_group_with_options_async(
        self,
        app_group_identity: str,
        request: main_models.ModifyAppGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.current_version):
            body['currentVersion'] = request.current_version
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.domain):
            body['domain'] = request.domain
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppGroup',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_group(
        self,
        app_group_identity: str,
        request: main_models.ModifyAppGroupRequest,
    ) -> main_models.ModifyAppGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_app_group_with_options(app_group_identity, request, headers, runtime)

    async def modify_app_group_async(
        self,
        app_group_identity: str,
        request: main_models.ModifyAppGroupRequest,
    ) -> main_models.ModifyAppGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_app_group_with_options_async(app_group_identity, request, headers, runtime)

    def modify_app_group_quota_with_options(
        self,
        app_group_identity: str,
        request: main_models.ModifyAppGroupQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppGroupQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppGroupQuota',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/quota',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppGroupQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_group_quota_with_options_async(
        self,
        app_group_identity: str,
        request: main_models.ModifyAppGroupQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppGroupQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppGroupQuota',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/quota',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppGroupQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_group_quota(
        self,
        app_group_identity: str,
        request: main_models.ModifyAppGroupQuotaRequest,
    ) -> main_models.ModifyAppGroupQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_app_group_quota_with_options(app_group_identity, request, headers, runtime)

    async def modify_app_group_quota_async(
        self,
        app_group_identity: str,
        request: main_models.ModifyAppGroupQuotaRequest,
    ) -> main_models.ModifyAppGroupQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_app_group_quota_with_options_async(app_group_identity, request, headers, runtime)

    def modify_first_rank_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: main_models.ModifyFirstRankRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFirstRankResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFirstRank',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/first-ranks/{DaraURL.percent_encode(name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFirstRankResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_first_rank_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: main_models.ModifyFirstRankRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFirstRankResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFirstRank',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/first-ranks/{DaraURL.percent_encode(name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFirstRankResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_first_rank(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: main_models.ModifyFirstRankRequest,
    ) -> main_models.ModifyFirstRankResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_first_rank_with_options(app_group_identity, app_id, name, request, headers, runtime)

    async def modify_first_rank_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: main_models.ModifyFirstRankRequest,
    ) -> main_models.ModifyFirstRankResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_first_rank_with_options_async(app_group_identity, app_id, name, request, headers, runtime)

    def modify_query_processor_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: main_models.ModifyQueryProcessorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyQueryProcessorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'ModifyQueryProcessor',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/query-processors/{DaraURL.percent_encode(name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyQueryProcessorResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_query_processor_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: main_models.ModifyQueryProcessorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyQueryProcessorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'ModifyQueryProcessor',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/query-processors/{DaraURL.percent_encode(name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyQueryProcessorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_query_processor(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: main_models.ModifyQueryProcessorRequest,
    ) -> main_models.ModifyQueryProcessorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_query_processor_with_options(app_group_identity, app_id, name, request, headers, runtime)

    async def modify_query_processor_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: main_models.ModifyQueryProcessorRequest,
    ) -> main_models.ModifyQueryProcessorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_query_processor_with_options_async(app_group_identity, app_id, name, request, headers, runtime)

    def modify_scheduled_task_with_options(
        self,
        app_group_identity: str,
        task_id: str,
        request: main_models.ModifyScheduledTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyScheduledTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'ModifyScheduledTask',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scheduled-tasks/{DaraURL.percent_encode(task_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scheduled_task_with_options_async(
        self,
        app_group_identity: str,
        task_id: str,
        request: main_models.ModifyScheduledTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyScheduledTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'ModifyScheduledTask',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scheduled-tasks/{DaraURL.percent_encode(task_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyScheduledTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_scheduled_task(
        self,
        app_group_identity: str,
        task_id: str,
        request: main_models.ModifyScheduledTaskRequest,
    ) -> main_models.ModifyScheduledTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_scheduled_task_with_options(app_group_identity, task_id, request, headers, runtime)

    async def modify_scheduled_task_async(
        self,
        app_group_identity: str,
        task_id: str,
        request: main_models.ModifyScheduledTaskRequest,
    ) -> main_models.ModifyScheduledTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_scheduled_task_with_options_async(app_group_identity, task_id, request, headers, runtime)

    def modify_second_rank_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: main_models.ModifySecondRankRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifySecondRankResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ModifySecondRank',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/second-ranks/{DaraURL.percent_encode(name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySecondRankResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_second_rank_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: main_models.ModifySecondRankRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifySecondRankResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ModifySecondRank',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/second-ranks/{DaraURL.percent_encode(name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySecondRankResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_second_rank(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: main_models.ModifySecondRankRequest,
    ) -> main_models.ModifySecondRankResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_second_rank_with_options(app_group_identity, app_id, name, request, headers, runtime)

    async def modify_second_rank_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: main_models.ModifySecondRankRequest,
    ) -> main_models.ModifySecondRankResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_second_rank_with_options_async(app_group_identity, app_id, name, request, headers, runtime)

    def push_intervention_dictionary_entries_with_options(
        self,
        name: str,
        request: main_models.PushInterventionDictionaryEntriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PushInterventionDictionaryEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'PushInterventionDictionaryEntries',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/intervention-dictionaries/{DaraURL.percent_encode(name)}/entries/actions/bulk',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushInterventionDictionaryEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_intervention_dictionary_entries_with_options_async(
        self,
        name: str,
        request: main_models.PushInterventionDictionaryEntriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PushInterventionDictionaryEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'PushInterventionDictionaryEntries',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/intervention-dictionaries/{DaraURL.percent_encode(name)}/entries/actions/bulk',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushInterventionDictionaryEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_intervention_dictionary_entries(
        self,
        name: str,
        request: main_models.PushInterventionDictionaryEntriesRequest,
    ) -> main_models.PushInterventionDictionaryEntriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.push_intervention_dictionary_entries_with_options(name, request, headers, runtime)

    async def push_intervention_dictionary_entries_async(
        self,
        name: str,
        request: main_models.PushInterventionDictionaryEntriesRequest,
    ) -> main_models.PushInterventionDictionaryEntriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.push_intervention_dictionary_entries_with_options_async(name, request, headers, runtime)

    def push_user_analyzer_entries_with_options(
        self,
        name: str,
        request: main_models.PushUserAnalyzerEntriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PushUserAnalyzerEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.entries):
            body['entries'] = request.entries
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushUserAnalyzerEntries',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/user-analyzers/{DaraURL.percent_encode(name)}/entries/actions/bulk',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushUserAnalyzerEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_user_analyzer_entries_with_options_async(
        self,
        name: str,
        request: main_models.PushUserAnalyzerEntriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PushUserAnalyzerEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.entries):
            body['entries'] = request.entries
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushUserAnalyzerEntries',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/user-analyzers/{DaraURL.percent_encode(name)}/entries/actions/bulk',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushUserAnalyzerEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_user_analyzer_entries(
        self,
        name: str,
        request: main_models.PushUserAnalyzerEntriesRequest,
    ) -> main_models.PushUserAnalyzerEntriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.push_user_analyzer_entries_with_options(name, request, headers, runtime)

    async def push_user_analyzer_entries_async(
        self,
        name: str,
        request: main_models.PushUserAnalyzerEntriesRequest,
    ) -> main_models.PushUserAnalyzerEntriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.push_user_analyzer_entries_with_options_async(name, request, headers, runtime)

    def release_sort_script_with_options(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseSortScriptResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ReleaseSortScript',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_version_id)}/sort-scripts/{DaraURL.percent_encode(script_name)}/actions/release',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseSortScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_sort_script_with_options_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseSortScriptResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ReleaseSortScript',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_version_id)}/sort-scripts/{DaraURL.percent_encode(script_name)}/actions/release',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseSortScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_sort_script(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
    ) -> main_models.ReleaseSortScriptResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.release_sort_script_with_options(app_group_identity, script_name, app_version_id, headers, runtime)

    async def release_sort_script_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
    ) -> main_models.ReleaseSortScriptResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.release_sort_script_with_options_async(app_group_identity, script_name, app_version_id, headers, runtime)

    def remove_app_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveAppResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveApp',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_app_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveAppResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveApp',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_app(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> main_models.RemoveAppResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.remove_app_with_options(app_group_identity, app_id, headers, runtime)

    async def remove_app_async(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> main_models.RemoveAppResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.remove_app_with_options_async(app_group_identity, app_id, headers, runtime)

    def remove_app_group_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveAppGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveAppGroup',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_app_group_with_options_async(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveAppGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveAppGroup',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveAppGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_app_group(
        self,
        app_group_identity: str,
    ) -> main_models.RemoveAppGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.remove_app_group_with_options(app_group_identity, headers, runtime)

    async def remove_app_group_async(
        self,
        app_group_identity: str,
    ) -> main_models.RemoveAppGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.remove_app_group_with_options_async(app_group_identity, headers, runtime)

    def remove_data_collection_with_options(
        self,
        app_group_identity: str,
        data_collection_identity: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveDataCollectionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveDataCollection',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/data-collections/{DaraURL.percent_encode(data_collection_identity)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveDataCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_data_collection_with_options_async(
        self,
        app_group_identity: str,
        data_collection_identity: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveDataCollectionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveDataCollection',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/data-collections/{DaraURL.percent_encode(data_collection_identity)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveDataCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_data_collection(
        self,
        app_group_identity: str,
        data_collection_identity: str,
    ) -> main_models.RemoveDataCollectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.remove_data_collection_with_options(app_group_identity, data_collection_identity, headers, runtime)

    async def remove_data_collection_async(
        self,
        app_group_identity: str,
        data_collection_identity: str,
    ) -> main_models.RemoveDataCollectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.remove_data_collection_with_options_async(app_group_identity, data_collection_identity, headers, runtime)

    def remove_first_rank_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveFirstRankResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveFirstRank',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/first-ranks/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveFirstRankResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_first_rank_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveFirstRankResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveFirstRank',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/first-ranks/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveFirstRankResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_first_rank(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> main_models.RemoveFirstRankResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.remove_first_rank_with_options(app_group_identity, app_id, name, headers, runtime)

    async def remove_first_rank_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> main_models.RemoveFirstRankResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.remove_first_rank_with_options_async(app_group_identity, app_id, name, headers, runtime)

    def remove_intervention_dictionary_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveInterventionDictionaryResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveInterventionDictionary',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/intervention-dictionaries/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveInterventionDictionaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_intervention_dictionary_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveInterventionDictionaryResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveInterventionDictionary',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/intervention-dictionaries/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveInterventionDictionaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_intervention_dictionary(
        self,
        name: str,
    ) -> main_models.RemoveInterventionDictionaryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.remove_intervention_dictionary_with_options(name, headers, runtime)

    async def remove_intervention_dictionary_async(
        self,
        name: str,
    ) -> main_models.RemoveInterventionDictionaryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.remove_intervention_dictionary_with_options_async(name, headers, runtime)

    def remove_query_processor_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveQueryProcessorResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveQueryProcessor',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/query-processors/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveQueryProcessorResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_query_processor_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveQueryProcessorResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveQueryProcessor',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/query-processors/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveQueryProcessorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_query_processor(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> main_models.RemoveQueryProcessorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.remove_query_processor_with_options(app_group_identity, app_id, name, headers, runtime)

    async def remove_query_processor_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> main_models.RemoveQueryProcessorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.remove_query_processor_with_options_async(app_group_identity, app_id, name, headers, runtime)

    def remove_scheduled_task_with_options(
        self,
        app_group_identity: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveScheduledTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveScheduledTask',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scheduled-tasks/{DaraURL.percent_encode(task_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_scheduled_task_with_options_async(
        self,
        app_group_identity: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveScheduledTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveScheduledTask',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scheduled-tasks/{DaraURL.percent_encode(task_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveScheduledTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_scheduled_task(
        self,
        app_group_identity: str,
        task_id: str,
    ) -> main_models.RemoveScheduledTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.remove_scheduled_task_with_options(app_group_identity, task_id, headers, runtime)

    async def remove_scheduled_task_async(
        self,
        app_group_identity: str,
        task_id: str,
    ) -> main_models.RemoveScheduledTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.remove_scheduled_task_with_options_async(app_group_identity, task_id, headers, runtime)

    def remove_search_strategy_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        strategy_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveSearchStrategyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveSearchStrategy',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/search-strategies/{DaraURL.percent_encode(strategy_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveSearchStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_search_strategy_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        strategy_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveSearchStrategyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveSearchStrategy',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/search-strategies/{DaraURL.percent_encode(strategy_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveSearchStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_search_strategy(
        self,
        app_group_identity: str,
        app_id: str,
        strategy_name: str,
    ) -> main_models.RemoveSearchStrategyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.remove_search_strategy_with_options(app_group_identity, app_id, strategy_name, headers, runtime)

    async def remove_search_strategy_async(
        self,
        app_group_identity: str,
        app_id: str,
        strategy_name: str,
    ) -> main_models.RemoveSearchStrategyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.remove_search_strategy_with_options_async(app_group_identity, app_id, strategy_name, headers, runtime)

    def remove_second_rank_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveSecondRankResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveSecondRank',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/second-ranks/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveSecondRankResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_second_rank_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveSecondRankResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveSecondRank',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/second-ranks/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveSecondRankResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_second_rank(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> main_models.RemoveSecondRankResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.remove_second_rank_with_options(app_group_identity, app_id, name, headers, runtime)

    async def remove_second_rank_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> main_models.RemoveSecondRankResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.remove_second_rank_with_options_async(app_group_identity, app_id, name, headers, runtime)

    def remove_user_analyzer_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUserAnalyzerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveUserAnalyzer',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/user-analyzers/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveUserAnalyzerResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_user_analyzer_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUserAnalyzerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveUserAnalyzer',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/user-analyzers/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveUserAnalyzerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_user_analyzer(
        self,
        name: str,
    ) -> main_models.RemoveUserAnalyzerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.remove_user_analyzer_with_options(name, headers, runtime)

    async def remove_user_analyzer_async(
        self,
        name: str,
    ) -> main_models.RemoveUserAnalyzerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.remove_user_analyzer_with_options_async(name, headers, runtime)

    def renew_app_group_with_options(
        self,
        app_group_identity: str,
        request: main_models.RenewAppGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RenewAppGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'RenewAppGroup',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/actions/renew',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_app_group_with_options_async(
        self,
        app_group_identity: str,
        request: main_models.RenewAppGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RenewAppGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'RenewAppGroup',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/actions/renew',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewAppGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_app_group(
        self,
        app_group_identity: str,
        request: main_models.RenewAppGroupRequest,
    ) -> main_models.RenewAppGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.renew_app_group_with_options(app_group_identity, request, headers, runtime)

    async def renew_app_group_async(
        self,
        app_group_identity: str,
        request: main_models.RenewAppGroupRequest,
    ) -> main_models.RenewAppGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.renew_app_group_with_options_async(app_group_identity, request, headers, runtime)

    def replace_app_group_commodity_code_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReplaceAppGroupCommodityCodeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ReplaceAppGroupCommodityCode',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/actions/to-instance-typed',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReplaceAppGroupCommodityCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def replace_app_group_commodity_code_with_options_async(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReplaceAppGroupCommodityCodeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ReplaceAppGroupCommodityCode',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/actions/to-instance-typed',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReplaceAppGroupCommodityCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def replace_app_group_commodity_code(
        self,
        app_group_identity: str,
    ) -> main_models.ReplaceAppGroupCommodityCodeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.replace_app_group_commodity_code_with_options(app_group_identity, headers, runtime)

    async def replace_app_group_commodity_code_async(
        self,
        app_group_identity: str,
    ) -> main_models.ReplaceAppGroupCommodityCodeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.replace_app_group_commodity_code_with_options_async(app_group_identity, headers, runtime)

    def save_sort_script_file_with_options(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        file_name: str,
        request: main_models.SaveSortScriptFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SaveSortScriptFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveSortScriptFile',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_version_id)}/sort-scripts/{DaraURL.percent_encode(script_name)}/files/src/{DaraURL.percent_encode(file_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSortScriptFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_sort_script_file_with_options_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        file_name: str,
        request: main_models.SaveSortScriptFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SaveSortScriptFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveSortScriptFile',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_version_id)}/sort-scripts/{DaraURL.percent_encode(script_name)}/files/src/{DaraURL.percent_encode(file_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveSortScriptFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_sort_script_file(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        file_name: str,
        request: main_models.SaveSortScriptFileRequest,
    ) -> main_models.SaveSortScriptFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.save_sort_script_file_with_options(app_group_identity, script_name, app_version_id, file_name, request, headers, runtime)

    async def save_sort_script_file_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        file_name: str,
        request: main_models.SaveSortScriptFileRequest,
    ) -> main_models.SaveSortScriptFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.save_sort_script_file_with_options_async(app_group_identity, script_name, app_version_id, file_name, request, headers, runtime)

    def start_slow_query_analyzer_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartSlowQueryAnalyzerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StartSlowQueryAnalyzer',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/optimizers/slow-query/actions/run',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartSlowQueryAnalyzerResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_slow_query_analyzer_with_options_async(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartSlowQueryAnalyzerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StartSlowQueryAnalyzer',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/optimizers/slow-query/actions/run',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartSlowQueryAnalyzerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_slow_query_analyzer(
        self,
        app_group_identity: str,
    ) -> main_models.StartSlowQueryAnalyzerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_slow_query_analyzer_with_options(app_group_identity, headers, runtime)

    async def start_slow_query_analyzer_async(
        self,
        app_group_identity: str,
    ) -> main_models.StartSlowQueryAnalyzerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_slow_query_analyzer_with_options_async(app_group_identity, headers, runtime)

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
        if not DaraCore.is_null(request.tag):
            body['tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/resource-tags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
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
        if not DaraCore.is_null(request.tag):
            body['tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/resource-tags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def unbind_esuser_analyzer_with_options(
        self,
        app_group_identity: str,
        es_instance_id: str,
        request: main_models.UnbindESUserAnalyzerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnbindESUserAnalyzerResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UnbindESUserAnalyzer',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/es/{DaraURL.percent_encode(es_instance_id)}/actions/unbind-analyzer',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindESUserAnalyzerResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_esuser_analyzer_with_options_async(
        self,
        app_group_identity: str,
        es_instance_id: str,
        request: main_models.UnbindESUserAnalyzerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnbindESUserAnalyzerResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UnbindESUserAnalyzer',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/es/{DaraURL.percent_encode(es_instance_id)}/actions/unbind-analyzer',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindESUserAnalyzerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_esuser_analyzer(
        self,
        app_group_identity: str,
        es_instance_id: str,
        request: main_models.UnbindESUserAnalyzerRequest,
    ) -> main_models.UnbindESUserAnalyzerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.unbind_esuser_analyzer_with_options(app_group_identity, es_instance_id, request, headers, runtime)

    async def unbind_esuser_analyzer_async(
        self,
        app_group_identity: str,
        es_instance_id: str,
        request: main_models.UnbindESUserAnalyzerRequest,
    ) -> main_models.UnbindESUserAnalyzerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.unbind_esuser_analyzer_with_options_async(app_group_identity, es_instance_id, request, headers, runtime)

    def unbind_es_instance_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnbindEsInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'UnbindEsInstance',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/actions/unbind-es-instance',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindEsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_es_instance_with_options_async(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnbindEsInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'UnbindEsInstance',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/actions/unbind-es-instance',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindEsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_es_instance(
        self,
        app_group_identity: str,
    ) -> main_models.UnbindEsInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.unbind_es_instance_with_options(app_group_identity, headers, runtime)

    async def unbind_es_instance_async(
        self,
        app_group_identity: str,
    ) -> main_models.UnbindEsInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.unbind_es_instance_with_options_async(app_group_identity, headers, runtime)

    def untag_resources_with_options(
        self,
        tmp_req: main_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        tmp_req.validate()
        request = main_models.UntagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id):
            request.resource_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id, 'resourceId', 'json')
        if not DaraCore.is_null(tmp_req.tag_key):
            request.tag_key_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_key, 'tagKey', 'json')
        query = {}
        if not DaraCore.is_null(request.all):
            query['all'] = request.all
        if not DaraCore.is_null(request.resource_id_shrink):
            query['resourceId'] = request.resource_id_shrink
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key_shrink):
            query['tagKey'] = request.tag_key_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/resource-tags',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        tmp_req: main_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        tmp_req.validate()
        request = main_models.UntagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id):
            request.resource_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id, 'resourceId', 'json')
        if not DaraCore.is_null(tmp_req.tag_key):
            request.tag_key_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_key, 'tagKey', 'json')
        query = {}
        if not DaraCore.is_null(request.all):
            query['all'] = request.all
        if not DaraCore.is_null(request.resource_id_shrink):
            query['resourceId'] = request.resource_id_shrink
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key_shrink):
            query['tagKey'] = request.tag_key_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/resource-tags',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def update_abtest_experiment_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        request: main_models.UpdateABTestExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateABTestExperimentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateABTestExperiment',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}/groups/{DaraURL.percent_encode(group_id)}/experiments/{DaraURL.percent_encode(experiment_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateABTestExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_abtest_experiment_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        request: main_models.UpdateABTestExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateABTestExperimentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateABTestExperiment',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}/groups/{DaraURL.percent_encode(group_id)}/experiments/{DaraURL.percent_encode(experiment_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateABTestExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_abtest_experiment(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        request: main_models.UpdateABTestExperimentRequest,
    ) -> main_models.UpdateABTestExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_abtest_experiment_with_options(app_group_identity, scene_id, group_id, experiment_id, request, headers, runtime)

    async def update_abtest_experiment_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        request: main_models.UpdateABTestExperimentRequest,
    ) -> main_models.UpdateABTestExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_abtest_experiment_with_options_async(app_group_identity, scene_id, group_id, experiment_id, request, headers, runtime)

    def update_abtest_fixed_flow_dividers_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        request: main_models.UpdateABTestFixedFlowDividersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateABTestFixedFlowDividersResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateABTestFixedFlowDividers',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}/groups/{DaraURL.percent_encode(group_id)}/experiments/{DaraURL.percent_encode(experiment_id)}/fixed-flow-dividers',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateABTestFixedFlowDividersResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_abtest_fixed_flow_dividers_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        request: main_models.UpdateABTestFixedFlowDividersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateABTestFixedFlowDividersResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateABTestFixedFlowDividers',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}/groups/{DaraURL.percent_encode(group_id)}/experiments/{DaraURL.percent_encode(experiment_id)}/fixed-flow-dividers',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateABTestFixedFlowDividersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_abtest_fixed_flow_dividers(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        request: main_models.UpdateABTestFixedFlowDividersRequest,
    ) -> main_models.UpdateABTestFixedFlowDividersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_abtest_fixed_flow_dividers_with_options(app_group_identity, scene_id, group_id, experiment_id, request, headers, runtime)

    async def update_abtest_fixed_flow_dividers_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        request: main_models.UpdateABTestFixedFlowDividersRequest,
    ) -> main_models.UpdateABTestFixedFlowDividersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_abtest_fixed_flow_dividers_with_options_async(app_group_identity, scene_id, group_id, experiment_id, request, headers, runtime)

    def update_abtest_group_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        request: main_models.UpdateABTestGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateABTestGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateABTestGroup',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}/groups/{DaraURL.percent_encode(group_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateABTestGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_abtest_group_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        request: main_models.UpdateABTestGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateABTestGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateABTestGroup',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}/groups/{DaraURL.percent_encode(group_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateABTestGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_abtest_group(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        request: main_models.UpdateABTestGroupRequest,
    ) -> main_models.UpdateABTestGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_abtest_group_with_options(app_group_identity, scene_id, group_id, request, headers, runtime)

    async def update_abtest_group_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        request: main_models.UpdateABTestGroupRequest,
    ) -> main_models.UpdateABTestGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_abtest_group_with_options_async(app_group_identity, scene_id, group_id, request, headers, runtime)

    def update_abtest_scene_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        request: main_models.UpdateABTestSceneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateABTestSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateABTestScene',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateABTestSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_abtest_scene_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        request: main_models.UpdateABTestSceneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateABTestSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateABTestScene',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/scenes/{DaraURL.percent_encode(scene_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateABTestSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_abtest_scene(
        self,
        app_group_identity: str,
        scene_id: str,
        request: main_models.UpdateABTestSceneRequest,
    ) -> main_models.UpdateABTestSceneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_abtest_scene_with_options(app_group_identity, scene_id, request, headers, runtime)

    async def update_abtest_scene_async(
        self,
        app_group_identity: str,
        scene_id: str,
        request: main_models.UpdateABTestSceneRequest,
    ) -> main_models.UpdateABTestSceneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_abtest_scene_with_options_async(app_group_identity, scene_id, request, headers, runtime)

    def update_fetch_fields_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        request: main_models.UpdateFetchFieldsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFetchFieldsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateFetchFields',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/fetch-fields',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFetchFieldsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_fetch_fields_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: main_models.UpdateFetchFieldsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFetchFieldsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateFetchFields',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/fetch-fields',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFetchFieldsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_fetch_fields(
        self,
        app_group_identity: str,
        app_id: str,
        request: main_models.UpdateFetchFieldsRequest,
    ) -> main_models.UpdateFetchFieldsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_fetch_fields_with_options(app_group_identity, app_id, request, headers, runtime)

    async def update_fetch_fields_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: main_models.UpdateFetchFieldsRequest,
    ) -> main_models.UpdateFetchFieldsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_fetch_fields_with_options_async(app_group_identity, app_id, request, headers, runtime)

    def update_function_default_instance_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        request: main_models.UpdateFunctionDefaultInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFunctionDefaultInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_name):
            body['instanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFunctionDefaultInstance',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/default-instance',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFunctionDefaultInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_function_default_instance_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        request: main_models.UpdateFunctionDefaultInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFunctionDefaultInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_name):
            body['instanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFunctionDefaultInstance',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/default-instance',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFunctionDefaultInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_function_default_instance(
        self,
        app_group_identity: str,
        function_name: str,
        request: main_models.UpdateFunctionDefaultInstanceRequest,
    ) -> main_models.UpdateFunctionDefaultInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_function_default_instance_with_options(app_group_identity, function_name, request, headers, runtime)

    async def update_function_default_instance_async(
        self,
        app_group_identity: str,
        function_name: str,
        request: main_models.UpdateFunctionDefaultInstanceRequest,
    ) -> main_models.UpdateFunctionDefaultInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_function_default_instance_with_options_async(app_group_identity, function_name, request, headers, runtime)

    def update_function_instance_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        request: main_models.UpdateFunctionInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFunctionInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.create_parameters):
            body['createParameters'] = request.create_parameters
        if not DaraCore.is_null(request.cron):
            body['cron'] = request.cron
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.usage_parameters):
            body['usageParameters'] = request.usage_parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFunctionInstance',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/instances/{DaraURL.percent_encode(instance_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFunctionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_function_instance_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        request: main_models.UpdateFunctionInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFunctionInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.create_parameters):
            body['createParameters'] = request.create_parameters
        if not DaraCore.is_null(request.cron):
            body['cron'] = request.cron
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.usage_parameters):
            body['usageParameters'] = request.usage_parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFunctionInstance',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/instances/{DaraURL.percent_encode(instance_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFunctionInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_function_instance(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        request: main_models.UpdateFunctionInstanceRequest,
    ) -> main_models.UpdateFunctionInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_function_instance_with_options(app_group_identity, function_name, instance_name, request, headers, runtime)

    async def update_function_instance_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        request: main_models.UpdateFunctionInstanceRequest,
    ) -> main_models.UpdateFunctionInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_function_instance_with_options_async(app_group_identity, function_name, instance_name, request, headers, runtime)

    def update_function_resource_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        resource_name: str,
        request: main_models.UpdateFunctionResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFunctionResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFunctionResource',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/resources/{DaraURL.percent_encode(resource_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFunctionResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_function_resource_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        resource_name: str,
        request: main_models.UpdateFunctionResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFunctionResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFunctionResource',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/functions/{DaraURL.percent_encode(function_name)}/resources/{DaraURL.percent_encode(resource_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFunctionResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_function_resource(
        self,
        app_group_identity: str,
        function_name: str,
        resource_name: str,
        request: main_models.UpdateFunctionResourceRequest,
    ) -> main_models.UpdateFunctionResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_function_resource_with_options(app_group_identity, function_name, resource_name, request, headers, runtime)

    async def update_function_resource_async(
        self,
        app_group_identity: str,
        function_name: str,
        resource_name: str,
        request: main_models.UpdateFunctionResourceRequest,
    ) -> main_models.UpdateFunctionResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_function_resource_with_options_async(app_group_identity, function_name, resource_name, request, headers, runtime)

    def update_search_strategy_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        strategy_name: str,
        request: main_models.UpdateSearchStrategyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSearchStrategyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSearchStrategy',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/search-strategies/{DaraURL.percent_encode(strategy_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSearchStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_search_strategy_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        strategy_name: str,
        request: main_models.UpdateSearchStrategyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSearchStrategyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSearchStrategy',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/search-strategies/{DaraURL.percent_encode(strategy_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSearchStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_search_strategy(
        self,
        app_group_identity: str,
        app_id: str,
        strategy_name: str,
        request: main_models.UpdateSearchStrategyRequest,
    ) -> main_models.UpdateSearchStrategyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_search_strategy_with_options(app_group_identity, app_id, strategy_name, request, headers, runtime)

    async def update_search_strategy_async(
        self,
        app_group_identity: str,
        app_id: str,
        strategy_name: str,
        request: main_models.UpdateSearchStrategyRequest,
    ) -> main_models.UpdateSearchStrategyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_search_strategy_with_options_async(app_group_identity, app_id, strategy_name, request, headers, runtime)

    def update_sort_script_with_options(
        self,
        app_group_identity: str,
        app_version_id: str,
        script_name: str,
        request: main_models.UpdateSortScriptRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSortScriptResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSortScript',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_version_id)}/sort-scripts/{DaraURL.percent_encode(script_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSortScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sort_script_with_options_async(
        self,
        app_group_identity: str,
        app_version_id: str,
        script_name: str,
        request: main_models.UpdateSortScriptRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSortScriptResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSortScript',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_version_id)}/sort-scripts/{DaraURL.percent_encode(script_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSortScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sort_script(
        self,
        app_group_identity: str,
        app_version_id: str,
        script_name: str,
        request: main_models.UpdateSortScriptRequest,
    ) -> main_models.UpdateSortScriptResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_sort_script_with_options(app_group_identity, app_version_id, script_name, request, headers, runtime)

    async def update_sort_script_async(
        self,
        app_group_identity: str,
        app_version_id: str,
        script_name: str,
        request: main_models.UpdateSortScriptRequest,
    ) -> main_models.UpdateSortScriptResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_sort_script_with_options_async(app_group_identity, app_version_id, script_name, request, headers, runtime)

    def update_summaries_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        request: main_models.UpdateSummariesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSummariesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSummaries',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/summaries',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSummariesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_summaries_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: main_models.UpdateSummariesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSummariesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSummaries',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/app-groups/{DaraURL.percent_encode(app_group_identity)}/apps/{DaraURL.percent_encode(app_id)}/summaries',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSummariesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_summaries(
        self,
        app_group_identity: str,
        app_id: str,
        request: main_models.UpdateSummariesRequest,
    ) -> main_models.UpdateSummariesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_summaries_with_options(app_group_identity, app_id, request, headers, runtime)

    async def update_summaries_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: main_models.UpdateSummariesRequest,
    ) -> main_models.UpdateSummariesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_summaries_with_options_async(app_group_identity, app_id, request, headers, runtime)

    def validate_data_sources_with_options(
        self,
        request: main_models.ValidateDataSourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ValidateDataSourcesResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ValidateDataSources',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/assist/data-sources/validations',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_data_sources_with_options_async(
        self,
        request: main_models.ValidateDataSourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ValidateDataSourcesResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ValidateDataSources',
            version = '2017-12-25',
            protocol = 'HTTPS',
            pathname = f'/v4/openapi/assist/data-sources/validations',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateDataSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_data_sources(
        self,
        request: main_models.ValidateDataSourcesRequest,
    ) -> main_models.ValidateDataSourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.validate_data_sources_with_options(request, headers, runtime)

    async def validate_data_sources_async(
        self,
        request: main_models.ValidateDataSourcesRequest,
    ) -> main_models.ValidateDataSourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.validate_data_sources_with_options_async(request, headers, runtime)
