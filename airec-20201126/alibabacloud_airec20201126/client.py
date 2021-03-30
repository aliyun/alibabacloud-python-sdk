# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_airec20201126 import models as airec_20201126_models
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
        self._endpoint = self.get_endpoint('airec', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def attach_dataset(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20201126_models.AttachDatasetResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.attach_dataset_with_options(instance_id, version_id, headers, runtime)

    async def attach_dataset_async(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20201126_models.AttachDatasetResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.attach_dataset_with_options_async(instance_id, version_id, headers, runtime)

    def attach_dataset_with_options(
        self,
        instance_id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.AttachDatasetResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='AttachDataset',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/dataSets/{{versionId}}/actions/current',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.AttachDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_dataset_with_options_async(
        self,
        instance_id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.AttachDatasetResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='AttachDataset',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/dataSets/{{versionId}}/actions/current',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.AttachDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_index_version(
        self,
        instance_id: str,
        algorithm_id: str,
        version_id: str,
    ) -> airec_20201126_models.AttachIndexVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.attach_index_version_with_options(instance_id, algorithm_id, version_id, headers, runtime)

    async def attach_index_version_async(
        self,
        instance_id: str,
        algorithm_id: str,
        version_id: str,
    ) -> airec_20201126_models.AttachIndexVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.attach_index_version_with_options_async(instance_id, algorithm_id, version_id, headers, runtime)

    def attach_index_version_with_options(
        self,
        instance_id: str,
        algorithm_id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.AttachIndexVersionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='AttachIndexVersion',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/filtering-algorithms/{{algorithmId}}/index-versions/{{versionId}}/actions/attach',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.AttachIndexVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_index_version_with_options_async(
        self,
        instance_id: str,
        algorithm_id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.AttachIndexVersionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='AttachIndexVersion',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/filtering-algorithms/{{algorithmId}}/index-versions/{{versionId}}/actions/attach',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.AttachIndexVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_ranking_model_reachable(
        self,
        instance_id: str,
        ranking_model_id: str,
    ) -> airec_20201126_models.CheckRankingModelReachableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_ranking_model_reachable_with_options(instance_id, ranking_model_id, headers, runtime)

    async def check_ranking_model_reachable_async(
        self,
        instance_id: str,
        ranking_model_id: str,
    ) -> airec_20201126_models.CheckRankingModelReachableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.check_ranking_model_reachable_with_options_async(instance_id, ranking_model_id, headers, runtime)

    def check_ranking_model_reachable_with_options(
        self,
        instance_id: str,
        ranking_model_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CheckRankingModelReachableResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CheckRankingModelReachable',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/ranking-models/{{rankingModelId}}/actions/check-connectivity',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CheckRankingModelReachableResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_ranking_model_reachable_with_options_async(
        self,
        instance_id: str,
        ranking_model_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CheckRankingModelReachableResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CheckRankingModelReachable',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/ranking-models/{{rankingModelId}}/actions/check-connectivity',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CheckRankingModelReachableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_experiment(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
        request: airec_20201126_models.CloneExperimentRequest,
    ) -> airec_20201126_models.CloneExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clone_experiment_with_options(instance_id, scene_id, experiment_id, request, headers, runtime)

    async def clone_experiment_async(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
        request: airec_20201126_models.CloneExperimentRequest,
    ) -> airec_20201126_models.CloneExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.clone_experiment_with_options_async(instance_id, scene_id, experiment_id, request, headers, runtime)

    def clone_experiment_with_options(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
        request: airec_20201126_models.CloneExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CloneExperimentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloneExperiment',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/experiments/{{experimentId}}/actions/clone',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CloneExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_experiment_with_options_async(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
        request: airec_20201126_models.CloneExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CloneExperimentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloneExperiment',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/experiments/{{experimentId}}/actions/clone',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CloneExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_filtering_algorithm(
        self,
        instance_id: str,
        request: airec_20201126_models.CreateFilteringAlgorithmRequest,
    ) -> airec_20201126_models.CreateFilteringAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_filtering_algorithm_with_options(instance_id, request, headers, runtime)

    async def create_filtering_algorithm_async(
        self,
        instance_id: str,
        request: airec_20201126_models.CreateFilteringAlgorithmRequest,
    ) -> airec_20201126_models.CreateFilteringAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_filtering_algorithm_with_options_async(instance_id, request, headers, runtime)

    def create_filtering_algorithm_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.CreateFilteringAlgorithmRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateFilteringAlgorithmResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFilteringAlgorithm',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/filtering-algorithms',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CreateFilteringAlgorithmResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_filtering_algorithm_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.CreateFilteringAlgorithmRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateFilteringAlgorithmResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFilteringAlgorithm',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/filtering-algorithms',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CreateFilteringAlgorithmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(self) -> airec_20201126_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_with_options(headers, runtime)

    async def create_instance_async(self) -> airec_20201126_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_with_options_async(headers, runtime)

    def create_instance_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ranking_model(
        self,
        instance_id: str,
        request: airec_20201126_models.CreateRankingModelRequest,
    ) -> airec_20201126_models.CreateRankingModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_ranking_model_with_options(instance_id, request, headers, runtime)

    async def create_ranking_model_async(
        self,
        instance_id: str,
        request: airec_20201126_models.CreateRankingModelRequest,
    ) -> airec_20201126_models.CreateRankingModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_ranking_model_with_options_async(instance_id, request, headers, runtime)

    def create_ranking_model_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.CreateRankingModelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateRankingModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRankingModel',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/ranking-models',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CreateRankingModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ranking_model_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.CreateRankingModelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateRankingModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRankingModel',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/ranking-models',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CreateRankingModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rule(
        self,
        instance_id: str,
    ) -> airec_20201126_models.CreateRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_rule_with_options(instance_id, headers, runtime)

    async def create_rule_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.CreateRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_rule_with_options_async(instance_id, headers, runtime)

    def create_rule_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateRuleResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateRule',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/rules',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CreateRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rule_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateRuleResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateRule',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/rules',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CreateRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scene(
        self,
        instance_id: str,
        request: airec_20201126_models.CreateSceneRequest,
    ) -> airec_20201126_models.CreateSceneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_scene_with_options(instance_id, request, headers, runtime)

    async def create_scene_async(
        self,
        instance_id: str,
        request: airec_20201126_models.CreateSceneRequest,
    ) -> airec_20201126_models.CreateSceneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_scene_with_options_async(instance_id, request, headers, runtime)

    def create_scene_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.CreateSceneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScene',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CreateSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scene_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.CreateSceneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScene',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CreateSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def decribe_ranking_model(
        self,
        instance_id: str,
        ranking_model_id: str,
    ) -> airec_20201126_models.DecribeRankingModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.decribe_ranking_model_with_options(instance_id, ranking_model_id, headers, runtime)

    async def decribe_ranking_model_async(
        self,
        instance_id: str,
        ranking_model_id: str,
    ) -> airec_20201126_models.DecribeRankingModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.decribe_ranking_model_with_options_async(instance_id, ranking_model_id, headers, runtime)

    def decribe_ranking_model_with_options(
        self,
        instance_id: str,
        ranking_model_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DecribeRankingModelResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DecribeRankingModel',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/ranking-models/{{rankingModelId}}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DecribeRankingModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def decribe_ranking_model_with_options_async(
        self,
        instance_id: str,
        ranking_model_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DecribeRankingModelResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DecribeRankingModel',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/ranking-models/{{rankingModelId}}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DecribeRankingModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_set(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20201126_models.DeleteDataSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_data_set_with_options(instance_id, version_id, headers, runtime)

    async def delete_data_set_async(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20201126_models.DeleteDataSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_data_set_with_options_async(instance_id, version_id, headers, runtime)

    def delete_data_set_with_options(
        self,
        instance_id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DeleteDataSetResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDataSet',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/dataSets/{{versionId}}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DeleteDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_set_with_options_async(
        self,
        instance_id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DeleteDataSetResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDataSet',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/dataSets/{{versionId}}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DeleteDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_experiment(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
    ) -> airec_20201126_models.DeleteExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_experiment_with_options(instance_id, scene_id, experiment_id, headers, runtime)

    async def delete_experiment_async(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
    ) -> airec_20201126_models.DeleteExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_experiment_with_options_async(instance_id, scene_id, experiment_id, headers, runtime)

    def delete_experiment_with_options(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DeleteExperimentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteExperiment',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/experiments/{{experimentId}}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DeleteExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_experiment_with_options_async(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DeleteExperimentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteExperiment',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/experiments/{{experimentId}}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DeleteExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_filtering_algorithm(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.DeleteFilteringAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_filtering_algorithm_with_options(instance_id, algorithm_id, headers, runtime)

    async def delete_filtering_algorithm_async(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.DeleteFilteringAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_filtering_algorithm_with_options_async(instance_id, algorithm_id, headers, runtime)

    def delete_filtering_algorithm_with_options(
        self,
        instance_id: str,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DeleteFilteringAlgorithmResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFilteringAlgorithm',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/filtering-algorithms/{{algorithmId}}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DeleteFilteringAlgorithmResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_filtering_algorithm_with_options_async(
        self,
        instance_id: str,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DeleteFilteringAlgorithmResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFilteringAlgorithm',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/filtering-algorithms/{{algorithmId}}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DeleteFilteringAlgorithmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ranking_model(
        self,
        instance_id: str,
        ranking_model_id: str,
    ) -> airec_20201126_models.DeleteRankingModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_ranking_model_with_options(instance_id, ranking_model_id, headers, runtime)

    async def delete_ranking_model_async(
        self,
        instance_id: str,
        ranking_model_id: str,
    ) -> airec_20201126_models.DeleteRankingModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_ranking_model_with_options_async(instance_id, ranking_model_id, headers, runtime)

    def delete_ranking_model_with_options(
        self,
        instance_id: str,
        ranking_model_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DeleteRankingModelResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRankingModel',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/ranking-models/{{rankingModelId}}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DeleteRankingModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ranking_model_with_options_async(
        self,
        instance_id: str,
        ranking_model_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DeleteRankingModelResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRankingModel',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/ranking-models/{{rankingModelId}}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DeleteRankingModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scene(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DeleteSceneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_scene_with_options(instance_id, scene_id, headers, runtime)

    async def delete_scene_async(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DeleteSceneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_scene_with_options_async(instance_id, scene_id, headers, runtime)

    def delete_scene_with_options(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DeleteSceneResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteScene',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DeleteSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scene_with_options_async(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DeleteSceneResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteScene',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DeleteSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_base_experiment(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DescribeBaseExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_base_experiment_with_options(instance_id, scene_id, headers, runtime)

    async def describe_base_experiment_async(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DescribeBaseExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_base_experiment_with_options_async(instance_id, scene_id, headers, runtime)

    def describe_base_experiment_with_options(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeBaseExperimentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeBaseExperiment',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/base-experiment',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeBaseExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_base_experiment_with_options_async(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeBaseExperimentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeBaseExperiment',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/base-experiment',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeBaseExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_set_message(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20201126_models.DescribeDataSetMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_data_set_message_with_options(instance_id, version_id, headers, runtime)

    async def describe_data_set_message_async(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20201126_models.DescribeDataSetMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_data_set_message_with_options_async(instance_id, version_id, headers, runtime)

    def describe_data_set_message_with_options(
        self,
        instance_id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeDataSetMessageResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeDataSetMessage',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/dataSets/{{versionId}}/messages',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeDataSetMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_set_message_with_options_async(
        self,
        instance_id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeDataSetMessageResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeDataSetMessage',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/dataSets/{{versionId}}/messages',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeDataSetMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_default_algorithms(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DescribeDefaultAlgorithmsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_default_algorithms_with_options(instance_id, scene_id, headers, runtime)

    async def describe_default_algorithms_async(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DescribeDefaultAlgorithmsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_default_algorithms_with_options_async(instance_id, scene_id, headers, runtime)

    def describe_default_algorithms_with_options(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeDefaultAlgorithmsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeDefaultAlgorithms',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/default-algorithms',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeDefaultAlgorithmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_default_algorithms_with_options_async(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeDefaultAlgorithmsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeDefaultAlgorithms',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/default-algorithms',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeDefaultAlgorithmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_experiment(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
    ) -> airec_20201126_models.DescribeExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_experiment_with_options(instance_id, scene_id, experiment_id, headers, runtime)

    async def describe_experiment_async(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
    ) -> airec_20201126_models.DescribeExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_experiment_with_options_async(instance_id, scene_id, experiment_id, headers, runtime)

    def describe_experiment_with_options(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeExperimentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeExperiment',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/experiments/{{experimentId}}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_experiment_with_options_async(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeExperimentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeExperiment',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/experiments/{{experimentId}}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_experiment_env(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DescribeExperimentEnvResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_experiment_env_with_options(instance_id, scene_id, headers, runtime)

    async def describe_experiment_env_async(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DescribeExperimentEnvResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_experiment_env_with_options_async(instance_id, scene_id, headers, runtime)

    def describe_experiment_env_with_options(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeExperimentEnvResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeExperimentEnv',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/experiment-env',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeExperimentEnvResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_experiment_env_with_options_async(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeExperimentEnvResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeExperimentEnv',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/experiment-env',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeExperimentEnvResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_experiment_env_progress(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DescribeExperimentEnvProgressResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_experiment_env_progress_with_options(instance_id, scene_id, headers, runtime)

    async def describe_experiment_env_progress_async(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DescribeExperimentEnvProgressResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_experiment_env_progress_with_options_async(instance_id, scene_id, headers, runtime)

    def describe_experiment_env_progress_with_options(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeExperimentEnvProgressResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeExperimentEnvProgress',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/experiment-progress',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeExperimentEnvProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_experiment_env_progress_with_options_async(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeExperimentEnvProgressResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeExperimentEnvProgress',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/experiment-progress',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeExperimentEnvProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_filtering_algorithm(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.DescribeFilteringAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_filtering_algorithm_with_options(instance_id, algorithm_id, headers, runtime)

    async def describe_filtering_algorithm_async(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.DescribeFilteringAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_filtering_algorithm_with_options_async(instance_id, algorithm_id, headers, runtime)

    def describe_filtering_algorithm_with_options(
        self,
        instance_id: str,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeFilteringAlgorithmResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeFilteringAlgorithm',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/filtering-algorithms/{{algorithmId}}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeFilteringAlgorithmResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_filtering_algorithm_with_options_async(
        self,
        instance_id: str,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeFilteringAlgorithmResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeFilteringAlgorithm',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/filtering-algorithms/{{algorithmId}}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeFilteringAlgorithmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance(
        self,
        instance_id: str,
    ) -> airec_20201126_models.DescribeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_instance_with_options(instance_id, headers, runtime)

    async def describe_instance_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.DescribeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_instance_with_options_async(instance_id, headers, runtime)

    def describe_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_latest_task(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.DescribeLatestTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_latest_task_with_options(instance_id, algorithm_id, headers, runtime)

    async def describe_latest_task_async(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.DescribeLatestTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_latest_task_with_options_async(instance_id, algorithm_id, headers, runtime)

    def describe_latest_task_with_options(
        self,
        instance_id: str,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeLatestTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeLatestTask',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/filtering-algorithms/{{algorithmId}}/tasks/latest',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeLatestTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_latest_task_with_options_async(
        self,
        instance_id: str,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeLatestTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeLatestTask',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/filtering-algorithms/{{algorithmId}}/tasks/latest',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeLatestTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_quota(
        self,
        instance_id: str,
    ) -> airec_20201126_models.DescribeQuotaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_quota_with_options(instance_id, headers, runtime)

    async def describe_quota_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.DescribeQuotaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_quota_with_options_async(instance_id, headers, runtime)

    def describe_quota_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeQuotaResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeQuota',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/quota',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_quota_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeQuotaResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeQuota',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/quota',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: airec_20201126_models.DescribeRegionsRequest,
    ) -> airec_20201126_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(request, headers, runtime)

    async def describe_regions_async(
        self,
        request: airec_20201126_models.DescribeRegionsRequest,
    ) -> airec_20201126_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_regions_with_options_async(request, headers, runtime)

    def describe_regions_with_options(
        self,
        request: airec_20201126_models.DescribeRegionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/configurations/regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: airec_20201126_models.DescribeRegionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/configurations/regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule(
        self,
        instance_id: str,
        rule_id: str,
        request: airec_20201126_models.DescribeRuleRequest,
    ) -> airec_20201126_models.DescribeRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_rule_with_options(instance_id, rule_id, request, headers, runtime)

    async def describe_rule_async(
        self,
        instance_id: str,
        rule_id: str,
        request: airec_20201126_models.DescribeRuleRequest,
    ) -> airec_20201126_models.DescribeRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_rule_with_options_async(instance_id, rule_id, request, headers, runtime)

    def describe_rule_with_options(
        self,
        instance_id: str,
        rule_id: str,
        request: airec_20201126_models.DescribeRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['sceneId'] = request.scene_id
        if not UtilClient.is_unset(request.rule_type):
            query['ruleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRule',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/rules/{{ruleId}}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_with_options_async(
        self,
        instance_id: str,
        rule_id: str,
        request: airec_20201126_models.DescribeRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['sceneId'] = request.scene_id
        if not UtilClient.is_unset(request.rule_type):
            query['ruleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRule',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/rules/{{ruleId}}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scene(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DescribeSceneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_scene_with_options(instance_id, scene_id, headers, runtime)

    async def describe_scene_async(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DescribeSceneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_scene_with_options_async(instance_id, scene_id, headers, runtime)

    def describe_scene_with_options(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeSceneResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeScene',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scene_with_options_async(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeSceneResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeScene',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scene_bucket(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DescribeSceneBucketResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_scene_bucket_with_options(instance_id, scene_id, headers, runtime)

    async def describe_scene_bucket_async(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DescribeSceneBucketResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_scene_bucket_with_options_async(instance_id, scene_id, headers, runtime)

    def describe_scene_bucket_with_options(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeSceneBucketResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeSceneBucket',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/experiment-bucket',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeSceneBucketResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scene_bucket_with_options_async(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeSceneBucketResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeSceneBucket',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/experiment-bucket',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeSceneBucketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scene_throughput(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DescribeSceneThroughputResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_scene_throughput_with_options(instance_id, scene_id, headers, runtime)

    async def describe_scene_throughput_async(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DescribeSceneThroughputResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_scene_throughput_with_options_async(instance_id, scene_id, headers, runtime)

    def describe_scene_throughput_with_options(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeSceneThroughputResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeSceneThroughput',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/throughput',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeSceneThroughputResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scene_throughput_with_options_async(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeSceneThroughputResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeSceneThroughput',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/throughput',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeSceneThroughputResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sync_report_detail(
        self,
        instance_id: str,
        request: airec_20201126_models.DescribeSyncReportDetailRequest,
    ) -> airec_20201126_models.DescribeSyncReportDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_sync_report_detail_with_options(instance_id, request, headers, runtime)

    async def describe_sync_report_detail_async(
        self,
        instance_id: str,
        request: airec_20201126_models.DescribeSyncReportDetailRequest,
    ) -> airec_20201126_models.DescribeSyncReportDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_sync_report_detail_with_options_async(instance_id, request, headers, runtime)

    def describe_sync_report_detail_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.DescribeSyncReportDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeSyncReportDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.level_type):
            query['levelType'] = request.level_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSyncReportDetail',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/sync-reports/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeSyncReportDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sync_report_detail_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.DescribeSyncReportDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeSyncReportDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.level_type):
            query['levelType'] = request.level_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSyncReportDetail',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/sync-reports/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeSyncReportDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sync_report_outliers(
        self,
        instance_id: str,
        request: airec_20201126_models.DescribeSyncReportOutliersRequest,
    ) -> airec_20201126_models.DescribeSyncReportOutliersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_sync_report_outliers_with_options(instance_id, request, headers, runtime)

    async def describe_sync_report_outliers_async(
        self,
        instance_id: str,
        request: airec_20201126_models.DescribeSyncReportOutliersRequest,
    ) -> airec_20201126_models.DescribeSyncReportOutliersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_sync_report_outliers_with_options_async(instance_id, request, headers, runtime)

    def describe_sync_report_outliers_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.DescribeSyncReportOutliersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeSyncReportOutliersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.key):
            query['key'] = request.key
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.level_type):
            query['levelType'] = request.level_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSyncReportOutliers',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/sync-reports/outliers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeSyncReportOutliersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sync_report_outliers_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.DescribeSyncReportOutliersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeSyncReportOutliersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.key):
            query['key'] = request.key
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.level_type):
            query['levelType'] = request.level_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSyncReportOutliers',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/sync-reports/outliers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeSyncReportOutliersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_metrics(
        self,
        instance_id: str,
        request: airec_20201126_models.DescribeUserMetricsRequest,
    ) -> airec_20201126_models.DescribeUserMetricsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_user_metrics_with_options(instance_id, request, headers, runtime)

    async def describe_user_metrics_async(
        self,
        instance_id: str,
        request: airec_20201126_models.DescribeUserMetricsRequest,
    ) -> airec_20201126_models.DescribeUserMetricsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_user_metrics_with_options_async(instance_id, request, headers, runtime)

    def describe_user_metrics_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.DescribeUserMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeUserMetricsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_type):
            query['metricType'] = request.metric_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserMetrics',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/metrics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeUserMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_metrics_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.DescribeUserMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeUserMetricsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_type):
            query['metricType'] = request.metric_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserMetrics',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/metrics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeUserMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def downgrade_instance(
        self,
        instance_id: str,
    ) -> airec_20201126_models.DowngradeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.downgrade_instance_with_options(instance_id, headers, runtime)

    async def downgrade_instance_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.DowngradeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.downgrade_instance_with_options_async(instance_id, headers, runtime)

    def downgrade_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DowngradeInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DowngradeInstance',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/actions/downgrade',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DowngradeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def downgrade_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DowngradeInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DowngradeInstance',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/actions/downgrade',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DowngradeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_experiment(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.EnableExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_experiment_with_options(instance_id, scene_id, headers, runtime)

    async def enable_experiment_async(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.EnableExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.enable_experiment_with_options_async(instance_id, scene_id, headers, runtime)

    def enable_experiment_with_options(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.EnableExperimentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='EnableExperiment',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/actions/enable-experiment',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.EnableExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_experiment_with_options_async(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.EnableExperimentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='EnableExperiment',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/actions/enable-experiment',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.EnableExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dashboard_details(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDashboardDetailsRequest,
    ) -> airec_20201126_models.ListDashboardDetailsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dashboard_details_with_options(instance_id, request, headers, runtime)

    async def list_dashboard_details_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDashboardDetailsRequest,
    ) -> airec_20201126_models.ListDashboardDetailsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_dashboard_details_with_options_async(instance_id, request, headers, runtime)

    def list_dashboard_details_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDashboardDetailsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListDashboardDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.trace_ids):
            query['traceIds'] = request.trace_ids
        if not UtilClient.is_unset(request.scene_ids):
            query['sceneIds'] = request.scene_ids
        if not UtilClient.is_unset(request.metric_type):
            query['metricType'] = request.metric_type
        if not UtilClient.is_unset(request.experiment_ids):
            query['experimentIds'] = request.experiment_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboardDetails',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/dashboard/details',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListDashboardDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dashboard_details_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDashboardDetailsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListDashboardDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.trace_ids):
            query['traceIds'] = request.trace_ids
        if not UtilClient.is_unset(request.scene_ids):
            query['sceneIds'] = request.scene_ids
        if not UtilClient.is_unset(request.metric_type):
            query['metricType'] = request.metric_type
        if not UtilClient.is_unset(request.experiment_ids):
            query['experimentIds'] = request.experiment_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboardDetails',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/dashboard/details',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListDashboardDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dashboard_details_flows(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDashboardDetailsFlowsRequest,
    ) -> airec_20201126_models.ListDashboardDetailsFlowsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dashboard_details_flows_with_options(instance_id, request, headers, runtime)

    async def list_dashboard_details_flows_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDashboardDetailsFlowsRequest,
    ) -> airec_20201126_models.ListDashboardDetailsFlowsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_dashboard_details_flows_with_options_async(instance_id, request, headers, runtime)

    def list_dashboard_details_flows_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDashboardDetailsFlowsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListDashboardDetailsFlowsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.trace_ids):
            query['traceIds'] = request.trace_ids
        if not UtilClient.is_unset(request.scene_ids):
            query['sceneIds'] = request.scene_ids
        if not UtilClient.is_unset(request.metric_type):
            query['metricType'] = request.metric_type
        if not UtilClient.is_unset(request.experiment_ids):
            query['experimentIds'] = request.experiment_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboardDetailsFlows',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/dashboard/details/flows',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListDashboardDetailsFlowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dashboard_details_flows_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDashboardDetailsFlowsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListDashboardDetailsFlowsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.trace_ids):
            query['traceIds'] = request.trace_ids
        if not UtilClient.is_unset(request.scene_ids):
            query['sceneIds'] = request.scene_ids
        if not UtilClient.is_unset(request.metric_type):
            query['metricType'] = request.metric_type
        if not UtilClient.is_unset(request.experiment_ids):
            query['experimentIds'] = request.experiment_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboardDetailsFlows',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/dashboard/details/flows',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListDashboardDetailsFlowsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dashboard_metrics(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDashboardMetricsRequest,
    ) -> airec_20201126_models.ListDashboardMetricsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dashboard_metrics_with_options(instance_id, request, headers, runtime)

    async def list_dashboard_metrics_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDashboardMetricsRequest,
    ) -> airec_20201126_models.ListDashboardMetricsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_dashboard_metrics_with_options_async(instance_id, request, headers, runtime)

    def list_dashboard_metrics_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDashboardMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListDashboardMetricsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_type):
            query['metricType'] = request.metric_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboardMetrics',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/dashboard/metrics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListDashboardMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dashboard_metrics_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDashboardMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListDashboardMetricsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_type):
            query['metricType'] = request.metric_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboardMetrics',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/dashboard/metrics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListDashboardMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dashboard_metrics_flows(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDashboardMetricsFlowsRequest,
    ) -> airec_20201126_models.ListDashboardMetricsFlowsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dashboard_metrics_flows_with_options(instance_id, request, headers, runtime)

    async def list_dashboard_metrics_flows_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDashboardMetricsFlowsRequest,
    ) -> airec_20201126_models.ListDashboardMetricsFlowsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_dashboard_metrics_flows_with_options_async(instance_id, request, headers, runtime)

    def list_dashboard_metrics_flows_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDashboardMetricsFlowsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListDashboardMetricsFlowsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_type):
            query['metricType'] = request.metric_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboardMetricsFlows',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/dashboard/metrics/flows',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListDashboardMetricsFlowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dashboard_metrics_flows_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDashboardMetricsFlowsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListDashboardMetricsFlowsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_type):
            query['metricType'] = request.metric_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboardMetricsFlows',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/dashboard/metrics/flows',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListDashboardMetricsFlowsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_set(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ListDataSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_set_with_options(instance_id, headers, runtime)

    async def list_data_set_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ListDataSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_data_set_with_options_async(instance_id, headers, runtime)

    def list_data_set_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListDataSetResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDataSet',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/dataSets',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_set_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListDataSetResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDataSet',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/dataSets',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_source(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ListDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_source_with_options(instance_id, headers, runtime)

    async def list_data_source_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ListDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_data_source_with_options_async(instance_id, headers, runtime)

    def list_data_source_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListDataSourceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDataSource',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/dataSources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_source_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListDataSourceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDataSource',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/dataSources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_experiments(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.ListExperimentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_experiments_with_options(instance_id, scene_id, headers, runtime)

    async def list_experiments_async(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.ListExperimentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_experiments_with_options_async(instance_id, scene_id, headers, runtime)

    def list_experiments_with_options(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListExperimentsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListExperiments',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/experiments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListExperimentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_experiments_with_options_async(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListExperimentsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListExperiments',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/experiments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListExperimentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_filtering_algorithms(
        self,
        instance_id: str,
        request: airec_20201126_models.ListFilteringAlgorithmsRequest,
    ) -> airec_20201126_models.ListFilteringAlgorithmsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_filtering_algorithms_with_options(instance_id, request, headers, runtime)

    async def list_filtering_algorithms_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListFilteringAlgorithmsRequest,
    ) -> airec_20201126_models.ListFilteringAlgorithmsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_filtering_algorithms_with_options_async(instance_id, request, headers, runtime)

    def list_filtering_algorithms_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListFilteringAlgorithmsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListFilteringAlgorithmsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.algorithm_id):
            query['algorithmId'] = request.algorithm_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFilteringAlgorithms',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/filtering-algorithms',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListFilteringAlgorithmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_filtering_algorithms_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListFilteringAlgorithmsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListFilteringAlgorithmsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.algorithm_id):
            query['algorithmId'] = request.algorithm_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFilteringAlgorithms',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/filtering-algorithms',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListFilteringAlgorithmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_index_versions(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.ListIndexVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_index_versions_with_options(instance_id, algorithm_id, headers, runtime)

    async def list_index_versions_async(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.ListIndexVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_index_versions_with_options_async(instance_id, algorithm_id, headers, runtime)

    def list_index_versions_with_options(
        self,
        instance_id: str,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListIndexVersionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListIndexVersions',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/filtering-algorithms/{{algorithmId}}/index-versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListIndexVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_index_versions_with_options_async(
        self,
        instance_id: str,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListIndexVersionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListIndexVersions',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/filtering-algorithms/{{algorithmId}}/index-versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListIndexVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance(
        self,
        request: airec_20201126_models.ListInstanceRequest,
    ) -> airec_20201126_models.ListInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_with_options(request, headers, runtime)

    async def list_instance_async(
        self,
        request: airec_20201126_models.ListInstanceRequest,
    ) -> airec_20201126_models.ListInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instance_with_options_async(request, headers, runtime)

    def list_instance_with_options(
        self,
        request: airec_20201126_models.ListInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.expired_time):
            query['expiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstance',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_with_options_async(
        self,
        request: airec_20201126_models.ListInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.expired_time):
            query['expiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstance',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_task(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ListInstanceTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_task_with_options(instance_id, headers, runtime)

    async def list_instance_task_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ListInstanceTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instance_task_with_options_async(instance_id, headers, runtime)

    def list_instance_task_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListInstanceTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListInstanceTask',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListInstanceTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_task_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListInstanceTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListInstanceTask',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListInstanceTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_items(
        self,
        instance_id: str,
        request: airec_20201126_models.ListItemsRequest,
    ) -> airec_20201126_models.ListItemsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_items_with_options(instance_id, request, headers, runtime)

    async def list_items_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListItemsRequest,
    ) -> airec_20201126_models.ListItemsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_items_with_options_async(instance_id, request, headers, runtime)

    def list_items_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListItemsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListItems',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/items/actions/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_items_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListItemsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListItems',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/items/actions/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_logs(
        self,
        instance_id: str,
        request: airec_20201126_models.ListLogsRequest,
    ) -> airec_20201126_models.ListLogsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_logs_with_options(instance_id, request, headers, runtime)

    async def list_logs_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListLogsRequest,
    ) -> airec_20201126_models.ListLogsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_logs_with_options_async(instance_id, request, headers, runtime)

    def list_logs_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query_params):
            query['queryParams'] = request.query_params
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogs',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_logs_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query_params):
            query['queryParams'] = request.query_params
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogs',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mix_categories(self) -> airec_20201126_models.ListMixCategoriesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_mix_categories_with_options(headers, runtime)

    async def list_mix_categories_async(self) -> airec_20201126_models.ListMixCategoriesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_mix_categories_with_options_async(headers, runtime)

    def list_mix_categories_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListMixCategoriesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListMixCategories',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/configurations/mixCategories',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListMixCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mix_categories_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListMixCategoriesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListMixCategories',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/configurations/mixCategories',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListMixCategoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ranking_models(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRankingModelsRequest,
    ) -> airec_20201126_models.ListRankingModelsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ranking_models_with_options(instance_id, request, headers, runtime)

    async def list_ranking_models_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRankingModelsRequest,
    ) -> airec_20201126_models.ListRankingModelsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_ranking_models_with_options_async(instance_id, request, headers, runtime)

    def list_ranking_models_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRankingModelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListRankingModelsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ranking_model_id):
            query['rankingModelId'] = request.ranking_model_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRankingModels',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/ranking-models',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListRankingModelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ranking_models_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRankingModelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListRankingModelsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ranking_model_id):
            query['rankingModelId'] = request.ranking_model_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRankingModels',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/ranking-models',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListRankingModelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rule_conditions(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ListRuleConditionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_rule_conditions_with_options(instance_id, headers, runtime)

    async def list_rule_conditions_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ListRuleConditionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_rule_conditions_with_options_async(instance_id, headers, runtime)

    def list_rule_conditions_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListRuleConditionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListRuleConditions',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/rule-conditions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListRuleConditionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rule_conditions_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListRuleConditionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListRuleConditions',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/rule-conditions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListRuleConditionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rules(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRulesRequest,
    ) -> airec_20201126_models.ListRulesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_rules_with_options(instance_id, request, headers, runtime)

    async def list_rules_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRulesRequest,
    ) -> airec_20201126_models.ListRulesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_rules_with_options_async(instance_id, request, headers, runtime)

    def list_rules_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['sceneId'] = request.scene_id
        if not UtilClient.is_unset(request.rule_type):
            query['ruleType'] = request.rule_type
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRules',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/rules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rules_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['sceneId'] = request.scene_id
        if not UtilClient.is_unset(request.rule_type):
            query['ruleType'] = request.rule_type
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRules',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/rules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rule_tasks(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRuleTasksRequest,
    ) -> airec_20201126_models.ListRuleTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_rule_tasks_with_options(instance_id, request, headers, runtime)

    async def list_rule_tasks_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRuleTasksRequest,
    ) -> airec_20201126_models.ListRuleTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_rule_tasks_with_options_async(instance_id, request, headers, runtime)

    def list_rule_tasks_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRuleTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListRuleTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['sceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRuleTasks',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/rule-tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListRuleTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rule_tasks_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRuleTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListRuleTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['sceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRuleTasks',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/rule-tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListRuleTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scene_items(
        self,
        instance_id: str,
        scene_id: str,
        request: airec_20201126_models.ListSceneItemsRequest,
    ) -> airec_20201126_models.ListSceneItemsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_scene_items_with_options(instance_id, scene_id, request, headers, runtime)

    async def list_scene_items_async(
        self,
        instance_id: str,
        scene_id: str,
        request: airec_20201126_models.ListSceneItemsRequest,
    ) -> airec_20201126_models.ListSceneItemsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_scene_items_with_options_async(instance_id, scene_id, request, headers, runtime)

    def list_scene_items_with_options(
        self,
        instance_id: str,
        scene_id: str,
        request: airec_20201126_models.ListSceneItemsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListSceneItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_rule_id):
            query['operationRuleId'] = request.operation_rule_id
        if not UtilClient.is_unset(request.selection_rule_id):
            query['selectionRuleId'] = request.selection_rule_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.preview_type):
            query['previewType'] = request.preview_type
        if not UtilClient.is_unset(request.query_count):
            query['queryCount'] = request.query_count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSceneItems',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/items',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListSceneItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scene_items_with_options_async(
        self,
        instance_id: str,
        scene_id: str,
        request: airec_20201126_models.ListSceneItemsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListSceneItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_rule_id):
            query['operationRuleId'] = request.operation_rule_id
        if not UtilClient.is_unset(request.selection_rule_id):
            query['selectionRuleId'] = request.selection_rule_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.preview_type):
            query['previewType'] = request.preview_type
        if not UtilClient.is_unset(request.query_count):
            query['queryCount'] = request.query_count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSceneItems',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/items',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListSceneItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scene_parameters(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ListSceneParametersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_scene_parameters_with_options(instance_id, headers, runtime)

    async def list_scene_parameters_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ListSceneParametersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_scene_parameters_with_options_async(instance_id, headers, runtime)

    def list_scene_parameters_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListSceneParametersResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSceneParameters',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/dashboard/scene-parameters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListSceneParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scene_parameters_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListSceneParametersResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSceneParameters',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/dashboard/scene-parameters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListSceneParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scenes(
        self,
        instance_id: str,
        request: airec_20201126_models.ListScenesRequest,
    ) -> airec_20201126_models.ListScenesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_scenes_with_options(instance_id, request, headers, runtime)

    async def list_scenes_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListScenesRequest,
    ) -> airec_20201126_models.ListScenesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_scenes_with_options_async(instance_id, request, headers, runtime)

    def list_scenes_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListScenesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListScenesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.scene_id):
            query['sceneId'] = request.scene_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScenes',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListScenesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scenes_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListScenesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListScenesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.scene_id):
            query['sceneId'] = request.scene_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScenes',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListScenesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_umeng_appkeys(self) -> airec_20201126_models.ListUmengAppkeysResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_umeng_appkeys_with_options(headers, runtime)

    async def list_umeng_appkeys_async(self) -> airec_20201126_models.ListUmengAppkeysResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_umeng_appkeys_with_options_async(headers, runtime)

    def list_umeng_appkeys_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListUmengAppkeysResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListUmengAppkeys',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/umeng/appkeys',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListUmengAppkeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_umeng_appkeys_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListUmengAppkeysResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListUmengAppkeys',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/umeng/appkeys',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListUmengAppkeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_clusters(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ListUserClustersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_user_clusters_with_options(instance_id, headers, runtime)

    async def list_user_clusters_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ListUserClustersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_user_clusters_with_options_async(instance_id, headers, runtime)

    def list_user_clusters_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListUserClustersResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListUserClusters',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/user-clusters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListUserClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_clusters_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListUserClustersResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListUserClusters',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/user-clusters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListUserClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_data_source(
        self,
        instance_id: str,
        table_name: str,
    ) -> airec_20201126_models.ModifyDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_data_source_with_options(instance_id, table_name, headers, runtime)

    async def modify_data_source_async(
        self,
        instance_id: str,
        table_name: str,
    ) -> airec_20201126_models.ModifyDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_data_source_with_options_async(instance_id, table_name, headers, runtime)

    def modify_data_source_with_options(
        self,
        instance_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifyDataSourceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyDataSource',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/dataSources/{{tableName}}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ModifyDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_data_source_with_options_async(
        self,
        instance_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifyDataSourceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyDataSource',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/dataSources/{{tableName}}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ModifyDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_filtering_algorithm_meta(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.ModifyFilteringAlgorithmMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_filtering_algorithm_meta_with_options(instance_id, algorithm_id, headers, runtime)

    async def modify_filtering_algorithm_meta_async(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.ModifyFilteringAlgorithmMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_filtering_algorithm_meta_with_options_async(instance_id, algorithm_id, headers, runtime)

    def modify_filtering_algorithm_meta_with_options(
        self,
        instance_id: str,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifyFilteringAlgorithmMetaResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyFilteringAlgorithmMeta',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/filtering-algorithms/{{algorithmId}}/meta',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ModifyFilteringAlgorithmMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_filtering_algorithm_meta_with_options_async(
        self,
        instance_id: str,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifyFilteringAlgorithmMetaResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyFilteringAlgorithmMeta',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/filtering-algorithms/{{algorithmId}}/meta',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ModifyFilteringAlgorithmMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ModifyInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_instance_with_options(instance_id, headers, runtime)

    async def modify_instance_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ModifyInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_instance_with_options_async(instance_id, headers, runtime)

    def modify_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifyInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyInstance',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ModifyInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifyInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyInstance',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ModifyInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_items(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ModifyItemsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_items_with_options(instance_id, headers, runtime)

    async def modify_items_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ModifyItemsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_items_with_options_async(instance_id, headers, runtime)

    def modify_items_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifyItemsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyItems',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/items',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ModifyItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_items_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifyItemsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyItems',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/items',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ModifyItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_ranking_model(
        self,
        instance_id: str,
        ranking_model_id: str,
    ) -> airec_20201126_models.ModifyRankingModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_ranking_model_with_options(instance_id, ranking_model_id, headers, runtime)

    async def modify_ranking_model_async(
        self,
        instance_id: str,
        ranking_model_id: str,
    ) -> airec_20201126_models.ModifyRankingModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_ranking_model_with_options_async(instance_id, ranking_model_id, headers, runtime)

    def modify_ranking_model_with_options(
        self,
        instance_id: str,
        ranking_model_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifyRankingModelResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyRankingModel',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/ranking-models/{{rankingModelId}}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ModifyRankingModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_ranking_model_with_options_async(
        self,
        instance_id: str,
        ranking_model_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifyRankingModelResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyRankingModel',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/ranking-models/{{rankingModelId}}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ModifyRankingModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_rule(
        self,
        instance_id: str,
        rule_id: str,
    ) -> airec_20201126_models.ModifyRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_rule_with_options(instance_id, rule_id, headers, runtime)

    async def modify_rule_async(
        self,
        instance_id: str,
        rule_id: str,
    ) -> airec_20201126_models.ModifyRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_rule_with_options_async(instance_id, rule_id, headers, runtime)

    def modify_rule_with_options(
        self,
        instance_id: str,
        rule_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifyRuleResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyRule',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/rules/{{ruleId}}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ModifyRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_rule_with_options_async(
        self,
        instance_id: str,
        rule_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifyRuleResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyRule',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/rules/{{ruleId}}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ModifyRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_scene(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.ModifySceneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_scene_with_options(instance_id, scene_id, headers, runtime)

    async def modify_scene_async(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.ModifySceneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_scene_with_options_async(instance_id, scene_id, headers, runtime)

    def modify_scene_with_options(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifySceneResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyScene',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ModifySceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scene_with_options_async(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifySceneResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyScene',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ModifySceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def offline_filtering_algorithm(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.OfflineFilteringAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.offline_filtering_algorithm_with_options(instance_id, algorithm_id, headers, runtime)

    async def offline_filtering_algorithm_async(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.OfflineFilteringAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.offline_filtering_algorithm_with_options_async(instance_id, algorithm_id, headers, runtime)

    def offline_filtering_algorithm_with_options(
        self,
        instance_id: str,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.OfflineFilteringAlgorithmResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='OfflineFilteringAlgorithm',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/filtering-algorithms/{{algorithmId}}/actions/offline',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.OfflineFilteringAlgorithmResponse(),
            self.call_api(params, req, runtime)
        )

    async def offline_filtering_algorithm_with_options_async(
        self,
        instance_id: str,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.OfflineFilteringAlgorithmResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='OfflineFilteringAlgorithm',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/filtering-algorithms/{{algorithmId}}/actions/offline',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.OfflineFilteringAlgorithmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_rule(
        self,
        rule_id: str,
        instance_id: str,
        request: airec_20201126_models.PublishRuleRequest,
    ) -> airec_20201126_models.PublishRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.publish_rule_with_options(rule_id, instance_id, request, headers, runtime)

    async def publish_rule_async(
        self,
        rule_id: str,
        instance_id: str,
        request: airec_20201126_models.PublishRuleRequest,
    ) -> airec_20201126_models.PublishRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.publish_rule_with_options_async(rule_id, instance_id, request, headers, runtime)

    def publish_rule_with_options(
        self,
        rule_id: str,
        instance_id: str,
        request: airec_20201126_models.PublishRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.PublishRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_type):
            query['ruleType'] = request.rule_type
        if not UtilClient.is_unset(request.scene_id):
            query['sceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishRule',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/rules/{{ruleId}}/actions/publish',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.PublishRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_rule_with_options_async(
        self,
        rule_id: str,
        instance_id: str,
        request: airec_20201126_models.PublishRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.PublishRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_type):
            query['ruleType'] = request.rule_type
        if not UtilClient.is_unset(request.scene_id):
            query['sceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishRule',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/rules/{{ruleId}}/actions/publish',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.PublishRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_document(
        self,
        instance_id: str,
        table_name: str,
    ) -> airec_20201126_models.PushDocumentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_document_with_options(instance_id, table_name, headers, runtime)

    async def push_document_async(
        self,
        instance_id: str,
        table_name: str,
    ) -> airec_20201126_models.PushDocumentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.push_document_with_options_async(instance_id, table_name, headers, runtime)

    def push_document_with_options(
        self,
        instance_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.PushDocumentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PushDocument',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/tables/{{tableName}}/actions/bulk',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.PushDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_document_with_options_async(
        self,
        instance_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.PushDocumentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PushDocument',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/tables/{{tableName}}/actions/bulk',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.PushDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_intervention(
        self,
        instance_id: str,
    ) -> airec_20201126_models.PushInterventionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_intervention_with_options(instance_id, headers, runtime)

    async def push_intervention_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.PushInterventionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.push_intervention_with_options_async(instance_id, headers, runtime)

    def push_intervention_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.PushInterventionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PushIntervention',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/actions/intervene',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.PushInterventionResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_intervention_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.PushInterventionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PushIntervention',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/actions/intervene',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.PushInterventionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_data_message(
        self,
        instance_id: str,
        table: str,
        request: airec_20201126_models.QueryDataMessageRequest,
    ) -> airec_20201126_models.QueryDataMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_data_message_with_options(instance_id, table, request, headers, runtime)

    async def query_data_message_async(
        self,
        instance_id: str,
        table: str,
        request: airec_20201126_models.QueryDataMessageRequest,
    ) -> airec_20201126_models.QueryDataMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_data_message_with_options_async(instance_id, table, request, headers, runtime)

    def query_data_message_with_options(
        self,
        instance_id: str,
        table: str,
        request: airec_20201126_models.QueryDataMessageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.QueryDataMessageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.cmd_type):
            query['cmdType'] = request.cmd_type
        if not UtilClient.is_unset(request.item_id):
            query['itemId'] = request.item_id
        if not UtilClient.is_unset(request.item_type):
            query['itemType'] = request.item_type
        if not UtilClient.is_unset(request.user_id):
            query['userId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            query['userType'] = request.user_type
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.trace_id):
            query['traceId'] = request.trace_id
        if not UtilClient.is_unset(request.scene_id):
            query['sceneId'] = request.scene_id
        if not UtilClient.is_unset(request.bhv_type):
            query['bhvType'] = request.bhv_type
        if not UtilClient.is_unset(request.message_source):
            query['messageSource'] = request.message_source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDataMessage',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/tables/{{table}}/data-message',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.QueryDataMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_data_message_with_options_async(
        self,
        instance_id: str,
        table: str,
        request: airec_20201126_models.QueryDataMessageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.QueryDataMessageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.cmd_type):
            query['cmdType'] = request.cmd_type
        if not UtilClient.is_unset(request.item_id):
            query['itemId'] = request.item_id
        if not UtilClient.is_unset(request.item_type):
            query['itemType'] = request.item_type
        if not UtilClient.is_unset(request.user_id):
            query['userId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            query['userType'] = request.user_type
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.trace_id):
            query['traceId'] = request.trace_id
        if not UtilClient.is_unset(request.scene_id):
            query['sceneId'] = request.scene_id
        if not UtilClient.is_unset(request.bhv_type):
            query['bhvType'] = request.bhv_type
        if not UtilClient.is_unset(request.message_source):
            query['messageSource'] = request.message_source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDataMessage',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/tables/{{table}}/data-message',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.QueryDataMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_data_message_statistics(
        self,
        instance_id: str,
        table: str,
        request: airec_20201126_models.QueryDataMessageStatisticsRequest,
    ) -> airec_20201126_models.QueryDataMessageStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_data_message_statistics_with_options(instance_id, table, request, headers, runtime)

    async def query_data_message_statistics_async(
        self,
        instance_id: str,
        table: str,
        request: airec_20201126_models.QueryDataMessageStatisticsRequest,
    ) -> airec_20201126_models.QueryDataMessageStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_data_message_statistics_with_options_async(instance_id, table, request, headers, runtime)

    def query_data_message_statistics_with_options(
        self,
        instance_id: str,
        table: str,
        request: airec_20201126_models.QueryDataMessageStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.QueryDataMessageStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.cmd_type):
            query['cmdType'] = request.cmd_type
        if not UtilClient.is_unset(request.item_id):
            query['itemId'] = request.item_id
        if not UtilClient.is_unset(request.item_type):
            query['itemType'] = request.item_type
        if not UtilClient.is_unset(request.user_id):
            query['userId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            query['userType'] = request.user_type
        if not UtilClient.is_unset(request.trace_id):
            query['traceId'] = request.trace_id
        if not UtilClient.is_unset(request.scene_id):
            query['sceneId'] = request.scene_id
        if not UtilClient.is_unset(request.bhv_type):
            query['bhvType'] = request.bhv_type
        if not UtilClient.is_unset(request.message_source):
            query['messageSource'] = request.message_source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDataMessageStatistics',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/tables/{{table}}/data-message-statistics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.QueryDataMessageStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_data_message_statistics_with_options_async(
        self,
        instance_id: str,
        table: str,
        request: airec_20201126_models.QueryDataMessageStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.QueryDataMessageStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.cmd_type):
            query['cmdType'] = request.cmd_type
        if not UtilClient.is_unset(request.item_id):
            query['itemId'] = request.item_id
        if not UtilClient.is_unset(request.item_type):
            query['itemType'] = request.item_type
        if not UtilClient.is_unset(request.user_id):
            query['userId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            query['userType'] = request.user_type
        if not UtilClient.is_unset(request.trace_id):
            query['traceId'] = request.trace_id
        if not UtilClient.is_unset(request.scene_id):
            query['sceneId'] = request.scene_id
        if not UtilClient.is_unset(request.bhv_type):
            query['bhvType'] = request.bhv_type
        if not UtilClient.is_unset(request.message_source):
            query['messageSource'] = request.message_source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDataMessageStatistics',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/tables/{{table}}/data-message-statistics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.QueryDataMessageStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_exception_history(
        self,
        instance_id: str,
        request: airec_20201126_models.QueryExceptionHistoryRequest,
    ) -> airec_20201126_models.QueryExceptionHistoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_exception_history_with_options(instance_id, request, headers, runtime)

    async def query_exception_history_async(
        self,
        instance_id: str,
        request: airec_20201126_models.QueryExceptionHistoryRequest,
    ) -> airec_20201126_models.QueryExceptionHistoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_exception_history_with_options_async(instance_id, request, headers, runtime)

    def query_exception_history_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.QueryExceptionHistoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.QueryExceptionHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryExceptionHistory',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/sync-reports/exception-history',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.QueryExceptionHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_exception_history_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.QueryExceptionHistoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.QueryExceptionHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryExceptionHistory',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/sync-reports/exception-history',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.QueryExceptionHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_raw_data(
        self,
        instance_id: str,
        table: str,
        request: airec_20201126_models.QueryRawDataRequest,
    ) -> airec_20201126_models.QueryRawDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_raw_data_with_options(instance_id, table, request, headers, runtime)

    async def query_raw_data_async(
        self,
        instance_id: str,
        table: str,
        request: airec_20201126_models.QueryRawDataRequest,
    ) -> airec_20201126_models.QueryRawDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_raw_data_with_options_async(instance_id, table, request, headers, runtime)

    def query_raw_data_with_options(
        self,
        instance_id: str,
        table: str,
        request: airec_20201126_models.QueryRawDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.QueryRawDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.item_id):
            query['itemId'] = request.item_id
        if not UtilClient.is_unset(request.item_type):
            query['itemType'] = request.item_type
        if not UtilClient.is_unset(request.user_id):
            query['userId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            query['userType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRawData',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/tables/{{table}}/raw-data',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.QueryRawDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_raw_data_with_options_async(
        self,
        instance_id: str,
        table: str,
        request: airec_20201126_models.QueryRawDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.QueryRawDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.item_id):
            query['itemId'] = request.item_id
        if not UtilClient.is_unset(request.item_type):
            query['itemType'] = request.item_type
        if not UtilClient.is_unset(request.user_id):
            query['userId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            query['userType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRawData',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/tables/{{table}}/raw-data',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.QueryRawDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_single_aggregation_report(
        self,
        instance_id: str,
    ) -> airec_20201126_models.QuerySingleAggregationReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_single_aggregation_report_with_options(instance_id, headers, runtime)

    async def query_single_aggregation_report_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.QuerySingleAggregationReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_single_aggregation_report_with_options_async(instance_id, headers, runtime)

    def query_single_aggregation_report_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.QuerySingleAggregationReportResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='QuerySingleAggregationReport',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/sync-reports/single-aggregation-report',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.QuerySingleAggregationReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_single_aggregation_report_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.QuerySingleAggregationReportResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='QuerySingleAggregationReport',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/sync-reports/single-aggregation-report',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.QuerySingleAggregationReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_single_report(
        self,
        instance_id: str,
        request: airec_20201126_models.QuerySingleReportRequest,
    ) -> airec_20201126_models.QuerySingleReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_single_report_with_options(instance_id, request, headers, runtime)

    async def query_single_report_async(
        self,
        instance_id: str,
        request: airec_20201126_models.QuerySingleReportRequest,
    ) -> airec_20201126_models.QuerySingleReportResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_single_report_with_options_async(instance_id, request, headers, runtime)

    def query_single_report_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.QuerySingleReportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.QuerySingleReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.report_type):
            query['reportType'] = request.report_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySingleReport',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/sync-reports/single-report',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.QuerySingleReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_single_report_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.QuerySingleReportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.QuerySingleReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.report_type):
            query['reportType'] = request.report_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySingleReport',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/sync-reports/single-report',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.QuerySingleReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sync_report_aggregation(
        self,
        instance_id: str,
        request: airec_20201126_models.QuerySyncReportAggregationRequest,
    ) -> airec_20201126_models.QuerySyncReportAggregationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_sync_report_aggregation_with_options(instance_id, request, headers, runtime)

    async def query_sync_report_aggregation_async(
        self,
        instance_id: str,
        request: airec_20201126_models.QuerySyncReportAggregationRequest,
    ) -> airec_20201126_models.QuerySyncReportAggregationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_sync_report_aggregation_with_options_async(instance_id, request, headers, runtime)

    def query_sync_report_aggregation_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.QuerySyncReportAggregationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.QuerySyncReportAggregationResponse:
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
        params = open_api_models.Params(
            action='QuerySyncReportAggregation',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/sync-reports/aggregation',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.QuerySyncReportAggregationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sync_report_aggregation_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.QuerySyncReportAggregationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.QuerySyncReportAggregationResponse:
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
        params = open_api_models.Params(
            action='QuerySyncReportAggregation',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/sync-reports/aggregation',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.QuerySyncReportAggregationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rebuild_index(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.RebuildIndexResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rebuild_index_with_options(instance_id, algorithm_id, headers, runtime)

    async def rebuild_index_async(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.RebuildIndexResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.rebuild_index_with_options_async(instance_id, algorithm_id, headers, runtime)

    def rebuild_index_with_options(
        self,
        instance_id: str,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.RebuildIndexResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RebuildIndex',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/filtering-algorithms/{{algorithmId}}/actions/rebuild',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.RebuildIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def rebuild_index_with_options_async(
        self,
        instance_id: str,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.RebuildIndexResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RebuildIndex',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/filtering-algorithms/{{algorithmId}}/actions/rebuild',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.RebuildIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recommend(
        self,
        instance_id: str,
        request: airec_20201126_models.RecommendRequest,
    ) -> airec_20201126_models.RecommendResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.recommend_with_options(instance_id, request, headers, runtime)

    async def recommend_async(
        self,
        instance_id: str,
        request: airec_20201126_models.RecommendRequest,
    ) -> airec_20201126_models.RecommendResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.recommend_with_options_async(instance_id, request, headers, runtime)

    def recommend_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.RecommendRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.RecommendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['sceneId'] = request.scene_id
        if not UtilClient.is_unset(request.user_id):
            query['userId'] = request.user_id
        if not UtilClient.is_unset(request.ip):
            query['ip'] = request.ip
        if not UtilClient.is_unset(request.imei):
            query['imei'] = request.imei
        if not UtilClient.is_unset(request.return_count):
            query['returnCount'] = request.return_count
        if not UtilClient.is_unset(request.items):
            query['items'] = request.items
        if not UtilClient.is_unset(request.service_type):
            query['serviceType'] = request.service_type
        if not UtilClient.is_unset(request.user_info):
            query['userInfo'] = request.user_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Recommend',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/actions/recommend',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.RecommendResponse(),
            self.call_api(params, req, runtime)
        )

    async def recommend_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.RecommendRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.RecommendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['sceneId'] = request.scene_id
        if not UtilClient.is_unset(request.user_id):
            query['userId'] = request.user_id
        if not UtilClient.is_unset(request.ip):
            query['ip'] = request.ip
        if not UtilClient.is_unset(request.imei):
            query['imei'] = request.imei
        if not UtilClient.is_unset(request.return_count):
            query['returnCount'] = request.return_count
        if not UtilClient.is_unset(request.items):
            query['items'] = request.items
        if not UtilClient.is_unset(request.service_type):
            query['serviceType'] = request.service_type
        if not UtilClient.is_unset(request.user_info):
            query['userInfo'] = request.user_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Recommend',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/actions/recommend',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.RecommendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_instance(
        self,
        instance_id: str,
    ) -> airec_20201126_models.RunInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_instance_with_options(instance_id, headers, runtime)

    async def run_instance_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.RunInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_instance_with_options_async(instance_id, headers, runtime)

    def run_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.RunInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RunInstance',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/actions/import',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.RunInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.RunInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RunInstance',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/actions/import',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.RunInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_data_set(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20201126_models.StopDataSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_data_set_with_options(instance_id, version_id, headers, runtime)

    async def stop_data_set_async(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20201126_models.StopDataSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_data_set_with_options_async(instance_id, version_id, headers, runtime)

    def stop_data_set_with_options(
        self,
        instance_id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.StopDataSetResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopDataSet',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/dataSets/{{versionId}}/actions/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.StopDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_data_set_with_options_async(
        self,
        instance_id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.StopDataSetResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopDataSet',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/dataSets/{{versionId}}/actions/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.StopDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_lock_index_version(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.UnLockIndexVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.un_lock_index_version_with_options(instance_id, algorithm_id, headers, runtime)

    async def un_lock_index_version_async(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.UnLockIndexVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.un_lock_index_version_with_options_async(instance_id, algorithm_id, headers, runtime)

    def un_lock_index_version_with_options(
        self,
        instance_id: str,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.UnLockIndexVersionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UnLockIndexVersion',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/filtering-algorithms/{{algorithmId}}/actions/unlock',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.UnLockIndexVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_lock_index_version_with_options_async(
        self,
        instance_id: str,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.UnLockIndexVersionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UnLockIndexVersion',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/filtering-algorithms/{{algorithmId}}/actions/unlock',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.UnLockIndexVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_experiment_basic_info(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
    ) -> airec_20201126_models.UpdateExperimentBasicInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_experiment_basic_info_with_options(instance_id, scene_id, experiment_id, headers, runtime)

    async def update_experiment_basic_info_async(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
    ) -> airec_20201126_models.UpdateExperimentBasicInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_experiment_basic_info_with_options_async(instance_id, scene_id, experiment_id, headers, runtime)

    def update_experiment_basic_info_with_options(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.UpdateExperimentBasicInfoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateExperimentBasicInfo',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/experiments/{{experimentId}}/basic',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.UpdateExperimentBasicInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_experiment_basic_info_with_options_async(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.UpdateExperimentBasicInfoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateExperimentBasicInfo',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/experiments/{{experimentId}}/basic',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.UpdateExperimentBasicInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_experiment_config(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
    ) -> airec_20201126_models.UpdateExperimentConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_experiment_config_with_options(instance_id, scene_id, experiment_id, headers, runtime)

    async def update_experiment_config_async(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
    ) -> airec_20201126_models.UpdateExperimentConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_experiment_config_with_options_async(instance_id, scene_id, experiment_id, headers, runtime)

    def update_experiment_config_with_options(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.UpdateExperimentConfigResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateExperimentConfig',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/experiments/{{experimentId}}/config',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.UpdateExperimentConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_experiment_config_with_options_async(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.UpdateExperimentConfigResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateExperimentConfig',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/experiments/{{experimentId}}/config',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.UpdateExperimentConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_experiment_status(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
    ) -> airec_20201126_models.UpdateExperimentStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_experiment_status_with_options(instance_id, scene_id, experiment_id, headers, runtime)

    async def update_experiment_status_async(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
    ) -> airec_20201126_models.UpdateExperimentStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_experiment_status_with_options_async(instance_id, scene_id, experiment_id, headers, runtime)

    def update_experiment_status_with_options(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.UpdateExperimentStatusResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateExperimentStatus',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/experiments/{{experimentId}}/status',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.UpdateExperimentStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_experiment_status_with_options_async(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.UpdateExperimentStatusResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateExperimentStatus',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/scenes/{{sceneId}}/experiments/{{experimentId}}/status',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.UpdateExperimentStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_instance(
        self,
        instance_id: str,
    ) -> airec_20201126_models.UpgradeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upgrade_instance_with_options(instance_id, headers, runtime)

    async def upgrade_instance_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.UpgradeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upgrade_instance_with_options_async(instance_id, headers, runtime)

    def upgrade_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.UpgradeInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpgradeInstance',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/actions/upgrade',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.UpgradeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.UpgradeInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpgradeInstance',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/actions/upgrade',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.UpgradeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_instance(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ValidateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.validate_instance_with_options(instance_id, headers, runtime)

    async def validate_instance_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ValidateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.validate_instance_with_options_async(instance_id, headers, runtime)

    def validate_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ValidateInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ValidateInstance',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/actions/validate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ValidateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ValidateInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ValidateInstance',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{instance_id}/actions/validate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ValidateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )
