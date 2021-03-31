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
        return TeaCore.from_map(
            open_search_20171225_models.CompileSortScriptResponse(),
            self.do_roarequest('CompileSortScript', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_version_id}/sort-scripts/{script_name}/actions/compiling', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.CompileSortScriptResponse(),
            await self.do_roarequest_async('CompileSortScript', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_version_id}/sort-scripts/{script_name}/actions/compiling', 'json', req, runtime)
        )

    def create_abtest_experiment(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
    ) -> open_search_20171225_models.CreateABTestExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_abtest_experiment_with_options(app_group_identity, scene_id, group_id, headers, runtime)

    async def create_abtest_experiment_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
    ) -> open_search_20171225_models.CreateABTestExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_abtest_experiment_with_options_async(app_group_identity, scene_id, group_id, headers, runtime)

    def create_abtest_experiment_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateABTestExperimentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateABTestExperimentResponse(),
            self.do_roarequest('CreateABTestExperiment', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}/groups/{group_id}/experiments', 'json', req, runtime)
        )

    async def create_abtest_experiment_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateABTestExperimentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateABTestExperimentResponse(),
            await self.do_roarequest_async('CreateABTestExperiment', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}/groups/{group_id}/experiments', 'json', req, runtime)
        )

    def create_abtest_group(
        self,
        app_group_identity: str,
        scene_id: str,
    ) -> open_search_20171225_models.CreateABTestGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_abtest_group_with_options(app_group_identity, scene_id, headers, runtime)

    async def create_abtest_group_async(
        self,
        app_group_identity: str,
        scene_id: str,
    ) -> open_search_20171225_models.CreateABTestGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_abtest_group_with_options_async(app_group_identity, scene_id, headers, runtime)

    def create_abtest_group_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateABTestGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateABTestGroupResponse(),
            self.do_roarequest('CreateABTestGroup', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}/groups', 'json', req, runtime)
        )

    async def create_abtest_group_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateABTestGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateABTestGroupResponse(),
            await self.do_roarequest_async('CreateABTestGroup', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}/groups', 'json', req, runtime)
        )

    def create_abtest_scene(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.CreateABTestSceneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_abtest_scene_with_options(app_group_identity, headers, runtime)

    async def create_abtest_scene_async(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.CreateABTestSceneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_abtest_scene_with_options_async(app_group_identity, headers, runtime)

    def create_abtest_scene_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateABTestSceneResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateABTestSceneResponse(),
            self.do_roarequest('CreateABTestScene', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes', 'json', req, runtime)
        )

    async def create_abtest_scene_with_options_async(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateABTestSceneResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateABTestSceneResponse(),
            await self.do_roarequest_async('CreateABTestScene', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes', 'json', req, runtime)
        )

    def create_app(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.CreateAppRequest,
    ) -> open_search_20171225_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_app_with_options(app_group_identity, request, headers, runtime)

    async def create_app_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.CreateAppRequest,
    ) -> open_search_20171225_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_app_with_options_async(app_group_identity, request, headers, runtime)

    def create_app_with_options(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.CreateAppRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateAppResponse(),
            self.do_roarequest('CreateApp', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps', 'json', req, runtime)
        )

    async def create_app_with_options_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.CreateAppRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateAppResponse(),
            await self.do_roarequest_async('CreateApp', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps', 'json', req, runtime)
        )

    def create_app_group(self) -> open_search_20171225_models.CreateAppGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_app_group_with_options(headers, runtime)

    async def create_app_group_async(self) -> open_search_20171225_models.CreateAppGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_app_group_with_options_async(headers, runtime)

    def create_app_group_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateAppGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateAppGroupResponse(),
            self.do_roarequest('CreateAppGroup', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups', 'json', req, runtime)
        )

    async def create_app_group_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateAppGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateAppGroupResponse(),
            await self.do_roarequest_async('CreateAppGroup', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups', 'json', req, runtime)
        )

    def create_data_collection(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.CreateDataCollectionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_data_collection_with_options(app_group_identity, headers, runtime)

    async def create_data_collection_async(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.CreateDataCollectionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_data_collection_with_options_async(app_group_identity, headers, runtime)

    def create_data_collection_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateDataCollectionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateDataCollectionResponse(),
            self.do_roarequest('CreateDataCollection', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/data-collections', 'json', req, runtime)
        )

    async def create_data_collection_with_options_async(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateDataCollectionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateDataCollectionResponse(),
            await self.do_roarequest_async('CreateDataCollection', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/data-collections', 'json', req, runtime)
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
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateFirstRankResponse(),
            self.do_roarequest('CreateFirstRank', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/first-ranks', 'json', req, runtime)
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
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateFirstRankResponse(),
            await self.do_roarequest_async('CreateFirstRank', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/first-ranks', 'json', req, runtime)
        )

    def create_intervention_dictionary(self) -> open_search_20171225_models.CreateInterventionDictionaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_intervention_dictionary_with_options(headers, runtime)

    async def create_intervention_dictionary_async(self) -> open_search_20171225_models.CreateInterventionDictionaryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_intervention_dictionary_with_options_async(headers, runtime)

    def create_intervention_dictionary_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateInterventionDictionaryResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateInterventionDictionaryResponse(),
            self.do_roarequest('CreateInterventionDictionary', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/intervention-dictionaries', 'json', req, runtime)
        )

    async def create_intervention_dictionary_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateInterventionDictionaryResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateInterventionDictionaryResponse(),
            await self.do_roarequest_async('CreateInterventionDictionary', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/intervention-dictionaries', 'json', req, runtime)
        )

    def create_model(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.CreateModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_model_with_options(app_group_identity, headers, runtime)

    async def create_model_async(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.CreateModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_model_with_options_async(app_group_identity, headers, runtime)

    def create_model_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateModelResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateModelResponse(),
            self.do_roarequest('CreateModel', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/algorithm/models', 'json', req, runtime)
        )

    async def create_model_with_options_async(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateModelResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateModelResponse(),
            await self.do_roarequest_async('CreateModel', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/algorithm/models', 'json', req, runtime)
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
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateQueryProcessorResponse(),
            self.do_roarequest('CreateQueryProcessor', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/query-processors', 'json', req, runtime)
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
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateQueryProcessorResponse(),
            await self.do_roarequest_async('CreateQueryProcessor', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/query-processors', 'json', req, runtime)
        )

    def create_scheduled_task(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.CreateScheduledTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_scheduled_task_with_options(app_group_identity, headers, runtime)

    async def create_scheduled_task_async(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.CreateScheduledTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_scheduled_task_with_options_async(app_group_identity, headers, runtime)

    def create_scheduled_task_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateScheduledTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateScheduledTaskResponse(),
            self.do_roarequest('CreateScheduledTask', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scheduled-tasks', 'json', req, runtime)
        )

    async def create_scheduled_task_with_options_async(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateScheduledTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateScheduledTaskResponse(),
            await self.do_roarequest_async('CreateScheduledTask', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scheduled-tasks', 'json', req, runtime)
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
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateSecondRankResponse(),
            self.do_roarequest('CreateSecondRank', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/second-ranks', 'json', req, runtime)
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
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateSecondRankResponse(),
            await self.do_roarequest_async('CreateSecondRank', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/second-ranks', 'json', req, runtime)
        )

    def create_sort_script(
        self,
        app_group_identity: str,
        app_version_id: str,
    ) -> open_search_20171225_models.CreateSortScriptResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_sort_script_with_options(app_group_identity, app_version_id, headers, runtime)

    async def create_sort_script_async(
        self,
        app_group_identity: str,
        app_version_id: str,
    ) -> open_search_20171225_models.CreateSortScriptResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_sort_script_with_options_async(app_group_identity, app_version_id, headers, runtime)

    def create_sort_script_with_options(
        self,
        app_group_identity: str,
        app_version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateSortScriptResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateSortScriptResponse(),
            self.do_roarequest('CreateSortScript', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_version_id}/sort-scripts', 'json', req, runtime)
        )

    async def create_sort_script_with_options_async(
        self,
        app_group_identity: str,
        app_version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateSortScriptResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateSortScriptResponse(),
            await self.do_roarequest_async('CreateSortScript', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_version_id}/sort-scripts', 'json', req, runtime)
        )

    def create_user_analyzer(self) -> open_search_20171225_models.CreateUserAnalyzerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_user_analyzer_with_options(headers, runtime)

    async def create_user_analyzer_async(self) -> open_search_20171225_models.CreateUserAnalyzerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_user_analyzer_with_options_async(headers, runtime)

    def create_user_analyzer_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateUserAnalyzerResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateUserAnalyzerResponse(),
            self.do_roarequest('CreateUserAnalyzer', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/user-analyzers', 'json', req, runtime)
        )

    async def create_user_analyzer_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.CreateUserAnalyzerResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateUserAnalyzerResponse(),
            await self.do_roarequest_async('CreateUserAnalyzer', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/user-analyzers', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DeleteABTestExperimentResponse(),
            self.do_roarequest('DeleteABTestExperiment', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}/groups/{group_id}/experiments/{experiment_id}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DeleteABTestExperimentResponse(),
            await self.do_roarequest_async('DeleteABTestExperiment', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}/groups/{group_id}/experiments/{experiment_id}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DeleteABTestGroupResponse(),
            self.do_roarequest('DeleteABTestGroup', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}/groups/{group_id}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DeleteABTestGroupResponse(),
            await self.do_roarequest_async('DeleteABTestGroup', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}/groups/{group_id}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DeleteABTestSceneResponse(),
            self.do_roarequest('DeleteABTestScene', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DeleteABTestSceneResponse(),
            await self.do_roarequest_async('DeleteABTestScene', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}', 'json', req, runtime)
        )

    def delete_model(
        self,
        app_group_identity: str,
        model_name: str,
    ) -> open_search_20171225_models.DeleteModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_model_with_options(app_group_identity, model_name, headers, runtime)

    async def delete_model_async(
        self,
        app_group_identity: str,
        model_name: str,
    ) -> open_search_20171225_models.DeleteModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_model_with_options_async(app_group_identity, model_name, headers, runtime)

    def delete_model_with_options(
        self,
        app_group_identity: str,
        model_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DeleteModelResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.DeleteModelResponse(),
            self.do_roarequest('DeleteModel', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/algorithm/models/{model_name}', 'json', req, runtime)
        )

    async def delete_model_with_options_async(
        self,
        app_group_identity: str,
        model_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DeleteModelResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.DeleteModelResponse(),
            await self.do_roarequest_async('DeleteModel', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/algorithm/models/{model_name}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DeleteSortScriptResponse(),
            self.do_roarequest('DeleteSortScript', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_version_id}/sort-scripts/{script_name}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DeleteSortScriptResponse(),
            await self.do_roarequest_async('DeleteSortScript', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_version_id}/sort-scripts/{script_name}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DeleteSortScriptFileResponse(),
            self.do_roarequest('DeleteSortScriptFile', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_version_id}/sort-scripts/{script_name}/files/src/{file_name}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DeleteSortScriptFileResponse(),
            await self.do_roarequest_async('DeleteSortScriptFile', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_version_id}/sort-scripts/{script_name}/files/src/{file_name}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DescribeABTestExperimentResponse(),
            self.do_roarequest('DescribeABTestExperiment', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}/groups/{group_id}/experiments/{experiment_id}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DescribeABTestExperimentResponse(),
            await self.do_roarequest_async('DescribeABTestExperiment', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}/groups/{group_id}/experiments/{experiment_id}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DescribeABTestGroupResponse(),
            self.do_roarequest('DescribeABTestGroup', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}/groups/{group_id}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DescribeABTestGroupResponse(),
            await self.do_roarequest_async('DescribeABTestGroup', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}/groups/{group_id}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DescribeABTestSceneResponse(),
            self.do_roarequest('DescribeABTestScene', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DescribeABTestSceneResponse(),
            await self.do_roarequest_async('DescribeABTestScene', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DescribeAppResponse(),
            self.do_roarequest('DescribeApp', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DescribeAppResponse(),
            await self.do_roarequest_async('DescribeApp', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}', 'json', req, runtime)
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

    def describe_app_group_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeAppGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeAppGroupResponse(),
            self.do_roarequest('DescribeAppGroup', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DescribeAppGroupResponse(),
            await self.do_roarequest_async('DescribeAppGroup', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}', 'json', req, runtime)
        )

    def describe_app_group_data_report(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.DescribeAppGroupDataReportRequest,
    ) -> open_search_20171225_models.DescribeAppGroupDataReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_app_group_data_report_with_options(app_group_identity, request, headers, runtime)

    async def describe_app_group_data_report_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.DescribeAppGroupDataReportRequest,
    ) -> open_search_20171225_models.DescribeAppGroupDataReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_app_group_data_report_with_options_async(app_group_identity, request, headers, runtime)

    def describe_app_group_data_report_with_options(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.DescribeAppGroupDataReportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeAppGroupDataReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeAppGroupDataReportResponse(),
            self.do_roarequest('DescribeAppGroupDataReport', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/data-report', 'json', req, runtime)
        )

    async def describe_app_group_data_report_with_options_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.DescribeAppGroupDataReportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeAppGroupDataReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeAppGroupDataReportResponse(),
            await self.do_roarequest_async('DescribeAppGroupDataReport', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/data-report', 'json', req, runtime)
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

    def describe_apps_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeAppsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeAppsResponse(),
            self.do_roarequest('DescribeApps', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DescribeAppsResponse(),
            await self.do_roarequest_async('DescribeApps', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DescribeAppStatisticsResponse(),
            self.do_roarequest('DescribeAppStatistics', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/statistics', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DescribeAppStatisticsResponse(),
            await self.do_roarequest_async('DescribeAppStatistics', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/statistics', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DescribeDataCollctionResponse(),
            self.do_roarequest('DescribeDataCollction', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/data-collections/{data_collection_identity}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DescribeDataCollctionResponse(),
            await self.do_roarequest_async('DescribeDataCollction', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/data-collections/{data_collection_identity}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DescribeFirstRankResponse(),
            self.do_roarequest('DescribeFirstRank', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/first-ranks/{name}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DescribeFirstRankResponse(),
            await self.do_roarequest_async('DescribeFirstRank', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/first-ranks/{name}', 'json', req, runtime)
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

    def describe_intervention_dictionary_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeInterventionDictionaryResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeInterventionDictionaryResponse(),
            self.do_roarequest('DescribeInterventionDictionary', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/intervention-dictionaries/{name}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DescribeInterventionDictionaryResponse(),
            await self.do_roarequest_async('DescribeInterventionDictionary', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/intervention-dictionaries/{name}', 'json', req, runtime)
        )

    def describe_model(
        self,
        app_group_identity: str,
        model_name: str,
    ) -> open_search_20171225_models.DescribeModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_model_with_options(app_group_identity, model_name, headers, runtime)

    async def describe_model_async(
        self,
        app_group_identity: str,
        model_name: str,
    ) -> open_search_20171225_models.DescribeModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_model_with_options_async(app_group_identity, model_name, headers, runtime)

    def describe_model_with_options(
        self,
        app_group_identity: str,
        model_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeModelResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeModelResponse(),
            self.do_roarequest('DescribeModel', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/algorithm/models/{model_name}', 'json', req, runtime)
        )

    async def describe_model_with_options_async(
        self,
        app_group_identity: str,
        model_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeModelResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeModelResponse(),
            await self.do_roarequest_async('DescribeModel', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/algorithm/models/{model_name}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DescribeQueryProcessorResponse(),
            self.do_roarequest('DescribeQueryProcessor', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/query-processors/{name}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DescribeQueryProcessorResponse(),
            await self.do_roarequest_async('DescribeQueryProcessor', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/query-processors/{name}', 'json', req, runtime)
        )

    def describe_region(self) -> open_search_20171225_models.DescribeRegionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_region_with_options(headers, runtime)

    async def describe_region_async(self) -> open_search_20171225_models.DescribeRegionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_region_with_options_async(headers, runtime)

    def describe_region_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeRegionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeRegionResponse(),
            self.do_roarequest('DescribeRegion', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/region', 'json', req, runtime)
        )

    async def describe_region_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeRegionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeRegionResponse(),
            await self.do_roarequest_async('DescribeRegion', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/region', 'json', req, runtime)
        )

    def describe_regions(self) -> open_search_20171225_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(headers, runtime)

    async def describe_regions_async(self) -> open_search_20171225_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_regions_with_options_async(headers, runtime)

    def describe_regions_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeRegionsResponse(),
            self.do_roarequest('DescribeRegions', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/regions', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeRegionsResponse(),
            await self.do_roarequest_async('DescribeRegions', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/regions', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DescribeScheduledTaskResponse(),
            self.do_roarequest('DescribeScheduledTask', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scheduled-tasks/{task_id}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DescribeScheduledTaskResponse(),
            await self.do_roarequest_async('DescribeScheduledTask', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scheduled-tasks/{task_id}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DescribeSecondRankResponse(),
            self.do_roarequest('DescribeSecondRank', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/second-ranks/{name}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DescribeSecondRankResponse(),
            await self.do_roarequest_async('DescribeSecondRank', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/second-ranks/{name}', 'json', req, runtime)
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

    def describe_slow_query_status_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DescribeSlowQueryStatusResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeSlowQueryStatusResponse(),
            self.do_roarequest('DescribeSlowQueryStatus', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/optimizers/slow-query', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DescribeSlowQueryStatusResponse(),
            await self.do_roarequest_async('DescribeSlowQueryStatus', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/optimizers/slow-query', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DescribeUserAnalyzerResponse(),
            self.do_roarequest('DescribeUserAnalyzer', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/user-analyzers/{name}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DescribeUserAnalyzerResponse(),
            await self.do_roarequest_async('DescribeUserAnalyzer', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/user-analyzers/{name}', 'json', req, runtime)
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

    def disable_slow_query_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.DisableSlowQueryResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.DisableSlowQueryResponse(),
            self.do_roarequest('DisableSlowQuery', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/optimizers/slow-query/actions/disable', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.DisableSlowQueryResponse(),
            await self.do_roarequest_async('DisableSlowQuery', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/optimizers/slow-query/actions/disable', 'json', req, runtime)
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

    def enable_slow_query_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.EnableSlowQueryResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.EnableSlowQueryResponse(),
            self.do_roarequest('EnableSlowQuery', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/optimizers/slow-query/actions/enable', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.EnableSlowQueryResponse(),
            await self.do_roarequest_async('EnableSlowQuery', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/optimizers/slow-query/actions/enable', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.GetDomainResponse(),
            self.do_roarequest('GetDomain', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/domains/{domain_name}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.GetDomainResponse(),
            await self.do_roarequest_async('GetDomain', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/domains/{domain_name}', 'json', req, runtime)
        )

    def get_model_progress(
        self,
        app_group_identity: str,
        model_name: str,
    ) -> open_search_20171225_models.GetModelProgressResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_model_progress_with_options(app_group_identity, model_name, headers, runtime)

    async def get_model_progress_async(
        self,
        app_group_identity: str,
        model_name: str,
    ) -> open_search_20171225_models.GetModelProgressResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_model_progress_with_options_async(app_group_identity, model_name, headers, runtime)

    def get_model_progress_with_options(
        self,
        app_group_identity: str,
        model_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetModelProgressResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetModelProgressResponse(),
            self.do_roarequest('GetModelProgress', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/algorithm/models/{model_name}/progress', 'json', req, runtime)
        )

    async def get_model_progress_with_options_async(
        self,
        app_group_identity: str,
        model_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetModelProgressResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetModelProgressResponse(),
            await self.do_roarequest_async('GetModelProgress', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/algorithm/models/{model_name}/progress', 'json', req, runtime)
        )

    def get_model_report(
        self,
        app_group_identity: str,
        model_name: str,
    ) -> open_search_20171225_models.GetModelReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_model_report_with_options(app_group_identity, model_name, headers, runtime)

    async def get_model_report_async(
        self,
        app_group_identity: str,
        model_name: str,
    ) -> open_search_20171225_models.GetModelReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_model_report_with_options_async(app_group_identity, model_name, headers, runtime)

    def get_model_report_with_options(
        self,
        app_group_identity: str,
        model_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetModelReportResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetModelReportResponse(),
            self.do_roarequest('GetModelReport', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/algorithm/models/{model_name}/report', 'json', req, runtime)
        )

    async def get_model_report_with_options_async(
        self,
        app_group_identity: str,
        model_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetModelReportResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetModelReportResponse(),
            await self.do_roarequest_async('GetModelReport', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/algorithm/models/{model_name}/report', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.GetScriptFileNamesResponse(),
            self.do_roarequest('GetScriptFileNames', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_version_id}/sort-scripts/{script_name}/file-names', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.GetScriptFileNamesResponse(),
            await self.do_roarequest_async('GetScriptFileNames', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_version_id}/sort-scripts/{script_name}/file-names', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.GetSortScriptResponse(),
            self.do_roarequest('GetSortScript', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_version_id}/sort-scripts/{script_name}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.GetSortScriptResponse(),
            await self.do_roarequest_async('GetSortScript', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_version_id}/sort-scripts/{script_name}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.GetSortScriptFileResponse(),
            self.do_roarequest('GetSortScriptFile', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_version_id}/sort-scripts/{script_name}/files/src/{file_name}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.GetSortScriptFileResponse(),
            await self.do_roarequest_async('GetSortScriptFile', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_version_id}/sort-scripts/{script_name}/files/src/{file_name}', 'json', req, runtime)
        )

    def get_validation_error(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.GetValidationErrorRequest,
    ) -> open_search_20171225_models.GetValidationErrorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_validation_error_with_options(app_group_identity, request, headers, runtime)

    async def get_validation_error_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.GetValidationErrorRequest,
    ) -> open_search_20171225_models.GetValidationErrorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_validation_error_with_options_async(app_group_identity, request, headers, runtime)

    def get_validation_error_with_options(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.GetValidationErrorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetValidationErrorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.error_code):
            query['errorCode'] = request.error_code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetValidationErrorResponse(),
            self.do_roarequest('GetValidationError', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/algorithm/data/validation-error', 'json', req, runtime)
        )

    async def get_validation_error_with_options_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.GetValidationErrorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetValidationErrorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.error_code):
            query['errorCode'] = request.error_code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetValidationErrorResponse(),
            await self.do_roarequest_async('GetValidationError', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/algorithm/data/validation-error', 'json', req, runtime)
        )

    def get_validation_report(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.GetValidationReportRequest,
    ) -> open_search_20171225_models.GetValidationReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_validation_report_with_options(app_group_identity, request, headers, runtime)

    async def get_validation_report_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.GetValidationReportRequest,
    ) -> open_search_20171225_models.GetValidationReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_validation_report_with_options_async(app_group_identity, request, headers, runtime)

    def get_validation_report_with_options(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.GetValidationReportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetValidationReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetValidationReportResponse(),
            self.do_roarequest('GetValidationReport', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/algorithm/data/validation-report', 'json', req, runtime)
        )

    async def get_validation_report_with_options_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.GetValidationReportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.GetValidationReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetValidationReportResponse(),
            await self.do_roarequest_async('GetValidationReport', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/algorithm/data/validation-report', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ListABTestExperimentsResponse(),
            self.do_roarequest('ListABTestExperiments', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}/groups/{group_id}/experiments', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ListABTestExperimentsResponse(),
            await self.do_roarequest_async('ListABTestExperiments', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}/groups/{group_id}/experiments', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ListABTestFixedFlowDividersResponse(),
            self.do_roarequest('ListABTestFixedFlowDividers', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}/groups/{group_id}/experiments/{experiment_id}/fixed-flow-dividers', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ListABTestFixedFlowDividersResponse(),
            await self.do_roarequest_async('ListABTestFixedFlowDividers', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}/groups/{group_id}/experiments/{experiment_id}/fixed-flow-dividers', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ListABTestGroupsResponse(),
            self.do_roarequest('ListABTestGroups', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}/groups', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ListABTestGroupsResponse(),
            await self.do_roarequest_async('ListABTestGroups', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}/groups', 'json', req, runtime)
        )

    def list_abtest_metrics(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
    ) -> open_search_20171225_models.ListABTestMetricsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_abtest_metrics_with_options(app_group_identity, scene_id, group_id, headers, runtime)

    async def list_abtest_metrics_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
    ) -> open_search_20171225_models.ListABTestMetricsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_abtest_metrics_with_options_async(app_group_identity, scene_id, group_id, headers, runtime)

    def list_abtest_metrics_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListABTestMetricsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListABTestMetricsResponse(),
            self.do_roarequest('ListABTestMetrics', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}/groups/{group_id}/metrics', 'json', req, runtime)
        )

    async def list_abtest_metrics_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListABTestMetricsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListABTestMetricsResponse(),
            await self.do_roarequest_async('ListABTestMetrics', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}/groups/{group_id}/metrics', 'json', req, runtime)
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

    def list_abtest_scenes_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListABTestScenesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListABTestScenesResponse(),
            self.do_roarequest('ListABTestScenes', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ListABTestScenesResponse(),
            await self.do_roarequest_async('ListABTestScenes', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes', 'json', req, runtime)
        )

    def list_app_group_errors(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListAppGroupErrorsRequest,
    ) -> open_search_20171225_models.ListAppGroupErrorsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_app_group_errors_with_options(app_group_identity, request, headers, runtime)

    async def list_app_group_errors_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListAppGroupErrorsRequest,
    ) -> open_search_20171225_models.ListAppGroupErrorsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_app_group_errors_with_options_async(app_group_identity, request, headers, runtime)

    def list_app_group_errors_with_options(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListAppGroupErrorsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListAppGroupErrorsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['appId'] = request.app_id
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.stop_time):
            query['stopTime'] = request.stop_time
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListAppGroupErrorsResponse(),
            self.do_roarequest('ListAppGroupErrors', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/errors', 'json', req, runtime)
        )

    async def list_app_group_errors_with_options_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListAppGroupErrorsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListAppGroupErrorsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['appId'] = request.app_id
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.stop_time):
            query['stopTime'] = request.stop_time
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListAppGroupErrorsResponse(),
            await self.do_roarequest_async('ListAppGroupErrors', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/errors', 'json', req, runtime)
        )

    def list_app_group_metrics(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListAppGroupMetricsRequest,
    ) -> open_search_20171225_models.ListAppGroupMetricsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_app_group_metrics_with_options(app_group_identity, request, headers, runtime)

    async def list_app_group_metrics_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListAppGroupMetricsRequest,
    ) -> open_search_20171225_models.ListAppGroupMetricsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_app_group_metrics_with_options_async(app_group_identity, request, headers, runtime)

    def list_app_group_metrics_with_options(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListAppGroupMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListAppGroupMetricsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.metric_type):
            query['metricType'] = request.metric_type
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.indexes):
            query['indexes'] = request.indexes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListAppGroupMetricsResponse(),
            self.do_roarequest('ListAppGroupMetrics', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/metrics', 'json', req, runtime)
        )

    async def list_app_group_metrics_with_options_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListAppGroupMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListAppGroupMetricsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.metric_type):
            query['metricType'] = request.metric_type
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.indexes):
            query['indexes'] = request.indexes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListAppGroupMetricsResponse(),
            await self.do_roarequest_async('ListAppGroupMetrics', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/metrics', 'json', req, runtime)
        )

    def list_app_groups(
        self,
        request: open_search_20171225_models.ListAppGroupsRequest,
    ) -> open_search_20171225_models.ListAppGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_app_groups_with_options(request, headers, runtime)

    async def list_app_groups_async(
        self,
        request: open_search_20171225_models.ListAppGroupsRequest,
    ) -> open_search_20171225_models.ListAppGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_app_groups_with_options_async(request, headers, runtime)

    def list_app_groups_with_options(
        self,
        request: open_search_20171225_models.ListAppGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListAppGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.sort_by):
            query['sortBy'] = request.sort_by
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListAppGroupsResponse(),
            self.do_roarequest('ListAppGroups', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups', 'json', req, runtime)
        )

    async def list_app_groups_with_options_async(
        self,
        request: open_search_20171225_models.ListAppGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListAppGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.sort_by):
            query['sortBy'] = request.sort_by
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListAppGroupsResponse(),
            await self.do_roarequest_async('ListAppGroups', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups', 'json', req, runtime)
        )

    def list_apps(
        self,
        request: open_search_20171225_models.ListAppsRequest,
    ) -> open_search_20171225_models.ListAppsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_apps_with_options(request, headers, runtime)

    async def list_apps_async(
        self,
        request: open_search_20171225_models.ListAppsRequest,
    ) -> open_search_20171225_models.ListAppsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_apps_with_options_async(request, headers, runtime)

    def list_apps_with_options(
        self,
        request: open_search_20171225_models.ListAppsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group):
            query['group'] = request.group
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListAppsResponse(),
            self.do_roarequest('ListApps', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/apps', 'none', req, runtime)
        )

    async def list_apps_with_options_async(
        self,
        request: open_search_20171225_models.ListAppsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group):
            query['group'] = request.group
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListAppsResponse(),
            await self.do_roarequest_async('ListApps', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/apps', 'none', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ListDataCollectionsResponse(),
            self.do_roarequest('ListDataCollections', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/data-collections', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ListDataCollectionsResponse(),
            await self.do_roarequest_async('ListDataCollections', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/data-collections', 'json', req, runtime)
        )

    def list_deployed_algorithm_models(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListDeployedAlgorithmModelsRequest,
    ) -> open_search_20171225_models.ListDeployedAlgorithmModelsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_deployed_algorithm_models_with_options(app_group_identity, request, headers, runtime)

    async def list_deployed_algorithm_models_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListDeployedAlgorithmModelsRequest,
    ) -> open_search_20171225_models.ListDeployedAlgorithmModelsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_deployed_algorithm_models_with_options_async(app_group_identity, request, headers, runtime)

    def list_deployed_algorithm_models_with_options(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListDeployedAlgorithmModelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListDeployedAlgorithmModelsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.in_service_only):
            query['inServiceOnly'] = request.in_service_only
        if not UtilClient.is_unset(request.algorithm_type):
            query['algorithmType'] = request.algorithm_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListDeployedAlgorithmModelsResponse(),
            self.do_roarequest('ListDeployedAlgorithmModels', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/deployed-algorithm-models', 'json', req, runtime)
        )

    async def list_deployed_algorithm_models_with_options_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListDeployedAlgorithmModelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListDeployedAlgorithmModelsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.in_service_only):
            query['inServiceOnly'] = request.in_service_only
        if not UtilClient.is_unset(request.algorithm_type):
            query['algorithmType'] = request.algorithm_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListDeployedAlgorithmModelsResponse(),
            await self.do_roarequest_async('ListDeployedAlgorithmModels', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/deployed-algorithm-models', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ListFirstRanksResponse(),
            self.do_roarequest('ListFirstRanks', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/first-ranks', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ListFirstRanksResponse(),
            await self.do_roarequest_async('ListFirstRanks', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/first-ranks', 'json', req, runtime)
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

    def list_intervention_dictionaries_with_options(
        self,
        request: open_search_20171225_models.ListInterventionDictionariesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListInterventionDictionariesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.types):
            query['types'] = request.types
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListInterventionDictionariesResponse(),
            self.do_roarequest('ListInterventionDictionaries', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/intervention-dictionaries', 'json', req, runtime)
        )

    async def list_intervention_dictionaries_with_options_async(
        self,
        request: open_search_20171225_models.ListInterventionDictionariesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListInterventionDictionariesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.types):
            query['types'] = request.types
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListInterventionDictionariesResponse(),
            await self.do_roarequest_async('ListInterventionDictionaries', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/intervention-dictionaries', 'json', req, runtime)
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

    def list_intervention_dictionary_entries_with_options(
        self,
        name: str,
        request: open_search_20171225_models.ListInterventionDictionaryEntriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListInterventionDictionaryEntriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.word):
            query['word'] = request.word
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListInterventionDictionaryEntriesResponse(),
            self.do_roarequest('ListInterventionDictionaryEntries', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/intervention-dictionaries/{name}/entries', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.word):
            query['word'] = request.word
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListInterventionDictionaryEntriesResponse(),
            await self.do_roarequest_async('ListInterventionDictionaryEntries', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/intervention-dictionaries/{name}/entries', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ListInterventionDictionaryNerResultsResponse(),
            self.do_roarequest('ListInterventionDictionaryNerResults', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/intervention-dictionaries/{name}/ner-results', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ListInterventionDictionaryNerResultsResponse(),
            await self.do_roarequest_async('ListInterventionDictionaryNerResults', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/intervention-dictionaries/{name}/ner-results', 'json', req, runtime)
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

    def list_intervention_dictionary_related_entities_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListInterventionDictionaryRelatedEntitiesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListInterventionDictionaryRelatedEntitiesResponse(),
            self.do_roarequest('ListInterventionDictionaryRelatedEntities', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/intervention-dictionaries/{name}/related', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ListInterventionDictionaryRelatedEntitiesResponse(),
            await self.do_roarequest_async('ListInterventionDictionaryRelatedEntities', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/intervention-dictionaries/{name}/related', 'json', req, runtime)
        )

    def list_models(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListModelsRequest,
    ) -> open_search_20171225_models.ListModelsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_models_with_options(app_group_identity, request, headers, runtime)

    async def list_models_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListModelsRequest,
    ) -> open_search_20171225_models.ListModelsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_models_with_options_async(app_group_identity, request, headers, runtime)

    def list_models_with_options(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListModelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListModelsResponse:
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
        return TeaCore.from_map(
            open_search_20171225_models.ListModelsResponse(),
            self.do_roarequest('ListModels', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/algorithm/models', 'json', req, runtime)
        )

    async def list_models_with_options_async(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListModelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListModelsResponse:
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
        return TeaCore.from_map(
            open_search_20171225_models.ListModelsResponse(),
            await self.do_roarequest_async('ListModels', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/algorithm/models', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ListQueryProcessorNersResponse(),
            self.do_roarequest('ListQueryProcessorNers', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/query-processor/ner/default-priorities', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ListQueryProcessorNersResponse(),
            await self.do_roarequest_async('ListQueryProcessorNers', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/query-processor/ner/default-priorities', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ListQueryProcessorsResponse(),
            self.do_roarequest('ListQueryProcessors', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/query-processors', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ListQueryProcessorsResponse(),
            await self.do_roarequest_async('ListQueryProcessors', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/query-processors', 'json', req, runtime)
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

    def list_scheduled_tasks_with_options(
        self,
        app_group_identity: str,
        request: open_search_20171225_models.ListScheduledTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListScheduledTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListScheduledTasksResponse(),
            self.do_roarequest('ListScheduledTasks', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scheduled-tasks', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListScheduledTasksResponse(),
            await self.do_roarequest_async('ListScheduledTasks', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scheduled-tasks', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ListSecondRanksResponse(),
            self.do_roarequest('ListSecondRanks', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/second-ranks', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ListSecondRanksResponse(),
            await self.do_roarequest_async('ListSecondRanks', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/second-ranks', 'json', req, runtime)
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

    def list_slow_query_categories_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListSlowQueryCategoriesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListSlowQueryCategoriesResponse(),
            self.do_roarequest('ListSlowQueryCategories', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/optimizers/slow-query/categories', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ListSlowQueryCategoriesResponse(),
            await self.do_roarequest_async('ListSlowQueryCategories', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/optimizers/slow-query/categories', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ListSlowQueryQueriesResponse(),
            self.do_roarequest('ListSlowQueryQueries', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/optimizers/slow-query/categories/{category_index}/queries', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ListSlowQueryQueriesResponse(),
            await self.do_roarequest_async('ListSlowQueryQueries', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/optimizers/slow-query/categories/{category_index}/queries', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ListSortExpressionsResponse(),
            self.do_roarequest('ListSortExpressions', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/sort-expressions', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ListSortExpressionsResponse(),
            await self.do_roarequest_async('ListSortExpressions', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/sort-expressions', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ListSortScriptsResponse(),
            self.do_roarequest('ListSortScripts', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_version_id}/sort-scripts', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ListSortScriptsResponse(),
            await self.do_roarequest_async('ListSortScripts', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_version_id}/sort-scripts', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.stop_time):
            query['stopTime'] = request.stop_time
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.sort_by):
            query['sortBy'] = request.sort_by
        if not UtilClient.is_unset(request.distinct):
            query['distinct'] = request.distinct
        if not UtilClient.is_unset(request.columns):
            query['columns'] = request.columns
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListStatisticLogsResponse(),
            self.do_roarequest('ListStatisticLogs', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/statistic-logs/{module_name}', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.stop_time):
            query['stopTime'] = request.stop_time
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.sort_by):
            query['sortBy'] = request.sort_by
        if not UtilClient.is_unset(request.distinct):
            query['distinct'] = request.distinct
        if not UtilClient.is_unset(request.columns):
            query['columns'] = request.columns
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListStatisticLogsResponse(),
            await self.do_roarequest_async('ListStatisticLogs', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/statistic-logs/{module_name}', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.columns):
            query['columns'] = request.columns
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListStatisticReportResponse(),
            self.do_roarequest('ListStatisticReport', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/statistic-report/{module_name}', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.columns):
            query['columns'] = request.columns
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListStatisticReportResponse(),
            await self.do_roarequest_async('ListStatisticReport', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/statistic-report/{module_name}', 'json', req, runtime)
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

    def list_user_analyzer_entries_with_options(
        self,
        name: str,
        request: open_search_20171225_models.ListUserAnalyzerEntriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ListUserAnalyzerEntriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.word):
            query['word'] = request.word
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListUserAnalyzerEntriesResponse(),
            self.do_roarequest('ListUserAnalyzerEntries', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/user-analyzers/{name}/entries', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.word):
            query['word'] = request.word
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListUserAnalyzerEntriesResponse(),
            await self.do_roarequest_async('ListUserAnalyzerEntries', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/user-analyzers/{name}/entries', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ListUserAnalyzersResponse(),
            self.do_roarequest('ListUserAnalyzers', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/user-analyzers', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ListUserAnalyzersResponse(),
            await self.do_roarequest_async('ListUserAnalyzers', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/user-analyzers', 'json', req, runtime)
        )

    def modify_app_group(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.ModifyAppGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_app_group_with_options(app_group_identity, headers, runtime)

    async def modify_app_group_async(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.ModifyAppGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_app_group_with_options_async(app_group_identity, headers, runtime)

    def modify_app_group_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ModifyAppGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifyAppGroupResponse(),
            self.do_roarequest('ModifyAppGroup', '2017-12-25', 'HTTPS', 'PUT', 'AK', f'/v4/openapi/app-groups/{app_group_identity}', 'json', req, runtime)
        )

    async def modify_app_group_with_options_async(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ModifyAppGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifyAppGroupResponse(),
            await self.do_roarequest_async('ModifyAppGroup', '2017-12-25', 'HTTPS', 'PUT', 'AK', f'/v4/openapi/app-groups/{app_group_identity}', 'json', req, runtime)
        )

    def modify_app_group_quota(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.ModifyAppGroupQuotaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_app_group_quota_with_options(app_group_identity, headers, runtime)

    async def modify_app_group_quota_async(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.ModifyAppGroupQuotaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_app_group_quota_with_options_async(app_group_identity, headers, runtime)

    def modify_app_group_quota_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ModifyAppGroupQuotaResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifyAppGroupQuotaResponse(),
            self.do_roarequest('ModifyAppGroupQuota', '2017-12-25', 'HTTPS', 'PUT', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/quota', 'json', req, runtime)
        )

    async def modify_app_group_quota_with_options_async(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ModifyAppGroupQuotaResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifyAppGroupQuotaResponse(),
            await self.do_roarequest_async('ModifyAppGroupQuota', '2017-12-25', 'HTTPS', 'PUT', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/quota', 'json', req, runtime)
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
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifyFirstRankResponse(),
            self.do_roarequest('ModifyFirstRank', '2017-12-25', 'HTTPS', 'PUT', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/first-ranks/{name}', 'json', req, runtime)
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
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifyFirstRankResponse(),
            await self.do_roarequest_async('ModifyFirstRank', '2017-12-25', 'HTTPS', 'PUT', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/first-ranks/{name}', 'json', req, runtime)
        )

    def modify_model(
        self,
        app_group_identity: str,
        model_name: str,
    ) -> open_search_20171225_models.ModifyModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_model_with_options(app_group_identity, model_name, headers, runtime)

    async def modify_model_async(
        self,
        app_group_identity: str,
        model_name: str,
    ) -> open_search_20171225_models.ModifyModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_model_with_options_async(app_group_identity, model_name, headers, runtime)

    def modify_model_with_options(
        self,
        app_group_identity: str,
        model_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ModifyModelResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifyModelResponse(),
            self.do_roarequest('ModifyModel', '2017-12-25', 'HTTPS', 'PUT', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/algorithm/models/{model_name}', 'json', req, runtime)
        )

    async def modify_model_with_options_async(
        self,
        app_group_identity: str,
        model_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ModifyModelResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifyModelResponse(),
            await self.do_roarequest_async('ModifyModel', '2017-12-25', 'HTTPS', 'PUT', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/algorithm/models/{model_name}', 'json', req, runtime)
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
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifyQueryProcessorResponse(),
            self.do_roarequest('ModifyQueryProcessor', '2017-12-25', 'HTTPS', 'PUT', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/query-processors/{name}', 'json', req, runtime)
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
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifyQueryProcessorResponse(),
            await self.do_roarequest_async('ModifyQueryProcessor', '2017-12-25', 'HTTPS', 'PUT', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/query-processors/{name}', 'json', req, runtime)
        )

    def modify_scheduled_task(
        self,
        app_group_identity: str,
        task_id: str,
    ) -> open_search_20171225_models.ModifyScheduledTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_scheduled_task_with_options(app_group_identity, task_id, headers, runtime)

    async def modify_scheduled_task_async(
        self,
        app_group_identity: str,
        task_id: str,
    ) -> open_search_20171225_models.ModifyScheduledTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_scheduled_task_with_options_async(app_group_identity, task_id, headers, runtime)

    def modify_scheduled_task_with_options(
        self,
        app_group_identity: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ModifyScheduledTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifyScheduledTaskResponse(),
            self.do_roarequest('ModifyScheduledTask', '2017-12-25', 'HTTPS', 'PUT', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scheduled-tasks/{task_id}', 'json', req, runtime)
        )

    async def modify_scheduled_task_with_options_async(
        self,
        app_group_identity: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ModifyScheduledTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifyScheduledTaskResponse(),
            await self.do_roarequest_async('ModifyScheduledTask', '2017-12-25', 'HTTPS', 'PUT', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scheduled-tasks/{task_id}', 'json', req, runtime)
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
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifySecondRankResponse(),
            self.do_roarequest('ModifySecondRank', '2017-12-25', 'HTTPS', 'PUT', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/second-ranks/{name}', 'json', req, runtime)
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
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifySecondRankResponse(),
            await self.do_roarequest_async('ModifySecondRank', '2017-12-25', 'HTTPS', 'PUT', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/second-ranks/{name}', 'json', req, runtime)
        )

    def preview_model(
        self,
        app_group_identity: str,
        model_name: str,
        request: open_search_20171225_models.PreviewModelRequest,
    ) -> open_search_20171225_models.PreviewModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.preview_model_with_options(app_group_identity, model_name, request, headers, runtime)

    async def preview_model_async(
        self,
        app_group_identity: str,
        model_name: str,
        request: open_search_20171225_models.PreviewModelRequest,
    ) -> open_search_20171225_models.PreviewModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.preview_model_with_options_async(app_group_identity, model_name, request, headers, runtime)

    def preview_model_with_options(
        self,
        app_group_identity: str,
        model_name: str,
        request: open_search_20171225_models.PreviewModelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.PreviewModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.PreviewModelResponse(),
            self.do_roarequest('PreviewModel', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/algorithm/models/{model_name}/actions/preview', 'json', req, runtime)
        )

    async def preview_model_with_options_async(
        self,
        app_group_identity: str,
        model_name: str,
        request: open_search_20171225_models.PreviewModelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.PreviewModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.PreviewModelResponse(),
            await self.do_roarequest_async('PreviewModel', '2017-12-25', 'HTTPS', 'GET', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/algorithm/models/{model_name}/actions/preview', 'json', req, runtime)
        )

    def push_intervention_dictionary_entries(
        self,
        name: str,
    ) -> open_search_20171225_models.PushInterventionDictionaryEntriesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_intervention_dictionary_entries_with_options(name, headers, runtime)

    async def push_intervention_dictionary_entries_async(
        self,
        name: str,
    ) -> open_search_20171225_models.PushInterventionDictionaryEntriesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.push_intervention_dictionary_entries_with_options_async(name, headers, runtime)

    def push_intervention_dictionary_entries_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.PushInterventionDictionaryEntriesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.PushInterventionDictionaryEntriesResponse(),
            self.do_roarequest('PushInterventionDictionaryEntries', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/intervention-dictionaries/{name}/entries/actions/bulk', 'json', req, runtime)
        )

    async def push_intervention_dictionary_entries_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.PushInterventionDictionaryEntriesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.PushInterventionDictionaryEntriesResponse(),
            await self.do_roarequest_async('PushInterventionDictionaryEntries', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/intervention-dictionaries/{name}/entries/actions/bulk', 'json', req, runtime)
        )

    def push_user_analyzer_entries(
        self,
        name: str,
    ) -> open_search_20171225_models.PushUserAnalyzerEntriesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_user_analyzer_entries_with_options(name, headers, runtime)

    async def push_user_analyzer_entries_async(
        self,
        name: str,
    ) -> open_search_20171225_models.PushUserAnalyzerEntriesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.push_user_analyzer_entries_with_options_async(name, headers, runtime)

    def push_user_analyzer_entries_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.PushUserAnalyzerEntriesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.PushUserAnalyzerEntriesResponse(),
            self.do_roarequest('PushUserAnalyzerEntries', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/user-analyzers/{name}/entries/actions/bulk', 'json', req, runtime)
        )

    async def push_user_analyzer_entries_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.PushUserAnalyzerEntriesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.PushUserAnalyzerEntriesResponse(),
            await self.do_roarequest_async('PushUserAnalyzerEntries', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/user-analyzers/{name}/entries/actions/bulk', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.RankPreviewQueryResponse(),
            self.do_roarequest('RankPreviewQuery', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/algorithm/models/{model_name}/actions/query-rank', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.RankPreviewQueryResponse(),
            await self.do_roarequest_async('RankPreviewQuery', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/algorithm/models/{model_name}/actions/query-rank', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ReleaseSortScriptResponse(),
            self.do_roarequest('ReleaseSortScript', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_version_id}/sort-scripts/{script_name}/actions/release', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ReleaseSortScriptResponse(),
            await self.do_roarequest_async('ReleaseSortScript', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_version_id}/sort-scripts/{script_name}/actions/release', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.RemoveAppResponse(),
            self.do_roarequest('RemoveApp', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.RemoveAppResponse(),
            await self.do_roarequest_async('RemoveApp', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}', 'json', req, runtime)
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

    def remove_app_group_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RemoveAppGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveAppGroupResponse(),
            self.do_roarequest('RemoveAppGroup', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/app-groups/{app_group_identity}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.RemoveAppGroupResponse(),
            await self.do_roarequest_async('RemoveAppGroup', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/app-groups/{app_group_identity}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.RemoveDataCollectionResponse(),
            self.do_roarequest('RemoveDataCollection', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/data-collections/{data_collection_identity}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.RemoveDataCollectionResponse(),
            await self.do_roarequest_async('RemoveDataCollection', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/data-collections/{data_collection_identity}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.RemoveFirstRankResponse(),
            self.do_roarequest('RemoveFirstRank', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/first-ranks/{name}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.RemoveFirstRankResponse(),
            await self.do_roarequest_async('RemoveFirstRank', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/first-ranks/{name}', 'json', req, runtime)
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

    def remove_intervention_dictionary_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RemoveInterventionDictionaryResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveInterventionDictionaryResponse(),
            self.do_roarequest('RemoveInterventionDictionary', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/intervention-dictionaries/{name}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.RemoveInterventionDictionaryResponse(),
            await self.do_roarequest_async('RemoveInterventionDictionary', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/intervention-dictionaries/{name}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.RemoveQueryProcessorResponse(),
            self.do_roarequest('RemoveQueryProcessor', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/query-processors/{name}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.RemoveQueryProcessorResponse(),
            await self.do_roarequest_async('RemoveQueryProcessor', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/query-processors/{name}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.RemoveScheduledTaskResponse(),
            self.do_roarequest('RemoveScheduledTask', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scheduled-tasks/{task_id}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.RemoveScheduledTaskResponse(),
            await self.do_roarequest_async('RemoveScheduledTask', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scheduled-tasks/{task_id}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.RemoveSecondRankResponse(),
            self.do_roarequest('RemoveSecondRank', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/second-ranks/{name}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.RemoveSecondRankResponse(),
            await self.do_roarequest_async('RemoveSecondRank', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/second-ranks/{name}', 'json', req, runtime)
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

    def remove_user_analyzer_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RemoveUserAnalyzerResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveUserAnalyzerResponse(),
            self.do_roarequest('RemoveUserAnalyzer', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/user-analyzers/{name}', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.RemoveUserAnalyzerResponse(),
            await self.do_roarequest_async('RemoveUserAnalyzer', '2017-12-25', 'HTTPS', 'DELETE', 'AK', f'/v4/openapi/user-analyzers/{name}', 'json', req, runtime)
        )

    def renew_app_group(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.RenewAppGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.renew_app_group_with_options(app_group_identity, headers, runtime)

    async def renew_app_group_async(
        self,
        app_group_identity: str,
    ) -> open_search_20171225_models.RenewAppGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.renew_app_group_with_options_async(app_group_identity, headers, runtime)

    def renew_app_group_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RenewAppGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.RenewAppGroupResponse(),
            self.do_roarequest('RenewAppGroup', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/actions/renew', 'json', req, runtime)
        )

    async def renew_app_group_with_options_async(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.RenewAppGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.RenewAppGroupResponse(),
            await self.do_roarequest_async('RenewAppGroup', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/actions/renew', 'json', req, runtime)
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

    def replace_app_group_commodity_code_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.ReplaceAppGroupCommodityCodeResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.ReplaceAppGroupCommodityCodeResponse(),
            self.do_roarequest('ReplaceAppGroupCommodityCode', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/actions/to-instance-typed', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.ReplaceAppGroupCommodityCodeResponse(),
            await self.do_roarequest_async('ReplaceAppGroupCommodityCode', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/actions/to-instance-typed', 'json', req, runtime)
        )

    def save_sort_script_file(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        file_name: str,
    ) -> open_search_20171225_models.SaveSortScriptFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.save_sort_script_file_with_options(app_group_identity, script_name, app_version_id, file_name, headers, runtime)

    async def save_sort_script_file_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        file_name: str,
    ) -> open_search_20171225_models.SaveSortScriptFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.save_sort_script_file_with_options_async(app_group_identity, script_name, app_version_id, file_name, headers, runtime)

    def save_sort_script_file_with_options(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        file_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.SaveSortScriptFileResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.SaveSortScriptFileResponse(),
            self.do_roarequest('SaveSortScriptFile', '2017-12-25', 'HTTPS', 'PUT', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_version_id}/sort-scripts/{script_name}/files/src/{file_name}', 'json', req, runtime)
        )

    async def save_sort_script_file_with_options_async(
        self,
        app_group_identity: str,
        script_name: str,
        app_version_id: str,
        file_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.SaveSortScriptFileResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.SaveSortScriptFileResponse(),
            await self.do_roarequest_async('SaveSortScriptFile', '2017-12-25', 'HTTPS', 'PUT', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_version_id}/sort-scripts/{script_name}/files/src/{file_name}', 'json', req, runtime)
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

    def start_slow_query_analyzer_with_options(
        self,
        app_group_identity: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.StartSlowQueryAnalyzerResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.StartSlowQueryAnalyzerResponse(),
            self.do_roarequest('StartSlowQueryAnalyzer', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/optimizers/slow-query/actions/run', 'json', req, runtime)
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
        return TeaCore.from_map(
            open_search_20171225_models.StartSlowQueryAnalyzerResponse(),
            await self.do_roarequest_async('StartSlowQueryAnalyzer', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/optimizers/slow-query/actions/run', 'json', req, runtime)
        )

    def train_model(
        self,
        app_group_identity: str,
        model_name: str,
    ) -> open_search_20171225_models.TrainModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.train_model_with_options(app_group_identity, model_name, headers, runtime)

    async def train_model_async(
        self,
        app_group_identity: str,
        model_name: str,
    ) -> open_search_20171225_models.TrainModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.train_model_with_options_async(app_group_identity, model_name, headers, runtime)

    def train_model_with_options(
        self,
        app_group_identity: str,
        model_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.TrainModelResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.TrainModelResponse(),
            self.do_roarequest('TrainModel', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/algorithm/models/{model_name}/actions/train', 'json', req, runtime)
        )

    async def train_model_with_options_async(
        self,
        app_group_identity: str,
        model_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.TrainModelResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.TrainModelResponse(),
            await self.do_roarequest_async('TrainModel', '2017-12-25', 'HTTPS', 'POST', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/algorithm/models/{model_name}/actions/train', 'json', req, runtime)
        )

    def update_abtest_experiment(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
    ) -> open_search_20171225_models.UpdateABTestExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_abtest_experiment_with_options(app_group_identity, scene_id, group_id, experiment_id, headers, runtime)

    async def update_abtest_experiment_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
    ) -> open_search_20171225_models.UpdateABTestExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_abtest_experiment_with_options_async(app_group_identity, scene_id, group_id, experiment_id, headers, runtime)

    def update_abtest_experiment_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateABTestExperimentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateABTestExperimentResponse(),
            self.do_roarequest('UpdateABTestExperiment', '2017-12-25', 'HTTPS', 'PUT', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}/groups/{group_id}/experiments/{experiment_id}', 'json', req, runtime)
        )

    async def update_abtest_experiment_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateABTestExperimentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateABTestExperimentResponse(),
            await self.do_roarequest_async('UpdateABTestExperiment', '2017-12-25', 'HTTPS', 'PUT', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}/groups/{group_id}/experiments/{experiment_id}', 'json', req, runtime)
        )

    def update_abtest_fixed_flow_dividers(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
    ) -> open_search_20171225_models.UpdateABTestFixedFlowDividersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_abtest_fixed_flow_dividers_with_options(app_group_identity, scene_id, group_id, experiment_id, headers, runtime)

    async def update_abtest_fixed_flow_dividers_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
    ) -> open_search_20171225_models.UpdateABTestFixedFlowDividersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_abtest_fixed_flow_dividers_with_options_async(app_group_identity, scene_id, group_id, experiment_id, headers, runtime)

    def update_abtest_fixed_flow_dividers_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateABTestFixedFlowDividersResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateABTestFixedFlowDividersResponse(),
            self.do_roarequest('UpdateABTestFixedFlowDividers', '2017-12-25', 'HTTPS', 'PUT', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}/groups/{group_id}/experiments/{experiment_id}/fixed-flow-dividers', 'json', req, runtime)
        )

    async def update_abtest_fixed_flow_dividers_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateABTestFixedFlowDividersResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateABTestFixedFlowDividersResponse(),
            await self.do_roarequest_async('UpdateABTestFixedFlowDividers', '2017-12-25', 'HTTPS', 'PUT', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}/groups/{group_id}/experiments/{experiment_id}/fixed-flow-dividers', 'json', req, runtime)
        )

    def update_abtest_group(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
    ) -> open_search_20171225_models.UpdateABTestGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_abtest_group_with_options(app_group_identity, scene_id, group_id, headers, runtime)

    async def update_abtest_group_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
    ) -> open_search_20171225_models.UpdateABTestGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_abtest_group_with_options_async(app_group_identity, scene_id, group_id, headers, runtime)

    def update_abtest_group_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateABTestGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateABTestGroupResponse(),
            self.do_roarequest('UpdateABTestGroup', '2017-12-25', 'HTTPS', 'PUT', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}/groups/{group_id}', 'json', req, runtime)
        )

    async def update_abtest_group_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateABTestGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateABTestGroupResponse(),
            await self.do_roarequest_async('UpdateABTestGroup', '2017-12-25', 'HTTPS', 'PUT', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}/groups/{group_id}', 'json', req, runtime)
        )

    def update_abtest_scene(
        self,
        app_group_identity: str,
        scene_id: str,
    ) -> open_search_20171225_models.UpdateABTestSceneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_abtest_scene_with_options(app_group_identity, scene_id, headers, runtime)

    async def update_abtest_scene_async(
        self,
        app_group_identity: str,
        scene_id: str,
    ) -> open_search_20171225_models.UpdateABTestSceneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_abtest_scene_with_options_async(app_group_identity, scene_id, headers, runtime)

    def update_abtest_scene_with_options(
        self,
        app_group_identity: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateABTestSceneResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateABTestSceneResponse(),
            self.do_roarequest('UpdateABTestScene', '2017-12-25', 'HTTPS', 'PUT', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}', 'json', req, runtime)
        )

    async def update_abtest_scene_with_options_async(
        self,
        app_group_identity: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> open_search_20171225_models.UpdateABTestSceneResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateABTestSceneResponse(),
            await self.do_roarequest_async('UpdateABTestScene', '2017-12-25', 'HTTPS', 'PUT', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/scenes/{scene_id}', 'json', req, runtime)
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
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateFetchFieldsResponse(),
            self.do_roarequest('UpdateFetchFields', '2017-12-25', 'HTTPS', 'PUT', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/fetch-fields', 'json', req, runtime)
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
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateFetchFieldsResponse(),
            await self.do_roarequest_async('UpdateFetchFields', '2017-12-25', 'HTTPS', 'PUT', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/fetch-fields', 'json', req, runtime)
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
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateSummariesResponse(),
            self.do_roarequest('UpdateSummaries', '2017-12-25', 'HTTPS', 'PUT', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/summaries', 'json', req, runtime)
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
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateSummariesResponse(),
            await self.do_roarequest_async('UpdateSummaries', '2017-12-25', 'HTTPS', 'PUT', 'AK', f'/v4/openapi/app-groups/{app_group_identity}/apps/{app_id}/summaries', 'json', req, runtime)
        )
