# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_pairecservice20221213 import models as pai_rec_service_20221213_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('pairecservice', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def backflow_feature_consistency_check_job_data_with_options(
        self,
        request: pai_rec_service_20221213_models.BackflowFeatureConsistencyCheckJobDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.BackflowFeatureConsistencyCheckJobDataResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.feature_consistency_check_job_config_id):
            body['FeatureConsistencyCheckJobConfigId'] = request.feature_consistency_check_job_config_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.item_features):
            body['ItemFeatures'] = request.item_features
        if not UtilClient.is_unset(request.log_item_id):
            body['LogItemId'] = request.log_item_id
        if not UtilClient.is_unset(request.log_request_id):
            body['LogRequestId'] = request.log_request_id
        if not UtilClient.is_unset(request.log_request_time):
            body['LogRequestTime'] = request.log_request_time
        if not UtilClient.is_unset(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not UtilClient.is_unset(request.scene_name):
            body['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.scores):
            body['Scores'] = request.scores
        if not UtilClient.is_unset(request.user_features):
            body['UserFeatures'] = request.user_features
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BackflowFeatureConsistencyCheckJobData',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/featureconsistencycheck/jobs/action/backflowdata',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.BackflowFeatureConsistencyCheckJobDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def backflow_feature_consistency_check_job_data_with_options_async(
        self,
        request: pai_rec_service_20221213_models.BackflowFeatureConsistencyCheckJobDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.BackflowFeatureConsistencyCheckJobDataResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.feature_consistency_check_job_config_id):
            body['FeatureConsistencyCheckJobConfigId'] = request.feature_consistency_check_job_config_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.item_features):
            body['ItemFeatures'] = request.item_features
        if not UtilClient.is_unset(request.log_item_id):
            body['LogItemId'] = request.log_item_id
        if not UtilClient.is_unset(request.log_request_id):
            body['LogRequestId'] = request.log_request_id
        if not UtilClient.is_unset(request.log_request_time):
            body['LogRequestTime'] = request.log_request_time
        if not UtilClient.is_unset(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not UtilClient.is_unset(request.scene_name):
            body['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.scores):
            body['Scores'] = request.scores
        if not UtilClient.is_unset(request.user_features):
            body['UserFeatures'] = request.user_features
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BackflowFeatureConsistencyCheckJobData',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/featureconsistencycheck/jobs/action/backflowdata',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.BackflowFeatureConsistencyCheckJobDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def backflow_feature_consistency_check_job_data(
        self,
        request: pai_rec_service_20221213_models.BackflowFeatureConsistencyCheckJobDataRequest,
    ) -> pai_rec_service_20221213_models.BackflowFeatureConsistencyCheckJobDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.backflow_feature_consistency_check_job_data_with_options(request, headers, runtime)

    async def backflow_feature_consistency_check_job_data_async(
        self,
        request: pai_rec_service_20221213_models.BackflowFeatureConsistencyCheckJobDataRequest,
    ) -> pai_rec_service_20221213_models.BackflowFeatureConsistencyCheckJobDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.backflow_feature_consistency_check_job_data_with_options_async(request, headers, runtime)

    def check_instance_resources_with_options(
        self,
        instance_id: str,
        request: pai_rec_service_20221213_models.CheckInstanceResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CheckInstanceResourcesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckInstanceResources',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/action/checkresources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CheckInstanceResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_instance_resources_with_options_async(
        self,
        instance_id: str,
        request: pai_rec_service_20221213_models.CheckInstanceResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CheckInstanceResourcesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckInstanceResources',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/action/checkresources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CheckInstanceResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_instance_resources(
        self,
        instance_id: str,
        request: pai_rec_service_20221213_models.CheckInstanceResourcesRequest,
    ) -> pai_rec_service_20221213_models.CheckInstanceResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_instance_resources_with_options(instance_id, request, headers, runtime)

    async def check_instance_resources_async(
        self,
        instance_id: str,
        request: pai_rec_service_20221213_models.CheckInstanceResourcesRequest,
    ) -> pai_rec_service_20221213_models.CheckInstanceResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.check_instance_resources_with_options_async(instance_id, request, headers, runtime)

    def clone_experiment_with_options(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.CloneExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CloneExperimentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloneExperiment',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}/action/clone',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CloneExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_experiment_with_options_async(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.CloneExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CloneExperimentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloneExperiment',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}/action/clone',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CloneExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_experiment(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.CloneExperimentRequest,
    ) -> pai_rec_service_20221213_models.CloneExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clone_experiment_with_options(experiment_id, request, headers, runtime)

    async def clone_experiment_async(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.CloneExperimentRequest,
    ) -> pai_rec_service_20221213_models.CloneExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.clone_experiment_with_options_async(experiment_id, request, headers, runtime)

    def clone_experiment_group_with_options(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.CloneExperimentGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CloneExperimentGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.layer_id):
            body['LayerId'] = request.layer_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloneExperimentGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experimentgroups/{OpenApiUtilClient.get_encode_param(experiment_group_id)}/action/clone',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CloneExperimentGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_experiment_group_with_options_async(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.CloneExperimentGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CloneExperimentGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.layer_id):
            body['LayerId'] = request.layer_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloneExperimentGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experimentgroups/{OpenApiUtilClient.get_encode_param(experiment_group_id)}/action/clone',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CloneExperimentGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_experiment_group(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.CloneExperimentGroupRequest,
    ) -> pai_rec_service_20221213_models.CloneExperimentGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clone_experiment_group_with_options(experiment_group_id, request, headers, runtime)

    async def clone_experiment_group_async(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.CloneExperimentGroupRequest,
    ) -> pai_rec_service_20221213_models.CloneExperimentGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.clone_experiment_group_with_options_async(experiment_group_id, request, headers, runtime)

    def clone_feature_consistency_check_job_config_with_options(
        self,
        source_feature_consistency_check_job_config_id: str,
        request: pai_rec_service_20221213_models.CloneFeatureConsistencyCheckJobConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CloneFeatureConsistencyCheckJobConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloneFeatureConsistencyCheckJobConfig',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/featureconsistencycheck/jobconfigs/{OpenApiUtilClient.get_encode_param(source_feature_consistency_check_job_config_id)}/action/clone',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CloneFeatureConsistencyCheckJobConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_feature_consistency_check_job_config_with_options_async(
        self,
        source_feature_consistency_check_job_config_id: str,
        request: pai_rec_service_20221213_models.CloneFeatureConsistencyCheckJobConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CloneFeatureConsistencyCheckJobConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloneFeatureConsistencyCheckJobConfig',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/featureconsistencycheck/jobconfigs/{OpenApiUtilClient.get_encode_param(source_feature_consistency_check_job_config_id)}/action/clone',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CloneFeatureConsistencyCheckJobConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_feature_consistency_check_job_config(
        self,
        source_feature_consistency_check_job_config_id: str,
        request: pai_rec_service_20221213_models.CloneFeatureConsistencyCheckJobConfigRequest,
    ) -> pai_rec_service_20221213_models.CloneFeatureConsistencyCheckJobConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clone_feature_consistency_check_job_config_with_options(source_feature_consistency_check_job_config_id, request, headers, runtime)

    async def clone_feature_consistency_check_job_config_async(
        self,
        source_feature_consistency_check_job_config_id: str,
        request: pai_rec_service_20221213_models.CloneFeatureConsistencyCheckJobConfigRequest,
    ) -> pai_rec_service_20221213_models.CloneFeatureConsistencyCheckJobConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.clone_feature_consistency_check_job_config_with_options_async(source_feature_consistency_check_job_config_id, request, headers, runtime)

    def clone_laboratory_with_options(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.CloneLaboratoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CloneLaboratoryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.clone_experiment_group):
            body['CloneExperimentGroup'] = request.clone_experiment_group
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloneLaboratory',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/laboratories/{OpenApiUtilClient.get_encode_param(laboratory_id)}/action/clone',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CloneLaboratoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_laboratory_with_options_async(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.CloneLaboratoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CloneLaboratoryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.clone_experiment_group):
            body['CloneExperimentGroup'] = request.clone_experiment_group
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloneLaboratory',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/laboratories/{OpenApiUtilClient.get_encode_param(laboratory_id)}/action/clone',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CloneLaboratoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_laboratory(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.CloneLaboratoryRequest,
    ) -> pai_rec_service_20221213_models.CloneLaboratoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clone_laboratory_with_options(laboratory_id, request, headers, runtime)

    async def clone_laboratory_async(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.CloneLaboratoryRequest,
    ) -> pai_rec_service_20221213_models.CloneLaboratoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.clone_laboratory_with_options_async(laboratory_id, request, headers, runtime)

    def create_abmetric_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateABMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateABMetricResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.definition):
            body['Definition'] = request.definition
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.left_metric_id):
            body['LeftMetricId'] = request.left_metric_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.realtime):
            body['Realtime'] = request.realtime
        if not UtilClient.is_unset(request.result_resource_id):
            body['ResultResourceId'] = request.result_resource_id
        if not UtilClient.is_unset(request.right_metric_id):
            body['RightMetricId'] = request.right_metric_id
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.statistics_cycle):
            body['StatisticsCycle'] = request.statistics_cycle
        if not UtilClient.is_unset(request.table_meta_id):
            body['TableMetaId'] = request.table_meta_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateABMetric',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/abmetrics',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateABMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_abmetric_with_options_async(
        self,
        request: pai_rec_service_20221213_models.CreateABMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateABMetricResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.definition):
            body['Definition'] = request.definition
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.left_metric_id):
            body['LeftMetricId'] = request.left_metric_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.realtime):
            body['Realtime'] = request.realtime
        if not UtilClient.is_unset(request.result_resource_id):
            body['ResultResourceId'] = request.result_resource_id
        if not UtilClient.is_unset(request.right_metric_id):
            body['RightMetricId'] = request.right_metric_id
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.statistics_cycle):
            body['StatisticsCycle'] = request.statistics_cycle
        if not UtilClient.is_unset(request.table_meta_id):
            body['TableMetaId'] = request.table_meta_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateABMetric',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/abmetrics',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateABMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_abmetric(
        self,
        request: pai_rec_service_20221213_models.CreateABMetricRequest,
    ) -> pai_rec_service_20221213_models.CreateABMetricResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_abmetric_with_options(request, headers, runtime)

    async def create_abmetric_async(
        self,
        request: pai_rec_service_20221213_models.CreateABMetricRequest,
    ) -> pai_rec_service_20221213_models.CreateABMetricResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_abmetric_with_options_async(request, headers, runtime)

    def create_abmetric_group_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateABMetricGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateABMetricGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.abmetric_ids):
            body['ABMetricIds'] = request.abmetric_ids
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.realtime):
            body['Realtime'] = request.realtime
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateABMetricGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/abmetricgroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateABMetricGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_abmetric_group_with_options_async(
        self,
        request: pai_rec_service_20221213_models.CreateABMetricGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateABMetricGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.abmetric_ids):
            body['ABMetricIds'] = request.abmetric_ids
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.realtime):
            body['Realtime'] = request.realtime
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateABMetricGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/abmetricgroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateABMetricGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_abmetric_group(
        self,
        request: pai_rec_service_20221213_models.CreateABMetricGroupRequest,
    ) -> pai_rec_service_20221213_models.CreateABMetricGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_abmetric_group_with_options(request, headers, runtime)

    async def create_abmetric_group_async(
        self,
        request: pai_rec_service_20221213_models.CreateABMetricGroupRequest,
    ) -> pai_rec_service_20221213_models.CreateABMetricGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_abmetric_group_with_options_async(request, headers, runtime)

    def create_calculation_jobs_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateCalculationJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateCalculationJobsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.abmetric_ids):
            body['ABMetricIds'] = request.abmetric_ids
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCalculationJobs',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/batch/calculationjobs/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateCalculationJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_calculation_jobs_with_options_async(
        self,
        request: pai_rec_service_20221213_models.CreateCalculationJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateCalculationJobsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.abmetric_ids):
            body['ABMetricIds'] = request.abmetric_ids
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCalculationJobs',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/batch/calculationjobs/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateCalculationJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_calculation_jobs(
        self,
        request: pai_rec_service_20221213_models.CreateCalculationJobsRequest,
    ) -> pai_rec_service_20221213_models.CreateCalculationJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_calculation_jobs_with_options(request, headers, runtime)

    async def create_calculation_jobs_async(
        self,
        request: pai_rec_service_20221213_models.CreateCalculationJobsRequest,
    ) -> pai_rec_service_20221213_models.CreateCalculationJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_calculation_jobs_with_options_async(request, headers, runtime)

    def create_crowd_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateCrowdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateCrowdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCrowd',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/crowds',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateCrowdResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_crowd_with_options_async(
        self,
        request: pai_rec_service_20221213_models.CreateCrowdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateCrowdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCrowd',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/crowds',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateCrowdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_crowd(
        self,
        request: pai_rec_service_20221213_models.CreateCrowdRequest,
    ) -> pai_rec_service_20221213_models.CreateCrowdResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_crowd_with_options(request, headers, runtime)

    async def create_crowd_async(
        self,
        request: pai_rec_service_20221213_models.CreateCrowdRequest,
    ) -> pai_rec_service_20221213_models.CreateCrowdResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_crowd_with_options_async(request, headers, runtime)

    def create_experiment_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateExperimentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.experiment_group_id):
            body['ExperimentGroupId'] = request.experiment_group_id
        if not UtilClient.is_unset(request.flow_percent):
            body['FlowPercent'] = request.flow_percent
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateExperiment',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_experiment_with_options_async(
        self,
        request: pai_rec_service_20221213_models.CreateExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateExperimentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.experiment_group_id):
            body['ExperimentGroupId'] = request.experiment_group_id
        if not UtilClient.is_unset(request.flow_percent):
            body['FlowPercent'] = request.flow_percent
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateExperiment',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_experiment(
        self,
        request: pai_rec_service_20221213_models.CreateExperimentRequest,
    ) -> pai_rec_service_20221213_models.CreateExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_experiment_with_options(request, headers, runtime)

    async def create_experiment_async(
        self,
        request: pai_rec_service_20221213_models.CreateExperimentRequest,
    ) -> pai_rec_service_20221213_models.CreateExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_experiment_with_options_async(request, headers, runtime)

    def create_experiment_group_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateExperimentGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateExperimentGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.crowd_id):
            body['CrowdId'] = request.crowd_id
        if not UtilClient.is_unset(request.crowd_target_type):
            body['CrowdTargetType'] = request.crowd_target_type
        if not UtilClient.is_unset(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.distribution_time_duration):
            body['DistributionTimeDuration'] = request.distribution_time_duration
        if not UtilClient.is_unset(request.distribution_type):
            body['DistributionType'] = request.distribution_type
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.layer_id):
            body['LayerId'] = request.layer_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.need_aa):
            body['NeedAA'] = request.need_aa
        if not UtilClient.is_unset(request.random_flow):
            body['RandomFlow'] = request.random_flow
        if not UtilClient.is_unset(request.reserved_buckets):
            body['ReservedBuckets'] = request.reserved_buckets
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateExperimentGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experimentgroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateExperimentGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_experiment_group_with_options_async(
        self,
        request: pai_rec_service_20221213_models.CreateExperimentGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateExperimentGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.crowd_id):
            body['CrowdId'] = request.crowd_id
        if not UtilClient.is_unset(request.crowd_target_type):
            body['CrowdTargetType'] = request.crowd_target_type
        if not UtilClient.is_unset(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.distribution_time_duration):
            body['DistributionTimeDuration'] = request.distribution_time_duration
        if not UtilClient.is_unset(request.distribution_type):
            body['DistributionType'] = request.distribution_type
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.layer_id):
            body['LayerId'] = request.layer_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.need_aa):
            body['NeedAA'] = request.need_aa
        if not UtilClient.is_unset(request.random_flow):
            body['RandomFlow'] = request.random_flow
        if not UtilClient.is_unset(request.reserved_buckets):
            body['ReservedBuckets'] = request.reserved_buckets
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateExperimentGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experimentgroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateExperimentGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_experiment_group(
        self,
        request: pai_rec_service_20221213_models.CreateExperimentGroupRequest,
    ) -> pai_rec_service_20221213_models.CreateExperimentGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_experiment_group_with_options(request, headers, runtime)

    async def create_experiment_group_async(
        self,
        request: pai_rec_service_20221213_models.CreateExperimentGroupRequest,
    ) -> pai_rec_service_20221213_models.CreateExperimentGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_experiment_group_with_options_async(request, headers, runtime)

    def create_feature_consistency_check_job_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.feature_consistency_check_job_config_id):
            body['FeatureConsistencyCheckJobConfigId'] = request.feature_consistency_check_job_config_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sampling_duration):
            body['SamplingDuration'] = request.sampling_duration
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFeatureConsistencyCheckJob',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/featureconsistencycheck/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_feature_consistency_check_job_with_options_async(
        self,
        request: pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.feature_consistency_check_job_config_id):
            body['FeatureConsistencyCheckJobConfigId'] = request.feature_consistency_check_job_config_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sampling_duration):
            body['SamplingDuration'] = request.sampling_duration
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFeatureConsistencyCheckJob',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/featureconsistencycheck/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_feature_consistency_check_job(
        self,
        request: pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobRequest,
    ) -> pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_feature_consistency_check_job_with_options(request, headers, runtime)

    async def create_feature_consistency_check_job_async(
        self,
        request: pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobRequest,
    ) -> pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_feature_consistency_check_job_with_options_async(request, headers, runtime)

    def create_feature_consistency_check_job_config_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.compare_feature):
            body['CompareFeature'] = request.compare_feature
        if not UtilClient.is_unset(request.eas_service_name):
            body['EasServiceName'] = request.eas_service_name
        if not UtilClient.is_unset(request.easy_rec_package_path):
            body['EasyRecPackagePath'] = request.easy_rec_package_path
        if not UtilClient.is_unset(request.easy_rec_version):
            body['EasyRecVersion'] = request.easy_rec_version
        if not UtilClient.is_unset(request.feature_display_exclude):
            body['FeatureDisplayExclude'] = request.feature_display_exclude
        if not UtilClient.is_unset(request.feature_landing_resource_id):
            body['FeatureLandingResourceId'] = request.feature_landing_resource_id
        if not UtilClient.is_unset(request.feature_priority):
            body['FeaturePriority'] = request.feature_priority
        if not UtilClient.is_unset(request.feature_store_item_id):
            body['FeatureStoreItemId'] = request.feature_store_item_id
        if not UtilClient.is_unset(request.feature_store_model_id):
            body['FeatureStoreModelId'] = request.feature_store_model_id
        if not UtilClient.is_unset(request.feature_store_project_id):
            body['FeatureStoreProjectId'] = request.feature_store_project_id
        if not UtilClient.is_unset(request.feature_store_project_name):
            body['FeatureStoreProjectName'] = request.feature_store_project_name
        if not UtilClient.is_unset(request.feature_store_seq_feature_view):
            body['FeatureStoreSeqFeatureView'] = request.feature_store_seq_feature_view
        if not UtilClient.is_unset(request.feature_store_user_id):
            body['FeatureStoreUserId'] = request.feature_store_user_id
        if not UtilClient.is_unset(request.fg_jar_version):
            body['FgJarVersion'] = request.fg_jar_version
        if not UtilClient.is_unset(request.fg_json_file_name):
            body['FgJsonFileName'] = request.fg_json_file_name
        if not UtilClient.is_unset(request.generate_zip):
            body['GenerateZip'] = request.generate_zip
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.item_id_field):
            body['ItemIdField'] = request.item_id_field
        if not UtilClient.is_unset(request.item_table):
            body['ItemTable'] = request.item_table
        if not UtilClient.is_unset(request.item_table_partition_field):
            body['ItemTablePartitionField'] = request.item_table_partition_field
        if not UtilClient.is_unset(request.item_table_partition_field_format):
            body['ItemTablePartitionFieldFormat'] = request.item_table_partition_field_format
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.oss_resource_id):
            body['OssResourceId'] = request.oss_resource_id
        if not UtilClient.is_unset(request.sample_rate):
            body['SampleRate'] = request.sample_rate
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.use_feature_store):
            body['UseFeatureStore'] = request.use_feature_store
        if not UtilClient.is_unset(request.user_id_field):
            body['UserIdField'] = request.user_id_field
        if not UtilClient.is_unset(request.user_table):
            body['UserTable'] = request.user_table
        if not UtilClient.is_unset(request.user_table_partition_field):
            body['UserTablePartitionField'] = request.user_table_partition_field
        if not UtilClient.is_unset(request.user_table_partition_field_format):
            body['UserTablePartitionFieldFormat'] = request.user_table_partition_field_format
        if not UtilClient.is_unset(request.workflow_name):
            body['WorkflowName'] = request.workflow_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFeatureConsistencyCheckJobConfig',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/featureconsistencycheck/jobconfigs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_feature_consistency_check_job_config_with_options_async(
        self,
        request: pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.compare_feature):
            body['CompareFeature'] = request.compare_feature
        if not UtilClient.is_unset(request.eas_service_name):
            body['EasServiceName'] = request.eas_service_name
        if not UtilClient.is_unset(request.easy_rec_package_path):
            body['EasyRecPackagePath'] = request.easy_rec_package_path
        if not UtilClient.is_unset(request.easy_rec_version):
            body['EasyRecVersion'] = request.easy_rec_version
        if not UtilClient.is_unset(request.feature_display_exclude):
            body['FeatureDisplayExclude'] = request.feature_display_exclude
        if not UtilClient.is_unset(request.feature_landing_resource_id):
            body['FeatureLandingResourceId'] = request.feature_landing_resource_id
        if not UtilClient.is_unset(request.feature_priority):
            body['FeaturePriority'] = request.feature_priority
        if not UtilClient.is_unset(request.feature_store_item_id):
            body['FeatureStoreItemId'] = request.feature_store_item_id
        if not UtilClient.is_unset(request.feature_store_model_id):
            body['FeatureStoreModelId'] = request.feature_store_model_id
        if not UtilClient.is_unset(request.feature_store_project_id):
            body['FeatureStoreProjectId'] = request.feature_store_project_id
        if not UtilClient.is_unset(request.feature_store_project_name):
            body['FeatureStoreProjectName'] = request.feature_store_project_name
        if not UtilClient.is_unset(request.feature_store_seq_feature_view):
            body['FeatureStoreSeqFeatureView'] = request.feature_store_seq_feature_view
        if not UtilClient.is_unset(request.feature_store_user_id):
            body['FeatureStoreUserId'] = request.feature_store_user_id
        if not UtilClient.is_unset(request.fg_jar_version):
            body['FgJarVersion'] = request.fg_jar_version
        if not UtilClient.is_unset(request.fg_json_file_name):
            body['FgJsonFileName'] = request.fg_json_file_name
        if not UtilClient.is_unset(request.generate_zip):
            body['GenerateZip'] = request.generate_zip
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.item_id_field):
            body['ItemIdField'] = request.item_id_field
        if not UtilClient.is_unset(request.item_table):
            body['ItemTable'] = request.item_table
        if not UtilClient.is_unset(request.item_table_partition_field):
            body['ItemTablePartitionField'] = request.item_table_partition_field
        if not UtilClient.is_unset(request.item_table_partition_field_format):
            body['ItemTablePartitionFieldFormat'] = request.item_table_partition_field_format
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.oss_resource_id):
            body['OssResourceId'] = request.oss_resource_id
        if not UtilClient.is_unset(request.sample_rate):
            body['SampleRate'] = request.sample_rate
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.use_feature_store):
            body['UseFeatureStore'] = request.use_feature_store
        if not UtilClient.is_unset(request.user_id_field):
            body['UserIdField'] = request.user_id_field
        if not UtilClient.is_unset(request.user_table):
            body['UserTable'] = request.user_table
        if not UtilClient.is_unset(request.user_table_partition_field):
            body['UserTablePartitionField'] = request.user_table_partition_field
        if not UtilClient.is_unset(request.user_table_partition_field_format):
            body['UserTablePartitionFieldFormat'] = request.user_table_partition_field_format
        if not UtilClient.is_unset(request.workflow_name):
            body['WorkflowName'] = request.workflow_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFeatureConsistencyCheckJobConfig',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/featureconsistencycheck/jobconfigs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_feature_consistency_check_job_config(
        self,
        request: pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobConfigRequest,
    ) -> pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_feature_consistency_check_job_config_with_options(request, headers, runtime)

    async def create_feature_consistency_check_job_config_async(
        self,
        request: pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobConfigRequest,
    ) -> pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_feature_consistency_check_job_config_with_options_async(request, headers, runtime)

    def create_instance_resource_with_options(
        self,
        instance_id: str,
        request: pai_rec_service_20221213_models.CreateInstanceResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateInstanceResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.group):
            body['Group'] = request.group
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstanceResource',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/resources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateInstanceResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_resource_with_options_async(
        self,
        instance_id: str,
        request: pai_rec_service_20221213_models.CreateInstanceResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateInstanceResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.group):
            body['Group'] = request.group
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstanceResource',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/resources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateInstanceResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_resource(
        self,
        instance_id: str,
        request: pai_rec_service_20221213_models.CreateInstanceResourceRequest,
    ) -> pai_rec_service_20221213_models.CreateInstanceResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_resource_with_options(instance_id, request, headers, runtime)

    async def create_instance_resource_async(
        self,
        instance_id: str,
        request: pai_rec_service_20221213_models.CreateInstanceResourceRequest,
    ) -> pai_rec_service_20221213_models.CreateInstanceResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_resource_with_options_async(instance_id, request, headers, runtime)

    def create_laboratory_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateLaboratoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateLaboratoryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bucket_count):
            body['BucketCount'] = request.bucket_count
        if not UtilClient.is_unset(request.bucket_type):
            body['BucketType'] = request.bucket_type
        if not UtilClient.is_unset(request.buckets):
            body['Buckets'] = request.buckets
        if not UtilClient.is_unset(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLaboratory',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/laboratories',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateLaboratoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_laboratory_with_options_async(
        self,
        request: pai_rec_service_20221213_models.CreateLaboratoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateLaboratoryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bucket_count):
            body['BucketCount'] = request.bucket_count
        if not UtilClient.is_unset(request.bucket_type):
            body['BucketType'] = request.bucket_type
        if not UtilClient.is_unset(request.buckets):
            body['Buckets'] = request.buckets
        if not UtilClient.is_unset(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLaboratory',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/laboratories',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateLaboratoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_laboratory(
        self,
        request: pai_rec_service_20221213_models.CreateLaboratoryRequest,
    ) -> pai_rec_service_20221213_models.CreateLaboratoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_laboratory_with_options(request, headers, runtime)

    async def create_laboratory_async(
        self,
        request: pai_rec_service_20221213_models.CreateLaboratoryRequest,
    ) -> pai_rec_service_20221213_models.CreateLaboratoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_laboratory_with_options_async(request, headers, runtime)

    def create_layer_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateLayerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateLayerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.laboratory_id):
            body['LaboratoryId'] = request.laboratory_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLayer',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/layers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_layer_with_options_async(
        self,
        request: pai_rec_service_20221213_models.CreateLayerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateLayerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.laboratory_id):
            body['LaboratoryId'] = request.laboratory_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLayer',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/layers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_layer(
        self,
        request: pai_rec_service_20221213_models.CreateLayerRequest,
    ) -> pai_rec_service_20221213_models.CreateLayerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_layer_with_options(request, headers, runtime)

    async def create_layer_async(
        self,
        request: pai_rec_service_20221213_models.CreateLayerRequest,
    ) -> pai_rec_service_20221213_models.CreateLayerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_layer_with_options_async(request, headers, runtime)

    def create_param_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateParamRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateParamResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateParam',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/params',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateParamResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_param_with_options_async(
        self,
        request: pai_rec_service_20221213_models.CreateParamRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateParamResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateParam',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/params',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateParamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_param(
        self,
        request: pai_rec_service_20221213_models.CreateParamRequest,
    ) -> pai_rec_service_20221213_models.CreateParamResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_param_with_options(request, headers, runtime)

    async def create_param_async(
        self,
        request: pai_rec_service_20221213_models.CreateParamRequest,
    ) -> pai_rec_service_20221213_models.CreateParamResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_param_with_options_async(request, headers, runtime)

    def create_scene_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateSceneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateSceneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.flows):
            body['Flows'] = request.flows
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateScene',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/scenes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scene_with_options_async(
        self,
        request: pai_rec_service_20221213_models.CreateSceneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateSceneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.flows):
            body['Flows'] = request.flows
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateScene',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/scenes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scene(
        self,
        request: pai_rec_service_20221213_models.CreateSceneRequest,
    ) -> pai_rec_service_20221213_models.CreateSceneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_scene_with_options(request, headers, runtime)

    async def create_scene_async(
        self,
        request: pai_rec_service_20221213_models.CreateSceneRequest,
    ) -> pai_rec_service_20221213_models.CreateSceneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_scene_with_options_async(request, headers, runtime)

    def create_sub_crowd_with_options(
        self,
        crowd_id: str,
        request: pai_rec_service_20221213_models.CreateSubCrowdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateSubCrowdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSubCrowd',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/crowds/{OpenApiUtilClient.get_encode_param(crowd_id)}/subcrowds',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateSubCrowdResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sub_crowd_with_options_async(
        self,
        crowd_id: str,
        request: pai_rec_service_20221213_models.CreateSubCrowdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateSubCrowdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSubCrowd',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/crowds/{OpenApiUtilClient.get_encode_param(crowd_id)}/subcrowds',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateSubCrowdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sub_crowd(
        self,
        crowd_id: str,
        request: pai_rec_service_20221213_models.CreateSubCrowdRequest,
    ) -> pai_rec_service_20221213_models.CreateSubCrowdResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_sub_crowd_with_options(crowd_id, request, headers, runtime)

    async def create_sub_crowd_async(
        self,
        crowd_id: str,
        request: pai_rec_service_20221213_models.CreateSubCrowdRequest,
    ) -> pai_rec_service_20221213_models.CreateSubCrowdResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_sub_crowd_with_options_async(crowd_id, request, headers, runtime)

    def create_table_meta_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateTableMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateTableMetaResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.fields):
            body['Fields'] = request.fields
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module):
            body['Module'] = request.module
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTableMeta',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/tablemetas',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateTableMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_table_meta_with_options_async(
        self,
        request: pai_rec_service_20221213_models.CreateTableMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateTableMetaResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.fields):
            body['Fields'] = request.fields
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module):
            body['Module'] = request.module
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTableMeta',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/tablemetas',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateTableMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_table_meta(
        self,
        request: pai_rec_service_20221213_models.CreateTableMetaRequest,
    ) -> pai_rec_service_20221213_models.CreateTableMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_table_meta_with_options(request, headers, runtime)

    async def create_table_meta_async(
        self,
        request: pai_rec_service_20221213_models.CreateTableMetaRequest,
    ) -> pai_rec_service_20221213_models.CreateTableMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_table_meta_with_options_async(request, headers, runtime)

    def delete_abmetric_with_options(
        self,
        abmetric_id: str,
        request: pai_rec_service_20221213_models.DeleteABMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteABMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteABMetric',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/abmetrics/{OpenApiUtilClient.get_encode_param(abmetric_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteABMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_abmetric_with_options_async(
        self,
        abmetric_id: str,
        request: pai_rec_service_20221213_models.DeleteABMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteABMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteABMetric',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/abmetrics/{OpenApiUtilClient.get_encode_param(abmetric_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteABMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_abmetric(
        self,
        abmetric_id: str,
        request: pai_rec_service_20221213_models.DeleteABMetricRequest,
    ) -> pai_rec_service_20221213_models.DeleteABMetricResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_abmetric_with_options(abmetric_id, request, headers, runtime)

    async def delete_abmetric_async(
        self,
        abmetric_id: str,
        request: pai_rec_service_20221213_models.DeleteABMetricRequest,
    ) -> pai_rec_service_20221213_models.DeleteABMetricResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_abmetric_with_options_async(abmetric_id, request, headers, runtime)

    def delete_abmetric_group_with_options(
        self,
        abmetric_group_id: str,
        request: pai_rec_service_20221213_models.DeleteABMetricGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteABMetricGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteABMetricGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/abmetricgroups/{OpenApiUtilClient.get_encode_param(abmetric_group_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteABMetricGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_abmetric_group_with_options_async(
        self,
        abmetric_group_id: str,
        request: pai_rec_service_20221213_models.DeleteABMetricGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteABMetricGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteABMetricGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/abmetricgroups/{OpenApiUtilClient.get_encode_param(abmetric_group_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteABMetricGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_abmetric_group(
        self,
        abmetric_group_id: str,
        request: pai_rec_service_20221213_models.DeleteABMetricGroupRequest,
    ) -> pai_rec_service_20221213_models.DeleteABMetricGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_abmetric_group_with_options(abmetric_group_id, request, headers, runtime)

    async def delete_abmetric_group_async(
        self,
        abmetric_group_id: str,
        request: pai_rec_service_20221213_models.DeleteABMetricGroupRequest,
    ) -> pai_rec_service_20221213_models.DeleteABMetricGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_abmetric_group_with_options_async(abmetric_group_id, request, headers, runtime)

    def delete_crowd_with_options(
        self,
        crowd_id: str,
        request: pai_rec_service_20221213_models.DeleteCrowdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteCrowdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCrowd',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/crowds/{OpenApiUtilClient.get_encode_param(crowd_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteCrowdResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_crowd_with_options_async(
        self,
        crowd_id: str,
        request: pai_rec_service_20221213_models.DeleteCrowdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteCrowdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCrowd',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/crowds/{OpenApiUtilClient.get_encode_param(crowd_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteCrowdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_crowd(
        self,
        crowd_id: str,
        request: pai_rec_service_20221213_models.DeleteCrowdRequest,
    ) -> pai_rec_service_20221213_models.DeleteCrowdResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_crowd_with_options(crowd_id, request, headers, runtime)

    async def delete_crowd_async(
        self,
        crowd_id: str,
        request: pai_rec_service_20221213_models.DeleteCrowdRequest,
    ) -> pai_rec_service_20221213_models.DeleteCrowdResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_crowd_with_options_async(crowd_id, request, headers, runtime)

    def delete_experiment_with_options(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.DeleteExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteExperimentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteExperiment',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_experiment_with_options_async(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.DeleteExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteExperimentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteExperiment',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_experiment(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.DeleteExperimentRequest,
    ) -> pai_rec_service_20221213_models.DeleteExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_experiment_with_options(experiment_id, request, headers, runtime)

    async def delete_experiment_async(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.DeleteExperimentRequest,
    ) -> pai_rec_service_20221213_models.DeleteExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_experiment_with_options_async(experiment_id, request, headers, runtime)

    def delete_experiment_group_with_options(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.DeleteExperimentGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteExperimentGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteExperimentGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experimentgroups/{OpenApiUtilClient.get_encode_param(experiment_group_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteExperimentGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_experiment_group_with_options_async(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.DeleteExperimentGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteExperimentGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteExperimentGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experimentgroups/{OpenApiUtilClient.get_encode_param(experiment_group_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteExperimentGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_experiment_group(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.DeleteExperimentGroupRequest,
    ) -> pai_rec_service_20221213_models.DeleteExperimentGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_experiment_group_with_options(experiment_group_id, request, headers, runtime)

    async def delete_experiment_group_async(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.DeleteExperimentGroupRequest,
    ) -> pai_rec_service_20221213_models.DeleteExperimentGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_experiment_group_with_options_async(experiment_group_id, request, headers, runtime)

    def delete_instance_resource_with_options(
        self,
        instance_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteInstanceResourceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstanceResource',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/resources/{OpenApiUtilClient.get_encode_param(resource_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteInstanceResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_resource_with_options_async(
        self,
        instance_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteInstanceResourceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstanceResource',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/resources/{OpenApiUtilClient.get_encode_param(resource_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteInstanceResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance_resource(
        self,
        instance_id: str,
        resource_id: str,
    ) -> pai_rec_service_20221213_models.DeleteInstanceResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_resource_with_options(instance_id, resource_id, headers, runtime)

    async def delete_instance_resource_async(
        self,
        instance_id: str,
        resource_id: str,
    ) -> pai_rec_service_20221213_models.DeleteInstanceResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_instance_resource_with_options_async(instance_id, resource_id, headers, runtime)

    def delete_laboratory_with_options(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.DeleteLaboratoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteLaboratoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLaboratory',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/laboratories/{OpenApiUtilClient.get_encode_param(laboratory_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteLaboratoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_laboratory_with_options_async(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.DeleteLaboratoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteLaboratoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLaboratory',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/laboratories/{OpenApiUtilClient.get_encode_param(laboratory_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteLaboratoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_laboratory(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.DeleteLaboratoryRequest,
    ) -> pai_rec_service_20221213_models.DeleteLaboratoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_laboratory_with_options(laboratory_id, request, headers, runtime)

    async def delete_laboratory_async(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.DeleteLaboratoryRequest,
    ) -> pai_rec_service_20221213_models.DeleteLaboratoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_laboratory_with_options_async(laboratory_id, request, headers, runtime)

    def delete_layer_with_options(
        self,
        layer_id: str,
        request: pai_rec_service_20221213_models.DeleteLayerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteLayerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLayer',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/layers/{OpenApiUtilClient.get_encode_param(layer_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_layer_with_options_async(
        self,
        layer_id: str,
        request: pai_rec_service_20221213_models.DeleteLayerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteLayerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLayer',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/layers/{OpenApiUtilClient.get_encode_param(layer_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_layer(
        self,
        layer_id: str,
        request: pai_rec_service_20221213_models.DeleteLayerRequest,
    ) -> pai_rec_service_20221213_models.DeleteLayerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_layer_with_options(layer_id, request, headers, runtime)

    async def delete_layer_async(
        self,
        layer_id: str,
        request: pai_rec_service_20221213_models.DeleteLayerRequest,
    ) -> pai_rec_service_20221213_models.DeleteLayerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_layer_with_options_async(layer_id, request, headers, runtime)

    def delete_param_with_options(
        self,
        param_id: str,
        request: pai_rec_service_20221213_models.DeleteParamRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteParamResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteParam',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/params/{OpenApiUtilClient.get_encode_param(param_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteParamResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_param_with_options_async(
        self,
        param_id: str,
        request: pai_rec_service_20221213_models.DeleteParamRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteParamResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteParam',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/params/{OpenApiUtilClient.get_encode_param(param_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteParamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_param(
        self,
        param_id: str,
        request: pai_rec_service_20221213_models.DeleteParamRequest,
    ) -> pai_rec_service_20221213_models.DeleteParamResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_param_with_options(param_id, request, headers, runtime)

    async def delete_param_async(
        self,
        param_id: str,
        request: pai_rec_service_20221213_models.DeleteParamRequest,
    ) -> pai_rec_service_20221213_models.DeleteParamResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_param_with_options_async(param_id, request, headers, runtime)

    def delete_scene_with_options(
        self,
        scene_id: str,
        request: pai_rec_service_20221213_models.DeleteSceneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScene',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scene_with_options_async(
        self,
        scene_id: str,
        request: pai_rec_service_20221213_models.DeleteSceneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScene',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scene(
        self,
        scene_id: str,
        request: pai_rec_service_20221213_models.DeleteSceneRequest,
    ) -> pai_rec_service_20221213_models.DeleteSceneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_scene_with_options(scene_id, request, headers, runtime)

    async def delete_scene_async(
        self,
        scene_id: str,
        request: pai_rec_service_20221213_models.DeleteSceneRequest,
    ) -> pai_rec_service_20221213_models.DeleteSceneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_scene_with_options_async(scene_id, request, headers, runtime)

    def delete_sub_crowd_with_options(
        self,
        crowd_id: str,
        sub_crowd_id: str,
        request: pai_rec_service_20221213_models.DeleteSubCrowdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteSubCrowdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSubCrowd',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/crowds/{OpenApiUtilClient.get_encode_param(crowd_id)}/subcrowds/{OpenApiUtilClient.get_encode_param(sub_crowd_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteSubCrowdResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sub_crowd_with_options_async(
        self,
        crowd_id: str,
        sub_crowd_id: str,
        request: pai_rec_service_20221213_models.DeleteSubCrowdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteSubCrowdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSubCrowd',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/crowds/{OpenApiUtilClient.get_encode_param(crowd_id)}/subcrowds/{OpenApiUtilClient.get_encode_param(sub_crowd_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteSubCrowdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sub_crowd(
        self,
        crowd_id: str,
        sub_crowd_id: str,
        request: pai_rec_service_20221213_models.DeleteSubCrowdRequest,
    ) -> pai_rec_service_20221213_models.DeleteSubCrowdResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_sub_crowd_with_options(crowd_id, sub_crowd_id, request, headers, runtime)

    async def delete_sub_crowd_async(
        self,
        crowd_id: str,
        sub_crowd_id: str,
        request: pai_rec_service_20221213_models.DeleteSubCrowdRequest,
    ) -> pai_rec_service_20221213_models.DeleteSubCrowdResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_sub_crowd_with_options_async(crowd_id, sub_crowd_id, request, headers, runtime)

    def delete_table_meta_with_options(
        self,
        table_meta_id: str,
        request: pai_rec_service_20221213_models.DeleteTableMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteTableMetaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTableMeta',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/tablemetas/{OpenApiUtilClient.get_encode_param(table_meta_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteTableMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_table_meta_with_options_async(
        self,
        table_meta_id: str,
        request: pai_rec_service_20221213_models.DeleteTableMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteTableMetaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTableMeta',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/tablemetas/{OpenApiUtilClient.get_encode_param(table_meta_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteTableMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_table_meta(
        self,
        table_meta_id: str,
        request: pai_rec_service_20221213_models.DeleteTableMetaRequest,
    ) -> pai_rec_service_20221213_models.DeleteTableMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_table_meta_with_options(table_meta_id, request, headers, runtime)

    async def delete_table_meta_async(
        self,
        table_meta_id: str,
        request: pai_rec_service_20221213_models.DeleteTableMetaRequest,
    ) -> pai_rec_service_20221213_models.DeleteTableMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_table_meta_with_options_async(table_meta_id, request, headers, runtime)

    def get_abmetric_with_options(
        self,
        abmetric_id: str,
        request: pai_rec_service_20221213_models.GetABMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetABMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetABMetric',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/abmetrics/{OpenApiUtilClient.get_encode_param(abmetric_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetABMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_abmetric_with_options_async(
        self,
        abmetric_id: str,
        request: pai_rec_service_20221213_models.GetABMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetABMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetABMetric',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/abmetrics/{OpenApiUtilClient.get_encode_param(abmetric_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetABMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_abmetric(
        self,
        abmetric_id: str,
        request: pai_rec_service_20221213_models.GetABMetricRequest,
    ) -> pai_rec_service_20221213_models.GetABMetricResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_abmetric_with_options(abmetric_id, request, headers, runtime)

    async def get_abmetric_async(
        self,
        abmetric_id: str,
        request: pai_rec_service_20221213_models.GetABMetricRequest,
    ) -> pai_rec_service_20221213_models.GetABMetricResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_abmetric_with_options_async(abmetric_id, request, headers, runtime)

    def get_abmetric_group_with_options(
        self,
        abmetric_group_id: str,
        request: pai_rec_service_20221213_models.GetABMetricGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetABMetricGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetABMetricGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/abmetricgroups/{OpenApiUtilClient.get_encode_param(abmetric_group_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetABMetricGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_abmetric_group_with_options_async(
        self,
        abmetric_group_id: str,
        request: pai_rec_service_20221213_models.GetABMetricGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetABMetricGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetABMetricGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/abmetricgroups/{OpenApiUtilClient.get_encode_param(abmetric_group_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetABMetricGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_abmetric_group(
        self,
        abmetric_group_id: str,
        request: pai_rec_service_20221213_models.GetABMetricGroupRequest,
    ) -> pai_rec_service_20221213_models.GetABMetricGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_abmetric_group_with_options(abmetric_group_id, request, headers, runtime)

    async def get_abmetric_group_async(
        self,
        abmetric_group_id: str,
        request: pai_rec_service_20221213_models.GetABMetricGroupRequest,
    ) -> pai_rec_service_20221213_models.GetABMetricGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_abmetric_group_with_options_async(abmetric_group_id, request, headers, runtime)

    def get_calculation_job_with_options(
        self,
        calculation_job_id: str,
        request: pai_rec_service_20221213_models.GetCalculationJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetCalculationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCalculationJob',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/calculationjobs/{OpenApiUtilClient.get_encode_param(calculation_job_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetCalculationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_calculation_job_with_options_async(
        self,
        calculation_job_id: str,
        request: pai_rec_service_20221213_models.GetCalculationJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetCalculationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCalculationJob',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/calculationjobs/{OpenApiUtilClient.get_encode_param(calculation_job_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetCalculationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_calculation_job(
        self,
        calculation_job_id: str,
        request: pai_rec_service_20221213_models.GetCalculationJobRequest,
    ) -> pai_rec_service_20221213_models.GetCalculationJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_calculation_job_with_options(calculation_job_id, request, headers, runtime)

    async def get_calculation_job_async(
        self,
        calculation_job_id: str,
        request: pai_rec_service_20221213_models.GetCalculationJobRequest,
    ) -> pai_rec_service_20221213_models.GetCalculationJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_calculation_job_with_options_async(calculation_job_id, request, headers, runtime)

    def get_experiment_with_options(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.GetExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetExperimentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExperiment',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_experiment_with_options_async(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.GetExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetExperimentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExperiment',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_experiment(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.GetExperimentRequest,
    ) -> pai_rec_service_20221213_models.GetExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_experiment_with_options(experiment_id, request, headers, runtime)

    async def get_experiment_async(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.GetExperimentRequest,
    ) -> pai_rec_service_20221213_models.GetExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_experiment_with_options_async(experiment_id, request, headers, runtime)

    def get_experiment_group_with_options(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.GetExperimentGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetExperimentGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExperimentGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experimentgroups/{OpenApiUtilClient.get_encode_param(experiment_group_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetExperimentGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_experiment_group_with_options_async(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.GetExperimentGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetExperimentGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExperimentGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experimentgroups/{OpenApiUtilClient.get_encode_param(experiment_group_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetExperimentGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_experiment_group(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.GetExperimentGroupRequest,
    ) -> pai_rec_service_20221213_models.GetExperimentGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_experiment_group_with_options(experiment_group_id, request, headers, runtime)

    async def get_experiment_group_async(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.GetExperimentGroupRequest,
    ) -> pai_rec_service_20221213_models.GetExperimentGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_experiment_group_with_options_async(experiment_group_id, request, headers, runtime)

    def get_feature_consistency_check_job_with_options(
        self,
        feature_consistency_check_job_id: str,
        request: pai_rec_service_20221213_models.GetFeatureConsistencyCheckJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetFeatureConsistencyCheckJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFeatureConsistencyCheckJob',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/featureconsistencycheck/jobs/{OpenApiUtilClient.get_encode_param(feature_consistency_check_job_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetFeatureConsistencyCheckJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_feature_consistency_check_job_with_options_async(
        self,
        feature_consistency_check_job_id: str,
        request: pai_rec_service_20221213_models.GetFeatureConsistencyCheckJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetFeatureConsistencyCheckJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFeatureConsistencyCheckJob',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/featureconsistencycheck/jobs/{OpenApiUtilClient.get_encode_param(feature_consistency_check_job_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetFeatureConsistencyCheckJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_feature_consistency_check_job(
        self,
        feature_consistency_check_job_id: str,
        request: pai_rec_service_20221213_models.GetFeatureConsistencyCheckJobRequest,
    ) -> pai_rec_service_20221213_models.GetFeatureConsistencyCheckJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_feature_consistency_check_job_with_options(feature_consistency_check_job_id, request, headers, runtime)

    async def get_feature_consistency_check_job_async(
        self,
        feature_consistency_check_job_id: str,
        request: pai_rec_service_20221213_models.GetFeatureConsistencyCheckJobRequest,
    ) -> pai_rec_service_20221213_models.GetFeatureConsistencyCheckJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_feature_consistency_check_job_with_options_async(feature_consistency_check_job_id, request, headers, runtime)

    def get_feature_consistency_check_job_config_with_options(
        self,
        feature_consistency_check_job_config_id: str,
        request: pai_rec_service_20221213_models.GetFeatureConsistencyCheckJobConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetFeatureConsistencyCheckJobConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFeatureConsistencyCheckJobConfig',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/featureconsistencycheck/jobconfigs/{OpenApiUtilClient.get_encode_param(feature_consistency_check_job_config_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetFeatureConsistencyCheckJobConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_feature_consistency_check_job_config_with_options_async(
        self,
        feature_consistency_check_job_config_id: str,
        request: pai_rec_service_20221213_models.GetFeatureConsistencyCheckJobConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetFeatureConsistencyCheckJobConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFeatureConsistencyCheckJobConfig',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/featureconsistencycheck/jobconfigs/{OpenApiUtilClient.get_encode_param(feature_consistency_check_job_config_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetFeatureConsistencyCheckJobConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_feature_consistency_check_job_config(
        self,
        feature_consistency_check_job_config_id: str,
        request: pai_rec_service_20221213_models.GetFeatureConsistencyCheckJobConfigRequest,
    ) -> pai_rec_service_20221213_models.GetFeatureConsistencyCheckJobConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_feature_consistency_check_job_config_with_options(feature_consistency_check_job_config_id, request, headers, runtime)

    async def get_feature_consistency_check_job_config_async(
        self,
        feature_consistency_check_job_config_id: str,
        request: pai_rec_service_20221213_models.GetFeatureConsistencyCheckJobConfigRequest,
    ) -> pai_rec_service_20221213_models.GetFeatureConsistencyCheckJobConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_feature_consistency_check_job_config_with_options_async(feature_consistency_check_job_config_id, request, headers, runtime)

    def get_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        instance_id: str,
    ) -> pai_rec_service_20221213_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(instance_id, headers, runtime)

    async def get_instance_async(
        self,
        instance_id: str,
    ) -> pai_rec_service_20221213_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_with_options_async(instance_id, headers, runtime)

    def get_instance_resource_with_options(
        self,
        instance_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetInstanceResourceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstanceResource',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/resources/{OpenApiUtilClient.get_encode_param(resource_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetInstanceResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_resource_with_options_async(
        self,
        instance_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetInstanceResourceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstanceResource',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/resources/{OpenApiUtilClient.get_encode_param(resource_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetInstanceResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_resource(
        self,
        instance_id: str,
        resource_id: str,
    ) -> pai_rec_service_20221213_models.GetInstanceResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_resource_with_options(instance_id, resource_id, headers, runtime)

    async def get_instance_resource_async(
        self,
        instance_id: str,
        resource_id: str,
    ) -> pai_rec_service_20221213_models.GetInstanceResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_resource_with_options_async(instance_id, resource_id, headers, runtime)

    def get_instance_resource_table_with_options(
        self,
        instance_id: str,
        resource_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetInstanceResourceTableResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstanceResourceTable',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/resources/{OpenApiUtilClient.get_encode_param(resource_id)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetInstanceResourceTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_resource_table_with_options_async(
        self,
        instance_id: str,
        resource_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetInstanceResourceTableResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstanceResourceTable',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/resources/{OpenApiUtilClient.get_encode_param(resource_id)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetInstanceResourceTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_resource_table(
        self,
        instance_id: str,
        resource_id: str,
        table_name: str,
    ) -> pai_rec_service_20221213_models.GetInstanceResourceTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_resource_table_with_options(instance_id, resource_id, table_name, headers, runtime)

    async def get_instance_resource_table_async(
        self,
        instance_id: str,
        resource_id: str,
        table_name: str,
    ) -> pai_rec_service_20221213_models.GetInstanceResourceTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_resource_table_with_options_async(instance_id, resource_id, table_name, headers, runtime)

    def get_laboratory_with_options(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.GetLaboratoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetLaboratoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLaboratory',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/laboratories/{OpenApiUtilClient.get_encode_param(laboratory_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetLaboratoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_laboratory_with_options_async(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.GetLaboratoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetLaboratoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLaboratory',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/laboratories/{OpenApiUtilClient.get_encode_param(laboratory_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetLaboratoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_laboratory(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.GetLaboratoryRequest,
    ) -> pai_rec_service_20221213_models.GetLaboratoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_laboratory_with_options(laboratory_id, request, headers, runtime)

    async def get_laboratory_async(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.GetLaboratoryRequest,
    ) -> pai_rec_service_20221213_models.GetLaboratoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_laboratory_with_options_async(laboratory_id, request, headers, runtime)

    def get_layer_with_options(
        self,
        layer_id: str,
        request: pai_rec_service_20221213_models.GetLayerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetLayerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLayer',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/layers/{OpenApiUtilClient.get_encode_param(layer_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_layer_with_options_async(
        self,
        layer_id: str,
        request: pai_rec_service_20221213_models.GetLayerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetLayerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLayer',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/layers/{OpenApiUtilClient.get_encode_param(layer_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_layer(
        self,
        layer_id: str,
        request: pai_rec_service_20221213_models.GetLayerRequest,
    ) -> pai_rec_service_20221213_models.GetLayerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_layer_with_options(layer_id, request, headers, runtime)

    async def get_layer_async(
        self,
        layer_id: str,
        request: pai_rec_service_20221213_models.GetLayerRequest,
    ) -> pai_rec_service_20221213_models.GetLayerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_layer_with_options_async(layer_id, request, headers, runtime)

    def get_scene_with_options(
        self,
        scene_id: str,
        request: pai_rec_service_20221213_models.GetSceneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScene',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scene_with_options_async(
        self,
        scene_id: str,
        request: pai_rec_service_20221213_models.GetSceneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScene',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scene(
        self,
        scene_id: str,
        request: pai_rec_service_20221213_models.GetSceneRequest,
    ) -> pai_rec_service_20221213_models.GetSceneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_scene_with_options(scene_id, request, headers, runtime)

    async def get_scene_async(
        self,
        scene_id: str,
        request: pai_rec_service_20221213_models.GetSceneRequest,
    ) -> pai_rec_service_20221213_models.GetSceneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_scene_with_options_async(scene_id, request, headers, runtime)

    def get_sub_crowd_with_options(
        self,
        crowd_id: str,
        sub_crowd_id: str,
        request: pai_rec_service_20221213_models.GetSubCrowdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetSubCrowdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSubCrowd',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/crowds/{OpenApiUtilClient.get_encode_param(crowd_id)}/subcrowds/{OpenApiUtilClient.get_encode_param(sub_crowd_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetSubCrowdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sub_crowd_with_options_async(
        self,
        crowd_id: str,
        sub_crowd_id: str,
        request: pai_rec_service_20221213_models.GetSubCrowdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetSubCrowdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSubCrowd',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/crowds/{OpenApiUtilClient.get_encode_param(crowd_id)}/subcrowds/{OpenApiUtilClient.get_encode_param(sub_crowd_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetSubCrowdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sub_crowd(
        self,
        crowd_id: str,
        sub_crowd_id: str,
        request: pai_rec_service_20221213_models.GetSubCrowdRequest,
    ) -> pai_rec_service_20221213_models.GetSubCrowdResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_sub_crowd_with_options(crowd_id, sub_crowd_id, request, headers, runtime)

    async def get_sub_crowd_async(
        self,
        crowd_id: str,
        sub_crowd_id: str,
        request: pai_rec_service_20221213_models.GetSubCrowdRequest,
    ) -> pai_rec_service_20221213_models.GetSubCrowdResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_sub_crowd_with_options_async(crowd_id, sub_crowd_id, request, headers, runtime)

    def get_table_meta_with_options(
        self,
        table_meta_id: str,
        request: pai_rec_service_20221213_models.GetTableMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetTableMetaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTableMeta',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/tablemetas/{OpenApiUtilClient.get_encode_param(table_meta_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetTableMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_meta_with_options_async(
        self,
        table_meta_id: str,
        request: pai_rec_service_20221213_models.GetTableMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetTableMetaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTableMeta',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/tablemetas/{OpenApiUtilClient.get_encode_param(table_meta_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetTableMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_meta(
        self,
        table_meta_id: str,
        request: pai_rec_service_20221213_models.GetTableMetaRequest,
    ) -> pai_rec_service_20221213_models.GetTableMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_table_meta_with_options(table_meta_id, request, headers, runtime)

    async def get_table_meta_async(
        self,
        table_meta_id: str,
        request: pai_rec_service_20221213_models.GetTableMetaRequest,
    ) -> pai_rec_service_20221213_models.GetTableMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_table_meta_with_options_async(table_meta_id, request, headers, runtime)

    def list_abmetric_groups_with_options(
        self,
        request: pai_rec_service_20221213_models.ListABMetricGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListABMetricGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.realtime):
            query['Realtime'] = request.realtime
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListABMetricGroups',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/abmetricgroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListABMetricGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_abmetric_groups_with_options_async(
        self,
        request: pai_rec_service_20221213_models.ListABMetricGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListABMetricGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.realtime):
            query['Realtime'] = request.realtime
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListABMetricGroups',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/abmetricgroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListABMetricGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_abmetric_groups(
        self,
        request: pai_rec_service_20221213_models.ListABMetricGroupsRequest,
    ) -> pai_rec_service_20221213_models.ListABMetricGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_abmetric_groups_with_options(request, headers, runtime)

    async def list_abmetric_groups_async(
        self,
        request: pai_rec_service_20221213_models.ListABMetricGroupsRequest,
    ) -> pai_rec_service_20221213_models.ListABMetricGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_abmetric_groups_with_options_async(request, headers, runtime)

    def list_abmetrics_with_options(
        self,
        request: pai_rec_service_20221213_models.ListABMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListABMetricsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.realtime):
            query['Realtime'] = request.realtime
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.table_meta_id):
            query['TableMetaId'] = request.table_meta_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListABMetrics',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/abmetrics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListABMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_abmetrics_with_options_async(
        self,
        request: pai_rec_service_20221213_models.ListABMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListABMetricsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.realtime):
            query['Realtime'] = request.realtime
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.table_meta_id):
            query['TableMetaId'] = request.table_meta_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListABMetrics',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/abmetrics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListABMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_abmetrics(
        self,
        request: pai_rec_service_20221213_models.ListABMetricsRequest,
    ) -> pai_rec_service_20221213_models.ListABMetricsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_abmetrics_with_options(request, headers, runtime)

    async def list_abmetrics_async(
        self,
        request: pai_rec_service_20221213_models.ListABMetricsRequest,
    ) -> pai_rec_service_20221213_models.ListABMetricsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_abmetrics_with_options_async(request, headers, runtime)

    def list_calculation_jobs_with_options(
        self,
        request: pai_rec_service_20221213_models.ListCalculationJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListCalculationJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCalculationJobs',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/calculationjobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListCalculationJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_calculation_jobs_with_options_async(
        self,
        request: pai_rec_service_20221213_models.ListCalculationJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListCalculationJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCalculationJobs',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/calculationjobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListCalculationJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_calculation_jobs(
        self,
        request: pai_rec_service_20221213_models.ListCalculationJobsRequest,
    ) -> pai_rec_service_20221213_models.ListCalculationJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_calculation_jobs_with_options(request, headers, runtime)

    async def list_calculation_jobs_async(
        self,
        request: pai_rec_service_20221213_models.ListCalculationJobsRequest,
    ) -> pai_rec_service_20221213_models.ListCalculationJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_calculation_jobs_with_options_async(request, headers, runtime)

    def list_crowd_users_with_options(
        self,
        crowd_id: str,
        request: pai_rec_service_20221213_models.ListCrowdUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListCrowdUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCrowdUsers',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/crowds/{OpenApiUtilClient.get_encode_param(crowd_id)}/users',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListCrowdUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_crowd_users_with_options_async(
        self,
        crowd_id: str,
        request: pai_rec_service_20221213_models.ListCrowdUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListCrowdUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCrowdUsers',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/crowds/{OpenApiUtilClient.get_encode_param(crowd_id)}/users',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListCrowdUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_crowd_users(
        self,
        crowd_id: str,
        request: pai_rec_service_20221213_models.ListCrowdUsersRequest,
    ) -> pai_rec_service_20221213_models.ListCrowdUsersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_crowd_users_with_options(crowd_id, request, headers, runtime)

    async def list_crowd_users_async(
        self,
        crowd_id: str,
        request: pai_rec_service_20221213_models.ListCrowdUsersRequest,
    ) -> pai_rec_service_20221213_models.ListCrowdUsersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_crowd_users_with_options_async(crowd_id, request, headers, runtime)

    def list_crowds_with_options(
        self,
        request: pai_rec_service_20221213_models.ListCrowdsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListCrowdsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCrowds',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/crowds',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListCrowdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_crowds_with_options_async(
        self,
        request: pai_rec_service_20221213_models.ListCrowdsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListCrowdsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCrowds',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/crowds',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListCrowdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_crowds(
        self,
        request: pai_rec_service_20221213_models.ListCrowdsRequest,
    ) -> pai_rec_service_20221213_models.ListCrowdsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_crowds_with_options(request, headers, runtime)

    async def list_crowds_async(
        self,
        request: pai_rec_service_20221213_models.ListCrowdsRequest,
    ) -> pai_rec_service_20221213_models.ListCrowdsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_crowds_with_options_async(request, headers, runtime)

    def list_experiment_groups_with_options(
        self,
        request: pai_rec_service_20221213_models.ListExperimentGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListExperimentGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.layer_id):
            query['LayerId'] = request.layer_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExperimentGroups',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experimentgroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListExperimentGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_experiment_groups_with_options_async(
        self,
        request: pai_rec_service_20221213_models.ListExperimentGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListExperimentGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.layer_id):
            query['LayerId'] = request.layer_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExperimentGroups',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experimentgroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListExperimentGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_experiment_groups(
        self,
        request: pai_rec_service_20221213_models.ListExperimentGroupsRequest,
    ) -> pai_rec_service_20221213_models.ListExperimentGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_experiment_groups_with_options(request, headers, runtime)

    async def list_experiment_groups_async(
        self,
        request: pai_rec_service_20221213_models.ListExperimentGroupsRequest,
    ) -> pai_rec_service_20221213_models.ListExperimentGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_experiment_groups_with_options_async(request, headers, runtime)

    def list_experiments_with_options(
        self,
        request: pai_rec_service_20221213_models.ListExperimentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListExperimentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.experiment_group_id):
            query['ExperimentGroupId'] = request.experiment_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExperiments',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListExperimentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_experiments_with_options_async(
        self,
        request: pai_rec_service_20221213_models.ListExperimentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListExperimentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.experiment_group_id):
            query['ExperimentGroupId'] = request.experiment_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExperiments',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListExperimentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_experiments(
        self,
        request: pai_rec_service_20221213_models.ListExperimentsRequest,
    ) -> pai_rec_service_20221213_models.ListExperimentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_experiments_with_options(request, headers, runtime)

    async def list_experiments_async(
        self,
        request: pai_rec_service_20221213_models.ListExperimentsRequest,
    ) -> pai_rec_service_20221213_models.ListExperimentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_experiments_with_options_async(request, headers, runtime)

    def list_feature_consistency_check_job_configs_with_options(
        self,
        request: pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFeatureConsistencyCheckJobConfigs',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/featureconsistencycheck/jobconfigs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_feature_consistency_check_job_configs_with_options_async(
        self,
        request: pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFeatureConsistencyCheckJobConfigs',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/featureconsistencycheck/jobconfigs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_feature_consistency_check_job_configs(
        self,
        request: pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobConfigsRequest,
    ) -> pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobConfigsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_feature_consistency_check_job_configs_with_options(request, headers, runtime)

    async def list_feature_consistency_check_job_configs_async(
        self,
        request: pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobConfigsRequest,
    ) -> pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobConfigsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_feature_consistency_check_job_configs_with_options_async(request, headers, runtime)

    def list_feature_consistency_check_job_feature_reports_with_options(
        self,
        feature_consistency_check_job_id: str,
        request: pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobFeatureReportsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobFeatureReportsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.log_item_id):
            query['LogItemId'] = request.log_item_id
        if not UtilClient.is_unset(request.log_request_id):
            query['LogRequestId'] = request.log_request_id
        if not UtilClient.is_unset(request.log_user_id):
            query['LogUserId'] = request.log_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFeatureConsistencyCheckJobFeatureReports',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/featureconsistencycheck/jobs/{OpenApiUtilClient.get_encode_param(feature_consistency_check_job_id)}/featurereports',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobFeatureReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_feature_consistency_check_job_feature_reports_with_options_async(
        self,
        feature_consistency_check_job_id: str,
        request: pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobFeatureReportsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobFeatureReportsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.log_item_id):
            query['LogItemId'] = request.log_item_id
        if not UtilClient.is_unset(request.log_request_id):
            query['LogRequestId'] = request.log_request_id
        if not UtilClient.is_unset(request.log_user_id):
            query['LogUserId'] = request.log_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFeatureConsistencyCheckJobFeatureReports',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/featureconsistencycheck/jobs/{OpenApiUtilClient.get_encode_param(feature_consistency_check_job_id)}/featurereports',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobFeatureReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_feature_consistency_check_job_feature_reports(
        self,
        feature_consistency_check_job_id: str,
        request: pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobFeatureReportsRequest,
    ) -> pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobFeatureReportsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_feature_consistency_check_job_feature_reports_with_options(feature_consistency_check_job_id, request, headers, runtime)

    async def list_feature_consistency_check_job_feature_reports_async(
        self,
        feature_consistency_check_job_id: str,
        request: pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobFeatureReportsRequest,
    ) -> pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobFeatureReportsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_feature_consistency_check_job_feature_reports_with_options_async(feature_consistency_check_job_id, request, headers, runtime)

    def list_feature_consistency_check_job_score_reports_with_options(
        self,
        feature_consistency_check_job_id: str,
        tmp_req: pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobScoreReportsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobScoreReportsResponse:
        UtilClient.validate_model(tmp_req)
        request = pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobScoreReportsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.exclude_request_ids):
            request.exclude_request_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.exclude_request_ids, 'ExcludeRequestIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.exclude_request_ids_shrink):
            query['ExcludeRequestIds'] = request.exclude_request_ids_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFeatureConsistencyCheckJobScoreReports',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/featureconsistencycheck/jobs/{OpenApiUtilClient.get_encode_param(feature_consistency_check_job_id)}/scorereports',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobScoreReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_feature_consistency_check_job_score_reports_with_options_async(
        self,
        feature_consistency_check_job_id: str,
        tmp_req: pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobScoreReportsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobScoreReportsResponse:
        UtilClient.validate_model(tmp_req)
        request = pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobScoreReportsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.exclude_request_ids):
            request.exclude_request_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.exclude_request_ids, 'ExcludeRequestIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.exclude_request_ids_shrink):
            query['ExcludeRequestIds'] = request.exclude_request_ids_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFeatureConsistencyCheckJobScoreReports',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/featureconsistencycheck/jobs/{OpenApiUtilClient.get_encode_param(feature_consistency_check_job_id)}/scorereports',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobScoreReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_feature_consistency_check_job_score_reports(
        self,
        feature_consistency_check_job_id: str,
        request: pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobScoreReportsRequest,
    ) -> pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobScoreReportsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_feature_consistency_check_job_score_reports_with_options(feature_consistency_check_job_id, request, headers, runtime)

    async def list_feature_consistency_check_job_score_reports_async(
        self,
        feature_consistency_check_job_id: str,
        request: pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobScoreReportsRequest,
    ) -> pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobScoreReportsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_feature_consistency_check_job_score_reports_with_options_async(feature_consistency_check_job_id, request, headers, runtime)

    def list_feature_consistency_check_jobs_with_options(
        self,
        request: pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFeatureConsistencyCheckJobs',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/featureconsistencycheck/jobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_feature_consistency_check_jobs_with_options_async(
        self,
        request: pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFeatureConsistencyCheckJobs',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/featureconsistencycheck/jobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_feature_consistency_check_jobs(
        self,
        request: pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobsRequest,
    ) -> pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_feature_consistency_check_jobs_with_options(request, headers, runtime)

    async def list_feature_consistency_check_jobs_async(
        self,
        request: pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobsRequest,
    ) -> pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_feature_consistency_check_jobs_with_options_async(request, headers, runtime)

    def list_instance_resources_with_options(
        self,
        instance_id: str,
        request: pai_rec_service_20221213_models.ListInstanceResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListInstanceResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceResources',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListInstanceResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_resources_with_options_async(
        self,
        instance_id: str,
        request: pai_rec_service_20221213_models.ListInstanceResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListInstanceResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceResources',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListInstanceResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_resources(
        self,
        instance_id: str,
        request: pai_rec_service_20221213_models.ListInstanceResourcesRequest,
    ) -> pai_rec_service_20221213_models.ListInstanceResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_resources_with_options(instance_id, request, headers, runtime)

    async def list_instance_resources_async(
        self,
        instance_id: str,
        request: pai_rec_service_20221213_models.ListInstanceResourcesRequest,
    ) -> pai_rec_service_20221213_models.ListInstanceResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instance_resources_with_options_async(instance_id, request, headers, runtime)

    def list_instances_with_options(
        self,
        request: pai_rec_service_20221213_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: pai_rec_service_20221213_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: pai_rec_service_20221213_models.ListInstancesRequest,
    ) -> pai_rec_service_20221213_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    async def list_instances_async(
        self,
        request: pai_rec_service_20221213_models.ListInstancesRequest,
    ) -> pai_rec_service_20221213_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instances_with_options_async(request, headers, runtime)

    def list_laboratories_with_options(
        self,
        request: pai_rec_service_20221213_models.ListLaboratoriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListLaboratoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment):
            query['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLaboratories',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/laboratories',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListLaboratoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_laboratories_with_options_async(
        self,
        request: pai_rec_service_20221213_models.ListLaboratoriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListLaboratoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment):
            query['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLaboratories',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/laboratories',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListLaboratoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_laboratories(
        self,
        request: pai_rec_service_20221213_models.ListLaboratoriesRequest,
    ) -> pai_rec_service_20221213_models.ListLaboratoriesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_laboratories_with_options(request, headers, runtime)

    async def list_laboratories_async(
        self,
        request: pai_rec_service_20221213_models.ListLaboratoriesRequest,
    ) -> pai_rec_service_20221213_models.ListLaboratoriesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_laboratories_with_options_async(request, headers, runtime)

    def list_layers_with_options(
        self,
        request: pai_rec_service_20221213_models.ListLayersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListLayersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.laboratory_id):
            query['LaboratoryId'] = request.laboratory_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLayers',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/layers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListLayersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_layers_with_options_async(
        self,
        request: pai_rec_service_20221213_models.ListLayersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListLayersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.laboratory_id):
            query['LaboratoryId'] = request.laboratory_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLayers',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/layers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListLayersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_layers(
        self,
        request: pai_rec_service_20221213_models.ListLayersRequest,
    ) -> pai_rec_service_20221213_models.ListLayersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_layers_with_options(request, headers, runtime)

    async def list_layers_async(
        self,
        request: pai_rec_service_20221213_models.ListLayersRequest,
    ) -> pai_rec_service_20221213_models.ListLayersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_layers_with_options_async(request, headers, runtime)

    def list_params_with_options(
        self,
        request: pai_rec_service_20221213_models.ListParamsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListParamsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment):
            query['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListParams',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/params',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListParamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_params_with_options_async(
        self,
        request: pai_rec_service_20221213_models.ListParamsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListParamsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment):
            query['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListParams',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/params',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListParamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_params(
        self,
        request: pai_rec_service_20221213_models.ListParamsRequest,
    ) -> pai_rec_service_20221213_models.ListParamsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_params_with_options(request, headers, runtime)

    async def list_params_async(
        self,
        request: pai_rec_service_20221213_models.ListParamsRequest,
    ) -> pai_rec_service_20221213_models.ListParamsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_params_with_options_async(request, headers, runtime)

    def list_scenes_with_options(
        self,
        request: pai_rec_service_20221213_models.ListScenesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListScenesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScenes',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/scenes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListScenesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scenes_with_options_async(
        self,
        request: pai_rec_service_20221213_models.ListScenesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListScenesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScenes',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/scenes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListScenesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scenes(
        self,
        request: pai_rec_service_20221213_models.ListScenesRequest,
    ) -> pai_rec_service_20221213_models.ListScenesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_scenes_with_options(request, headers, runtime)

    async def list_scenes_async(
        self,
        request: pai_rec_service_20221213_models.ListScenesRequest,
    ) -> pai_rec_service_20221213_models.ListScenesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_scenes_with_options_async(request, headers, runtime)

    def list_sub_crowds_with_options(
        self,
        crowd_id: str,
        request: pai_rec_service_20221213_models.ListSubCrowdsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListSubCrowdsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSubCrowds',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/crowds/{OpenApiUtilClient.get_encode_param(crowd_id)}/subcrowds',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListSubCrowdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sub_crowds_with_options_async(
        self,
        crowd_id: str,
        request: pai_rec_service_20221213_models.ListSubCrowdsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListSubCrowdsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSubCrowds',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/crowds/{OpenApiUtilClient.get_encode_param(crowd_id)}/subcrowds',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListSubCrowdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sub_crowds(
        self,
        crowd_id: str,
        request: pai_rec_service_20221213_models.ListSubCrowdsRequest,
    ) -> pai_rec_service_20221213_models.ListSubCrowdsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_sub_crowds_with_options(crowd_id, request, headers, runtime)

    async def list_sub_crowds_async(
        self,
        crowd_id: str,
        request: pai_rec_service_20221213_models.ListSubCrowdsRequest,
    ) -> pai_rec_service_20221213_models.ListSubCrowdsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_sub_crowds_with_options_async(crowd_id, request, headers, runtime)

    def list_table_metas_with_options(
        self,
        request: pai_rec_service_20221213_models.ListTableMetasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListTableMetasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module):
            query['Module'] = request.module
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTableMetas',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/tablemetas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListTableMetasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_table_metas_with_options_async(
        self,
        request: pai_rec_service_20221213_models.ListTableMetasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListTableMetasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module):
            query['Module'] = request.module
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTableMetas',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/tablemetas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListTableMetasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_table_metas(
        self,
        request: pai_rec_service_20221213_models.ListTableMetasRequest,
    ) -> pai_rec_service_20221213_models.ListTableMetasResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_table_metas_with_options(request, headers, runtime)

    async def list_table_metas_async(
        self,
        request: pai_rec_service_20221213_models.ListTableMetasRequest,
    ) -> pai_rec_service_20221213_models.ListTableMetasResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_table_metas_with_options_async(request, headers, runtime)

    def offline_experiment_with_options(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.OfflineExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.OfflineExperimentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OfflineExperiment',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}/action/offline',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.OfflineExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def offline_experiment_with_options_async(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.OfflineExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.OfflineExperimentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OfflineExperiment',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}/action/offline',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.OfflineExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def offline_experiment(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.OfflineExperimentRequest,
    ) -> pai_rec_service_20221213_models.OfflineExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.offline_experiment_with_options(experiment_id, request, headers, runtime)

    async def offline_experiment_async(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.OfflineExperimentRequest,
    ) -> pai_rec_service_20221213_models.OfflineExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.offline_experiment_with_options_async(experiment_id, request, headers, runtime)

    def offline_experiment_group_with_options(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.OfflineExperimentGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.OfflineExperimentGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OfflineExperimentGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experimentgroups/{OpenApiUtilClient.get_encode_param(experiment_group_id)}/action/offline',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.OfflineExperimentGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def offline_experiment_group_with_options_async(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.OfflineExperimentGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.OfflineExperimentGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OfflineExperimentGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experimentgroups/{OpenApiUtilClient.get_encode_param(experiment_group_id)}/action/offline',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.OfflineExperimentGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def offline_experiment_group(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.OfflineExperimentGroupRequest,
    ) -> pai_rec_service_20221213_models.OfflineExperimentGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.offline_experiment_group_with_options(experiment_group_id, request, headers, runtime)

    async def offline_experiment_group_async(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.OfflineExperimentGroupRequest,
    ) -> pai_rec_service_20221213_models.OfflineExperimentGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.offline_experiment_group_with_options_async(experiment_group_id, request, headers, runtime)

    def offline_laboratory_with_options(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.OfflineLaboratoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.OfflineLaboratoryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OfflineLaboratory',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/laboratories/{OpenApiUtilClient.get_encode_param(laboratory_id)}/action/offline',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.OfflineLaboratoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def offline_laboratory_with_options_async(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.OfflineLaboratoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.OfflineLaboratoryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OfflineLaboratory',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/laboratories/{OpenApiUtilClient.get_encode_param(laboratory_id)}/action/offline',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.OfflineLaboratoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def offline_laboratory(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.OfflineLaboratoryRequest,
    ) -> pai_rec_service_20221213_models.OfflineLaboratoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.offline_laboratory_with_options(laboratory_id, request, headers, runtime)

    async def offline_laboratory_async(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.OfflineLaboratoryRequest,
    ) -> pai_rec_service_20221213_models.OfflineLaboratoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.offline_laboratory_with_options_async(laboratory_id, request, headers, runtime)

    def online_experiment_with_options(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.OnlineExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.OnlineExperimentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OnlineExperiment',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}/action/online',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.OnlineExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def online_experiment_with_options_async(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.OnlineExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.OnlineExperimentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OnlineExperiment',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}/action/online',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.OnlineExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def online_experiment(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.OnlineExperimentRequest,
    ) -> pai_rec_service_20221213_models.OnlineExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.online_experiment_with_options(experiment_id, request, headers, runtime)

    async def online_experiment_async(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.OnlineExperimentRequest,
    ) -> pai_rec_service_20221213_models.OnlineExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.online_experiment_with_options_async(experiment_id, request, headers, runtime)

    def online_experiment_group_with_options(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.OnlineExperimentGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.OnlineExperimentGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OnlineExperimentGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experimentgroups/{OpenApiUtilClient.get_encode_param(experiment_group_id)}/action/online',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.OnlineExperimentGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def online_experiment_group_with_options_async(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.OnlineExperimentGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.OnlineExperimentGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OnlineExperimentGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experimentgroups/{OpenApiUtilClient.get_encode_param(experiment_group_id)}/action/online',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.OnlineExperimentGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def online_experiment_group(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.OnlineExperimentGroupRequest,
    ) -> pai_rec_service_20221213_models.OnlineExperimentGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.online_experiment_group_with_options(experiment_group_id, request, headers, runtime)

    async def online_experiment_group_async(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.OnlineExperimentGroupRequest,
    ) -> pai_rec_service_20221213_models.OnlineExperimentGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.online_experiment_group_with_options_async(experiment_group_id, request, headers, runtime)

    def online_laboratory_with_options(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.OnlineLaboratoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.OnlineLaboratoryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OnlineLaboratory',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/laboratories/{OpenApiUtilClient.get_encode_param(laboratory_id)}/action/online',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.OnlineLaboratoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def online_laboratory_with_options_async(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.OnlineLaboratoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.OnlineLaboratoryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OnlineLaboratory',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/laboratories/{OpenApiUtilClient.get_encode_param(laboratory_id)}/action/online',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.OnlineLaboratoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def online_laboratory(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.OnlineLaboratoryRequest,
    ) -> pai_rec_service_20221213_models.OnlineLaboratoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.online_laboratory_with_options(laboratory_id, request, headers, runtime)

    async def online_laboratory_async(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.OnlineLaboratoryRequest,
    ) -> pai_rec_service_20221213_models.OnlineLaboratoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.online_laboratory_with_options_async(laboratory_id, request, headers, runtime)

    def push_all_experiment_with_options(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.PushAllExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.PushAllExperimentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushAllExperiment',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}/action/pushall',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.PushAllExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_all_experiment_with_options_async(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.PushAllExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.PushAllExperimentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushAllExperiment',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}/action/pushall',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.PushAllExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_all_experiment(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.PushAllExperimentRequest,
    ) -> pai_rec_service_20221213_models.PushAllExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_all_experiment_with_options(experiment_id, request, headers, runtime)

    async def push_all_experiment_async(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.PushAllExperimentRequest,
    ) -> pai_rec_service_20221213_models.PushAllExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.push_all_experiment_with_options_async(experiment_id, request, headers, runtime)

    def report_abmetric_group_with_options(
        self,
        abmetric_group_id: str,
        request: pai_rec_service_20221213_models.ReportABMetricGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ReportABMetricGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.base_experiment_id):
            body['BaseExperimentId'] = request.base_experiment_id
        if not UtilClient.is_unset(request.dimension_fields):
            body['DimensionFields'] = request.dimension_fields
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.experiment_group_id):
            body['ExperimentGroupId'] = request.experiment_group_id
        if not UtilClient.is_unset(request.experiment_ids):
            body['ExperimentIds'] = request.experiment_ids
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.report_type):
            body['ReportType'] = request.report_type
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.time_statistics_method):
            body['TimeStatisticsMethod'] = request.time_statistics_method
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReportABMetricGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/abmetricgroups/{OpenApiUtilClient.get_encode_param(abmetric_group_id)}/action/report',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ReportABMetricGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_abmetric_group_with_options_async(
        self,
        abmetric_group_id: str,
        request: pai_rec_service_20221213_models.ReportABMetricGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ReportABMetricGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.base_experiment_id):
            body['BaseExperimentId'] = request.base_experiment_id
        if not UtilClient.is_unset(request.dimension_fields):
            body['DimensionFields'] = request.dimension_fields
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.experiment_group_id):
            body['ExperimentGroupId'] = request.experiment_group_id
        if not UtilClient.is_unset(request.experiment_ids):
            body['ExperimentIds'] = request.experiment_ids
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.report_type):
            body['ReportType'] = request.report_type
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.time_statistics_method):
            body['TimeStatisticsMethod'] = request.time_statistics_method
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReportABMetricGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/abmetricgroups/{OpenApiUtilClient.get_encode_param(abmetric_group_id)}/action/report',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ReportABMetricGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_abmetric_group(
        self,
        abmetric_group_id: str,
        request: pai_rec_service_20221213_models.ReportABMetricGroupRequest,
    ) -> pai_rec_service_20221213_models.ReportABMetricGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.report_abmetric_group_with_options(abmetric_group_id, request, headers, runtime)

    async def report_abmetric_group_async(
        self,
        abmetric_group_id: str,
        request: pai_rec_service_20221213_models.ReportABMetricGroupRequest,
    ) -> pai_rec_service_20221213_models.ReportABMetricGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.report_abmetric_group_with_options_async(abmetric_group_id, request, headers, runtime)

    def sync_feature_consistency_check_job_replay_log_with_options(
        self,
        request: pai_rec_service_20221213_models.SyncFeatureConsistencyCheckJobReplayLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.SyncFeatureConsistencyCheckJobReplayLogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.context_features):
            body['ContextFeatures'] = request.context_features
        if not UtilClient.is_unset(request.feature_consistency_check_job_config_id):
            body['FeatureConsistencyCheckJobConfigId'] = request.feature_consistency_check_job_config_id
        if not UtilClient.is_unset(request.generated_features):
            body['GeneratedFeatures'] = request.generated_features
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.log_item_id):
            body['LogItemId'] = request.log_item_id
        if not UtilClient.is_unset(request.log_request_id):
            body['LogRequestId'] = request.log_request_id
        if not UtilClient.is_unset(request.log_request_time):
            body['LogRequestTime'] = request.log_request_time
        if not UtilClient.is_unset(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not UtilClient.is_unset(request.raw_features):
            body['RawFeatures'] = request.raw_features
        if not UtilClient.is_unset(request.scene_name):
            body['SceneName'] = request.scene_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SyncFeatureConsistencyCheckJobReplayLog',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/featureconsistencycheck/jobs/action/syncreplaylog',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.SyncFeatureConsistencyCheckJobReplayLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_feature_consistency_check_job_replay_log_with_options_async(
        self,
        request: pai_rec_service_20221213_models.SyncFeatureConsistencyCheckJobReplayLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.SyncFeatureConsistencyCheckJobReplayLogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.context_features):
            body['ContextFeatures'] = request.context_features
        if not UtilClient.is_unset(request.feature_consistency_check_job_config_id):
            body['FeatureConsistencyCheckJobConfigId'] = request.feature_consistency_check_job_config_id
        if not UtilClient.is_unset(request.generated_features):
            body['GeneratedFeatures'] = request.generated_features
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.log_item_id):
            body['LogItemId'] = request.log_item_id
        if not UtilClient.is_unset(request.log_request_id):
            body['LogRequestId'] = request.log_request_id
        if not UtilClient.is_unset(request.log_request_time):
            body['LogRequestTime'] = request.log_request_time
        if not UtilClient.is_unset(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not UtilClient.is_unset(request.raw_features):
            body['RawFeatures'] = request.raw_features
        if not UtilClient.is_unset(request.scene_name):
            body['SceneName'] = request.scene_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SyncFeatureConsistencyCheckJobReplayLog',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/featureconsistencycheck/jobs/action/syncreplaylog',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.SyncFeatureConsistencyCheckJobReplayLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_feature_consistency_check_job_replay_log(
        self,
        request: pai_rec_service_20221213_models.SyncFeatureConsistencyCheckJobReplayLogRequest,
    ) -> pai_rec_service_20221213_models.SyncFeatureConsistencyCheckJobReplayLogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.sync_feature_consistency_check_job_replay_log_with_options(request, headers, runtime)

    async def sync_feature_consistency_check_job_replay_log_async(
        self,
        request: pai_rec_service_20221213_models.SyncFeatureConsistencyCheckJobReplayLogRequest,
    ) -> pai_rec_service_20221213_models.SyncFeatureConsistencyCheckJobReplayLogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.sync_feature_consistency_check_job_replay_log_with_options_async(request, headers, runtime)

    def terminate_feature_consistency_check_job_with_options(
        self,
        feature_consistency_check_job_id: str,
        request: pai_rec_service_20221213_models.TerminateFeatureConsistencyCheckJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.TerminateFeatureConsistencyCheckJobResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TerminateFeatureConsistencyCheckJob',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/featureconsistencycheck/jobs/{OpenApiUtilClient.get_encode_param(feature_consistency_check_job_id)}/action/terminate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.TerminateFeatureConsistencyCheckJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def terminate_feature_consistency_check_job_with_options_async(
        self,
        feature_consistency_check_job_id: str,
        request: pai_rec_service_20221213_models.TerminateFeatureConsistencyCheckJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.TerminateFeatureConsistencyCheckJobResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TerminateFeatureConsistencyCheckJob',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/featureconsistencycheck/jobs/{OpenApiUtilClient.get_encode_param(feature_consistency_check_job_id)}/action/terminate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.TerminateFeatureConsistencyCheckJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def terminate_feature_consistency_check_job(
        self,
        feature_consistency_check_job_id: str,
        request: pai_rec_service_20221213_models.TerminateFeatureConsistencyCheckJobRequest,
    ) -> pai_rec_service_20221213_models.TerminateFeatureConsistencyCheckJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.terminate_feature_consistency_check_job_with_options(feature_consistency_check_job_id, request, headers, runtime)

    async def terminate_feature_consistency_check_job_async(
        self,
        feature_consistency_check_job_id: str,
        request: pai_rec_service_20221213_models.TerminateFeatureConsistencyCheckJobRequest,
    ) -> pai_rec_service_20221213_models.TerminateFeatureConsistencyCheckJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.terminate_feature_consistency_check_job_with_options_async(feature_consistency_check_job_id, request, headers, runtime)

    def update_abmetric_with_options(
        self,
        abmetric_id: str,
        request: pai_rec_service_20221213_models.UpdateABMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateABMetricResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.definition):
            body['Definition'] = request.definition
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.left_metric_id):
            body['LeftMetricId'] = request.left_metric_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.realtime):
            body['Realtime'] = request.realtime
        if not UtilClient.is_unset(request.result_resource_id):
            body['ResultResourceId'] = request.result_resource_id
        if not UtilClient.is_unset(request.right_metric_id):
            body['RightMetricId'] = request.right_metric_id
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.statistics_cycle):
            body['StatisticsCycle'] = request.statistics_cycle
        if not UtilClient.is_unset(request.table_meta_id):
            body['TableMetaId'] = request.table_meta_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateABMetric',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/abmetrics/{OpenApiUtilClient.get_encode_param(abmetric_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateABMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_abmetric_with_options_async(
        self,
        abmetric_id: str,
        request: pai_rec_service_20221213_models.UpdateABMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateABMetricResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.definition):
            body['Definition'] = request.definition
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.left_metric_id):
            body['LeftMetricId'] = request.left_metric_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.realtime):
            body['Realtime'] = request.realtime
        if not UtilClient.is_unset(request.result_resource_id):
            body['ResultResourceId'] = request.result_resource_id
        if not UtilClient.is_unset(request.right_metric_id):
            body['RightMetricId'] = request.right_metric_id
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.statistics_cycle):
            body['StatisticsCycle'] = request.statistics_cycle
        if not UtilClient.is_unset(request.table_meta_id):
            body['TableMetaId'] = request.table_meta_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateABMetric',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/abmetrics/{OpenApiUtilClient.get_encode_param(abmetric_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateABMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_abmetric(
        self,
        abmetric_id: str,
        request: pai_rec_service_20221213_models.UpdateABMetricRequest,
    ) -> pai_rec_service_20221213_models.UpdateABMetricResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_abmetric_with_options(abmetric_id, request, headers, runtime)

    async def update_abmetric_async(
        self,
        abmetric_id: str,
        request: pai_rec_service_20221213_models.UpdateABMetricRequest,
    ) -> pai_rec_service_20221213_models.UpdateABMetricResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_abmetric_with_options_async(abmetric_id, request, headers, runtime)

    def update_abmetric_group_with_options(
        self,
        abmetric_group_id: str,
        request: pai_rec_service_20221213_models.UpdateABMetricGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateABMetricGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.abmetric_ids):
            body['ABMetricIds'] = request.abmetric_ids
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.realtime):
            body['Realtime'] = request.realtime
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateABMetricGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/abmetricgroups/{OpenApiUtilClient.get_encode_param(abmetric_group_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateABMetricGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_abmetric_group_with_options_async(
        self,
        abmetric_group_id: str,
        request: pai_rec_service_20221213_models.UpdateABMetricGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateABMetricGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.abmetric_ids):
            body['ABMetricIds'] = request.abmetric_ids
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.realtime):
            body['Realtime'] = request.realtime
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateABMetricGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/abmetricgroups/{OpenApiUtilClient.get_encode_param(abmetric_group_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateABMetricGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_abmetric_group(
        self,
        abmetric_group_id: str,
        request: pai_rec_service_20221213_models.UpdateABMetricGroupRequest,
    ) -> pai_rec_service_20221213_models.UpdateABMetricGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_abmetric_group_with_options(abmetric_group_id, request, headers, runtime)

    async def update_abmetric_group_async(
        self,
        abmetric_group_id: str,
        request: pai_rec_service_20221213_models.UpdateABMetricGroupRequest,
    ) -> pai_rec_service_20221213_models.UpdateABMetricGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_abmetric_group_with_options_async(abmetric_group_id, request, headers, runtime)

    def update_crowd_with_options(
        self,
        crowd_id: str,
        request: pai_rec_service_20221213_models.UpdateCrowdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateCrowdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCrowd',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/crowds/{OpenApiUtilClient.get_encode_param(crowd_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateCrowdResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_crowd_with_options_async(
        self,
        crowd_id: str,
        request: pai_rec_service_20221213_models.UpdateCrowdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateCrowdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCrowd',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/crowds/{OpenApiUtilClient.get_encode_param(crowd_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateCrowdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_crowd(
        self,
        crowd_id: str,
        request: pai_rec_service_20221213_models.UpdateCrowdRequest,
    ) -> pai_rec_service_20221213_models.UpdateCrowdResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_crowd_with_options(crowd_id, request, headers, runtime)

    async def update_crowd_async(
        self,
        crowd_id: str,
        request: pai_rec_service_20221213_models.UpdateCrowdRequest,
    ) -> pai_rec_service_20221213_models.UpdateCrowdResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_crowd_with_options_async(crowd_id, request, headers, runtime)

    def update_experiment_with_options(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.UpdateExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateExperimentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.flow_percent):
            body['FlowPercent'] = request.flow_percent
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateExperiment',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_experiment_with_options_async(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.UpdateExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateExperimentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.flow_percent):
            body['FlowPercent'] = request.flow_percent
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateExperiment',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_experiment(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.UpdateExperimentRequest,
    ) -> pai_rec_service_20221213_models.UpdateExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_experiment_with_options(experiment_id, request, headers, runtime)

    async def update_experiment_async(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.UpdateExperimentRequest,
    ) -> pai_rec_service_20221213_models.UpdateExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_experiment_with_options_async(experiment_id, request, headers, runtime)

    def update_experiment_group_with_options(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.UpdateExperimentGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateExperimentGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.crowd_id):
            body['CrowdId'] = request.crowd_id
        if not UtilClient.is_unset(request.crowd_target_type):
            body['CrowdTargetType'] = request.crowd_target_type
        if not UtilClient.is_unset(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.distribution_time_duration):
            body['DistributionTimeDuration'] = request.distribution_time_duration
        if not UtilClient.is_unset(request.distribution_type):
            body['DistributionType'] = request.distribution_type
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.layer_id):
            body['LayerId'] = request.layer_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.need_aa):
            body['NeedAA'] = request.need_aa
        if not UtilClient.is_unset(request.random_flow):
            body['RandomFlow'] = request.random_flow
        if not UtilClient.is_unset(request.reservced_buckets):
            body['ReservcedBuckets'] = request.reservced_buckets
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateExperimentGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experimentgroups/{OpenApiUtilClient.get_encode_param(experiment_group_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateExperimentGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_experiment_group_with_options_async(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.UpdateExperimentGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateExperimentGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.crowd_id):
            body['CrowdId'] = request.crowd_id
        if not UtilClient.is_unset(request.crowd_target_type):
            body['CrowdTargetType'] = request.crowd_target_type
        if not UtilClient.is_unset(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.distribution_time_duration):
            body['DistributionTimeDuration'] = request.distribution_time_duration
        if not UtilClient.is_unset(request.distribution_type):
            body['DistributionType'] = request.distribution_type
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.layer_id):
            body['LayerId'] = request.layer_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.need_aa):
            body['NeedAA'] = request.need_aa
        if not UtilClient.is_unset(request.random_flow):
            body['RandomFlow'] = request.random_flow
        if not UtilClient.is_unset(request.reservced_buckets):
            body['ReservcedBuckets'] = request.reservced_buckets
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateExperimentGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/experimentgroups/{OpenApiUtilClient.get_encode_param(experiment_group_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateExperimentGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_experiment_group(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.UpdateExperimentGroupRequest,
    ) -> pai_rec_service_20221213_models.UpdateExperimentGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_experiment_group_with_options(experiment_group_id, request, headers, runtime)

    async def update_experiment_group_async(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.UpdateExperimentGroupRequest,
    ) -> pai_rec_service_20221213_models.UpdateExperimentGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_experiment_group_with_options_async(experiment_group_id, request, headers, runtime)

    def update_feature_consistency_check_job_config_with_options(
        self,
        feature_consistency_check_job_config_id: str,
        request: pai_rec_service_20221213_models.UpdateFeatureConsistencyCheckJobConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateFeatureConsistencyCheckJobConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.compare_feature):
            body['CompareFeature'] = request.compare_feature
        if not UtilClient.is_unset(request.eas_service_name):
            body['EasServiceName'] = request.eas_service_name
        if not UtilClient.is_unset(request.easy_rec_package_path):
            body['EasyRecPackagePath'] = request.easy_rec_package_path
        if not UtilClient.is_unset(request.easy_rec_version):
            body['EasyRecVersion'] = request.easy_rec_version
        if not UtilClient.is_unset(request.feature_display_exclude):
            body['FeatureDisplayExclude'] = request.feature_display_exclude
        if not UtilClient.is_unset(request.feature_landing_resource_id):
            body['FeatureLandingResourceId'] = request.feature_landing_resource_id
        if not UtilClient.is_unset(request.feature_priority):
            body['FeaturePriority'] = request.feature_priority
        if not UtilClient.is_unset(request.feature_store_item_id):
            body['FeatureStoreItemId'] = request.feature_store_item_id
        if not UtilClient.is_unset(request.feature_store_model_id):
            body['FeatureStoreModelId'] = request.feature_store_model_id
        if not UtilClient.is_unset(request.feature_store_project_id):
            body['FeatureStoreProjectId'] = request.feature_store_project_id
        if not UtilClient.is_unset(request.feature_store_project_name):
            body['FeatureStoreProjectName'] = request.feature_store_project_name
        if not UtilClient.is_unset(request.feature_store_seq_feature_view):
            body['FeatureStoreSeqFeatureView'] = request.feature_store_seq_feature_view
        if not UtilClient.is_unset(request.feature_store_user_id):
            body['FeatureStoreUserId'] = request.feature_store_user_id
        if not UtilClient.is_unset(request.fg_jar_version):
            body['FgJarVersion'] = request.fg_jar_version
        if not UtilClient.is_unset(request.fg_json_file_name):
            body['FgJsonFileName'] = request.fg_json_file_name
        if not UtilClient.is_unset(request.generate_zip):
            body['GenerateZip'] = request.generate_zip
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_use_feature_store):
            body['IsUseFeatureStore'] = request.is_use_feature_store
        if not UtilClient.is_unset(request.item_id_field):
            body['ItemIdField'] = request.item_id_field
        if not UtilClient.is_unset(request.item_table):
            body['ItemTable'] = request.item_table
        if not UtilClient.is_unset(request.item_table_partition_field):
            body['ItemTablePartitionField'] = request.item_table_partition_field
        if not UtilClient.is_unset(request.item_table_partition_field_format):
            body['ItemTablePartitionFieldFormat'] = request.item_table_partition_field_format
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.oss_resource_id):
            body['OssResourceId'] = request.oss_resource_id
        if not UtilClient.is_unset(request.sample_rate):
            body['SampleRate'] = request.sample_rate
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.user_id_field):
            body['UserIdField'] = request.user_id_field
        if not UtilClient.is_unset(request.user_table):
            body['UserTable'] = request.user_table
        if not UtilClient.is_unset(request.user_table_partition_field):
            body['UserTablePartitionField'] = request.user_table_partition_field
        if not UtilClient.is_unset(request.user_table_partition_field_format):
            body['UserTablePartitionFieldFormat'] = request.user_table_partition_field_format
        if not UtilClient.is_unset(request.workflow_name):
            body['WorkflowName'] = request.workflow_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFeatureConsistencyCheckJobConfig',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/featureconsistencycheck/jobconfigs/{OpenApiUtilClient.get_encode_param(feature_consistency_check_job_config_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateFeatureConsistencyCheckJobConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_feature_consistency_check_job_config_with_options_async(
        self,
        feature_consistency_check_job_config_id: str,
        request: pai_rec_service_20221213_models.UpdateFeatureConsistencyCheckJobConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateFeatureConsistencyCheckJobConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.compare_feature):
            body['CompareFeature'] = request.compare_feature
        if not UtilClient.is_unset(request.eas_service_name):
            body['EasServiceName'] = request.eas_service_name
        if not UtilClient.is_unset(request.easy_rec_package_path):
            body['EasyRecPackagePath'] = request.easy_rec_package_path
        if not UtilClient.is_unset(request.easy_rec_version):
            body['EasyRecVersion'] = request.easy_rec_version
        if not UtilClient.is_unset(request.feature_display_exclude):
            body['FeatureDisplayExclude'] = request.feature_display_exclude
        if not UtilClient.is_unset(request.feature_landing_resource_id):
            body['FeatureLandingResourceId'] = request.feature_landing_resource_id
        if not UtilClient.is_unset(request.feature_priority):
            body['FeaturePriority'] = request.feature_priority
        if not UtilClient.is_unset(request.feature_store_item_id):
            body['FeatureStoreItemId'] = request.feature_store_item_id
        if not UtilClient.is_unset(request.feature_store_model_id):
            body['FeatureStoreModelId'] = request.feature_store_model_id
        if not UtilClient.is_unset(request.feature_store_project_id):
            body['FeatureStoreProjectId'] = request.feature_store_project_id
        if not UtilClient.is_unset(request.feature_store_project_name):
            body['FeatureStoreProjectName'] = request.feature_store_project_name
        if not UtilClient.is_unset(request.feature_store_seq_feature_view):
            body['FeatureStoreSeqFeatureView'] = request.feature_store_seq_feature_view
        if not UtilClient.is_unset(request.feature_store_user_id):
            body['FeatureStoreUserId'] = request.feature_store_user_id
        if not UtilClient.is_unset(request.fg_jar_version):
            body['FgJarVersion'] = request.fg_jar_version
        if not UtilClient.is_unset(request.fg_json_file_name):
            body['FgJsonFileName'] = request.fg_json_file_name
        if not UtilClient.is_unset(request.generate_zip):
            body['GenerateZip'] = request.generate_zip
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_use_feature_store):
            body['IsUseFeatureStore'] = request.is_use_feature_store
        if not UtilClient.is_unset(request.item_id_field):
            body['ItemIdField'] = request.item_id_field
        if not UtilClient.is_unset(request.item_table):
            body['ItemTable'] = request.item_table
        if not UtilClient.is_unset(request.item_table_partition_field):
            body['ItemTablePartitionField'] = request.item_table_partition_field
        if not UtilClient.is_unset(request.item_table_partition_field_format):
            body['ItemTablePartitionFieldFormat'] = request.item_table_partition_field_format
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.oss_resource_id):
            body['OssResourceId'] = request.oss_resource_id
        if not UtilClient.is_unset(request.sample_rate):
            body['SampleRate'] = request.sample_rate
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.user_id_field):
            body['UserIdField'] = request.user_id_field
        if not UtilClient.is_unset(request.user_table):
            body['UserTable'] = request.user_table
        if not UtilClient.is_unset(request.user_table_partition_field):
            body['UserTablePartitionField'] = request.user_table_partition_field
        if not UtilClient.is_unset(request.user_table_partition_field_format):
            body['UserTablePartitionFieldFormat'] = request.user_table_partition_field_format
        if not UtilClient.is_unset(request.workflow_name):
            body['WorkflowName'] = request.workflow_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFeatureConsistencyCheckJobConfig',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/featureconsistencycheck/jobconfigs/{OpenApiUtilClient.get_encode_param(feature_consistency_check_job_config_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateFeatureConsistencyCheckJobConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_feature_consistency_check_job_config(
        self,
        feature_consistency_check_job_config_id: str,
        request: pai_rec_service_20221213_models.UpdateFeatureConsistencyCheckJobConfigRequest,
    ) -> pai_rec_service_20221213_models.UpdateFeatureConsistencyCheckJobConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_feature_consistency_check_job_config_with_options(feature_consistency_check_job_config_id, request, headers, runtime)

    async def update_feature_consistency_check_job_config_async(
        self,
        feature_consistency_check_job_config_id: str,
        request: pai_rec_service_20221213_models.UpdateFeatureConsistencyCheckJobConfigRequest,
    ) -> pai_rec_service_20221213_models.UpdateFeatureConsistencyCheckJobConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_feature_consistency_check_job_config_with_options_async(feature_consistency_check_job_config_id, request, headers, runtime)

    def update_instance_resource_with_options(
        self,
        instance_id: str,
        resource_id: str,
        request: pai_rec_service_20221213_models.UpdateInstanceResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateInstanceResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstanceResource',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/resources/{OpenApiUtilClient.get_encode_param(resource_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateInstanceResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_resource_with_options_async(
        self,
        instance_id: str,
        resource_id: str,
        request: pai_rec_service_20221213_models.UpdateInstanceResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateInstanceResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstanceResource',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/resources/{OpenApiUtilClient.get_encode_param(resource_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateInstanceResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_resource(
        self,
        instance_id: str,
        resource_id: str,
        request: pai_rec_service_20221213_models.UpdateInstanceResourceRequest,
    ) -> pai_rec_service_20221213_models.UpdateInstanceResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_resource_with_options(instance_id, resource_id, request, headers, runtime)

    async def update_instance_resource_async(
        self,
        instance_id: str,
        resource_id: str,
        request: pai_rec_service_20221213_models.UpdateInstanceResourceRequest,
    ) -> pai_rec_service_20221213_models.UpdateInstanceResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_instance_resource_with_options_async(instance_id, resource_id, request, headers, runtime)

    def update_laboratory_with_options(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.UpdateLaboratoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateLaboratoryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bucket_count):
            body['BucketCount'] = request.bucket_count
        if not UtilClient.is_unset(request.bucket_type):
            body['BucketType'] = request.bucket_type
        if not UtilClient.is_unset(request.buckets):
            body['Buckets'] = request.buckets
        if not UtilClient.is_unset(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLaboratory',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/laboratories/{OpenApiUtilClient.get_encode_param(laboratory_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateLaboratoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_laboratory_with_options_async(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.UpdateLaboratoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateLaboratoryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bucket_count):
            body['BucketCount'] = request.bucket_count
        if not UtilClient.is_unset(request.bucket_type):
            body['BucketType'] = request.bucket_type
        if not UtilClient.is_unset(request.buckets):
            body['Buckets'] = request.buckets
        if not UtilClient.is_unset(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLaboratory',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/laboratories/{OpenApiUtilClient.get_encode_param(laboratory_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateLaboratoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_laboratory(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.UpdateLaboratoryRequest,
    ) -> pai_rec_service_20221213_models.UpdateLaboratoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_laboratory_with_options(laboratory_id, request, headers, runtime)

    async def update_laboratory_async(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.UpdateLaboratoryRequest,
    ) -> pai_rec_service_20221213_models.UpdateLaboratoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_laboratory_with_options_async(laboratory_id, request, headers, runtime)

    def update_layer_with_options(
        self,
        layer_id: str,
        request: pai_rec_service_20221213_models.UpdateLayerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateLayerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLayer',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/layers/{OpenApiUtilClient.get_encode_param(layer_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_layer_with_options_async(
        self,
        layer_id: str,
        request: pai_rec_service_20221213_models.UpdateLayerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateLayerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLayer',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/layers/{OpenApiUtilClient.get_encode_param(layer_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_layer(
        self,
        layer_id: str,
        request: pai_rec_service_20221213_models.UpdateLayerRequest,
    ) -> pai_rec_service_20221213_models.UpdateLayerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_layer_with_options(layer_id, request, headers, runtime)

    async def update_layer_async(
        self,
        layer_id: str,
        request: pai_rec_service_20221213_models.UpdateLayerRequest,
    ) -> pai_rec_service_20221213_models.UpdateLayerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_layer_with_options_async(layer_id, request, headers, runtime)

    def update_param_with_options(
        self,
        param_id: str,
        request: pai_rec_service_20221213_models.UpdateParamRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateParamResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateParam',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/params/{OpenApiUtilClient.get_encode_param(param_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateParamResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_param_with_options_async(
        self,
        param_id: str,
        request: pai_rec_service_20221213_models.UpdateParamRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateParamResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateParam',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/params/{OpenApiUtilClient.get_encode_param(param_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateParamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_param(
        self,
        param_id: str,
        request: pai_rec_service_20221213_models.UpdateParamRequest,
    ) -> pai_rec_service_20221213_models.UpdateParamResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_param_with_options(param_id, request, headers, runtime)

    async def update_param_async(
        self,
        param_id: str,
        request: pai_rec_service_20221213_models.UpdateParamRequest,
    ) -> pai_rec_service_20221213_models.UpdateParamResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_param_with_options_async(param_id, request, headers, runtime)

    def update_scene_with_options(
        self,
        scene_id: str,
        request: pai_rec_service_20221213_models.UpdateSceneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateSceneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.flows):
            body['Flows'] = request.flows
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateScene',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_scene_with_options_async(
        self,
        scene_id: str,
        request: pai_rec_service_20221213_models.UpdateSceneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateSceneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.flows):
            body['Flows'] = request.flows
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateScene',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/scenes/{OpenApiUtilClient.get_encode_param(scene_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_scene(
        self,
        scene_id: str,
        request: pai_rec_service_20221213_models.UpdateSceneRequest,
    ) -> pai_rec_service_20221213_models.UpdateSceneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_scene_with_options(scene_id, request, headers, runtime)

    async def update_scene_async(
        self,
        scene_id: str,
        request: pai_rec_service_20221213_models.UpdateSceneRequest,
    ) -> pai_rec_service_20221213_models.UpdateSceneResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_scene_with_options_async(scene_id, request, headers, runtime)

    def update_table_meta_with_options(
        self,
        table_meta_id: str,
        request: pai_rec_service_20221213_models.UpdateTableMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateTableMetaResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.fields):
            body['Fields'] = request.fields
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module):
            body['Module'] = request.module
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTableMeta',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/tablemetas/{OpenApiUtilClient.get_encode_param(table_meta_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateTableMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_table_meta_with_options_async(
        self,
        table_meta_id: str,
        request: pai_rec_service_20221213_models.UpdateTableMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateTableMetaResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.fields):
            body['Fields'] = request.fields
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module):
            body['Module'] = request.module
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTableMeta',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/tablemetas/{OpenApiUtilClient.get_encode_param(table_meta_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateTableMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_table_meta(
        self,
        table_meta_id: str,
        request: pai_rec_service_20221213_models.UpdateTableMetaRequest,
    ) -> pai_rec_service_20221213_models.UpdateTableMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_table_meta_with_options(table_meta_id, request, headers, runtime)

    async def update_table_meta_async(
        self,
        table_meta_id: str,
        request: pai_rec_service_20221213_models.UpdateTableMetaRequest,
    ) -> pai_rec_service_20221213_models.UpdateTableMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_table_meta_with_options_async(table_meta_id, request, headers, runtime)

    def upload_recommendation_data_with_options(
        self,
        request: pai_rec_service_20221213_models.UploadRecommendationDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UploadRecommendationDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.data_type):
            body['DataType'] = request.data_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadRecommendationData',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/recommendationdata/action/upload',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UploadRecommendationDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_recommendation_data_with_options_async(
        self,
        request: pai_rec_service_20221213_models.UploadRecommendationDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UploadRecommendationDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.data_type):
            body['DataType'] = request.data_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadRecommendationData',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/recommendationdata/action/upload',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UploadRecommendationDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_recommendation_data(
        self,
        request: pai_rec_service_20221213_models.UploadRecommendationDataRequest,
    ) -> pai_rec_service_20221213_models.UploadRecommendationDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upload_recommendation_data_with_options(request, headers, runtime)

    async def upload_recommendation_data_async(
        self,
        request: pai_rec_service_20221213_models.UploadRecommendationDataRequest,
    ) -> pai_rec_service_20221213_models.UploadRecommendationDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upload_recommendation_data_with_options_async(request, headers, runtime)
