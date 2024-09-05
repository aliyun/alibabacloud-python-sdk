# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_opensearch20171225 import models as open_search_20171225_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def bind_esuser_analyzer_with_options(
        self,
        app_group_identity: str,
        es_instance_id: str,
        request: open_search_20171225_models.BindESUserAnalyzerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.BindESUserAnalyzerResponse:
        """
        @summary Binds a custom analyzer to an Elasticsearch instance.
        
        @param request: BindESUserAnalyzerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindESUserAnalyzerResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='BindESUserAnalyzer',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/es/{OpenApiUtilClient.get_encode_param(es_instance_id)}/actions/bind-analyzer',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.BindESUserAnalyzerResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_esuser_analyzer_with_options_async(
        self,
        app_group_identity: str,
        es_instance_id: str,
        request: open_search_20171225_models.BindESUserAnalyzerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.BindESUserAnalyzerResponse:
        """
        @summary Binds a custom analyzer to an Elasticsearch instance.
        
        @param request: BindESUserAnalyzerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindESUserAnalyzerResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='BindESUserAnalyzer',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/es/{OpenApiUtilClient.get_encode_param(es_instance_id)}/actions/bind-analyzer',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.BindESUserAnalyzerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_esuser_analyzer(
        self,
        app_group_identity: str,
        es_instance_id: str,
        request: open_search_20171225_models.BindESUserAnalyzerRequest,
    ) -> open_search_20171225_models.BindESUserAnalyzerResponse:
        """
        @summary Binds a custom analyzer to an Elasticsearch instance.
        
        @param request: BindESUserAnalyzerRequest
        @return: BindESUserAnalyzerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.bind_esuser_analyzer_with_options(app_group_identity, es_instance_id, request, headers, runtime)

    async def bind_esuser_analyzer_async(
        self,
        app_group_identity: str,
        es_instance_id: str,
        request: open_search_20171225_models.BindESUserAnalyzerRequest,
    ) -> open_search_20171225_models.BindESUserAnalyzerResponse:
        """
        @summary Binds a custom analyzer to an Elasticsearch instance.
        
        @param request: BindESUserAnalyzerRequest
        @return: BindESUserAnalyzerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.bind_esuser_analyzer_with_options_async(app_group_identity, es_instance_id, request, headers, runtime)

    def bind_es_instance_with_options(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.BindEsInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.BindEsInstanceResponse:
        """
        @summary Binds an Elasticsearch instance.
        
        @param request: BindEsInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindEsInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BindEsInstance',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/actions/bind-es-instance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.BindEsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_es_instance_with_options_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.BindEsInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.BindEsInstanceResponse:
        """
        @summary Binds an Elasticsearch instance.
        
        @param request: BindEsInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindEsInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BindEsInstance',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/actions/bind-es-instance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.BindEsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_es_instance(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.BindEsInstanceRequest,
    ) -> open_search_20171225_models.BindEsInstanceResponse:
        """
        @summary Binds an Elasticsearch instance.
        
        @param request: BindEsInstanceRequest
        @return: BindEsInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.bind_es_instance_with_options(app_group_identity, request, headers, runtime)

    async def bind_es_instance_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.BindEsInstanceRequest,
    ) -> open_search_20171225_models.BindEsInstanceResponse:
        """
        @summary Binds an Elasticsearch instance.
        
        @param request: BindEsInstanceRequest
        @return: BindEsInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.bind_es_instance_with_options_async(app_group_identity, request, headers, runtime)

    def compile_sort_script_with_options(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CompileSortScriptResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CompileSortScriptResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CompileSortScript',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_version_id)}/sort-scripts/{OpenApiUtilClient.get_encode_param(script_name)}/actions/compiling',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CompileSortScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def compile_sort_script_with_options_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CompileSortScriptResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CompileSortScriptResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CompileSortScript',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_version_id)}/sort-scripts/{OpenApiUtilClient.get_encode_param(script_name)}/actions/compiling',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CompileSortScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def compile_sort_script(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
    ) -> open_search_20171225_models.CompileSortScriptResponse:
        """
        @return: CompileSortScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.compile_sort_script_with_options(app_group_identity, script_name, app_version_id, headers, runtime)

    async def compile_sort_script_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
    ) -> open_search_20171225_models.CompileSortScriptResponse:
        """
        @return: CompileSortScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.compile_sort_script_with_options_async(app_group_identity, script_name, app_version_id, headers, runtime)

    def create_abtest_experiment_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        request: open_search_20171225_models.CreateABTestExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateABTestExperimentResponse:
        """
        @summary Creates an experiment.
        
        @param request: CreateABTestExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateABTestExperimentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateABTestExperiment',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}/experiments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateABTestExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_abtest_experiment_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        request: open_search_20171225_models.CreateABTestExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateABTestExperimentResponse:
        """
        @summary Creates an experiment.
        
        @param request: CreateABTestExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateABTestExperimentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateABTestExperiment',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}/experiments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateABTestExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_abtest_experiment(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        request: open_search_20171225_models.CreateABTestExperimentRequest,
    ) -> open_search_20171225_models.CreateABTestExperimentResponse:
        """
        @summary Creates an experiment.
        
        @param request: CreateABTestExperimentRequest
        @return: CreateABTestExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_abtest_experiment_with_options(app_group_identity, scene_id, group_id, request, headers, runtime)

    async def create_abtest_experiment_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        request: open_search_20171225_models.CreateABTestExperimentRequest,
    ) -> open_search_20171225_models.CreateABTestExperimentResponse:
        """
        @summary Creates an experiment.
        
        @param request: CreateABTestExperimentRequest
        @return: CreateABTestExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_abtest_experiment_with_options_async(app_group_identity, scene_id, group_id, request, headers, runtime)

    def create_abtest_group_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        request: open_search_20171225_models.CreateABTestGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateABTestGroupResponse:
        """
        @summary Creates a test group.
        
        @param request: CreateABTestGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateABTestGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateABTestGroup',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateABTestGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_abtest_group_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        request: open_search_20171225_models.CreateABTestGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateABTestGroupResponse:
        """
        @summary Creates a test group.
        
        @param request: CreateABTestGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateABTestGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateABTestGroup',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateABTestGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_abtest_group(
        self,
        app_group_identity: str,
        scene_id: str,
        request: open_search_20171225_models.CreateABTestGroupRequest,
    ) -> open_search_20171225_models.CreateABTestGroupResponse:
        """
        @summary Creates a test group.
        
        @param request: CreateABTestGroupRequest
        @return: CreateABTestGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_abtest_group_with_options(app_group_identity, scene_id, request, headers, runtime)

    async def create_abtest_group_async(
        self,
        app_group_identity: str,
        scene_id: str,
        request: open_search_20171225_models.CreateABTestGroupRequest,
    ) -> open_search_20171225_models.CreateABTestGroupResponse:
        """
        @summary Creates a test group.
        
        @param request: CreateABTestGroupRequest
        @return: CreateABTestGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_abtest_group_with_options_async(app_group_identity, scene_id, request, headers, runtime)

    def create_abtest_scene_with_options(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.CreateABTestSceneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateABTestSceneResponse:
        """
        @param request: CreateABTestSceneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateABTestSceneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateABTestScene',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateABTestSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_abtest_scene_with_options_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.CreateABTestSceneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateABTestSceneResponse:
        """
        @param request: CreateABTestSceneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateABTestSceneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateABTestScene',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateABTestSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_abtest_scene(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.CreateABTestSceneRequest,
    ) -> open_search_20171225_models.CreateABTestSceneResponse:
        """
        @param request: CreateABTestSceneRequest
        @return: CreateABTestSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_abtest_scene_with_options(app_group_identity, request, headers, runtime)

    async def create_abtest_scene_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.CreateABTestSceneRequest,
    ) -> open_search_20171225_models.CreateABTestSceneResponse:
        """
        @param request: CreateABTestSceneRequest
        @return: CreateABTestSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_abtest_scene_with_options_async(app_group_identity, request, headers, runtime)

    def create_app_with_options(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.CreateAppRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateAppResponse:
        """
        @summary Creates a version for an OpenSearch application.
        
        @description    When you create a standard application, a new version of the application is created if the specified application name already exists.
        When you create a version of an existing application, you must specify the autoSwitch and realtimeShared parameters.
        When you create a version of an existing application, the value of the quota parameter is the same as that of the quota parameter in the previous version of the application.
        When you create a version of an existing application, the modification of the value of the quota parameter does not take effect.
        
        @param request: CreateAppRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.auto_switch):
            body['autoSwitch'] = request.auto_switch
        if not UtilClient.is_unset(request.cluster):
            body['cluster'] = request.cluster
        if not UtilClient.is_unset(request.data_sources):
            body['dataSources'] = request.data_sources
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.domain):
            body['domain'] = request.domain
        if not UtilClient.is_unset(request.fetch_fields):
            body['fetchFields'] = request.fetch_fields
        if not UtilClient.is_unset(request.first_ranks):
            body['firstRanks'] = request.first_ranks
        if not UtilClient.is_unset(request.network_type):
            body['networkType'] = request.network_type
        if not UtilClient.is_unset(request.query_processors):
            body['queryProcessors'] = request.query_processors
        if not UtilClient.is_unset(request.schema):
            body['schema'] = request.schema
        if not UtilClient.is_unset(request.schemas):
            body['schemas'] = request.schemas
        if not UtilClient.is_unset(request.second_ranks):
            body['secondRanks'] = request.second_ranks
        if not UtilClient.is_unset(request.summaries):
            body['summaries'] = request.summaries
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_with_options_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.CreateAppRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateAppResponse:
        """
        @summary Creates a version for an OpenSearch application.
        
        @description    When you create a standard application, a new version of the application is created if the specified application name already exists.
        When you create a version of an existing application, you must specify the autoSwitch and realtimeShared parameters.
        When you create a version of an existing application, the value of the quota parameter is the same as that of the quota parameter in the previous version of the application.
        When you create a version of an existing application, the modification of the value of the quota parameter does not take effect.
        
        @param request: CreateAppRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.auto_switch):
            body['autoSwitch'] = request.auto_switch
        if not UtilClient.is_unset(request.cluster):
            body['cluster'] = request.cluster
        if not UtilClient.is_unset(request.data_sources):
            body['dataSources'] = request.data_sources
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.domain):
            body['domain'] = request.domain
        if not UtilClient.is_unset(request.fetch_fields):
            body['fetchFields'] = request.fetch_fields
        if not UtilClient.is_unset(request.first_ranks):
            body['firstRanks'] = request.first_ranks
        if not UtilClient.is_unset(request.network_type):
            body['networkType'] = request.network_type
        if not UtilClient.is_unset(request.query_processors):
            body['queryProcessors'] = request.query_processors
        if not UtilClient.is_unset(request.schema):
            body['schema'] = request.schema
        if not UtilClient.is_unset(request.schemas):
            body['schemas'] = request.schemas
        if not UtilClient.is_unset(request.second_ranks):
            body['secondRanks'] = request.second_ranks
        if not UtilClient.is_unset(request.summaries):
            body['summaries'] = request.summaries
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.CreateAppRequest,
    ) -> open_search_20171225_models.CreateAppResponse:
        """
        @summary Creates a version for an OpenSearch application.
        
        @description    When you create a standard application, a new version of the application is created if the specified application name already exists.
        When you create a version of an existing application, you must specify the autoSwitch and realtimeShared parameters.
        When you create a version of an existing application, the value of the quota parameter is the same as that of the quota parameter in the previous version of the application.
        When you create a version of an existing application, the modification of the value of the quota parameter does not take effect.
        
        @param request: CreateAppRequest
        @return: CreateAppResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_app_with_options(app_group_identity, request, headers, runtime)

    async def create_app_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.CreateAppRequest,
    ) -> open_search_20171225_models.CreateAppResponse:
        """
        @summary Creates a version for an OpenSearch application.
        
        @description    When you create a standard application, a new version of the application is created if the specified application name already exists.
        When you create a version of an existing application, you must specify the autoSwitch and realtimeShared parameters.
        When you create a version of an existing application, the value of the quota parameter is the same as that of the quota parameter in the previous version of the application.
        When you create a version of an existing application, the modification of the value of the quota parameter does not take effect.
        
        @param request: CreateAppRequest
        @return: CreateAppResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_app_with_options_async(app_group_identity, request, headers, runtime)

    def create_app_group_with_options(
        self,
        request: open_search_20171225_models.CreateAppGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateAppGroupResponse:
        """
        @summary Create an OpenSearch application.
        
        @param request: CreateAppGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.charge_type):
            body['chargeType'] = request.charge_type
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.quota):
            body['quota'] = request.quota
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAppGroup',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_group_with_options_async(
        self,
        request: open_search_20171225_models.CreateAppGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateAppGroupResponse:
        """
        @summary Create an OpenSearch application.
        
        @param request: CreateAppGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.charge_type):
            body['chargeType'] = request.charge_type
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.quota):
            body['quota'] = request.quota
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAppGroup',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateAppGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_group(
        self,
        request: open_search_20171225_models.CreateAppGroupRequest,
    ) -> open_search_20171225_models.CreateAppGroupResponse:
        """
        @summary Create an OpenSearch application.
        
        @param request: CreateAppGroupRequest
        @return: CreateAppGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_app_group_with_options(request, headers, runtime)

    async def create_app_group_async(
        self,
        request: open_search_20171225_models.CreateAppGroupRequest,
    ) -> open_search_20171225_models.CreateAppGroupResponse:
        """
        @summary Create an OpenSearch application.
        
        @param request: CreateAppGroupRequest
        @return: CreateAppGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_app_group_with_options_async(request, headers, runtime)

    def create_app_group_credentials_with_options(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.CreateAppGroupCredentialsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateAppGroupCredentialsResponse:
        """
        @param request: CreateAppGroupCredentialsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppGroupCredentialsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAppGroupCredentials',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/credentials',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateAppGroupCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_group_credentials_with_options_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.CreateAppGroupCredentialsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateAppGroupCredentialsResponse:
        """
        @param request: CreateAppGroupCredentialsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppGroupCredentialsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAppGroupCredentials',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/credentials',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateAppGroupCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_group_credentials(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.CreateAppGroupCredentialsRequest,
    ) -> open_search_20171225_models.CreateAppGroupCredentialsResponse:
        """
        @param request: CreateAppGroupCredentialsRequest
        @return: CreateAppGroupCredentialsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_app_group_credentials_with_options(app_group_identity, request, headers, runtime)

    async def create_app_group_credentials_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.CreateAppGroupCredentialsRequest,
    ) -> open_search_20171225_models.CreateAppGroupCredentialsResponse:
        """
        @param request: CreateAppGroupCredentialsRequest
        @return: CreateAppGroupCredentialsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_app_group_credentials_with_options_async(app_group_identity, request, headers, runtime)

    def create_first_rank_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.CreateFirstRankRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateFirstRankResponse:
        """
        @summary Creates a rough sort expression for a version of an OpenSearch application. If you set dryRun to true, this operation checks the specified rough sort expression. By default, the value of dryRun is false if you do not set this parameter.
        
        @param request: CreateFirstRankRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFirstRankResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateFirstRank',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/first-ranks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateFirstRankResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_first_rank_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.CreateFirstRankRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateFirstRankResponse:
        """
        @summary Creates a rough sort expression for a version of an OpenSearch application. If you set dryRun to true, this operation checks the specified rough sort expression. By default, the value of dryRun is false if you do not set this parameter.
        
        @param request: CreateFirstRankRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFirstRankResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateFirstRank',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/first-ranks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateFirstRankResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_first_rank(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.CreateFirstRankRequest,
    ) -> open_search_20171225_models.CreateFirstRankResponse:
        """
        @summary Creates a rough sort expression for a version of an OpenSearch application. If you set dryRun to true, this operation checks the specified rough sort expression. By default, the value of dryRun is false if you do not set this parameter.
        
        @param request: CreateFirstRankRequest
        @return: CreateFirstRankResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_first_rank_with_options(app_group_identity, app_id, request, headers, runtime)

    async def create_first_rank_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.CreateFirstRankRequest,
    ) -> open_search_20171225_models.CreateFirstRankResponse:
        """
        @summary Creates a rough sort expression for a version of an OpenSearch application. If you set dryRun to true, this operation checks the specified rough sort expression. By default, the value of dryRun is false if you do not set this parameter.
        
        @param request: CreateFirstRankRequest
        @return: CreateFirstRankResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_first_rank_with_options_async(app_group_identity, app_id, request, headers, runtime)

    def create_function_instance_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        request: open_search_20171225_models.CreateFunctionInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateFunctionInstanceResponse:
        """
        @summary Creates an algorithm instance of a feature.
        
        @description You can call the [GetFunctionCurrentVersion](https://help.aliyun.com/document_detail/421377.html) operation to query the latest version of a feature. The response of the operation includes the createParameters parameter that is used to create an algorithm instance, the usageParameters parameter, and the requirements for setting these parameters.
        
        @param request: CreateFunctionInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFunctionInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.create_parameters):
            body['createParameters'] = request.create_parameters
        if not UtilClient.is_unset(request.cron):
            body['cron'] = request.cron
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.function_type):
            body['functionType'] = request.function_type
        if not UtilClient.is_unset(request.instance_name):
            body['instanceName'] = request.instance_name
        if not UtilClient.is_unset(request.model_type):
            body['modelType'] = request.model_type
        if not UtilClient.is_unset(request.usage_parameters):
            body['usageParameters'] = request.usage_parameters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFunctionInstance',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateFunctionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_function_instance_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        request: open_search_20171225_models.CreateFunctionInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateFunctionInstanceResponse:
        """
        @summary Creates an algorithm instance of a feature.
        
        @description You can call the [GetFunctionCurrentVersion](https://help.aliyun.com/document_detail/421377.html) operation to query the latest version of a feature. The response of the operation includes the createParameters parameter that is used to create an algorithm instance, the usageParameters parameter, and the requirements for setting these parameters.
        
        @param request: CreateFunctionInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFunctionInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.create_parameters):
            body['createParameters'] = request.create_parameters
        if not UtilClient.is_unset(request.cron):
            body['cron'] = request.cron
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.function_type):
            body['functionType'] = request.function_type
        if not UtilClient.is_unset(request.instance_name):
            body['instanceName'] = request.instance_name
        if not UtilClient.is_unset(request.model_type):
            body['modelType'] = request.model_type
        if not UtilClient.is_unset(request.usage_parameters):
            body['usageParameters'] = request.usage_parameters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFunctionInstance',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateFunctionInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_function_instance(
        self,
        app_group_identity: str,
        function_name: str,
        request: open_search_20171225_models.CreateFunctionInstanceRequest,
    ) -> open_search_20171225_models.CreateFunctionInstanceResponse:
        """
        @summary Creates an algorithm instance of a feature.
        
        @description You can call the [GetFunctionCurrentVersion](https://help.aliyun.com/document_detail/421377.html) operation to query the latest version of a feature. The response of the operation includes the createParameters parameter that is used to create an algorithm instance, the usageParameters parameter, and the requirements for setting these parameters.
        
        @param request: CreateFunctionInstanceRequest
        @return: CreateFunctionInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_function_instance_with_options(app_group_identity, function_name, request, headers, runtime)

    async def create_function_instance_async(
        self,
        app_group_identity: str,
        function_name: str,
        request: open_search_20171225_models.CreateFunctionInstanceRequest,
    ) -> open_search_20171225_models.CreateFunctionInstanceResponse:
        """
        @summary Creates an algorithm instance of a feature.
        
        @description You can call the [GetFunctionCurrentVersion](https://help.aliyun.com/document_detail/421377.html) operation to query the latest version of a feature. The response of the operation includes the createParameters parameter that is used to create an algorithm instance, the usageParameters parameter, and the requirements for setting these parameters.
        
        @param request: CreateFunctionInstanceRequest
        @return: CreateFunctionInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_function_instance_with_options_async(app_group_identity, function_name, request, headers, runtime)

    def create_function_resource_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        request: open_search_20171225_models.CreateFunctionResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateFunctionResourceResponse:
        """
        @summary Creates an algorithm resource for a specific feature.
        
        @param request: CreateFunctionResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFunctionResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.resource_name):
            body['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFunctionResource',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/resources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateFunctionResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_function_resource_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        request: open_search_20171225_models.CreateFunctionResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateFunctionResourceResponse:
        """
        @summary Creates an algorithm resource for a specific feature.
        
        @param request: CreateFunctionResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFunctionResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.resource_name):
            body['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFunctionResource',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/resources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateFunctionResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_function_resource(
        self,
        app_group_identity: str,
        function_name: str,
        request: open_search_20171225_models.CreateFunctionResourceRequest,
    ) -> open_search_20171225_models.CreateFunctionResourceResponse:
        """
        @summary Creates an algorithm resource for a specific feature.
        
        @param request: CreateFunctionResourceRequest
        @return: CreateFunctionResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_function_resource_with_options(app_group_identity, function_name, request, headers, runtime)

    async def create_function_resource_async(
        self,
        app_group_identity: str,
        function_name: str,
        request: open_search_20171225_models.CreateFunctionResourceRequest,
    ) -> open_search_20171225_models.CreateFunctionResourceResponse:
        """
        @summary Creates an algorithm resource for a specific feature.
        
        @param request: CreateFunctionResourceRequest
        @return: CreateFunctionResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_function_resource_with_options_async(app_group_identity, function_name, request, headers, runtime)

    def create_function_task_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateFunctionTaskResponse:
        """
        @summary Starts a training task for an algorithm instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFunctionTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateFunctionTask',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/instances/{OpenApiUtilClient.get_encode_param(instance_name)}/tasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateFunctionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_function_task_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateFunctionTaskResponse:
        """
        @summary Starts a training task for an algorithm instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFunctionTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateFunctionTask',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/instances/{OpenApiUtilClient.get_encode_param(instance_name)}/tasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateFunctionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_function_task(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
    ) -> open_search_20171225_models.CreateFunctionTaskResponse:
        """
        @summary Starts a training task for an algorithm instance.
        
        @return: CreateFunctionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_function_task_with_options(app_group_identity, function_name, instance_name, headers, runtime)

    async def create_function_task_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
    ) -> open_search_20171225_models.CreateFunctionTaskResponse:
        """
        @summary Starts a training task for an algorithm instance.
        
        @return: CreateFunctionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_function_task_with_options_async(app_group_identity, function_name, instance_name, headers, runtime)

    def create_intervention_dictionary_with_options(
        self,
        request: open_search_20171225_models.CreateInterventionDictionaryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateInterventionDictionaryResponse:
        """
        @summary Create an intervention dictionary.
        
        @param request: CreateInterventionDictionaryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInterventionDictionaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.analyzer_type):
            body['analyzerType'] = request.analyzer_type
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInterventionDictionary',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/intervention-dictionaries',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateInterventionDictionaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_intervention_dictionary_with_options_async(
        self,
        request: open_search_20171225_models.CreateInterventionDictionaryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateInterventionDictionaryResponse:
        """
        @summary Create an intervention dictionary.
        
        @param request: CreateInterventionDictionaryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInterventionDictionaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.analyzer_type):
            body['analyzerType'] = request.analyzer_type
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInterventionDictionary',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/intervention-dictionaries',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateInterventionDictionaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_intervention_dictionary(
        self,
        request: open_search_20171225_models.CreateInterventionDictionaryRequest,
    ) -> open_search_20171225_models.CreateInterventionDictionaryResponse:
        """
        @summary Create an intervention dictionary.
        
        @param request: CreateInterventionDictionaryRequest
        @return: CreateInterventionDictionaryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_intervention_dictionary_with_options(request, headers, runtime)

    async def create_intervention_dictionary_async(
        self,
        request: open_search_20171225_models.CreateInterventionDictionaryRequest,
    ) -> open_search_20171225_models.CreateInterventionDictionaryResponse:
        """
        @summary Create an intervention dictionary.
        
        @param request: CreateInterventionDictionaryRequest
        @return: CreateInterventionDictionaryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_intervention_dictionary_with_options_async(request, headers, runtime)

    def create_query_processor_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.CreateQueryProcessorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateQueryProcessorResponse:
        """
        @summary Creates a query analysis rule. If you set dryRun to true, this operation checks the specified query analysis rule. By default, the value of dryRun is false if you do not set this parameter.
        
        @param request: CreateQueryProcessorRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQueryProcessorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateQueryProcessor',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/query-processors',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateQueryProcessorResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_query_processor_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.CreateQueryProcessorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateQueryProcessorResponse:
        """
        @summary Creates a query analysis rule. If you set dryRun to true, this operation checks the specified query analysis rule. By default, the value of dryRun is false if you do not set this parameter.
        
        @param request: CreateQueryProcessorRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQueryProcessorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateQueryProcessor',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/query-processors',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateQueryProcessorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_query_processor(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.CreateQueryProcessorRequest,
    ) -> open_search_20171225_models.CreateQueryProcessorResponse:
        """
        @summary Creates a query analysis rule. If you set dryRun to true, this operation checks the specified query analysis rule. By default, the value of dryRun is false if you do not set this parameter.
        
        @param request: CreateQueryProcessorRequest
        @return: CreateQueryProcessorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_query_processor_with_options(app_group_identity, app_id, request, headers, runtime)

    async def create_query_processor_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.CreateQueryProcessorRequest,
    ) -> open_search_20171225_models.CreateQueryProcessorResponse:
        """
        @summary Creates a query analysis rule. If you set dryRun to true, this operation checks the specified query analysis rule. By default, the value of dryRun is false if you do not set this parameter.
        
        @param request: CreateQueryProcessorRequest
        @return: CreateQueryProcessorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_query_processor_with_options_async(app_group_identity, app_id, request, headers, runtime)

    def create_scheduled_task_with_options(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.CreateScheduledTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateScheduledTaskResponse:
        """
        @param request: CreateScheduledTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScheduledTaskResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateScheduledTask',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scheduled-tasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scheduled_task_with_options_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.CreateScheduledTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateScheduledTaskResponse:
        """
        @param request: CreateScheduledTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScheduledTaskResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateScheduledTask',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scheduled-tasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateScheduledTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scheduled_task(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.CreateScheduledTaskRequest,
    ) -> open_search_20171225_models.CreateScheduledTaskResponse:
        """
        @param request: CreateScheduledTaskRequest
        @return: CreateScheduledTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_scheduled_task_with_options(app_group_identity, request, headers, runtime)

    async def create_scheduled_task_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.CreateScheduledTaskRequest,
    ) -> open_search_20171225_models.CreateScheduledTaskResponse:
        """
        @param request: CreateScheduledTaskRequest
        @return: CreateScheduledTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_scheduled_task_with_options_async(app_group_identity, request, headers, runtime)

    def create_search_strategy_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.CreateSearchStrategyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateSearchStrategyResponse:
        """
        @summary Creates a query policy.
        
        @param request: CreateSearchStrategyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSearchStrategyResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateSearchStrategy',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/search-strategies',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateSearchStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_search_strategy_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.CreateSearchStrategyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateSearchStrategyResponse:
        """
        @summary Creates a query policy.
        
        @param request: CreateSearchStrategyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSearchStrategyResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateSearchStrategy',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/search-strategies',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateSearchStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_search_strategy(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.CreateSearchStrategyRequest,
    ) -> open_search_20171225_models.CreateSearchStrategyResponse:
        """
        @summary Creates a query policy.
        
        @param request: CreateSearchStrategyRequest
        @return: CreateSearchStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_search_strategy_with_options(app_group_identity, app_id, request, headers, runtime)

    async def create_search_strategy_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.CreateSearchStrategyRequest,
    ) -> open_search_20171225_models.CreateSearchStrategyResponse:
        """
        @summary Creates a query policy.
        
        @param request: CreateSearchStrategyRequest
        @return: CreateSearchStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_search_strategy_with_options_async(app_group_identity, app_id, request, headers, runtime)

    def create_second_rank_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.CreateSecondRankRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateSecondRankResponse:
        """
        @summary Creates a fine sort expression for a version of an OpenSearch application. If you set dryRun to true, this operation checks the specified fine sort expression. The default value of dryRun is false if you do not set this parameter.
        
        @param request: CreateSecondRankRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSecondRankResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateSecondRank',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/second-ranks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateSecondRankResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_second_rank_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.CreateSecondRankRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateSecondRankResponse:
        """
        @summary Creates a fine sort expression for a version of an OpenSearch application. If you set dryRun to true, this operation checks the specified fine sort expression. The default value of dryRun is false if you do not set this parameter.
        
        @param request: CreateSecondRankRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSecondRankResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateSecondRank',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/second-ranks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateSecondRankResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_second_rank(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.CreateSecondRankRequest,
    ) -> open_search_20171225_models.CreateSecondRankResponse:
        """
        @summary Creates a fine sort expression for a version of an OpenSearch application. If you set dryRun to true, this operation checks the specified fine sort expression. The default value of dryRun is false if you do not set this parameter.
        
        @param request: CreateSecondRankRequest
        @return: CreateSecondRankResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_second_rank_with_options(app_group_identity, app_id, request, headers, runtime)

    async def create_second_rank_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.CreateSecondRankRequest,
    ) -> open_search_20171225_models.CreateSecondRankResponse:
        """
        @summary Creates a fine sort expression for a version of an OpenSearch application. If you set dryRun to true, this operation checks the specified fine sort expression. The default value of dryRun is false if you do not set this parameter.
        
        @param request: CreateSecondRankRequest
        @return: CreateSecondRankResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_second_rank_with_options_async(app_group_identity, app_id, request, headers, runtime)

    def create_sort_script_with_options(
        self,
        app_group_identity: str,
        app_version_id: str,
        request: open_search_20171225_models.CreateSortScriptRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateSortScriptResponse:
        """
        @summary Creates a sort script.
        
        @param request: CreateSortScriptRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSortScriptResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.script_name):
            body['scriptName'] = request.script_name
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSortScript',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_version_id)}/sort-scripts',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateSortScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sort_script_with_options_async(
        self,
        app_group_identity: str,
        app_version_id: str,
        request: open_search_20171225_models.CreateSortScriptRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateSortScriptResponse:
        """
        @summary Creates a sort script.
        
        @param request: CreateSortScriptRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSortScriptResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.script_name):
            body['scriptName'] = request.script_name
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSortScript',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_version_id)}/sort-scripts',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateSortScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sort_script(
        self,
        app_group_identity: str,
        app_version_id: str,
        request: open_search_20171225_models.CreateSortScriptRequest,
    ) -> open_search_20171225_models.CreateSortScriptResponse:
        """
        @summary Creates a sort script.
        
        @param request: CreateSortScriptRequest
        @return: CreateSortScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_sort_script_with_options(app_group_identity, app_version_id, request, headers, runtime)

    async def create_sort_script_async(
        self,
        app_group_identity: str,
        app_version_id: str,
        request: open_search_20171225_models.CreateSortScriptRequest,
    ) -> open_search_20171225_models.CreateSortScriptResponse:
        """
        @summary Creates a sort script.
        
        @param request: CreateSortScriptRequest
        @return: CreateSortScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_sort_script_with_options_async(app_group_identity, app_version_id, request, headers, runtime)

    def create_user_analyzer_with_options(
        self,
        request: open_search_20171225_models.CreateUserAnalyzerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateUserAnalyzerResponse:
        """
        @param request: CreateUserAnalyzerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserAnalyzerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.business):
            body['business'] = request.business
        if not UtilClient.is_unset(request.business_app_group_id):
            body['businessAppGroupId'] = request.business_app_group_id
        if not UtilClient.is_unset(request.business_type):
            body['businessType'] = request.business_type
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUserAnalyzer',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/user-analyzers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateUserAnalyzerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_analyzer_with_options_async(
        self,
        request: open_search_20171225_models.CreateUserAnalyzerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateUserAnalyzerResponse:
        """
        @param request: CreateUserAnalyzerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserAnalyzerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.business):
            body['business'] = request.business
        if not UtilClient.is_unset(request.business_app_group_id):
            body['businessAppGroupId'] = request.business_app_group_id
        if not UtilClient.is_unset(request.business_type):
            body['businessType'] = request.business_type
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUserAnalyzer',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/user-analyzers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateUserAnalyzerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_analyzer(
        self,
        request: open_search_20171225_models.CreateUserAnalyzerRequest,
    ) -> open_search_20171225_models.CreateUserAnalyzerResponse:
        """
        @param request: CreateUserAnalyzerRequest
        @return: CreateUserAnalyzerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_user_analyzer_with_options(request, headers, runtime)

    async def create_user_analyzer_async(
        self,
        request: open_search_20171225_models.CreateUserAnalyzerRequest,
    ) -> open_search_20171225_models.CreateUserAnalyzerResponse:
        """
        @param request: CreateUserAnalyzerRequest
        @return: CreateUserAnalyzerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_user_analyzer_with_options_async(request, headers, runtime)

    def delete_abtest_experiment_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DeleteABTestExperimentResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteABTestExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteABTestExperiment',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DeleteABTestExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_abtest_experiment_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DeleteABTestExperimentResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteABTestExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteABTestExperiment',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DeleteABTestExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_abtest_experiment(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
    ) -> open_search_20171225_models.DeleteABTestExperimentResponse:
        """
        @return: DeleteABTestExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_abtest_experiment_with_options(app_group_identity, scene_id, group_id, experiment_id, headers, runtime)

    async def delete_abtest_experiment_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
    ) -> open_search_20171225_models.DeleteABTestExperimentResponse:
        """
        @return: DeleteABTestExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_abtest_experiment_with_options_async(app_group_identity, scene_id, group_id, experiment_id, headers, runtime)

    def delete_abtest_group_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DeleteABTestGroupResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteABTestGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteABTestGroup',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DeleteABTestGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_abtest_group_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DeleteABTestGroupResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteABTestGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteABTestGroup',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DeleteABTestGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_abtest_group(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
    ) -> open_search_20171225_models.DeleteABTestGroupResponse:
        """
        @return: DeleteABTestGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_abtest_group_with_options(app_group_identity, scene_id, group_id, headers, runtime)

    async def delete_abtest_group_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
    ) -> open_search_20171225_models.DeleteABTestGroupResponse:
        """
        @return: DeleteABTestGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_abtest_group_with_options_async(app_group_identity, scene_id, group_id, headers, runtime)

    def delete_abtest_scene_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DeleteABTestSceneResponse:
        """
        @summary Deletes an A/B test scenario.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteABTestSceneResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteABTestScene',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DeleteABTestSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_abtest_scene_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DeleteABTestSceneResponse:
        """
        @summary Deletes an A/B test scenario.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteABTestSceneResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteABTestScene',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DeleteABTestSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_abtest_scene(
        self,
        app_group_identity: str,
        scene_id: str,
    ) -> open_search_20171225_models.DeleteABTestSceneResponse:
        """
        @summary Deletes an A/B test scenario.
        
        @return: DeleteABTestSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_abtest_scene_with_options(app_group_identity, scene_id, headers, runtime)

    async def delete_abtest_scene_async(
        self,
        app_group_identity: str,
        scene_id: str,
    ) -> open_search_20171225_models.DeleteABTestSceneResponse:
        """
        @summary Deletes an A/B test scenario.
        
        @return: DeleteABTestSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_abtest_scene_with_options_async(app_group_identity, scene_id, headers, runtime)

    def delete_function_instance_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DeleteFunctionInstanceResponse:
        """
        @summary Deletes an algorithm instance. Before you delete an instance, make sure that it is not in use to prevent service interruptions.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFunctionInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFunctionInstance',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/instances/{OpenApiUtilClient.get_encode_param(instance_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DeleteFunctionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_function_instance_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DeleteFunctionInstanceResponse:
        """
        @summary Deletes an algorithm instance. Before you delete an instance, make sure that it is not in use to prevent service interruptions.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFunctionInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFunctionInstance',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/instances/{OpenApiUtilClient.get_encode_param(instance_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DeleteFunctionInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_function_instance(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
    ) -> open_search_20171225_models.DeleteFunctionInstanceResponse:
        """
        @summary Deletes an algorithm instance. Before you delete an instance, make sure that it is not in use to prevent service interruptions.
        
        @return: DeleteFunctionInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_function_instance_with_options(app_group_identity, function_name, instance_name, headers, runtime)

    async def delete_function_instance_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
    ) -> open_search_20171225_models.DeleteFunctionInstanceResponse:
        """
        @summary Deletes an algorithm instance. Before you delete an instance, make sure that it is not in use to prevent service interruptions.
        
        @return: DeleteFunctionInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_function_instance_with_options_async(app_group_identity, function_name, instance_name, headers, runtime)

    def delete_function_resource_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        resource_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DeleteFunctionResourceResponse:
        """
        @summary Deletes an algorithm resource.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFunctionResourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFunctionResource',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/resources/{OpenApiUtilClient.get_encode_param(resource_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DeleteFunctionResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_function_resource_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        resource_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DeleteFunctionResourceResponse:
        """
        @summary Deletes an algorithm resource.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFunctionResourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFunctionResource',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/resources/{OpenApiUtilClient.get_encode_param(resource_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DeleteFunctionResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_function_resource(
        self,
        app_group_identity: str,
        function_name: str,
        resource_name: str,
    ) -> open_search_20171225_models.DeleteFunctionResourceResponse:
        """
        @summary Deletes an algorithm resource.
        
        @return: DeleteFunctionResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_function_resource_with_options(app_group_identity, function_name, resource_name, headers, runtime)

    async def delete_function_resource_async(
        self,
        app_group_identity: str,
        function_name: str,
        resource_name: str,
    ) -> open_search_20171225_models.DeleteFunctionResourceResponse:
        """
        @summary Deletes an algorithm resource.
        
        @return: DeleteFunctionResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_function_resource_with_options_async(app_group_identity, function_name, resource_name, headers, runtime)

    def delete_function_task_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        generation: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DeleteFunctionTaskResponse:
        """
        @summary Deletes a training task. The training task in progress cannot be deleted.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFunctionTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFunctionTask',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/instances/{OpenApiUtilClient.get_encode_param(instance_name)}/tasks/{OpenApiUtilClient.get_encode_param(generation)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DeleteFunctionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_function_task_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        generation: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DeleteFunctionTaskResponse:
        """
        @summary Deletes a training task. The training task in progress cannot be deleted.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFunctionTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFunctionTask',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/instances/{OpenApiUtilClient.get_encode_param(instance_name)}/tasks/{OpenApiUtilClient.get_encode_param(generation)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DeleteFunctionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_function_task(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        generation: str,
    ) -> open_search_20171225_models.DeleteFunctionTaskResponse:
        """
        @summary Deletes a training task. The training task in progress cannot be deleted.
        
        @return: DeleteFunctionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_function_task_with_options(app_group_identity, function_name, instance_name, generation, headers, runtime)

    async def delete_function_task_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        generation: str,
    ) -> open_search_20171225_models.DeleteFunctionTaskResponse:
        """
        @summary Deletes a training task. The training task in progress cannot be deleted.
        
        @return: DeleteFunctionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_function_task_with_options_async(app_group_identity, function_name, instance_name, generation, headers, runtime)

    def delete_sort_script_with_options(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DeleteSortScriptResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSortScriptResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSortScript',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_version_id)}/sort-scripts/{OpenApiUtilClient.get_encode_param(script_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DeleteSortScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sort_script_with_options_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DeleteSortScriptResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSortScriptResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSortScript',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_version_id)}/sort-scripts/{OpenApiUtilClient.get_encode_param(script_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DeleteSortScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sort_script(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
    ) -> open_search_20171225_models.DeleteSortScriptResponse:
        """
        @return: DeleteSortScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_sort_script_with_options(app_group_identity, script_name, app_version_id, headers, runtime)

    async def delete_sort_script_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
    ) -> open_search_20171225_models.DeleteSortScriptResponse:
        """
        @return: DeleteSortScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_sort_script_with_options_async(app_group_identity, script_name, app_version_id, headers, runtime)

    def delete_sort_script_file_with_options(
        self,
        app_group_identity: str,
        app_version_id: str,
        script_name: str,
        file_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DeleteSortScriptFileResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSortScriptFileResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSortScriptFile',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_version_id)}/sort-scripts/{OpenApiUtilClient.get_encode_param(script_name)}/files/src/{OpenApiUtilClient.get_encode_param(file_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DeleteSortScriptFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sort_script_file_with_options_async(
        self,
        app_group_identity: str,
        app_version_id: str,
        script_name: str,
        file_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DeleteSortScriptFileResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSortScriptFileResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSortScriptFile',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_version_id)}/sort-scripts/{OpenApiUtilClient.get_encode_param(script_name)}/files/src/{OpenApiUtilClient.get_encode_param(file_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DeleteSortScriptFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sort_script_file(
        self,
        app_group_identity: str,
        app_version_id: str,
        script_name: str,
        file_name: str,
    ) -> open_search_20171225_models.DeleteSortScriptFileResponse:
        """
        @return: DeleteSortScriptFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_sort_script_file_with_options(app_group_identity, app_version_id, script_name, file_name, headers, runtime)

    async def delete_sort_script_file_async(
        self,
        app_group_identity: str,
        app_version_id: str,
        script_name: str,
        file_name: str,
    ) -> open_search_20171225_models.DeleteSortScriptFileResponse:
        """
        @return: DeleteSortScriptFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_sort_script_file_with_options_async(app_group_identity, app_version_id, script_name, file_name, headers, runtime)

    def describe_abtest_experiment_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeABTestExperimentResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeABTestExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeABTestExperiment',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeABTestExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_abtest_experiment_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeABTestExperimentResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeABTestExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeABTestExperiment',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeABTestExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_abtest_experiment(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
    ) -> open_search_20171225_models.DescribeABTestExperimentResponse:
        """
        @return: DescribeABTestExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_abtest_experiment_with_options(app_group_identity, scene_id, group_id, experiment_id, headers, runtime)

    async def describe_abtest_experiment_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
    ) -> open_search_20171225_models.DescribeABTestExperimentResponse:
        """
        @return: DescribeABTestExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_abtest_experiment_with_options_async(app_group_identity, scene_id, group_id, experiment_id, headers, runtime)

    def describe_abtest_group_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeABTestGroupResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeABTestGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeABTestGroup',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeABTestGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_abtest_group_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeABTestGroupResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeABTestGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeABTestGroup',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeABTestGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_abtest_group(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
    ) -> open_search_20171225_models.DescribeABTestGroupResponse:
        """
        @return: DescribeABTestGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_abtest_group_with_options(app_group_identity, scene_id, group_id, headers, runtime)

    async def describe_abtest_group_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
    ) -> open_search_20171225_models.DescribeABTestGroupResponse:
        """
        @return: DescribeABTestGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_abtest_group_with_options_async(app_group_identity, scene_id, group_id, headers, runtime)

    def describe_abtest_scene_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeABTestSceneResponse:
        """
        @summary Queries the information about an A/B test scenario.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeABTestSceneResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeABTestScene',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeABTestSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_abtest_scene_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeABTestSceneResponse:
        """
        @summary Queries the information about an A/B test scenario.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeABTestSceneResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeABTestScene',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeABTestSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_abtest_scene(
        self,
        app_group_identity: str,
        scene_id: str,
    ) -> open_search_20171225_models.DescribeABTestSceneResponse:
        """
        @summary Queries the information about an A/B test scenario.
        
        @return: DescribeABTestSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_abtest_scene_with_options(app_group_identity, scene_id, headers, runtime)

    async def describe_abtest_scene_async(
        self,
        app_group_identity: str,
        scene_id: str,
    ) -> open_search_20171225_models.DescribeABTestSceneResponse:
        """
        @summary Queries the information about an A/B test scenario.
        
        @return: DescribeABTestSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_abtest_scene_with_options_async(app_group_identity, scene_id, headers, runtime)

    def describe_app_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeAppResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeApp',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeAppResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeApp',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> open_search_20171225_models.DescribeAppResponse:
        """
        @return: DescribeAppResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_app_with_options(app_group_identity, app_id, headers, runtime)

    async def describe_app_async(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> open_search_20171225_models.DescribeAppResponse:
        """
        @return: DescribeAppResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_app_with_options_async(app_group_identity, app_id, headers, runtime)

    def describe_app_group_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeAppGroupResponse:
        """
        @summary Queries the details of an OpenSearch application.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeAppGroup',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_group_with_options_async(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeAppGroupResponse:
        """
        @summary Queries the details of an OpenSearch application.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeAppGroup',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeAppGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_group(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.DescribeAppGroupResponse:
        """
        @summary Queries the details of an OpenSearch application.
        
        @return: DescribeAppGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_app_group_with_options(app_group_identity, headers, runtime)

    async def describe_app_group_async(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.DescribeAppGroupResponse:
        """
        @summary Queries the details of an OpenSearch application.
        
        @return: DescribeAppGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_app_group_with_options_async(app_group_identity, headers, runtime)

    def describe_app_statistics_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeAppStatisticsResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppStatisticsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeAppStatistics',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/statistics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeAppStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_statistics_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeAppStatisticsResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppStatisticsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeAppStatistics',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/statistics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeAppStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_statistics(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> open_search_20171225_models.DescribeAppStatisticsResponse:
        """
        @return: DescribeAppStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_app_statistics_with_options(app_group_identity, app_id, headers, runtime)

    async def describe_app_statistics_async(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> open_search_20171225_models.DescribeAppStatisticsResponse:
        """
        @return: DescribeAppStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_app_statistics_with_options_async(app_group_identity, app_id, headers, runtime)

    def describe_apps_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeAppsResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeApps',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apps_with_options_async(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeAppsResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeApps',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apps(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.DescribeAppsResponse:
        """
        @return: DescribeAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_apps_with_options(app_group_identity, headers, runtime)

    async def describe_apps_async(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.DescribeAppsResponse:
        """
        @return: DescribeAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_apps_with_options_async(app_group_identity, headers, runtime)

    def describe_data_collction_with_options(
        self,
        app_group_identity: str,
        data_collection_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeDataCollctionResponse:
        """
        @summary Queries the details of a data collection task of an application.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataCollctionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeDataCollction',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/data-collections/{OpenApiUtilClient.get_encode_param(data_collection_identity)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeDataCollctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_collction_with_options_async(
        self,
        app_group_identity: str,
        data_collection_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeDataCollctionResponse:
        """
        @summary Queries the details of a data collection task of an application.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataCollctionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeDataCollction',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/data-collections/{OpenApiUtilClient.get_encode_param(data_collection_identity)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeDataCollctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_collction(
        self,
        app_group_identity: str,
        data_collection_identity: str,
    ) -> open_search_20171225_models.DescribeDataCollctionResponse:
        """
        @summary Queries the details of a data collection task of an application.
        
        @return: DescribeDataCollctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_data_collction_with_options(app_group_identity, data_collection_identity, headers, runtime)

    async def describe_data_collction_async(
        self,
        app_group_identity: str,
        data_collection_identity: str,
    ) -> open_search_20171225_models.DescribeDataCollctionResponse:
        """
        @summary Queries the details of a data collection task of an application.
        
        @return: DescribeDataCollctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_data_collction_with_options_async(app_group_identity, data_collection_identity, headers, runtime)

    def describe_first_rank_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeFirstRankResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFirstRankResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeFirstRank',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/first-ranks/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeFirstRankResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_first_rank_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeFirstRankResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFirstRankResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeFirstRank',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/first-ranks/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeFirstRankResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_first_rank(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> open_search_20171225_models.DescribeFirstRankResponse:
        """
        @return: DescribeFirstRankResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_first_rank_with_options(app_group_identity, app_id, name, headers, runtime)

    async def describe_first_rank_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> open_search_20171225_models.DescribeFirstRankResponse:
        """
        @return: DescribeFirstRankResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_first_rank_with_options_async(app_group_identity, app_id, name, headers, runtime)

    def describe_intervention_dictionary_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeInterventionDictionaryResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInterventionDictionaryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeInterventionDictionary',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/intervention-dictionaries/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeInterventionDictionaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_intervention_dictionary_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeInterventionDictionaryResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInterventionDictionaryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeInterventionDictionary',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/intervention-dictionaries/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeInterventionDictionaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_intervention_dictionary(
        self,
        name: str,
    ) -> open_search_20171225_models.DescribeInterventionDictionaryResponse:
        """
        @return: DescribeInterventionDictionaryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_intervention_dictionary_with_options(name, headers, runtime)

    async def describe_intervention_dictionary_async(
        self,
        name: str,
    ) -> open_search_20171225_models.DescribeInterventionDictionaryResponse:
        """
        @return: DescribeInterventionDictionaryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_intervention_dictionary_with_options_async(name, headers, runtime)

    def describe_query_processor_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeQueryProcessorResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeQueryProcessorResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeQueryProcessor',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/query-processors/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeQueryProcessorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_query_processor_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeQueryProcessorResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeQueryProcessorResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeQueryProcessor',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/query-processors/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeQueryProcessorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_query_processor(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> open_search_20171225_models.DescribeQueryProcessorResponse:
        """
        @return: DescribeQueryProcessorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_query_processor_with_options(app_group_identity, app_id, name, headers, runtime)

    async def describe_query_processor_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> open_search_20171225_models.DescribeQueryProcessorResponse:
        """
        @return: DescribeQueryProcessorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_query_processor_with_options_async(app_group_identity, app_id, name, headers, runtime)

    def describe_regions_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeRegionsResponse:
        """
        @summary Queries the endpoints of all regions that support OpenSearch.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeRegionsResponse:
        """
        @summary Queries the endpoints of all regions that support OpenSearch.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(self) -> open_search_20171225_models.DescribeRegionsResponse:
        """
        @summary Queries the endpoints of all regions that support OpenSearch.
        
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(headers, runtime)

    async def describe_regions_async(self) -> open_search_20171225_models.DescribeRegionsResponse:
        """
        @summary Queries the endpoints of all regions that support OpenSearch.
        
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_regions_with_options_async(headers, runtime)

    def describe_scheduled_task_with_options(
        self,
        app_group_identity: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeScheduledTaskResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScheduledTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeScheduledTask',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scheduled-tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scheduled_task_with_options_async(
        self,
        app_group_identity: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeScheduledTaskResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScheduledTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeScheduledTask',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scheduled-tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeScheduledTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scheduled_task(
        self,
        app_group_identity: str,
        task_id: str,
    ) -> open_search_20171225_models.DescribeScheduledTaskResponse:
        """
        @return: DescribeScheduledTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_scheduled_task_with_options(app_group_identity, task_id, headers, runtime)

    async def describe_scheduled_task_async(
        self,
        app_group_identity: str,
        task_id: str,
    ) -> open_search_20171225_models.DescribeScheduledTaskResponse:
        """
        @return: DescribeScheduledTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_scheduled_task_with_options_async(app_group_identity, task_id, headers, runtime)

    def describe_second_rank_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeSecondRankResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSecondRankResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeSecondRank',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/second-ranks/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeSecondRankResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_second_rank_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeSecondRankResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSecondRankResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeSecondRank',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/second-ranks/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeSecondRankResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_second_rank(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> open_search_20171225_models.DescribeSecondRankResponse:
        """
        @return: DescribeSecondRankResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_second_rank_with_options(app_group_identity, app_id, name, headers, runtime)

    async def describe_second_rank_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> open_search_20171225_models.DescribeSecondRankResponse:
        """
        @return: DescribeSecondRankResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_second_rank_with_options_async(app_group_identity, app_id, name, headers, runtime)

    def describe_slow_query_status_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeSlowQueryStatusResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowQueryStatusResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeSlowQueryStatus',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/optimizers/slow-query',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeSlowQueryStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_query_status_with_options_async(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeSlowQueryStatusResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowQueryStatusResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeSlowQueryStatus',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/optimizers/slow-query',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeSlowQueryStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slow_query_status(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.DescribeSlowQueryStatusResponse:
        """
        @return: DescribeSlowQueryStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_slow_query_status_with_options(app_group_identity, headers, runtime)

    async def describe_slow_query_status_async(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.DescribeSlowQueryStatusResponse:
        """
        @return: DescribeSlowQueryStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_slow_query_status_with_options_async(app_group_identity, headers, runtime)

    def describe_user_analyzer_with_options(
        self,
        name: str,
        request: open_search_20171225_models.DescribeUserAnalyzerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeUserAnalyzerResponse:
        """
        @param request: DescribeUserAnalyzerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserAnalyzerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.with_):
            query['with'] = request.with_
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserAnalyzer',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/user-analyzers/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeUserAnalyzerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_analyzer_with_options_async(
        self,
        name: str,
        request: open_search_20171225_models.DescribeUserAnalyzerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeUserAnalyzerResponse:
        """
        @param request: DescribeUserAnalyzerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserAnalyzerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.with_):
            query['with'] = request.with_
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserAnalyzer',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/user-analyzers/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeUserAnalyzerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_analyzer(
        self,
        name: str,
        request: open_search_20171225_models.DescribeUserAnalyzerRequest,
    ) -> open_search_20171225_models.DescribeUserAnalyzerResponse:
        """
        @param request: DescribeUserAnalyzerRequest
        @return: DescribeUserAnalyzerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_user_analyzer_with_options(name, request, headers, runtime)

    async def describe_user_analyzer_async(
        self,
        name: str,
        request: open_search_20171225_models.DescribeUserAnalyzerRequest,
    ) -> open_search_20171225_models.DescribeUserAnalyzerResponse:
        """
        @param request: DescribeUserAnalyzerRequest
        @return: DescribeUserAnalyzerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_user_analyzer_with_options_async(name, request, headers, runtime)

    def disable_slow_query_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DisableSlowQueryResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableSlowQueryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DisableSlowQuery',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/optimizers/slow-query/actions/disable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DisableSlowQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_slow_query_with_options_async(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DisableSlowQueryResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableSlowQueryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DisableSlowQuery',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/optimizers/slow-query/actions/disable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DisableSlowQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_slow_query(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.DisableSlowQueryResponse:
        """
        @return: DisableSlowQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.disable_slow_query_with_options(app_group_identity, headers, runtime)

    async def disable_slow_query_async(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.DisableSlowQueryResponse:
        """
        @return: DisableSlowQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.disable_slow_query_with_options_async(app_group_identity, headers, runtime)

    def enable_slow_query_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.EnableSlowQueryResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableSlowQueryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='EnableSlowQuery',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/optimizers/slow-query/actions/enable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.EnableSlowQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_slow_query_with_options_async(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.EnableSlowQueryResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableSlowQueryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='EnableSlowQuery',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/optimizers/slow-query/actions/enable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.EnableSlowQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_slow_query(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.EnableSlowQueryResponse:
        """
        @return: EnableSlowQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_slow_query_with_options(app_group_identity, headers, runtime)

    async def enable_slow_query_async(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.EnableSlowQueryResponse:
        """
        @return: EnableSlowQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.enable_slow_query_with_options_async(app_group_identity, headers, runtime)

    def generate_merged_table_with_options(
        self,
        request: open_search_20171225_models.GenerateMergedTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GenerateMergedTableResponse:
        """
        @summary Queries the information about a wide table that is generated after a JOIN operation is performed on multiple tables.
        
        @param request: GenerateMergedTableRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateMergedTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.spec):
            query['spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='GenerateMergedTable',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/assist/schema/actions/merge',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GenerateMergedTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_merged_table_with_options_async(
        self,
        request: open_search_20171225_models.GenerateMergedTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GenerateMergedTableResponse:
        """
        @summary Queries the information about a wide table that is generated after a JOIN operation is performed on multiple tables.
        
        @param request: GenerateMergedTableRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateMergedTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.spec):
            query['spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='GenerateMergedTable',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/assist/schema/actions/merge',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GenerateMergedTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_merged_table(
        self,
        request: open_search_20171225_models.GenerateMergedTableRequest,
    ) -> open_search_20171225_models.GenerateMergedTableResponse:
        """
        @summary Queries the information about a wide table that is generated after a JOIN operation is performed on multiple tables.
        
        @param request: GenerateMergedTableRequest
        @return: GenerateMergedTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_merged_table_with_options(request, headers, runtime)

    async def generate_merged_table_async(
        self,
        request: open_search_20171225_models.GenerateMergedTableRequest,
    ) -> open_search_20171225_models.GenerateMergedTableResponse:
        """
        @summary Queries the information about a wide table that is generated after a JOIN operation is performed on multiple tables.
        
        @param request: GenerateMergedTableRequest
        @return: GenerateMergedTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.generate_merged_table_with_options_async(request, headers, runtime)

    def get_domain_with_options(
        self,
        domain_name: str,
        request: open_search_20171225_models.GetDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetDomainResponse:
        """
        @summary Queries the type of an industry.
        
        @param request: GetDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_group_identity):
            query['appGroupIdentity'] = request.app_group_identity
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomain',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/domains/{OpenApiUtilClient.get_encode_param(domain_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_domain_with_options_async(
        self,
        domain_name: str,
        request: open_search_20171225_models.GetDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetDomainResponse:
        """
        @summary Queries the type of an industry.
        
        @param request: GetDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_group_identity):
            query['appGroupIdentity'] = request.app_group_identity
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomain',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/domains/{OpenApiUtilClient.get_encode_param(domain_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_domain(
        self,
        domain_name: str,
        request: open_search_20171225_models.GetDomainRequest,
    ) -> open_search_20171225_models.GetDomainResponse:
        """
        @summary Queries the type of an industry.
        
        @param request: GetDomainRequest
        @return: GetDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_domain_with_options(domain_name, request, headers, runtime)

    async def get_domain_async(
        self,
        domain_name: str,
        request: open_search_20171225_models.GetDomainRequest,
    ) -> open_search_20171225_models.GetDomainResponse:
        """
        @summary Queries the type of an industry.
        
        @param request: GetDomainRequest
        @return: GetDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_domain_with_options_async(domain_name, request, headers, runtime)

    def get_function_current_version_with_options(
        self,
        function_name: str,
        request: open_search_20171225_models.GetFunctionCurrentVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetFunctionCurrentVersionResponse:
        """
        @summary Queries the version information about the current feature when you create an instance.
        
        @param request: GetFunctionCurrentVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFunctionCurrentVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.domain):
            query['domain'] = request.domain
        if not UtilClient.is_unset(request.function_type):
            query['functionType'] = request.function_type
        if not UtilClient.is_unset(request.model_type):
            query['modelType'] = request.model_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFunctionCurrentVersion',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/functions/{OpenApiUtilClient.get_encode_param(function_name)}/current-version',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetFunctionCurrentVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_function_current_version_with_options_async(
        self,
        function_name: str,
        request: open_search_20171225_models.GetFunctionCurrentVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetFunctionCurrentVersionResponse:
        """
        @summary Queries the version information about the current feature when you create an instance.
        
        @param request: GetFunctionCurrentVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFunctionCurrentVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.domain):
            query['domain'] = request.domain
        if not UtilClient.is_unset(request.function_type):
            query['functionType'] = request.function_type
        if not UtilClient.is_unset(request.model_type):
            query['modelType'] = request.model_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFunctionCurrentVersion',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/functions/{OpenApiUtilClient.get_encode_param(function_name)}/current-version',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetFunctionCurrentVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_function_current_version(
        self,
        function_name: str,
        request: open_search_20171225_models.GetFunctionCurrentVersionRequest,
    ) -> open_search_20171225_models.GetFunctionCurrentVersionResponse:
        """
        @summary Queries the version information about the current feature when you create an instance.
        
        @param request: GetFunctionCurrentVersionRequest
        @return: GetFunctionCurrentVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_function_current_version_with_options(function_name, request, headers, runtime)

    async def get_function_current_version_async(
        self,
        function_name: str,
        request: open_search_20171225_models.GetFunctionCurrentVersionRequest,
    ) -> open_search_20171225_models.GetFunctionCurrentVersionResponse:
        """
        @summary Queries the version information about the current feature when you create an instance.
        
        @param request: GetFunctionCurrentVersionRequest
        @return: GetFunctionCurrentVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_function_current_version_with_options_async(function_name, request, headers, runtime)

    def get_function_default_instance_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetFunctionDefaultInstanceResponse:
        """
        @summary Queries the algorithm instance that an application uses by default.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFunctionDefaultInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFunctionDefaultInstance',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/default-instance',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetFunctionDefaultInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_function_default_instance_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetFunctionDefaultInstanceResponse:
        """
        @summary Queries the algorithm instance that an application uses by default.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFunctionDefaultInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFunctionDefaultInstance',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/default-instance',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetFunctionDefaultInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_function_default_instance(
        self,
        app_group_identity: str,
        function_name: str,
    ) -> open_search_20171225_models.GetFunctionDefaultInstanceResponse:
        """
        @summary Queries the algorithm instance that an application uses by default.
        
        @return: GetFunctionDefaultInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_function_default_instance_with_options(app_group_identity, function_name, headers, runtime)

    async def get_function_default_instance_async(
        self,
        app_group_identity: str,
        function_name: str,
    ) -> open_search_20171225_models.GetFunctionDefaultInstanceResponse:
        """
        @summary Queries the algorithm instance that an application uses by default.
        
        @return: GetFunctionDefaultInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_function_default_instance_with_options_async(app_group_identity, function_name, headers, runtime)

    def get_function_instance_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        request: open_search_20171225_models.GetFunctionInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetFunctionInstanceResponse:
        """
        @summary Queries the details of an algorithm instance by instance name.
        
        @param request: GetFunctionInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFunctionInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output):
            query['output'] = request.output
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFunctionInstance',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/instances/{OpenApiUtilClient.get_encode_param(instance_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetFunctionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_function_instance_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        request: open_search_20171225_models.GetFunctionInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetFunctionInstanceResponse:
        """
        @summary Queries the details of an algorithm instance by instance name.
        
        @param request: GetFunctionInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFunctionInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output):
            query['output'] = request.output
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFunctionInstance',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/instances/{OpenApiUtilClient.get_encode_param(instance_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetFunctionInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_function_instance(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        request: open_search_20171225_models.GetFunctionInstanceRequest,
    ) -> open_search_20171225_models.GetFunctionInstanceResponse:
        """
        @summary Queries the details of an algorithm instance by instance name.
        
        @param request: GetFunctionInstanceRequest
        @return: GetFunctionInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_function_instance_with_options(app_group_identity, function_name, instance_name, request, headers, runtime)

    async def get_function_instance_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        request: open_search_20171225_models.GetFunctionInstanceRequest,
    ) -> open_search_20171225_models.GetFunctionInstanceResponse:
        """
        @summary Queries the details of an algorithm instance by instance name.
        
        @param request: GetFunctionInstanceRequest
        @return: GetFunctionInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_function_instance_with_options_async(app_group_identity, function_name, instance_name, request, headers, runtime)

    def get_function_resource_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        resource_name: str,
        request: open_search_20171225_models.GetFunctionResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetFunctionResourceResponse:
        """
        @summary Queries an algorithm resource.
        
        @param request: GetFunctionResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFunctionResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output):
            query['output'] = request.output
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFunctionResource',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/resources/{OpenApiUtilClient.get_encode_param(resource_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetFunctionResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_function_resource_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        resource_name: str,
        request: open_search_20171225_models.GetFunctionResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetFunctionResourceResponse:
        """
        @summary Queries an algorithm resource.
        
        @param request: GetFunctionResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFunctionResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output):
            query['output'] = request.output
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFunctionResource',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/resources/{OpenApiUtilClient.get_encode_param(resource_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetFunctionResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_function_resource(
        self,
        app_group_identity: str,
        function_name: str,
        resource_name: str,
        request: open_search_20171225_models.GetFunctionResourceRequest,
    ) -> open_search_20171225_models.GetFunctionResourceResponse:
        """
        @summary Queries an algorithm resource.
        
        @param request: GetFunctionResourceRequest
        @return: GetFunctionResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_function_resource_with_options(app_group_identity, function_name, resource_name, request, headers, runtime)

    async def get_function_resource_async(
        self,
        app_group_identity: str,
        function_name: str,
        resource_name: str,
        request: open_search_20171225_models.GetFunctionResourceRequest,
    ) -> open_search_20171225_models.GetFunctionResourceResponse:
        """
        @summary Queries an algorithm resource.
        
        @param request: GetFunctionResourceRequest
        @return: GetFunctionResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_function_resource_with_options_async(app_group_identity, function_name, resource_name, request, headers, runtime)

    def get_function_task_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        generation: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetFunctionTaskResponse:
        """
        @summary Queries the details of a training task.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFunctionTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFunctionTask',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/instances/{OpenApiUtilClient.get_encode_param(instance_name)}/tasks/{OpenApiUtilClient.get_encode_param(generation)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetFunctionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_function_task_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        generation: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetFunctionTaskResponse:
        """
        @summary Queries the details of a training task.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFunctionTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFunctionTask',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/instances/{OpenApiUtilClient.get_encode_param(instance_name)}/tasks/{OpenApiUtilClient.get_encode_param(generation)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetFunctionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_function_task(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        generation: str,
    ) -> open_search_20171225_models.GetFunctionTaskResponse:
        """
        @summary Queries the details of a training task.
        
        @return: GetFunctionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_function_task_with_options(app_group_identity, function_name, instance_name, generation, headers, runtime)

    async def get_function_task_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        generation: str,
    ) -> open_search_20171225_models.GetFunctionTaskResponse:
        """
        @summary Queries the details of a training task.
        
        @return: GetFunctionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_function_task_with_options_async(app_group_identity, function_name, instance_name, generation, headers, runtime)

    def get_function_version_with_options(
        self,
        function_name: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetFunctionVersionResponse:
        """
        @summary Queries version information by version ID.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFunctionVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFunctionVersion',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/functions/{OpenApiUtilClient.get_encode_param(function_name)}/versions/{OpenApiUtilClient.get_encode_param(version_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetFunctionVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_function_version_with_options_async(
        self,
        function_name: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetFunctionVersionResponse:
        """
        @summary Queries version information by version ID.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFunctionVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFunctionVersion',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/functions/{OpenApiUtilClient.get_encode_param(function_name)}/versions/{OpenApiUtilClient.get_encode_param(version_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetFunctionVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_function_version(
        self,
        function_name: str,
        version_id: str,
    ) -> open_search_20171225_models.GetFunctionVersionResponse:
        """
        @summary Queries version information by version ID.
        
        @return: GetFunctionVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_function_version_with_options(function_name, version_id, headers, runtime)

    async def get_function_version_async(
        self,
        function_name: str,
        version_id: str,
    ) -> open_search_20171225_models.GetFunctionVersionResponse:
        """
        @summary Queries version information by version ID.
        
        @return: GetFunctionVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_function_version_with_options_async(function_name, version_id, headers, runtime)

    def get_script_file_names_with_options(
        self,
        app_group_identity: str,
        app_version_id: str,
        script_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetScriptFileNamesResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetScriptFileNamesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetScriptFileNames',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_version_id)}/sort-scripts/{OpenApiUtilClient.get_encode_param(script_name)}/file-names',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetScriptFileNamesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_script_file_names_with_options_async(
        self,
        app_group_identity: str,
        app_version_id: str,
        script_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetScriptFileNamesResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetScriptFileNamesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetScriptFileNames',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_version_id)}/sort-scripts/{OpenApiUtilClient.get_encode_param(script_name)}/file-names',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetScriptFileNamesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_script_file_names(
        self,
        app_group_identity: str,
        app_version_id: str,
        script_name: str,
    ) -> open_search_20171225_models.GetScriptFileNamesResponse:
        """
        @return: GetScriptFileNamesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_script_file_names_with_options(app_group_identity, app_version_id, script_name, headers, runtime)

    async def get_script_file_names_async(
        self,
        app_group_identity: str,
        app_version_id: str,
        script_name: str,
    ) -> open_search_20171225_models.GetScriptFileNamesResponse:
        """
        @return: GetScriptFileNamesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_script_file_names_with_options_async(app_group_identity, app_version_id, script_name, headers, runtime)

    def get_search_strategy_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        strategy_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetSearchStrategyResponse:
        """
        @summary Queries the details of a query policy.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSearchStrategyResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSearchStrategy',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/search-strategies/{OpenApiUtilClient.get_encode_param(strategy_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetSearchStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_search_strategy_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        strategy_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetSearchStrategyResponse:
        """
        @summary Queries the details of a query policy.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSearchStrategyResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSearchStrategy',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/search-strategies/{OpenApiUtilClient.get_encode_param(strategy_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetSearchStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_search_strategy(
        self,
        app_group_identity: str,
        app_id: str,
        strategy_name: str,
    ) -> open_search_20171225_models.GetSearchStrategyResponse:
        """
        @summary Queries the details of a query policy.
        
        @return: GetSearchStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_search_strategy_with_options(app_group_identity, app_id, strategy_name, headers, runtime)

    async def get_search_strategy_async(
        self,
        app_group_identity: str,
        app_id: str,
        strategy_name: str,
    ) -> open_search_20171225_models.GetSearchStrategyResponse:
        """
        @summary Queries the details of a query policy.
        
        @return: GetSearchStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_search_strategy_with_options_async(app_group_identity, app_id, strategy_name, headers, runtime)

    def get_sort_script_with_options(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetSortScriptResponse:
        """
        @summary Queries the details of a sort script.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSortScriptResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSortScript',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_version_id)}/sort-scripts/{OpenApiUtilClient.get_encode_param(script_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetSortScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sort_script_with_options_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetSortScriptResponse:
        """
        @summary Queries the details of a sort script.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSortScriptResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSortScript',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_version_id)}/sort-scripts/{OpenApiUtilClient.get_encode_param(script_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetSortScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sort_script(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
    ) -> open_search_20171225_models.GetSortScriptResponse:
        """
        @summary Queries the details of a sort script.
        
        @return: GetSortScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_sort_script_with_options(app_group_identity, script_name, app_version_id, headers, runtime)

    async def get_sort_script_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
    ) -> open_search_20171225_models.GetSortScriptResponse:
        """
        @summary Queries the details of a sort script.
        
        @return: GetSortScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_sort_script_with_options_async(app_group_identity, script_name, app_version_id, headers, runtime)

    def get_sort_script_file_with_options(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        file_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetSortScriptFileResponse:
        """
        @summary Queries the content of a sort script.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSortScriptFileResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSortScriptFile',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_version_id)}/sort-scripts/{OpenApiUtilClient.get_encode_param(script_name)}/files/src/{OpenApiUtilClient.get_encode_param(file_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetSortScriptFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sort_script_file_with_options_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        file_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetSortScriptFileResponse:
        """
        @summary Queries the content of a sort script.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSortScriptFileResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSortScriptFile',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_version_id)}/sort-scripts/{OpenApiUtilClient.get_encode_param(script_name)}/files/src/{OpenApiUtilClient.get_encode_param(file_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetSortScriptFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sort_script_file(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        file_name: str,
    ) -> open_search_20171225_models.GetSortScriptFileResponse:
        """
        @summary Queries the content of a sort script.
        
        @return: GetSortScriptFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_sort_script_file_with_options(app_group_identity, script_name, app_version_id, file_name, headers, runtime)

    async def get_sort_script_file_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        file_name: str,
    ) -> open_search_20171225_models.GetSortScriptFileResponse:
        """
        @summary Queries the content of a sort script.
        
        @return: GetSortScriptFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_sort_script_file_with_options_async(app_group_identity, script_name, app_version_id, file_name, headers, runtime)

    def list_abtest_experiments_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListABTestExperimentsResponse:
        """
        @summary Queries a list of experiments.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListABTestExperimentsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListABTestExperiments',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}/experiments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListABTestExperimentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_abtest_experiments_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListABTestExperimentsResponse:
        """
        @summary Queries a list of experiments.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListABTestExperimentsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListABTestExperiments',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}/experiments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListABTestExperimentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_abtest_experiments(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
    ) -> open_search_20171225_models.ListABTestExperimentsResponse:
        """
        @summary Queries a list of experiments.
        
        @return: ListABTestExperimentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_abtest_experiments_with_options(app_group_identity, scene_id, group_id, headers, runtime)

    async def list_abtest_experiments_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
    ) -> open_search_20171225_models.ListABTestExperimentsResponse:
        """
        @summary Queries a list of experiments.
        
        @return: ListABTestExperimentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_abtest_experiments_with_options_async(app_group_identity, scene_id, group_id, headers, runtime)

    def list_abtest_fixed_flow_dividers_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListABTestFixedFlowDividersResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListABTestFixedFlowDividersResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListABTestFixedFlowDividers',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}/fixed-flow-dividers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListABTestFixedFlowDividersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_abtest_fixed_flow_dividers_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListABTestFixedFlowDividersResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListABTestFixedFlowDividersResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListABTestFixedFlowDividers',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}/fixed-flow-dividers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListABTestFixedFlowDividersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_abtest_fixed_flow_dividers(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
    ) -> open_search_20171225_models.ListABTestFixedFlowDividersResponse:
        """
        @return: ListABTestFixedFlowDividersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_abtest_fixed_flow_dividers_with_options(app_group_identity, scene_id, group_id, experiment_id, headers, runtime)

    async def list_abtest_fixed_flow_dividers_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
    ) -> open_search_20171225_models.ListABTestFixedFlowDividersResponse:
        """
        @return: ListABTestFixedFlowDividersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_abtest_fixed_flow_dividers_with_options_async(app_group_identity, scene_id, group_id, experiment_id, headers, runtime)

    def list_abtest_groups_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListABTestGroupsResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListABTestGroupsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListABTestGroups',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/groups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListABTestGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_abtest_groups_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListABTestGroupsResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListABTestGroupsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListABTestGroups',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/groups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListABTestGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_abtest_groups(
        self,
        app_group_identity: str,
        scene_id: str,
    ) -> open_search_20171225_models.ListABTestGroupsResponse:
        """
        @return: ListABTestGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_abtest_groups_with_options(app_group_identity, scene_id, headers, runtime)

    async def list_abtest_groups_async(
        self,
        app_group_identity: str,
        scene_id: str,
    ) -> open_search_20171225_models.ListABTestGroupsResponse:
        """
        @return: ListABTestGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_abtest_groups_with_options_async(app_group_identity, scene_id, headers, runtime)

    def list_abtest_scenes_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListABTestScenesResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListABTestScenesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListABTestScenes',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListABTestScenesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_abtest_scenes_with_options_async(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListABTestScenesResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListABTestScenesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListABTestScenes',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListABTestScenesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_abtest_scenes(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.ListABTestScenesResponse:
        """
        @return: ListABTestScenesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_abtest_scenes_with_options(app_group_identity, headers, runtime)

    async def list_abtest_scenes_async(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.ListABTestScenesResponse:
        """
        @return: ListABTestScenesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_abtest_scenes_with_options_async(app_group_identity, headers, runtime)

    def list_app_groups_with_options(
        self,
        tmp_req: open_search_20171225_models.ListAppGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListAppGroupsResponse:
        """
        @summary Queries a list of OpenSearch applications.
        
        @description    This operation allows you to query applications by application name, instance ID, and application type.
        This operation allows you to sort the applications based on their creation time.
        This operation supports the parameters for paging.
        
        @param tmp_req: ListAppGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppGroupsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = open_search_20171225_models.ListAppGroupsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sort_by):
            query['sortBy'] = request.sort_by
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppGroups',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListAppGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_groups_with_options_async(
        self,
        tmp_req: open_search_20171225_models.ListAppGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListAppGroupsResponse:
        """
        @summary Queries a list of OpenSearch applications.
        
        @description    This operation allows you to query applications by application name, instance ID, and application type.
        This operation allows you to sort the applications based on their creation time.
        This operation supports the parameters for paging.
        
        @param tmp_req: ListAppGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppGroupsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = open_search_20171225_models.ListAppGroupsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sort_by):
            query['sortBy'] = request.sort_by
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppGroups',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListAppGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_groups(
        self,
        request: open_search_20171225_models.ListAppGroupsRequest,
    ) -> open_search_20171225_models.ListAppGroupsResponse:
        """
        @summary Queries a list of OpenSearch applications.
        
        @description    This operation allows you to query applications by application name, instance ID, and application type.
        This operation allows you to sort the applications based on their creation time.
        This operation supports the parameters for paging.
        
        @param request: ListAppGroupsRequest
        @return: ListAppGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_app_groups_with_options(request, headers, runtime)

    async def list_app_groups_async(
        self,
        request: open_search_20171225_models.ListAppGroupsRequest,
    ) -> open_search_20171225_models.ListAppGroupsResponse:
        """
        @summary Queries a list of OpenSearch applications.
        
        @description    This operation allows you to query applications by application name, instance ID, and application type.
        This operation allows you to sort the applications based on their creation time.
        This operation supports the parameters for paging.
        
        @param request: ListAppGroupsRequest
        @return: ListAppGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_app_groups_with_options_async(request, headers, runtime)

    def list_data_collections_with_options(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListDataCollectionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListDataCollectionsResponse:
        """
        @param request: ListDataCollectionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataCollectionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataCollections',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/data-collections',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListDataCollectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_collections_with_options_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListDataCollectionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListDataCollectionsResponse:
        """
        @param request: ListDataCollectionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataCollectionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataCollections',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/data-collections',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListDataCollectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_collections(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListDataCollectionsRequest,
    ) -> open_search_20171225_models.ListDataCollectionsResponse:
        """
        @param request: ListDataCollectionsRequest
        @return: ListDataCollectionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_collections_with_options(app_group_identity, request, headers, runtime)

    async def list_data_collections_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListDataCollectionsRequest,
    ) -> open_search_20171225_models.ListDataCollectionsResponse:
        """
        @param request: ListDataCollectionsRequest
        @return: ListDataCollectionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_data_collections_with_options_async(app_group_identity, request, headers, runtime)

    def list_data_source_table_fields_with_options(
        self,
        data_source_type: str,
        request: open_search_20171225_models.ListDataSourceTableFieldsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListDataSourceTableFieldsResponse:
        """
        @summary Queries all fields in a table of a data source. This operation is for internal use only.
        
        @param request: ListDataSourceTableFieldsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourceTableFieldsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.params):
            query['params'] = request.params
        if not UtilClient.is_unset(request.raw_type):
            query['rawType'] = request.raw_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataSourceTableFields',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/assist/data-sources/{OpenApiUtilClient.get_encode_param(data_source_type)}/fields',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListDataSourceTableFieldsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_source_table_fields_with_options_async(
        self,
        data_source_type: str,
        request: open_search_20171225_models.ListDataSourceTableFieldsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListDataSourceTableFieldsResponse:
        """
        @summary Queries all fields in a table of a data source. This operation is for internal use only.
        
        @param request: ListDataSourceTableFieldsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourceTableFieldsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.params):
            query['params'] = request.params
        if not UtilClient.is_unset(request.raw_type):
            query['rawType'] = request.raw_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataSourceTableFields',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/assist/data-sources/{OpenApiUtilClient.get_encode_param(data_source_type)}/fields',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListDataSourceTableFieldsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_source_table_fields(
        self,
        data_source_type: str,
        request: open_search_20171225_models.ListDataSourceTableFieldsRequest,
    ) -> open_search_20171225_models.ListDataSourceTableFieldsResponse:
        """
        @summary Queries all fields in a table of a data source. This operation is for internal use only.
        
        @param request: ListDataSourceTableFieldsRequest
        @return: ListDataSourceTableFieldsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_source_table_fields_with_options(data_source_type, request, headers, runtime)

    async def list_data_source_table_fields_async(
        self,
        data_source_type: str,
        request: open_search_20171225_models.ListDataSourceTableFieldsRequest,
    ) -> open_search_20171225_models.ListDataSourceTableFieldsResponse:
        """
        @summary Queries all fields in a table of a data source. This operation is for internal use only.
        
        @param request: ListDataSourceTableFieldsRequest
        @return: ListDataSourceTableFieldsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_data_source_table_fields_with_options_async(data_source_type, request, headers, runtime)

    def list_data_source_tables_with_options(
        self,
        data_source_type: str,
        request: open_search_20171225_models.ListDataSourceTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListDataSourceTablesResponse:
        """
        @param request: ListDataSourceTablesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourceTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.params):
            query['params'] = request.params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataSourceTables',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/assist/data-sources/{OpenApiUtilClient.get_encode_param(data_source_type)}/tables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListDataSourceTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_source_tables_with_options_async(
        self,
        data_source_type: str,
        request: open_search_20171225_models.ListDataSourceTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListDataSourceTablesResponse:
        """
        @param request: ListDataSourceTablesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourceTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.params):
            query['params'] = request.params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataSourceTables',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/assist/data-sources/{OpenApiUtilClient.get_encode_param(data_source_type)}/tables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListDataSourceTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_source_tables(
        self,
        data_source_type: str,
        request: open_search_20171225_models.ListDataSourceTablesRequest,
    ) -> open_search_20171225_models.ListDataSourceTablesResponse:
        """
        @param request: ListDataSourceTablesRequest
        @return: ListDataSourceTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_source_tables_with_options(data_source_type, request, headers, runtime)

    async def list_data_source_tables_async(
        self,
        data_source_type: str,
        request: open_search_20171225_models.ListDataSourceTablesRequest,
    ) -> open_search_20171225_models.ListDataSourceTablesResponse:
        """
        @param request: ListDataSourceTablesRequest
        @return: ListDataSourceTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_data_source_tables_with_options_async(data_source_type, request, headers, runtime)

    def list_first_ranks_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListFirstRanksResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFirstRanksResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListFirstRanks',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/first-ranks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListFirstRanksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_first_ranks_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListFirstRanksResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFirstRanksResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListFirstRanks',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/first-ranks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListFirstRanksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_first_ranks(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> open_search_20171225_models.ListFirstRanksResponse:
        """
        @return: ListFirstRanksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_first_ranks_with_options(app_group_identity, app_id, headers, runtime)

    async def list_first_ranks_async(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> open_search_20171225_models.ListFirstRanksResponse:
        """
        @return: ListFirstRanksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_first_ranks_with_options_async(app_group_identity, app_id, headers, runtime)

    def list_function_instances_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        request: open_search_20171225_models.ListFunctionInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListFunctionInstancesResponse:
        """
        @summary Queries all algorithm instances of a user, which meet specified conditions.
        
        @param request: ListFunctionInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFunctionInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_type):
            query['functionType'] = request.function_type
        if not UtilClient.is_unset(request.model_type):
            query['modelType'] = request.model_type
        if not UtilClient.is_unset(request.output):
            query['output'] = request.output
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.source):
            query['source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctionInstances',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListFunctionInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_function_instances_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        request: open_search_20171225_models.ListFunctionInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListFunctionInstancesResponse:
        """
        @summary Queries all algorithm instances of a user, which meet specified conditions.
        
        @param request: ListFunctionInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFunctionInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_type):
            query['functionType'] = request.function_type
        if not UtilClient.is_unset(request.model_type):
            query['modelType'] = request.model_type
        if not UtilClient.is_unset(request.output):
            query['output'] = request.output
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.source):
            query['source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctionInstances',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListFunctionInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_function_instances(
        self,
        app_group_identity: str,
        function_name: str,
        request: open_search_20171225_models.ListFunctionInstancesRequest,
    ) -> open_search_20171225_models.ListFunctionInstancesResponse:
        """
        @summary Queries all algorithm instances of a user, which meet specified conditions.
        
        @param request: ListFunctionInstancesRequest
        @return: ListFunctionInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_function_instances_with_options(app_group_identity, function_name, request, headers, runtime)

    async def list_function_instances_async(
        self,
        app_group_identity: str,
        function_name: str,
        request: open_search_20171225_models.ListFunctionInstancesRequest,
    ) -> open_search_20171225_models.ListFunctionInstancesResponse:
        """
        @summary Queries all algorithm instances of a user, which meet specified conditions.
        
        @param request: ListFunctionInstancesRequest
        @return: ListFunctionInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_function_instances_with_options_async(app_group_identity, function_name, request, headers, runtime)

    def list_function_resources_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        request: open_search_20171225_models.ListFunctionResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListFunctionResourcesResponse:
        """
        @summary Queries algorithm resources.
        
        @param request: ListFunctionResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFunctionResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output):
            query['output'] = request.output
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctionResources',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListFunctionResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_function_resources_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        request: open_search_20171225_models.ListFunctionResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListFunctionResourcesResponse:
        """
        @summary Queries algorithm resources.
        
        @param request: ListFunctionResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFunctionResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output):
            query['output'] = request.output
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctionResources',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListFunctionResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_function_resources(
        self,
        app_group_identity: str,
        function_name: str,
        request: open_search_20171225_models.ListFunctionResourcesRequest,
    ) -> open_search_20171225_models.ListFunctionResourcesResponse:
        """
        @summary Queries algorithm resources.
        
        @param request: ListFunctionResourcesRequest
        @return: ListFunctionResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_function_resources_with_options(app_group_identity, function_name, request, headers, runtime)

    async def list_function_resources_async(
        self,
        app_group_identity: str,
        function_name: str,
        request: open_search_20171225_models.ListFunctionResourcesRequest,
    ) -> open_search_20171225_models.ListFunctionResourcesResponse:
        """
        @summary Queries algorithm resources.
        
        @param request: ListFunctionResourcesRequest
        @return: ListFunctionResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_function_resources_with_options_async(app_group_identity, function_name, request, headers, runtime)

    def list_function_tasks_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        request: open_search_20171225_models.ListFunctionTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListFunctionTasksResponse:
        """
        @summary Queries the training tasks. The returned results are sorted by start time in descending order.
        
        @param request: ListFunctionTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFunctionTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctionTasks',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/instances/{OpenApiUtilClient.get_encode_param(instance_name)}/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListFunctionTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_function_tasks_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        request: open_search_20171225_models.ListFunctionTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListFunctionTasksResponse:
        """
        @summary Queries the training tasks. The returned results are sorted by start time in descending order.
        
        @param request: ListFunctionTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFunctionTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctionTasks',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/instances/{OpenApiUtilClient.get_encode_param(instance_name)}/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListFunctionTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_function_tasks(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        request: open_search_20171225_models.ListFunctionTasksRequest,
    ) -> open_search_20171225_models.ListFunctionTasksResponse:
        """
        @summary Queries the training tasks. The returned results are sorted by start time in descending order.
        
        @param request: ListFunctionTasksRequest
        @return: ListFunctionTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_function_tasks_with_options(app_group_identity, function_name, instance_name, request, headers, runtime)

    async def list_function_tasks_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        request: open_search_20171225_models.ListFunctionTasksRequest,
    ) -> open_search_20171225_models.ListFunctionTasksResponse:
        """
        @summary Queries the training tasks. The returned results are sorted by start time in descending order.
        
        @param request: ListFunctionTasksRequest
        @return: ListFunctionTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_function_tasks_with_options_async(app_group_identity, function_name, instance_name, request, headers, runtime)

    def list_intervention_dictionaries_with_options(
        self,
        request: open_search_20171225_models.ListInterventionDictionariesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListInterventionDictionariesResponse:
        """
        @param request: ListInterventionDictionariesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInterventionDictionariesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.types):
            query['types'] = request.types
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInterventionDictionaries',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/intervention-dictionaries',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListInterventionDictionariesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_intervention_dictionaries_with_options_async(
        self,
        request: open_search_20171225_models.ListInterventionDictionariesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListInterventionDictionariesResponse:
        """
        @param request: ListInterventionDictionariesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInterventionDictionariesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.types):
            query['types'] = request.types
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInterventionDictionaries',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/intervention-dictionaries',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListInterventionDictionariesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_intervention_dictionaries(
        self,
        request: open_search_20171225_models.ListInterventionDictionariesRequest,
    ) -> open_search_20171225_models.ListInterventionDictionariesResponse:
        """
        @param request: ListInterventionDictionariesRequest
        @return: ListInterventionDictionariesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_intervention_dictionaries_with_options(request, headers, runtime)

    async def list_intervention_dictionaries_async(
        self,
        request: open_search_20171225_models.ListInterventionDictionariesRequest,
    ) -> open_search_20171225_models.ListInterventionDictionariesResponse:
        """
        @param request: ListInterventionDictionariesRequest
        @return: ListInterventionDictionariesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_intervention_dictionaries_with_options_async(request, headers, runtime)

    def list_intervention_dictionary_entries_with_options(
        self,
        name: str,
        request: open_search_20171225_models.ListInterventionDictionaryEntriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListInterventionDictionaryEntriesResponse:
        """
        @summary Queries the intervention entries in an intervention dictionary.
        
        @param request: ListInterventionDictionaryEntriesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInterventionDictionaryEntriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.word):
            query['word'] = request.word
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInterventionDictionaryEntries',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/intervention-dictionaries/{OpenApiUtilClient.get_encode_param(name)}/entries',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListInterventionDictionaryEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_intervention_dictionary_entries_with_options_async(
        self,
        name: str,
        request: open_search_20171225_models.ListInterventionDictionaryEntriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListInterventionDictionaryEntriesResponse:
        """
        @summary Queries the intervention entries in an intervention dictionary.
        
        @param request: ListInterventionDictionaryEntriesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInterventionDictionaryEntriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.word):
            query['word'] = request.word
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInterventionDictionaryEntries',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/intervention-dictionaries/{OpenApiUtilClient.get_encode_param(name)}/entries',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListInterventionDictionaryEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_intervention_dictionary_entries(
        self,
        name: str,
        request: open_search_20171225_models.ListInterventionDictionaryEntriesRequest,
    ) -> open_search_20171225_models.ListInterventionDictionaryEntriesResponse:
        """
        @summary Queries the intervention entries in an intervention dictionary.
        
        @param request: ListInterventionDictionaryEntriesRequest
        @return: ListInterventionDictionaryEntriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_intervention_dictionary_entries_with_options(name, request, headers, runtime)

    async def list_intervention_dictionary_entries_async(
        self,
        name: str,
        request: open_search_20171225_models.ListInterventionDictionaryEntriesRequest,
    ) -> open_search_20171225_models.ListInterventionDictionaryEntriesResponse:
        """
        @summary Queries the intervention entries in an intervention dictionary.
        
        @param request: ListInterventionDictionaryEntriesRequest
        @return: ListInterventionDictionaryEntriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_intervention_dictionary_entries_with_options_async(name, request, headers, runtime)

    def list_intervention_dictionary_ner_results_with_options(
        self,
        name: str,
        request: open_search_20171225_models.ListInterventionDictionaryNerResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListInterventionDictionaryNerResultsResponse:
        """
        @param request: ListInterventionDictionaryNerResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInterventionDictionaryNerResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInterventionDictionaryNerResults',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/intervention-dictionaries/{OpenApiUtilClient.get_encode_param(name)}/ner-results',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListInterventionDictionaryNerResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_intervention_dictionary_ner_results_with_options_async(
        self,
        name: str,
        request: open_search_20171225_models.ListInterventionDictionaryNerResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListInterventionDictionaryNerResultsResponse:
        """
        @param request: ListInterventionDictionaryNerResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInterventionDictionaryNerResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInterventionDictionaryNerResults',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/intervention-dictionaries/{OpenApiUtilClient.get_encode_param(name)}/ner-results',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListInterventionDictionaryNerResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_intervention_dictionary_ner_results(
        self,
        name: str,
        request: open_search_20171225_models.ListInterventionDictionaryNerResultsRequest,
    ) -> open_search_20171225_models.ListInterventionDictionaryNerResultsResponse:
        """
        @param request: ListInterventionDictionaryNerResultsRequest
        @return: ListInterventionDictionaryNerResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_intervention_dictionary_ner_results_with_options(name, request, headers, runtime)

    async def list_intervention_dictionary_ner_results_async(
        self,
        name: str,
        request: open_search_20171225_models.ListInterventionDictionaryNerResultsRequest,
    ) -> open_search_20171225_models.ListInterventionDictionaryNerResultsResponse:
        """
        @param request: ListInterventionDictionaryNerResultsRequest
        @return: ListInterventionDictionaryNerResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_intervention_dictionary_ner_results_with_options_async(name, request, headers, runtime)

    def list_intervention_dictionary_related_entities_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListInterventionDictionaryRelatedEntitiesResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInterventionDictionaryRelatedEntitiesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListInterventionDictionaryRelatedEntities',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/intervention-dictionaries/{OpenApiUtilClient.get_encode_param(name)}/related',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListInterventionDictionaryRelatedEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_intervention_dictionary_related_entities_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListInterventionDictionaryRelatedEntitiesResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInterventionDictionaryRelatedEntitiesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListInterventionDictionaryRelatedEntities',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/intervention-dictionaries/{OpenApiUtilClient.get_encode_param(name)}/related',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListInterventionDictionaryRelatedEntitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_intervention_dictionary_related_entities(
        self,
        name: str,
    ) -> open_search_20171225_models.ListInterventionDictionaryRelatedEntitiesResponse:
        """
        @return: ListInterventionDictionaryRelatedEntitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_intervention_dictionary_related_entities_with_options(name, headers, runtime)

    async def list_intervention_dictionary_related_entities_async(
        self,
        name: str,
    ) -> open_search_20171225_models.ListInterventionDictionaryRelatedEntitiesResponse:
        """
        @return: ListInterventionDictionaryRelatedEntitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_intervention_dictionary_related_entities_with_options_async(name, headers, runtime)

    def list_proceedings_with_options(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListProceedingsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListProceedingsResponse:
        """
        @summary 查看当前的处理流
        
        @param request: ListProceedingsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProceedingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_finished):
            query['filterFinished'] = request.filter_finished
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProceedings',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/proceedings',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListProceedingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_proceedings_with_options_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListProceedingsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListProceedingsResponse:
        """
        @summary 查看当前的处理流
        
        @param request: ListProceedingsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProceedingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_finished):
            query['filterFinished'] = request.filter_finished
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProceedings',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/proceedings',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListProceedingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_proceedings(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListProceedingsRequest,
    ) -> open_search_20171225_models.ListProceedingsResponse:
        """
        @summary 查看当前的处理流
        
        @param request: ListProceedingsRequest
        @return: ListProceedingsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_proceedings_with_options(app_group_identity, request, headers, runtime)

    async def list_proceedings_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListProceedingsRequest,
    ) -> open_search_20171225_models.ListProceedingsResponse:
        """
        @summary 查看当前的处理流
        
        @param request: ListProceedingsRequest
        @return: ListProceedingsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_proceedings_with_options_async(app_group_identity, request, headers, runtime)

    def list_query_processor_analyzer_results_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: open_search_20171225_models.ListQueryProcessorAnalyzerResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListQueryProcessorAnalyzerResultsResponse:
        """
        @summary Queries the results of a query analysis test. This API operation is available only to existing applications of OpenSearch Open Source Compatible Edition.
        
        @param request: ListQueryProcessorAnalyzerResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQueryProcessorAnalyzerResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.text):
            query['text'] = request.text
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueryProcessorAnalyzerResults',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/query-processors/{OpenApiUtilClient.get_encode_param(name)}/analyze',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListQueryProcessorAnalyzerResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_query_processor_analyzer_results_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: open_search_20171225_models.ListQueryProcessorAnalyzerResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListQueryProcessorAnalyzerResultsResponse:
        """
        @summary Queries the results of a query analysis test. This API operation is available only to existing applications of OpenSearch Open Source Compatible Edition.
        
        @param request: ListQueryProcessorAnalyzerResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQueryProcessorAnalyzerResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.text):
            query['text'] = request.text
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueryProcessorAnalyzerResults',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/query-processors/{OpenApiUtilClient.get_encode_param(name)}/analyze',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListQueryProcessorAnalyzerResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_query_processor_analyzer_results(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: open_search_20171225_models.ListQueryProcessorAnalyzerResultsRequest,
    ) -> open_search_20171225_models.ListQueryProcessorAnalyzerResultsResponse:
        """
        @summary Queries the results of a query analysis test. This API operation is available only to existing applications of OpenSearch Open Source Compatible Edition.
        
        @param request: ListQueryProcessorAnalyzerResultsRequest
        @return: ListQueryProcessorAnalyzerResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_query_processor_analyzer_results_with_options(app_group_identity, app_id, name, request, headers, runtime)

    async def list_query_processor_analyzer_results_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: open_search_20171225_models.ListQueryProcessorAnalyzerResultsRequest,
    ) -> open_search_20171225_models.ListQueryProcessorAnalyzerResultsResponse:
        """
        @summary Queries the results of a query analysis test. This API operation is available only to existing applications of OpenSearch Open Source Compatible Edition.
        
        @param request: ListQueryProcessorAnalyzerResultsRequest
        @return: ListQueryProcessorAnalyzerResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_query_processor_analyzer_results_with_options_async(app_group_identity, app_id, name, request, headers, runtime)

    def list_query_processor_ners_with_options(
        self,
        request: open_search_20171225_models.ListQueryProcessorNersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListQueryProcessorNersResponse:
        """
        @summary Queries the recommended priority settings of entity types for named entity recognition (NER).
        
        @param request: ListQueryProcessorNersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQueryProcessorNersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueryProcessorNers',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/query-processor/ner/default-priorities',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListQueryProcessorNersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_query_processor_ners_with_options_async(
        self,
        request: open_search_20171225_models.ListQueryProcessorNersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListQueryProcessorNersResponse:
        """
        @summary Queries the recommended priority settings of entity types for named entity recognition (NER).
        
        @param request: ListQueryProcessorNersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQueryProcessorNersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueryProcessorNers',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/query-processor/ner/default-priorities',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListQueryProcessorNersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_query_processor_ners(
        self,
        request: open_search_20171225_models.ListQueryProcessorNersRequest,
    ) -> open_search_20171225_models.ListQueryProcessorNersResponse:
        """
        @summary Queries the recommended priority settings of entity types for named entity recognition (NER).
        
        @param request: ListQueryProcessorNersRequest
        @return: ListQueryProcessorNersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_query_processor_ners_with_options(request, headers, runtime)

    async def list_query_processor_ners_async(
        self,
        request: open_search_20171225_models.ListQueryProcessorNersRequest,
    ) -> open_search_20171225_models.ListQueryProcessorNersResponse:
        """
        @summary Queries the recommended priority settings of entity types for named entity recognition (NER).
        
        @param request: ListQueryProcessorNersRequest
        @return: ListQueryProcessorNersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_query_processor_ners_with_options_async(request, headers, runtime)

    def list_query_processors_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.ListQueryProcessorsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListQueryProcessorsResponse:
        """
        @summary Queries a list of query analysis rules that are configured for a version of an OpenSearch application.
        
        @param request: ListQueryProcessorsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQueryProcessorsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_active):
            query['isActive'] = request.is_active
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueryProcessors',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/query-processors',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListQueryProcessorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_query_processors_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.ListQueryProcessorsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListQueryProcessorsResponse:
        """
        @summary Queries a list of query analysis rules that are configured for a version of an OpenSearch application.
        
        @param request: ListQueryProcessorsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQueryProcessorsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_active):
            query['isActive'] = request.is_active
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueryProcessors',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/query-processors',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListQueryProcessorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_query_processors(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.ListQueryProcessorsRequest,
    ) -> open_search_20171225_models.ListQueryProcessorsResponse:
        """
        @summary Queries a list of query analysis rules that are configured for a version of an OpenSearch application.
        
        @param request: ListQueryProcessorsRequest
        @return: ListQueryProcessorsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_query_processors_with_options(app_group_identity, app_id, request, headers, runtime)

    async def list_query_processors_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.ListQueryProcessorsRequest,
    ) -> open_search_20171225_models.ListQueryProcessorsResponse:
        """
        @summary Queries a list of query analysis rules that are configured for a version of an OpenSearch application.
        
        @param request: ListQueryProcessorsRequest
        @return: ListQueryProcessorsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_query_processors_with_options_async(app_group_identity, app_id, request, headers, runtime)

    def list_quota_review_tasks_with_options(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListQuotaReviewTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListQuotaReviewTasksResponse:
        """
        @summary Queries tickets that are submitted to apply for quotas for an OpenSearch application.
        
        @param request: ListQuotaReviewTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQuotaReviewTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQuotaReviewTasks',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/quota-review-tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListQuotaReviewTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quota_review_tasks_with_options_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListQuotaReviewTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListQuotaReviewTasksResponse:
        """
        @summary Queries tickets that are submitted to apply for quotas for an OpenSearch application.
        
        @param request: ListQuotaReviewTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQuotaReviewTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQuotaReviewTasks',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/quota-review-tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListQuotaReviewTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quota_review_tasks(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListQuotaReviewTasksRequest,
    ) -> open_search_20171225_models.ListQuotaReviewTasksResponse:
        """
        @summary Queries tickets that are submitted to apply for quotas for an OpenSearch application.
        
        @param request: ListQuotaReviewTasksRequest
        @return: ListQuotaReviewTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_quota_review_tasks_with_options(app_group_identity, request, headers, runtime)

    async def list_quota_review_tasks_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListQuotaReviewTasksRequest,
    ) -> open_search_20171225_models.ListQuotaReviewTasksResponse:
        """
        @summary Queries tickets that are submitted to apply for quotas for an OpenSearch application.
        
        @param request: ListQuotaReviewTasksRequest
        @return: ListQuotaReviewTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_quota_review_tasks_with_options_async(app_group_identity, request, headers, runtime)

    def list_scheduled_tasks_with_options(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListScheduledTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListScheduledTasksResponse:
        """
        @summary Queries a list of scheduled tasks of an OpenSearch application.
        
        @param request: ListScheduledTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScheduledTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScheduledTasks',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scheduled-tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListScheduledTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scheduled_tasks_with_options_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListScheduledTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListScheduledTasksResponse:
        """
        @summary Queries a list of scheduled tasks of an OpenSearch application.
        
        @param request: ListScheduledTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScheduledTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScheduledTasks',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scheduled-tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListScheduledTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scheduled_tasks(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListScheduledTasksRequest,
    ) -> open_search_20171225_models.ListScheduledTasksResponse:
        """
        @summary Queries a list of scheduled tasks of an OpenSearch application.
        
        @param request: ListScheduledTasksRequest
        @return: ListScheduledTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_scheduled_tasks_with_options(app_group_identity, request, headers, runtime)

    async def list_scheduled_tasks_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListScheduledTasksRequest,
    ) -> open_search_20171225_models.ListScheduledTasksResponse:
        """
        @summary Queries a list of scheduled tasks of an OpenSearch application.
        
        @param request: ListScheduledTasksRequest
        @return: ListScheduledTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_scheduled_tasks_with_options_async(app_group_identity, request, headers, runtime)

    def list_search_strategies_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListSearchStrategiesResponse:
        """
        @summary Queries the details of query policies.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSearchStrategiesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSearchStrategies',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/search-strategies',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListSearchStrategiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_search_strategies_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListSearchStrategiesResponse:
        """
        @summary Queries the details of query policies.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSearchStrategiesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSearchStrategies',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/search-strategies',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListSearchStrategiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_search_strategies(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> open_search_20171225_models.ListSearchStrategiesResponse:
        """
        @summary Queries the details of query policies.
        
        @return: ListSearchStrategiesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_search_strategies_with_options(app_group_identity, app_id, headers, runtime)

    async def list_search_strategies_async(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> open_search_20171225_models.ListSearchStrategiesResponse:
        """
        @summary Queries the details of query policies.
        
        @return: ListSearchStrategiesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_search_strategies_with_options_async(app_group_identity, app_id, headers, runtime)

    def list_second_ranks_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListSecondRanksResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSecondRanksResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSecondRanks',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/second-ranks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListSecondRanksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_second_ranks_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListSecondRanksResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSecondRanksResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSecondRanks',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/second-ranks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListSecondRanksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_second_ranks(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> open_search_20171225_models.ListSecondRanksResponse:
        """
        @return: ListSecondRanksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_second_ranks_with_options(app_group_identity, app_id, headers, runtime)

    async def list_second_ranks_async(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> open_search_20171225_models.ListSecondRanksResponse:
        """
        @return: ListSecondRanksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_second_ranks_with_options_async(app_group_identity, app_id, headers, runtime)

    def list_slow_query_categories_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListSlowQueryCategoriesResponse:
        """
        @summary Queries the suggestions that are provided by Optimization Master for slow queries.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSlowQueryCategoriesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSlowQueryCategories',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/optimizers/slow-query/categories',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListSlowQueryCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_slow_query_categories_with_options_async(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListSlowQueryCategoriesResponse:
        """
        @summary Queries the suggestions that are provided by Optimization Master for slow queries.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSlowQueryCategoriesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSlowQueryCategories',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/optimizers/slow-query/categories',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListSlowQueryCategoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_slow_query_categories(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.ListSlowQueryCategoriesResponse:
        """
        @summary Queries the suggestions that are provided by Optimization Master for slow queries.
        
        @return: ListSlowQueryCategoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_slow_query_categories_with_options(app_group_identity, headers, runtime)

    async def list_slow_query_categories_async(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.ListSlowQueryCategoriesResponse:
        """
        @summary Queries the suggestions that are provided by Optimization Master for slow queries.
        
        @return: ListSlowQueryCategoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_slow_query_categories_with_options_async(app_group_identity, headers, runtime)

    def list_slow_query_queries_with_options(
        self,
        app_group_identity: str,
        category_index: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListSlowQueryQueriesResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSlowQueryQueriesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSlowQueryQueries',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/optimizers/slow-query/categories/{OpenApiUtilClient.get_encode_param(category_index)}/queries',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListSlowQueryQueriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_slow_query_queries_with_options_async(
        self,
        app_group_identity: str,
        category_index: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListSlowQueryQueriesResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSlowQueryQueriesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSlowQueryQueries',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/optimizers/slow-query/categories/{OpenApiUtilClient.get_encode_param(category_index)}/queries',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListSlowQueryQueriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_slow_query_queries(
        self,
        app_group_identity: str,
        category_index: str,
    ) -> open_search_20171225_models.ListSlowQueryQueriesResponse:
        """
        @return: ListSlowQueryQueriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_slow_query_queries_with_options(app_group_identity, category_index, headers, runtime)

    async def list_slow_query_queries_async(
        self,
        app_group_identity: str,
        category_index: str,
    ) -> open_search_20171225_models.ListSlowQueryQueriesResponse:
        """
        @return: ListSlowQueryQueriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_slow_query_queries_with_options_async(app_group_identity, category_index, headers, runtime)

    def list_sort_expressions_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListSortExpressionsResponse:
        """
        @summary Queries a list of sort expressions that are configured for a version of an OpenSearch application.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSortExpressionsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSortExpressions',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/sort-expressions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListSortExpressionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sort_expressions_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListSortExpressionsResponse:
        """
        @summary Queries a list of sort expressions that are configured for a version of an OpenSearch application.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSortExpressionsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSortExpressions',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/sort-expressions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListSortExpressionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sort_expressions(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> open_search_20171225_models.ListSortExpressionsResponse:
        """
        @summary Queries a list of sort expressions that are configured for a version of an OpenSearch application.
        
        @return: ListSortExpressionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_sort_expressions_with_options(app_group_identity, app_id, headers, runtime)

    async def list_sort_expressions_async(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> open_search_20171225_models.ListSortExpressionsResponse:
        """
        @summary Queries a list of sort expressions that are configured for a version of an OpenSearch application.
        
        @return: ListSortExpressionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_sort_expressions_with_options_async(app_group_identity, app_id, headers, runtime)

    def list_sort_scripts_with_options(
        self,
        app_group_identity: str,
        app_version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListSortScriptsResponse:
        """
        @summary Queries all sort scripts of an application version.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSortScriptsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSortScripts',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_version_id)}/sort-scripts',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListSortScriptsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sort_scripts_with_options_async(
        self,
        app_group_identity: str,
        app_version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListSortScriptsResponse:
        """
        @summary Queries all sort scripts of an application version.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSortScriptsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSortScripts',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_version_id)}/sort-scripts',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListSortScriptsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sort_scripts(
        self,
        app_group_identity: str,
        app_version_id: str,
    ) -> open_search_20171225_models.ListSortScriptsResponse:
        """
        @summary Queries all sort scripts of an application version.
        
        @return: ListSortScriptsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_sort_scripts_with_options(app_group_identity, app_version_id, headers, runtime)

    async def list_sort_scripts_async(
        self,
        app_group_identity: str,
        app_version_id: str,
    ) -> open_search_20171225_models.ListSortScriptsResponse:
        """
        @summary Queries all sort scripts of an application version.
        
        @return: ListSortScriptsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_sort_scripts_with_options_async(app_group_identity, app_version_id, headers, runtime)

    def list_statistic_logs_with_options(
        self,
        app_group_identity: str,
        module_name: str,
        request: open_search_20171225_models.ListStatisticLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListStatisticLogsResponse:
        """
        @summary Queries log statistics, such as application error logs, hotword rankings, and slow query logs.
        
        @param request: ListStatisticLogsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStatisticLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.columns):
            query['columns'] = request.columns
        if not UtilClient.is_unset(request.distinct):
            query['distinct'] = request.distinct
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.sort_by):
            query['sortBy'] = request.sort_by
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.stop_time):
            query['stopTime'] = request.stop_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStatisticLogs',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/statistic-logs/{OpenApiUtilClient.get_encode_param(module_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListStatisticLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_statistic_logs_with_options_async(
        self,
        app_group_identity: str,
        module_name: str,
        request: open_search_20171225_models.ListStatisticLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListStatisticLogsResponse:
        """
        @summary Queries log statistics, such as application error logs, hotword rankings, and slow query logs.
        
        @param request: ListStatisticLogsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStatisticLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.columns):
            query['columns'] = request.columns
        if not UtilClient.is_unset(request.distinct):
            query['distinct'] = request.distinct
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.sort_by):
            query['sortBy'] = request.sort_by
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.stop_time):
            query['stopTime'] = request.stop_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStatisticLogs',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/statistic-logs/{OpenApiUtilClient.get_encode_param(module_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListStatisticLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_statistic_logs(
        self,
        app_group_identity: str,
        module_name: str,
        request: open_search_20171225_models.ListStatisticLogsRequest,
    ) -> open_search_20171225_models.ListStatisticLogsResponse:
        """
        @summary Queries log statistics, such as application error logs, hotword rankings, and slow query logs.
        
        @param request: ListStatisticLogsRequest
        @return: ListStatisticLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_statistic_logs_with_options(app_group_identity, module_name, request, headers, runtime)

    async def list_statistic_logs_async(
        self,
        app_group_identity: str,
        module_name: str,
        request: open_search_20171225_models.ListStatisticLogsRequest,
    ) -> open_search_20171225_models.ListStatisticLogsResponse:
        """
        @summary Queries log statistics, such as application error logs, hotword rankings, and slow query logs.
        
        @param request: ListStatisticLogsRequest
        @return: ListStatisticLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_statistic_logs_with_options_async(app_group_identity, module_name, request, headers, runtime)

    def list_statistic_report_with_options(
        self,
        app_group_identity: str,
        module_name: str,
        request: open_search_20171225_models.ListStatisticReportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListStatisticReportResponse:
        """
        @param request: ListStatisticReportRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStatisticReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.columns):
            query['columns'] = request.columns
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStatisticReport',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/statistic-report/{OpenApiUtilClient.get_encode_param(module_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListStatisticReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_statistic_report_with_options_async(
        self,
        app_group_identity: str,
        module_name: str,
        request: open_search_20171225_models.ListStatisticReportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListStatisticReportResponse:
        """
        @param request: ListStatisticReportRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStatisticReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.columns):
            query['columns'] = request.columns
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStatisticReport',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/statistic-report/{OpenApiUtilClient.get_encode_param(module_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListStatisticReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_statistic_report(
        self,
        app_group_identity: str,
        module_name: str,
        request: open_search_20171225_models.ListStatisticReportRequest,
    ) -> open_search_20171225_models.ListStatisticReportResponse:
        """
        @param request: ListStatisticReportRequest
        @return: ListStatisticReportResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_statistic_report_with_options(app_group_identity, module_name, request, headers, runtime)

    async def list_statistic_report_async(
        self,
        app_group_identity: str,
        module_name: str,
        request: open_search_20171225_models.ListStatisticReportRequest,
    ) -> open_search_20171225_models.ListStatisticReportResponse:
        """
        @param request: ListStatisticReportRequest
        @return: ListStatisticReportResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_statistic_report_with_options_async(app_group_identity, module_name, request, headers, runtime)

    def list_tag_resources_with_options(
        self,
        tmp_req: open_search_20171225_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListTagResourcesResponse:
        """
        @summary Queries tagged resources.
        
        @param tmp_req: ListTagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = open_search_20171225_models.ListTagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_id):
            request.resource_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_id, 'resourceId', 'json')
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id_shrink):
            query['resourceId'] = request.resource_id_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/resource-tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        tmp_req: open_search_20171225_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListTagResourcesResponse:
        """
        @summary Queries tagged resources.
        
        @param tmp_req: ListTagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = open_search_20171225_models.ListTagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_id):
            request.resource_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_id, 'resourceId', 'json')
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id_shrink):
            query['resourceId'] = request.resource_id_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/resource-tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: open_search_20171225_models.ListTagResourcesRequest,
    ) -> open_search_20171225_models.ListTagResourcesResponse:
        """
        @summary Queries tagged resources.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    async def list_tag_resources_async(
        self,
        request: open_search_20171225_models.ListTagResourcesRequest,
    ) -> open_search_20171225_models.ListTagResourcesResponse:
        """
        @summary Queries tagged resources.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tag_resources_with_options_async(request, headers, runtime)

    def list_user_analyzer_entries_with_options(
        self,
        name: str,
        request: open_search_20171225_models.ListUserAnalyzerEntriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListUserAnalyzerEntriesResponse:
        """
        @summary Queries the entries of a custom analyzer.
        
        @param request: ListUserAnalyzerEntriesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserAnalyzerEntriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.word):
            query['word'] = request.word
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserAnalyzerEntries',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/user-analyzers/{OpenApiUtilClient.get_encode_param(name)}/entries',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListUserAnalyzerEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_analyzer_entries_with_options_async(
        self,
        name: str,
        request: open_search_20171225_models.ListUserAnalyzerEntriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListUserAnalyzerEntriesResponse:
        """
        @summary Queries the entries of a custom analyzer.
        
        @param request: ListUserAnalyzerEntriesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserAnalyzerEntriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.word):
            query['word'] = request.word
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserAnalyzerEntries',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/user-analyzers/{OpenApiUtilClient.get_encode_param(name)}/entries',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListUserAnalyzerEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_analyzer_entries(
        self,
        name: str,
        request: open_search_20171225_models.ListUserAnalyzerEntriesRequest,
    ) -> open_search_20171225_models.ListUserAnalyzerEntriesResponse:
        """
        @summary Queries the entries of a custom analyzer.
        
        @param request: ListUserAnalyzerEntriesRequest
        @return: ListUserAnalyzerEntriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_user_analyzer_entries_with_options(name, request, headers, runtime)

    async def list_user_analyzer_entries_async(
        self,
        name: str,
        request: open_search_20171225_models.ListUserAnalyzerEntriesRequest,
    ) -> open_search_20171225_models.ListUserAnalyzerEntriesResponse:
        """
        @summary Queries the entries of a custom analyzer.
        
        @param request: ListUserAnalyzerEntriesRequest
        @return: ListUserAnalyzerEntriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_user_analyzer_entries_with_options_async(name, request, headers, runtime)

    def list_user_analyzers_with_options(
        self,
        request: open_search_20171225_models.ListUserAnalyzersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListUserAnalyzersResponse:
        """
        @summary Queries the custom analyzers that belong to the current account.
        
        @param request: ListUserAnalyzersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserAnalyzersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserAnalyzers',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/user-analyzers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListUserAnalyzersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_analyzers_with_options_async(
        self,
        request: open_search_20171225_models.ListUserAnalyzersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListUserAnalyzersResponse:
        """
        @summary Queries the custom analyzers that belong to the current account.
        
        @param request: ListUserAnalyzersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserAnalyzersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserAnalyzers',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/user-analyzers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListUserAnalyzersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_analyzers(
        self,
        request: open_search_20171225_models.ListUserAnalyzersRequest,
    ) -> open_search_20171225_models.ListUserAnalyzersResponse:
        """
        @summary Queries the custom analyzers that belong to the current account.
        
        @param request: ListUserAnalyzersRequest
        @return: ListUserAnalyzersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_user_analyzers_with_options(request, headers, runtime)

    async def list_user_analyzers_async(
        self,
        request: open_search_20171225_models.ListUserAnalyzersRequest,
    ) -> open_search_20171225_models.ListUserAnalyzersResponse:
        """
        @summary Queries the custom analyzers that belong to the current account.
        
        @param request: ListUserAnalyzersRequest
        @return: ListUserAnalyzersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_user_analyzers_with_options_async(request, headers, runtime)

    def modify_app_group_with_options(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ModifyAppGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ModifyAppGroupResponse:
        """
        @summary Modifies the properties of an OpenSearch application or sets the online version of an OpenSearch application.
        
        @param request: ModifyAppGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.current_version):
            body['currentVersion'] = request.current_version
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.domain):
            body['domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyAppGroup',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifyAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_group_with_options_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ModifyAppGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ModifyAppGroupResponse:
        """
        @summary Modifies the properties of an OpenSearch application or sets the online version of an OpenSearch application.
        
        @param request: ModifyAppGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.current_version):
            body['currentVersion'] = request.current_version
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.domain):
            body['domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyAppGroup',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifyAppGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_group(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ModifyAppGroupRequest,
    ) -> open_search_20171225_models.ModifyAppGroupResponse:
        """
        @summary Modifies the properties of an OpenSearch application or sets the online version of an OpenSearch application.
        
        @param request: ModifyAppGroupRequest
        @return: ModifyAppGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_app_group_with_options(app_group_identity, request, headers, runtime)

    async def modify_app_group_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ModifyAppGroupRequest,
    ) -> open_search_20171225_models.ModifyAppGroupResponse:
        """
        @summary Modifies the properties of an OpenSearch application or sets the online version of an OpenSearch application.
        
        @param request: ModifyAppGroupRequest
        @return: ModifyAppGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_app_group_with_options_async(app_group_identity, request, headers, runtime)

    def modify_app_group_quota_with_options(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ModifyAppGroupQuotaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ModifyAppGroupQuotaResponse:
        """
        @param request: ModifyAppGroupQuotaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppGroupQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='ModifyAppGroupQuota',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/quota',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifyAppGroupQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_group_quota_with_options_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ModifyAppGroupQuotaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ModifyAppGroupQuotaResponse:
        """
        @param request: ModifyAppGroupQuotaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppGroupQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='ModifyAppGroupQuota',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/quota',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifyAppGroupQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_group_quota(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ModifyAppGroupQuotaRequest,
    ) -> open_search_20171225_models.ModifyAppGroupQuotaResponse:
        """
        @param request: ModifyAppGroupQuotaRequest
        @return: ModifyAppGroupQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_app_group_quota_with_options(app_group_identity, request, headers, runtime)

    async def modify_app_group_quota_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ModifyAppGroupQuotaRequest,
    ) -> open_search_20171225_models.ModifyAppGroupQuotaResponse:
        """
        @param request: ModifyAppGroupQuotaRequest
        @return: ModifyAppGroupQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_app_group_quota_with_options_async(app_group_identity, request, headers, runtime)

    def modify_first_rank_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: open_search_20171225_models.ModifyFirstRankRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ModifyFirstRankResponse:
        """
        @summary Modifies a rough sort expression for an OpenSearch application. If you set dryRun to true, this operation checks the rough sort expression after the expression is modified. If you do not specify this parameter, false is used by default.
        
        @param request: ModifyFirstRankRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyFirstRankResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='ModifyFirstRank',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/first-ranks/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifyFirstRankResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_first_rank_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: open_search_20171225_models.ModifyFirstRankRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ModifyFirstRankResponse:
        """
        @summary Modifies a rough sort expression for an OpenSearch application. If you set dryRun to true, this operation checks the rough sort expression after the expression is modified. If you do not specify this parameter, false is used by default.
        
        @param request: ModifyFirstRankRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyFirstRankResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='ModifyFirstRank',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/first-ranks/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifyFirstRankResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_first_rank(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: open_search_20171225_models.ModifyFirstRankRequest,
    ) -> open_search_20171225_models.ModifyFirstRankResponse:
        """
        @summary Modifies a rough sort expression for an OpenSearch application. If you set dryRun to true, this operation checks the rough sort expression after the expression is modified. If you do not specify this parameter, false is used by default.
        
        @param request: ModifyFirstRankRequest
        @return: ModifyFirstRankResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_first_rank_with_options(app_group_identity, app_id, name, request, headers, runtime)

    async def modify_first_rank_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: open_search_20171225_models.ModifyFirstRankRequest,
    ) -> open_search_20171225_models.ModifyFirstRankResponse:
        """
        @summary Modifies a rough sort expression for an OpenSearch application. If you set dryRun to true, this operation checks the rough sort expression after the expression is modified. If you do not specify this parameter, false is used by default.
        
        @param request: ModifyFirstRankRequest
        @return: ModifyFirstRankResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_first_rank_with_options_async(app_group_identity, app_id, name, request, headers, runtime)

    def modify_query_processor_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: open_search_20171225_models.ModifyQueryProcessorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ModifyQueryProcessorResponse:
        """
        @summary Modifies a query analysis rule for a specific application version. If you set dryRun to true, this operation checks the specified query analysis rule. By default, the value of dryRun is false if you do not specify this parameter.
        
        @param request: ModifyQueryProcessorRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyQueryProcessorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='ModifyQueryProcessor',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/query-processors/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifyQueryProcessorResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_query_processor_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: open_search_20171225_models.ModifyQueryProcessorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ModifyQueryProcessorResponse:
        """
        @summary Modifies a query analysis rule for a specific application version. If you set dryRun to true, this operation checks the specified query analysis rule. By default, the value of dryRun is false if you do not specify this parameter.
        
        @param request: ModifyQueryProcessorRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyQueryProcessorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='ModifyQueryProcessor',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/query-processors/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifyQueryProcessorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_query_processor(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: open_search_20171225_models.ModifyQueryProcessorRequest,
    ) -> open_search_20171225_models.ModifyQueryProcessorResponse:
        """
        @summary Modifies a query analysis rule for a specific application version. If you set dryRun to true, this operation checks the specified query analysis rule. By default, the value of dryRun is false if you do not specify this parameter.
        
        @param request: ModifyQueryProcessorRequest
        @return: ModifyQueryProcessorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_query_processor_with_options(app_group_identity, app_id, name, request, headers, runtime)

    async def modify_query_processor_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: open_search_20171225_models.ModifyQueryProcessorRequest,
    ) -> open_search_20171225_models.ModifyQueryProcessorResponse:
        """
        @summary Modifies a query analysis rule for a specific application version. If you set dryRun to true, this operation checks the specified query analysis rule. By default, the value of dryRun is false if you do not specify this parameter.
        
        @param request: ModifyQueryProcessorRequest
        @return: ModifyQueryProcessorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_query_processor_with_options_async(app_group_identity, app_id, name, request, headers, runtime)

    def modify_scheduled_task_with_options(
        self,
        app_group_identity: str,
        task_id: str,
        request: open_search_20171225_models.ModifyScheduledTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ModifyScheduledTaskResponse:
        """
        @summary Modifies a scheduled task.
        
        @param request: ModifyScheduledTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScheduledTaskResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='ModifyScheduledTask',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scheduled-tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifyScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scheduled_task_with_options_async(
        self,
        app_group_identity: str,
        task_id: str,
        request: open_search_20171225_models.ModifyScheduledTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ModifyScheduledTaskResponse:
        """
        @summary Modifies a scheduled task.
        
        @param request: ModifyScheduledTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScheduledTaskResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='ModifyScheduledTask',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scheduled-tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifyScheduledTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_scheduled_task(
        self,
        app_group_identity: str,
        task_id: str,
        request: open_search_20171225_models.ModifyScheduledTaskRequest,
    ) -> open_search_20171225_models.ModifyScheduledTaskResponse:
        """
        @summary Modifies a scheduled task.
        
        @param request: ModifyScheduledTaskRequest
        @return: ModifyScheduledTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_scheduled_task_with_options(app_group_identity, task_id, request, headers, runtime)

    async def modify_scheduled_task_async(
        self,
        app_group_identity: str,
        task_id: str,
        request: open_search_20171225_models.ModifyScheduledTaskRequest,
    ) -> open_search_20171225_models.ModifyScheduledTaskResponse:
        """
        @summary Modifies a scheduled task.
        
        @param request: ModifyScheduledTaskRequest
        @return: ModifyScheduledTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_scheduled_task_with_options_async(app_group_identity, task_id, request, headers, runtime)

    def modify_second_rank_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: open_search_20171225_models.ModifySecondRankRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ModifySecondRankResponse:
        """
        @summary Modifies a fine sort expression that is configured for a specific OpenSearch application version. If you set dryRun to true, the specified fine sort expression is checked after the expression is modified. By default, the value of dryRun is false if you do not specify this parameter.
        
        @param request: ModifySecondRankRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySecondRankResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='ModifySecondRank',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/second-ranks/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifySecondRankResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_second_rank_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: open_search_20171225_models.ModifySecondRankRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ModifySecondRankResponse:
        """
        @summary Modifies a fine sort expression that is configured for a specific OpenSearch application version. If you set dryRun to true, the specified fine sort expression is checked after the expression is modified. By default, the value of dryRun is false if you do not specify this parameter.
        
        @param request: ModifySecondRankRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySecondRankResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='ModifySecondRank',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/second-ranks/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifySecondRankResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_second_rank(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: open_search_20171225_models.ModifySecondRankRequest,
    ) -> open_search_20171225_models.ModifySecondRankResponse:
        """
        @summary Modifies a fine sort expression that is configured for a specific OpenSearch application version. If you set dryRun to true, the specified fine sort expression is checked after the expression is modified. By default, the value of dryRun is false if you do not specify this parameter.
        
        @param request: ModifySecondRankRequest
        @return: ModifySecondRankResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_second_rank_with_options(app_group_identity, app_id, name, request, headers, runtime)

    async def modify_second_rank_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        request: open_search_20171225_models.ModifySecondRankRequest,
    ) -> open_search_20171225_models.ModifySecondRankResponse:
        """
        @summary Modifies a fine sort expression that is configured for a specific OpenSearch application version. If you set dryRun to true, the specified fine sort expression is checked after the expression is modified. By default, the value of dryRun is false if you do not specify this parameter.
        
        @param request: ModifySecondRankRequest
        @return: ModifySecondRankResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_second_rank_with_options_async(app_group_identity, app_id, name, request, headers, runtime)

    def push_intervention_dictionary_entries_with_options(
        self,
        name: str,
        request: open_search_20171225_models.PushInterventionDictionaryEntriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.PushInterventionDictionaryEntriesResponse:
        """
        @summary Accepts the changes in intervention entries.
        
        @param request: PushInterventionDictionaryEntriesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushInterventionDictionaryEntriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='PushInterventionDictionaryEntries',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/intervention-dictionaries/{OpenApiUtilClient.get_encode_param(name)}/entries/actions/bulk',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.PushInterventionDictionaryEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_intervention_dictionary_entries_with_options_async(
        self,
        name: str,
        request: open_search_20171225_models.PushInterventionDictionaryEntriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.PushInterventionDictionaryEntriesResponse:
        """
        @summary Accepts the changes in intervention entries.
        
        @param request: PushInterventionDictionaryEntriesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushInterventionDictionaryEntriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='PushInterventionDictionaryEntries',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/intervention-dictionaries/{OpenApiUtilClient.get_encode_param(name)}/entries/actions/bulk',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.PushInterventionDictionaryEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_intervention_dictionary_entries(
        self,
        name: str,
        request: open_search_20171225_models.PushInterventionDictionaryEntriesRequest,
    ) -> open_search_20171225_models.PushInterventionDictionaryEntriesResponse:
        """
        @summary Accepts the changes in intervention entries.
        
        @param request: PushInterventionDictionaryEntriesRequest
        @return: PushInterventionDictionaryEntriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_intervention_dictionary_entries_with_options(name, request, headers, runtime)

    async def push_intervention_dictionary_entries_async(
        self,
        name: str,
        request: open_search_20171225_models.PushInterventionDictionaryEntriesRequest,
    ) -> open_search_20171225_models.PushInterventionDictionaryEntriesResponse:
        """
        @summary Accepts the changes in intervention entries.
        
        @param request: PushInterventionDictionaryEntriesRequest
        @return: PushInterventionDictionaryEntriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.push_intervention_dictionary_entries_with_options_async(name, request, headers, runtime)

    def push_user_analyzer_entries_with_options(
        self,
        name: str,
        request: open_search_20171225_models.PushUserAnalyzerEntriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.PushUserAnalyzerEntriesResponse:
        """
        @summary Accepts the changes in the entries of a custom analyzer.
        
        @param request: PushUserAnalyzerEntriesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushUserAnalyzerEntriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.entries):
            body['entries'] = request.entries
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushUserAnalyzerEntries',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/user-analyzers/{OpenApiUtilClient.get_encode_param(name)}/entries/actions/bulk',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.PushUserAnalyzerEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_user_analyzer_entries_with_options_async(
        self,
        name: str,
        request: open_search_20171225_models.PushUserAnalyzerEntriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.PushUserAnalyzerEntriesResponse:
        """
        @summary Accepts the changes in the entries of a custom analyzer.
        
        @param request: PushUserAnalyzerEntriesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushUserAnalyzerEntriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.entries):
            body['entries'] = request.entries
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushUserAnalyzerEntries',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/user-analyzers/{OpenApiUtilClient.get_encode_param(name)}/entries/actions/bulk',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.PushUserAnalyzerEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_user_analyzer_entries(
        self,
        name: str,
        request: open_search_20171225_models.PushUserAnalyzerEntriesRequest,
    ) -> open_search_20171225_models.PushUserAnalyzerEntriesResponse:
        """
        @summary Accepts the changes in the entries of a custom analyzer.
        
        @param request: PushUserAnalyzerEntriesRequest
        @return: PushUserAnalyzerEntriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_user_analyzer_entries_with_options(name, request, headers, runtime)

    async def push_user_analyzer_entries_async(
        self,
        name: str,
        request: open_search_20171225_models.PushUserAnalyzerEntriesRequest,
    ) -> open_search_20171225_models.PushUserAnalyzerEntriesResponse:
        """
        @summary Accepts the changes in the entries of a custom analyzer.
        
        @param request: PushUserAnalyzerEntriesRequest
        @return: PushUserAnalyzerEntriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.push_user_analyzer_entries_with_options_async(name, request, headers, runtime)

    def release_sort_script_with_options(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ReleaseSortScriptResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseSortScriptResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ReleaseSortScript',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_version_id)}/sort-scripts/{OpenApiUtilClient.get_encode_param(script_name)}/actions/release',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ReleaseSortScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_sort_script_with_options_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ReleaseSortScriptResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseSortScriptResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ReleaseSortScript',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_version_id)}/sort-scripts/{OpenApiUtilClient.get_encode_param(script_name)}/actions/release',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ReleaseSortScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_sort_script(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
    ) -> open_search_20171225_models.ReleaseSortScriptResponse:
        """
        @return: ReleaseSortScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.release_sort_script_with_options(app_group_identity, script_name, app_version_id, headers, runtime)

    async def release_sort_script_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
    ) -> open_search_20171225_models.ReleaseSortScriptResponse:
        """
        @return: ReleaseSortScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.release_sort_script_with_options_async(app_group_identity, script_name, app_version_id, headers, runtime)

    def remove_app_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RemoveAppResponse:
        """
        @summary Deletes a version of an OpenSearch application.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveAppResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveApp',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_app_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RemoveAppResponse:
        """
        @summary Deletes a version of an OpenSearch application.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveAppResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveApp',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_app(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> open_search_20171225_models.RemoveAppResponse:
        """
        @summary Deletes a version of an OpenSearch application.
        
        @return: RemoveAppResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_app_with_options(app_group_identity, app_id, headers, runtime)

    async def remove_app_async(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> open_search_20171225_models.RemoveAppResponse:
        """
        @summary Deletes a version of an OpenSearch application.
        
        @return: RemoveAppResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_app_with_options_async(app_group_identity, app_id, headers, runtime)

    def remove_app_group_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RemoveAppGroupResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveAppGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveAppGroup',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_app_group_with_options_async(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RemoveAppGroupResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveAppGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveAppGroup',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveAppGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_app_group(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.RemoveAppGroupResponse:
        """
        @return: RemoveAppGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_app_group_with_options(app_group_identity, headers, runtime)

    async def remove_app_group_async(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.RemoveAppGroupResponse:
        """
        @return: RemoveAppGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_app_group_with_options_async(app_group_identity, headers, runtime)

    def remove_data_collection_with_options(
        self,
        app_group_identity: str,
        data_collection_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RemoveDataCollectionResponse:
        """
        @summary Disables data collection.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveDataCollectionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveDataCollection',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/data-collections/{OpenApiUtilClient.get_encode_param(data_collection_identity)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveDataCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_data_collection_with_options_async(
        self,
        app_group_identity: str,
        data_collection_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RemoveDataCollectionResponse:
        """
        @summary Disables data collection.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveDataCollectionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveDataCollection',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/data-collections/{OpenApiUtilClient.get_encode_param(data_collection_identity)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveDataCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_data_collection(
        self,
        app_group_identity: str,
        data_collection_identity: str,
    ) -> open_search_20171225_models.RemoveDataCollectionResponse:
        """
        @summary Disables data collection.
        
        @return: RemoveDataCollectionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_data_collection_with_options(app_group_identity, data_collection_identity, headers, runtime)

    async def remove_data_collection_async(
        self,
        app_group_identity: str,
        data_collection_identity: str,
    ) -> open_search_20171225_models.RemoveDataCollectionResponse:
        """
        @summary Disables data collection.
        
        @return: RemoveDataCollectionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_data_collection_with_options_async(app_group_identity, data_collection_identity, headers, runtime)

    def remove_first_rank_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RemoveFirstRankResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveFirstRankResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveFirstRank',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/first-ranks/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveFirstRankResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_first_rank_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RemoveFirstRankResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveFirstRankResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveFirstRank',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/first-ranks/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveFirstRankResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_first_rank(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> open_search_20171225_models.RemoveFirstRankResponse:
        """
        @return: RemoveFirstRankResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_first_rank_with_options(app_group_identity, app_id, name, headers, runtime)

    async def remove_first_rank_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> open_search_20171225_models.RemoveFirstRankResponse:
        """
        @return: RemoveFirstRankResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_first_rank_with_options_async(app_group_identity, app_id, name, headers, runtime)

    def remove_intervention_dictionary_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RemoveInterventionDictionaryResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveInterventionDictionaryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveInterventionDictionary',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/intervention-dictionaries/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveInterventionDictionaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_intervention_dictionary_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RemoveInterventionDictionaryResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveInterventionDictionaryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveInterventionDictionary',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/intervention-dictionaries/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveInterventionDictionaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_intervention_dictionary(
        self,
        name: str,
    ) -> open_search_20171225_models.RemoveInterventionDictionaryResponse:
        """
        @return: RemoveInterventionDictionaryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_intervention_dictionary_with_options(name, headers, runtime)

    async def remove_intervention_dictionary_async(
        self,
        name: str,
    ) -> open_search_20171225_models.RemoveInterventionDictionaryResponse:
        """
        @return: RemoveInterventionDictionaryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_intervention_dictionary_with_options_async(name, headers, runtime)

    def remove_query_processor_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RemoveQueryProcessorResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveQueryProcessorResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveQueryProcessor',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/query-processors/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveQueryProcessorResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_query_processor_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RemoveQueryProcessorResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveQueryProcessorResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveQueryProcessor',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/query-processors/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveQueryProcessorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_query_processor(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> open_search_20171225_models.RemoveQueryProcessorResponse:
        """
        @return: RemoveQueryProcessorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_query_processor_with_options(app_group_identity, app_id, name, headers, runtime)

    async def remove_query_processor_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> open_search_20171225_models.RemoveQueryProcessorResponse:
        """
        @return: RemoveQueryProcessorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_query_processor_with_options_async(app_group_identity, app_id, name, headers, runtime)

    def remove_scheduled_task_with_options(
        self,
        app_group_identity: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RemoveScheduledTaskResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveScheduledTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveScheduledTask',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scheduled-tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_scheduled_task_with_options_async(
        self,
        app_group_identity: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RemoveScheduledTaskResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveScheduledTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveScheduledTask',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scheduled-tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveScheduledTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_scheduled_task(
        self,
        app_group_identity: str,
        task_id: str,
    ) -> open_search_20171225_models.RemoveScheduledTaskResponse:
        """
        @return: RemoveScheduledTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_scheduled_task_with_options(app_group_identity, task_id, headers, runtime)

    async def remove_scheduled_task_async(
        self,
        app_group_identity: str,
        task_id: str,
    ) -> open_search_20171225_models.RemoveScheduledTaskResponse:
        """
        @return: RemoveScheduledTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_scheduled_task_with_options_async(app_group_identity, task_id, headers, runtime)

    def remove_search_strategy_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        strategy_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RemoveSearchStrategyResponse:
        """
        @summary Deletes a query policy.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveSearchStrategyResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveSearchStrategy',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/search-strategies/{OpenApiUtilClient.get_encode_param(strategy_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveSearchStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_search_strategy_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        strategy_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RemoveSearchStrategyResponse:
        """
        @summary Deletes a query policy.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveSearchStrategyResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveSearchStrategy',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/search-strategies/{OpenApiUtilClient.get_encode_param(strategy_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveSearchStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_search_strategy(
        self,
        app_group_identity: str,
        app_id: str,
        strategy_name: str,
    ) -> open_search_20171225_models.RemoveSearchStrategyResponse:
        """
        @summary Deletes a query policy.
        
        @return: RemoveSearchStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_search_strategy_with_options(app_group_identity, app_id, strategy_name, headers, runtime)

    async def remove_search_strategy_async(
        self,
        app_group_identity: str,
        app_id: str,
        strategy_name: str,
    ) -> open_search_20171225_models.RemoveSearchStrategyResponse:
        """
        @summary Deletes a query policy.
        
        @return: RemoveSearchStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_search_strategy_with_options_async(app_group_identity, app_id, strategy_name, headers, runtime)

    def remove_second_rank_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RemoveSecondRankResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveSecondRankResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveSecondRank',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/second-ranks/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveSecondRankResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_second_rank_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RemoveSecondRankResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveSecondRankResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveSecondRank',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/second-ranks/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveSecondRankResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_second_rank(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> open_search_20171225_models.RemoveSecondRankResponse:
        """
        @return: RemoveSecondRankResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_second_rank_with_options(app_group_identity, app_id, name, headers, runtime)

    async def remove_second_rank_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> open_search_20171225_models.RemoveSecondRankResponse:
        """
        @return: RemoveSecondRankResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_second_rank_with_options_async(app_group_identity, app_id, name, headers, runtime)

    def remove_user_analyzer_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RemoveUserAnalyzerResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveUserAnalyzerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveUserAnalyzer',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/user-analyzers/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveUserAnalyzerResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_user_analyzer_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RemoveUserAnalyzerResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveUserAnalyzerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveUserAnalyzer',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/user-analyzers/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveUserAnalyzerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_user_analyzer(
        self,
        name: str,
    ) -> open_search_20171225_models.RemoveUserAnalyzerResponse:
        """
        @return: RemoveUserAnalyzerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_user_analyzer_with_options(name, headers, runtime)

    async def remove_user_analyzer_async(
        self,
        name: str,
    ) -> open_search_20171225_models.RemoveUserAnalyzerResponse:
        """
        @return: RemoveUserAnalyzerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_user_analyzer_with_options_async(name, headers, runtime)

    def renew_app_group_with_options(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.RenewAppGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RenewAppGroupResponse:
        """
        @summary Renews an application. This operation is not available now. You must renew an application in the OpenSearch console.
        
        @param request: RenewAppGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewAppGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='RenewAppGroup',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/actions/renew',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RenewAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_app_group_with_options_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.RenewAppGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RenewAppGroupResponse:
        """
        @summary Renews an application. This operation is not available now. You must renew an application in the OpenSearch console.
        
        @param request: RenewAppGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewAppGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='RenewAppGroup',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/actions/renew',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RenewAppGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_app_group(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.RenewAppGroupRequest,
    ) -> open_search_20171225_models.RenewAppGroupResponse:
        """
        @summary Renews an application. This operation is not available now. You must renew an application in the OpenSearch console.
        
        @param request: RenewAppGroupRequest
        @return: RenewAppGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.renew_app_group_with_options(app_group_identity, request, headers, runtime)

    async def renew_app_group_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.RenewAppGroupRequest,
    ) -> open_search_20171225_models.RenewAppGroupResponse:
        """
        @summary Renews an application. This operation is not available now. You must renew an application in the OpenSearch console.
        
        @param request: RenewAppGroupRequest
        @return: RenewAppGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.renew_app_group_with_options_async(app_group_identity, request, headers, runtime)

    def replace_app_group_commodity_code_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ReplaceAppGroupCommodityCodeResponse:
        """
        @summary Converts a service-based application to an instance-based application.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReplaceAppGroupCommodityCodeResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ReplaceAppGroupCommodityCode',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/actions/to-instance-typed',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ReplaceAppGroupCommodityCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def replace_app_group_commodity_code_with_options_async(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ReplaceAppGroupCommodityCodeResponse:
        """
        @summary Converts a service-based application to an instance-based application.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReplaceAppGroupCommodityCodeResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ReplaceAppGroupCommodityCode',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/actions/to-instance-typed',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ReplaceAppGroupCommodityCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def replace_app_group_commodity_code(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.ReplaceAppGroupCommodityCodeResponse:
        """
        @summary Converts a service-based application to an instance-based application.
        
        @return: ReplaceAppGroupCommodityCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.replace_app_group_commodity_code_with_options(app_group_identity, headers, runtime)

    async def replace_app_group_commodity_code_async(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.ReplaceAppGroupCommodityCodeResponse:
        """
        @summary Converts a service-based application to an instance-based application.
        
        @return: ReplaceAppGroupCommodityCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.replace_app_group_commodity_code_with_options_async(app_group_identity, headers, runtime)

    def save_sort_script_file_with_options(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        file_name: str,
        request: open_search_20171225_models.SaveSortScriptFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.SaveSortScriptFileResponse:
        """
        @summary Uploads a sort script.
        
        @param request: SaveSortScriptFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSortScriptFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveSortScriptFile',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_version_id)}/sort-scripts/{OpenApiUtilClient.get_encode_param(script_name)}/files/src/{OpenApiUtilClient.get_encode_param(file_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.SaveSortScriptFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_sort_script_file_with_options_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        file_name: str,
        request: open_search_20171225_models.SaveSortScriptFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.SaveSortScriptFileResponse:
        """
        @summary Uploads a sort script.
        
        @param request: SaveSortScriptFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveSortScriptFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveSortScriptFile',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_version_id)}/sort-scripts/{OpenApiUtilClient.get_encode_param(script_name)}/files/src/{OpenApiUtilClient.get_encode_param(file_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.SaveSortScriptFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_sort_script_file(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        file_name: str,
        request: open_search_20171225_models.SaveSortScriptFileRequest,
    ) -> open_search_20171225_models.SaveSortScriptFileResponse:
        """
        @summary Uploads a sort script.
        
        @param request: SaveSortScriptFileRequest
        @return: SaveSortScriptFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.save_sort_script_file_with_options(app_group_identity, script_name, app_version_id, file_name, request, headers, runtime)

    async def save_sort_script_file_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        file_name: str,
        request: open_search_20171225_models.SaveSortScriptFileRequest,
    ) -> open_search_20171225_models.SaveSortScriptFileResponse:
        """
        @summary Uploads a sort script.
        
        @param request: SaveSortScriptFileRequest
        @return: SaveSortScriptFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.save_sort_script_file_with_options_async(app_group_identity, script_name, app_version_id, file_name, request, headers, runtime)

    def start_slow_query_analyzer_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.StartSlowQueryAnalyzerResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartSlowQueryAnalyzerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartSlowQueryAnalyzer',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/optimizers/slow-query/actions/run',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.StartSlowQueryAnalyzerResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_slow_query_analyzer_with_options_async(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.StartSlowQueryAnalyzerResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartSlowQueryAnalyzerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartSlowQueryAnalyzer',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/optimizers/slow-query/actions/run',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.StartSlowQueryAnalyzerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_slow_query_analyzer(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.StartSlowQueryAnalyzerResponse:
        """
        @return: StartSlowQueryAnalyzerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_slow_query_analyzer_with_options(app_group_identity, headers, runtime)

    async def start_slow_query_analyzer_async(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.StartSlowQueryAnalyzerResponse:
        """
        @return: StartSlowQueryAnalyzerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_slow_query_analyzer_with_options_async(app_group_identity, headers, runtime)

    def tag_resources_with_options(
        self,
        request: open_search_20171225_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.TagResourcesResponse:
        """
        @summary Adds tags to resources.
        
        @param request: TagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_id):
            body['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            body['tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/resource-tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: open_search_20171225_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.TagResourcesResponse:
        """
        @summary Adds tags to resources.
        
        @param request: TagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_id):
            body['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            body['tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/resource-tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: open_search_20171225_models.TagResourcesRequest,
    ) -> open_search_20171225_models.TagResourcesResponse:
        """
        @summary Adds tags to resources.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    async def tag_resources_async(
        self,
        request: open_search_20171225_models.TagResourcesRequest,
    ) -> open_search_20171225_models.TagResourcesResponse:
        """
        @summary Adds tags to resources.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.tag_resources_with_options_async(request, headers, runtime)

    def unbind_esuser_analyzer_with_options(
        self,
        app_group_identity: str,
        es_instance_id: str,
        request: open_search_20171225_models.UnbindESUserAnalyzerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UnbindESUserAnalyzerResponse:
        """
        @summary Unbinds a custom analyzer from an Elasticsearch instance.
        
        @description You can call this operation to unbind a custom analyzer from an Elasticsearch instance.
        
        @param request: UnbindESUserAnalyzerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindESUserAnalyzerResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='UnbindESUserAnalyzer',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/es/{OpenApiUtilClient.get_encode_param(es_instance_id)}/actions/unbind-analyzer',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UnbindESUserAnalyzerResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_esuser_analyzer_with_options_async(
        self,
        app_group_identity: str,
        es_instance_id: str,
        request: open_search_20171225_models.UnbindESUserAnalyzerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UnbindESUserAnalyzerResponse:
        """
        @summary Unbinds a custom analyzer from an Elasticsearch instance.
        
        @description You can call this operation to unbind a custom analyzer from an Elasticsearch instance.
        
        @param request: UnbindESUserAnalyzerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindESUserAnalyzerResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='UnbindESUserAnalyzer',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/es/{OpenApiUtilClient.get_encode_param(es_instance_id)}/actions/unbind-analyzer',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UnbindESUserAnalyzerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_esuser_analyzer(
        self,
        app_group_identity: str,
        es_instance_id: str,
        request: open_search_20171225_models.UnbindESUserAnalyzerRequest,
    ) -> open_search_20171225_models.UnbindESUserAnalyzerResponse:
        """
        @summary Unbinds a custom analyzer from an Elasticsearch instance.
        
        @description You can call this operation to unbind a custom analyzer from an Elasticsearch instance.
        
        @param request: UnbindESUserAnalyzerRequest
        @return: UnbindESUserAnalyzerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.unbind_esuser_analyzer_with_options(app_group_identity, es_instance_id, request, headers, runtime)

    async def unbind_esuser_analyzer_async(
        self,
        app_group_identity: str,
        es_instance_id: str,
        request: open_search_20171225_models.UnbindESUserAnalyzerRequest,
    ) -> open_search_20171225_models.UnbindESUserAnalyzerResponse:
        """
        @summary Unbinds a custom analyzer from an Elasticsearch instance.
        
        @description You can call this operation to unbind a custom analyzer from an Elasticsearch instance.
        
        @param request: UnbindESUserAnalyzerRequest
        @return: UnbindESUserAnalyzerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.unbind_esuser_analyzer_with_options_async(app_group_identity, es_instance_id, request, headers, runtime)

    def unbind_es_instance_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UnbindEsInstanceResponse:
        """
        @summary Unbinds an Elasticsearch instance from an OpenSearch application.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindEsInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UnbindEsInstance',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/actions/unbind-es-instance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UnbindEsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_es_instance_with_options_async(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UnbindEsInstanceResponse:
        """
        @summary Unbinds an Elasticsearch instance from an OpenSearch application.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindEsInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UnbindEsInstance',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/actions/unbind-es-instance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UnbindEsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_es_instance(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.UnbindEsInstanceResponse:
        """
        @summary Unbinds an Elasticsearch instance from an OpenSearch application.
        
        @return: UnbindEsInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.unbind_es_instance_with_options(app_group_identity, headers, runtime)

    async def unbind_es_instance_async(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.UnbindEsInstanceResponse:
        """
        @summary Unbinds an Elasticsearch instance from an OpenSearch application.
        
        @return: UnbindEsInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.unbind_es_instance_with_options_async(app_group_identity, headers, runtime)

    def untag_resources_with_options(
        self,
        tmp_req: open_search_20171225_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UntagResourcesResponse:
        """
        @summary Remove tags from resources.
        
        @param tmp_req: UntagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = open_search_20171225_models.UntagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_id):
            request.resource_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_id, 'resourceId', 'json')
        if not UtilClient.is_unset(tmp_req.tag_key):
            request.tag_key_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_key, 'tagKey', 'json')
        query = {}
        if not UtilClient.is_unset(request.all):
            query['all'] = request.all
        if not UtilClient.is_unset(request.resource_id_shrink):
            query['resourceId'] = request.resource_id_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key_shrink):
            query['tagKey'] = request.tag_key_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/resource-tags',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        tmp_req: open_search_20171225_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UntagResourcesResponse:
        """
        @summary Remove tags from resources.
        
        @param tmp_req: UntagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = open_search_20171225_models.UntagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_id):
            request.resource_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_id, 'resourceId', 'json')
        if not UtilClient.is_unset(tmp_req.tag_key):
            request.tag_key_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_key, 'tagKey', 'json')
        query = {}
        if not UtilClient.is_unset(request.all):
            query['all'] = request.all
        if not UtilClient.is_unset(request.resource_id_shrink):
            query['resourceId'] = request.resource_id_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key_shrink):
            query['tagKey'] = request.tag_key_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/resource-tags',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: open_search_20171225_models.UntagResourcesRequest,
    ) -> open_search_20171225_models.UntagResourcesResponse:
        """
        @summary Remove tags from resources.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.untag_resources_with_options(request, headers, runtime)

    async def untag_resources_async(
        self,
        request: open_search_20171225_models.UntagResourcesRequest,
    ) -> open_search_20171225_models.UntagResourcesResponse:
        """
        @summary Remove tags from resources.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.untag_resources_with_options_async(request, headers, runtime)

    def update_abtest_experiment_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        request: open_search_20171225_models.UpdateABTestExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateABTestExperimentResponse:
        """
        @summary Modifies the parameters of an A/B test.
        
        @param request: UpdateABTestExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateABTestExperimentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateABTestExperiment',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateABTestExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_abtest_experiment_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        request: open_search_20171225_models.UpdateABTestExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateABTestExperimentResponse:
        """
        @summary Modifies the parameters of an A/B test.
        
        @param request: UpdateABTestExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateABTestExperimentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateABTestExperiment',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateABTestExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_abtest_experiment(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        request: open_search_20171225_models.UpdateABTestExperimentRequest,
    ) -> open_search_20171225_models.UpdateABTestExperimentResponse:
        """
        @summary Modifies the parameters of an A/B test.
        
        @param request: UpdateABTestExperimentRequest
        @return: UpdateABTestExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_abtest_experiment_with_options(app_group_identity, scene_id, group_id, experiment_id, request, headers, runtime)

    async def update_abtest_experiment_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        request: open_search_20171225_models.UpdateABTestExperimentRequest,
    ) -> open_search_20171225_models.UpdateABTestExperimentResponse:
        """
        @summary Modifies the parameters of an A/B test.
        
        @param request: UpdateABTestExperimentRequest
        @return: UpdateABTestExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_abtest_experiment_with_options_async(app_group_identity, scene_id, group_id, experiment_id, request, headers, runtime)

    def update_abtest_fixed_flow_dividers_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        request: open_search_20171225_models.UpdateABTestFixedFlowDividersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateABTestFixedFlowDividersResponse:
        """
        @summary Modifies whitelists.
        
        @param request: UpdateABTestFixedFlowDividersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateABTestFixedFlowDividersResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateABTestFixedFlowDividers',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}/fixed-flow-dividers',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateABTestFixedFlowDividersResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_abtest_fixed_flow_dividers_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        request: open_search_20171225_models.UpdateABTestFixedFlowDividersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateABTestFixedFlowDividersResponse:
        """
        @summary Modifies whitelists.
        
        @param request: UpdateABTestFixedFlowDividersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateABTestFixedFlowDividersResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateABTestFixedFlowDividers',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}/fixed-flow-dividers',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateABTestFixedFlowDividersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_abtest_fixed_flow_dividers(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        request: open_search_20171225_models.UpdateABTestFixedFlowDividersRequest,
    ) -> open_search_20171225_models.UpdateABTestFixedFlowDividersResponse:
        """
        @summary Modifies whitelists.
        
        @param request: UpdateABTestFixedFlowDividersRequest
        @return: UpdateABTestFixedFlowDividersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_abtest_fixed_flow_dividers_with_options(app_group_identity, scene_id, group_id, experiment_id, request, headers, runtime)

    async def update_abtest_fixed_flow_dividers_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        request: open_search_20171225_models.UpdateABTestFixedFlowDividersRequest,
    ) -> open_search_20171225_models.UpdateABTestFixedFlowDividersResponse:
        """
        @summary Modifies whitelists.
        
        @param request: UpdateABTestFixedFlowDividersRequest
        @return: UpdateABTestFixedFlowDividersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_abtest_fixed_flow_dividers_with_options_async(app_group_identity, scene_id, group_id, experiment_id, request, headers, runtime)

    def update_abtest_group_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        request: open_search_20171225_models.UpdateABTestGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateABTestGroupResponse:
        """
        @summary Modifies a test group.
        
        @param request: UpdateABTestGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateABTestGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateABTestGroup',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateABTestGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_abtest_group_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        request: open_search_20171225_models.UpdateABTestGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateABTestGroupResponse:
        """
        @summary Modifies a test group.
        
        @param request: UpdateABTestGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateABTestGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateABTestGroup',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateABTestGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_abtest_group(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        request: open_search_20171225_models.UpdateABTestGroupRequest,
    ) -> open_search_20171225_models.UpdateABTestGroupResponse:
        """
        @summary Modifies a test group.
        
        @param request: UpdateABTestGroupRequest
        @return: UpdateABTestGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_abtest_group_with_options(app_group_identity, scene_id, group_id, request, headers, runtime)

    async def update_abtest_group_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        request: open_search_20171225_models.UpdateABTestGroupRequest,
    ) -> open_search_20171225_models.UpdateABTestGroupResponse:
        """
        @summary Modifies a test group.
        
        @param request: UpdateABTestGroupRequest
        @return: UpdateABTestGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_abtest_group_with_options_async(app_group_identity, scene_id, group_id, request, headers, runtime)

    def update_abtest_scene_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        request: open_search_20171225_models.UpdateABTestSceneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateABTestSceneResponse:
        """
        @summary Modifies an A/B test scenario.
        
        @param request: UpdateABTestSceneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateABTestSceneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateABTestScene',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateABTestSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_abtest_scene_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        request: open_search_20171225_models.UpdateABTestSceneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateABTestSceneResponse:
        """
        @summary Modifies an A/B test scenario.
        
        @param request: UpdateABTestSceneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateABTestSceneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateABTestScene',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateABTestSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_abtest_scene(
        self,
        app_group_identity: str,
        scene_id: str,
        request: open_search_20171225_models.UpdateABTestSceneRequest,
    ) -> open_search_20171225_models.UpdateABTestSceneResponse:
        """
        @summary Modifies an A/B test scenario.
        
        @param request: UpdateABTestSceneRequest
        @return: UpdateABTestSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_abtest_scene_with_options(app_group_identity, scene_id, request, headers, runtime)

    async def update_abtest_scene_async(
        self,
        app_group_identity: str,
        scene_id: str,
        request: open_search_20171225_models.UpdateABTestSceneRequest,
    ) -> open_search_20171225_models.UpdateABTestSceneResponse:
        """
        @summary Modifies an A/B test scenario.
        
        @param request: UpdateABTestSceneRequest
        @return: UpdateABTestSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_abtest_scene_with_options_async(app_group_identity, scene_id, request, headers, runtime)

    def update_fetch_fields_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.UpdateFetchFieldsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateFetchFieldsResponse:
        """
        @param request: UpdateFetchFieldsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFetchFieldsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateFetchFields',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/fetch-fields',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateFetchFieldsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_fetch_fields_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.UpdateFetchFieldsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateFetchFieldsResponse:
        """
        @param request: UpdateFetchFieldsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFetchFieldsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateFetchFields',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/fetch-fields',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateFetchFieldsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_fetch_fields(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.UpdateFetchFieldsRequest,
    ) -> open_search_20171225_models.UpdateFetchFieldsResponse:
        """
        @param request: UpdateFetchFieldsRequest
        @return: UpdateFetchFieldsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_fetch_fields_with_options(app_group_identity, app_id, request, headers, runtime)

    async def update_fetch_fields_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.UpdateFetchFieldsRequest,
    ) -> open_search_20171225_models.UpdateFetchFieldsResponse:
        """
        @param request: UpdateFetchFieldsRequest
        @return: UpdateFetchFieldsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_fetch_fields_with_options_async(app_group_identity, app_id, request, headers, runtime)

    def update_function_default_instance_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        request: open_search_20171225_models.UpdateFunctionDefaultInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateFunctionDefaultInstanceResponse:
        """
        @summary Sets the default algorithm instance used by the specified application. The new algorithm instance automatically overwrites the most recently set default instance. If no instance is set, the default instance is canceled.
        
        @param request: UpdateFunctionDefaultInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFunctionDefaultInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_name):
            body['instanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFunctionDefaultInstance',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/default-instance',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateFunctionDefaultInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_function_default_instance_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        request: open_search_20171225_models.UpdateFunctionDefaultInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateFunctionDefaultInstanceResponse:
        """
        @summary Sets the default algorithm instance used by the specified application. The new algorithm instance automatically overwrites the most recently set default instance. If no instance is set, the default instance is canceled.
        
        @param request: UpdateFunctionDefaultInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFunctionDefaultInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_name):
            body['instanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFunctionDefaultInstance',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/default-instance',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateFunctionDefaultInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_function_default_instance(
        self,
        app_group_identity: str,
        function_name: str,
        request: open_search_20171225_models.UpdateFunctionDefaultInstanceRequest,
    ) -> open_search_20171225_models.UpdateFunctionDefaultInstanceResponse:
        """
        @summary Sets the default algorithm instance used by the specified application. The new algorithm instance automatically overwrites the most recently set default instance. If no instance is set, the default instance is canceled.
        
        @param request: UpdateFunctionDefaultInstanceRequest
        @return: UpdateFunctionDefaultInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_function_default_instance_with_options(app_group_identity, function_name, request, headers, runtime)

    async def update_function_default_instance_async(
        self,
        app_group_identity: str,
        function_name: str,
        request: open_search_20171225_models.UpdateFunctionDefaultInstanceRequest,
    ) -> open_search_20171225_models.UpdateFunctionDefaultInstanceResponse:
        """
        @summary Sets the default algorithm instance used by the specified application. The new algorithm instance automatically overwrites the most recently set default instance. If no instance is set, the default instance is canceled.
        
        @param request: UpdateFunctionDefaultInstanceRequest
        @return: UpdateFunctionDefaultInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_function_default_instance_with_options_async(app_group_identity, function_name, request, headers, runtime)

    def update_function_instance_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        request: open_search_20171225_models.UpdateFunctionInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateFunctionInstanceResponse:
        """
        @summary Updates an algorithm instance.
        
        @param request: UpdateFunctionInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFunctionInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.create_parameters):
            body['createParameters'] = request.create_parameters
        if not UtilClient.is_unset(request.cron):
            body['cron'] = request.cron
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.usage_parameters):
            body['usageParameters'] = request.usage_parameters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFunctionInstance',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/instances/{OpenApiUtilClient.get_encode_param(instance_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateFunctionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_function_instance_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        request: open_search_20171225_models.UpdateFunctionInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateFunctionInstanceResponse:
        """
        @summary Updates an algorithm instance.
        
        @param request: UpdateFunctionInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFunctionInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.create_parameters):
            body['createParameters'] = request.create_parameters
        if not UtilClient.is_unset(request.cron):
            body['cron'] = request.cron
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.usage_parameters):
            body['usageParameters'] = request.usage_parameters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFunctionInstance',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/instances/{OpenApiUtilClient.get_encode_param(instance_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateFunctionInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_function_instance(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        request: open_search_20171225_models.UpdateFunctionInstanceRequest,
    ) -> open_search_20171225_models.UpdateFunctionInstanceResponse:
        """
        @summary Updates an algorithm instance.
        
        @param request: UpdateFunctionInstanceRequest
        @return: UpdateFunctionInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_function_instance_with_options(app_group_identity, function_name, instance_name, request, headers, runtime)

    async def update_function_instance_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
        request: open_search_20171225_models.UpdateFunctionInstanceRequest,
    ) -> open_search_20171225_models.UpdateFunctionInstanceResponse:
        """
        @summary Updates an algorithm instance.
        
        @param request: UpdateFunctionInstanceRequest
        @return: UpdateFunctionInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_function_instance_with_options_async(app_group_identity, function_name, instance_name, request, headers, runtime)

    def update_function_resource_with_options(
        self,
        app_group_identity: str,
        function_name: str,
        resource_name: str,
        request: open_search_20171225_models.UpdateFunctionResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateFunctionResourceResponse:
        """
        @summary Updates an algorithm resource.
        
        @description You can call this operation to update the information about resources by resource name. You can modify only the values of data and description.
        
        @param request: UpdateFunctionResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFunctionResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFunctionResource',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/resources/{OpenApiUtilClient.get_encode_param(resource_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateFunctionResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_function_resource_with_options_async(
        self,
        app_group_identity: str,
        function_name: str,
        resource_name: str,
        request: open_search_20171225_models.UpdateFunctionResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateFunctionResourceResponse:
        """
        @summary Updates an algorithm resource.
        
        @description You can call this operation to update the information about resources by resource name. You can modify only the values of data and description.
        
        @param request: UpdateFunctionResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFunctionResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFunctionResource',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/functions/{OpenApiUtilClient.get_encode_param(function_name)}/resources/{OpenApiUtilClient.get_encode_param(resource_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateFunctionResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_function_resource(
        self,
        app_group_identity: str,
        function_name: str,
        resource_name: str,
        request: open_search_20171225_models.UpdateFunctionResourceRequest,
    ) -> open_search_20171225_models.UpdateFunctionResourceResponse:
        """
        @summary Updates an algorithm resource.
        
        @description You can call this operation to update the information about resources by resource name. You can modify only the values of data and description.
        
        @param request: UpdateFunctionResourceRequest
        @return: UpdateFunctionResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_function_resource_with_options(app_group_identity, function_name, resource_name, request, headers, runtime)

    async def update_function_resource_async(
        self,
        app_group_identity: str,
        function_name: str,
        resource_name: str,
        request: open_search_20171225_models.UpdateFunctionResourceRequest,
    ) -> open_search_20171225_models.UpdateFunctionResourceResponse:
        """
        @summary Updates an algorithm resource.
        
        @description You can call this operation to update the information about resources by resource name. You can modify only the values of data and description.
        
        @param request: UpdateFunctionResourceRequest
        @return: UpdateFunctionResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_function_resource_with_options_async(app_group_identity, function_name, resource_name, request, headers, runtime)

    def update_search_strategy_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        strategy_name: str,
        request: open_search_20171225_models.UpdateSearchStrategyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateSearchStrategyResponse:
        """
        @summary Modifies a query policy.
        
        @param request: UpdateSearchStrategyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSearchStrategyResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateSearchStrategy',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/search-strategies/{OpenApiUtilClient.get_encode_param(strategy_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateSearchStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_search_strategy_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        strategy_name: str,
        request: open_search_20171225_models.UpdateSearchStrategyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateSearchStrategyResponse:
        """
        @summary Modifies a query policy.
        
        @param request: UpdateSearchStrategyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSearchStrategyResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateSearchStrategy',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/search-strategies/{OpenApiUtilClient.get_encode_param(strategy_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateSearchStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_search_strategy(
        self,
        app_group_identity: str,
        app_id: str,
        strategy_name: str,
        request: open_search_20171225_models.UpdateSearchStrategyRequest,
    ) -> open_search_20171225_models.UpdateSearchStrategyResponse:
        """
        @summary Modifies a query policy.
        
        @param request: UpdateSearchStrategyRequest
        @return: UpdateSearchStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_search_strategy_with_options(app_group_identity, app_id, strategy_name, request, headers, runtime)

    async def update_search_strategy_async(
        self,
        app_group_identity: str,
        app_id: str,
        strategy_name: str,
        request: open_search_20171225_models.UpdateSearchStrategyRequest,
    ) -> open_search_20171225_models.UpdateSearchStrategyResponse:
        """
        @summary Modifies a query policy.
        
        @param request: UpdateSearchStrategyRequest
        @return: UpdateSearchStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_search_strategy_with_options_async(app_group_identity, app_id, strategy_name, request, headers, runtime)

    def update_sort_script_with_options(
        self,
        app_group_identity: str,
        app_version_id: str,
        script_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateSortScriptResponse:
        """
        @summary Modifies the description of a sort script.
        
        @description You can call this operation to modify the description of a sort script.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSortScriptResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateSortScript',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_version_id)}/sort-scripts/{OpenApiUtilClient.get_encode_param(script_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateSortScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sort_script_with_options_async(
        self,
        app_group_identity: str,
        app_version_id: str,
        script_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateSortScriptResponse:
        """
        @summary Modifies the description of a sort script.
        
        @description You can call this operation to modify the description of a sort script.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSortScriptResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateSortScript',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_version_id)}/sort-scripts/{OpenApiUtilClient.get_encode_param(script_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateSortScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sort_script(
        self,
        app_group_identity: str,
        app_version_id: str,
        script_name: str,
    ) -> open_search_20171225_models.UpdateSortScriptResponse:
        """
        @summary Modifies the description of a sort script.
        
        @description You can call this operation to modify the description of a sort script.
        
        @return: UpdateSortScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_sort_script_with_options(app_group_identity, app_version_id, script_name, headers, runtime)

    async def update_sort_script_async(
        self,
        app_group_identity: str,
        app_version_id: str,
        script_name: str,
    ) -> open_search_20171225_models.UpdateSortScriptResponse:
        """
        @summary Modifies the description of a sort script.
        
        @description You can call this operation to modify the description of a sort script.
        
        @return: UpdateSortScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_sort_script_with_options_async(app_group_identity, app_version_id, script_name, headers, runtime)

    def update_summaries_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.UpdateSummariesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateSummariesResponse:
        """
        @summary Updates summaries. A dry run is supported.
        
        @param request: UpdateSummariesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSummariesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='UpdateSummaries',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/summaries',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateSummariesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_summaries_with_options_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.UpdateSummariesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateSummariesResponse:
        """
        @summary Updates summaries. A dry run is supported.
        
        @param request: UpdateSummariesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSummariesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='UpdateSummaries',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/apps/{OpenApiUtilClient.get_encode_param(app_id)}/summaries',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateSummariesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_summaries(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.UpdateSummariesRequest,
    ) -> open_search_20171225_models.UpdateSummariesResponse:
        """
        @summary Updates summaries. A dry run is supported.
        
        @param request: UpdateSummariesRequest
        @return: UpdateSummariesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_summaries_with_options(app_group_identity, app_id, request, headers, runtime)

    async def update_summaries_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.UpdateSummariesRequest,
    ) -> open_search_20171225_models.UpdateSummariesResponse:
        """
        @summary Updates summaries. A dry run is supported.
        
        @param request: UpdateSummariesRequest
        @return: UpdateSummariesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_summaries_with_options_async(app_group_identity, app_id, request, headers, runtime)

    def validate_data_sources_with_options(
        self,
        request: open_search_20171225_models.ValidateDataSourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ValidateDataSourcesResponse:
        """
        @summary Verifies data sources.
        
        @param request: ValidateDataSourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateDataSourcesResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='ValidateDataSources',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/assist/data-sources/validations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ValidateDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_data_sources_with_options_async(
        self,
        request: open_search_20171225_models.ValidateDataSourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ValidateDataSourcesResponse:
        """
        @summary Verifies data sources.
        
        @param request: ValidateDataSourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateDataSourcesResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='ValidateDataSources',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/assist/data-sources/validations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ValidateDataSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_data_sources(
        self,
        request: open_search_20171225_models.ValidateDataSourcesRequest,
    ) -> open_search_20171225_models.ValidateDataSourcesResponse:
        """
        @summary Verifies data sources.
        
        @param request: ValidateDataSourcesRequest
        @return: ValidateDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.validate_data_sources_with_options(request, headers, runtime)

    async def validate_data_sources_async(
        self,
        request: open_search_20171225_models.ValidateDataSourcesRequest,
    ) -> open_search_20171225_models.ValidateDataSourcesResponse:
        """
        @summary Verifies data sources.
        
        @param request: ValidateDataSourcesRequest
        @return: ValidateDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.validate_data_sources_with_options_async(request, headers, runtime)
