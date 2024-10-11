# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_airec20201126 import models as airec_20201126_models
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

    def attach_dataset_with_options(
        self,
        instance_id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.AttachDatasetResponse:
        """
        @summary Uses a dataset of a specified version of a specified instance to provide online services.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachDatasetResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='AttachDataset',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/dataSets/{OpenApiUtilClient.get_encode_param(version_id)}/actions/current',
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
        """
        @summary Uses a dataset of a specified version of a specified instance to provide online services.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachDatasetResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='AttachDataset',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/dataSets/{OpenApiUtilClient.get_encode_param(version_id)}/actions/current',
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

    def attach_dataset(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20201126_models.AttachDatasetResponse:
        """
        @summary Uses a dataset of a specified version of a specified instance to provide online services.
        
        @return: AttachDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.attach_dataset_with_options(instance_id, version_id, headers, runtime)

    async def attach_dataset_async(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20201126_models.AttachDatasetResponse:
        """
        @summary Uses a dataset of a specified version of a specified instance to provide online services.
        
        @return: AttachDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.attach_dataset_with_options_async(instance_id, version_id, headers, runtime)

    def attach_index_version_with_options(
        self,
        instance_id: str,
        algorithm_id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.AttachIndexVersionResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachIndexVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='AttachIndexVersion',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/filtering-algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}/index-versions/{OpenApiUtilClient.get_encode_param(version_id)}/actions/attach',
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
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachIndexVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='AttachIndexVersion',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/filtering-algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}/index-versions/{OpenApiUtilClient.get_encode_param(version_id)}/actions/attach',
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

    def attach_index_version(
        self,
        instance_id: str,
        algorithm_id: str,
        version_id: str,
    ) -> airec_20201126_models.AttachIndexVersionResponse:
        """
        @return: AttachIndexVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.attach_index_version_with_options(instance_id, algorithm_id, version_id, headers, runtime)

    async def attach_index_version_async(
        self,
        instance_id: str,
        algorithm_id: str,
        version_id: str,
    ) -> airec_20201126_models.AttachIndexVersionResponse:
        """
        @return: AttachIndexVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.attach_index_version_with_options_async(instance_id, algorithm_id, version_id, headers, runtime)

    def check_ranking_model_reachable_with_options(
        self,
        instance_id: str,
        ranking_model_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CheckRankingModelReachableResponse:
        """
        @summary Checks the network connectivity of a ranking model.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckRankingModelReachableResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CheckRankingModelReachable',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-models/{OpenApiUtilClient.get_encode_param(ranking_model_id)}/actions/check-connectivity',
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
        """
        @summary Checks the network connectivity of a ranking model.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckRankingModelReachableResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CheckRankingModelReachable',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-models/{OpenApiUtilClient.get_encode_param(ranking_model_id)}/actions/check-connectivity',
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

    def check_ranking_model_reachable(
        self,
        instance_id: str,
        ranking_model_id: str,
    ) -> airec_20201126_models.CheckRankingModelReachableResponse:
        """
        @summary Checks the network connectivity of a ranking model.
        
        @return: CheckRankingModelReachableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_ranking_model_reachable_with_options(instance_id, ranking_model_id, headers, runtime)

    async def check_ranking_model_reachable_async(
        self,
        instance_id: str,
        ranking_model_id: str,
    ) -> airec_20201126_models.CheckRankingModelReachableResponse:
        """
        @summary Checks the network connectivity of a ranking model.
        
        @return: CheckRankingModelReachableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.check_ranking_model_reachable_with_options_async(instance_id, ranking_model_id, headers, runtime)

    def clone_experiment_with_options(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
        request: airec_20201126_models.CloneExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CloneExperimentResponse:
        """
        @summary Clones an experiment.
        
        @param request: CloneExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneExperimentResponse
        """
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
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}/actions/clone',
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
        """
        @summary Clones an experiment.
        
        @param request: CloneExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneExperimentResponse
        """
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
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}/actions/clone',
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

    def clone_experiment(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
        request: airec_20201126_models.CloneExperimentRequest,
    ) -> airec_20201126_models.CloneExperimentResponse:
        """
        @summary Clones an experiment.
        
        @param request: CloneExperimentRequest
        @return: CloneExperimentResponse
        """
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
        """
        @summary Clones an experiment.
        
        @param request: CloneExperimentRequest
        @return: CloneExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.clone_experiment_with_options_async(instance_id, scene_id, experiment_id, request, headers, runtime)

    def clone_sample_with_options(
        self,
        instance_id: str,
        sample_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CloneSampleResponse:
        """
        @summary Clones a sample.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneSampleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CloneSample',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/samples/{OpenApiUtilClient.get_encode_param(sample_id)}/actions/clone',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CloneSampleResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_sample_with_options_async(
        self,
        instance_id: str,
        sample_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CloneSampleResponse:
        """
        @summary Clones a sample.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneSampleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CloneSample',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/samples/{OpenApiUtilClient.get_encode_param(sample_id)}/actions/clone',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CloneSampleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_sample(
        self,
        instance_id: str,
        sample_id: str,
    ) -> airec_20201126_models.CloneSampleResponse:
        """
        @summary Clones a sample.
        
        @return: CloneSampleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clone_sample_with_options(instance_id, sample_id, headers, runtime)

    async def clone_sample_async(
        self,
        instance_id: str,
        sample_id: str,
    ) -> airec_20201126_models.CloneSampleResponse:
        """
        @summary Clones a sample.
        
        @return: CloneSampleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.clone_sample_with_options_async(instance_id, sample_id, headers, runtime)

    def cold_start_rank_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ColdStartRankRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ColdStartRankResponse:
        """
        @summary 该接口用于获取指定冷启动实例的排序结果。
        
        @param request: ColdStartRankRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ColdStartRankResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.features):
            query['features'] = request.features
        if not UtilClient.is_unset(request.imei):
            query['imei'] = request.imei
        if not UtilClient.is_unset(request.items):
            query['items'] = request.items
        if not UtilClient.is_unset(request.scene_id):
            query['sceneId'] = request.scene_id
        if not UtilClient.is_unset(request.user_id):
            query['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ColdStartRank',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/cold-start/{OpenApiUtilClient.get_encode_param(instance_id)}/actions/rank',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ColdStartRankResponse(),
            self.call_api(params, req, runtime)
        )

    async def cold_start_rank_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ColdStartRankRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ColdStartRankResponse:
        """
        @summary 该接口用于获取指定冷启动实例的排序结果。
        
        @param request: ColdStartRankRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ColdStartRankResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.features):
            query['features'] = request.features
        if not UtilClient.is_unset(request.imei):
            query['imei'] = request.imei
        if not UtilClient.is_unset(request.items):
            query['items'] = request.items
        if not UtilClient.is_unset(request.scene_id):
            query['sceneId'] = request.scene_id
        if not UtilClient.is_unset(request.user_id):
            query['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ColdStartRank',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/cold-start/{OpenApiUtilClient.get_encode_param(instance_id)}/actions/rank',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ColdStartRankResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cold_start_rank(
        self,
        instance_id: str,
        request: airec_20201126_models.ColdStartRankRequest,
    ) -> airec_20201126_models.ColdStartRankResponse:
        """
        @summary 该接口用于获取指定冷启动实例的排序结果。
        
        @param request: ColdStartRankRequest
        @return: ColdStartRankResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cold_start_rank_with_options(instance_id, request, headers, runtime)

    async def cold_start_rank_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ColdStartRankRequest,
    ) -> airec_20201126_models.ColdStartRankResponse:
        """
        @summary 该接口用于获取指定冷启动实例的排序结果。
        
        @param request: ColdStartRankRequest
        @return: ColdStartRankResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cold_start_rank_with_options_async(instance_id, request, headers, runtime)

    def create_custom_analysis_task_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.CreateCustomAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateCustomAnalysisTaskResponse:
        """
        @summary 创建自定义分析任务
        
        @param request: CreateCustomAnalysisTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomAnalysisTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomAnalysisTask',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/dashboard/custom-analysis-tasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CreateCustomAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_analysis_task_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.CreateCustomAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateCustomAnalysisTaskResponse:
        """
        @summary 创建自定义分析任务
        
        @param request: CreateCustomAnalysisTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomAnalysisTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomAnalysisTask',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/dashboard/custom-analysis-tasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CreateCustomAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_analysis_task(
        self,
        instance_id: str,
        request: airec_20201126_models.CreateCustomAnalysisTaskRequest,
    ) -> airec_20201126_models.CreateCustomAnalysisTaskResponse:
        """
        @summary 创建自定义分析任务
        
        @param request: CreateCustomAnalysisTaskRequest
        @return: CreateCustomAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_custom_analysis_task_with_options(instance_id, request, headers, runtime)

    async def create_custom_analysis_task_async(
        self,
        instance_id: str,
        request: airec_20201126_models.CreateCustomAnalysisTaskRequest,
    ) -> airec_20201126_models.CreateCustomAnalysisTaskResponse:
        """
        @summary 创建自定义分析任务
        
        @param request: CreateCustomAnalysisTaskRequest
        @return: CreateCustomAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_custom_analysis_task_with_options_async(instance_id, request, headers, runtime)

    def create_custom_sample_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateCustomSampleResponse:
        """
        @summary 创建自定义样本
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomSampleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateCustomSample',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/samples',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CreateCustomSampleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_sample_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateCustomSampleResponse:
        """
        @summary 创建自定义样本
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomSampleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateCustomSample',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/samples',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CreateCustomSampleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_sample(
        self,
        instance_id: str,
    ) -> airec_20201126_models.CreateCustomSampleResponse:
        """
        @summary 创建自定义样本
        
        @return: CreateCustomSampleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_custom_sample_with_options(instance_id, headers, runtime)

    async def create_custom_sample_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.CreateCustomSampleResponse:
        """
        @summary 创建自定义样本
        
        @return: CreateCustomSampleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_custom_sample_with_options_async(instance_id, headers, runtime)

    def create_data_diagnose_task_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateDataDiagnoseTaskResponse:
        """
        @summary 创建数据诊断任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataDiagnoseTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateDataDiagnoseTask',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-diagnose-task',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CreateDataDiagnoseTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_diagnose_task_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateDataDiagnoseTaskResponse:
        """
        @summary 创建数据诊断任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataDiagnoseTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateDataDiagnoseTask',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-diagnose-task',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CreateDataDiagnoseTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_diagnose_task(
        self,
        instance_id: str,
    ) -> airec_20201126_models.CreateDataDiagnoseTaskResponse:
        """
        @summary 创建数据诊断任务
        
        @return: CreateDataDiagnoseTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_data_diagnose_task_with_options(instance_id, headers, runtime)

    async def create_data_diagnose_task_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.CreateDataDiagnoseTaskResponse:
        """
        @summary 创建数据诊断任务
        
        @return: CreateDataDiagnoseTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_data_diagnose_task_with_options_async(instance_id, headers, runtime)

    def create_extra_data_source_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateExtraDataSourceResponse:
        """
        @summary Creates a data source.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateExtraDataSourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateExtraDataSource',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/extra-data-sources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CreateExtraDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_extra_data_source_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateExtraDataSourceResponse:
        """
        @summary Creates a data source.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateExtraDataSourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateExtraDataSource',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/extra-data-sources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CreateExtraDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_extra_data_source(
        self,
        instance_id: str,
    ) -> airec_20201126_models.CreateExtraDataSourceResponse:
        """
        @summary Creates a data source.
        
        @return: CreateExtraDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_extra_data_source_with_options(instance_id, headers, runtime)

    async def create_extra_data_source_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.CreateExtraDataSourceResponse:
        """
        @summary Creates a data source.
        
        @return: CreateExtraDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_extra_data_source_with_options_async(instance_id, headers, runtime)

    def create_filtering_algorithm_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.CreateFilteringAlgorithmRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateFilteringAlgorithmResponse:
        """
        @summary The time when the filtering table was created.
        
        @param request: CreateFilteringAlgorithmRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFilteringAlgorithmResponse
        """
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
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/filtering-algorithms',
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
        """
        @summary The time when the filtering table was created.
        
        @param request: CreateFilteringAlgorithmRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFilteringAlgorithmResponse
        """
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
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/filtering-algorithms',
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

    def create_filtering_algorithm(
        self,
        instance_id: str,
        request: airec_20201126_models.CreateFilteringAlgorithmRequest,
    ) -> airec_20201126_models.CreateFilteringAlgorithmResponse:
        """
        @summary The time when the filtering table was created.
        
        @param request: CreateFilteringAlgorithmRequest
        @return: CreateFilteringAlgorithmResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_filtering_algorithm_with_options(instance_id, request, headers, runtime)

    async def create_filtering_algorithm_async(
        self,
        instance_id: str,
        request: airec_20201126_models.CreateFilteringAlgorithmRequest,
    ) -> airec_20201126_models.CreateFilteringAlgorithmResponse:
        """
        @summary The time when the filtering table was created.
        
        @param request: CreateFilteringAlgorithmRequest
        @return: CreateFilteringAlgorithmResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_filtering_algorithm_with_options_async(instance_id, request, headers, runtime)

    def create_flow_control_task_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.CreateFlowControlTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateFlowControlTaskResponse:
        """
        @summary Creates a throttling task.
        
        @param request: CreateFlowControlTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFlowControlTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowControlTask',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/flowControlTasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CreateFlowControlTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_control_task_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.CreateFlowControlTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateFlowControlTaskResponse:
        """
        @summary Creates a throttling task.
        
        @param request: CreateFlowControlTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFlowControlTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowControlTask',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/flowControlTasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CreateFlowControlTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_flow_control_task(
        self,
        instance_id: str,
        request: airec_20201126_models.CreateFlowControlTaskRequest,
    ) -> airec_20201126_models.CreateFlowControlTaskResponse:
        """
        @summary Creates a throttling task.
        
        @param request: CreateFlowControlTaskRequest
        @return: CreateFlowControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_flow_control_task_with_options(instance_id, request, headers, runtime)

    async def create_flow_control_task_async(
        self,
        instance_id: str,
        request: airec_20201126_models.CreateFlowControlTaskRequest,
    ) -> airec_20201126_models.CreateFlowControlTaskResponse:
        """
        @summary Creates a throttling task.
        
        @param request: CreateFlowControlTaskRequest
        @return: CreateFlowControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_flow_control_task_with_options_async(instance_id, request, headers, runtime)

    def create_instance_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateInstanceResponse:
        """
        @summary Creates an Artificial Intelligence Recommendation (AIRec) instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
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
        """
        @summary Creates an Artificial Intelligence Recommendation (AIRec) instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
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

    def create_instance(self) -> airec_20201126_models.CreateInstanceResponse:
        """
        @summary Creates an Artificial Intelligence Recommendation (AIRec) instance.
        
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_with_options(headers, runtime)

    async def create_instance_async(self) -> airec_20201126_models.CreateInstanceResponse:
        """
        @summary Creates an Artificial Intelligence Recommendation (AIRec) instance.
        
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_with_options_async(headers, runtime)

    def create_ranking_model_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.CreateRankingModelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateRankingModelResponse:
        """
        @param request: CreateRankingModelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRankingModelResponse
        """
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
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-models',
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
        """
        @param request: CreateRankingModelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRankingModelResponse
        """
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
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-models',
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

    def create_ranking_model(
        self,
        instance_id: str,
        request: airec_20201126_models.CreateRankingModelRequest,
    ) -> airec_20201126_models.CreateRankingModelResponse:
        """
        @param request: CreateRankingModelRequest
        @return: CreateRankingModelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_ranking_model_with_options(instance_id, request, headers, runtime)

    async def create_ranking_model_async(
        self,
        instance_id: str,
        request: airec_20201126_models.CreateRankingModelRequest,
    ) -> airec_20201126_models.CreateRankingModelResponse:
        """
        @param request: CreateRankingModelRequest
        @return: CreateRankingModelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_ranking_model_with_options_async(instance_id, request, headers, runtime)

    def create_ranking_model_template_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateRankingModelTemplateResponse:
        """
        @summary 创建排序模型模板配置
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRankingModelTemplateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateRankingModelTemplate',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-model-templates',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CreateRankingModelTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ranking_model_template_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateRankingModelTemplateResponse:
        """
        @summary 创建排序模型模板配置
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRankingModelTemplateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateRankingModelTemplate',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-model-templates',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CreateRankingModelTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ranking_model_template(
        self,
        instance_id: str,
    ) -> airec_20201126_models.CreateRankingModelTemplateResponse:
        """
        @summary 创建排序模型模板配置
        
        @return: CreateRankingModelTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_ranking_model_template_with_options(instance_id, headers, runtime)

    async def create_ranking_model_template_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.CreateRankingModelTemplateResponse:
        """
        @summary 创建排序模型模板配置
        
        @return: CreateRankingModelTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_ranking_model_template_with_options_async(instance_id, headers, runtime)

    def create_ranking_system_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateRankingSystemResponse:
        """
        @summary 创建排序服务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRankingSystemResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateRankingSystem',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-systems',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CreateRankingSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ranking_system_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateRankingSystemResponse:
        """
        @summary 创建排序服务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRankingSystemResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateRankingSystem',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-systems',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CreateRankingSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ranking_system(
        self,
        instance_id: str,
    ) -> airec_20201126_models.CreateRankingSystemResponse:
        """
        @summary 创建排序服务
        
        @return: CreateRankingSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_ranking_system_with_options(instance_id, headers, runtime)

    async def create_ranking_system_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.CreateRankingSystemResponse:
        """
        @summary 创建排序服务
        
        @return: CreateRankingSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_ranking_system_with_options_async(instance_id, headers, runtime)

    def create_rule_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateRuleResponse:
        """
        @summary Creates a rule.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRuleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateRule',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/rules',
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
        """
        @summary Creates a rule.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRuleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateRule',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/rules',
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

    def create_rule(
        self,
        instance_id: str,
    ) -> airec_20201126_models.CreateRuleResponse:
        """
        @summary Creates a rule.
        
        @return: CreateRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_rule_with_options(instance_id, headers, runtime)

    async def create_rule_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.CreateRuleResponse:
        """
        @summary Creates a rule.
        
        @return: CreateRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_rule_with_options_async(instance_id, headers, runtime)

    def create_sample_format_config_with_options(
        self,
        instance_id: str,
        sample_id: str,
        request: airec_20201126_models.CreateSampleFormatConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateSampleFormatConfigResponse:
        """
        @summary 创建样本格式化配置
        
        @param request: CreateSampleFormatConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSampleFormatConfigResponse
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
            action='CreateSampleFormatConfig',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/samples/{OpenApiUtilClient.get_encode_param(sample_id)}/format-configs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CreateSampleFormatConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sample_format_config_with_options_async(
        self,
        instance_id: str,
        sample_id: str,
        request: airec_20201126_models.CreateSampleFormatConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateSampleFormatConfigResponse:
        """
        @summary 创建样本格式化配置
        
        @param request: CreateSampleFormatConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSampleFormatConfigResponse
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
            action='CreateSampleFormatConfig',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/samples/{OpenApiUtilClient.get_encode_param(sample_id)}/format-configs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CreateSampleFormatConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sample_format_config(
        self,
        instance_id: str,
        sample_id: str,
        request: airec_20201126_models.CreateSampleFormatConfigRequest,
    ) -> airec_20201126_models.CreateSampleFormatConfigResponse:
        """
        @summary 创建样本格式化配置
        
        @param request: CreateSampleFormatConfigRequest
        @return: CreateSampleFormatConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_sample_format_config_with_options(instance_id, sample_id, request, headers, runtime)

    async def create_sample_format_config_async(
        self,
        instance_id: str,
        sample_id: str,
        request: airec_20201126_models.CreateSampleFormatConfigRequest,
    ) -> airec_20201126_models.CreateSampleFormatConfigResponse:
        """
        @summary 创建样本格式化配置
        
        @param request: CreateSampleFormatConfigRequest
        @return: CreateSampleFormatConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_sample_format_config_with_options_async(instance_id, sample_id, request, headers, runtime)

    def create_scene_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.CreateSceneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateSceneResponse:
        """
        @summary Verifies the information that you specified for creating a scene.
        
        @description We recommend that you do not call an API operation to manage scenes. We recommend that you go to the Scenario Building page in the Artificial Intelligence Recommendation (AIRec) console to manage scenes.
        
        @param request: CreateSceneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSceneResponse
        """
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
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes',
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
        """
        @summary Verifies the information that you specified for creating a scene.
        
        @description We recommend that you do not call an API operation to manage scenes. We recommend that you go to the Scenario Building page in the Artificial Intelligence Recommendation (AIRec) console to manage scenes.
        
        @param request: CreateSceneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSceneResponse
        """
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
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes',
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

    def create_scene(
        self,
        instance_id: str,
        request: airec_20201126_models.CreateSceneRequest,
    ) -> airec_20201126_models.CreateSceneResponse:
        """
        @summary Verifies the information that you specified for creating a scene.
        
        @description We recommend that you do not call an API operation to manage scenes. We recommend that you go to the Scenario Building page in the Artificial Intelligence Recommendation (AIRec) console to manage scenes.
        
        @param request: CreateSceneRequest
        @return: CreateSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_scene_with_options(instance_id, request, headers, runtime)

    async def create_scene_async(
        self,
        instance_id: str,
        request: airec_20201126_models.CreateSceneRequest,
    ) -> airec_20201126_models.CreateSceneResponse:
        """
        @summary Verifies the information that you specified for creating a scene.
        
        @description We recommend that you do not call an API operation to manage scenes. We recommend that you go to the Scenario Building page in the Artificial Intelligence Recommendation (AIRec) console to manage scenes.
        
        @param request: CreateSceneRequest
        @return: CreateSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_scene_with_options_async(instance_id, request, headers, runtime)

    def create_umeng_token_with_options(
        self,
        request: airec_20201126_models.CreateUmengTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateUmengTokenResponse:
        """
        @summary 创建友盟授权token
        
        @param request: CreateUmengTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUmengTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['code'] = request.code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUmengToken',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/umeng/token',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CreateUmengTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_umeng_token_with_options_async(
        self,
        request: airec_20201126_models.CreateUmengTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.CreateUmengTokenResponse:
        """
        @summary 创建友盟授权token
        
        @param request: CreateUmengTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUmengTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['code'] = request.code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUmengToken',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/umeng/token',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.CreateUmengTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_umeng_token(
        self,
        request: airec_20201126_models.CreateUmengTokenRequest,
    ) -> airec_20201126_models.CreateUmengTokenResponse:
        """
        @summary 创建友盟授权token
        
        @param request: CreateUmengTokenRequest
        @return: CreateUmengTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_umeng_token_with_options(request, headers, runtime)

    async def create_umeng_token_async(
        self,
        request: airec_20201126_models.CreateUmengTokenRequest,
    ) -> airec_20201126_models.CreateUmengTokenResponse:
        """
        @summary 创建友盟授权token
        
        @param request: CreateUmengTokenRequest
        @return: CreateUmengTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_umeng_token_with_options_async(request, headers, runtime)

    def decribe_ranking_model_with_options(
        self,
        instance_id: str,
        ranking_model_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DecribeRankingModelResponse:
        """
        @summary Queries the information of a ranking model.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DecribeRankingModelResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DecribeRankingModel',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-models/{OpenApiUtilClient.get_encode_param(ranking_model_id)}',
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
        """
        @summary Queries the information of a ranking model.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DecribeRankingModelResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DecribeRankingModel',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-models/{OpenApiUtilClient.get_encode_param(ranking_model_id)}',
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

    def decribe_ranking_model(
        self,
        instance_id: str,
        ranking_model_id: str,
    ) -> airec_20201126_models.DecribeRankingModelResponse:
        """
        @summary Queries the information of a ranking model.
        
        @return: DecribeRankingModelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.decribe_ranking_model_with_options(instance_id, ranking_model_id, headers, runtime)

    async def decribe_ranking_model_async(
        self,
        instance_id: str,
        ranking_model_id: str,
    ) -> airec_20201126_models.DecribeRankingModelResponse:
        """
        @summary Queries the information of a ranking model.
        
        @return: DecribeRankingModelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.decribe_ranking_model_with_options_async(instance_id, ranking_model_id, headers, runtime)

    def delete_data_set_with_options(
        self,
        instance_id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DeleteDataSetResponse:
        """
        @summary Deletes a dataset of a specified version for an instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataSetResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDataSet',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/dataSets/{OpenApiUtilClient.get_encode_param(version_id)}',
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
        """
        @summary Deletes a dataset of a specified version for an instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataSetResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDataSet',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/dataSets/{OpenApiUtilClient.get_encode_param(version_id)}',
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

    def delete_data_set(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20201126_models.DeleteDataSetResponse:
        """
        @summary Deletes a dataset of a specified version for an instance.
        
        @return: DeleteDataSetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_data_set_with_options(instance_id, version_id, headers, runtime)

    async def delete_data_set_async(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20201126_models.DeleteDataSetResponse:
        """
        @summary Deletes a dataset of a specified version for an instance.
        
        @return: DeleteDataSetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_data_set_with_options_async(instance_id, version_id, headers, runtime)

    def delete_experiment_with_options(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DeleteExperimentResponse:
        """
        @summary The ID of the test.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteExperiment',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}',
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
        """
        @summary The ID of the test.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteExperiment',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}',
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

    def delete_experiment(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
    ) -> airec_20201126_models.DeleteExperimentResponse:
        """
        @summary The ID of the test.
        
        @return: DeleteExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_experiment_with_options(instance_id, scene_id, experiment_id, headers, runtime)

    async def delete_experiment_async(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
    ) -> airec_20201126_models.DeleteExperimentResponse:
        """
        @summary The ID of the test.
        
        @return: DeleteExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_experiment_with_options_async(instance_id, scene_id, experiment_id, headers, runtime)

    def delete_extra_data_source_with_options(
        self,
        instance_id: str,
        type: str,
        data_source_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DeleteExtraDataSourceResponse:
        """
        @summary 删除特征、样本等表扩展数据源
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExtraDataSourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteExtraDataSource',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/extra-data-sources/{OpenApiUtilClient.get_encode_param(type)}/{OpenApiUtilClient.get_encode_param(data_source_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DeleteExtraDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_extra_data_source_with_options_async(
        self,
        instance_id: str,
        type: str,
        data_source_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DeleteExtraDataSourceResponse:
        """
        @summary 删除特征、样本等表扩展数据源
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExtraDataSourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteExtraDataSource',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/extra-data-sources/{OpenApiUtilClient.get_encode_param(type)}/{OpenApiUtilClient.get_encode_param(data_source_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DeleteExtraDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_extra_data_source(
        self,
        instance_id: str,
        type: str,
        data_source_id: str,
    ) -> airec_20201126_models.DeleteExtraDataSourceResponse:
        """
        @summary 删除特征、样本等表扩展数据源
        
        @return: DeleteExtraDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_extra_data_source_with_options(instance_id, type, data_source_id, headers, runtime)

    async def delete_extra_data_source_async(
        self,
        instance_id: str,
        type: str,
        data_source_id: str,
    ) -> airec_20201126_models.DeleteExtraDataSourceResponse:
        """
        @summary 删除特征、样本等表扩展数据源
        
        @return: DeleteExtraDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_extra_data_source_with_options_async(instance_id, type, data_source_id, headers, runtime)

    def delete_filtering_algorithm_with_options(
        self,
        instance_id: str,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DeleteFilteringAlgorithmResponse:
        """
        @summary Deletes the configurations of a specified filtering table and the information about the related index table.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFilteringAlgorithmResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFilteringAlgorithm',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/filtering-algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}',
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
        """
        @summary Deletes the configurations of a specified filtering table and the information about the related index table.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFilteringAlgorithmResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFilteringAlgorithm',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/filtering-algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}',
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

    def delete_filtering_algorithm(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.DeleteFilteringAlgorithmResponse:
        """
        @summary Deletes the configurations of a specified filtering table and the information about the related index table.
        
        @return: DeleteFilteringAlgorithmResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_filtering_algorithm_with_options(instance_id, algorithm_id, headers, runtime)

    async def delete_filtering_algorithm_async(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.DeleteFilteringAlgorithmResponse:
        """
        @summary Deletes the configurations of a specified filtering table and the information about the related index table.
        
        @return: DeleteFilteringAlgorithmResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_filtering_algorithm_with_options_async(instance_id, algorithm_id, headers, runtime)

    def delete_flow_control_task_with_options(
        self,
        instance_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DeleteFlowControlTaskResponse:
        """
        @summary Deletes a throttling task.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFlowControlTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFlowControlTask',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/flowControlTasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DeleteFlowControlTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_control_task_with_options_async(
        self,
        instance_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DeleteFlowControlTaskResponse:
        """
        @summary Deletes a throttling task.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFlowControlTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFlowControlTask',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/flowControlTasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DeleteFlowControlTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_flow_control_task(
        self,
        instance_id: str,
        task_id: str,
    ) -> airec_20201126_models.DeleteFlowControlTaskResponse:
        """
        @summary Deletes a throttling task.
        
        @return: DeleteFlowControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_flow_control_task_with_options(instance_id, task_id, headers, runtime)

    async def delete_flow_control_task_async(
        self,
        instance_id: str,
        task_id: str,
    ) -> airec_20201126_models.DeleteFlowControlTaskResponse:
        """
        @summary Deletes a throttling task.
        
        @return: DeleteFlowControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_flow_control_task_with_options_async(instance_id, task_id, headers, runtime)

    def delete_ranking_model_with_options(
        self,
        instance_id: str,
        ranking_model_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DeleteRankingModelResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRankingModelResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRankingModel',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-models/{OpenApiUtilClient.get_encode_param(ranking_model_id)}',
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
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRankingModelResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRankingModel',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-models/{OpenApiUtilClient.get_encode_param(ranking_model_id)}',
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

    def delete_ranking_model(
        self,
        instance_id: str,
        ranking_model_id: str,
    ) -> airec_20201126_models.DeleteRankingModelResponse:
        """
        @return: DeleteRankingModelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_ranking_model_with_options(instance_id, ranking_model_id, headers, runtime)

    async def delete_ranking_model_async(
        self,
        instance_id: str,
        ranking_model_id: str,
    ) -> airec_20201126_models.DeleteRankingModelResponse:
        """
        @return: DeleteRankingModelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_ranking_model_with_options_async(instance_id, ranking_model_id, headers, runtime)

    def delete_ranking_model_template_with_options(
        self,
        instance_id: str,
        template_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DeleteRankingModelTemplateResponse:
        """
        @summary 删除排序模型模板
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRankingModelTemplateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRankingModelTemplate',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-model-templates/{OpenApiUtilClient.get_encode_param(template_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DeleteRankingModelTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ranking_model_template_with_options_async(
        self,
        instance_id: str,
        template_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DeleteRankingModelTemplateResponse:
        """
        @summary 删除排序模型模板
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRankingModelTemplateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRankingModelTemplate',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-model-templates/{OpenApiUtilClient.get_encode_param(template_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DeleteRankingModelTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ranking_model_template(
        self,
        instance_id: str,
        template_id: str,
    ) -> airec_20201126_models.DeleteRankingModelTemplateResponse:
        """
        @summary 删除排序模型模板
        
        @return: DeleteRankingModelTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_ranking_model_template_with_options(instance_id, template_id, headers, runtime)

    async def delete_ranking_model_template_async(
        self,
        instance_id: str,
        template_id: str,
    ) -> airec_20201126_models.DeleteRankingModelTemplateResponse:
        """
        @summary 删除排序模型模板
        
        @return: DeleteRankingModelTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_ranking_model_template_with_options_async(instance_id, template_id, headers, runtime)

    def delete_ranking_model_version_with_options(
        self,
        instance_id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DeleteRankingModelVersionResponse:
        """
        @summary 删除排序模型版本
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRankingModelVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRankingModelVersion',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-model-versions/{OpenApiUtilClient.get_encode_param(version_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DeleteRankingModelVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ranking_model_version_with_options_async(
        self,
        instance_id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DeleteRankingModelVersionResponse:
        """
        @summary 删除排序模型版本
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRankingModelVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRankingModelVersion',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-model-versions/{OpenApiUtilClient.get_encode_param(version_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DeleteRankingModelVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ranking_model_version(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20201126_models.DeleteRankingModelVersionResponse:
        """
        @summary 删除排序模型版本
        
        @return: DeleteRankingModelVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_ranking_model_version_with_options(instance_id, version_id, headers, runtime)

    async def delete_ranking_model_version_async(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20201126_models.DeleteRankingModelVersionResponse:
        """
        @summary 删除排序模型版本
        
        @return: DeleteRankingModelVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_ranking_model_version_with_options_async(instance_id, version_id, headers, runtime)

    def delete_ranking_system_with_options(
        self,
        instance_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DeleteRankingSystemResponse:
        """
        @summary 删除某个排序服务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRankingSystemResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRankingSystem',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-systems/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DeleteRankingSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ranking_system_with_options_async(
        self,
        instance_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DeleteRankingSystemResponse:
        """
        @summary 删除某个排序服务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRankingSystemResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRankingSystem',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-systems/{OpenApiUtilClient.get_encode_param(name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DeleteRankingSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ranking_system(
        self,
        instance_id: str,
        name: str,
    ) -> airec_20201126_models.DeleteRankingSystemResponse:
        """
        @summary 删除某个排序服务
        
        @return: DeleteRankingSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_ranking_system_with_options(instance_id, name, headers, runtime)

    async def delete_ranking_system_async(
        self,
        instance_id: str,
        name: str,
    ) -> airec_20201126_models.DeleteRankingSystemResponse:
        """
        @summary 删除某个排序服务
        
        @return: DeleteRankingSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_ranking_system_with_options_async(instance_id, name, headers, runtime)

    def delete_sample_with_options(
        self,
        instance_id: str,
        sample_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DeleteSampleResponse:
        """
        @summary 删除样本
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSampleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSample',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/samples/{OpenApiUtilClient.get_encode_param(sample_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DeleteSampleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sample_with_options_async(
        self,
        instance_id: str,
        sample_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DeleteSampleResponse:
        """
        @summary 删除样本
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSampleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSample',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/samples/{OpenApiUtilClient.get_encode_param(sample_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DeleteSampleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sample(
        self,
        instance_id: str,
        sample_id: str,
    ) -> airec_20201126_models.DeleteSampleResponse:
        """
        @summary 删除样本
        
        @return: DeleteSampleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_sample_with_options(instance_id, sample_id, headers, runtime)

    async def delete_sample_async(
        self,
        instance_id: str,
        sample_id: str,
    ) -> airec_20201126_models.DeleteSampleResponse:
        """
        @summary 删除样本
        
        @return: DeleteSampleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_sample_with_options_async(instance_id, sample_id, headers, runtime)

    def delete_scene_with_options(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DeleteSceneResponse:
        """
        @summary Deletes a scene.
        
        @description We recommend that you do not call an API operation to manage scenes. We recommend that you go to the Scenario Building page in the Artificial Intelligence Recommendation (AIRec) console to manage scenes.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSceneResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteScene',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}',
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
        """
        @summary Deletes a scene.
        
        @description We recommend that you do not call an API operation to manage scenes. We recommend that you go to the Scenario Building page in the Artificial Intelligence Recommendation (AIRec) console to manage scenes.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSceneResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteScene',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}',
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

    def delete_scene(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DeleteSceneResponse:
        """
        @summary Deletes a scene.
        
        @description We recommend that you do not call an API operation to manage scenes. We recommend that you go to the Scenario Building page in the Artificial Intelligence Recommendation (AIRec) console to manage scenes.
        
        @return: DeleteSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_scene_with_options(instance_id, scene_id, headers, runtime)

    async def delete_scene_async(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DeleteSceneResponse:
        """
        @summary Deletes a scene.
        
        @description We recommend that you do not call an API operation to manage scenes. We recommend that you go to the Scenario Building page in the Artificial Intelligence Recommendation (AIRec) console to manage scenes.
        
        @return: DeleteSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_scene_with_options_async(instance_id, scene_id, headers, runtime)

    def deploy_ranking_system_with_options(
        self,
        instance_id: str,
        name: str,
        request: airec_20201126_models.DeployRankingSystemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DeployRankingSystemResponse:
        """
        @summary The ID of the instance.
        
        @param request: DeployRankingSystemRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployRankingSystemResponse
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
            action='DeployRankingSystem',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-systems/{OpenApiUtilClient.get_encode_param(name)}/actions/deploy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DeployRankingSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_ranking_system_with_options_async(
        self,
        instance_id: str,
        name: str,
        request: airec_20201126_models.DeployRankingSystemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DeployRankingSystemResponse:
        """
        @summary The ID of the instance.
        
        @param request: DeployRankingSystemRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployRankingSystemResponse
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
            action='DeployRankingSystem',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-systems/{OpenApiUtilClient.get_encode_param(name)}/actions/deploy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DeployRankingSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_ranking_system(
        self,
        instance_id: str,
        name: str,
        request: airec_20201126_models.DeployRankingSystemRequest,
    ) -> airec_20201126_models.DeployRankingSystemResponse:
        """
        @summary The ID of the instance.
        
        @param request: DeployRankingSystemRequest
        @return: DeployRankingSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.deploy_ranking_system_with_options(instance_id, name, request, headers, runtime)

    async def deploy_ranking_system_async(
        self,
        instance_id: str,
        name: str,
        request: airec_20201126_models.DeployRankingSystemRequest,
    ) -> airec_20201126_models.DeployRankingSystemResponse:
        """
        @summary The ID of the instance.
        
        @param request: DeployRankingSystemRequest
        @return: DeployRankingSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.deploy_ranking_system_with_options_async(instance_id, name, request, headers, runtime)

    def describe_base_experiment_with_options(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeBaseExperimentResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBaseExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeBaseExperiment',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/base-experiment',
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
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBaseExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeBaseExperiment',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/base-experiment',
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

    def describe_base_experiment(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DescribeBaseExperimentResponse:
        """
        @return: DescribeBaseExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_base_experiment_with_options(instance_id, scene_id, headers, runtime)

    async def describe_base_experiment_async(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DescribeBaseExperimentResponse:
        """
        @return: DescribeBaseExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_base_experiment_with_options_async(instance_id, scene_id, headers, runtime)

    def describe_custom_analysis_task_with_options(
        self,
        instance_id: str,
        task_id: str,
        request: airec_20201126_models.DescribeCustomAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeCustomAnalysisTaskResponse:
        """
        @summary 查询自定义分析任务
        
        @param request: DescribeCustomAnalysisTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCustomAnalysisTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomAnalysisTask',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/dashboard/custom-analysis-tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeCustomAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_analysis_task_with_options_async(
        self,
        instance_id: str,
        task_id: str,
        request: airec_20201126_models.DescribeCustomAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeCustomAnalysisTaskResponse:
        """
        @summary 查询自定义分析任务
        
        @param request: DescribeCustomAnalysisTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCustomAnalysisTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomAnalysisTask',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/dashboard/custom-analysis-tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.DescribeCustomAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_analysis_task(
        self,
        instance_id: str,
        task_id: str,
        request: airec_20201126_models.DescribeCustomAnalysisTaskRequest,
    ) -> airec_20201126_models.DescribeCustomAnalysisTaskResponse:
        """
        @summary 查询自定义分析任务
        
        @param request: DescribeCustomAnalysisTaskRequest
        @return: DescribeCustomAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_custom_analysis_task_with_options(instance_id, task_id, request, headers, runtime)

    async def describe_custom_analysis_task_async(
        self,
        instance_id: str,
        task_id: str,
        request: airec_20201126_models.DescribeCustomAnalysisTaskRequest,
    ) -> airec_20201126_models.DescribeCustomAnalysisTaskResponse:
        """
        @summary 查询自定义分析任务
        
        @param request: DescribeCustomAnalysisTaskRequest
        @return: DescribeCustomAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_custom_analysis_task_with_options_async(instance_id, task_id, request, headers, runtime)

    def describe_data_set_message_with_options(
        self,
        instance_id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeDataSetMessageResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataSetMessageResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeDataSetMessage',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/dataSets/{OpenApiUtilClient.get_encode_param(version_id)}/messages',
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
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataSetMessageResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeDataSetMessage',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/dataSets/{OpenApiUtilClient.get_encode_param(version_id)}/messages',
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

    def describe_data_set_message(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20201126_models.DescribeDataSetMessageResponse:
        """
        @return: DescribeDataSetMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_data_set_message_with_options(instance_id, version_id, headers, runtime)

    async def describe_data_set_message_async(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20201126_models.DescribeDataSetMessageResponse:
        """
        @return: DescribeDataSetMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_data_set_message_with_options_async(instance_id, version_id, headers, runtime)

    def describe_default_algorithms_with_options(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeDefaultAlgorithmsResponse:
        """
        @summary Queries the information of default algorithms.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefaultAlgorithmsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeDefaultAlgorithms',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/default-algorithms',
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
        """
        @summary Queries the information of default algorithms.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefaultAlgorithmsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeDefaultAlgorithms',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/default-algorithms',
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

    def describe_default_algorithms(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DescribeDefaultAlgorithmsResponse:
        """
        @summary Queries the information of default algorithms.
        
        @return: DescribeDefaultAlgorithmsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_default_algorithms_with_options(instance_id, scene_id, headers, runtime)

    async def describe_default_algorithms_async(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DescribeDefaultAlgorithmsResponse:
        """
        @summary Queries the information of default algorithms.
        
        @return: DescribeDefaultAlgorithmsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_default_algorithms_with_options_async(instance_id, scene_id, headers, runtime)

    def describe_experiment_with_options(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeExperimentResponse:
        """
        @summary Queries the details about an experiment.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeExperiment',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}',
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
        """
        @summary Queries the details about an experiment.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeExperiment',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}',
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

    def describe_experiment(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
    ) -> airec_20201126_models.DescribeExperimentResponse:
        """
        @summary Queries the details about an experiment.
        
        @return: DescribeExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_experiment_with_options(instance_id, scene_id, experiment_id, headers, runtime)

    async def describe_experiment_async(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
    ) -> airec_20201126_models.DescribeExperimentResponse:
        """
        @summary Queries the details about an experiment.
        
        @return: DescribeExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_experiment_with_options_async(instance_id, scene_id, experiment_id, headers, runtime)

    def describe_experiment_env_with_options(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeExperimentEnvResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeExperimentEnvResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeExperimentEnv',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/experiment-env',
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
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeExperimentEnvResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeExperimentEnv',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/experiment-env',
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

    def describe_experiment_env(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DescribeExperimentEnvResponse:
        """
        @return: DescribeExperimentEnvResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_experiment_env_with_options(instance_id, scene_id, headers, runtime)

    async def describe_experiment_env_async(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DescribeExperimentEnvResponse:
        """
        @return: DescribeExperimentEnvResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_experiment_env_with_options_async(instance_id, scene_id, headers, runtime)

    def describe_experiment_env_progress_with_options(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeExperimentEnvProgressResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeExperimentEnvProgressResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeExperimentEnvProgress',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/experiment-progress',
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
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeExperimentEnvProgressResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeExperimentEnvProgress',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/experiment-progress',
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

    def describe_experiment_env_progress(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DescribeExperimentEnvProgressResponse:
        """
        @return: DescribeExperimentEnvProgressResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_experiment_env_progress_with_options(instance_id, scene_id, headers, runtime)

    async def describe_experiment_env_progress_async(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DescribeExperimentEnvProgressResponse:
        """
        @return: DescribeExperimentEnvProgressResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_experiment_env_progress_with_options_async(instance_id, scene_id, headers, runtime)

    def describe_filtering_algorithm_with_options(
        self,
        instance_id: str,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeFilteringAlgorithmResponse:
        """
        @summary The fluctuation threshold for the data entries in the source table.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFilteringAlgorithmResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeFilteringAlgorithm',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/filtering-algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}',
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
        """
        @summary The fluctuation threshold for the data entries in the source table.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFilteringAlgorithmResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeFilteringAlgorithm',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/filtering-algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}',
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

    def describe_filtering_algorithm(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.DescribeFilteringAlgorithmResponse:
        """
        @summary The fluctuation threshold for the data entries in the source table.
        
        @return: DescribeFilteringAlgorithmResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_filtering_algorithm_with_options(instance_id, algorithm_id, headers, runtime)

    async def describe_filtering_algorithm_async(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.DescribeFilteringAlgorithmResponse:
        """
        @summary The fluctuation threshold for the data entries in the source table.
        
        @return: DescribeFilteringAlgorithmResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_filtering_algorithm_with_options_async(instance_id, algorithm_id, headers, runtime)

    def describe_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeInstanceResponse:
        """
        @summary Queries the details about an instance based on the instance ID.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
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
        """
        @summary Queries the details about an instance based on the instance ID.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
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

    def describe_instance(
        self,
        instance_id: str,
    ) -> airec_20201126_models.DescribeInstanceResponse:
        """
        @summary Queries the details about an instance based on the instance ID.
        
        @return: DescribeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_instance_with_options(instance_id, headers, runtime)

    async def describe_instance_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.DescribeInstanceResponse:
        """
        @summary Queries the details about an instance based on the instance ID.
        
        @return: DescribeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_instance_with_options_async(instance_id, headers, runtime)

    def describe_latest_task_with_options(
        self,
        instance_id: str,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeLatestTaskResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLatestTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeLatestTask',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/filtering-algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}/tasks/latest',
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
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLatestTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeLatestTask',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/filtering-algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}/tasks/latest',
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

    def describe_latest_task(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.DescribeLatestTaskResponse:
        """
        @return: DescribeLatestTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_latest_task_with_options(instance_id, algorithm_id, headers, runtime)

    async def describe_latest_task_async(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.DescribeLatestTaskResponse:
        """
        @return: DescribeLatestTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_latest_task_with_options_async(instance_id, algorithm_id, headers, runtime)

    def describe_quota_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeQuotaResponse:
        """
        @summary Queries the quotas of an instance based on a specified instance ID.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeQuotaResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeQuota',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/quota',
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
        """
        @summary Queries the quotas of an instance based on a specified instance ID.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeQuotaResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeQuota',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/quota',
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

    def describe_quota(
        self,
        instance_id: str,
    ) -> airec_20201126_models.DescribeQuotaResponse:
        """
        @summary Queries the quotas of an instance based on a specified instance ID.
        
        @return: DescribeQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_quota_with_options(instance_id, headers, runtime)

    async def describe_quota_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.DescribeQuotaResponse:
        """
        @summary Queries the quotas of an instance based on a specified instance ID.
        
        @return: DescribeQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_quota_with_options_async(instance_id, headers, runtime)

    def describe_regions_with_options(
        self,
        request: airec_20201126_models.DescribeRegionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeRegionsResponse:
        """
        @summary Queries available Alibaba Cloud regions.
        
        @param request: DescribeRegionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
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
        """
        @summary Queries available Alibaba Cloud regions.
        
        @param request: DescribeRegionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
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

    def describe_regions(
        self,
        request: airec_20201126_models.DescribeRegionsRequest,
    ) -> airec_20201126_models.DescribeRegionsResponse:
        """
        @summary Queries available Alibaba Cloud regions.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(request, headers, runtime)

    async def describe_regions_async(
        self,
        request: airec_20201126_models.DescribeRegionsRequest,
    ) -> airec_20201126_models.DescribeRegionsResponse:
        """
        @summary Queries available Alibaba Cloud regions.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_regions_with_options_async(request, headers, runtime)

    def describe_rule_with_options(
        self,
        instance_id: str,
        rule_id: str,
        request: airec_20201126_models.DescribeRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeRuleResponse:
        """
        @summary The ID of the instance.
        
        @param request: DescribeRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRuleResponse
        """
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
            action='DescribeRule',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/rules/{OpenApiUtilClient.get_encode_param(rule_id)}',
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
        """
        @summary The ID of the instance.
        
        @param request: DescribeRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRuleResponse
        """
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
            action='DescribeRule',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/rules/{OpenApiUtilClient.get_encode_param(rule_id)}',
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

    def describe_rule(
        self,
        instance_id: str,
        rule_id: str,
        request: airec_20201126_models.DescribeRuleRequest,
    ) -> airec_20201126_models.DescribeRuleResponse:
        """
        @summary The ID of the instance.
        
        @param request: DescribeRuleRequest
        @return: DescribeRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_rule_with_options(instance_id, rule_id, request, headers, runtime)

    async def describe_rule_async(
        self,
        instance_id: str,
        rule_id: str,
        request: airec_20201126_models.DescribeRuleRequest,
    ) -> airec_20201126_models.DescribeRuleResponse:
        """
        @summary The ID of the instance.
        
        @param request: DescribeRuleRequest
        @return: DescribeRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_rule_with_options_async(instance_id, rule_id, request, headers, runtime)

    def describe_scene_with_options(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeSceneResponse:
        """
        @summary Queries the details about a specified scene.
        
        @description We recommend that you do not call an API operation to manage scenes. We recommend that you go to the Scenario Building page in the Artificial Intelligence Recommendation (AIRec) console to manage scenes.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSceneResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeScene',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}',
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
        """
        @summary Queries the details about a specified scene.
        
        @description We recommend that you do not call an API operation to manage scenes. We recommend that you go to the Scenario Building page in the Artificial Intelligence Recommendation (AIRec) console to manage scenes.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSceneResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeScene',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}',
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

    def describe_scene(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DescribeSceneResponse:
        """
        @summary Queries the details about a specified scene.
        
        @description We recommend that you do not call an API operation to manage scenes. We recommend that you go to the Scenario Building page in the Artificial Intelligence Recommendation (AIRec) console to manage scenes.
        
        @return: DescribeSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_scene_with_options(instance_id, scene_id, headers, runtime)

    async def describe_scene_async(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DescribeSceneResponse:
        """
        @summary Queries the details about a specified scene.
        
        @description We recommend that you do not call an API operation to manage scenes. We recommend that you go to the Scenario Building page in the Artificial Intelligence Recommendation (AIRec) console to manage scenes.
        
        @return: DescribeSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_scene_with_options_async(instance_id, scene_id, headers, runtime)

    def describe_scene_bucket_with_options(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeSceneBucketResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSceneBucketResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeSceneBucket',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/experiment-bucket',
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
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSceneBucketResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeSceneBucket',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/experiment-bucket',
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

    def describe_scene_bucket(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DescribeSceneBucketResponse:
        """
        @return: DescribeSceneBucketResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_scene_bucket_with_options(instance_id, scene_id, headers, runtime)

    async def describe_scene_bucket_async(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DescribeSceneBucketResponse:
        """
        @return: DescribeSceneBucketResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_scene_bucket_with_options_async(instance_id, scene_id, headers, runtime)

    def describe_scene_throughput_with_options(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeSceneThroughputResponse:
        """
        @summary The error message.
        
        @description __null__
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSceneThroughputResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeSceneThroughput',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/throughput',
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
        """
        @summary The error message.
        
        @description __null__
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSceneThroughputResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeSceneThroughput',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/throughput',
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

    def describe_scene_throughput(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DescribeSceneThroughputResponse:
        """
        @summary The error message.
        
        @description __null__
        
        @return: DescribeSceneThroughputResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_scene_throughput_with_options(instance_id, scene_id, headers, runtime)

    async def describe_scene_throughput_async(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.DescribeSceneThroughputResponse:
        """
        @summary The error message.
        
        @description __null__
        
        @return: DescribeSceneThroughputResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_scene_throughput_with_options_async(instance_id, scene_id, headers, runtime)

    def describe_sync_report_detail_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.DescribeSyncReportDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeSyncReportDetailResponse:
        """
        @param request: DescribeSyncReportDetailRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSyncReportDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.level_type):
            query['levelType'] = request.level_type
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSyncReportDetail',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sync-reports/detail',
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
        """
        @param request: DescribeSyncReportDetailRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSyncReportDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.level_type):
            query['levelType'] = request.level_type
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSyncReportDetail',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sync-reports/detail',
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

    def describe_sync_report_detail(
        self,
        instance_id: str,
        request: airec_20201126_models.DescribeSyncReportDetailRequest,
    ) -> airec_20201126_models.DescribeSyncReportDetailResponse:
        """
        @param request: DescribeSyncReportDetailRequest
        @return: DescribeSyncReportDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_sync_report_detail_with_options(instance_id, request, headers, runtime)

    async def describe_sync_report_detail_async(
        self,
        instance_id: str,
        request: airec_20201126_models.DescribeSyncReportDetailRequest,
    ) -> airec_20201126_models.DescribeSyncReportDetailResponse:
        """
        @param request: DescribeSyncReportDetailRequest
        @return: DescribeSyncReportDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_sync_report_detail_with_options_async(instance_id, request, headers, runtime)

    def describe_sync_report_outliers_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.DescribeSyncReportOutliersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeSyncReportOutliersResponse:
        """
        @param request: DescribeSyncReportOutliersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSyncReportOutliersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['key'] = request.key
        if not UtilClient.is_unset(request.level_type):
            query['levelType'] = request.level_type
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSyncReportOutliers',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sync-reports/outliers',
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
        """
        @param request: DescribeSyncReportOutliersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSyncReportOutliersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['key'] = request.key
        if not UtilClient.is_unset(request.level_type):
            query['levelType'] = request.level_type
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSyncReportOutliers',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sync-reports/outliers',
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

    def describe_sync_report_outliers(
        self,
        instance_id: str,
        request: airec_20201126_models.DescribeSyncReportOutliersRequest,
    ) -> airec_20201126_models.DescribeSyncReportOutliersResponse:
        """
        @param request: DescribeSyncReportOutliersRequest
        @return: DescribeSyncReportOutliersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_sync_report_outliers_with_options(instance_id, request, headers, runtime)

    async def describe_sync_report_outliers_async(
        self,
        instance_id: str,
        request: airec_20201126_models.DescribeSyncReportOutliersRequest,
    ) -> airec_20201126_models.DescribeSyncReportOutliersResponse:
        """
        @param request: DescribeSyncReportOutliersRequest
        @return: DescribeSyncReportOutliersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_sync_report_outliers_with_options_async(instance_id, request, headers, runtime)

    def describe_user_metrics_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.DescribeUserMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DescribeUserMetricsResponse:
        """
        @summary Queries user metrics related to the conversion rate.
        
        @param request: DescribeUserMetricsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserMetricsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_type):
            query['metricType'] = request.metric_type
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserMetrics',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/metrics',
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
        """
        @summary Queries user metrics related to the conversion rate.
        
        @param request: DescribeUserMetricsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserMetricsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_type):
            query['metricType'] = request.metric_type
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserMetrics',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/metrics',
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

    def describe_user_metrics(
        self,
        instance_id: str,
        request: airec_20201126_models.DescribeUserMetricsRequest,
    ) -> airec_20201126_models.DescribeUserMetricsResponse:
        """
        @summary Queries user metrics related to the conversion rate.
        
        @param request: DescribeUserMetricsRequest
        @return: DescribeUserMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_user_metrics_with_options(instance_id, request, headers, runtime)

    async def describe_user_metrics_async(
        self,
        instance_id: str,
        request: airec_20201126_models.DescribeUserMetricsRequest,
    ) -> airec_20201126_models.DescribeUserMetricsResponse:
        """
        @summary Queries user metrics related to the conversion rate.
        
        @param request: DescribeUserMetricsRequest
        @return: DescribeUserMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_user_metrics_with_options_async(instance_id, request, headers, runtime)

    def downgrade_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.DowngradeInstanceResponse:
        """
        @summary The ID of the instance.
        
        @description The returned results.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DowngradeInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DowngradeInstance',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/actions/downgrade',
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
        """
        @summary The ID of the instance.
        
        @description The returned results.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DowngradeInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DowngradeInstance',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/actions/downgrade',
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

    def downgrade_instance(
        self,
        instance_id: str,
    ) -> airec_20201126_models.DowngradeInstanceResponse:
        """
        @summary The ID of the instance.
        
        @description The returned results.
        
        @return: DowngradeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.downgrade_instance_with_options(instance_id, headers, runtime)

    async def downgrade_instance_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.DowngradeInstanceResponse:
        """
        @summary The ID of the instance.
        
        @description The returned results.
        
        @return: DowngradeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.downgrade_instance_with_options_async(instance_id, headers, runtime)

    def enable_experiment_with_options(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.EnableExperimentResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='EnableExperiment',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/actions/enable-experiment',
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
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='EnableExperiment',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/actions/enable-experiment',
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

    def enable_experiment(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.EnableExperimentResponse:
        """
        @return: EnableExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_experiment_with_options(instance_id, scene_id, headers, runtime)

    async def enable_experiment_async(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.EnableExperimentResponse:
        """
        @return: EnableExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.enable_experiment_with_options_async(instance_id, scene_id, headers, runtime)

    def generate_sample_with_options(
        self,
        instance_id: str,
        sample_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.GenerateSampleResponse:
        """
        @summary 生成样本，只针对复制创建的样本
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateSampleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GenerateSample',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/samples/{OpenApiUtilClient.get_encode_param(sample_id)}/actions/generate',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.GenerateSampleResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_sample_with_options_async(
        self,
        instance_id: str,
        sample_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.GenerateSampleResponse:
        """
        @summary 生成样本，只针对复制创建的样本
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateSampleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GenerateSample',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/samples/{OpenApiUtilClient.get_encode_param(sample_id)}/actions/generate',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.GenerateSampleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_sample(
        self,
        instance_id: str,
        sample_id: str,
    ) -> airec_20201126_models.GenerateSampleResponse:
        """
        @summary 生成样本，只针对复制创建的样本
        
        @return: GenerateSampleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_sample_with_options(instance_id, sample_id, headers, runtime)

    async def generate_sample_async(
        self,
        instance_id: str,
        sample_id: str,
    ) -> airec_20201126_models.GenerateSampleResponse:
        """
        @summary 生成样本，只针对复制创建的样本
        
        @return: GenerateSampleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.generate_sample_with_options_async(instance_id, sample_id, headers, runtime)

    def get_extra_data_source_with_options(
        self,
        instance_id: str,
        type: str,
        data_source_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.GetExtraDataSourceResponse:
        """
        @summary Queries the details of other data sources.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExtraDataSourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetExtraDataSource',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/extra-data-sources/{OpenApiUtilClient.get_encode_param(type)}/{OpenApiUtilClient.get_encode_param(data_source_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.GetExtraDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_extra_data_source_with_options_async(
        self,
        instance_id: str,
        type: str,
        data_source_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.GetExtraDataSourceResponse:
        """
        @summary Queries the details of other data sources.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExtraDataSourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetExtraDataSource',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/extra-data-sources/{OpenApiUtilClient.get_encode_param(type)}/{OpenApiUtilClient.get_encode_param(data_source_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.GetExtraDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_extra_data_source(
        self,
        instance_id: str,
        type: str,
        data_source_id: str,
    ) -> airec_20201126_models.GetExtraDataSourceResponse:
        """
        @summary Queries the details of other data sources.
        
        @return: GetExtraDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_extra_data_source_with_options(instance_id, type, data_source_id, headers, runtime)

    async def get_extra_data_source_async(
        self,
        instance_id: str,
        type: str,
        data_source_id: str,
    ) -> airec_20201126_models.GetExtraDataSourceResponse:
        """
        @summary Queries the details of other data sources.
        
        @return: GetExtraDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_extra_data_source_with_options_async(instance_id, type, data_source_id, headers, runtime)

    def get_flow_control_task_with_options(
        self,
        instance_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.GetFlowControlTaskResponse:
        """
        @summary Obtains the details of a throttling task.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFlowControlTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFlowControlTask',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/flowControlTasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.GetFlowControlTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_flow_control_task_with_options_async(
        self,
        instance_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.GetFlowControlTaskResponse:
        """
        @summary Obtains the details of a throttling task.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFlowControlTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFlowControlTask',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/flowControlTasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.GetFlowControlTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_flow_control_task(
        self,
        instance_id: str,
        task_id: str,
    ) -> airec_20201126_models.GetFlowControlTaskResponse:
        """
        @summary Obtains the details of a throttling task.
        
        @return: GetFlowControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_flow_control_task_with_options(instance_id, task_id, headers, runtime)

    async def get_flow_control_task_async(
        self,
        instance_id: str,
        task_id: str,
    ) -> airec_20201126_models.GetFlowControlTaskResponse:
        """
        @summary Obtains the details of a throttling task.
        
        @return: GetFlowControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_flow_control_task_with_options_async(instance_id, task_id, headers, runtime)

    def get_latest_data_diagnose_task_status_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.GetLatestDataDiagnoseTaskStatusResponse:
        """
        @summary 获取最新诊断任务状态
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLatestDataDiagnoseTaskStatusResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLatestDataDiagnoseTaskStatus',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-diagnose-task/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.GetLatestDataDiagnoseTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_latest_data_diagnose_task_status_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.GetLatestDataDiagnoseTaskStatusResponse:
        """
        @summary 获取最新诊断任务状态
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLatestDataDiagnoseTaskStatusResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLatestDataDiagnoseTaskStatus',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-diagnose-task/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.GetLatestDataDiagnoseTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_latest_data_diagnose_task_status(
        self,
        instance_id: str,
    ) -> airec_20201126_models.GetLatestDataDiagnoseTaskStatusResponse:
        """
        @summary 获取最新诊断任务状态
        
        @return: GetLatestDataDiagnoseTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_latest_data_diagnose_task_status_with_options(instance_id, headers, runtime)

    async def get_latest_data_diagnose_task_status_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.GetLatestDataDiagnoseTaskStatusResponse:
        """
        @summary 获取最新诊断任务状态
        
        @return: GetLatestDataDiagnoseTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_latest_data_diagnose_task_status_with_options_async(instance_id, headers, runtime)

    def get_ranking_model_template_with_options(
        self,
        instance_id: str,
        template_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.GetRankingModelTemplateResponse:
        """
        @summary 查看排序模型模板配置详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRankingModelTemplateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRankingModelTemplate',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-model-templates/{OpenApiUtilClient.get_encode_param(template_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.GetRankingModelTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ranking_model_template_with_options_async(
        self,
        instance_id: str,
        template_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.GetRankingModelTemplateResponse:
        """
        @summary 查看排序模型模板配置详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRankingModelTemplateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRankingModelTemplate',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-model-templates/{OpenApiUtilClient.get_encode_param(template_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.GetRankingModelTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ranking_model_template(
        self,
        instance_id: str,
        template_id: str,
    ) -> airec_20201126_models.GetRankingModelTemplateResponse:
        """
        @summary 查看排序模型模板配置详情
        
        @return: GetRankingModelTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_ranking_model_template_with_options(instance_id, template_id, headers, runtime)

    async def get_ranking_model_template_async(
        self,
        instance_id: str,
        template_id: str,
    ) -> airec_20201126_models.GetRankingModelTemplateResponse:
        """
        @summary 查看排序模型模板配置详情
        
        @return: GetRankingModelTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_ranking_model_template_with_options_async(instance_id, template_id, headers, runtime)

    def get_ranking_model_version_with_options(
        self,
        instance_id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.GetRankingModelVersionResponse:
        """
        @summary 查看排序模型版本详情，包括评估结果和训练结果
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRankingModelVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRankingModelVersion',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-model-versions/{OpenApiUtilClient.get_encode_param(version_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.GetRankingModelVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ranking_model_version_with_options_async(
        self,
        instance_id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.GetRankingModelVersionResponse:
        """
        @summary 查看排序模型版本详情，包括评估结果和训练结果
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRankingModelVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRankingModelVersion',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-model-versions/{OpenApiUtilClient.get_encode_param(version_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.GetRankingModelVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ranking_model_version(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20201126_models.GetRankingModelVersionResponse:
        """
        @summary 查看排序模型版本详情，包括评估结果和训练结果
        
        @return: GetRankingModelVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_ranking_model_version_with_options(instance_id, version_id, headers, runtime)

    async def get_ranking_model_version_async(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20201126_models.GetRankingModelVersionResponse:
        """
        @summary 查看排序模型版本详情，包括评估结果和训练结果
        
        @return: GetRankingModelVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_ranking_model_version_with_options_async(instance_id, version_id, headers, runtime)

    def get_ranking_system_with_options(
        self,
        instance_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.GetRankingSystemResponse:
        """
        @summary 获取某个排序服务详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRankingSystemResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRankingSystem',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-systems/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.GetRankingSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ranking_system_with_options_async(
        self,
        instance_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.GetRankingSystemResponse:
        """
        @summary 获取某个排序服务详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRankingSystemResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRankingSystem',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-systems/{OpenApiUtilClient.get_encode_param(name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.GetRankingSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ranking_system(
        self,
        instance_id: str,
        name: str,
    ) -> airec_20201126_models.GetRankingSystemResponse:
        """
        @summary 获取某个排序服务详情
        
        @return: GetRankingSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_ranking_system_with_options(instance_id, name, headers, runtime)

    async def get_ranking_system_async(
        self,
        instance_id: str,
        name: str,
    ) -> airec_20201126_models.GetRankingSystemResponse:
        """
        @summary 获取某个排序服务详情
        
        @return: GetRankingSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_ranking_system_with_options_async(instance_id, name, headers, runtime)

    def get_ranking_system_history_with_options(
        self,
        instance_id: str,
        name: str,
        operate_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.GetRankingSystemHistoryResponse:
        """
        @summary 查询某个服务操作记录
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRankingSystemHistoryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRankingSystemHistory',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-systems/{OpenApiUtilClient.get_encode_param(name)}/histories/{OpenApiUtilClient.get_encode_param(operate_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.GetRankingSystemHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ranking_system_history_with_options_async(
        self,
        instance_id: str,
        name: str,
        operate_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.GetRankingSystemHistoryResponse:
        """
        @summary 查询某个服务操作记录
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRankingSystemHistoryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRankingSystemHistory',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-systems/{OpenApiUtilClient.get_encode_param(name)}/histories/{OpenApiUtilClient.get_encode_param(operate_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.GetRankingSystemHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ranking_system_history(
        self,
        instance_id: str,
        name: str,
        operate_id: str,
    ) -> airec_20201126_models.GetRankingSystemHistoryResponse:
        """
        @summary 查询某个服务操作记录
        
        @return: GetRankingSystemHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_ranking_system_history_with_options(instance_id, name, operate_id, headers, runtime)

    async def get_ranking_system_history_async(
        self,
        instance_id: str,
        name: str,
        operate_id: str,
    ) -> airec_20201126_models.GetRankingSystemHistoryResponse:
        """
        @summary 查询某个服务操作记录
        
        @return: GetRankingSystemHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_ranking_system_history_with_options_async(instance_id, name, operate_id, headers, runtime)

    def get_sample_with_options(
        self,
        instance_id: str,
        sample_id: str,
        request: airec_20201126_models.GetSampleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.GetSampleResponse:
        """
        @summary 获取样本详情
        
        @param request: GetSampleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSampleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.with_extend_parmas):
            query['withExtendParmas'] = request.with_extend_parmas
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSample',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/samples/{OpenApiUtilClient.get_encode_param(sample_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.GetSampleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sample_with_options_async(
        self,
        instance_id: str,
        sample_id: str,
        request: airec_20201126_models.GetSampleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.GetSampleResponse:
        """
        @summary 获取样本详情
        
        @param request: GetSampleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSampleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.with_extend_parmas):
            query['withExtendParmas'] = request.with_extend_parmas
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSample',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/samples/{OpenApiUtilClient.get_encode_param(sample_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.GetSampleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sample(
        self,
        instance_id: str,
        sample_id: str,
        request: airec_20201126_models.GetSampleRequest,
    ) -> airec_20201126_models.GetSampleResponse:
        """
        @summary 获取样本详情
        
        @param request: GetSampleRequest
        @return: GetSampleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_sample_with_options(instance_id, sample_id, request, headers, runtime)

    async def get_sample_async(
        self,
        instance_id: str,
        sample_id: str,
        request: airec_20201126_models.GetSampleRequest,
    ) -> airec_20201126_models.GetSampleResponse:
        """
        @summary 获取样本详情
        
        @param request: GetSampleRequest
        @return: GetSampleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_sample_with_options_async(instance_id, sample_id, request, headers, runtime)

    def init_computing_resource_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.InitComputingResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.InitComputingResourceResponse:
        """
        @summary 初始化计算资源
        
        @param request: InitComputingResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitComputingResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['key'] = request.key
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitComputingResource',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/computing-resources/actions/init',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.InitComputingResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_computing_resource_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.InitComputingResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.InitComputingResourceResponse:
        """
        @summary 初始化计算资源
        
        @param request: InitComputingResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitComputingResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['key'] = request.key
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitComputingResource',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/computing-resources/actions/init',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.InitComputingResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def init_computing_resource(
        self,
        instance_id: str,
        request: airec_20201126_models.InitComputingResourceRequest,
    ) -> airec_20201126_models.InitComputingResourceResponse:
        """
        @summary 初始化计算资源
        
        @param request: InitComputingResourceRequest
        @return: InitComputingResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.init_computing_resource_with_options(instance_id, request, headers, runtime)

    async def init_computing_resource_async(
        self,
        instance_id: str,
        request: airec_20201126_models.InitComputingResourceRequest,
    ) -> airec_20201126_models.InitComputingResourceResponse:
        """
        @summary 初始化计算资源
        
        @param request: InitComputingResourceRequest
        @return: InitComputingResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.init_computing_resource_with_options_async(instance_id, request, headers, runtime)

    def list_dashboard_details_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDashboardDetailsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListDashboardDetailsResponse:
        """
        @param request: ListDashboardDetailsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDashboardDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.experiment_ids):
            query['experimentIds'] = request.experiment_ids
        if not UtilClient.is_unset(request.match_types):
            query['matchTypes'] = request.match_types
        if not UtilClient.is_unset(request.metric_type):
            query['metricType'] = request.metric_type
        if not UtilClient.is_unset(request.scene_ids):
            query['sceneIds'] = request.scene_ids
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.trace_ids):
            query['traceIds'] = request.trace_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboardDetails',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/dashboard/details',
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
        """
        @param request: ListDashboardDetailsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDashboardDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.experiment_ids):
            query['experimentIds'] = request.experiment_ids
        if not UtilClient.is_unset(request.match_types):
            query['matchTypes'] = request.match_types
        if not UtilClient.is_unset(request.metric_type):
            query['metricType'] = request.metric_type
        if not UtilClient.is_unset(request.scene_ids):
            query['sceneIds'] = request.scene_ids
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.trace_ids):
            query['traceIds'] = request.trace_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboardDetails',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/dashboard/details',
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

    def list_dashboard_details(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDashboardDetailsRequest,
    ) -> airec_20201126_models.ListDashboardDetailsResponse:
        """
        @param request: ListDashboardDetailsRequest
        @return: ListDashboardDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dashboard_details_with_options(instance_id, request, headers, runtime)

    async def list_dashboard_details_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDashboardDetailsRequest,
    ) -> airec_20201126_models.ListDashboardDetailsResponse:
        """
        @param request: ListDashboardDetailsRequest
        @return: ListDashboardDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_dashboard_details_with_options_async(instance_id, request, headers, runtime)

    def list_dashboard_details_flows_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDashboardDetailsFlowsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListDashboardDetailsFlowsResponse:
        """
        @param request: ListDashboardDetailsFlowsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDashboardDetailsFlowsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.experiment_ids):
            query['experimentIds'] = request.experiment_ids
        if not UtilClient.is_unset(request.metric_type):
            query['metricType'] = request.metric_type
        if not UtilClient.is_unset(request.scene_ids):
            query['sceneIds'] = request.scene_ids
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.trace_ids):
            query['traceIds'] = request.trace_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboardDetailsFlows',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/dashboard/details/flows',
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
        """
        @param request: ListDashboardDetailsFlowsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDashboardDetailsFlowsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.experiment_ids):
            query['experimentIds'] = request.experiment_ids
        if not UtilClient.is_unset(request.metric_type):
            query['metricType'] = request.metric_type
        if not UtilClient.is_unset(request.scene_ids):
            query['sceneIds'] = request.scene_ids
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.trace_ids):
            query['traceIds'] = request.trace_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboardDetailsFlows',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/dashboard/details/flows',
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

    def list_dashboard_details_flows(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDashboardDetailsFlowsRequest,
    ) -> airec_20201126_models.ListDashboardDetailsFlowsResponse:
        """
        @param request: ListDashboardDetailsFlowsRequest
        @return: ListDashboardDetailsFlowsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dashboard_details_flows_with_options(instance_id, request, headers, runtime)

    async def list_dashboard_details_flows_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDashboardDetailsFlowsRequest,
    ) -> airec_20201126_models.ListDashboardDetailsFlowsResponse:
        """
        @param request: ListDashboardDetailsFlowsRequest
        @return: ListDashboardDetailsFlowsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_dashboard_details_flows_with_options_async(instance_id, request, headers, runtime)

    def list_dashboard_metrics_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDashboardMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListDashboardMetricsResponse:
        """
        @summary The end time. The value is a timestamp in seconds.
        
        @param request: ListDashboardMetricsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDashboardMetricsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_query):
            query['metricQuery'] = request.metric_query
        if not UtilClient.is_unset(request.metric_type):
            query['metricType'] = request.metric_type
        if not UtilClient.is_unset(request.metric_view):
            query['metricView'] = request.metric_view
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboardMetrics',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/dashboard/metrics',
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
        """
        @summary The end time. The value is a timestamp in seconds.
        
        @param request: ListDashboardMetricsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDashboardMetricsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_query):
            query['metricQuery'] = request.metric_query
        if not UtilClient.is_unset(request.metric_type):
            query['metricType'] = request.metric_type
        if not UtilClient.is_unset(request.metric_view):
            query['metricView'] = request.metric_view
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboardMetrics',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/dashboard/metrics',
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

    def list_dashboard_metrics(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDashboardMetricsRequest,
    ) -> airec_20201126_models.ListDashboardMetricsResponse:
        """
        @summary The end time. The value is a timestamp in seconds.
        
        @param request: ListDashboardMetricsRequest
        @return: ListDashboardMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dashboard_metrics_with_options(instance_id, request, headers, runtime)

    async def list_dashboard_metrics_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDashboardMetricsRequest,
    ) -> airec_20201126_models.ListDashboardMetricsResponse:
        """
        @summary The end time. The value is a timestamp in seconds.
        
        @param request: ListDashboardMetricsRequest
        @return: ListDashboardMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_dashboard_metrics_with_options_async(instance_id, request, headers, runtime)

    def list_dashboard_metrics_flows_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDashboardMetricsFlowsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListDashboardMetricsFlowsResponse:
        """
        @summary The end time. The value is a timestamp in seconds.
        
        @param request: ListDashboardMetricsFlowsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDashboardMetricsFlowsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_type):
            query['metricType'] = request.metric_type
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboardMetricsFlows',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/dashboard/metrics/flows',
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
        """
        @summary The end time. The value is a timestamp in seconds.
        
        @param request: ListDashboardMetricsFlowsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDashboardMetricsFlowsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_type):
            query['metricType'] = request.metric_type
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboardMetricsFlows',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/dashboard/metrics/flows',
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

    def list_dashboard_metrics_flows(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDashboardMetricsFlowsRequest,
    ) -> airec_20201126_models.ListDashboardMetricsFlowsResponse:
        """
        @summary The end time. The value is a timestamp in seconds.
        
        @param request: ListDashboardMetricsFlowsRequest
        @return: ListDashboardMetricsFlowsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dashboard_metrics_flows_with_options(instance_id, request, headers, runtime)

    async def list_dashboard_metrics_flows_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDashboardMetricsFlowsRequest,
    ) -> airec_20201126_models.ListDashboardMetricsFlowsResponse:
        """
        @summary The end time. The value is a timestamp in seconds.
        
        @param request: ListDashboardMetricsFlowsRequest
        @return: ListDashboardMetricsFlowsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_dashboard_metrics_flows_with_options_async(instance_id, request, headers, runtime)

    def list_data_diagnose_reports_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDataDiagnoseReportsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListDataDiagnoseReportsResponse:
        """
        @summary 获取数据诊断报告 (包括用户手动触发的诊断、每天产出的周期报告、数据启动时诊断的报告)
        
        @param request: ListDataDiagnoseReportsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataDiagnoseReportsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_create_time):
            query['taskCreateTime'] = request.task_create_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataDiagnoseReports',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-diagnose-reports',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListDataDiagnoseReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_diagnose_reports_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDataDiagnoseReportsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListDataDiagnoseReportsResponse:
        """
        @summary 获取数据诊断报告 (包括用户手动触发的诊断、每天产出的周期报告、数据启动时诊断的报告)
        
        @param request: ListDataDiagnoseReportsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataDiagnoseReportsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_create_time):
            query['taskCreateTime'] = request.task_create_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataDiagnoseReports',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-diagnose-reports',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListDataDiagnoseReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_diagnose_reports(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDataDiagnoseReportsRequest,
    ) -> airec_20201126_models.ListDataDiagnoseReportsResponse:
        """
        @summary 获取数据诊断报告 (包括用户手动触发的诊断、每天产出的周期报告、数据启动时诊断的报告)
        
        @param request: ListDataDiagnoseReportsRequest
        @return: ListDataDiagnoseReportsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_diagnose_reports_with_options(instance_id, request, headers, runtime)

    async def list_data_diagnose_reports_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDataDiagnoseReportsRequest,
    ) -> airec_20201126_models.ListDataDiagnoseReportsResponse:
        """
        @summary 获取数据诊断报告 (包括用户手动触发的诊断、每天产出的周期报告、数据启动时诊断的报告)
        
        @param request: ListDataDiagnoseReportsRequest
        @return: ListDataDiagnoseReportsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_data_diagnose_reports_with_options_async(instance_id, request, headers, runtime)

    def list_data_diagnose_sample_details_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDataDiagnoseSampleDetailsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListDataDiagnoseSampleDetailsResponse:
        """
        @summary 获取数据诊断项抽样明细
        
        @param request: ListDataDiagnoseSampleDetailsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataDiagnoseSampleDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['key'] = request.key
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.task_create_time):
            query['taskCreateTime'] = request.task_create_time
        if not UtilClient.is_unset(request.task_source):
            query['taskSource'] = request.task_source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataDiagnoseSampleDetails',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-diagnose-reports/sample-details',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListDataDiagnoseSampleDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_diagnose_sample_details_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDataDiagnoseSampleDetailsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListDataDiagnoseSampleDetailsResponse:
        """
        @summary 获取数据诊断项抽样明细
        
        @param request: ListDataDiagnoseSampleDetailsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataDiagnoseSampleDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['key'] = request.key
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.task_create_time):
            query['taskCreateTime'] = request.task_create_time
        if not UtilClient.is_unset(request.task_source):
            query['taskSource'] = request.task_source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataDiagnoseSampleDetails',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-diagnose-reports/sample-details',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListDataDiagnoseSampleDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_diagnose_sample_details(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDataDiagnoseSampleDetailsRequest,
    ) -> airec_20201126_models.ListDataDiagnoseSampleDetailsResponse:
        """
        @summary 获取数据诊断项抽样明细
        
        @param request: ListDataDiagnoseSampleDetailsRequest
        @return: ListDataDiagnoseSampleDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_diagnose_sample_details_with_options(instance_id, request, headers, runtime)

    async def list_data_diagnose_sample_details_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListDataDiagnoseSampleDetailsRequest,
    ) -> airec_20201126_models.ListDataDiagnoseSampleDetailsResponse:
        """
        @summary 获取数据诊断项抽样明细
        
        @param request: ListDataDiagnoseSampleDetailsRequest
        @return: ListDataDiagnoseSampleDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_data_diagnose_sample_details_with_options_async(instance_id, request, headers, runtime)

    def list_data_set_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListDataSetResponse:
        """
        @summary Queries datasets of a specified instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSetResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDataSet',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/dataSets',
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
        """
        @summary Queries datasets of a specified instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSetResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDataSet',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/dataSets',
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

    def list_data_set(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ListDataSetResponse:
        """
        @summary Queries datasets of a specified instance.
        
        @return: ListDataSetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_set_with_options(instance_id, headers, runtime)

    async def list_data_set_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ListDataSetResponse:
        """
        @summary Queries datasets of a specified instance.
        
        @return: ListDataSetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_data_set_with_options_async(instance_id, headers, runtime)

    def list_data_source_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListDataSourceResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDataSource',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/dataSources',
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
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDataSource',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/dataSources',
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

    def list_data_source(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ListDataSourceResponse:
        """
        @return: ListDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_source_with_options(instance_id, headers, runtime)

    async def list_data_source_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ListDataSourceResponse:
        """
        @return: ListDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_data_source_with_options_async(instance_id, headers, runtime)

    def list_experiments_with_options(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListExperimentsResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExperimentsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListExperiments',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/experiments',
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
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExperimentsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListExperiments',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/experiments',
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

    def list_experiments(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.ListExperimentsResponse:
        """
        @return: ListExperimentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_experiments_with_options(instance_id, scene_id, headers, runtime)

    async def list_experiments_async(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.ListExperimentsResponse:
        """
        @return: ListExperimentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_experiments_with_options_async(instance_id, scene_id, headers, runtime)

    def list_extra_data_sources_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListExtraDataSourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListExtraDataSourcesResponse:
        """
        @summary 获取特征、样本等表扩展数据源列表
        
        @param request: ListExtraDataSourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExtraDataSourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExtraDataSources',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/extra-data-sources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListExtraDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_extra_data_sources_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListExtraDataSourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListExtraDataSourcesResponse:
        """
        @summary 获取特征、样本等表扩展数据源列表
        
        @param request: ListExtraDataSourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExtraDataSourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExtraDataSources',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/extra-data-sources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListExtraDataSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_extra_data_sources(
        self,
        instance_id: str,
        request: airec_20201126_models.ListExtraDataSourcesRequest,
    ) -> airec_20201126_models.ListExtraDataSourcesResponse:
        """
        @summary 获取特征、样本等表扩展数据源列表
        
        @param request: ListExtraDataSourcesRequest
        @return: ListExtraDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_extra_data_sources_with_options(instance_id, request, headers, runtime)

    async def list_extra_data_sources_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListExtraDataSourcesRequest,
    ) -> airec_20201126_models.ListExtraDataSourcesResponse:
        """
        @summary 获取特征、样本等表扩展数据源列表
        
        @param request: ListExtraDataSourcesRequest
        @return: ListExtraDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_extra_data_sources_with_options_async(instance_id, request, headers, runtime)

    def list_feature_tables_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListFeatureTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListFeatureTablesResponse:
        """
        @summary 获取特征表列表
        
        @param request: ListFeatureTablesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFeatureTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_id):
            query['dataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.update_frequency):
            query['updateFrequency'] = request.update_frequency
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFeatureTables',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/feature-tables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListFeatureTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_feature_tables_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListFeatureTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListFeatureTablesResponse:
        """
        @summary 获取特征表列表
        
        @param request: ListFeatureTablesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFeatureTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_id):
            query['dataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.update_frequency):
            query['updateFrequency'] = request.update_frequency
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFeatureTables',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/feature-tables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListFeatureTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_feature_tables(
        self,
        instance_id: str,
        request: airec_20201126_models.ListFeatureTablesRequest,
    ) -> airec_20201126_models.ListFeatureTablesResponse:
        """
        @summary 获取特征表列表
        
        @param request: ListFeatureTablesRequest
        @return: ListFeatureTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_feature_tables_with_options(instance_id, request, headers, runtime)

    async def list_feature_tables_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListFeatureTablesRequest,
    ) -> airec_20201126_models.ListFeatureTablesResponse:
        """
        @summary 获取特征表列表
        
        @param request: ListFeatureTablesRequest
        @return: ListFeatureTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_feature_tables_with_options_async(instance_id, request, headers, runtime)

    def list_filtering_algorithms_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListFilteringAlgorithmsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListFilteringAlgorithmsResponse:
        """
        @param request: ListFilteringAlgorithmsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFilteringAlgorithmsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm_id):
            query['algorithmId'] = request.algorithm_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFilteringAlgorithms',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/filtering-algorithms',
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
        """
        @param request: ListFilteringAlgorithmsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFilteringAlgorithmsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm_id):
            query['algorithmId'] = request.algorithm_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFilteringAlgorithms',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/filtering-algorithms',
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

    def list_filtering_algorithms(
        self,
        instance_id: str,
        request: airec_20201126_models.ListFilteringAlgorithmsRequest,
    ) -> airec_20201126_models.ListFilteringAlgorithmsResponse:
        """
        @param request: ListFilteringAlgorithmsRequest
        @return: ListFilteringAlgorithmsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_filtering_algorithms_with_options(instance_id, request, headers, runtime)

    async def list_filtering_algorithms_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListFilteringAlgorithmsRequest,
    ) -> airec_20201126_models.ListFilteringAlgorithmsResponse:
        """
        @param request: ListFilteringAlgorithmsRequest
        @return: ListFilteringAlgorithmsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_filtering_algorithms_with_options_async(instance_id, request, headers, runtime)

    def list_flow_control_task_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListFlowControlTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListFlowControlTaskResponse:
        """
        @summary 查询流控任务列表
        
        @param request: ListFlowControlTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFlowControlTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowControlTask',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/flowControlTasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListFlowControlTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_control_task_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListFlowControlTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListFlowControlTaskResponse:
        """
        @summary 查询流控任务列表
        
        @param request: ListFlowControlTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFlowControlTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowControlTask',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/flowControlTasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListFlowControlTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flow_control_task(
        self,
        instance_id: str,
        request: airec_20201126_models.ListFlowControlTaskRequest,
    ) -> airec_20201126_models.ListFlowControlTaskResponse:
        """
        @summary 查询流控任务列表
        
        @param request: ListFlowControlTaskRequest
        @return: ListFlowControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_flow_control_task_with_options(instance_id, request, headers, runtime)

    async def list_flow_control_task_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListFlowControlTaskRequest,
    ) -> airec_20201126_models.ListFlowControlTaskResponse:
        """
        @summary 查询流控任务列表
        
        @param request: ListFlowControlTaskRequest
        @return: ListFlowControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_flow_control_task_with_options_async(instance_id, request, headers, runtime)

    def list_flow_control_task_invalid_items_with_options(
        self,
        instance_id: str,
        task_id: str,
        request: airec_20201126_models.ListFlowControlTaskInvalidItemsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListFlowControlTaskInvalidItemsResponse:
        """
        @summary 查询失效物品 id_type
        
        @param request: ListFlowControlTaskInvalidItemsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFlowControlTaskInvalidItemsResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='ListFlowControlTaskInvalidItems',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/flowControlTasks/{OpenApiUtilClient.get_encode_param(task_id)}/invalidItems',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListFlowControlTaskInvalidItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_control_task_invalid_items_with_options_async(
        self,
        instance_id: str,
        task_id: str,
        request: airec_20201126_models.ListFlowControlTaskInvalidItemsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListFlowControlTaskInvalidItemsResponse:
        """
        @summary 查询失效物品 id_type
        
        @param request: ListFlowControlTaskInvalidItemsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFlowControlTaskInvalidItemsResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='ListFlowControlTaskInvalidItems',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/flowControlTasks/{OpenApiUtilClient.get_encode_param(task_id)}/invalidItems',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListFlowControlTaskInvalidItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flow_control_task_invalid_items(
        self,
        instance_id: str,
        task_id: str,
        request: airec_20201126_models.ListFlowControlTaskInvalidItemsRequest,
    ) -> airec_20201126_models.ListFlowControlTaskInvalidItemsResponse:
        """
        @summary 查询失效物品 id_type
        
        @param request: ListFlowControlTaskInvalidItemsRequest
        @return: ListFlowControlTaskInvalidItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_flow_control_task_invalid_items_with_options(instance_id, task_id, request, headers, runtime)

    async def list_flow_control_task_invalid_items_async(
        self,
        instance_id: str,
        task_id: str,
        request: airec_20201126_models.ListFlowControlTaskInvalidItemsRequest,
    ) -> airec_20201126_models.ListFlowControlTaskInvalidItemsResponse:
        """
        @summary 查询失效物品 id_type
        
        @param request: ListFlowControlTaskInvalidItemsRequest
        @return: ListFlowControlTaskInvalidItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_flow_control_task_invalid_items_with_options_async(instance_id, task_id, request, headers, runtime)

    def list_flow_control_task_item_reports_with_options(
        self,
        instance_id: str,
        task_id: str,
        request: airec_20201126_models.ListFlowControlTaskItemReportsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListFlowControlTaskItemReportsResponse:
        """
        @summary 流量调控曝光排名物品/失效物品查询
        
        @param request: ListFlowControlTaskItemReportsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFlowControlTaskItemReportsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.count):
            query['count'] = request.count
        if not UtilClient.is_unset(request.select_time_type):
            query['selectTimeType'] = request.select_time_type
        if not UtilClient.is_unset(request.select_type):
            query['selectType'] = request.select_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowControlTaskItemReports',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/flowControlTasks/{OpenApiUtilClient.get_encode_param(task_id)}/itemReports',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListFlowControlTaskItemReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_control_task_item_reports_with_options_async(
        self,
        instance_id: str,
        task_id: str,
        request: airec_20201126_models.ListFlowControlTaskItemReportsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListFlowControlTaskItemReportsResponse:
        """
        @summary 流量调控曝光排名物品/失效物品查询
        
        @param request: ListFlowControlTaskItemReportsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFlowControlTaskItemReportsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.count):
            query['count'] = request.count
        if not UtilClient.is_unset(request.select_time_type):
            query['selectTimeType'] = request.select_time_type
        if not UtilClient.is_unset(request.select_type):
            query['selectType'] = request.select_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowControlTaskItemReports',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/flowControlTasks/{OpenApiUtilClient.get_encode_param(task_id)}/itemReports',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListFlowControlTaskItemReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flow_control_task_item_reports(
        self,
        instance_id: str,
        task_id: str,
        request: airec_20201126_models.ListFlowControlTaskItemReportsRequest,
    ) -> airec_20201126_models.ListFlowControlTaskItemReportsResponse:
        """
        @summary 流量调控曝光排名物品/失效物品查询
        
        @param request: ListFlowControlTaskItemReportsRequest
        @return: ListFlowControlTaskItemReportsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_flow_control_task_item_reports_with_options(instance_id, task_id, request, headers, runtime)

    async def list_flow_control_task_item_reports_async(
        self,
        instance_id: str,
        task_id: str,
        request: airec_20201126_models.ListFlowControlTaskItemReportsRequest,
    ) -> airec_20201126_models.ListFlowControlTaskItemReportsResponse:
        """
        @summary 流量调控曝光排名物品/失效物品查询
        
        @param request: ListFlowControlTaskItemReportsRequest
        @return: ListFlowControlTaskItemReportsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_flow_control_task_item_reports_with_options_async(instance_id, task_id, request, headers, runtime)

    def list_flow_control_task_items_with_options(
        self,
        instance_id: str,
        task_id: str,
        request: airec_20201126_models.ListFlowControlTaskItemsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListFlowControlTaskItemsResponse:
        """
        @summary 流量调控预览
        
        @param request: ListFlowControlTaskItemsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFlowControlTaskItemsResponse
        """
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
            action='ListFlowControlTaskItems',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/flowControlTasks/{OpenApiUtilClient.get_encode_param(task_id)}/actions/items',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListFlowControlTaskItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_control_task_items_with_options_async(
        self,
        instance_id: str,
        task_id: str,
        request: airec_20201126_models.ListFlowControlTaskItemsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListFlowControlTaskItemsResponse:
        """
        @summary 流量调控预览
        
        @param request: ListFlowControlTaskItemsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFlowControlTaskItemsResponse
        """
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
            action='ListFlowControlTaskItems',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/flowControlTasks/{OpenApiUtilClient.get_encode_param(task_id)}/actions/items',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListFlowControlTaskItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flow_control_task_items(
        self,
        instance_id: str,
        task_id: str,
        request: airec_20201126_models.ListFlowControlTaskItemsRequest,
    ) -> airec_20201126_models.ListFlowControlTaskItemsResponse:
        """
        @summary 流量调控预览
        
        @param request: ListFlowControlTaskItemsRequest
        @return: ListFlowControlTaskItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_flow_control_task_items_with_options(instance_id, task_id, request, headers, runtime)

    async def list_flow_control_task_items_async(
        self,
        instance_id: str,
        task_id: str,
        request: airec_20201126_models.ListFlowControlTaskItemsRequest,
    ) -> airec_20201126_models.ListFlowControlTaskItemsResponse:
        """
        @summary 流量调控预览
        
        @param request: ListFlowControlTaskItemsRequest
        @return: ListFlowControlTaskItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_flow_control_task_items_with_options_async(instance_id, task_id, request, headers, runtime)

    def list_flow_control_task_reference_with_options(
        self,
        instance_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListFlowControlTaskReferenceResponse:
        """
        @summary Queries reference data for throttling.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFlowControlTaskReferenceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListFlowControlTaskReference',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/flowControlTasks/{OpenApiUtilClient.get_encode_param(task_id)}/reference',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListFlowControlTaskReferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_control_task_reference_with_options_async(
        self,
        instance_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListFlowControlTaskReferenceResponse:
        """
        @summary Queries reference data for throttling.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFlowControlTaskReferenceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListFlowControlTaskReference',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/flowControlTasks/{OpenApiUtilClient.get_encode_param(task_id)}/reference',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListFlowControlTaskReferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flow_control_task_reference(
        self,
        instance_id: str,
        task_id: str,
    ) -> airec_20201126_models.ListFlowControlTaskReferenceResponse:
        """
        @summary Queries reference data for throttling.
        
        @return: ListFlowControlTaskReferenceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_flow_control_task_reference_with_options(instance_id, task_id, headers, runtime)

    async def list_flow_control_task_reference_async(
        self,
        instance_id: str,
        task_id: str,
    ) -> airec_20201126_models.ListFlowControlTaskReferenceResponse:
        """
        @summary Queries reference data for throttling.
        
        @return: ListFlowControlTaskReferenceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_flow_control_task_reference_with_options_async(instance_id, task_id, headers, runtime)

    def list_flow_control_task_reports_with_options(
        self,
        instance_id: str,
        task_id: str,
        request: airec_20201126_models.ListFlowControlTaskReportsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListFlowControlTaskReportsResponse:
        """
        @summary 流量调控任务曝光分析
        
        @param request: ListFlowControlTaskReportsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFlowControlTaskReportsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowControlTaskReports',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/flowControlTasks/{OpenApiUtilClient.get_encode_param(task_id)}/flowTaskReports',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListFlowControlTaskReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_control_task_reports_with_options_async(
        self,
        instance_id: str,
        task_id: str,
        request: airec_20201126_models.ListFlowControlTaskReportsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListFlowControlTaskReportsResponse:
        """
        @summary 流量调控任务曝光分析
        
        @param request: ListFlowControlTaskReportsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFlowControlTaskReportsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowControlTaskReports',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/flowControlTasks/{OpenApiUtilClient.get_encode_param(task_id)}/flowTaskReports',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListFlowControlTaskReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flow_control_task_reports(
        self,
        instance_id: str,
        task_id: str,
        request: airec_20201126_models.ListFlowControlTaskReportsRequest,
    ) -> airec_20201126_models.ListFlowControlTaskReportsResponse:
        """
        @summary 流量调控任务曝光分析
        
        @param request: ListFlowControlTaskReportsRequest
        @return: ListFlowControlTaskReportsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_flow_control_task_reports_with_options(instance_id, task_id, request, headers, runtime)

    async def list_flow_control_task_reports_async(
        self,
        instance_id: str,
        task_id: str,
        request: airec_20201126_models.ListFlowControlTaskReportsRequest,
    ) -> airec_20201126_models.ListFlowControlTaskReportsResponse:
        """
        @summary 流量调控任务曝光分析
        
        @param request: ListFlowControlTaskReportsRequest
        @return: ListFlowControlTaskReportsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_flow_control_task_reports_with_options_async(instance_id, task_id, request, headers, runtime)

    def list_index_versions_with_options(
        self,
        instance_id: str,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListIndexVersionsResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIndexVersionsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListIndexVersions',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/filtering-algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}/index-versions',
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
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIndexVersionsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListIndexVersions',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/filtering-algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}/index-versions',
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

    def list_index_versions(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.ListIndexVersionsResponse:
        """
        @return: ListIndexVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_index_versions_with_options(instance_id, algorithm_id, headers, runtime)

    async def list_index_versions_async(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.ListIndexVersionsResponse:
        """
        @return: ListIndexVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_index_versions_with_options_async(instance_id, algorithm_id, headers, runtime)

    def list_instance_with_options(
        self,
        request: airec_20201126_models.ListInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListInstanceResponse:
        """
        @summary Queries the information of instances.
        
        @description You can call this API operation to query the list of instances. The returned instances are ranked in descending order based on the values of GmtCreate. You can specify multiple request parameters. These request parameters can be used to filter query results. The request parameters that you specify have logical AND relations. Only the specified parameters can be used to filter query results.
        
        @param request: ListInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expired_time):
            query['expiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
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
        """
        @summary Queries the information of instances.
        
        @description You can call this API operation to query the list of instances. The returned instances are ranked in descending order based on the values of GmtCreate. You can specify multiple request parameters. These request parameters can be used to filter query results. The request parameters that you specify have logical AND relations. Only the specified parameters can be used to filter query results.
        
        @param request: ListInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expired_time):
            query['expiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
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

    def list_instance(
        self,
        request: airec_20201126_models.ListInstanceRequest,
    ) -> airec_20201126_models.ListInstanceResponse:
        """
        @summary Queries the information of instances.
        
        @description You can call this API operation to query the list of instances. The returned instances are ranked in descending order based on the values of GmtCreate. You can specify multiple request parameters. These request parameters can be used to filter query results. The request parameters that you specify have logical AND relations. Only the specified parameters can be used to filter query results.
        
        @param request: ListInstanceRequest
        @return: ListInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_with_options(request, headers, runtime)

    async def list_instance_async(
        self,
        request: airec_20201126_models.ListInstanceRequest,
    ) -> airec_20201126_models.ListInstanceResponse:
        """
        @summary Queries the information of instances.
        
        @description You can call this API operation to query the list of instances. The returned instances are ranked in descending order based on the values of GmtCreate. You can specify multiple request parameters. These request parameters can be used to filter query results. The request parameters that you specify have logical AND relations. Only the specified parameters can be used to filter query results.
        
        @param request: ListInstanceRequest
        @return: ListInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instance_with_options_async(request, headers, runtime)

    def list_instance_task_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListInstanceTaskResponse:
        """
        @summary Queries all asynchronous tasks of a specified instance by using the instance ID.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListInstanceTask',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tasks',
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
        """
        @summary Queries all asynchronous tasks of a specified instance by using the instance ID.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListInstanceTask',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tasks',
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

    def list_instance_task(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ListInstanceTaskResponse:
        """
        @summary Queries all asynchronous tasks of a specified instance by using the instance ID.
        
        @return: ListInstanceTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_task_with_options(instance_id, headers, runtime)

    async def list_instance_task_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ListInstanceTaskResponse:
        """
        @summary Queries all asynchronous tasks of a specified instance by using the instance ID.
        
        @return: ListInstanceTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instance_task_with_options_async(instance_id, headers, runtime)

    def list_items_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListItemsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListItemsResponse:
        """
        @param request: ListItemsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListItemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.strategy_used):
            query['strategyUsed'] = request.strategy_used
        if not UtilClient.is_unset(request.with_invalid_detail):
            query['withInvalidDetail'] = request.with_invalid_detail
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListItems',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/items/actions/list',
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
        """
        @param request: ListItemsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListItemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.strategy_used):
            query['strategyUsed'] = request.strategy_used
        if not UtilClient.is_unset(request.with_invalid_detail):
            query['withInvalidDetail'] = request.with_invalid_detail
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListItems',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/items/actions/list',
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

    def list_items(
        self,
        instance_id: str,
        request: airec_20201126_models.ListItemsRequest,
    ) -> airec_20201126_models.ListItemsResponse:
        """
        @param request: ListItemsRequest
        @return: ListItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_items_with_options(instance_id, request, headers, runtime)

    async def list_items_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListItemsRequest,
    ) -> airec_20201126_models.ListItemsResponse:
        """
        @param request: ListItemsRequest
        @return: ListItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_items_with_options_async(instance_id, request, headers, runtime)

    def list_logs_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListLogsResponse:
        """
        @param request: ListLogsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.query_params):
            query['queryParams'] = request.query_params
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogs',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/logs',
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
        """
        @param request: ListLogsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.query_params):
            query['queryParams'] = request.query_params
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogs',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/logs',
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

    def list_logs(
        self,
        instance_id: str,
        request: airec_20201126_models.ListLogsRequest,
    ) -> airec_20201126_models.ListLogsResponse:
        """
        @param request: ListLogsRequest
        @return: ListLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_logs_with_options(instance_id, request, headers, runtime)

    async def list_logs_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListLogsRequest,
    ) -> airec_20201126_models.ListLogsResponse:
        """
        @param request: ListLogsRequest
        @return: ListLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_logs_with_options_async(instance_id, request, headers, runtime)

    def list_mix_categories_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListMixCategoriesResponse:
        """
        @summary Queries the content types supported in the diversity rule configurations of an instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMixCategoriesResponse
        """
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
        """
        @summary Queries the content types supported in the diversity rule configurations of an instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMixCategoriesResponse
        """
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

    def list_mix_categories(self) -> airec_20201126_models.ListMixCategoriesResponse:
        """
        @summary Queries the content types supported in the diversity rule configurations of an instance.
        
        @return: ListMixCategoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_mix_categories_with_options(headers, runtime)

    async def list_mix_categories_async(self) -> airec_20201126_models.ListMixCategoriesResponse:
        """
        @summary Queries the content types supported in the diversity rule configurations of an instance.
        
        @return: ListMixCategoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_mix_categories_with_options_async(headers, runtime)

    def list_offline_storages_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListOfflineStoragesResponse:
        """
        @summary 获取离线存储列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOfflineStoragesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListOfflineStorages',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/%5BinstanceId%5D/offlineStorages',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListOfflineStoragesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_offline_storages_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListOfflineStoragesResponse:
        """
        @summary 获取离线存储列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOfflineStoragesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListOfflineStorages',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/%5BinstanceId%5D/offlineStorages',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListOfflineStoragesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_offline_storages(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ListOfflineStoragesResponse:
        """
        @summary 获取离线存储列表
        
        @return: ListOfflineStoragesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_offline_storages_with_options(instance_id, headers, runtime)

    async def list_offline_storages_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ListOfflineStoragesResponse:
        """
        @summary 获取离线存储列表
        
        @return: ListOfflineStoragesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_offline_storages_with_options_async(instance_id, headers, runtime)

    def list_ranking_model_templates_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRankingModelTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListRankingModelTemplatesResponse:
        """
        @summary Queries the templates of a ranking model. The returned templates are sorted in reverse chronological order based on the time when the templates were created.
        
        @param request: ListRankingModelTemplatesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRankingModelTemplatesResponse
        """
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
            action='ListRankingModelTemplates',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-model-templates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListRankingModelTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ranking_model_templates_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRankingModelTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListRankingModelTemplatesResponse:
        """
        @summary Queries the templates of a ranking model. The returned templates are sorted in reverse chronological order based on the time when the templates were created.
        
        @param request: ListRankingModelTemplatesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRankingModelTemplatesResponse
        """
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
            action='ListRankingModelTemplates',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-model-templates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListRankingModelTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ranking_model_templates(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRankingModelTemplatesRequest,
    ) -> airec_20201126_models.ListRankingModelTemplatesResponse:
        """
        @summary Queries the templates of a ranking model. The returned templates are sorted in reverse chronological order based on the time when the templates were created.
        
        @param request: ListRankingModelTemplatesRequest
        @return: ListRankingModelTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ranking_model_templates_with_options(instance_id, request, headers, runtime)

    async def list_ranking_model_templates_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRankingModelTemplatesRequest,
    ) -> airec_20201126_models.ListRankingModelTemplatesResponse:
        """
        @summary Queries the templates of a ranking model. The returned templates are sorted in reverse chronological order based on the time when the templates were created.
        
        @param request: ListRankingModelTemplatesRequest
        @return: ListRankingModelTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_ranking_model_templates_with_options_async(instance_id, request, headers, runtime)

    def list_ranking_model_versions_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRankingModelVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListRankingModelVersionsResponse:
        """
        @summary Queries a list of versions for a ranking model.
        
        @param request: ListRankingModelVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRankingModelVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.template_id):
            query['templateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRankingModelVersions',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-model-versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListRankingModelVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ranking_model_versions_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRankingModelVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListRankingModelVersionsResponse:
        """
        @summary Queries a list of versions for a ranking model.
        
        @param request: ListRankingModelVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRankingModelVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.template_id):
            query['templateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRankingModelVersions',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-model-versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListRankingModelVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ranking_model_versions(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRankingModelVersionsRequest,
    ) -> airec_20201126_models.ListRankingModelVersionsResponse:
        """
        @summary Queries a list of versions for a ranking model.
        
        @param request: ListRankingModelVersionsRequest
        @return: ListRankingModelVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ranking_model_versions_with_options(instance_id, request, headers, runtime)

    async def list_ranking_model_versions_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRankingModelVersionsRequest,
    ) -> airec_20201126_models.ListRankingModelVersionsResponse:
        """
        @summary Queries a list of versions for a ranking model.
        
        @param request: ListRankingModelVersionsRequest
        @return: ListRankingModelVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_ranking_model_versions_with_options_async(instance_id, request, headers, runtime)

    def list_ranking_models_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRankingModelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListRankingModelsResponse:
        """
        @param request: ListRankingModelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRankingModelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.ranking_model_id):
            query['rankingModelId'] = request.ranking_model_id
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
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-models',
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
        """
        @param request: ListRankingModelsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRankingModelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.ranking_model_id):
            query['rankingModelId'] = request.ranking_model_id
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
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-models',
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

    def list_ranking_models(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRankingModelsRequest,
    ) -> airec_20201126_models.ListRankingModelsResponse:
        """
        @param request: ListRankingModelsRequest
        @return: ListRankingModelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ranking_models_with_options(instance_id, request, headers, runtime)

    async def list_ranking_models_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRankingModelsRequest,
    ) -> airec_20201126_models.ListRankingModelsResponse:
        """
        @param request: ListRankingModelsRequest
        @return: ListRankingModelsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_ranking_models_with_options_async(instance_id, request, headers, runtime)

    def list_ranking_system_histories_with_options(
        self,
        instance_id: str,
        name: str,
        request: airec_20201126_models.ListRankingSystemHistoriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListRankingSystemHistoriesResponse:
        """
        @summary The ID of the instance.
        
        @param request: ListRankingSystemHistoriesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRankingSystemHistoriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operate_type):
            query['operateType'] = request.operate_type
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRankingSystemHistories',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-systems/{OpenApiUtilClient.get_encode_param(name)}/histories',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListRankingSystemHistoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ranking_system_histories_with_options_async(
        self,
        instance_id: str,
        name: str,
        request: airec_20201126_models.ListRankingSystemHistoriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListRankingSystemHistoriesResponse:
        """
        @summary The ID of the instance.
        
        @param request: ListRankingSystemHistoriesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRankingSystemHistoriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operate_type):
            query['operateType'] = request.operate_type
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRankingSystemHistories',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-systems/{OpenApiUtilClient.get_encode_param(name)}/histories',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListRankingSystemHistoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ranking_system_histories(
        self,
        instance_id: str,
        name: str,
        request: airec_20201126_models.ListRankingSystemHistoriesRequest,
    ) -> airec_20201126_models.ListRankingSystemHistoriesResponse:
        """
        @summary The ID of the instance.
        
        @param request: ListRankingSystemHistoriesRequest
        @return: ListRankingSystemHistoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ranking_system_histories_with_options(instance_id, name, request, headers, runtime)

    async def list_ranking_system_histories_async(
        self,
        instance_id: str,
        name: str,
        request: airec_20201126_models.ListRankingSystemHistoriesRequest,
    ) -> airec_20201126_models.ListRankingSystemHistoriesResponse:
        """
        @summary The ID of the instance.
        
        @param request: ListRankingSystemHistoriesRequest
        @return: ListRankingSystemHistoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_ranking_system_histories_with_options_async(instance_id, name, request, headers, runtime)

    def list_ranking_systems_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRankingSystemsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListRankingSystemsResponse:
        """
        @summary 获取排序服务列表
        
        @param request: ListRankingSystemsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRankingSystemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deploy_status):
            query['deployStatus'] = request.deploy_status
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRankingSystems',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-systems',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListRankingSystemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ranking_systems_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRankingSystemsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListRankingSystemsResponse:
        """
        @summary 获取排序服务列表
        
        @param request: ListRankingSystemsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRankingSystemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deploy_status):
            query['deployStatus'] = request.deploy_status
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRankingSystems',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-systems',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListRankingSystemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ranking_systems(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRankingSystemsRequest,
    ) -> airec_20201126_models.ListRankingSystemsResponse:
        """
        @summary 获取排序服务列表
        
        @param request: ListRankingSystemsRequest
        @return: ListRankingSystemsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ranking_systems_with_options(instance_id, request, headers, runtime)

    async def list_ranking_systems_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRankingSystemsRequest,
    ) -> airec_20201126_models.ListRankingSystemsResponse:
        """
        @summary 获取排序服务列表
        
        @param request: ListRankingSystemsRequest
        @return: ListRankingSystemsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_ranking_systems_with_options_async(instance_id, request, headers, runtime)

    def list_rule_conditions_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListRuleConditionsResponse:
        """
        @summary Queries item selection rules of an instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRuleConditionsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListRuleConditions',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/rule-conditions',
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
        """
        @summary Queries item selection rules of an instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRuleConditionsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListRuleConditions',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/rule-conditions',
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

    def list_rule_conditions(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ListRuleConditionsResponse:
        """
        @summary Queries item selection rules of an instance.
        
        @return: ListRuleConditionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_rule_conditions_with_options(instance_id, headers, runtime)

    async def list_rule_conditions_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ListRuleConditionsResponse:
        """
        @summary Queries item selection rules of an instance.
        
        @return: ListRuleConditionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_rule_conditions_with_options_async(instance_id, headers, runtime)

    def list_rule_tasks_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRuleTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListRuleTasksResponse:
        """
        @summary The returned results.
        
        @param request: ListRuleTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRuleTasksResponse
        """
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
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/rule-tasks',
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
        """
        @summary The returned results.
        
        @param request: ListRuleTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRuleTasksResponse
        """
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
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/rule-tasks',
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

    def list_rule_tasks(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRuleTasksRequest,
    ) -> airec_20201126_models.ListRuleTasksResponse:
        """
        @summary The returned results.
        
        @param request: ListRuleTasksRequest
        @return: ListRuleTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_rule_tasks_with_options(instance_id, request, headers, runtime)

    async def list_rule_tasks_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRuleTasksRequest,
    ) -> airec_20201126_models.ListRuleTasksResponse:
        """
        @summary The returned results.
        
        @param request: ListRuleTasksRequest
        @return: ListRuleTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_rule_tasks_with_options_async(instance_id, request, headers, runtime)

    def list_rules_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListRulesResponse:
        """
        @param request: ListRulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.rule_type):
            query['ruleType'] = request.rule_type
        if not UtilClient.is_unset(request.scene_id):
            query['sceneId'] = request.scene_id
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRules',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/rules',
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
        """
        @param request: ListRulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.rule_type):
            query['ruleType'] = request.rule_type
        if not UtilClient.is_unset(request.scene_id):
            query['sceneId'] = request.scene_id
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRules',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/rules',
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

    def list_rules(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRulesRequest,
    ) -> airec_20201126_models.ListRulesResponse:
        """
        @param request: ListRulesRequest
        @return: ListRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_rules_with_options(instance_id, request, headers, runtime)

    async def list_rules_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListRulesRequest,
    ) -> airec_20201126_models.ListRulesResponse:
        """
        @param request: ListRulesRequest
        @return: ListRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_rules_with_options_async(instance_id, request, headers, runtime)

    def list_sample_format_configs_with_options(
        self,
        instance_id: str,
        sample_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListSampleFormatConfigsResponse:
        """
        @summary 获取样本格式化配置列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSampleFormatConfigsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSampleFormatConfigs',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/samples/{OpenApiUtilClient.get_encode_param(sample_id)}/format-configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListSampleFormatConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sample_format_configs_with_options_async(
        self,
        instance_id: str,
        sample_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListSampleFormatConfigsResponse:
        """
        @summary 获取样本格式化配置列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSampleFormatConfigsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSampleFormatConfigs',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/samples/{OpenApiUtilClient.get_encode_param(sample_id)}/format-configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListSampleFormatConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sample_format_configs(
        self,
        instance_id: str,
        sample_id: str,
    ) -> airec_20201126_models.ListSampleFormatConfigsResponse:
        """
        @summary 获取样本格式化配置列表
        
        @return: ListSampleFormatConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_sample_format_configs_with_options(instance_id, sample_id, headers, runtime)

    async def list_sample_format_configs_async(
        self,
        instance_id: str,
        sample_id: str,
    ) -> airec_20201126_models.ListSampleFormatConfigsResponse:
        """
        @summary 获取样本格式化配置列表
        
        @return: ListSampleFormatConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_sample_format_configs_with_options_async(instance_id, sample_id, headers, runtime)

    def list_samples_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListSamplesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListSamplesResponse:
        """
        @summary 获取样本列表
        
        @param request: ListSamplesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSamplesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.sample_id):
            query['sampleId'] = request.sample_id
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSamples',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/samples',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListSamplesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_samples_with_options_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListSamplesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListSamplesResponse:
        """
        @summary 获取样本列表
        
        @param request: ListSamplesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSamplesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.sample_id):
            query['sampleId'] = request.sample_id
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSamples',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/samples',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ListSamplesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_samples(
        self,
        instance_id: str,
        request: airec_20201126_models.ListSamplesRequest,
    ) -> airec_20201126_models.ListSamplesResponse:
        """
        @summary 获取样本列表
        
        @param request: ListSamplesRequest
        @return: ListSamplesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_samples_with_options(instance_id, request, headers, runtime)

    async def list_samples_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListSamplesRequest,
    ) -> airec_20201126_models.ListSamplesResponse:
        """
        @summary 获取样本列表
        
        @param request: ListSamplesRequest
        @return: ListSamplesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_samples_with_options_async(instance_id, request, headers, runtime)

    def list_scene_items_with_options(
        self,
        instance_id: str,
        scene_id: str,
        request: airec_20201126_models.ListSceneItemsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListSceneItemsResponse:
        """
        @summary Queries preview results.
        
        @description We recommend that you do not call an API operation to manage scenes. We recommend that you go to the Scenario Building page in the Artificial Intelligence Recommendation (AIRec) console to manage scenes.
        
        @param request: ListSceneItemsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSceneItemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_rule_id):
            query['operationRuleId'] = request.operation_rule_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.preview_type):
            query['previewType'] = request.preview_type
        if not UtilClient.is_unset(request.query_count):
            query['queryCount'] = request.query_count
        if not UtilClient.is_unset(request.selection_rule_id):
            query['selectionRuleId'] = request.selection_rule_id
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSceneItems',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/items',
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
        """
        @summary Queries preview results.
        
        @description We recommend that you do not call an API operation to manage scenes. We recommend that you go to the Scenario Building page in the Artificial Intelligence Recommendation (AIRec) console to manage scenes.
        
        @param request: ListSceneItemsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSceneItemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_rule_id):
            query['operationRuleId'] = request.operation_rule_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.preview_type):
            query['previewType'] = request.preview_type
        if not UtilClient.is_unset(request.query_count):
            query['queryCount'] = request.query_count
        if not UtilClient.is_unset(request.selection_rule_id):
            query['selectionRuleId'] = request.selection_rule_id
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSceneItems',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/items',
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

    def list_scene_items(
        self,
        instance_id: str,
        scene_id: str,
        request: airec_20201126_models.ListSceneItemsRequest,
    ) -> airec_20201126_models.ListSceneItemsResponse:
        """
        @summary Queries preview results.
        
        @description We recommend that you do not call an API operation to manage scenes. We recommend that you go to the Scenario Building page in the Artificial Intelligence Recommendation (AIRec) console to manage scenes.
        
        @param request: ListSceneItemsRequest
        @return: ListSceneItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_scene_items_with_options(instance_id, scene_id, request, headers, runtime)

    async def list_scene_items_async(
        self,
        instance_id: str,
        scene_id: str,
        request: airec_20201126_models.ListSceneItemsRequest,
    ) -> airec_20201126_models.ListSceneItemsResponse:
        """
        @summary Queries preview results.
        
        @description We recommend that you do not call an API operation to manage scenes. We recommend that you go to the Scenario Building page in the Artificial Intelligence Recommendation (AIRec) console to manage scenes.
        
        @param request: ListSceneItemsRequest
        @return: ListSceneItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_scene_items_with_options_async(instance_id, scene_id, request, headers, runtime)

    def list_scene_parameters_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListSceneParametersResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSceneParametersResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSceneParameters',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/dashboard/scene-parameters',
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
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSceneParametersResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSceneParameters',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/dashboard/scene-parameters',
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

    def list_scene_parameters(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ListSceneParametersResponse:
        """
        @return: ListSceneParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_scene_parameters_with_options(instance_id, headers, runtime)

    async def list_scene_parameters_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ListSceneParametersResponse:
        """
        @return: ListSceneParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_scene_parameters_with_options_async(instance_id, headers, runtime)

    def list_scenes_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.ListScenesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListScenesResponse:
        """
        @summary Queries scenes of a specified instance.
        
        @description We recommend that you do not call an API operation to manage scenes. Go to the Scenario Building page in the AIRec console to manage scenes.
        
        @param request: ListScenesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScenesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.scene_id):
            query['sceneId'] = request.scene_id
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScenes',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes',
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
        """
        @summary Queries scenes of a specified instance.
        
        @description We recommend that you do not call an API operation to manage scenes. Go to the Scenario Building page in the AIRec console to manage scenes.
        
        @param request: ListScenesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScenesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.scene_id):
            query['sceneId'] = request.scene_id
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScenes',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes',
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

    def list_scenes(
        self,
        instance_id: str,
        request: airec_20201126_models.ListScenesRequest,
    ) -> airec_20201126_models.ListScenesResponse:
        """
        @summary Queries scenes of a specified instance.
        
        @description We recommend that you do not call an API operation to manage scenes. Go to the Scenario Building page in the AIRec console to manage scenes.
        
        @param request: ListScenesRequest
        @return: ListScenesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_scenes_with_options(instance_id, request, headers, runtime)

    async def list_scenes_async(
        self,
        instance_id: str,
        request: airec_20201126_models.ListScenesRequest,
    ) -> airec_20201126_models.ListScenesResponse:
        """
        @summary Queries scenes of a specified instance.
        
        @description We recommend that you do not call an API operation to manage scenes. Go to the Scenario Building page in the AIRec console to manage scenes.
        
        @param request: ListScenesRequest
        @return: ListScenesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_scenes_with_options_async(instance_id, request, headers, runtime)

    def list_umeng_appkeys_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListUmengAppkeysResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUmengAppkeysResponse
        """
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
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUmengAppkeysResponse
        """
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

    def list_umeng_appkeys(self) -> airec_20201126_models.ListUmengAppkeysResponse:
        """
        @return: ListUmengAppkeysResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_umeng_appkeys_with_options(headers, runtime)

    async def list_umeng_appkeys_async(self) -> airec_20201126_models.ListUmengAppkeysResponse:
        """
        @return: ListUmengAppkeysResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_umeng_appkeys_with_options_async(headers, runtime)

    def list_user_clusters_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ListUserClustersResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserClustersResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListUserClusters',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/user-clusters',
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
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserClustersResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListUserClusters',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/user-clusters',
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

    def list_user_clusters(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ListUserClustersResponse:
        """
        @return: ListUserClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_user_clusters_with_options(instance_id, headers, runtime)

    async def list_user_clusters_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ListUserClustersResponse:
        """
        @return: ListUserClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_user_clusters_with_options_async(instance_id, headers, runtime)

    def modify_data_source_with_options(
        self,
        instance_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifyDataSourceResponse:
        """
        @summary Modifies the information of a single data source in a table of a specified instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDataSourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyDataSource',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/dataSources/{OpenApiUtilClient.get_encode_param(table_name)}',
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
        """
        @summary Modifies the information of a single data source in a table of a specified instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDataSourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyDataSource',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/dataSources/{OpenApiUtilClient.get_encode_param(table_name)}',
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

    def modify_data_source(
        self,
        instance_id: str,
        table_name: str,
    ) -> airec_20201126_models.ModifyDataSourceResponse:
        """
        @summary Modifies the information of a single data source in a table of a specified instance.
        
        @return: ModifyDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_data_source_with_options(instance_id, table_name, headers, runtime)

    async def modify_data_source_async(
        self,
        instance_id: str,
        table_name: str,
    ) -> airec_20201126_models.ModifyDataSourceResponse:
        """
        @summary Modifies the information of a single data source in a table of a specified instance.
        
        @return: ModifyDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_data_source_with_options_async(instance_id, table_name, headers, runtime)

    def modify_feature_table_with_options(
        self,
        instance_id: str,
        type: str,
        feature_table_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifyFeatureTableResponse:
        """
        @summary 修改特征表，只支表级别持特征列表的全量修改
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyFeatureTableResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyFeatureTable',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/feature-tables/{OpenApiUtilClient.get_encode_param(type)}/{OpenApiUtilClient.get_encode_param(feature_table_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ModifyFeatureTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_feature_table_with_options_async(
        self,
        instance_id: str,
        type: str,
        feature_table_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifyFeatureTableResponse:
        """
        @summary 修改特征表，只支表级别持特征列表的全量修改
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyFeatureTableResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyFeatureTable',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/feature-tables/{OpenApiUtilClient.get_encode_param(type)}/{OpenApiUtilClient.get_encode_param(feature_table_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ModifyFeatureTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_feature_table(
        self,
        instance_id: str,
        type: str,
        feature_table_id: str,
    ) -> airec_20201126_models.ModifyFeatureTableResponse:
        """
        @summary 修改特征表，只支表级别持特征列表的全量修改
        
        @return: ModifyFeatureTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_feature_table_with_options(instance_id, type, feature_table_id, headers, runtime)

    async def modify_feature_table_async(
        self,
        instance_id: str,
        type: str,
        feature_table_id: str,
    ) -> airec_20201126_models.ModifyFeatureTableResponse:
        """
        @summary 修改特征表，只支表级别持特征列表的全量修改
        
        @return: ModifyFeatureTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_feature_table_with_options_async(instance_id, type, feature_table_id, headers, runtime)

    def modify_filtering_algorithm_meta_with_options(
        self,
        instance_id: str,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifyFilteringAlgorithmMetaResponse:
        """
        @summary The name of the project.
        
        @description The name of the filtering algorithm.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyFilteringAlgorithmMetaResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyFilteringAlgorithmMeta',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/filtering-algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}/meta',
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
        """
        @summary The name of the project.
        
        @description The name of the filtering algorithm.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyFilteringAlgorithmMetaResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyFilteringAlgorithmMeta',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/filtering-algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}/meta',
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

    def modify_filtering_algorithm_meta(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.ModifyFilteringAlgorithmMetaResponse:
        """
        @summary The name of the project.
        
        @description The name of the filtering algorithm.
        
        @return: ModifyFilteringAlgorithmMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_filtering_algorithm_meta_with_options(instance_id, algorithm_id, headers, runtime)

    async def modify_filtering_algorithm_meta_async(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.ModifyFilteringAlgorithmMetaResponse:
        """
        @summary The name of the project.
        
        @description The name of the filtering algorithm.
        
        @return: ModifyFilteringAlgorithmMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_filtering_algorithm_meta_with_options_async(instance_id, algorithm_id, headers, runtime)

    def modify_flow_control_task_with_options(
        self,
        instance_id: str,
        task_id: str,
        request: airec_20201126_models.ModifyFlowControlTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifyFlowControlTaskResponse:
        """
        @summary Modifies a throttling task.
        
        @param request: ModifyFlowControlTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyFlowControlTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.meta_type):
            body['metaType'] = request.meta_type
        if not UtilClient.is_unset(request.scene_ids):
            body['sceneIds'] = request.scene_ids
        if not UtilClient.is_unset(request.selection_params):
            body['selectionParams'] = request.selection_params
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.target):
            body['target'] = request.target
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyFlowControlTask',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/flowControlTasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ModifyFlowControlTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_flow_control_task_with_options_async(
        self,
        instance_id: str,
        task_id: str,
        request: airec_20201126_models.ModifyFlowControlTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifyFlowControlTaskResponse:
        """
        @summary Modifies a throttling task.
        
        @param request: ModifyFlowControlTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyFlowControlTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.meta_type):
            body['metaType'] = request.meta_type
        if not UtilClient.is_unset(request.scene_ids):
            body['sceneIds'] = request.scene_ids
        if not UtilClient.is_unset(request.selection_params):
            body['selectionParams'] = request.selection_params
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.target):
            body['target'] = request.target
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyFlowControlTask',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/flowControlTasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ModifyFlowControlTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_flow_control_task(
        self,
        instance_id: str,
        task_id: str,
        request: airec_20201126_models.ModifyFlowControlTaskRequest,
    ) -> airec_20201126_models.ModifyFlowControlTaskResponse:
        """
        @summary Modifies a throttling task.
        
        @param request: ModifyFlowControlTaskRequest
        @return: ModifyFlowControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_flow_control_task_with_options(instance_id, task_id, request, headers, runtime)

    async def modify_flow_control_task_async(
        self,
        instance_id: str,
        task_id: str,
        request: airec_20201126_models.ModifyFlowControlTaskRequest,
    ) -> airec_20201126_models.ModifyFlowControlTaskResponse:
        """
        @summary Modifies a throttling task.
        
        @param request: ModifyFlowControlTaskRequest
        @return: ModifyFlowControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_flow_control_task_with_options_async(instance_id, task_id, request, headers, runtime)

    def modify_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifyInstanceResponse:
        """
        @summary Modifies the configurations of a specified instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyInstance',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
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
        """
        @summary Modifies the configurations of a specified instance.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyInstance',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
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

    def modify_instance(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ModifyInstanceResponse:
        """
        @summary Modifies the configurations of a specified instance.
        
        @return: ModifyInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_instance_with_options(instance_id, headers, runtime)

    async def modify_instance_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ModifyInstanceResponse:
        """
        @summary Modifies the configurations of a specified instance.
        
        @return: ModifyInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_instance_with_options_async(instance_id, headers, runtime)

    def modify_items_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifyItemsResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyItemsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyItems',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/items',
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
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyItemsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyItems',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/items',
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

    def modify_items(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ModifyItemsResponse:
        """
        @return: ModifyItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_items_with_options(instance_id, headers, runtime)

    async def modify_items_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ModifyItemsResponse:
        """
        @return: ModifyItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_items_with_options_async(instance_id, headers, runtime)

    def modify_offline_storages_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifyOfflineStoragesResponse:
        """
        @summary Modifies the offline storage configurations of an instance. You need to modify three tables at the same time.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyOfflineStoragesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyOfflineStorages',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/%5BinstanceId%5D/offlineStorages',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ModifyOfflineStoragesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_offline_storages_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifyOfflineStoragesResponse:
        """
        @summary Modifies the offline storage configurations of an instance. You need to modify three tables at the same time.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyOfflineStoragesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyOfflineStorages',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/%5BinstanceId%5D/offlineStorages',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ModifyOfflineStoragesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_offline_storages(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ModifyOfflineStoragesResponse:
        """
        @summary Modifies the offline storage configurations of an instance. You need to modify three tables at the same time.
        
        @return: ModifyOfflineStoragesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_offline_storages_with_options(instance_id, headers, runtime)

    async def modify_offline_storages_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ModifyOfflineStoragesResponse:
        """
        @summary Modifies the offline storage configurations of an instance. You need to modify three tables at the same time.
        
        @return: ModifyOfflineStoragesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_offline_storages_with_options_async(instance_id, headers, runtime)

    def modify_ranking_model_with_options(
        self,
        instance_id: str,
        ranking_model_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifyRankingModelResponse:
        """
        @summary The ID of the ranking model.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyRankingModelResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyRankingModel',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-models/{OpenApiUtilClient.get_encode_param(ranking_model_id)}',
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
        """
        @summary The ID of the ranking model.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyRankingModelResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyRankingModel',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-models/{OpenApiUtilClient.get_encode_param(ranking_model_id)}',
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

    def modify_ranking_model(
        self,
        instance_id: str,
        ranking_model_id: str,
    ) -> airec_20201126_models.ModifyRankingModelResponse:
        """
        @summary The ID of the ranking model.
        
        @return: ModifyRankingModelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_ranking_model_with_options(instance_id, ranking_model_id, headers, runtime)

    async def modify_ranking_model_async(
        self,
        instance_id: str,
        ranking_model_id: str,
    ) -> airec_20201126_models.ModifyRankingModelResponse:
        """
        @summary The ID of the ranking model.
        
        @return: ModifyRankingModelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_ranking_model_with_options_async(instance_id, ranking_model_id, headers, runtime)

    def modify_ranking_model_template_with_options(
        self,
        instance_id: str,
        template_id: str,
        request: airec_20201126_models.ModifyRankingModelTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifyRankingModelTemplateResponse:
        """
        @summary Modifies a ranking model.
        
        @param request: ModifyRankingModelTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyRankingModelTemplateResponse
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
            action='ModifyRankingModelTemplate',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-model-templates/{OpenApiUtilClient.get_encode_param(template_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ModifyRankingModelTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_ranking_model_template_with_options_async(
        self,
        instance_id: str,
        template_id: str,
        request: airec_20201126_models.ModifyRankingModelTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifyRankingModelTemplateResponse:
        """
        @summary Modifies a ranking model.
        
        @param request: ModifyRankingModelTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyRankingModelTemplateResponse
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
            action='ModifyRankingModelTemplate',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-model-templates/{OpenApiUtilClient.get_encode_param(template_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ModifyRankingModelTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_ranking_model_template(
        self,
        instance_id: str,
        template_id: str,
        request: airec_20201126_models.ModifyRankingModelTemplateRequest,
    ) -> airec_20201126_models.ModifyRankingModelTemplateResponse:
        """
        @summary Modifies a ranking model.
        
        @param request: ModifyRankingModelTemplateRequest
        @return: ModifyRankingModelTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_ranking_model_template_with_options(instance_id, template_id, request, headers, runtime)

    async def modify_ranking_model_template_async(
        self,
        instance_id: str,
        template_id: str,
        request: airec_20201126_models.ModifyRankingModelTemplateRequest,
    ) -> airec_20201126_models.ModifyRankingModelTemplateResponse:
        """
        @summary Modifies a ranking model.
        
        @param request: ModifyRankingModelTemplateRequest
        @return: ModifyRankingModelTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_ranking_model_template_with_options_async(instance_id, template_id, request, headers, runtime)

    def modify_ranking_system_with_options(
        self,
        instance_id: str,
        name: str,
        request: airec_20201126_models.ModifyRankingSystemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifyRankingSystemResponse:
        """
        @summary Modifies a ranking service.
        
        @param request: ModifyRankingSystemRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyRankingSystemResponse
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
            action='ModifyRankingSystem',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-systems/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ModifyRankingSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_ranking_system_with_options_async(
        self,
        instance_id: str,
        name: str,
        request: airec_20201126_models.ModifyRankingSystemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifyRankingSystemResponse:
        """
        @summary Modifies a ranking service.
        
        @param request: ModifyRankingSystemRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyRankingSystemResponse
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
            action='ModifyRankingSystem',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-systems/{OpenApiUtilClient.get_encode_param(name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ModifyRankingSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_ranking_system(
        self,
        instance_id: str,
        name: str,
        request: airec_20201126_models.ModifyRankingSystemRequest,
    ) -> airec_20201126_models.ModifyRankingSystemResponse:
        """
        @summary Modifies a ranking service.
        
        @param request: ModifyRankingSystemRequest
        @return: ModifyRankingSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_ranking_system_with_options(instance_id, name, request, headers, runtime)

    async def modify_ranking_system_async(
        self,
        instance_id: str,
        name: str,
        request: airec_20201126_models.ModifyRankingSystemRequest,
    ) -> airec_20201126_models.ModifyRankingSystemResponse:
        """
        @summary Modifies a ranking service.
        
        @param request: ModifyRankingSystemRequest
        @return: ModifyRankingSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_ranking_system_with_options_async(instance_id, name, request, headers, runtime)

    def modify_rule_with_options(
        self,
        instance_id: str,
        rule_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifyRuleResponse:
        """
        @summary Modifies a rule.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyRuleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyRule',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/rules/{OpenApiUtilClient.get_encode_param(rule_id)}',
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
        """
        @summary Modifies a rule.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyRuleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyRule',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/rules/{OpenApiUtilClient.get_encode_param(rule_id)}',
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

    def modify_rule(
        self,
        instance_id: str,
        rule_id: str,
    ) -> airec_20201126_models.ModifyRuleResponse:
        """
        @summary Modifies a rule.
        
        @return: ModifyRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_rule_with_options(instance_id, rule_id, headers, runtime)

    async def modify_rule_async(
        self,
        instance_id: str,
        rule_id: str,
    ) -> airec_20201126_models.ModifyRuleResponse:
        """
        @summary Modifies a rule.
        
        @return: ModifyRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_rule_with_options_async(instance_id, rule_id, headers, runtime)

    def modify_sample_with_options(
        self,
        instance_id: str,
        sample_id: str,
        request: airec_20201126_models.ModifySampleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifySampleResponse:
        """
        @summary 修改样本配置
        
        @param request: ModifySampleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySampleResponse
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
            action='ModifySample',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/samples/{OpenApiUtilClient.get_encode_param(sample_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ModifySampleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sample_with_options_async(
        self,
        instance_id: str,
        sample_id: str,
        request: airec_20201126_models.ModifySampleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifySampleResponse:
        """
        @summary 修改样本配置
        
        @param request: ModifySampleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySampleResponse
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
            action='ModifySample',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/samples/{OpenApiUtilClient.get_encode_param(sample_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.ModifySampleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sample(
        self,
        instance_id: str,
        sample_id: str,
        request: airec_20201126_models.ModifySampleRequest,
    ) -> airec_20201126_models.ModifySampleResponse:
        """
        @summary 修改样本配置
        
        @param request: ModifySampleRequest
        @return: ModifySampleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_sample_with_options(instance_id, sample_id, request, headers, runtime)

    async def modify_sample_async(
        self,
        instance_id: str,
        sample_id: str,
        request: airec_20201126_models.ModifySampleRequest,
    ) -> airec_20201126_models.ModifySampleResponse:
        """
        @summary 修改样本配置
        
        @param request: ModifySampleRequest
        @return: ModifySampleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_sample_with_options_async(instance_id, sample_id, request, headers, runtime)

    def modify_scene_with_options(
        self,
        instance_id: str,
        scene_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ModifySceneResponse:
        """
        @summary Modifies the information about a scene.
        
        @description We recommend that you do not call an API operation to manage scenes. We recommend that you go to the Scenario Building page in the Artificial Intelligence Recommendation (AIRec) console to manage scenes.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySceneResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyScene',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}',
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
        """
        @summary Modifies the information about a scene.
        
        @description We recommend that you do not call an API operation to manage scenes. We recommend that you go to the Scenario Building page in the Artificial Intelligence Recommendation (AIRec) console to manage scenes.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySceneResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyScene',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}',
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

    def modify_scene(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.ModifySceneResponse:
        """
        @summary Modifies the information about a scene.
        
        @description We recommend that you do not call an API operation to manage scenes. We recommend that you go to the Scenario Building page in the Artificial Intelligence Recommendation (AIRec) console to manage scenes.
        
        @return: ModifySceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_scene_with_options(instance_id, scene_id, headers, runtime)

    async def modify_scene_async(
        self,
        instance_id: str,
        scene_id: str,
    ) -> airec_20201126_models.ModifySceneResponse:
        """
        @summary Modifies the information about a scene.
        
        @description We recommend that you do not call an API operation to manage scenes. We recommend that you go to the Scenario Building page in the Artificial Intelligence Recommendation (AIRec) console to manage scenes.
        
        @return: ModifySceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_scene_with_options_async(instance_id, scene_id, headers, runtime)

    def offline_filtering_algorithm_with_options(
        self,
        instance_id: str,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.OfflineFilteringAlgorithmResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OfflineFilteringAlgorithmResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='OfflineFilteringAlgorithm',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/filtering-algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}/actions/offline',
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
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OfflineFilteringAlgorithmResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='OfflineFilteringAlgorithm',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/filtering-algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}/actions/offline',
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

    def offline_filtering_algorithm(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.OfflineFilteringAlgorithmResponse:
        """
        @return: OfflineFilteringAlgorithmResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.offline_filtering_algorithm_with_options(instance_id, algorithm_id, headers, runtime)

    async def offline_filtering_algorithm_async(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.OfflineFilteringAlgorithmResponse:
        """
        @return: OfflineFilteringAlgorithmResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.offline_filtering_algorithm_with_options_async(instance_id, algorithm_id, headers, runtime)

    def publish_flow_control_task_with_options(
        self,
        instance_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.PublishFlowControlTaskResponse:
        """
        @summary 发布流调任务接口
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishFlowControlTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PublishFlowControlTask',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/flowControlTasks/{OpenApiUtilClient.get_encode_param(task_id)}/actions/publish',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.PublishFlowControlTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_flow_control_task_with_options_async(
        self,
        instance_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.PublishFlowControlTaskResponse:
        """
        @summary 发布流调任务接口
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishFlowControlTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PublishFlowControlTask',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/flowControlTasks/{OpenApiUtilClient.get_encode_param(task_id)}/actions/publish',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.PublishFlowControlTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_flow_control_task(
        self,
        instance_id: str,
        task_id: str,
    ) -> airec_20201126_models.PublishFlowControlTaskResponse:
        """
        @summary 发布流调任务接口
        
        @return: PublishFlowControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.publish_flow_control_task_with_options(instance_id, task_id, headers, runtime)

    async def publish_flow_control_task_async(
        self,
        instance_id: str,
        task_id: str,
    ) -> airec_20201126_models.PublishFlowControlTaskResponse:
        """
        @summary 发布流调任务接口
        
        @return: PublishFlowControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.publish_flow_control_task_with_options_async(instance_id, task_id, headers, runtime)

    def publish_rule_with_options(
        self,
        rule_id: str,
        instance_id: str,
        request: airec_20201126_models.PublishRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.PublishRuleResponse:
        """
        @summary Publishes a rule.
        
        @param request: PublishRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishRuleResponse
        """
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
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/rules/{OpenApiUtilClient.get_encode_param(rule_id)}/actions/publish',
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
        """
        @summary Publishes a rule.
        
        @param request: PublishRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishRuleResponse
        """
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
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/rules/{OpenApiUtilClient.get_encode_param(rule_id)}/actions/publish',
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

    def publish_rule(
        self,
        rule_id: str,
        instance_id: str,
        request: airec_20201126_models.PublishRuleRequest,
    ) -> airec_20201126_models.PublishRuleResponse:
        """
        @summary Publishes a rule.
        
        @param request: PublishRuleRequest
        @return: PublishRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.publish_rule_with_options(rule_id, instance_id, request, headers, runtime)

    async def publish_rule_async(
        self,
        rule_id: str,
        instance_id: str,
        request: airec_20201126_models.PublishRuleRequest,
    ) -> airec_20201126_models.PublishRuleResponse:
        """
        @summary Publishes a rule.
        
        @param request: PublishRuleRequest
        @return: PublishRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.publish_rule_with_options_async(rule_id, instance_id, request, headers, runtime)

    def push_cold_start_document_with_options(
        self,
        instance_id: str,
        table_name: str,
        request: airec_20201126_models.PushColdStartDocumentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.PushColdStartDocumentResponse:
        """
        @summary 该接口用于向指定冷启动实例指定表推送文档
        
        @param request: PushColdStartDocumentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushColdStartDocumentResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='PushColdStartDocument',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/cold-start/{OpenApiUtilClient.get_encode_param(instance_id)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}/actions/bulk',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.PushColdStartDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_cold_start_document_with_options_async(
        self,
        instance_id: str,
        table_name: str,
        request: airec_20201126_models.PushColdStartDocumentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.PushColdStartDocumentResponse:
        """
        @summary 该接口用于向指定冷启动实例指定表推送文档
        
        @param request: PushColdStartDocumentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushColdStartDocumentResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='PushColdStartDocument',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/cold-start/{OpenApiUtilClient.get_encode_param(instance_id)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}/actions/bulk',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.PushColdStartDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_cold_start_document(
        self,
        instance_id: str,
        table_name: str,
        request: airec_20201126_models.PushColdStartDocumentRequest,
    ) -> airec_20201126_models.PushColdStartDocumentResponse:
        """
        @summary 该接口用于向指定冷启动实例指定表推送文档
        
        @param request: PushColdStartDocumentRequest
        @return: PushColdStartDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_cold_start_document_with_options(instance_id, table_name, request, headers, runtime)

    async def push_cold_start_document_async(
        self,
        instance_id: str,
        table_name: str,
        request: airec_20201126_models.PushColdStartDocumentRequest,
    ) -> airec_20201126_models.PushColdStartDocumentResponse:
        """
        @summary 该接口用于向指定冷启动实例指定表推送文档
        
        @param request: PushColdStartDocumentRequest
        @return: PushColdStartDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.push_cold_start_document_with_options_async(instance_id, table_name, request, headers, runtime)

    def push_document_with_options(
        self,
        instance_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.PushDocumentResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushDocumentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PushDocument',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}/actions/bulk',
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
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushDocumentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PushDocument',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}/actions/bulk',
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

    def push_document(
        self,
        instance_id: str,
        table_name: str,
    ) -> airec_20201126_models.PushDocumentResponse:
        """
        @return: PushDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_document_with_options(instance_id, table_name, headers, runtime)

    async def push_document_async(
        self,
        instance_id: str,
        table_name: str,
    ) -> airec_20201126_models.PushDocumentResponse:
        """
        @return: PushDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.push_document_with_options_async(instance_id, table_name, headers, runtime)

    def push_intervention_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.PushInterventionResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushInterventionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PushIntervention',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/actions/intervene',
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
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushInterventionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PushIntervention',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/actions/intervene',
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

    def push_intervention(
        self,
        instance_id: str,
    ) -> airec_20201126_models.PushInterventionResponse:
        """
        @return: PushInterventionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_intervention_with_options(instance_id, headers, runtime)

    async def push_intervention_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.PushInterventionResponse:
        """
        @return: PushInterventionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.push_intervention_with_options_async(instance_id, headers, runtime)

    def query_data_message_with_options(
        self,
        instance_id: str,
        table: str,
        request: airec_20201126_models.QueryDataMessageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.QueryDataMessageResponse:
        """
        @param request: QueryDataMessageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDataMessageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bhv_type):
            query['bhvType'] = request.bhv_type
        if not UtilClient.is_unset(request.cmd_type):
            query['cmdType'] = request.cmd_type
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.imei):
            query['imei'] = request.imei
        if not UtilClient.is_unset(request.item_id):
            query['itemId'] = request.item_id
        if not UtilClient.is_unset(request.item_type):
            query['itemType'] = request.item_type
        if not UtilClient.is_unset(request.message_source):
            query['messageSource'] = request.message_source
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.scene_id):
            query['sceneId'] = request.scene_id
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.trace_id):
            query['traceId'] = request.trace_id
        if not UtilClient.is_unset(request.user_id):
            query['userId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            query['userType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDataMessage',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tables/{OpenApiUtilClient.get_encode_param(table)}/data-message',
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
        """
        @param request: QueryDataMessageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDataMessageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bhv_type):
            query['bhvType'] = request.bhv_type
        if not UtilClient.is_unset(request.cmd_type):
            query['cmdType'] = request.cmd_type
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.imei):
            query['imei'] = request.imei
        if not UtilClient.is_unset(request.item_id):
            query['itemId'] = request.item_id
        if not UtilClient.is_unset(request.item_type):
            query['itemType'] = request.item_type
        if not UtilClient.is_unset(request.message_source):
            query['messageSource'] = request.message_source
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.scene_id):
            query['sceneId'] = request.scene_id
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.trace_id):
            query['traceId'] = request.trace_id
        if not UtilClient.is_unset(request.user_id):
            query['userId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            query['userType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDataMessage',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tables/{OpenApiUtilClient.get_encode_param(table)}/data-message',
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

    def query_data_message(
        self,
        instance_id: str,
        table: str,
        request: airec_20201126_models.QueryDataMessageRequest,
    ) -> airec_20201126_models.QueryDataMessageResponse:
        """
        @param request: QueryDataMessageRequest
        @return: QueryDataMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_data_message_with_options(instance_id, table, request, headers, runtime)

    async def query_data_message_async(
        self,
        instance_id: str,
        table: str,
        request: airec_20201126_models.QueryDataMessageRequest,
    ) -> airec_20201126_models.QueryDataMessageResponse:
        """
        @param request: QueryDataMessageRequest
        @return: QueryDataMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_data_message_with_options_async(instance_id, table, request, headers, runtime)

    def query_data_message_statistics_with_options(
        self,
        instance_id: str,
        table: str,
        request: airec_20201126_models.QueryDataMessageStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.QueryDataMessageStatisticsResponse:
        """
        @summary Queries statistics on update messages in a data table of an instance.
        
        @description You can call this API operation to query statistics on update messages in a specified data table of a specified instance.
        
        @param request: QueryDataMessageStatisticsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDataMessageStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bhv_type):
            query['bhvType'] = request.bhv_type
        if not UtilClient.is_unset(request.cmd_type):
            query['cmdType'] = request.cmd_type
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.imei):
            query['imei'] = request.imei
        if not UtilClient.is_unset(request.item_id):
            query['itemId'] = request.item_id
        if not UtilClient.is_unset(request.item_type):
            query['itemType'] = request.item_type
        if not UtilClient.is_unset(request.message_source):
            query['messageSource'] = request.message_source
        if not UtilClient.is_unset(request.scene_id):
            query['sceneId'] = request.scene_id
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.trace_id):
            query['traceId'] = request.trace_id
        if not UtilClient.is_unset(request.user_id):
            query['userId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            query['userType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDataMessageStatistics',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tables/{OpenApiUtilClient.get_encode_param(table)}/data-message-statistics',
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
        """
        @summary Queries statistics on update messages in a data table of an instance.
        
        @description You can call this API operation to query statistics on update messages in a specified data table of a specified instance.
        
        @param request: QueryDataMessageStatisticsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDataMessageStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bhv_type):
            query['bhvType'] = request.bhv_type
        if not UtilClient.is_unset(request.cmd_type):
            query['cmdType'] = request.cmd_type
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.imei):
            query['imei'] = request.imei
        if not UtilClient.is_unset(request.item_id):
            query['itemId'] = request.item_id
        if not UtilClient.is_unset(request.item_type):
            query['itemType'] = request.item_type
        if not UtilClient.is_unset(request.message_source):
            query['messageSource'] = request.message_source
        if not UtilClient.is_unset(request.scene_id):
            query['sceneId'] = request.scene_id
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.trace_id):
            query['traceId'] = request.trace_id
        if not UtilClient.is_unset(request.user_id):
            query['userId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            query['userType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDataMessageStatistics',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tables/{OpenApiUtilClient.get_encode_param(table)}/data-message-statistics',
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

    def query_data_message_statistics(
        self,
        instance_id: str,
        table: str,
        request: airec_20201126_models.QueryDataMessageStatisticsRequest,
    ) -> airec_20201126_models.QueryDataMessageStatisticsResponse:
        """
        @summary Queries statistics on update messages in a data table of an instance.
        
        @description You can call this API operation to query statistics on update messages in a specified data table of a specified instance.
        
        @param request: QueryDataMessageStatisticsRequest
        @return: QueryDataMessageStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_data_message_statistics_with_options(instance_id, table, request, headers, runtime)

    async def query_data_message_statistics_async(
        self,
        instance_id: str,
        table: str,
        request: airec_20201126_models.QueryDataMessageStatisticsRequest,
    ) -> airec_20201126_models.QueryDataMessageStatisticsResponse:
        """
        @summary Queries statistics on update messages in a data table of an instance.
        
        @description You can call this API operation to query statistics on update messages in a specified data table of a specified instance.
        
        @param request: QueryDataMessageStatisticsRequest
        @return: QueryDataMessageStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_data_message_statistics_with_options_async(instance_id, table, request, headers, runtime)

    def query_exception_history_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.QueryExceptionHistoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.QueryExceptionHistoryResponse:
        """
        @param request: QueryExceptionHistoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryExceptionHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
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
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sync-reports/exception-history',
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
        """
        @param request: QueryExceptionHistoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryExceptionHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
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
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sync-reports/exception-history',
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

    def query_exception_history(
        self,
        instance_id: str,
        request: airec_20201126_models.QueryExceptionHistoryRequest,
    ) -> airec_20201126_models.QueryExceptionHistoryResponse:
        """
        @param request: QueryExceptionHistoryRequest
        @return: QueryExceptionHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_exception_history_with_options(instance_id, request, headers, runtime)

    async def query_exception_history_async(
        self,
        instance_id: str,
        request: airec_20201126_models.QueryExceptionHistoryRequest,
    ) -> airec_20201126_models.QueryExceptionHistoryResponse:
        """
        @param request: QueryExceptionHistoryRequest
        @return: QueryExceptionHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_exception_history_with_options_async(instance_id, request, headers, runtime)

    def query_raw_data_with_options(
        self,
        instance_id: str,
        table: str,
        request: airec_20201126_models.QueryRawDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.QueryRawDataResponse:
        """
        @summary Queries raw data in a specific data table of an instance by using the primary key.
        
        @description You can call this operation to query raw data in a specific data table of an instance by using the primary key. The returned results need to be confirmed by customers.
        
        @param request: QueryRawDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRawDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.imei):
            query['imei'] = request.imei
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
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tables/{OpenApiUtilClient.get_encode_param(table)}/raw-data',
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
        """
        @summary Queries raw data in a specific data table of an instance by using the primary key.
        
        @description You can call this operation to query raw data in a specific data table of an instance by using the primary key. The returned results need to be confirmed by customers.
        
        @param request: QueryRawDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRawDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.imei):
            query['imei'] = request.imei
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
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tables/{OpenApiUtilClient.get_encode_param(table)}/raw-data',
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

    def query_raw_data(
        self,
        instance_id: str,
        table: str,
        request: airec_20201126_models.QueryRawDataRequest,
    ) -> airec_20201126_models.QueryRawDataResponse:
        """
        @summary Queries raw data in a specific data table of an instance by using the primary key.
        
        @description You can call this operation to query raw data in a specific data table of an instance by using the primary key. The returned results need to be confirmed by customers.
        
        @param request: QueryRawDataRequest
        @return: QueryRawDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_raw_data_with_options(instance_id, table, request, headers, runtime)

    async def query_raw_data_async(
        self,
        instance_id: str,
        table: str,
        request: airec_20201126_models.QueryRawDataRequest,
    ) -> airec_20201126_models.QueryRawDataResponse:
        """
        @summary Queries raw data in a specific data table of an instance by using the primary key.
        
        @description You can call this operation to query raw data in a specific data table of an instance by using the primary key. The returned results need to be confirmed by customers.
        
        @param request: QueryRawDataRequest
        @return: QueryRawDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_raw_data_with_options_async(instance_id, table, request, headers, runtime)

    def query_single_aggregation_report_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.QuerySingleAggregationReportResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySingleAggregationReportResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='QuerySingleAggregationReport',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sync-reports/single-aggregation-report',
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
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySingleAggregationReportResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='QuerySingleAggregationReport',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sync-reports/single-aggregation-report',
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

    def query_single_aggregation_report(
        self,
        instance_id: str,
    ) -> airec_20201126_models.QuerySingleAggregationReportResponse:
        """
        @return: QuerySingleAggregationReportResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_single_aggregation_report_with_options(instance_id, headers, runtime)

    async def query_single_aggregation_report_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.QuerySingleAggregationReportResponse:
        """
        @return: QuerySingleAggregationReportResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_single_aggregation_report_with_options_async(instance_id, headers, runtime)

    def query_single_report_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.QuerySingleReportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.QuerySingleReportResponse:
        """
        @summary Queries a single table report. More report types may be supported.
        
        @param request: QuerySingleReportRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySingleReportResponse
        """
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
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sync-reports/single-report',
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
        """
        @summary Queries a single table report. More report types may be supported.
        
        @param request: QuerySingleReportRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySingleReportResponse
        """
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
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sync-reports/single-report',
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

    def query_single_report(
        self,
        instance_id: str,
        request: airec_20201126_models.QuerySingleReportRequest,
    ) -> airec_20201126_models.QuerySingleReportResponse:
        """
        @summary Queries a single table report. More report types may be supported.
        
        @param request: QuerySingleReportRequest
        @return: QuerySingleReportResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_single_report_with_options(instance_id, request, headers, runtime)

    async def query_single_report_async(
        self,
        instance_id: str,
        request: airec_20201126_models.QuerySingleReportRequest,
    ) -> airec_20201126_models.QuerySingleReportResponse:
        """
        @summary Queries a single table report. More report types may be supported.
        
        @param request: QuerySingleReportRequest
        @return: QuerySingleReportResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_single_report_with_options_async(instance_id, request, headers, runtime)

    def query_sync_report_aggregation_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.QuerySyncReportAggregationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.QuerySyncReportAggregationResponse:
        """
        @summary Queries the data overview.
        
        @param request: QuerySyncReportAggregationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySyncReportAggregationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySyncReportAggregation',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sync-reports/aggregation',
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
        """
        @summary Queries the data overview.
        
        @param request: QuerySyncReportAggregationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySyncReportAggregationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySyncReportAggregation',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sync-reports/aggregation',
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

    def query_sync_report_aggregation(
        self,
        instance_id: str,
        request: airec_20201126_models.QuerySyncReportAggregationRequest,
    ) -> airec_20201126_models.QuerySyncReportAggregationResponse:
        """
        @summary Queries the data overview.
        
        @param request: QuerySyncReportAggregationRequest
        @return: QuerySyncReportAggregationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_sync_report_aggregation_with_options(instance_id, request, headers, runtime)

    async def query_sync_report_aggregation_async(
        self,
        instance_id: str,
        request: airec_20201126_models.QuerySyncReportAggregationRequest,
    ) -> airec_20201126_models.QuerySyncReportAggregationResponse:
        """
        @summary Queries the data overview.
        
        @param request: QuerySyncReportAggregationRequest
        @return: QuerySyncReportAggregationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_sync_report_aggregation_with_options_async(instance_id, request, headers, runtime)

    def rebuild_index_with_options(
        self,
        instance_id: str,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.RebuildIndexResponse:
        """
        @summary Rebuilds an index.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebuildIndexResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RebuildIndex',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/filtering-algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}/actions/rebuild',
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
        """
        @summary Rebuilds an index.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebuildIndexResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RebuildIndex',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/filtering-algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}/actions/rebuild',
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

    def rebuild_index(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.RebuildIndexResponse:
        """
        @summary Rebuilds an index.
        
        @return: RebuildIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rebuild_index_with_options(instance_id, algorithm_id, headers, runtime)

    async def rebuild_index_async(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.RebuildIndexResponse:
        """
        @summary Rebuilds an index.
        
        @return: RebuildIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.rebuild_index_with_options_async(instance_id, algorithm_id, headers, runtime)

    def recommend_with_options(
        self,
        instance_id: str,
        request: airec_20201126_models.RecommendRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.RecommendResponse:
        """
        @summary The type of the recommendation service.
        
        @param request: RecommendRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecommendResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['filter'] = request.filter
        if not UtilClient.is_unset(request.imei):
            query['imei'] = request.imei
        if not UtilClient.is_unset(request.ip):
            query['ip'] = request.ip
        if not UtilClient.is_unset(request.items):
            query['items'] = request.items
        if not UtilClient.is_unset(request.rank_open):
            query['rankOpen'] = request.rank_open
        if not UtilClient.is_unset(request.rec_type):
            query['recType'] = request.rec_type
        if not UtilClient.is_unset(request.return_count):
            query['returnCount'] = request.return_count
        if not UtilClient.is_unset(request.scene_id):
            query['sceneId'] = request.scene_id
        if not UtilClient.is_unset(request.service_type):
            query['serviceType'] = request.service_type
        if not UtilClient.is_unset(request.strategy):
            query['strategy'] = request.strategy
        if not UtilClient.is_unset(request.user_id):
            query['userId'] = request.user_id
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
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/actions/recommend',
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
        """
        @summary The type of the recommendation service.
        
        @param request: RecommendRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecommendResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['filter'] = request.filter
        if not UtilClient.is_unset(request.imei):
            query['imei'] = request.imei
        if not UtilClient.is_unset(request.ip):
            query['ip'] = request.ip
        if not UtilClient.is_unset(request.items):
            query['items'] = request.items
        if not UtilClient.is_unset(request.rank_open):
            query['rankOpen'] = request.rank_open
        if not UtilClient.is_unset(request.rec_type):
            query['recType'] = request.rec_type
        if not UtilClient.is_unset(request.return_count):
            query['returnCount'] = request.return_count
        if not UtilClient.is_unset(request.scene_id):
            query['sceneId'] = request.scene_id
        if not UtilClient.is_unset(request.service_type):
            query['serviceType'] = request.service_type
        if not UtilClient.is_unset(request.strategy):
            query['strategy'] = request.strategy
        if not UtilClient.is_unset(request.user_id):
            query['userId'] = request.user_id
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
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/actions/recommend',
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

    def recommend(
        self,
        instance_id: str,
        request: airec_20201126_models.RecommendRequest,
    ) -> airec_20201126_models.RecommendResponse:
        """
        @summary The type of the recommendation service.
        
        @param request: RecommendRequest
        @return: RecommendResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.recommend_with_options(instance_id, request, headers, runtime)

    async def recommend_async(
        self,
        instance_id: str,
        request: airec_20201126_models.RecommendRequest,
    ) -> airec_20201126_models.RecommendResponse:
        """
        @summary The type of the recommendation service.
        
        @param request: RecommendRequest
        @return: RecommendResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.recommend_with_options_async(instance_id, request, headers, runtime)

    def refresh_feature_table_with_options(
        self,
        instance_id: str,
        type: str,
        feature_table_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.RefreshFeatureTableResponse:
        """
        @summary Refreshes a feature table based on the source table in MaxCompute. The refresh policy is subject to data in the source table.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshFeatureTableResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RefreshFeatureTable',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/feature-tables/{OpenApiUtilClient.get_encode_param(type)}/{OpenApiUtilClient.get_encode_param(feature_table_id)}/actions/refresh',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.RefreshFeatureTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_feature_table_with_options_async(
        self,
        instance_id: str,
        type: str,
        feature_table_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.RefreshFeatureTableResponse:
        """
        @summary Refreshes a feature table based on the source table in MaxCompute. The refresh policy is subject to data in the source table.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshFeatureTableResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RefreshFeatureTable',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/feature-tables/{OpenApiUtilClient.get_encode_param(type)}/{OpenApiUtilClient.get_encode_param(feature_table_id)}/actions/refresh',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.RefreshFeatureTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_feature_table(
        self,
        instance_id: str,
        type: str,
        feature_table_id: str,
    ) -> airec_20201126_models.RefreshFeatureTableResponse:
        """
        @summary Refreshes a feature table based on the source table in MaxCompute. The refresh policy is subject to data in the source table.
        
        @return: RefreshFeatureTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.refresh_feature_table_with_options(instance_id, type, feature_table_id, headers, runtime)

    async def refresh_feature_table_async(
        self,
        instance_id: str,
        type: str,
        feature_table_id: str,
    ) -> airec_20201126_models.RefreshFeatureTableResponse:
        """
        @summary Refreshes a feature table based on the source table in MaxCompute. The refresh policy is subject to data in the source table.
        
        @return: RefreshFeatureTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.refresh_feature_table_with_options_async(instance_id, type, feature_table_id, headers, runtime)

    def rollback_ranking_system_with_options(
        self,
        instance_id: str,
        name: str,
        request: airec_20201126_models.RollbackRankingSystemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.RollbackRankingSystemResponse:
        """
        @summary 回滚某个排序服务
        
        @param request: RollbackRankingSystemRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RollbackRankingSystemResponse
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
            action='RollbackRankingSystem',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-systems/{OpenApiUtilClient.get_encode_param(name)}/actions/rollback',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.RollbackRankingSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_ranking_system_with_options_async(
        self,
        instance_id: str,
        name: str,
        request: airec_20201126_models.RollbackRankingSystemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.RollbackRankingSystemResponse:
        """
        @summary 回滚某个排序服务
        
        @param request: RollbackRankingSystemRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RollbackRankingSystemResponse
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
            action='RollbackRankingSystem',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-systems/{OpenApiUtilClient.get_encode_param(name)}/actions/rollback',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.RollbackRankingSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_ranking_system(
        self,
        instance_id: str,
        name: str,
        request: airec_20201126_models.RollbackRankingSystemRequest,
    ) -> airec_20201126_models.RollbackRankingSystemResponse:
        """
        @summary 回滚某个排序服务
        
        @param request: RollbackRankingSystemRequest
        @return: RollbackRankingSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rollback_ranking_system_with_options(instance_id, name, request, headers, runtime)

    async def rollback_ranking_system_async(
        self,
        instance_id: str,
        name: str,
        request: airec_20201126_models.RollbackRankingSystemRequest,
    ) -> airec_20201126_models.RollbackRankingSystemResponse:
        """
        @summary 回滚某个排序服务
        
        @param request: RollbackRankingSystemRequest
        @return: RollbackRankingSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.rollback_ranking_system_with_options_async(instance_id, name, request, headers, runtime)

    def run_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.RunInstanceResponse:
        """
        @summary Runs an instance to start a full data import task.
        
        @description You can call this API operation to run an instance to start a full data import task. After you call this API operation, the system creates a dataset. Then, the system imports all data from your data sources into the dataset for data training.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RunInstance',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/actions/import',
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
        """
        @summary Runs an instance to start a full data import task.
        
        @description You can call this API operation to run an instance to start a full data import task. After you call this API operation, the system creates a dataset. Then, the system imports all data from your data sources into the dataset for data training.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RunInstance',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/actions/import',
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

    def run_instance(
        self,
        instance_id: str,
    ) -> airec_20201126_models.RunInstanceResponse:
        """
        @summary Runs an instance to start a full data import task.
        
        @description You can call this API operation to run an instance to start a full data import task. After you call this API operation, the system creates a dataset. Then, the system imports all data from your data sources into the dataset for data training.
        
        @return: RunInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_instance_with_options(instance_id, headers, runtime)

    async def run_instance_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.RunInstanceResponse:
        """
        @summary Runs an instance to start a full data import task.
        
        @description You can call this API operation to run an instance to start a full data import task. After you call this API operation, the system creates a dataset. Then, the system imports all data from your data sources into the dataset for data training.
        
        @return: RunInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_instance_with_options_async(instance_id, headers, runtime)

    def run_ranking_model_template_with_options(
        self,
        instance_id: str,
        template_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.RunRankingModelTemplateResponse:
        """
        @summary 启动模型训练
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunRankingModelTemplateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RunRankingModelTemplate',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-model-templates/{OpenApiUtilClient.get_encode_param(template_id)}/actions/run',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.RunRankingModelTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_ranking_model_template_with_options_async(
        self,
        instance_id: str,
        template_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.RunRankingModelTemplateResponse:
        """
        @summary 启动模型训练
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunRankingModelTemplateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RunRankingModelTemplate',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-model-templates/{OpenApiUtilClient.get_encode_param(template_id)}/actions/run',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.RunRankingModelTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_ranking_model_template(
        self,
        instance_id: str,
        template_id: str,
    ) -> airec_20201126_models.RunRankingModelTemplateResponse:
        """
        @summary 启动模型训练
        
        @return: RunRankingModelTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_ranking_model_template_with_options(instance_id, template_id, headers, runtime)

    async def run_ranking_model_template_async(
        self,
        instance_id: str,
        template_id: str,
    ) -> airec_20201126_models.RunRankingModelTemplateResponse:
        """
        @summary 启动模型训练
        
        @return: RunRankingModelTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_ranking_model_template_with_options_async(instance_id, template_id, headers, runtime)

    def run_sample_format_config_with_options(
        self,
        instance_id: str,
        sample_id: str,
        request: airec_20201126_models.RunSampleFormatConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.RunSampleFormatConfigResponse:
        """
        @summary Triggers sample formatting configurations.
        
        @param request: RunSampleFormatConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunSampleFormatConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mode):
            query['mode'] = request.mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunSampleFormatConfig',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/samples/{OpenApiUtilClient.get_encode_param(sample_id)}/format-configs/actions/run',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.RunSampleFormatConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_sample_format_config_with_options_async(
        self,
        instance_id: str,
        sample_id: str,
        request: airec_20201126_models.RunSampleFormatConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.RunSampleFormatConfigResponse:
        """
        @summary Triggers sample formatting configurations.
        
        @param request: RunSampleFormatConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunSampleFormatConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mode):
            query['mode'] = request.mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunSampleFormatConfig',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/samples/{OpenApiUtilClient.get_encode_param(sample_id)}/format-configs/actions/run',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.RunSampleFormatConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_sample_format_config(
        self,
        instance_id: str,
        sample_id: str,
        request: airec_20201126_models.RunSampleFormatConfigRequest,
    ) -> airec_20201126_models.RunSampleFormatConfigResponse:
        """
        @summary Triggers sample formatting configurations.
        
        @param request: RunSampleFormatConfigRequest
        @return: RunSampleFormatConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_sample_format_config_with_options(instance_id, sample_id, request, headers, runtime)

    async def run_sample_format_config_async(
        self,
        instance_id: str,
        sample_id: str,
        request: airec_20201126_models.RunSampleFormatConfigRequest,
    ) -> airec_20201126_models.RunSampleFormatConfigResponse:
        """
        @summary Triggers sample formatting configurations.
        
        @param request: RunSampleFormatConfigRequest
        @return: RunSampleFormatConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_sample_format_config_with_options_async(instance_id, sample_id, request, headers, runtime)

    def stop_data_set_with_options(
        self,
        instance_id: str,
        version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.StopDataSetResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDataSetResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopDataSet',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/dataSets/{OpenApiUtilClient.get_encode_param(version_id)}/actions/stop',
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
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDataSetResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopDataSet',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/dataSets/{OpenApiUtilClient.get_encode_param(version_id)}/actions/stop',
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

    def stop_data_set(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20201126_models.StopDataSetResponse:
        """
        @return: StopDataSetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_data_set_with_options(instance_id, version_id, headers, runtime)

    async def stop_data_set_async(
        self,
        instance_id: str,
        version_id: str,
    ) -> airec_20201126_models.StopDataSetResponse:
        """
        @return: StopDataSetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_data_set_with_options_async(instance_id, version_id, headers, runtime)

    def stop_flow_control_task_with_options(
        self,
        instance_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.StopFlowControlTaskResponse:
        """
        @summary 停止流调任务接口
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopFlowControlTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopFlowControlTask',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/flowControlTasks/{OpenApiUtilClient.get_encode_param(task_id)}/actions/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.StopFlowControlTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_flow_control_task_with_options_async(
        self,
        instance_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.StopFlowControlTaskResponse:
        """
        @summary 停止流调任务接口
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopFlowControlTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopFlowControlTask',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/flowControlTasks/{OpenApiUtilClient.get_encode_param(task_id)}/actions/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.StopFlowControlTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_flow_control_task(
        self,
        instance_id: str,
        task_id: str,
    ) -> airec_20201126_models.StopFlowControlTaskResponse:
        """
        @summary 停止流调任务接口
        
        @return: StopFlowControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_flow_control_task_with_options(instance_id, task_id, headers, runtime)

    async def stop_flow_control_task_async(
        self,
        instance_id: str,
        task_id: str,
    ) -> airec_20201126_models.StopFlowControlTaskResponse:
        """
        @summary 停止流调任务接口
        
        @return: StopFlowControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_flow_control_task_with_options_async(instance_id, task_id, headers, runtime)

    def un_lock_index_version_with_options(
        self,
        instance_id: str,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.UnLockIndexVersionResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnLockIndexVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UnLockIndexVersion',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/filtering-algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}/actions/unlock',
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
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnLockIndexVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UnLockIndexVersion',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/filtering-algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}/actions/unlock',
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

    def un_lock_index_version(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.UnLockIndexVersionResponse:
        """
        @return: UnLockIndexVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.un_lock_index_version_with_options(instance_id, algorithm_id, headers, runtime)

    async def un_lock_index_version_async(
        self,
        instance_id: str,
        algorithm_id: str,
    ) -> airec_20201126_models.UnLockIndexVersionResponse:
        """
        @return: UnLockIndexVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.un_lock_index_version_with_options_async(instance_id, algorithm_id, headers, runtime)

    def update_experiment_basic_info_with_options(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.UpdateExperimentBasicInfoResponse:
        """
        @summary Updates the basic information about an experiment.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExperimentBasicInfoResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateExperimentBasicInfo',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}/basic',
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
        """
        @summary Updates the basic information about an experiment.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExperimentBasicInfoResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateExperimentBasicInfo',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}/basic',
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

    def update_experiment_basic_info(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
    ) -> airec_20201126_models.UpdateExperimentBasicInfoResponse:
        """
        @summary Updates the basic information about an experiment.
        
        @return: UpdateExperimentBasicInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_experiment_basic_info_with_options(instance_id, scene_id, experiment_id, headers, runtime)

    async def update_experiment_basic_info_async(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
    ) -> airec_20201126_models.UpdateExperimentBasicInfoResponse:
        """
        @summary Updates the basic information about an experiment.
        
        @return: UpdateExperimentBasicInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_experiment_basic_info_with_options_async(instance_id, scene_id, experiment_id, headers, runtime)

    def update_experiment_config_with_options(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.UpdateExperimentConfigResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExperimentConfigResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateExperimentConfig',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}/config',
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
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExperimentConfigResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateExperimentConfig',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}/config',
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

    def update_experiment_config(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
    ) -> airec_20201126_models.UpdateExperimentConfigResponse:
        """
        @return: UpdateExperimentConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_experiment_config_with_options(instance_id, scene_id, experiment_id, headers, runtime)

    async def update_experiment_config_async(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
    ) -> airec_20201126_models.UpdateExperimentConfigResponse:
        """
        @return: UpdateExperimentConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_experiment_config_with_options_async(instance_id, scene_id, experiment_id, headers, runtime)

    def update_experiment_status_with_options(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.UpdateExperimentStatusResponse:
        """
        @summary Updates the state of an experiment.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExperimentStatusResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateExperimentStatus',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}/status',
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
        """
        @summary Updates the state of an experiment.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExperimentStatusResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateExperimentStatus',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}/status',
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

    def update_experiment_status(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
    ) -> airec_20201126_models.UpdateExperimentStatusResponse:
        """
        @summary Updates the state of an experiment.
        
        @return: UpdateExperimentStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_experiment_status_with_options(instance_id, scene_id, experiment_id, headers, runtime)

    async def update_experiment_status_async(
        self,
        instance_id: str,
        scene_id: str,
        experiment_id: str,
    ) -> airec_20201126_models.UpdateExperimentStatusResponse:
        """
        @summary Updates the state of an experiment.
        
        @return: UpdateExperimentStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_experiment_status_with_options_async(instance_id, scene_id, experiment_id, headers, runtime)

    def upgrade_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.UpgradeInstanceResponse:
        """
        @summary Modifies the quotas of a specified instance.
        
        @description You can call this operation to modify the quotas of a specified instance.
        The limits on the number of users: 1,000,000 to 10,000,000. The limits on the number of items: 1,000,000 to 10,000,000. The limits on the queries per second (QPS) for recommendation requests: 10 to 500.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpgradeInstance',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/actions/upgrade',
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
        """
        @summary Modifies the quotas of a specified instance.
        
        @description You can call this operation to modify the quotas of a specified instance.
        The limits on the number of users: 1,000,000 to 10,000,000. The limits on the number of items: 1,000,000 to 10,000,000. The limits on the queries per second (QPS) for recommendation requests: 10 to 500.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpgradeInstance',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/actions/upgrade',
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

    def upgrade_instance(
        self,
        instance_id: str,
    ) -> airec_20201126_models.UpgradeInstanceResponse:
        """
        @summary Modifies the quotas of a specified instance.
        
        @description You can call this operation to modify the quotas of a specified instance.
        The limits on the number of users: 1,000,000 to 10,000,000. The limits on the number of items: 1,000,000 to 10,000,000. The limits on the queries per second (QPS) for recommendation requests: 10 to 500.
        
        @return: UpgradeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upgrade_instance_with_options(instance_id, headers, runtime)

    async def upgrade_instance_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.UpgradeInstanceResponse:
        """
        @summary Modifies the quotas of a specified instance.
        
        @description You can call this operation to modify the quotas of a specified instance.
        The limits on the number of users: 1,000,000 to 10,000,000. The limits on the number of items: 1,000,000 to 10,000,000. The limits on the queries per second (QPS) for recommendation requests: 10 to 500.
        
        @return: UpgradeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upgrade_instance_with_options_async(instance_id, headers, runtime)

    def validate_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.ValidateInstanceResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ValidateInstance',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/actions/validate',
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
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ValidateInstance',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/actions/validate',
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

    def validate_instance(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ValidateInstanceResponse:
        """
        @return: ValidateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.validate_instance_with_options(instance_id, headers, runtime)

    async def validate_instance_async(
        self,
        instance_id: str,
    ) -> airec_20201126_models.ValidateInstanceResponse:
        """
        @return: ValidateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.validate_instance_with_options_async(instance_id, headers, runtime)

    def verify_ranking_system_with_options(
        self,
        instance_id: str,
        name: str,
        request: airec_20201126_models.VerifyRankingSystemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.VerifyRankingSystemResponse:
        """
        @summary 调试排序服务
        
        @param request: VerifyRankingSystemRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyRankingSystemResponse
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
            action='VerifyRankingSystem',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-systems/{OpenApiUtilClient.get_encode_param(name)}/actions/verify',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.VerifyRankingSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_ranking_system_with_options_async(
        self,
        instance_id: str,
        name: str,
        request: airec_20201126_models.VerifyRankingSystemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> airec_20201126_models.VerifyRankingSystemResponse:
        """
        @summary 调试排序服务
        
        @param request: VerifyRankingSystemRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyRankingSystemResponse
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
            action='VerifyRankingSystem',
            version='2020-11-26',
            protocol='HTTPS',
            pathname=f'/v2/openapi/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/ranking-systems/{OpenApiUtilClient.get_encode_param(name)}/actions/verify',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airec_20201126_models.VerifyRankingSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_ranking_system(
        self,
        instance_id: str,
        name: str,
        request: airec_20201126_models.VerifyRankingSystemRequest,
    ) -> airec_20201126_models.VerifyRankingSystemResponse:
        """
        @summary 调试排序服务
        
        @param request: VerifyRankingSystemRequest
        @return: VerifyRankingSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.verify_ranking_system_with_options(instance_id, name, request, headers, runtime)

    async def verify_ranking_system_async(
        self,
        instance_id: str,
        name: str,
        request: airec_20201126_models.VerifyRankingSystemRequest,
    ) -> airec_20201126_models.VerifyRankingSystemResponse:
        """
        @summary 调试排序服务
        
        @param request: VerifyRankingSystemRequest
        @return: VerifyRankingSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.verify_ranking_system_with_options_async(instance_id, name, request, headers, runtime)
