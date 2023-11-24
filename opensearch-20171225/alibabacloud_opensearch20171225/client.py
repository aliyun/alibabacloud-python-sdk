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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.bind_esuser_analyzer_with_options(app_group_identity, es_instance_id, request, headers, runtime)

    async def bind_esuser_analyzer_async(
        self,
        app_group_identity: str,
        es_instance_id: str,
        request: open_search_20171225_models.BindESUserAnalyzerRequest,
    ) -> open_search_20171225_models.BindESUserAnalyzerResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.bind_es_instance_with_options(app_group_identity, request, headers, runtime)

    async def bind_es_instance_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.BindEsInstanceRequest,
    ) -> open_search_20171225_models.BindEsInstanceResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.compile_sort_script_with_options(app_group_identity, script_name, app_version_id, headers, runtime)

    async def compile_sort_script_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
    ) -> open_search_20171225_models.CompileSortScriptResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_abtest_group_with_options(app_group_identity, scene_id, request, headers, runtime)

    async def create_abtest_group_async(
        self,
        app_group_identity: str,
        scene_id: str,
        request: open_search_20171225_models.CreateABTestGroupRequest,
    ) -> open_search_20171225_models.CreateABTestGroupResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_abtest_scene_with_options(app_group_identity, request, headers, runtime)

    async def create_abtest_scene_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.CreateABTestSceneRequest,
    ) -> open_search_20171225_models.CreateABTestSceneResponse:
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
        When you create a standard application, a new version of the application is created if the specified application name already exists.
        *   When you create a version of an existing application, you must specify the autoSwitch and realtimeShared parameters.
        *   When you create a version of an existing application, the value of the quota parameter is the same as that of the quota parameter in the previous version of the application.
        *   When you create a version of an existing application, the modification of the value of the quota parameter does not take effect.
        
        @param request: CreateAppRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppResponse
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
        When you create a standard application, a new version of the application is created if the specified application name already exists.
        *   When you create a version of an existing application, you must specify the autoSwitch and realtimeShared parameters.
        *   When you create a version of an existing application, the value of the quota parameter is the same as that of the quota parameter in the previous version of the application.
        *   When you create a version of an existing application, the modification of the value of the quota parameter does not take effect.
        
        @param request: CreateAppRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppResponse
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
        When you create a standard application, a new version of the application is created if the specified application name already exists.
        *   When you create a version of an existing application, you must specify the autoSwitch and realtimeShared parameters.
        *   When you create a version of an existing application, the value of the quota parameter is the same as that of the quota parameter in the previous version of the application.
        *   When you create a version of an existing application, the modification of the value of the quota parameter does not take effect.
        
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
        When you create a standard application, a new version of the application is created if the specified application name already exists.
        *   When you create a version of an existing application, you must specify the autoSwitch and realtimeShared parameters.
        *   When you create a version of an existing application, the value of the quota parameter is the same as that of the quota parameter in the previous version of the application.
        *   When you create a version of an existing application, the modification of the value of the quota parameter does not take effect.
        
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_app_group_with_options(request, headers, runtime)

    async def create_app_group_async(
        self,
        request: open_search_20171225_models.CreateAppGroupRequest,
    ) -> open_search_20171225_models.CreateAppGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_app_group_with_options_async(request, headers, runtime)

    def create_first_rank_with_options(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.CreateFirstRankRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateFirstRankResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_first_rank_with_options(app_group_identity, app_id, request, headers, runtime)

    async def create_first_rank_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.CreateFirstRankRequest,
    ) -> open_search_20171225_models.CreateFirstRankResponse:
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
        You can call the [GetFunctionCurrentVersion](~~421377~~) operation to query the latest version of the current feature. The response of the operation includes the createParameters parameter that is used to create an algorithm instance, the usageParameters parameter, and the requirements for setting these parameters.
        
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
        You can call the [GetFunctionCurrentVersion](~~421377~~) operation to query the latest version of the current feature. The response of the operation includes the createParameters parameter that is used to create an algorithm instance, the usageParameters parameter, and the requirements for setting these parameters.
        
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
        You can call the [GetFunctionCurrentVersion](~~421377~~) operation to query the latest version of the current feature. The response of the operation includes the createParameters parameter that is used to create an algorithm instance, the usageParameters parameter, and the requirements for setting these parameters.
        
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
        You can call the [GetFunctionCurrentVersion](~~421377~~) operation to query the latest version of the current feature. The response of the operation includes the createParameters parameter that is used to create an algorithm instance, the usageParameters parameter, and the requirements for setting these parameters.
        
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_function_resource_with_options(app_group_identity, function_name, request, headers, runtime)

    async def create_function_resource_async(
        self,
        app_group_identity: str,
        function_name: str,
        request: open_search_20171225_models.CreateFunctionResourceRequest,
    ) -> open_search_20171225_models.CreateFunctionResourceResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_function_task_with_options(app_group_identity, function_name, instance_name, headers, runtime)

    async def create_function_task_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
    ) -> open_search_20171225_models.CreateFunctionTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_function_task_with_options_async(app_group_identity, function_name, instance_name, headers, runtime)

    def create_intervention_dictionary_with_options(
        self,
        request: open_search_20171225_models.CreateInterventionDictionaryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateInterventionDictionaryResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_intervention_dictionary_with_options(request, headers, runtime)

    async def create_intervention_dictionary_async(
        self,
        request: open_search_20171225_models.CreateInterventionDictionaryRequest,
    ) -> open_search_20171225_models.CreateInterventionDictionaryResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_query_processor_with_options(app_group_identity, app_id, request, headers, runtime)

    async def create_query_processor_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.CreateQueryProcessorRequest,
    ) -> open_search_20171225_models.CreateQueryProcessorResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_scheduled_task_with_options(app_group_identity, request, headers, runtime)

    async def create_scheduled_task_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.CreateScheduledTaskRequest,
    ) -> open_search_20171225_models.CreateScheduledTaskResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_search_strategy_with_options(app_group_identity, app_id, request, headers, runtime)

    async def create_search_strategy_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.CreateSearchStrategyRequest,
    ) -> open_search_20171225_models.CreateSearchStrategyResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_second_rank_with_options(app_group_identity, app_id, request, headers, runtime)

    async def create_second_rank_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.CreateSecondRankRequest,
    ) -> open_search_20171225_models.CreateSecondRankResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_sort_script_with_options(app_group_identity, app_version_id, request, headers, runtime)

    async def create_sort_script_async(
        self,
        app_group_identity: str,
        app_version_id: str,
        request: open_search_20171225_models.CreateSortScriptRequest,
    ) -> open_search_20171225_models.CreateSortScriptResponse:
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
        ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=OpenSearch\\&api=CreateUserAnalyzer\\&type=ROA\\&version=2017-12-25)
        
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
        ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=OpenSearch\\&api=CreateUserAnalyzer\\&type=ROA\\&version=2017-12-25)
        
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
        ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=OpenSearch\\&api=CreateUserAnalyzer\\&type=ROA\\&version=2017-12-25)
        
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
        ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=OpenSearch\\&api=CreateUserAnalyzer\\&type=ROA\\&version=2017-12-25)
        
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_abtest_group_with_options(app_group_identity, scene_id, group_id, headers, runtime)

    async def delete_abtest_group_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
    ) -> open_search_20171225_models.DeleteABTestGroupResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_abtest_scene_with_options(app_group_identity, scene_id, headers, runtime)

    async def delete_abtest_scene_async(
        self,
        app_group_identity: str,
        scene_id: str,
    ) -> open_search_20171225_models.DeleteABTestSceneResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_function_instance_with_options(app_group_identity, function_name, instance_name, headers, runtime)

    async def delete_function_instance_async(
        self,
        app_group_identity: str,
        function_name: str,
        instance_name: str,
    ) -> open_search_20171225_models.DeleteFunctionInstanceResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_function_resource_with_options(app_group_identity, function_name, resource_name, headers, runtime)

    async def delete_function_resource_async(
        self,
        app_group_identity: str,
        function_name: str,
        resource_name: str,
    ) -> open_search_20171225_models.DeleteFunctionResourceResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_sort_script_with_options(app_group_identity, script_name, app_version_id, headers, runtime)

    async def delete_sort_script_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
    ) -> open_search_20171225_models.DeleteSortScriptResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_abtest_group_with_options(app_group_identity, scene_id, group_id, headers, runtime)

    async def describe_abtest_group_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
    ) -> open_search_20171225_models.DescribeABTestGroupResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_abtest_scene_with_options(app_group_identity, scene_id, headers, runtime)

    async def describe_abtest_scene_async(
        self,
        app_group_identity: str,
        scene_id: str,
    ) -> open_search_20171225_models.DescribeABTestSceneResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_app_with_options(app_group_identity, app_id, headers, runtime)

    async def describe_app_async(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> open_search_20171225_models.DescribeAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_app_with_options_async(app_group_identity, app_id, headers, runtime)

    def describe_app_group_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeAppGroupResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_app_group_with_options(app_group_identity, headers, runtime)

    async def describe_app_group_async(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.DescribeAppGroupResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_app_statistics_with_options(app_group_identity, app_id, headers, runtime)

    async def describe_app_statistics_async(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> open_search_20171225_models.DescribeAppStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_app_statistics_with_options_async(app_group_identity, app_id, headers, runtime)

    def describe_apps_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeAppsResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_apps_with_options(app_group_identity, headers, runtime)

    async def describe_apps_async(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.DescribeAppsResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_data_collction_with_options(app_group_identity, data_collection_identity, headers, runtime)

    async def describe_data_collction_async(
        self,
        app_group_identity: str,
        data_collection_identity: str,
    ) -> open_search_20171225_models.DescribeDataCollctionResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_first_rank_with_options(app_group_identity, app_id, name, headers, runtime)

    async def describe_first_rank_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> open_search_20171225_models.DescribeFirstRankResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_first_rank_with_options_async(app_group_identity, app_id, name, headers, runtime)

    def describe_intervention_dictionary_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeInterventionDictionaryResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_intervention_dictionary_with_options(name, headers, runtime)

    async def describe_intervention_dictionary_async(
        self,
        name: str,
    ) -> open_search_20171225_models.DescribeInterventionDictionaryResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_query_processor_with_options(app_group_identity, app_id, name, headers, runtime)

    async def describe_query_processor_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> open_search_20171225_models.DescribeQueryProcessorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_query_processor_with_options_async(app_group_identity, app_id, name, headers, runtime)

    def describe_regions_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeRegionsResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(headers, runtime)

    async def describe_regions_async(self) -> open_search_20171225_models.DescribeRegionsResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_scheduled_task_with_options(app_group_identity, task_id, headers, runtime)

    async def describe_scheduled_task_async(
        self,
        app_group_identity: str,
        task_id: str,
    ) -> open_search_20171225_models.DescribeScheduledTaskResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_second_rank_with_options(app_group_identity, app_id, name, headers, runtime)

    async def describe_second_rank_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> open_search_20171225_models.DescribeSecondRankResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_second_rank_with_options_async(app_group_identity, app_id, name, headers, runtime)

    def describe_slow_query_status_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeSlowQueryStatusResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_slow_query_status_with_options(app_group_identity, headers, runtime)

    async def describe_slow_query_status_async(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.DescribeSlowQueryStatusResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_user_analyzer_with_options(name, request, headers, runtime)

    async def describe_user_analyzer_async(
        self,
        name: str,
        request: open_search_20171225_models.DescribeUserAnalyzerRequest,
    ) -> open_search_20171225_models.DescribeUserAnalyzerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_user_analyzer_with_options_async(name, request, headers, runtime)

    def disable_slow_query_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DisableSlowQueryResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.disable_slow_query_with_options(app_group_identity, headers, runtime)

    async def disable_slow_query_async(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.DisableSlowQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.disable_slow_query_with_options_async(app_group_identity, headers, runtime)

    def enable_slow_query_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.EnableSlowQueryResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_slow_query_with_options(app_group_identity, headers, runtime)

    async def enable_slow_query_async(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.EnableSlowQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.enable_slow_query_with_options_async(app_group_identity, headers, runtime)

    def generate_merged_table_with_options(
        self,
        request: open_search_20171225_models.GenerateMergedTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GenerateMergedTableResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_merged_table_with_options(request, headers, runtime)

    async def generate_merged_table_async(
        self,
        request: open_search_20171225_models.GenerateMergedTableRequest,
    ) -> open_search_20171225_models.GenerateMergedTableResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_domain_with_options(domain_name, request, headers, runtime)

    async def get_domain_async(
        self,
        domain_name: str,
        request: open_search_20171225_models.GetDomainRequest,
    ) -> open_search_20171225_models.GetDomainResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_function_current_version_with_options(function_name, request, headers, runtime)

    async def get_function_current_version_async(
        self,
        function_name: str,
        request: open_search_20171225_models.GetFunctionCurrentVersionRequest,
    ) -> open_search_20171225_models.GetFunctionCurrentVersionResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_function_default_instance_with_options(app_group_identity, function_name, headers, runtime)

    async def get_function_default_instance_async(
        self,
        app_group_identity: str,
        function_name: str,
    ) -> open_search_20171225_models.GetFunctionDefaultInstanceResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_function_version_with_options(function_name, version_id, headers, runtime)

    async def get_function_version_async(
        self,
        function_name: str,
        version_id: str,
    ) -> open_search_20171225_models.GetFunctionVersionResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_script_file_names_with_options(app_group_identity, app_version_id, script_name, headers, runtime)

    async def get_script_file_names_async(
        self,
        app_group_identity: str,
        app_version_id: str,
        script_name: str,
    ) -> open_search_20171225_models.GetScriptFileNamesResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_search_strategy_with_options(app_group_identity, app_id, strategy_name, headers, runtime)

    async def get_search_strategy_async(
        self,
        app_group_identity: str,
        app_id: str,
        strategy_name: str,
    ) -> open_search_20171225_models.GetSearchStrategyResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_sort_script_with_options(app_group_identity, script_name, app_version_id, headers, runtime)

    async def get_sort_script_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
    ) -> open_search_20171225_models.GetSortScriptResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_abtest_experiments_with_options(app_group_identity, scene_id, group_id, headers, runtime)

    async def list_abtest_experiments_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
    ) -> open_search_20171225_models.ListABTestExperimentsResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_abtest_groups_with_options(app_group_identity, scene_id, headers, runtime)

    async def list_abtest_groups_async(
        self,
        app_group_identity: str,
        scene_id: str,
    ) -> open_search_20171225_models.ListABTestGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_abtest_groups_with_options_async(app_group_identity, scene_id, headers, runtime)

    def list_abtest_scenes_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListABTestScenesResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_abtest_scenes_with_options(app_group_identity, headers, runtime)

    async def list_abtest_scenes_async(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.ListABTestScenesResponse:
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
        This operation allows you to query applications by application name, instance ID, and application type.
        *   This operation can sort the applications based on their creation time.
        *   This operation supports the parameters for paging.
        
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
        This operation allows you to query applications by application name, instance ID, and application type.
        *   This operation can sort the applications based on their creation time.
        *   This operation supports the parameters for paging.
        
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
        This operation allows you to query applications by application name, instance ID, and application type.
        *   This operation can sort the applications based on their creation time.
        *   This operation supports the parameters for paging.
        
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
        This operation allows you to query applications by application name, instance ID, and application type.
        *   This operation can sort the applications based on their creation time.
        *   This operation supports the parameters for paging.
        
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_collections_with_options(app_group_identity, request, headers, runtime)

    async def list_data_collections_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListDataCollectionsRequest,
    ) -> open_search_20171225_models.ListDataCollectionsResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_source_table_fields_with_options(data_source_type, request, headers, runtime)

    async def list_data_source_table_fields_async(
        self,
        data_source_type: str,
        request: open_search_20171225_models.ListDataSourceTableFieldsRequest,
    ) -> open_search_20171225_models.ListDataSourceTableFieldsResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_source_tables_with_options(data_source_type, request, headers, runtime)

    async def list_data_source_tables_async(
        self,
        data_source_type: str,
        request: open_search_20171225_models.ListDataSourceTablesRequest,
    ) -> open_search_20171225_models.ListDataSourceTablesResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_first_ranks_with_options(app_group_identity, app_id, headers, runtime)

    async def list_first_ranks_async(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> open_search_20171225_models.ListFirstRanksResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_function_instances_with_options(app_group_identity, function_name, request, headers, runtime)

    async def list_function_instances_async(
        self,
        app_group_identity: str,
        function_name: str,
        request: open_search_20171225_models.ListFunctionInstancesRequest,
    ) -> open_search_20171225_models.ListFunctionInstancesResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_function_resources_with_options(app_group_identity, function_name, request, headers, runtime)

    async def list_function_resources_async(
        self,
        app_group_identity: str,
        function_name: str,
        request: open_search_20171225_models.ListFunctionResourcesRequest,
    ) -> open_search_20171225_models.ListFunctionResourcesResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_function_tasks_with_options_async(app_group_identity, function_name, instance_name, request, headers, runtime)

    def list_intervention_dictionaries_with_options(
        self,
        request: open_search_20171225_models.ListInterventionDictionariesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListInterventionDictionariesResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_intervention_dictionaries_with_options(request, headers, runtime)

    async def list_intervention_dictionaries_async(
        self,
        request: open_search_20171225_models.ListInterventionDictionariesRequest,
    ) -> open_search_20171225_models.ListInterventionDictionariesResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_intervention_dictionary_entries_with_options(name, request, headers, runtime)

    async def list_intervention_dictionary_entries_async(
        self,
        name: str,
        request: open_search_20171225_models.ListInterventionDictionaryEntriesRequest,
    ) -> open_search_20171225_models.ListInterventionDictionaryEntriesResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_intervention_dictionary_ner_results_with_options(name, request, headers, runtime)

    async def list_intervention_dictionary_ner_results_async(
        self,
        name: str,
        request: open_search_20171225_models.ListInterventionDictionaryNerResultsRequest,
    ) -> open_search_20171225_models.ListInterventionDictionaryNerResultsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_intervention_dictionary_ner_results_with_options_async(name, request, headers, runtime)

    def list_intervention_dictionary_related_entities_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListInterventionDictionaryRelatedEntitiesResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_intervention_dictionary_related_entities_with_options(name, headers, runtime)

    async def list_intervention_dictionary_related_entities_async(
        self,
        name: str,
    ) -> open_search_20171225_models.ListInterventionDictionaryRelatedEntitiesResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_proceedings_with_options(app_group_identity, request, headers, runtime)

    async def list_proceedings_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListProceedingsRequest,
    ) -> open_search_20171225_models.ListProceedingsResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_query_processor_analyzer_results_with_options_async(app_group_identity, app_id, name, request, headers, runtime)

    def list_query_processor_ners_with_options(
        self,
        request: open_search_20171225_models.ListQueryProcessorNersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListQueryProcessorNersResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_query_processor_ners_with_options(request, headers, runtime)

    async def list_query_processor_ners_async(
        self,
        request: open_search_20171225_models.ListQueryProcessorNersRequest,
    ) -> open_search_20171225_models.ListQueryProcessorNersResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_query_processors_with_options(app_group_identity, app_id, request, headers, runtime)

    async def list_query_processors_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.ListQueryProcessorsRequest,
    ) -> open_search_20171225_models.ListQueryProcessorsResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_quota_review_tasks_with_options(app_group_identity, request, headers, runtime)

    async def list_quota_review_tasks_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListQuotaReviewTasksRequest,
    ) -> open_search_20171225_models.ListQuotaReviewTasksResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_scheduled_tasks_with_options(app_group_identity, request, headers, runtime)

    async def list_scheduled_tasks_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListScheduledTasksRequest,
    ) -> open_search_20171225_models.ListScheduledTasksResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_search_strategies_with_options(app_group_identity, app_id, headers, runtime)

    async def list_search_strategies_async(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> open_search_20171225_models.ListSearchStrategiesResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_second_ranks_with_options(app_group_identity, app_id, headers, runtime)

    async def list_second_ranks_async(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> open_search_20171225_models.ListSecondRanksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_second_ranks_with_options_async(app_group_identity, app_id, headers, runtime)

    def list_slow_query_categories_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListSlowQueryCategoriesResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_slow_query_categories_with_options(app_group_identity, headers, runtime)

    async def list_slow_query_categories_async(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.ListSlowQueryCategoriesResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_slow_query_queries_with_options(app_group_identity, category_index, headers, runtime)

    async def list_slow_query_queries_async(
        self,
        app_group_identity: str,
        category_index: str,
    ) -> open_search_20171225_models.ListSlowQueryQueriesResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_sort_expressions_with_options(app_group_identity, app_id, headers, runtime)

    async def list_sort_expressions_async(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> open_search_20171225_models.ListSortExpressionsResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_sort_scripts_with_options(app_group_identity, app_version_id, headers, runtime)

    async def list_sort_scripts_async(
        self,
        app_group_identity: str,
        app_version_id: str,
    ) -> open_search_20171225_models.ListSortScriptsResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_statistic_logs_with_options(app_group_identity, module_name, request, headers, runtime)

    async def list_statistic_logs_async(
        self,
        app_group_identity: str,
        module_name: str,
        request: open_search_20171225_models.ListStatisticLogsRequest,
    ) -> open_search_20171225_models.ListStatisticLogsResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_statistic_report_with_options(app_group_identity, module_name, request, headers, runtime)

    async def list_statistic_report_async(
        self,
        app_group_identity: str,
        module_name: str,
        request: open_search_20171225_models.ListStatisticReportRequest,
    ) -> open_search_20171225_models.ListStatisticReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_statistic_report_with_options_async(app_group_identity, module_name, request, headers, runtime)

    def list_tag_resources_with_options(
        self,
        tmp_req: open_search_20171225_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListTagResourcesResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    async def list_tag_resources_async(
        self,
        request: open_search_20171225_models.ListTagResourcesRequest,
    ) -> open_search_20171225_models.ListTagResourcesResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_user_analyzer_entries_with_options(name, request, headers, runtime)

    async def list_user_analyzer_entries_async(
        self,
        name: str,
        request: open_search_20171225_models.ListUserAnalyzerEntriesRequest,
    ) -> open_search_20171225_models.ListUserAnalyzerEntriesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_user_analyzer_entries_with_options_async(name, request, headers, runtime)

    def list_user_analyzers_with_options(
        self,
        request: open_search_20171225_models.ListUserAnalyzersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListUserAnalyzersResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_user_analyzers_with_options(request, headers, runtime)

    async def list_user_analyzers_async(
        self,
        request: open_search_20171225_models.ListUserAnalyzersRequest,
    ) -> open_search_20171225_models.ListUserAnalyzersResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_app_group_with_options(app_group_identity, request, headers, runtime)

    async def modify_app_group_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ModifyAppGroupRequest,
    ) -> open_search_20171225_models.ModifyAppGroupResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_app_group_quota_with_options(app_group_identity, request, headers, runtime)

    async def modify_app_group_quota_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ModifyAppGroupQuotaRequest,
    ) -> open_search_20171225_models.ModifyAppGroupQuotaResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_scheduled_task_with_options(app_group_identity, task_id, request, headers, runtime)

    async def modify_scheduled_task_async(
        self,
        app_group_identity: str,
        task_id: str,
        request: open_search_20171225_models.ModifyScheduledTaskRequest,
    ) -> open_search_20171225_models.ModifyScheduledTaskResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_intervention_dictionary_entries_with_options(name, request, headers, runtime)

    async def push_intervention_dictionary_entries_async(
        self,
        name: str,
        request: open_search_20171225_models.PushInterventionDictionaryEntriesRequest,
    ) -> open_search_20171225_models.PushInterventionDictionaryEntriesResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_user_analyzer_entries_with_options(name, request, headers, runtime)

    async def push_user_analyzer_entries_async(
        self,
        name: str,
        request: open_search_20171225_models.PushUserAnalyzerEntriesRequest,
    ) -> open_search_20171225_models.PushUserAnalyzerEntriesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.push_user_analyzer_entries_with_options_async(name, request, headers, runtime)

    def rank_preview_query_with_options(
        self,
        app_group_identity: str,
        model_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RankPreviewQueryResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RankPreviewQuery',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/algorithm/models/{OpenApiUtilClient.get_encode_param(model_name)}/actions/query-rank',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RankPreviewQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def rank_preview_query_with_options_async(
        self,
        app_group_identity: str,
        model_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RankPreviewQueryResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RankPreviewQuery',
            version='2017-12-25',
            protocol='HTTPS',
            pathname=f'/v4/openapi/app-groups/{OpenApiUtilClient.get_encode_param(app_group_identity)}/algorithm/models/{OpenApiUtilClient.get_encode_param(model_name)}/actions/query-rank',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RankPreviewQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rank_preview_query(
        self,
        app_group_identity: str,
        model_name: str,
    ) -> open_search_20171225_models.RankPreviewQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rank_preview_query_with_options(app_group_identity, model_name, headers, runtime)

    async def rank_preview_query_async(
        self,
        app_group_identity: str,
        model_name: str,
    ) -> open_search_20171225_models.RankPreviewQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.rank_preview_query_with_options_async(app_group_identity, model_name, headers, runtime)

    def release_sort_script_with_options(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ReleaseSortScriptResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.release_sort_script_with_options(app_group_identity, script_name, app_version_id, headers, runtime)

    async def release_sort_script_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
    ) -> open_search_20171225_models.ReleaseSortScriptResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_app_with_options(app_group_identity, app_id, headers, runtime)

    async def remove_app_async(
        self,
        app_group_identity: str,
        app_id: str,
    ) -> open_search_20171225_models.RemoveAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_app_with_options_async(app_group_identity, app_id, headers, runtime)

    def remove_app_group_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RemoveAppGroupResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_app_group_with_options(app_group_identity, headers, runtime)

    async def remove_app_group_async(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.RemoveAppGroupResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_data_collection_with_options(app_group_identity, data_collection_identity, headers, runtime)

    async def remove_data_collection_async(
        self,
        app_group_identity: str,
        data_collection_identity: str,
    ) -> open_search_20171225_models.RemoveDataCollectionResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_first_rank_with_options(app_group_identity, app_id, name, headers, runtime)

    async def remove_first_rank_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> open_search_20171225_models.RemoveFirstRankResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_first_rank_with_options_async(app_group_identity, app_id, name, headers, runtime)

    def remove_intervention_dictionary_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RemoveInterventionDictionaryResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_intervention_dictionary_with_options(name, headers, runtime)

    async def remove_intervention_dictionary_async(
        self,
        name: str,
    ) -> open_search_20171225_models.RemoveInterventionDictionaryResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_query_processor_with_options(app_group_identity, app_id, name, headers, runtime)

    async def remove_query_processor_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> open_search_20171225_models.RemoveQueryProcessorResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_scheduled_task_with_options(app_group_identity, task_id, headers, runtime)

    async def remove_scheduled_task_async(
        self,
        app_group_identity: str,
        task_id: str,
    ) -> open_search_20171225_models.RemoveScheduledTaskResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_search_strategy_with_options(app_group_identity, app_id, strategy_name, headers, runtime)

    async def remove_search_strategy_async(
        self,
        app_group_identity: str,
        app_id: str,
        strategy_name: str,
    ) -> open_search_20171225_models.RemoveSearchStrategyResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_second_rank_with_options(app_group_identity, app_id, name, headers, runtime)

    async def remove_second_rank_async(
        self,
        app_group_identity: str,
        app_id: str,
        name: str,
    ) -> open_search_20171225_models.RemoveSecondRankResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_second_rank_with_options_async(app_group_identity, app_id, name, headers, runtime)

    def remove_user_analyzer_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RemoveUserAnalyzerResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_user_analyzer_with_options(name, headers, runtime)

    async def remove_user_analyzer_async(
        self,
        name: str,
    ) -> open_search_20171225_models.RemoveUserAnalyzerResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.renew_app_group_with_options(app_group_identity, request, headers, runtime)

    async def renew_app_group_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.RenewAppGroupRequest,
    ) -> open_search_20171225_models.RenewAppGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.renew_app_group_with_options_async(app_group_identity, request, headers, runtime)

    def replace_app_group_commodity_code_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ReplaceAppGroupCommodityCodeResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.replace_app_group_commodity_code_with_options(app_group_identity, headers, runtime)

    async def replace_app_group_commodity_code_async(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.ReplaceAppGroupCommodityCodeResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.save_sort_script_file_with_options_async(app_group_identity, script_name, app_version_id, file_name, request, headers, runtime)

    def start_slow_query_analyzer_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.StartSlowQueryAnalyzerResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_slow_query_analyzer_with_options(app_group_identity, headers, runtime)

    async def start_slow_query_analyzer_async(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.StartSlowQueryAnalyzerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_slow_query_analyzer_with_options_async(app_group_identity, headers, runtime)

    def tag_resources_with_options(
        self,
        request: open_search_20171225_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.TagResourcesResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    async def tag_resources_async(
        self,
        request: open_search_20171225_models.TagResourcesRequest,
    ) -> open_search_20171225_models.TagResourcesResponse:
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
        The ID of the request.
        
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
        The ID of the request.
        
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
        The ID of the request.
        
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
        The ID of the request.
        
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.unbind_es_instance_with_options(app_group_identity, headers, runtime)

    async def unbind_es_instance_async(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.UnbindEsInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.unbind_es_instance_with_options_async(app_group_identity, headers, runtime)

    def untag_resources_with_options(
        self,
        tmp_req: open_search_20171225_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UntagResourcesResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.untag_resources_with_options(request, headers, runtime)

    async def untag_resources_async(
        self,
        request: open_search_20171225_models.UntagResourcesRequest,
    ) -> open_search_20171225_models.UntagResourcesResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_abtest_scene_with_options(app_group_identity, scene_id, request, headers, runtime)

    async def update_abtest_scene_async(
        self,
        app_group_identity: str,
        scene_id: str,
        request: open_search_20171225_models.UpdateABTestSceneRequest,
    ) -> open_search_20171225_models.UpdateABTestSceneResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_fetch_fields_with_options(app_group_identity, app_id, request, headers, runtime)

    async def update_fetch_fields_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.UpdateFetchFieldsRequest,
    ) -> open_search_20171225_models.UpdateFetchFieldsResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_function_default_instance_with_options(app_group_identity, function_name, request, headers, runtime)

    async def update_function_default_instance_async(
        self,
        app_group_identity: str,
        function_name: str,
        request: open_search_20171225_models.UpdateFunctionDefaultInstanceRequest,
    ) -> open_search_20171225_models.UpdateFunctionDefaultInstanceResponse:
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
        You can call this operation to modify the description of a sort script.
        
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
        You can call this operation to modify the description of a sort script.
        
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
        You can call this operation to modify the description of a sort script.
        
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
        You can call this operation to modify the description of a sort script.
        
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_summaries_with_options(app_group_identity, app_id, request, headers, runtime)

    async def update_summaries_async(
        self,
        app_group_identity: str,
        app_id: str,
        request: open_search_20171225_models.UpdateSummariesRequest,
    ) -> open_search_20171225_models.UpdateSummariesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_summaries_with_options_async(app_group_identity, app_id, request, headers, runtime)

    def validate_data_sources_with_options(
        self,
        request: open_search_20171225_models.ValidateDataSourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ValidateDataSourcesResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.validate_data_sources_with_options(request, headers, runtime)

    async def validate_data_sources_async(
        self,
        request: open_search_20171225_models.ValidateDataSourcesRequest,
    ) -> open_search_20171225_models.ValidateDataSourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.validate_data_sources_with_options_async(request, headers, runtime)
