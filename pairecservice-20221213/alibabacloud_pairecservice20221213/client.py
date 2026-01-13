# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_pairecservice20221213 import models as main_models
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def apply_engine_config_with_options(
        self,
        engine_config_id: str,
        request: main_models.ApplyEngineConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ApplyEngineConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyEngineConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/engineconfigs/{DaraURL.percent_encode(engine_config_id)}/action/apply',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyEngineConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_engine_config_with_options_async(
        self,
        engine_config_id: str,
        request: main_models.ApplyEngineConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ApplyEngineConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyEngineConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/engineconfigs/{DaraURL.percent_encode(engine_config_id)}/action/apply',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyEngineConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_engine_config(
        self,
        engine_config_id: str,
        request: main_models.ApplyEngineConfigRequest,
    ) -> main_models.ApplyEngineConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.apply_engine_config_with_options(engine_config_id, request, headers, runtime)

    async def apply_engine_config_async(
        self,
        engine_config_id: str,
        request: main_models.ApplyEngineConfigRequest,
    ) -> main_models.ApplyEngineConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.apply_engine_config_with_options_async(engine_config_id, request, headers, runtime)

    def backflow_feature_consistency_check_job_data_with_options(
        self,
        request: main_models.BackflowFeatureConsistencyCheckJobDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BackflowFeatureConsistencyCheckJobDataResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.feature_consistency_check_job_config_id):
            body['FeatureConsistencyCheckJobConfigId'] = request.feature_consistency_check_job_config_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.item_features):
            body['ItemFeatures'] = request.item_features
        if not DaraCore.is_null(request.log_item_id):
            body['LogItemId'] = request.log_item_id
        if not DaraCore.is_null(request.log_request_id):
            body['LogRequestId'] = request.log_request_id
        if not DaraCore.is_null(request.log_request_time):
            body['LogRequestTime'] = request.log_request_time
        if not DaraCore.is_null(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not DaraCore.is_null(request.scene_name):
            body['SceneName'] = request.scene_name
        if not DaraCore.is_null(request.scores):
            body['Scores'] = request.scores
        if not DaraCore.is_null(request.service_name):
            body['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.user_features):
            body['UserFeatures'] = request.user_features
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BackflowFeatureConsistencyCheckJobData',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/featureconsistencycheck/jobs/action/backflowdata',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BackflowFeatureConsistencyCheckJobDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def backflow_feature_consistency_check_job_data_with_options_async(
        self,
        request: main_models.BackflowFeatureConsistencyCheckJobDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BackflowFeatureConsistencyCheckJobDataResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.feature_consistency_check_job_config_id):
            body['FeatureConsistencyCheckJobConfigId'] = request.feature_consistency_check_job_config_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.item_features):
            body['ItemFeatures'] = request.item_features
        if not DaraCore.is_null(request.log_item_id):
            body['LogItemId'] = request.log_item_id
        if not DaraCore.is_null(request.log_request_id):
            body['LogRequestId'] = request.log_request_id
        if not DaraCore.is_null(request.log_request_time):
            body['LogRequestTime'] = request.log_request_time
        if not DaraCore.is_null(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not DaraCore.is_null(request.scene_name):
            body['SceneName'] = request.scene_name
        if not DaraCore.is_null(request.scores):
            body['Scores'] = request.scores
        if not DaraCore.is_null(request.service_name):
            body['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.user_features):
            body['UserFeatures'] = request.user_features
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BackflowFeatureConsistencyCheckJobData',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/featureconsistencycheck/jobs/action/backflowdata',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BackflowFeatureConsistencyCheckJobDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def backflow_feature_consistency_check_job_data(
        self,
        request: main_models.BackflowFeatureConsistencyCheckJobDataRequest,
    ) -> main_models.BackflowFeatureConsistencyCheckJobDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.backflow_feature_consistency_check_job_data_with_options(request, headers, runtime)

    async def backflow_feature_consistency_check_job_data_async(
        self,
        request: main_models.BackflowFeatureConsistencyCheckJobDataRequest,
    ) -> main_models.BackflowFeatureConsistencyCheckJobDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.backflow_feature_consistency_check_job_data_with_options_async(request, headers, runtime)

    def change_recall_management_service_version_with_options(
        self,
        recall_management_service_id: str,
        request: main_models.ChangeRecallManagementServiceVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChangeRecallManagementServiceVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.recall_management_service_version_id):
            body['RecallManagementServiceVersionId'] = request.recall_management_service_version_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeRecallManagementServiceVersion',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices/{DaraURL.percent_encode(recall_management_service_id)}/action/changeversion',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeRecallManagementServiceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_recall_management_service_version_with_options_async(
        self,
        recall_management_service_id: str,
        request: main_models.ChangeRecallManagementServiceVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChangeRecallManagementServiceVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.recall_management_service_version_id):
            body['RecallManagementServiceVersionId'] = request.recall_management_service_version_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeRecallManagementServiceVersion',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices/{DaraURL.percent_encode(recall_management_service_id)}/action/changeversion',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeRecallManagementServiceVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_recall_management_service_version(
        self,
        recall_management_service_id: str,
        request: main_models.ChangeRecallManagementServiceVersionRequest,
    ) -> main_models.ChangeRecallManagementServiceVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.change_recall_management_service_version_with_options(recall_management_service_id, request, headers, runtime)

    async def change_recall_management_service_version_async(
        self,
        recall_management_service_id: str,
        request: main_models.ChangeRecallManagementServiceVersionRequest,
    ) -> main_models.ChangeRecallManagementServiceVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.change_recall_management_service_version_with_options_async(recall_management_service_id, request, headers, runtime)

    def check_instance_resources_with_options(
        self,
        instance_id: str,
        request: main_models.CheckInstanceResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckInstanceResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.uri):
            body['Uri'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckInstanceResources',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/action/checkresources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckInstanceResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_instance_resources_with_options_async(
        self,
        instance_id: str,
        request: main_models.CheckInstanceResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckInstanceResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.uri):
            body['Uri'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckInstanceResources',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/action/checkresources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckInstanceResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_instance_resources(
        self,
        instance_id: str,
        request: main_models.CheckInstanceResourcesRequest,
    ) -> main_models.CheckInstanceResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.check_instance_resources_with_options(instance_id, request, headers, runtime)

    async def check_instance_resources_async(
        self,
        instance_id: str,
        request: main_models.CheckInstanceResourcesRequest,
    ) -> main_models.CheckInstanceResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.check_instance_resources_with_options_async(instance_id, request, headers, runtime)

    def check_traffic_control_task_expression_with_options(
        self,
        request: main_models.CheckTrafficControlTaskExpressionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckTrafficControlTaskExpressionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expression):
            query['Expression'] = request.expression
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.table_meta_id):
            query['TableMetaId'] = request.table_meta_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckTrafficControlTaskExpression',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltasks/action/checkexpression',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckTrafficControlTaskExpressionResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_traffic_control_task_expression_with_options_async(
        self,
        request: main_models.CheckTrafficControlTaskExpressionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckTrafficControlTaskExpressionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expression):
            query['Expression'] = request.expression
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.table_meta_id):
            query['TableMetaId'] = request.table_meta_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckTrafficControlTaskExpression',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltasks/action/checkexpression',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckTrafficControlTaskExpressionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_traffic_control_task_expression(
        self,
        request: main_models.CheckTrafficControlTaskExpressionRequest,
    ) -> main_models.CheckTrafficControlTaskExpressionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.check_traffic_control_task_expression_with_options(request, headers, runtime)

    async def check_traffic_control_task_expression_async(
        self,
        request: main_models.CheckTrafficControlTaskExpressionRequest,
    ) -> main_models.CheckTrafficControlTaskExpressionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.check_traffic_control_task_expression_with_options_async(request, headers, runtime)

    def clone_engine_config_with_options(
        self,
        engine_config_id: str,
        request: main_models.CloneEngineConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CloneEngineConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config_value):
            body['ConfigValue'] = request.config_value
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CloneEngineConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/engineconfigs/{DaraURL.percent_encode(engine_config_id)}/action/clone',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloneEngineConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_engine_config_with_options_async(
        self,
        engine_config_id: str,
        request: main_models.CloneEngineConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CloneEngineConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config_value):
            body['ConfigValue'] = request.config_value
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CloneEngineConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/engineconfigs/{DaraURL.percent_encode(engine_config_id)}/action/clone',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloneEngineConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_engine_config(
        self,
        engine_config_id: str,
        request: main_models.CloneEngineConfigRequest,
    ) -> main_models.CloneEngineConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.clone_engine_config_with_options(engine_config_id, request, headers, runtime)

    async def clone_engine_config_async(
        self,
        engine_config_id: str,
        request: main_models.CloneEngineConfigRequest,
    ) -> main_models.CloneEngineConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.clone_engine_config_with_options_async(engine_config_id, request, headers, runtime)

    def clone_experiment_with_options(
        self,
        experiment_id: str,
        request: main_models.CloneExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CloneExperimentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CloneExperiment',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(experiment_id)}/action/clone',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloneExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_experiment_with_options_async(
        self,
        experiment_id: str,
        request: main_models.CloneExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CloneExperimentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CloneExperiment',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(experiment_id)}/action/clone',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloneExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_experiment(
        self,
        experiment_id: str,
        request: main_models.CloneExperimentRequest,
    ) -> main_models.CloneExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.clone_experiment_with_options(experiment_id, request, headers, runtime)

    async def clone_experiment_async(
        self,
        experiment_id: str,
        request: main_models.CloneExperimentRequest,
    ) -> main_models.CloneExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.clone_experiment_with_options_async(experiment_id, request, headers, runtime)

    def clone_experiment_group_with_options(
        self,
        experiment_group_id: str,
        request: main_models.CloneExperimentGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CloneExperimentGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.layer_id):
            body['LayerId'] = request.layer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CloneExperimentGroup',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experimentgroups/{DaraURL.percent_encode(experiment_group_id)}/action/clone',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloneExperimentGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_experiment_group_with_options_async(
        self,
        experiment_group_id: str,
        request: main_models.CloneExperimentGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CloneExperimentGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.layer_id):
            body['LayerId'] = request.layer_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CloneExperimentGroup',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experimentgroups/{DaraURL.percent_encode(experiment_group_id)}/action/clone',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloneExperimentGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_experiment_group(
        self,
        experiment_group_id: str,
        request: main_models.CloneExperimentGroupRequest,
    ) -> main_models.CloneExperimentGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.clone_experiment_group_with_options(experiment_group_id, request, headers, runtime)

    async def clone_experiment_group_async(
        self,
        experiment_group_id: str,
        request: main_models.CloneExperimentGroupRequest,
    ) -> main_models.CloneExperimentGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.clone_experiment_group_with_options_async(experiment_group_id, request, headers, runtime)

    def clone_feature_consistency_check_job_config_with_options(
        self,
        source_feature_consistency_check_job_config_id: str,
        request: main_models.CloneFeatureConsistencyCheckJobConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CloneFeatureConsistencyCheckJobConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CloneFeatureConsistencyCheckJobConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/featureconsistencycheck/jobconfigs/{DaraURL.percent_encode(source_feature_consistency_check_job_config_id)}/action/clone',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloneFeatureConsistencyCheckJobConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_feature_consistency_check_job_config_with_options_async(
        self,
        source_feature_consistency_check_job_config_id: str,
        request: main_models.CloneFeatureConsistencyCheckJobConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CloneFeatureConsistencyCheckJobConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CloneFeatureConsistencyCheckJobConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/featureconsistencycheck/jobconfigs/{DaraURL.percent_encode(source_feature_consistency_check_job_config_id)}/action/clone',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloneFeatureConsistencyCheckJobConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_feature_consistency_check_job_config(
        self,
        source_feature_consistency_check_job_config_id: str,
        request: main_models.CloneFeatureConsistencyCheckJobConfigRequest,
    ) -> main_models.CloneFeatureConsistencyCheckJobConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.clone_feature_consistency_check_job_config_with_options(source_feature_consistency_check_job_config_id, request, headers, runtime)

    async def clone_feature_consistency_check_job_config_async(
        self,
        source_feature_consistency_check_job_config_id: str,
        request: main_models.CloneFeatureConsistencyCheckJobConfigRequest,
    ) -> main_models.CloneFeatureConsistencyCheckJobConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.clone_feature_consistency_check_job_config_with_options_async(source_feature_consistency_check_job_config_id, request, headers, runtime)

    def clone_laboratory_with_options(
        self,
        laboratory_id: str,
        request: main_models.CloneLaboratoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CloneLaboratoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.clone_experiment_group):
            body['CloneExperimentGroup'] = request.clone_experiment_group
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CloneLaboratory',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/laboratories/{DaraURL.percent_encode(laboratory_id)}/action/clone',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloneLaboratoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_laboratory_with_options_async(
        self,
        laboratory_id: str,
        request: main_models.CloneLaboratoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CloneLaboratoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.clone_experiment_group):
            body['CloneExperimentGroup'] = request.clone_experiment_group
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CloneLaboratory',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/laboratories/{DaraURL.percent_encode(laboratory_id)}/action/clone',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloneLaboratoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_laboratory(
        self,
        laboratory_id: str,
        request: main_models.CloneLaboratoryRequest,
    ) -> main_models.CloneLaboratoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.clone_laboratory_with_options(laboratory_id, request, headers, runtime)

    async def clone_laboratory_async(
        self,
        laboratory_id: str,
        request: main_models.CloneLaboratoryRequest,
    ) -> main_models.CloneLaboratoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.clone_laboratory_with_options_async(laboratory_id, request, headers, runtime)

    def clone_traffic_control_task_with_options(
        self,
        traffic_control_task_id: str,
        request: main_models.CloneTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CloneTrafficControlTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CloneTrafficControlTask',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltasks/{DaraURL.percent_encode(traffic_control_task_id)}/action/clone',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloneTrafficControlTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_traffic_control_task_with_options_async(
        self,
        traffic_control_task_id: str,
        request: main_models.CloneTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CloneTrafficControlTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CloneTrafficControlTask',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltasks/{DaraURL.percent_encode(traffic_control_task_id)}/action/clone',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloneTrafficControlTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_traffic_control_task(
        self,
        traffic_control_task_id: str,
        request: main_models.CloneTrafficControlTaskRequest,
    ) -> main_models.CloneTrafficControlTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.clone_traffic_control_task_with_options(traffic_control_task_id, request, headers, runtime)

    async def clone_traffic_control_task_async(
        self,
        traffic_control_task_id: str,
        request: main_models.CloneTrafficControlTaskRequest,
    ) -> main_models.CloneTrafficControlTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.clone_traffic_control_task_with_options_async(traffic_control_task_id, request, headers, runtime)

    def compare_sample_consistency_job_with_options(
        self,
        sample_consistency_job_id: str,
        request: main_models.CompareSampleConsistencyJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CompareSampleConsistencyJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CompareSampleConsistencyJob',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sampleconsistencyjobs/{DaraURL.percent_encode(sample_consistency_job_id)}/action/compare',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompareSampleConsistencyJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def compare_sample_consistency_job_with_options_async(
        self,
        sample_consistency_job_id: str,
        request: main_models.CompareSampleConsistencyJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CompareSampleConsistencyJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CompareSampleConsistencyJob',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sampleconsistencyjobs/{DaraURL.percent_encode(sample_consistency_job_id)}/action/compare',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompareSampleConsistencyJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def compare_sample_consistency_job(
        self,
        sample_consistency_job_id: str,
        request: main_models.CompareSampleConsistencyJobRequest,
    ) -> main_models.CompareSampleConsistencyJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.compare_sample_consistency_job_with_options(sample_consistency_job_id, request, headers, runtime)

    async def compare_sample_consistency_job_async(
        self,
        sample_consistency_job_id: str,
        request: main_models.CompareSampleConsistencyJobRequest,
    ) -> main_models.CompareSampleConsistencyJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.compare_sample_consistency_job_with_options_async(sample_consistency_job_id, request, headers, runtime)

    def create_abmetric_with_options(
        self,
        request: main_models.CreateABMetricRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateABMetricResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.definition):
            body['Definition'] = request.definition
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.left_metric_id):
            body['LeftMetricId'] = request.left_metric_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.operator):
            body['Operator'] = request.operator
        if not DaraCore.is_null(request.realtime):
            body['Realtime'] = request.realtime
        if not DaraCore.is_null(request.result_resource_id):
            body['ResultResourceId'] = request.result_resource_id
        if not DaraCore.is_null(request.right_metric_id):
            body['RightMetricId'] = request.right_metric_id
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.statistics_cycle):
            body['StatisticsCycle'] = request.statistics_cycle
        if not DaraCore.is_null(request.table_meta_id):
            body['TableMetaId'] = request.table_meta_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateABMetric',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/abmetrics',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateABMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_abmetric_with_options_async(
        self,
        request: main_models.CreateABMetricRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateABMetricResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.definition):
            body['Definition'] = request.definition
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.left_metric_id):
            body['LeftMetricId'] = request.left_metric_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.operator):
            body['Operator'] = request.operator
        if not DaraCore.is_null(request.realtime):
            body['Realtime'] = request.realtime
        if not DaraCore.is_null(request.result_resource_id):
            body['ResultResourceId'] = request.result_resource_id
        if not DaraCore.is_null(request.right_metric_id):
            body['RightMetricId'] = request.right_metric_id
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.statistics_cycle):
            body['StatisticsCycle'] = request.statistics_cycle
        if not DaraCore.is_null(request.table_meta_id):
            body['TableMetaId'] = request.table_meta_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateABMetric',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/abmetrics',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateABMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_abmetric(
        self,
        request: main_models.CreateABMetricRequest,
    ) -> main_models.CreateABMetricResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_abmetric_with_options(request, headers, runtime)

    async def create_abmetric_async(
        self,
        request: main_models.CreateABMetricRequest,
    ) -> main_models.CreateABMetricResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_abmetric_with_options_async(request, headers, runtime)

    def create_abmetric_group_with_options(
        self,
        request: main_models.CreateABMetricGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateABMetricGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.abmetric_ids):
            body['ABMetricIds'] = request.abmetric_ids
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.realtime):
            body['Realtime'] = request.realtime
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateABMetricGroup',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/abmetricgroups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateABMetricGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_abmetric_group_with_options_async(
        self,
        request: main_models.CreateABMetricGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateABMetricGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.abmetric_ids):
            body['ABMetricIds'] = request.abmetric_ids
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.realtime):
            body['Realtime'] = request.realtime
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateABMetricGroup',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/abmetricgroups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateABMetricGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_abmetric_group(
        self,
        request: main_models.CreateABMetricGroupRequest,
    ) -> main_models.CreateABMetricGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_abmetric_group_with_options(request, headers, runtime)

    async def create_abmetric_group_async(
        self,
        request: main_models.CreateABMetricGroupRequest,
    ) -> main_models.CreateABMetricGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_abmetric_group_with_options_async(request, headers, runtime)

    def create_calculation_jobs_with_options(
        self,
        request: main_models.CreateCalculationJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCalculationJobsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.abmetric_ids):
            body['ABMetricIds'] = request.abmetric_ids
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCalculationJobs',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/batch/calculationjobs/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCalculationJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_calculation_jobs_with_options_async(
        self,
        request: main_models.CreateCalculationJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCalculationJobsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.abmetric_ids):
            body['ABMetricIds'] = request.abmetric_ids
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCalculationJobs',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/batch/calculationjobs/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCalculationJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_calculation_jobs(
        self,
        request: main_models.CreateCalculationJobsRequest,
    ) -> main_models.CreateCalculationJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_calculation_jobs_with_options(request, headers, runtime)

    async def create_calculation_jobs_async(
        self,
        request: main_models.CreateCalculationJobsRequest,
    ) -> main_models.CreateCalculationJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_calculation_jobs_with_options_async(request, headers, runtime)

    def create_crowd_with_options(
        self,
        request: main_models.CreateCrowdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCrowdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.label):
            body['Label'] = request.label
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.source):
            body['Source'] = request.source
        if not DaraCore.is_null(request.users):
            body['Users'] = request.users
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCrowd',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/crowds',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCrowdResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_crowd_with_options_async(
        self,
        request: main_models.CreateCrowdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCrowdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.label):
            body['Label'] = request.label
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.source):
            body['Source'] = request.source
        if not DaraCore.is_null(request.users):
            body['Users'] = request.users
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCrowd',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/crowds',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCrowdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_crowd(
        self,
        request: main_models.CreateCrowdRequest,
    ) -> main_models.CreateCrowdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_crowd_with_options(request, headers, runtime)

    async def create_crowd_async(
        self,
        request: main_models.CreateCrowdRequest,
    ) -> main_models.CreateCrowdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_crowd_with_options_async(request, headers, runtime)

    def create_engine_config_with_options(
        self,
        request: main_models.CreateEngineConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateEngineConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config_value):
            body['ConfigValue'] = request.config_value
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEngineConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/engineconfigs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEngineConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_engine_config_with_options_async(
        self,
        request: main_models.CreateEngineConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateEngineConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config_value):
            body['ConfigValue'] = request.config_value
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEngineConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/engineconfigs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEngineConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_engine_config(
        self,
        request: main_models.CreateEngineConfigRequest,
    ) -> main_models.CreateEngineConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_engine_config_with_options(request, headers, runtime)

    async def create_engine_config_async(
        self,
        request: main_models.CreateEngineConfigRequest,
    ) -> main_models.CreateEngineConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_engine_config_with_options_async(request, headers, runtime)

    def create_experiment_with_options(
        self,
        request: main_models.CreateExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateExperimentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not DaraCore.is_null(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.experiment_group_id):
            body['ExperimentGroupId'] = request.experiment_group_id
        if not DaraCore.is_null(request.flow_percent):
            body['FlowPercent'] = request.flow_percent
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateExperiment',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_experiment_with_options_async(
        self,
        request: main_models.CreateExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateExperimentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not DaraCore.is_null(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.experiment_group_id):
            body['ExperimentGroupId'] = request.experiment_group_id
        if not DaraCore.is_null(request.flow_percent):
            body['FlowPercent'] = request.flow_percent
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateExperiment',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_experiment(
        self,
        request: main_models.CreateExperimentRequest,
    ) -> main_models.CreateExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_experiment_with_options(request, headers, runtime)

    async def create_experiment_async(
        self,
        request: main_models.CreateExperimentRequest,
    ) -> main_models.CreateExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_experiment_with_options_async(request, headers, runtime)

    def create_experiment_group_with_options(
        self,
        request: main_models.CreateExperimentGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateExperimentGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.crowd_id):
            body['CrowdId'] = request.crowd_id
        if not DaraCore.is_null(request.crowd_target_type):
            body['CrowdTargetType'] = request.crowd_target_type
        if not DaraCore.is_null(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not DaraCore.is_null(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.distribution_time_duration):
            body['DistributionTimeDuration'] = request.distribution_time_duration
        if not DaraCore.is_null(request.distribution_type):
            body['DistributionType'] = request.distribution_type
        if not DaraCore.is_null(request.filter):
            body['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.layer_id):
            body['LayerId'] = request.layer_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.need_aa):
            body['NeedAA'] = request.need_aa
        if not DaraCore.is_null(request.random_flow):
            body['RandomFlow'] = request.random_flow
        if not DaraCore.is_null(request.reserved_buckets):
            body['ReservedBuckets'] = request.reserved_buckets
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateExperimentGroup',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experimentgroups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExperimentGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_experiment_group_with_options_async(
        self,
        request: main_models.CreateExperimentGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateExperimentGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.crowd_id):
            body['CrowdId'] = request.crowd_id
        if not DaraCore.is_null(request.crowd_target_type):
            body['CrowdTargetType'] = request.crowd_target_type
        if not DaraCore.is_null(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not DaraCore.is_null(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.distribution_time_duration):
            body['DistributionTimeDuration'] = request.distribution_time_duration
        if not DaraCore.is_null(request.distribution_type):
            body['DistributionType'] = request.distribution_type
        if not DaraCore.is_null(request.filter):
            body['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.layer_id):
            body['LayerId'] = request.layer_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.need_aa):
            body['NeedAA'] = request.need_aa
        if not DaraCore.is_null(request.random_flow):
            body['RandomFlow'] = request.random_flow
        if not DaraCore.is_null(request.reserved_buckets):
            body['ReservedBuckets'] = request.reserved_buckets
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateExperimentGroup',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experimentgroups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExperimentGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_experiment_group(
        self,
        request: main_models.CreateExperimentGroupRequest,
    ) -> main_models.CreateExperimentGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_experiment_group_with_options(request, headers, runtime)

    async def create_experiment_group_async(
        self,
        request: main_models.CreateExperimentGroupRequest,
    ) -> main_models.CreateExperimentGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_experiment_group_with_options_async(request, headers, runtime)

    def create_feature_consistency_check_job_with_options(
        self,
        request: main_models.CreateFeatureConsistencyCheckJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateFeatureConsistencyCheckJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.feature_consistency_check_job_config_id):
            body['FeatureConsistencyCheckJobConfigId'] = request.feature_consistency_check_job_config_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sampling_duration):
            body['SamplingDuration'] = request.sampling_duration
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFeatureConsistencyCheckJob',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/featureconsistencycheck/jobs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFeatureConsistencyCheckJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_feature_consistency_check_job_with_options_async(
        self,
        request: main_models.CreateFeatureConsistencyCheckJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateFeatureConsistencyCheckJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.feature_consistency_check_job_config_id):
            body['FeatureConsistencyCheckJobConfigId'] = request.feature_consistency_check_job_config_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sampling_duration):
            body['SamplingDuration'] = request.sampling_duration
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFeatureConsistencyCheckJob',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/featureconsistencycheck/jobs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFeatureConsistencyCheckJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_feature_consistency_check_job(
        self,
        request: main_models.CreateFeatureConsistencyCheckJobRequest,
    ) -> main_models.CreateFeatureConsistencyCheckJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_feature_consistency_check_job_with_options(request, headers, runtime)

    async def create_feature_consistency_check_job_async(
        self,
        request: main_models.CreateFeatureConsistencyCheckJobRequest,
    ) -> main_models.CreateFeatureConsistencyCheckJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_feature_consistency_check_job_with_options_async(request, headers, runtime)

    def create_feature_consistency_check_job_config_with_options(
        self,
        request: main_models.CreateFeatureConsistencyCheckJobConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateFeatureConsistencyCheckJobConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.compare_feature):
            body['CompareFeature'] = request.compare_feature
        if not DaraCore.is_null(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_mount_path):
            body['DatasetMountPath'] = request.dataset_mount_path
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.dataset_type):
            body['DatasetType'] = request.dataset_type
        if not DaraCore.is_null(request.dataset_uri):
            body['DatasetUri'] = request.dataset_uri
        if not DaraCore.is_null(request.default_route):
            body['DefaultRoute'] = request.default_route
        if not DaraCore.is_null(request.eas_service_name):
            body['EasServiceName'] = request.eas_service_name
        if not DaraCore.is_null(request.easy_rec_package_path):
            body['EasyRecPackagePath'] = request.easy_rec_package_path
        if not DaraCore.is_null(request.easy_rec_version):
            body['EasyRecVersion'] = request.easy_rec_version
        if not DaraCore.is_null(request.feature_display_exclude):
            body['FeatureDisplayExclude'] = request.feature_display_exclude
        if not DaraCore.is_null(request.feature_landing_resource_id):
            body['FeatureLandingResourceId'] = request.feature_landing_resource_id
        if not DaraCore.is_null(request.feature_priority):
            body['FeaturePriority'] = request.feature_priority
        if not DaraCore.is_null(request.feature_store_item_id):
            body['FeatureStoreItemId'] = request.feature_store_item_id
        if not DaraCore.is_null(request.feature_store_model_id):
            body['FeatureStoreModelId'] = request.feature_store_model_id
        if not DaraCore.is_null(request.feature_store_project_id):
            body['FeatureStoreProjectId'] = request.feature_store_project_id
        if not DaraCore.is_null(request.feature_store_project_name):
            body['FeatureStoreProjectName'] = request.feature_store_project_name
        if not DaraCore.is_null(request.feature_store_seq_feature_view):
            body['FeatureStoreSeqFeatureView'] = request.feature_store_seq_feature_view
        if not DaraCore.is_null(request.feature_store_user_id):
            body['FeatureStoreUserId'] = request.feature_store_user_id
        if not DaraCore.is_null(request.fg_jar_version):
            body['FgJarVersion'] = request.fg_jar_version
        if not DaraCore.is_null(request.fg_json_file_name):
            body['FgJsonFileName'] = request.fg_json_file_name
        if not DaraCore.is_null(request.generate_zip):
            body['GenerateZip'] = request.generate_zip
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.item_id_field):
            body['ItemIdField'] = request.item_id_field
        if not DaraCore.is_null(request.item_table):
            body['ItemTable'] = request.item_table
        if not DaraCore.is_null(request.item_table_partition_field):
            body['ItemTablePartitionField'] = request.item_table_partition_field
        if not DaraCore.is_null(request.item_table_partition_field_format):
            body['ItemTablePartitionFieldFormat'] = request.item_table_partition_field_format
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.oss_resource_id):
            body['OssResourceId'] = request.oss_resource_id
        if not DaraCore.is_null(request.predict_worker_count):
            body['PredictWorkerCount'] = request.predict_worker_count
        if not DaraCore.is_null(request.predict_worker_cpu):
            body['PredictWorkerCpu'] = request.predict_worker_cpu
        if not DaraCore.is_null(request.predict_worker_memory):
            body['PredictWorkerMemory'] = request.predict_worker_memory
        if not DaraCore.is_null(request.resource_config):
            body['ResourceConfig'] = request.resource_config
        if not DaraCore.is_null(request.sample_rate):
            body['SampleRate'] = request.sample_rate
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.security_group_id):
            body['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.service_id):
            body['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.switch_id):
            body['SwitchId'] = request.switch_id
        if not DaraCore.is_null(request.use_feature_store):
            body['UseFeatureStore'] = request.use_feature_store
        if not DaraCore.is_null(request.user_id_field):
            body['UserIdField'] = request.user_id_field
        if not DaraCore.is_null(request.user_table):
            body['UserTable'] = request.user_table
        if not DaraCore.is_null(request.user_table_partition_field):
            body['UserTablePartitionField'] = request.user_table_partition_field
        if not DaraCore.is_null(request.user_table_partition_field_format):
            body['UserTablePartitionFieldFormat'] = request.user_table_partition_field_format
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.workflow_name):
            body['WorkflowName'] = request.workflow_name
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFeatureConsistencyCheckJobConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/featureconsistencycheck/jobconfigs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFeatureConsistencyCheckJobConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_feature_consistency_check_job_config_with_options_async(
        self,
        request: main_models.CreateFeatureConsistencyCheckJobConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateFeatureConsistencyCheckJobConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.compare_feature):
            body['CompareFeature'] = request.compare_feature
        if not DaraCore.is_null(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_mount_path):
            body['DatasetMountPath'] = request.dataset_mount_path
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.dataset_type):
            body['DatasetType'] = request.dataset_type
        if not DaraCore.is_null(request.dataset_uri):
            body['DatasetUri'] = request.dataset_uri
        if not DaraCore.is_null(request.default_route):
            body['DefaultRoute'] = request.default_route
        if not DaraCore.is_null(request.eas_service_name):
            body['EasServiceName'] = request.eas_service_name
        if not DaraCore.is_null(request.easy_rec_package_path):
            body['EasyRecPackagePath'] = request.easy_rec_package_path
        if not DaraCore.is_null(request.easy_rec_version):
            body['EasyRecVersion'] = request.easy_rec_version
        if not DaraCore.is_null(request.feature_display_exclude):
            body['FeatureDisplayExclude'] = request.feature_display_exclude
        if not DaraCore.is_null(request.feature_landing_resource_id):
            body['FeatureLandingResourceId'] = request.feature_landing_resource_id
        if not DaraCore.is_null(request.feature_priority):
            body['FeaturePriority'] = request.feature_priority
        if not DaraCore.is_null(request.feature_store_item_id):
            body['FeatureStoreItemId'] = request.feature_store_item_id
        if not DaraCore.is_null(request.feature_store_model_id):
            body['FeatureStoreModelId'] = request.feature_store_model_id
        if not DaraCore.is_null(request.feature_store_project_id):
            body['FeatureStoreProjectId'] = request.feature_store_project_id
        if not DaraCore.is_null(request.feature_store_project_name):
            body['FeatureStoreProjectName'] = request.feature_store_project_name
        if not DaraCore.is_null(request.feature_store_seq_feature_view):
            body['FeatureStoreSeqFeatureView'] = request.feature_store_seq_feature_view
        if not DaraCore.is_null(request.feature_store_user_id):
            body['FeatureStoreUserId'] = request.feature_store_user_id
        if not DaraCore.is_null(request.fg_jar_version):
            body['FgJarVersion'] = request.fg_jar_version
        if not DaraCore.is_null(request.fg_json_file_name):
            body['FgJsonFileName'] = request.fg_json_file_name
        if not DaraCore.is_null(request.generate_zip):
            body['GenerateZip'] = request.generate_zip
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.item_id_field):
            body['ItemIdField'] = request.item_id_field
        if not DaraCore.is_null(request.item_table):
            body['ItemTable'] = request.item_table
        if not DaraCore.is_null(request.item_table_partition_field):
            body['ItemTablePartitionField'] = request.item_table_partition_field
        if not DaraCore.is_null(request.item_table_partition_field_format):
            body['ItemTablePartitionFieldFormat'] = request.item_table_partition_field_format
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.oss_resource_id):
            body['OssResourceId'] = request.oss_resource_id
        if not DaraCore.is_null(request.predict_worker_count):
            body['PredictWorkerCount'] = request.predict_worker_count
        if not DaraCore.is_null(request.predict_worker_cpu):
            body['PredictWorkerCpu'] = request.predict_worker_cpu
        if not DaraCore.is_null(request.predict_worker_memory):
            body['PredictWorkerMemory'] = request.predict_worker_memory
        if not DaraCore.is_null(request.resource_config):
            body['ResourceConfig'] = request.resource_config
        if not DaraCore.is_null(request.sample_rate):
            body['SampleRate'] = request.sample_rate
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.security_group_id):
            body['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.service_id):
            body['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.switch_id):
            body['SwitchId'] = request.switch_id
        if not DaraCore.is_null(request.use_feature_store):
            body['UseFeatureStore'] = request.use_feature_store
        if not DaraCore.is_null(request.user_id_field):
            body['UserIdField'] = request.user_id_field
        if not DaraCore.is_null(request.user_table):
            body['UserTable'] = request.user_table
        if not DaraCore.is_null(request.user_table_partition_field):
            body['UserTablePartitionField'] = request.user_table_partition_field
        if not DaraCore.is_null(request.user_table_partition_field_format):
            body['UserTablePartitionFieldFormat'] = request.user_table_partition_field_format
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.workflow_name):
            body['WorkflowName'] = request.workflow_name
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFeatureConsistencyCheckJobConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/featureconsistencycheck/jobconfigs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFeatureConsistencyCheckJobConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_feature_consistency_check_job_config(
        self,
        request: main_models.CreateFeatureConsistencyCheckJobConfigRequest,
    ) -> main_models.CreateFeatureConsistencyCheckJobConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_feature_consistency_check_job_config_with_options(request, headers, runtime)

    async def create_feature_consistency_check_job_config_async(
        self,
        request: main_models.CreateFeatureConsistencyCheckJobConfigRequest,
    ) -> main_models.CreateFeatureConsistencyCheckJobConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_feature_consistency_check_job_config_with_options_async(request, headers, runtime)

    def create_instance_resource_with_options(
        self,
        instance_id: str,
        request: main_models.CreateInstanceResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category):
            body['Category'] = request.category
        if not DaraCore.is_null(request.group):
            body['Group'] = request.group
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.uri):
            body['Uri'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceResource',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/resources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_resource_with_options_async(
        self,
        instance_id: str,
        request: main_models.CreateInstanceResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category):
            body['Category'] = request.category
        if not DaraCore.is_null(request.group):
            body['Group'] = request.group
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.uri):
            body['Uri'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceResource',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/resources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_resource(
        self,
        instance_id: str,
        request: main_models.CreateInstanceResourceRequest,
    ) -> main_models.CreateInstanceResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_instance_resource_with_options(instance_id, request, headers, runtime)

    async def create_instance_resource_async(
        self,
        instance_id: str,
        request: main_models.CreateInstanceResourceRequest,
    ) -> main_models.CreateInstanceResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_instance_resource_with_options_async(instance_id, request, headers, runtime)

    def create_laboratory_with_options(
        self,
        request: main_models.CreateLaboratoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLaboratoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.bucket_count):
            body['BucketCount'] = request.bucket_count
        if not DaraCore.is_null(request.bucket_type):
            body['BucketType'] = request.bucket_type
        if not DaraCore.is_null(request.buckets):
            body['Buckets'] = request.buckets
        if not DaraCore.is_null(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not DaraCore.is_null(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.filter):
            body['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLaboratory',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/laboratories',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLaboratoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_laboratory_with_options_async(
        self,
        request: main_models.CreateLaboratoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLaboratoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.bucket_count):
            body['BucketCount'] = request.bucket_count
        if not DaraCore.is_null(request.bucket_type):
            body['BucketType'] = request.bucket_type
        if not DaraCore.is_null(request.buckets):
            body['Buckets'] = request.buckets
        if not DaraCore.is_null(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not DaraCore.is_null(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.filter):
            body['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLaboratory',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/laboratories',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLaboratoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_laboratory(
        self,
        request: main_models.CreateLaboratoryRequest,
    ) -> main_models.CreateLaboratoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_laboratory_with_options(request, headers, runtime)

    async def create_laboratory_async(
        self,
        request: main_models.CreateLaboratoryRequest,
    ) -> main_models.CreateLaboratoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_laboratory_with_options_async(request, headers, runtime)

    def create_layer_with_options(
        self,
        request: main_models.CreateLayerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLayerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.laboratory_id):
            body['LaboratoryId'] = request.laboratory_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLayer',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/layers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_layer_with_options_async(
        self,
        request: main_models.CreateLayerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLayerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.laboratory_id):
            body['LaboratoryId'] = request.laboratory_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLayer',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/layers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_layer(
        self,
        request: main_models.CreateLayerRequest,
    ) -> main_models.CreateLayerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_layer_with_options(request, headers, runtime)

    async def create_layer_async(
        self,
        request: main_models.CreateLayerRequest,
    ) -> main_models.CreateLayerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_layer_with_options_async(request, headers, runtime)

    def create_param_with_options(
        self,
        request: main_models.CreateParamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateParamResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.value):
            body['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateParam',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/params',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateParamResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_param_with_options_async(
        self,
        request: main_models.CreateParamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateParamResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.value):
            body['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateParam',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/params',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateParamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_param(
        self,
        request: main_models.CreateParamRequest,
    ) -> main_models.CreateParamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_param_with_options(request, headers, runtime)

    async def create_param_async(
        self,
        request: main_models.CreateParamRequest,
    ) -> main_models.CreateParamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_param_with_options_async(request, headers, runtime)

    def create_recall_management_config_with_options(
        self,
        request: main_models.CreateRecallManagementConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRecallManagementConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_configs):
            body['NetworkConfigs'] = request.network_configs
        if not DaraCore.is_null(request.password):
            body['Password'] = request.password
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRecallManagementConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementconfigs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRecallManagementConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_recall_management_config_with_options_async(
        self,
        request: main_models.CreateRecallManagementConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRecallManagementConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_configs):
            body['NetworkConfigs'] = request.network_configs
        if not DaraCore.is_null(request.password):
            body['Password'] = request.password
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRecallManagementConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementconfigs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRecallManagementConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_recall_management_config(
        self,
        request: main_models.CreateRecallManagementConfigRequest,
    ) -> main_models.CreateRecallManagementConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_recall_management_config_with_options(request, headers, runtime)

    async def create_recall_management_config_async(
        self,
        request: main_models.CreateRecallManagementConfigRequest,
    ) -> main_models.CreateRecallManagementConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_recall_management_config_with_options_async(request, headers, runtime)

    def create_recall_management_service_with_options(
        self,
        request: main_models.CreateRecallManagementServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRecallManagementServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRecallManagementService',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRecallManagementServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_recall_management_service_with_options_async(
        self,
        request: main_models.CreateRecallManagementServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRecallManagementServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRecallManagementService',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRecallManagementServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_recall_management_service(
        self,
        request: main_models.CreateRecallManagementServiceRequest,
    ) -> main_models.CreateRecallManagementServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_recall_management_service_with_options(request, headers, runtime)

    async def create_recall_management_service_async(
        self,
        request: main_models.CreateRecallManagementServiceRequest,
    ) -> main_models.CreateRecallManagementServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_recall_management_service_with_options_async(request, headers, runtime)

    def create_recall_management_service_version_with_options(
        self,
        recall_management_service_id: str,
        request: main_models.CreateRecallManagementServiceVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRecallManagementServiceVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.configs):
            body['Configs'] = request.configs
        if not DaraCore.is_null(request.source_recall_management_service_version_id):
            body['SourceRecallManagementServiceVersionId'] = request.source_recall_management_service_version_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRecallManagementServiceVersion',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices/{DaraURL.percent_encode(recall_management_service_id)}/versions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRecallManagementServiceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_recall_management_service_version_with_options_async(
        self,
        recall_management_service_id: str,
        request: main_models.CreateRecallManagementServiceVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRecallManagementServiceVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.configs):
            body['Configs'] = request.configs
        if not DaraCore.is_null(request.source_recall_management_service_version_id):
            body['SourceRecallManagementServiceVersionId'] = request.source_recall_management_service_version_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRecallManagementServiceVersion',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices/{DaraURL.percent_encode(recall_management_service_id)}/versions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRecallManagementServiceVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_recall_management_service_version(
        self,
        recall_management_service_id: str,
        request: main_models.CreateRecallManagementServiceVersionRequest,
    ) -> main_models.CreateRecallManagementServiceVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_recall_management_service_version_with_options(recall_management_service_id, request, headers, runtime)

    async def create_recall_management_service_version_async(
        self,
        recall_management_service_id: str,
        request: main_models.CreateRecallManagementServiceVersionRequest,
    ) -> main_models.CreateRecallManagementServiceVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_recall_management_service_version_with_options_async(recall_management_service_id, request, headers, runtime)

    def create_recall_management_service_version_config_with_options(
        self,
        recall_management_service_id: str,
        recall_management_service_version_id: str,
        request: main_models.CreateRecallManagementServiceVersionConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRecallManagementServiceVersionConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config_type):
            body['ConfigType'] = request.config_type
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.merge_config):
            body['MergeConfig'] = request.merge_config
        if not DaraCore.is_null(request.recall_config):
            body['RecallConfig'] = request.recall_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRecallManagementServiceVersionConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices/{DaraURL.percent_encode(recall_management_service_id)}/versions/{DaraURL.percent_encode(recall_management_service_version_id)}/configs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRecallManagementServiceVersionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_recall_management_service_version_config_with_options_async(
        self,
        recall_management_service_id: str,
        recall_management_service_version_id: str,
        request: main_models.CreateRecallManagementServiceVersionConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRecallManagementServiceVersionConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config_type):
            body['ConfigType'] = request.config_type
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.merge_config):
            body['MergeConfig'] = request.merge_config
        if not DaraCore.is_null(request.recall_config):
            body['RecallConfig'] = request.recall_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRecallManagementServiceVersionConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices/{DaraURL.percent_encode(recall_management_service_id)}/versions/{DaraURL.percent_encode(recall_management_service_version_id)}/configs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRecallManagementServiceVersionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_recall_management_service_version_config(
        self,
        recall_management_service_id: str,
        recall_management_service_version_id: str,
        request: main_models.CreateRecallManagementServiceVersionConfigRequest,
    ) -> main_models.CreateRecallManagementServiceVersionConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_recall_management_service_version_config_with_options(recall_management_service_id, recall_management_service_version_id, request, headers, runtime)

    async def create_recall_management_service_version_config_async(
        self,
        recall_management_service_id: str,
        recall_management_service_version_id: str,
        request: main_models.CreateRecallManagementServiceVersionConfigRequest,
    ) -> main_models.CreateRecallManagementServiceVersionConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_recall_management_service_version_config_with_options_async(recall_management_service_id, recall_management_service_version_id, request, headers, runtime)

    def create_recall_management_table_with_options(
        self,
        request: main_models.CreateRecallManagementTableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRecallManagementTableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.data_source):
            body['DataSource'] = request.data_source
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.enable_data_size_fluctuation_threshold):
            body['EnableDataSizeFluctuationThreshold'] = request.enable_data_size_fluctuation_threshold
        if not DaraCore.is_null(request.enable_row_count_fluctuation_threshold):
            body['EnableRowCountFluctuationThreshold'] = request.enable_row_count_fluctuation_threshold
        if not DaraCore.is_null(request.fields):
            body['Fields'] = request.fields
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_data_size_fluctuation_threshold):
            body['MaxDataSizeFluctuationThreshold'] = request.max_data_size_fluctuation_threshold
        if not DaraCore.is_null(request.max_row_count_fluctuation_threshold):
            body['MaxRowCountFluctuationThreshold'] = request.max_row_count_fluctuation_threshold
        if not DaraCore.is_null(request.maxcompute_project_name):
            body['MaxcomputeProjectName'] = request.maxcompute_project_name
        if not DaraCore.is_null(request.maxcompute_schema):
            body['MaxcomputeSchema'] = request.maxcompute_schema
        if not DaraCore.is_null(request.maxcompute_table_name):
            body['MaxcomputeTableName'] = request.maxcompute_table_name
        if not DaraCore.is_null(request.min_data_size_fluctuation_threshold):
            body['MinDataSizeFluctuationThreshold'] = request.min_data_size_fluctuation_threshold
        if not DaraCore.is_null(request.min_row_count_fluctuation_threshold):
            body['MinRowCountFluctuationThreshold'] = request.min_row_count_fluctuation_threshold
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.recall_type):
            body['RecallType'] = request.recall_type
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRecallManagementTable',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementtables',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRecallManagementTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_recall_management_table_with_options_async(
        self,
        request: main_models.CreateRecallManagementTableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRecallManagementTableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.data_source):
            body['DataSource'] = request.data_source
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.enable_data_size_fluctuation_threshold):
            body['EnableDataSizeFluctuationThreshold'] = request.enable_data_size_fluctuation_threshold
        if not DaraCore.is_null(request.enable_row_count_fluctuation_threshold):
            body['EnableRowCountFluctuationThreshold'] = request.enable_row_count_fluctuation_threshold
        if not DaraCore.is_null(request.fields):
            body['Fields'] = request.fields
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_data_size_fluctuation_threshold):
            body['MaxDataSizeFluctuationThreshold'] = request.max_data_size_fluctuation_threshold
        if not DaraCore.is_null(request.max_row_count_fluctuation_threshold):
            body['MaxRowCountFluctuationThreshold'] = request.max_row_count_fluctuation_threshold
        if not DaraCore.is_null(request.maxcompute_project_name):
            body['MaxcomputeProjectName'] = request.maxcompute_project_name
        if not DaraCore.is_null(request.maxcompute_schema):
            body['MaxcomputeSchema'] = request.maxcompute_schema
        if not DaraCore.is_null(request.maxcompute_table_name):
            body['MaxcomputeTableName'] = request.maxcompute_table_name
        if not DaraCore.is_null(request.min_data_size_fluctuation_threshold):
            body['MinDataSizeFluctuationThreshold'] = request.min_data_size_fluctuation_threshold
        if not DaraCore.is_null(request.min_row_count_fluctuation_threshold):
            body['MinRowCountFluctuationThreshold'] = request.min_row_count_fluctuation_threshold
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.recall_type):
            body['RecallType'] = request.recall_type
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRecallManagementTable',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementtables',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRecallManagementTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_recall_management_table(
        self,
        request: main_models.CreateRecallManagementTableRequest,
    ) -> main_models.CreateRecallManagementTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_recall_management_table_with_options(request, headers, runtime)

    async def create_recall_management_table_async(
        self,
        request: main_models.CreateRecallManagementTableRequest,
    ) -> main_models.CreateRecallManagementTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_recall_management_table_with_options_async(request, headers, runtime)

    def create_resource_rule_with_options(
        self,
        request: main_models.CreateResourceRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.metric_operation_type):
            body['MetricOperationType'] = request.metric_operation_type
        if not DaraCore.is_null(request.metric_pull_info):
            body['MetricPullInfo'] = request.metric_pull_info
        if not DaraCore.is_null(request.metric_pull_period):
            body['MetricPullPeriod'] = request.metric_pull_period
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.rule_computing_definition):
            body['RuleComputingDefinition'] = request.rule_computing_definition
        if not DaraCore.is_null(request.rule_items):
            body['RuleItems'] = request.rule_items
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourceRule',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resourcerules',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_rule_with_options_async(
        self,
        request: main_models.CreateResourceRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.metric_operation_type):
            body['MetricOperationType'] = request.metric_operation_type
        if not DaraCore.is_null(request.metric_pull_info):
            body['MetricPullInfo'] = request.metric_pull_info
        if not DaraCore.is_null(request.metric_pull_period):
            body['MetricPullPeriod'] = request.metric_pull_period
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.rule_computing_definition):
            body['RuleComputingDefinition'] = request.rule_computing_definition
        if not DaraCore.is_null(request.rule_items):
            body['RuleItems'] = request.rule_items
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourceRule',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resourcerules',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_rule(
        self,
        request: main_models.CreateResourceRuleRequest,
    ) -> main_models.CreateResourceRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_resource_rule_with_options(request, headers, runtime)

    async def create_resource_rule_async(
        self,
        request: main_models.CreateResourceRuleRequest,
    ) -> main_models.CreateResourceRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_resource_rule_with_options_async(request, headers, runtime)

    def create_resource_rule_item_with_options(
        self,
        resource_rule_id: str,
        request: main_models.CreateResourceRuleItemRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceRuleItemResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_value):
            body['MaxValue'] = request.max_value
        if not DaraCore.is_null(request.min_value):
            body['MinValue'] = request.min_value
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.value):
            body['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourceRuleItem',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resourcerules/{DaraURL.percent_encode(resource_rule_id)}/items',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceRuleItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_rule_item_with_options_async(
        self,
        resource_rule_id: str,
        request: main_models.CreateResourceRuleItemRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceRuleItemResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_value):
            body['MaxValue'] = request.max_value
        if not DaraCore.is_null(request.min_value):
            body['MinValue'] = request.min_value
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.value):
            body['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourceRuleItem',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resourcerules/{DaraURL.percent_encode(resource_rule_id)}/items',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceRuleItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_rule_item(
        self,
        resource_rule_id: str,
        request: main_models.CreateResourceRuleItemRequest,
    ) -> main_models.CreateResourceRuleItemResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_resource_rule_item_with_options(resource_rule_id, request, headers, runtime)

    async def create_resource_rule_item_async(
        self,
        resource_rule_id: str,
        request: main_models.CreateResourceRuleItemRequest,
    ) -> main_models.CreateResourceRuleItemResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_resource_rule_item_with_options_async(resource_rule_id, request, headers, runtime)

    def create_sample_consistency_job_with_options(
        self,
        request: main_models.CreateSampleConsistencyJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSampleConsistencyJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.duration):
            body['Duration'] = request.duration
        if not DaraCore.is_null(request.eas_model_service_name):
            body['EasModelServiceName'] = request.eas_model_service_name
        if not DaraCore.is_null(request.feature_save_resource_id):
            body['FeatureSaveResourceId'] = request.feature_save_resource_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.item_id_field):
            body['ItemIdField'] = request.item_id_field
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.partition_field):
            body['PartitionField'] = request.partition_field
        if not DaraCore.is_null(request.partition_field_format):
            body['PartitionFieldFormat'] = request.partition_field_format
        if not DaraCore.is_null(request.request_id_field):
            body['RequestIdField'] = request.request_id_field
        if not DaraCore.is_null(request.sample_rate):
            body['SampleRate'] = request.sample_rate
        if not DaraCore.is_null(request.sample_table_name):
            body['SampleTableName'] = request.sample_table_name
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.user_id_field):
            body['UserIdField'] = request.user_id_field
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSampleConsistencyJob',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sampleconsistencyjobs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSampleConsistencyJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sample_consistency_job_with_options_async(
        self,
        request: main_models.CreateSampleConsistencyJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSampleConsistencyJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.duration):
            body['Duration'] = request.duration
        if not DaraCore.is_null(request.eas_model_service_name):
            body['EasModelServiceName'] = request.eas_model_service_name
        if not DaraCore.is_null(request.feature_save_resource_id):
            body['FeatureSaveResourceId'] = request.feature_save_resource_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.item_id_field):
            body['ItemIdField'] = request.item_id_field
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.partition_field):
            body['PartitionField'] = request.partition_field
        if not DaraCore.is_null(request.partition_field_format):
            body['PartitionFieldFormat'] = request.partition_field_format
        if not DaraCore.is_null(request.request_id_field):
            body['RequestIdField'] = request.request_id_field
        if not DaraCore.is_null(request.sample_rate):
            body['SampleRate'] = request.sample_rate
        if not DaraCore.is_null(request.sample_table_name):
            body['SampleTableName'] = request.sample_table_name
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.user_id_field):
            body['UserIdField'] = request.user_id_field
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSampleConsistencyJob',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sampleconsistencyjobs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSampleConsistencyJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sample_consistency_job(
        self,
        request: main_models.CreateSampleConsistencyJobRequest,
    ) -> main_models.CreateSampleConsistencyJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_sample_consistency_job_with_options(request, headers, runtime)

    async def create_sample_consistency_job_async(
        self,
        request: main_models.CreateSampleConsistencyJobRequest,
    ) -> main_models.CreateSampleConsistencyJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_sample_consistency_job_with_options_async(request, headers, runtime)

    def create_scene_with_options(
        self,
        request: main_models.CreateSceneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSceneResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.flows):
            body['Flows'] = request.flows
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateScene',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/scenes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scene_with_options_async(
        self,
        request: main_models.CreateSceneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSceneResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.flows):
            body['Flows'] = request.flows
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateScene',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/scenes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scene(
        self,
        request: main_models.CreateSceneRequest,
    ) -> main_models.CreateSceneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_scene_with_options(request, headers, runtime)

    async def create_scene_async(
        self,
        request: main_models.CreateSceneRequest,
    ) -> main_models.CreateSceneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_scene_with_options_async(request, headers, runtime)

    def create_sub_crowd_with_options(
        self,
        crowd_id: str,
        request: main_models.CreateSubCrowdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSubCrowdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.source):
            body['Source'] = request.source
        if not DaraCore.is_null(request.users):
            body['Users'] = request.users
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSubCrowd',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/crowds/{DaraURL.percent_encode(crowd_id)}/subcrowds',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSubCrowdResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sub_crowd_with_options_async(
        self,
        crowd_id: str,
        request: main_models.CreateSubCrowdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSubCrowdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.source):
            body['Source'] = request.source
        if not DaraCore.is_null(request.users):
            body['Users'] = request.users
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSubCrowd',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/crowds/{DaraURL.percent_encode(crowd_id)}/subcrowds',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSubCrowdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sub_crowd(
        self,
        crowd_id: str,
        request: main_models.CreateSubCrowdRequest,
    ) -> main_models.CreateSubCrowdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_sub_crowd_with_options(crowd_id, request, headers, runtime)

    async def create_sub_crowd_async(
        self,
        crowd_id: str,
        request: main_models.CreateSubCrowdRequest,
    ) -> main_models.CreateSubCrowdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_sub_crowd_with_options_async(crowd_id, request, headers, runtime)

    def create_table_meta_with_options(
        self,
        request: main_models.CreateTableMetaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTableMetaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.fields):
            body['Fields'] = request.fields
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module):
            body['Module'] = request.module
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTableMeta',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tablemetas',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTableMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_table_meta_with_options_async(
        self,
        request: main_models.CreateTableMetaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTableMetaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.fields):
            body['Fields'] = request.fields
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module):
            body['Module'] = request.module
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTableMeta',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tablemetas',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTableMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_table_meta(
        self,
        request: main_models.CreateTableMetaRequest,
    ) -> main_models.CreateTableMetaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_table_meta_with_options(request, headers, runtime)

    async def create_table_meta_async(
        self,
        request: main_models.CreateTableMetaRequest,
    ) -> main_models.CreateTableMetaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_table_meta_with_options_async(request, headers, runtime)

    def create_traffic_control_target_with_options(
        self,
        request: main_models.CreateTrafficControlTargetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTrafficControlTargetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event):
            body['Event'] = request.event
        if not DaraCore.is_null(request.item_condition_array):
            body['ItemConditionArray'] = request.item_condition_array
        if not DaraCore.is_null(request.item_condition_express):
            body['ItemConditionExpress'] = request.item_condition_express
        if not DaraCore.is_null(request.item_condition_type):
            body['ItemConditionType'] = request.item_condition_type
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.new_product_regulation):
            body['NewProductRegulation'] = request.new_product_regulation
        if not DaraCore.is_null(request.recall_name):
            body['RecallName'] = request.recall_name
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.statis_period):
            body['StatisPeriod'] = request.statis_period
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tolerance_value):
            body['ToleranceValue'] = request.tolerance_value
        if not DaraCore.is_null(request.traffic_control_task_id):
            body['TrafficControlTaskId'] = request.traffic_control_task_id
        if not DaraCore.is_null(request.value):
            body['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTrafficControlTarget',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltargets',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTrafficControlTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_traffic_control_target_with_options_async(
        self,
        request: main_models.CreateTrafficControlTargetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTrafficControlTargetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event):
            body['Event'] = request.event
        if not DaraCore.is_null(request.item_condition_array):
            body['ItemConditionArray'] = request.item_condition_array
        if not DaraCore.is_null(request.item_condition_express):
            body['ItemConditionExpress'] = request.item_condition_express
        if not DaraCore.is_null(request.item_condition_type):
            body['ItemConditionType'] = request.item_condition_type
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.new_product_regulation):
            body['NewProductRegulation'] = request.new_product_regulation
        if not DaraCore.is_null(request.recall_name):
            body['RecallName'] = request.recall_name
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.statis_period):
            body['StatisPeriod'] = request.statis_period
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tolerance_value):
            body['ToleranceValue'] = request.tolerance_value
        if not DaraCore.is_null(request.traffic_control_task_id):
            body['TrafficControlTaskId'] = request.traffic_control_task_id
        if not DaraCore.is_null(request.value):
            body['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTrafficControlTarget',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltargets',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTrafficControlTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_traffic_control_target(
        self,
        request: main_models.CreateTrafficControlTargetRequest,
    ) -> main_models.CreateTrafficControlTargetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_traffic_control_target_with_options(request, headers, runtime)

    async def create_traffic_control_target_async(
        self,
        request: main_models.CreateTrafficControlTargetRequest,
    ) -> main_models.CreateTrafficControlTargetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_traffic_control_target_with_options_async(request, headers, runtime)

    def create_traffic_control_task_with_options(
        self,
        request: main_models.CreateTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTrafficControlTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.behavior_table_meta_id):
            body['BehaviorTableMetaId'] = request.behavior_table_meta_id
        if not DaraCore.is_null(request.control_granularity):
            body['ControlGranularity'] = request.control_granularity
        if not DaraCore.is_null(request.control_logic):
            body['ControlLogic'] = request.control_logic
        if not DaraCore.is_null(request.control_type):
            body['ControlType'] = request.control_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.effective_scene_ids):
            body['EffectiveSceneIds'] = request.effective_scene_ids
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.execution_time):
            body['ExecutionTime'] = request.execution_time
        if not DaraCore.is_null(request.flink_resource_id):
            body['FlinkResourceId'] = request.flink_resource_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.item_condition_array):
            body['ItemConditionArray'] = request.item_condition_array
        if not DaraCore.is_null(request.item_condition_express):
            body['ItemConditionExpress'] = request.item_condition_express
        if not DaraCore.is_null(request.item_condition_type):
            body['ItemConditionType'] = request.item_condition_type
        if not DaraCore.is_null(request.item_table_meta_id):
            body['ItemTableMetaId'] = request.item_table_meta_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.pre_experiment_ids):
            body['PreExperimentIds'] = request.pre_experiment_ids
        if not DaraCore.is_null(request.prod_experiment_ids):
            body['ProdExperimentIds'] = request.prod_experiment_ids
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.service_id):
            body['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_ids):
            body['ServiceIds'] = request.service_ids
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.statis_behavior_condition_array):
            body['StatisBehaviorConditionArray'] = request.statis_behavior_condition_array
        if not DaraCore.is_null(request.statis_behavior_condition_express):
            body['StatisBehaviorConditionExpress'] = request.statis_behavior_condition_express
        if not DaraCore.is_null(request.statis_behavior_condition_type):
            body['StatisBehaviorConditionType'] = request.statis_behavior_condition_type
        if not DaraCore.is_null(request.traffic_control_targets):
            body['TrafficControlTargets'] = request.traffic_control_targets
        if not DaraCore.is_null(request.user_condition_array):
            body['UserConditionArray'] = request.user_condition_array
        if not DaraCore.is_null(request.user_condition_express):
            body['UserConditionExpress'] = request.user_condition_express
        if not DaraCore.is_null(request.user_condition_type):
            body['UserConditionType'] = request.user_condition_type
        if not DaraCore.is_null(request.user_table_meta_id):
            body['UserTableMetaId'] = request.user_table_meta_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTrafficControlTask',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltasks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTrafficControlTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_traffic_control_task_with_options_async(
        self,
        request: main_models.CreateTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTrafficControlTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.behavior_table_meta_id):
            body['BehaviorTableMetaId'] = request.behavior_table_meta_id
        if not DaraCore.is_null(request.control_granularity):
            body['ControlGranularity'] = request.control_granularity
        if not DaraCore.is_null(request.control_logic):
            body['ControlLogic'] = request.control_logic
        if not DaraCore.is_null(request.control_type):
            body['ControlType'] = request.control_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.effective_scene_ids):
            body['EffectiveSceneIds'] = request.effective_scene_ids
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.execution_time):
            body['ExecutionTime'] = request.execution_time
        if not DaraCore.is_null(request.flink_resource_id):
            body['FlinkResourceId'] = request.flink_resource_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.item_condition_array):
            body['ItemConditionArray'] = request.item_condition_array
        if not DaraCore.is_null(request.item_condition_express):
            body['ItemConditionExpress'] = request.item_condition_express
        if not DaraCore.is_null(request.item_condition_type):
            body['ItemConditionType'] = request.item_condition_type
        if not DaraCore.is_null(request.item_table_meta_id):
            body['ItemTableMetaId'] = request.item_table_meta_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.pre_experiment_ids):
            body['PreExperimentIds'] = request.pre_experiment_ids
        if not DaraCore.is_null(request.prod_experiment_ids):
            body['ProdExperimentIds'] = request.prod_experiment_ids
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.service_id):
            body['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_ids):
            body['ServiceIds'] = request.service_ids
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.statis_behavior_condition_array):
            body['StatisBehaviorConditionArray'] = request.statis_behavior_condition_array
        if not DaraCore.is_null(request.statis_behavior_condition_express):
            body['StatisBehaviorConditionExpress'] = request.statis_behavior_condition_express
        if not DaraCore.is_null(request.statis_behavior_condition_type):
            body['StatisBehaviorConditionType'] = request.statis_behavior_condition_type
        if not DaraCore.is_null(request.traffic_control_targets):
            body['TrafficControlTargets'] = request.traffic_control_targets
        if not DaraCore.is_null(request.user_condition_array):
            body['UserConditionArray'] = request.user_condition_array
        if not DaraCore.is_null(request.user_condition_express):
            body['UserConditionExpress'] = request.user_condition_express
        if not DaraCore.is_null(request.user_condition_type):
            body['UserConditionType'] = request.user_condition_type
        if not DaraCore.is_null(request.user_table_meta_id):
            body['UserTableMetaId'] = request.user_table_meta_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTrafficControlTask',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltasks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTrafficControlTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_traffic_control_task(
        self,
        request: main_models.CreateTrafficControlTaskRequest,
    ) -> main_models.CreateTrafficControlTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_traffic_control_task_with_options(request, headers, runtime)

    async def create_traffic_control_task_async(
        self,
        request: main_models.CreateTrafficControlTaskRequest,
    ) -> main_models.CreateTrafficControlTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_traffic_control_task_with_options_async(request, headers, runtime)

    def debug_resource_rule_with_options(
        self,
        resource_rule_id: str,
        tmp_req: main_models.DebugResourceRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DebugResourceRuleResponse:
        tmp_req.validate()
        request = main_models.DebugResourceRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.metric_info):
            request.metric_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.metric_info, 'MetricInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.metric_info_shrink):
            query['MetricInfo'] = request.metric_info_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DebugResourceRule',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resourcerules/{DaraURL.percent_encode(resource_rule_id)}/action/debug',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DebugResourceRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def debug_resource_rule_with_options_async(
        self,
        resource_rule_id: str,
        tmp_req: main_models.DebugResourceRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DebugResourceRuleResponse:
        tmp_req.validate()
        request = main_models.DebugResourceRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.metric_info):
            request.metric_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.metric_info, 'MetricInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.metric_info_shrink):
            query['MetricInfo'] = request.metric_info_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DebugResourceRule',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resourcerules/{DaraURL.percent_encode(resource_rule_id)}/action/debug',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DebugResourceRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def debug_resource_rule(
        self,
        resource_rule_id: str,
        request: main_models.DebugResourceRuleRequest,
    ) -> main_models.DebugResourceRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.debug_resource_rule_with_options(resource_rule_id, request, headers, runtime)

    async def debug_resource_rule_async(
        self,
        resource_rule_id: str,
        request: main_models.DebugResourceRuleRequest,
    ) -> main_models.DebugResourceRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.debug_resource_rule_with_options_async(resource_rule_id, request, headers, runtime)

    def delete_abmetric_with_options(
        self,
        abmetric_id: str,
        request: main_models.DeleteABMetricRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteABMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteABMetric',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/abmetrics/{DaraURL.percent_encode(abmetric_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteABMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_abmetric_with_options_async(
        self,
        abmetric_id: str,
        request: main_models.DeleteABMetricRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteABMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteABMetric',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/abmetrics/{DaraURL.percent_encode(abmetric_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteABMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_abmetric(
        self,
        abmetric_id: str,
        request: main_models.DeleteABMetricRequest,
    ) -> main_models.DeleteABMetricResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_abmetric_with_options(abmetric_id, request, headers, runtime)

    async def delete_abmetric_async(
        self,
        abmetric_id: str,
        request: main_models.DeleteABMetricRequest,
    ) -> main_models.DeleteABMetricResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_abmetric_with_options_async(abmetric_id, request, headers, runtime)

    def delete_abmetric_group_with_options(
        self,
        abmetric_group_id: str,
        request: main_models.DeleteABMetricGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteABMetricGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteABMetricGroup',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/abmetricgroups/{DaraURL.percent_encode(abmetric_group_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteABMetricGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_abmetric_group_with_options_async(
        self,
        abmetric_group_id: str,
        request: main_models.DeleteABMetricGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteABMetricGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteABMetricGroup',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/abmetricgroups/{DaraURL.percent_encode(abmetric_group_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteABMetricGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_abmetric_group(
        self,
        abmetric_group_id: str,
        request: main_models.DeleteABMetricGroupRequest,
    ) -> main_models.DeleteABMetricGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_abmetric_group_with_options(abmetric_group_id, request, headers, runtime)

    async def delete_abmetric_group_async(
        self,
        abmetric_group_id: str,
        request: main_models.DeleteABMetricGroupRequest,
    ) -> main_models.DeleteABMetricGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_abmetric_group_with_options_async(abmetric_group_id, request, headers, runtime)

    def delete_crowd_with_options(
        self,
        crowd_id: str,
        request: main_models.DeleteCrowdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCrowdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCrowd',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/crowds/{DaraURL.percent_encode(crowd_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCrowdResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_crowd_with_options_async(
        self,
        crowd_id: str,
        request: main_models.DeleteCrowdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCrowdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCrowd',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/crowds/{DaraURL.percent_encode(crowd_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCrowdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_crowd(
        self,
        crowd_id: str,
        request: main_models.DeleteCrowdRequest,
    ) -> main_models.DeleteCrowdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_crowd_with_options(crowd_id, request, headers, runtime)

    async def delete_crowd_async(
        self,
        crowd_id: str,
        request: main_models.DeleteCrowdRequest,
    ) -> main_models.DeleteCrowdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_crowd_with_options_async(crowd_id, request, headers, runtime)

    def delete_engine_config_with_options(
        self,
        engine_config_id: str,
        request: main_models.DeleteEngineConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEngineConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEngineConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/engineconfigs/{DaraURL.percent_encode(engine_config_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEngineConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_engine_config_with_options_async(
        self,
        engine_config_id: str,
        request: main_models.DeleteEngineConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEngineConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEngineConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/engineconfigs/{DaraURL.percent_encode(engine_config_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEngineConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_engine_config(
        self,
        engine_config_id: str,
        request: main_models.DeleteEngineConfigRequest,
    ) -> main_models.DeleteEngineConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_engine_config_with_options(engine_config_id, request, headers, runtime)

    async def delete_engine_config_async(
        self,
        engine_config_id: str,
        request: main_models.DeleteEngineConfigRequest,
    ) -> main_models.DeleteEngineConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_engine_config_with_options_async(engine_config_id, request, headers, runtime)

    def delete_experiment_with_options(
        self,
        experiment_id: str,
        request: main_models.DeleteExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExperimentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteExperiment',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(experiment_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_experiment_with_options_async(
        self,
        experiment_id: str,
        request: main_models.DeleteExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExperimentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteExperiment',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(experiment_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_experiment(
        self,
        experiment_id: str,
        request: main_models.DeleteExperimentRequest,
    ) -> main_models.DeleteExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_experiment_with_options(experiment_id, request, headers, runtime)

    async def delete_experiment_async(
        self,
        experiment_id: str,
        request: main_models.DeleteExperimentRequest,
    ) -> main_models.DeleteExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_experiment_with_options_async(experiment_id, request, headers, runtime)

    def delete_experiment_group_with_options(
        self,
        experiment_group_id: str,
        request: main_models.DeleteExperimentGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExperimentGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteExperimentGroup',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experimentgroups/{DaraURL.percent_encode(experiment_group_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExperimentGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_experiment_group_with_options_async(
        self,
        experiment_group_id: str,
        request: main_models.DeleteExperimentGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExperimentGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteExperimentGroup',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experimentgroups/{DaraURL.percent_encode(experiment_group_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExperimentGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_experiment_group(
        self,
        experiment_group_id: str,
        request: main_models.DeleteExperimentGroupRequest,
    ) -> main_models.DeleteExperimentGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_experiment_group_with_options(experiment_group_id, request, headers, runtime)

    async def delete_experiment_group_async(
        self,
        experiment_group_id: str,
        request: main_models.DeleteExperimentGroupRequest,
    ) -> main_models.DeleteExperimentGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_experiment_group_with_options_async(experiment_group_id, request, headers, runtime)

    def delete_instance_resource_with_options(
        self,
        instance_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstanceResource',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/resources/{DaraURL.percent_encode(resource_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_resource_with_options_async(
        self,
        instance_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstanceResource',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/resources/{DaraURL.percent_encode(resource_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance_resource(
        self,
        instance_id: str,
        resource_id: str,
    ) -> main_models.DeleteInstanceResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_instance_resource_with_options(instance_id, resource_id, headers, runtime)

    async def delete_instance_resource_async(
        self,
        instance_id: str,
        resource_id: str,
    ) -> main_models.DeleteInstanceResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_instance_resource_with_options_async(instance_id, resource_id, headers, runtime)

    def delete_laboratory_with_options(
        self,
        laboratory_id: str,
        request: main_models.DeleteLaboratoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLaboratoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLaboratory',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/laboratories/{DaraURL.percent_encode(laboratory_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLaboratoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_laboratory_with_options_async(
        self,
        laboratory_id: str,
        request: main_models.DeleteLaboratoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLaboratoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLaboratory',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/laboratories/{DaraURL.percent_encode(laboratory_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLaboratoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_laboratory(
        self,
        laboratory_id: str,
        request: main_models.DeleteLaboratoryRequest,
    ) -> main_models.DeleteLaboratoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_laboratory_with_options(laboratory_id, request, headers, runtime)

    async def delete_laboratory_async(
        self,
        laboratory_id: str,
        request: main_models.DeleteLaboratoryRequest,
    ) -> main_models.DeleteLaboratoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_laboratory_with_options_async(laboratory_id, request, headers, runtime)

    def delete_layer_with_options(
        self,
        layer_id: str,
        request: main_models.DeleteLayerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLayerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLayer',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/layers/{DaraURL.percent_encode(layer_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_layer_with_options_async(
        self,
        layer_id: str,
        request: main_models.DeleteLayerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLayerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLayer',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/layers/{DaraURL.percent_encode(layer_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_layer(
        self,
        layer_id: str,
        request: main_models.DeleteLayerRequest,
    ) -> main_models.DeleteLayerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_layer_with_options(layer_id, request, headers, runtime)

    async def delete_layer_async(
        self,
        layer_id: str,
        request: main_models.DeleteLayerRequest,
    ) -> main_models.DeleteLayerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_layer_with_options_async(layer_id, request, headers, runtime)

    def delete_param_with_options(
        self,
        param_id: str,
        request: main_models.DeleteParamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteParamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteParam',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/params/{DaraURL.percent_encode(param_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteParamResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_param_with_options_async(
        self,
        param_id: str,
        request: main_models.DeleteParamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteParamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteParam',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/params/{DaraURL.percent_encode(param_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteParamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_param(
        self,
        param_id: str,
        request: main_models.DeleteParamRequest,
    ) -> main_models.DeleteParamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_param_with_options(param_id, request, headers, runtime)

    async def delete_param_async(
        self,
        param_id: str,
        request: main_models.DeleteParamRequest,
    ) -> main_models.DeleteParamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_param_with_options_async(param_id, request, headers, runtime)

    def delete_recall_management_service_with_options(
        self,
        recall_management_service_id: str,
        request: main_models.DeleteRecallManagementServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRecallManagementServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRecallManagementService',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices/{DaraURL.percent_encode(recall_management_service_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRecallManagementServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_recall_management_service_with_options_async(
        self,
        recall_management_service_id: str,
        request: main_models.DeleteRecallManagementServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRecallManagementServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRecallManagementService',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices/{DaraURL.percent_encode(recall_management_service_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRecallManagementServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_recall_management_service(
        self,
        recall_management_service_id: str,
        request: main_models.DeleteRecallManagementServiceRequest,
    ) -> main_models.DeleteRecallManagementServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_recall_management_service_with_options(recall_management_service_id, request, headers, runtime)

    async def delete_recall_management_service_async(
        self,
        recall_management_service_id: str,
        request: main_models.DeleteRecallManagementServiceRequest,
    ) -> main_models.DeleteRecallManagementServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_recall_management_service_with_options_async(recall_management_service_id, request, headers, runtime)

    def delete_recall_management_service_version_with_options(
        self,
        recall_management_service_id: str,
        recall_management_service_version_id: str,
        request: main_models.DeleteRecallManagementServiceVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRecallManagementServiceVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRecallManagementServiceVersion',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices/{DaraURL.percent_encode(recall_management_service_id)}/versions/{DaraURL.percent_encode(recall_management_service_version_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRecallManagementServiceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_recall_management_service_version_with_options_async(
        self,
        recall_management_service_id: str,
        recall_management_service_version_id: str,
        request: main_models.DeleteRecallManagementServiceVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRecallManagementServiceVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRecallManagementServiceVersion',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices/{DaraURL.percent_encode(recall_management_service_id)}/versions/{DaraURL.percent_encode(recall_management_service_version_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRecallManagementServiceVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_recall_management_service_version(
        self,
        recall_management_service_id: str,
        recall_management_service_version_id: str,
        request: main_models.DeleteRecallManagementServiceVersionRequest,
    ) -> main_models.DeleteRecallManagementServiceVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_recall_management_service_version_with_options(recall_management_service_id, recall_management_service_version_id, request, headers, runtime)

    async def delete_recall_management_service_version_async(
        self,
        recall_management_service_id: str,
        recall_management_service_version_id: str,
        request: main_models.DeleteRecallManagementServiceVersionRequest,
    ) -> main_models.DeleteRecallManagementServiceVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_recall_management_service_version_with_options_async(recall_management_service_id, recall_management_service_version_id, request, headers, runtime)

    def delete_recall_management_service_version_config_with_options(
        self,
        recall_management_service_id: str,
        recall_management_service_version_id: str,
        recall_management_service_version_config_id: str,
        request: main_models.DeleteRecallManagementServiceVersionConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRecallManagementServiceVersionConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRecallManagementServiceVersionConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices/{DaraURL.percent_encode(recall_management_service_id)}/versions/{DaraURL.percent_encode(recall_management_service_version_id)}/configs/{DaraURL.percent_encode(recall_management_service_version_config_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRecallManagementServiceVersionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_recall_management_service_version_config_with_options_async(
        self,
        recall_management_service_id: str,
        recall_management_service_version_id: str,
        recall_management_service_version_config_id: str,
        request: main_models.DeleteRecallManagementServiceVersionConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRecallManagementServiceVersionConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRecallManagementServiceVersionConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices/{DaraURL.percent_encode(recall_management_service_id)}/versions/{DaraURL.percent_encode(recall_management_service_version_id)}/configs/{DaraURL.percent_encode(recall_management_service_version_config_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRecallManagementServiceVersionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_recall_management_service_version_config(
        self,
        recall_management_service_id: str,
        recall_management_service_version_id: str,
        recall_management_service_version_config_id: str,
        request: main_models.DeleteRecallManagementServiceVersionConfigRequest,
    ) -> main_models.DeleteRecallManagementServiceVersionConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_recall_management_service_version_config_with_options(recall_management_service_id, recall_management_service_version_id, recall_management_service_version_config_id, request, headers, runtime)

    async def delete_recall_management_service_version_config_async(
        self,
        recall_management_service_id: str,
        recall_management_service_version_id: str,
        recall_management_service_version_config_id: str,
        request: main_models.DeleteRecallManagementServiceVersionConfigRequest,
    ) -> main_models.DeleteRecallManagementServiceVersionConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_recall_management_service_version_config_with_options_async(recall_management_service_id, recall_management_service_version_id, recall_management_service_version_config_id, request, headers, runtime)

    def delete_recall_management_table_with_options(
        self,
        recall_management_table_id: str,
        request: main_models.DeleteRecallManagementTableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRecallManagementTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRecallManagementTable',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementtables/{DaraURL.percent_encode(recall_management_table_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRecallManagementTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_recall_management_table_with_options_async(
        self,
        recall_management_table_id: str,
        request: main_models.DeleteRecallManagementTableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRecallManagementTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRecallManagementTable',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementtables/{DaraURL.percent_encode(recall_management_table_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRecallManagementTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_recall_management_table(
        self,
        recall_management_table_id: str,
        request: main_models.DeleteRecallManagementTableRequest,
    ) -> main_models.DeleteRecallManagementTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_recall_management_table_with_options(recall_management_table_id, request, headers, runtime)

    async def delete_recall_management_table_async(
        self,
        recall_management_table_id: str,
        request: main_models.DeleteRecallManagementTableRequest,
    ) -> main_models.DeleteRecallManagementTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_recall_management_table_with_options_async(recall_management_table_id, request, headers, runtime)

    def delete_resource_rule_with_options(
        self,
        resource_rule_id: str,
        request: main_models.DeleteResourceRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceRule',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resourcerules/{DaraURL.percent_encode(resource_rule_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_rule_with_options_async(
        self,
        resource_rule_id: str,
        request: main_models.DeleteResourceRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceRule',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resourcerules/{DaraURL.percent_encode(resource_rule_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_rule(
        self,
        resource_rule_id: str,
        request: main_models.DeleteResourceRuleRequest,
    ) -> main_models.DeleteResourceRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_resource_rule_with_options(resource_rule_id, request, headers, runtime)

    async def delete_resource_rule_async(
        self,
        resource_rule_id: str,
        request: main_models.DeleteResourceRuleRequest,
    ) -> main_models.DeleteResourceRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_resource_rule_with_options_async(resource_rule_id, request, headers, runtime)

    def delete_resource_rule_item_with_options(
        self,
        resource_rule_id: str,
        resource_rule_item_id: str,
        request: main_models.DeleteResourceRuleItemRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceRuleItemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceRuleItem',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resourcerules/{DaraURL.percent_encode(resource_rule_id)}/items/{DaraURL.percent_encode(resource_rule_item_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceRuleItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_rule_item_with_options_async(
        self,
        resource_rule_id: str,
        resource_rule_item_id: str,
        request: main_models.DeleteResourceRuleItemRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceRuleItemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceRuleItem',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resourcerules/{DaraURL.percent_encode(resource_rule_id)}/items/{DaraURL.percent_encode(resource_rule_item_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceRuleItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_rule_item(
        self,
        resource_rule_id: str,
        resource_rule_item_id: str,
        request: main_models.DeleteResourceRuleItemRequest,
    ) -> main_models.DeleteResourceRuleItemResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_resource_rule_item_with_options(resource_rule_id, resource_rule_item_id, request, headers, runtime)

    async def delete_resource_rule_item_async(
        self,
        resource_rule_id: str,
        resource_rule_item_id: str,
        request: main_models.DeleteResourceRuleItemRequest,
    ) -> main_models.DeleteResourceRuleItemResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_resource_rule_item_with_options_async(resource_rule_id, resource_rule_item_id, request, headers, runtime)

    def delete_sample_consistency_job_with_options(
        self,
        sample_consistency_job_id: str,
        request: main_models.DeleteSampleConsistencyJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSampleConsistencyJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSampleConsistencyJob',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sampleconsistencyjobs/{DaraURL.percent_encode(sample_consistency_job_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSampleConsistencyJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sample_consistency_job_with_options_async(
        self,
        sample_consistency_job_id: str,
        request: main_models.DeleteSampleConsistencyJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSampleConsistencyJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSampleConsistencyJob',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sampleconsistencyjobs/{DaraURL.percent_encode(sample_consistency_job_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSampleConsistencyJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sample_consistency_job(
        self,
        sample_consistency_job_id: str,
        request: main_models.DeleteSampleConsistencyJobRequest,
    ) -> main_models.DeleteSampleConsistencyJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_sample_consistency_job_with_options(sample_consistency_job_id, request, headers, runtime)

    async def delete_sample_consistency_job_async(
        self,
        sample_consistency_job_id: str,
        request: main_models.DeleteSampleConsistencyJobRequest,
    ) -> main_models.DeleteSampleConsistencyJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_sample_consistency_job_with_options_async(sample_consistency_job_id, request, headers, runtime)

    def delete_scene_with_options(
        self,
        scene_id: str,
        request: main_models.DeleteSceneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScene',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/scenes/{DaraURL.percent_encode(scene_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scene_with_options_async(
        self,
        scene_id: str,
        request: main_models.DeleteSceneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScene',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/scenes/{DaraURL.percent_encode(scene_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scene(
        self,
        scene_id: str,
        request: main_models.DeleteSceneRequest,
    ) -> main_models.DeleteSceneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_scene_with_options(scene_id, request, headers, runtime)

    async def delete_scene_async(
        self,
        scene_id: str,
        request: main_models.DeleteSceneRequest,
    ) -> main_models.DeleteSceneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_scene_with_options_async(scene_id, request, headers, runtime)

    def delete_sub_crowd_with_options(
        self,
        crowd_id: str,
        sub_crowd_id: str,
        request: main_models.DeleteSubCrowdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSubCrowdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSubCrowd',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/crowds/{DaraURL.percent_encode(crowd_id)}/subcrowds/{DaraURL.percent_encode(sub_crowd_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSubCrowdResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sub_crowd_with_options_async(
        self,
        crowd_id: str,
        sub_crowd_id: str,
        request: main_models.DeleteSubCrowdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSubCrowdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSubCrowd',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/crowds/{DaraURL.percent_encode(crowd_id)}/subcrowds/{DaraURL.percent_encode(sub_crowd_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSubCrowdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sub_crowd(
        self,
        crowd_id: str,
        sub_crowd_id: str,
        request: main_models.DeleteSubCrowdRequest,
    ) -> main_models.DeleteSubCrowdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_sub_crowd_with_options(crowd_id, sub_crowd_id, request, headers, runtime)

    async def delete_sub_crowd_async(
        self,
        crowd_id: str,
        sub_crowd_id: str,
        request: main_models.DeleteSubCrowdRequest,
    ) -> main_models.DeleteSubCrowdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_sub_crowd_with_options_async(crowd_id, sub_crowd_id, request, headers, runtime)

    def delete_table_meta_with_options(
        self,
        table_meta_id: str,
        request: main_models.DeleteTableMetaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTableMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTableMeta',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tablemetas/{DaraURL.percent_encode(table_meta_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTableMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_table_meta_with_options_async(
        self,
        table_meta_id: str,
        request: main_models.DeleteTableMetaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTableMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTableMeta',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tablemetas/{DaraURL.percent_encode(table_meta_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTableMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_table_meta(
        self,
        table_meta_id: str,
        request: main_models.DeleteTableMetaRequest,
    ) -> main_models.DeleteTableMetaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_table_meta_with_options(table_meta_id, request, headers, runtime)

    async def delete_table_meta_async(
        self,
        table_meta_id: str,
        request: main_models.DeleteTableMetaRequest,
    ) -> main_models.DeleteTableMetaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_table_meta_with_options_async(table_meta_id, request, headers, runtime)

    def delete_traffic_control_target_with_options(
        self,
        traffic_control_target_id: str,
        request: main_models.DeleteTrafficControlTargetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTrafficControlTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTrafficControlTarget',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltargets/{DaraURL.percent_encode(traffic_control_target_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTrafficControlTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_traffic_control_target_with_options_async(
        self,
        traffic_control_target_id: str,
        request: main_models.DeleteTrafficControlTargetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTrafficControlTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTrafficControlTarget',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltargets/{DaraURL.percent_encode(traffic_control_target_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTrafficControlTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_traffic_control_target(
        self,
        traffic_control_target_id: str,
        request: main_models.DeleteTrafficControlTargetRequest,
    ) -> main_models.DeleteTrafficControlTargetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_traffic_control_target_with_options(traffic_control_target_id, request, headers, runtime)

    async def delete_traffic_control_target_async(
        self,
        traffic_control_target_id: str,
        request: main_models.DeleteTrafficControlTargetRequest,
    ) -> main_models.DeleteTrafficControlTargetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_traffic_control_target_with_options_async(traffic_control_target_id, request, headers, runtime)

    def delete_traffic_control_task_with_options(
        self,
        traffic_control_task_id: str,
        request: main_models.DeleteTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTrafficControlTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTrafficControlTask',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltasks/{DaraURL.percent_encode(traffic_control_task_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTrafficControlTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_traffic_control_task_with_options_async(
        self,
        traffic_control_task_id: str,
        request: main_models.DeleteTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTrafficControlTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTrafficControlTask',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltasks/{DaraURL.percent_encode(traffic_control_task_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTrafficControlTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_traffic_control_task(
        self,
        traffic_control_task_id: str,
        request: main_models.DeleteTrafficControlTaskRequest,
    ) -> main_models.DeleteTrafficControlTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_traffic_control_task_with_options(traffic_control_task_id, request, headers, runtime)

    async def delete_traffic_control_task_async(
        self,
        traffic_control_task_id: str,
        request: main_models.DeleteTrafficControlTaskRequest,
    ) -> main_models.DeleteTrafficControlTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_traffic_control_task_with_options_async(traffic_control_task_id, request, headers, runtime)

    def generate_algorithm_customization_script_with_options(
        self,
        algorithm_customization_id: str,
        request: main_models.GenerateAlgorithmCustomizationScriptRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateAlgorithmCustomizationScriptResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.deploy_mode):
            body['DeployMode'] = request.deploy_mode
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module_field_types):
            body['ModuleFieldTypes'] = request.module_field_types
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateAlgorithmCustomizationScript',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/algorithmcustomizations/{DaraURL.percent_encode(algorithm_customization_id)}/action/generatescript',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateAlgorithmCustomizationScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_algorithm_customization_script_with_options_async(
        self,
        algorithm_customization_id: str,
        request: main_models.GenerateAlgorithmCustomizationScriptRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateAlgorithmCustomizationScriptResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.deploy_mode):
            body['DeployMode'] = request.deploy_mode
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module_field_types):
            body['ModuleFieldTypes'] = request.module_field_types
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateAlgorithmCustomizationScript',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/algorithmcustomizations/{DaraURL.percent_encode(algorithm_customization_id)}/action/generatescript',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateAlgorithmCustomizationScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_algorithm_customization_script(
        self,
        algorithm_customization_id: str,
        request: main_models.GenerateAlgorithmCustomizationScriptRequest,
    ) -> main_models.GenerateAlgorithmCustomizationScriptResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.generate_algorithm_customization_script_with_options(algorithm_customization_id, request, headers, runtime)

    async def generate_algorithm_customization_script_async(
        self,
        algorithm_customization_id: str,
        request: main_models.GenerateAlgorithmCustomizationScriptRequest,
    ) -> main_models.GenerateAlgorithmCustomizationScriptResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.generate_algorithm_customization_script_with_options_async(algorithm_customization_id, request, headers, runtime)

    def generate_traffic_control_task_code_with_options(
        self,
        traffic_control_task_id: str,
        request: main_models.GenerateTrafficControlTaskCodeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateTrafficControlTaskCodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateTrafficControlTaskCode',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltasks/{DaraURL.percent_encode(traffic_control_task_id)}/action/generatecode',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateTrafficControlTaskCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_traffic_control_task_code_with_options_async(
        self,
        traffic_control_task_id: str,
        request: main_models.GenerateTrafficControlTaskCodeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateTrafficControlTaskCodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateTrafficControlTaskCode',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltasks/{DaraURL.percent_encode(traffic_control_task_id)}/action/generatecode',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateTrafficControlTaskCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_traffic_control_task_code(
        self,
        traffic_control_task_id: str,
        request: main_models.GenerateTrafficControlTaskCodeRequest,
    ) -> main_models.GenerateTrafficControlTaskCodeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.generate_traffic_control_task_code_with_options(traffic_control_task_id, request, headers, runtime)

    async def generate_traffic_control_task_code_async(
        self,
        traffic_control_task_id: str,
        request: main_models.GenerateTrafficControlTaskCodeRequest,
    ) -> main_models.GenerateTrafficControlTaskCodeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.generate_traffic_control_task_code_with_options_async(traffic_control_task_id, request, headers, runtime)

    def generate_traffic_control_task_config_with_options(
        self,
        traffic_control_task_id: str,
        request: main_models.GenerateTrafficControlTaskConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateTrafficControlTaskConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateTrafficControlTaskConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltasks/{DaraURL.percent_encode(traffic_control_task_id)}/action/generateconfig',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateTrafficControlTaskConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_traffic_control_task_config_with_options_async(
        self,
        traffic_control_task_id: str,
        request: main_models.GenerateTrafficControlTaskConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateTrafficControlTaskConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateTrafficControlTaskConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltasks/{DaraURL.percent_encode(traffic_control_task_id)}/action/generateconfig',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateTrafficControlTaskConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_traffic_control_task_config(
        self,
        traffic_control_task_id: str,
        request: main_models.GenerateTrafficControlTaskConfigRequest,
    ) -> main_models.GenerateTrafficControlTaskConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.generate_traffic_control_task_config_with_options(traffic_control_task_id, request, headers, runtime)

    async def generate_traffic_control_task_config_async(
        self,
        traffic_control_task_id: str,
        request: main_models.GenerateTrafficControlTaskConfigRequest,
    ) -> main_models.GenerateTrafficControlTaskConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.generate_traffic_control_task_config_with_options_async(traffic_control_task_id, request, headers, runtime)

    def get_abmetric_with_options(
        self,
        abmetric_id: str,
        request: main_models.GetABMetricRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetABMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetABMetric',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/abmetrics/{DaraURL.percent_encode(abmetric_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetABMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_abmetric_with_options_async(
        self,
        abmetric_id: str,
        request: main_models.GetABMetricRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetABMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetABMetric',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/abmetrics/{DaraURL.percent_encode(abmetric_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetABMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_abmetric(
        self,
        abmetric_id: str,
        request: main_models.GetABMetricRequest,
    ) -> main_models.GetABMetricResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_abmetric_with_options(abmetric_id, request, headers, runtime)

    async def get_abmetric_async(
        self,
        abmetric_id: str,
        request: main_models.GetABMetricRequest,
    ) -> main_models.GetABMetricResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_abmetric_with_options_async(abmetric_id, request, headers, runtime)

    def get_abmetric_group_with_options(
        self,
        abmetric_group_id: str,
        request: main_models.GetABMetricGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetABMetricGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetABMetricGroup',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/abmetricgroups/{DaraURL.percent_encode(abmetric_group_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetABMetricGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_abmetric_group_with_options_async(
        self,
        abmetric_group_id: str,
        request: main_models.GetABMetricGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetABMetricGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetABMetricGroup',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/abmetricgroups/{DaraURL.percent_encode(abmetric_group_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetABMetricGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_abmetric_group(
        self,
        abmetric_group_id: str,
        request: main_models.GetABMetricGroupRequest,
    ) -> main_models.GetABMetricGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_abmetric_group_with_options(abmetric_group_id, request, headers, runtime)

    async def get_abmetric_group_async(
        self,
        abmetric_group_id: str,
        request: main_models.GetABMetricGroupRequest,
    ) -> main_models.GetABMetricGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_abmetric_group_with_options_async(abmetric_group_id, request, headers, runtime)

    def get_calculation_job_with_options(
        self,
        calculation_job_id: str,
        request: main_models.GetCalculationJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCalculationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCalculationJob',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/calculationjobs/{DaraURL.percent_encode(calculation_job_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCalculationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_calculation_job_with_options_async(
        self,
        calculation_job_id: str,
        request: main_models.GetCalculationJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCalculationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCalculationJob',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/calculationjobs/{DaraURL.percent_encode(calculation_job_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCalculationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_calculation_job(
        self,
        calculation_job_id: str,
        request: main_models.GetCalculationJobRequest,
    ) -> main_models.GetCalculationJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_calculation_job_with_options(calculation_job_id, request, headers, runtime)

    async def get_calculation_job_async(
        self,
        calculation_job_id: str,
        request: main_models.GetCalculationJobRequest,
    ) -> main_models.GetCalculationJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_calculation_job_with_options_async(calculation_job_id, request, headers, runtime)

    def get_engine_config_with_options(
        self,
        engine_config_id: str,
        request: main_models.GetEngineConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEngineConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEngineConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/engineconfigs/{DaraURL.percent_encode(engine_config_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEngineConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_engine_config_with_options_async(
        self,
        engine_config_id: str,
        request: main_models.GetEngineConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEngineConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEngineConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/engineconfigs/{DaraURL.percent_encode(engine_config_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEngineConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_engine_config(
        self,
        engine_config_id: str,
        request: main_models.GetEngineConfigRequest,
    ) -> main_models.GetEngineConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_engine_config_with_options(engine_config_id, request, headers, runtime)

    async def get_engine_config_async(
        self,
        engine_config_id: str,
        request: main_models.GetEngineConfigRequest,
    ) -> main_models.GetEngineConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_engine_config_with_options_async(engine_config_id, request, headers, runtime)

    def get_experiment_with_options(
        self,
        experiment_id: str,
        request: main_models.GetExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetExperimentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExperiment',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(experiment_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_experiment_with_options_async(
        self,
        experiment_id: str,
        request: main_models.GetExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetExperimentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExperiment',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(experiment_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_experiment(
        self,
        experiment_id: str,
        request: main_models.GetExperimentRequest,
    ) -> main_models.GetExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_experiment_with_options(experiment_id, request, headers, runtime)

    async def get_experiment_async(
        self,
        experiment_id: str,
        request: main_models.GetExperimentRequest,
    ) -> main_models.GetExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_experiment_with_options_async(experiment_id, request, headers, runtime)

    def get_experiment_group_with_options(
        self,
        experiment_group_id: str,
        request: main_models.GetExperimentGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetExperimentGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExperimentGroup',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experimentgroups/{DaraURL.percent_encode(experiment_group_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExperimentGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_experiment_group_with_options_async(
        self,
        experiment_group_id: str,
        request: main_models.GetExperimentGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetExperimentGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExperimentGroup',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experimentgroups/{DaraURL.percent_encode(experiment_group_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExperimentGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_experiment_group(
        self,
        experiment_group_id: str,
        request: main_models.GetExperimentGroupRequest,
    ) -> main_models.GetExperimentGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_experiment_group_with_options(experiment_group_id, request, headers, runtime)

    async def get_experiment_group_async(
        self,
        experiment_group_id: str,
        request: main_models.GetExperimentGroupRequest,
    ) -> main_models.GetExperimentGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_experiment_group_with_options_async(experiment_group_id, request, headers, runtime)

    def get_feature_consistency_check_job_with_options(
        self,
        feature_consistency_check_job_id: str,
        request: main_models.GetFeatureConsistencyCheckJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFeatureConsistencyCheckJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFeatureConsistencyCheckJob',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/featureconsistencycheck/jobs/{DaraURL.percent_encode(feature_consistency_check_job_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFeatureConsistencyCheckJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_feature_consistency_check_job_with_options_async(
        self,
        feature_consistency_check_job_id: str,
        request: main_models.GetFeatureConsistencyCheckJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFeatureConsistencyCheckJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFeatureConsistencyCheckJob',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/featureconsistencycheck/jobs/{DaraURL.percent_encode(feature_consistency_check_job_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFeatureConsistencyCheckJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_feature_consistency_check_job(
        self,
        feature_consistency_check_job_id: str,
        request: main_models.GetFeatureConsistencyCheckJobRequest,
    ) -> main_models.GetFeatureConsistencyCheckJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_feature_consistency_check_job_with_options(feature_consistency_check_job_id, request, headers, runtime)

    async def get_feature_consistency_check_job_async(
        self,
        feature_consistency_check_job_id: str,
        request: main_models.GetFeatureConsistencyCheckJobRequest,
    ) -> main_models.GetFeatureConsistencyCheckJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_feature_consistency_check_job_with_options_async(feature_consistency_check_job_id, request, headers, runtime)

    def get_feature_consistency_check_job_config_with_options(
        self,
        feature_consistency_check_job_config_id: str,
        request: main_models.GetFeatureConsistencyCheckJobConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFeatureConsistencyCheckJobConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFeatureConsistencyCheckJobConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/featureconsistencycheck/jobconfigs/{DaraURL.percent_encode(feature_consistency_check_job_config_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFeatureConsistencyCheckJobConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_feature_consistency_check_job_config_with_options_async(
        self,
        feature_consistency_check_job_config_id: str,
        request: main_models.GetFeatureConsistencyCheckJobConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFeatureConsistencyCheckJobConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFeatureConsistencyCheckJobConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/featureconsistencycheck/jobconfigs/{DaraURL.percent_encode(feature_consistency_check_job_config_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFeatureConsistencyCheckJobConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_feature_consistency_check_job_config(
        self,
        feature_consistency_check_job_config_id: str,
        request: main_models.GetFeatureConsistencyCheckJobConfigRequest,
    ) -> main_models.GetFeatureConsistencyCheckJobConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_feature_consistency_check_job_config_with_options(feature_consistency_check_job_config_id, request, headers, runtime)

    async def get_feature_consistency_check_job_config_async(
        self,
        feature_consistency_check_job_config_id: str,
        request: main_models.GetFeatureConsistencyCheckJobConfigRequest,
    ) -> main_models.GetFeatureConsistencyCheckJobConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_feature_consistency_check_job_config_with_options_async(feature_consistency_check_job_config_id, request, headers, runtime)

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
            version = '2022-12-13',
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
            version = '2022-12-13',
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

    def get_instance_resource_with_options(
        self,
        instance_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceResourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceResource',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/resources/{DaraURL.percent_encode(resource_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_resource_with_options_async(
        self,
        instance_id: str,
        resource_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceResourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceResource',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/resources/{DaraURL.percent_encode(resource_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_resource(
        self,
        instance_id: str,
        resource_id: str,
    ) -> main_models.GetInstanceResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_instance_resource_with_options(instance_id, resource_id, headers, runtime)

    async def get_instance_resource_async(
        self,
        instance_id: str,
        resource_id: str,
    ) -> main_models.GetInstanceResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_instance_resource_with_options_async(instance_id, resource_id, headers, runtime)

    def get_instance_resource_table_with_options(
        self,
        instance_id: str,
        resource_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceResourceTableResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceResourceTable',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/resources/{DaraURL.percent_encode(resource_id)}/tables/{DaraURL.percent_encode(table_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceResourceTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_resource_table_with_options_async(
        self,
        instance_id: str,
        resource_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceResourceTableResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceResourceTable',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/resources/{DaraURL.percent_encode(resource_id)}/tables/{DaraURL.percent_encode(table_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceResourceTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_resource_table(
        self,
        instance_id: str,
        resource_id: str,
        table_name: str,
    ) -> main_models.GetInstanceResourceTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_instance_resource_table_with_options(instance_id, resource_id, table_name, headers, runtime)

    async def get_instance_resource_table_async(
        self,
        instance_id: str,
        resource_id: str,
        table_name: str,
    ) -> main_models.GetInstanceResourceTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_instance_resource_table_with_options_async(instance_id, resource_id, table_name, headers, runtime)

    def get_laboratory_with_options(
        self,
        laboratory_id: str,
        request: main_models.GetLaboratoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLaboratoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLaboratory',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/laboratories/{DaraURL.percent_encode(laboratory_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLaboratoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_laboratory_with_options_async(
        self,
        laboratory_id: str,
        request: main_models.GetLaboratoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLaboratoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLaboratory',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/laboratories/{DaraURL.percent_encode(laboratory_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLaboratoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_laboratory(
        self,
        laboratory_id: str,
        request: main_models.GetLaboratoryRequest,
    ) -> main_models.GetLaboratoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_laboratory_with_options(laboratory_id, request, headers, runtime)

    async def get_laboratory_async(
        self,
        laboratory_id: str,
        request: main_models.GetLaboratoryRequest,
    ) -> main_models.GetLaboratoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_laboratory_with_options_async(laboratory_id, request, headers, runtime)

    def get_layer_with_options(
        self,
        layer_id: str,
        request: main_models.GetLayerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLayerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLayer',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/layers/{DaraURL.percent_encode(layer_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_layer_with_options_async(
        self,
        layer_id: str,
        request: main_models.GetLayerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLayerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLayer',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/layers/{DaraURL.percent_encode(layer_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_layer(
        self,
        layer_id: str,
        request: main_models.GetLayerRequest,
    ) -> main_models.GetLayerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_layer_with_options(layer_id, request, headers, runtime)

    async def get_layer_async(
        self,
        layer_id: str,
        request: main_models.GetLayerRequest,
    ) -> main_models.GetLayerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_layer_with_options_async(layer_id, request, headers, runtime)

    def get_recall_management_config_with_options(
        self,
        request: main_models.GetRecallManagementConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRecallManagementConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRecallManagementConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementconfigs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRecallManagementConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_recall_management_config_with_options_async(
        self,
        request: main_models.GetRecallManagementConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRecallManagementConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRecallManagementConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementconfigs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRecallManagementConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_recall_management_config(
        self,
        request: main_models.GetRecallManagementConfigRequest,
    ) -> main_models.GetRecallManagementConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_recall_management_config_with_options(request, headers, runtime)

    async def get_recall_management_config_async(
        self,
        request: main_models.GetRecallManagementConfigRequest,
    ) -> main_models.GetRecallManagementConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_recall_management_config_with_options_async(request, headers, runtime)

    def get_recall_management_job_with_options(
        self,
        recall_management_job_id: str,
        request: main_models.GetRecallManagementJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRecallManagementJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRecallManagementJob',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementjobs/{DaraURL.percent_encode(recall_management_job_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRecallManagementJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_recall_management_job_with_options_async(
        self,
        recall_management_job_id: str,
        request: main_models.GetRecallManagementJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRecallManagementJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRecallManagementJob',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementjobs/{DaraURL.percent_encode(recall_management_job_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRecallManagementJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_recall_management_job(
        self,
        recall_management_job_id: str,
        request: main_models.GetRecallManagementJobRequest,
    ) -> main_models.GetRecallManagementJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_recall_management_job_with_options(recall_management_job_id, request, headers, runtime)

    async def get_recall_management_job_async(
        self,
        recall_management_job_id: str,
        request: main_models.GetRecallManagementJobRequest,
    ) -> main_models.GetRecallManagementJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_recall_management_job_with_options_async(recall_management_job_id, request, headers, runtime)

    def get_recall_management_service_with_options(
        self,
        recall_management_service_id: str,
        request: main_models.GetRecallManagementServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRecallManagementServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRecallManagementService',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices/{DaraURL.percent_encode(recall_management_service_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRecallManagementServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_recall_management_service_with_options_async(
        self,
        recall_management_service_id: str,
        request: main_models.GetRecallManagementServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRecallManagementServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRecallManagementService',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices/{DaraURL.percent_encode(recall_management_service_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRecallManagementServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_recall_management_service(
        self,
        recall_management_service_id: str,
        request: main_models.GetRecallManagementServiceRequest,
    ) -> main_models.GetRecallManagementServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_recall_management_service_with_options(recall_management_service_id, request, headers, runtime)

    async def get_recall_management_service_async(
        self,
        recall_management_service_id: str,
        request: main_models.GetRecallManagementServiceRequest,
    ) -> main_models.GetRecallManagementServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_recall_management_service_with_options_async(recall_management_service_id, request, headers, runtime)

    def get_recall_management_service_version_with_options(
        self,
        recall_management_service_id: str,
        recall_management_service_version_id: str,
        request: main_models.GetRecallManagementServiceVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRecallManagementServiceVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRecallManagementServiceVersion',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices/{DaraURL.percent_encode(recall_management_service_id)}/versions/{DaraURL.percent_encode(recall_management_service_version_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRecallManagementServiceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_recall_management_service_version_with_options_async(
        self,
        recall_management_service_id: str,
        recall_management_service_version_id: str,
        request: main_models.GetRecallManagementServiceVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRecallManagementServiceVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRecallManagementServiceVersion',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices/{DaraURL.percent_encode(recall_management_service_id)}/versions/{DaraURL.percent_encode(recall_management_service_version_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRecallManagementServiceVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_recall_management_service_version(
        self,
        recall_management_service_id: str,
        recall_management_service_version_id: str,
        request: main_models.GetRecallManagementServiceVersionRequest,
    ) -> main_models.GetRecallManagementServiceVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_recall_management_service_version_with_options(recall_management_service_id, recall_management_service_version_id, request, headers, runtime)

    async def get_recall_management_service_version_async(
        self,
        recall_management_service_id: str,
        recall_management_service_version_id: str,
        request: main_models.GetRecallManagementServiceVersionRequest,
    ) -> main_models.GetRecallManagementServiceVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_recall_management_service_version_with_options_async(recall_management_service_id, recall_management_service_version_id, request, headers, runtime)

    def get_recall_management_service_version_config_with_options(
        self,
        recall_management_service_id: str,
        recall_management_service_version_id: str,
        recall_management_service_version_config_id: str,
        request: main_models.GetRecallManagementServiceVersionConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRecallManagementServiceVersionConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRecallManagementServiceVersionConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices/{DaraURL.percent_encode(recall_management_service_id)}/versions/{DaraURL.percent_encode(recall_management_service_version_id)}/configs/{DaraURL.percent_encode(recall_management_service_version_config_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRecallManagementServiceVersionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_recall_management_service_version_config_with_options_async(
        self,
        recall_management_service_id: str,
        recall_management_service_version_id: str,
        recall_management_service_version_config_id: str,
        request: main_models.GetRecallManagementServiceVersionConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRecallManagementServiceVersionConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRecallManagementServiceVersionConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices/{DaraURL.percent_encode(recall_management_service_id)}/versions/{DaraURL.percent_encode(recall_management_service_version_id)}/configs/{DaraURL.percent_encode(recall_management_service_version_config_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRecallManagementServiceVersionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_recall_management_service_version_config(
        self,
        recall_management_service_id: str,
        recall_management_service_version_id: str,
        recall_management_service_version_config_id: str,
        request: main_models.GetRecallManagementServiceVersionConfigRequest,
    ) -> main_models.GetRecallManagementServiceVersionConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_recall_management_service_version_config_with_options(recall_management_service_id, recall_management_service_version_id, recall_management_service_version_config_id, request, headers, runtime)

    async def get_recall_management_service_version_config_async(
        self,
        recall_management_service_id: str,
        recall_management_service_version_id: str,
        recall_management_service_version_config_id: str,
        request: main_models.GetRecallManagementServiceVersionConfigRequest,
    ) -> main_models.GetRecallManagementServiceVersionConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_recall_management_service_version_config_with_options_async(recall_management_service_id, recall_management_service_version_id, recall_management_service_version_config_id, request, headers, runtime)

    def get_recall_management_table_with_options(
        self,
        recall_management_table_id: str,
        request: main_models.GetRecallManagementTableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRecallManagementTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRecallManagementTable',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementtables/{DaraURL.percent_encode(recall_management_table_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRecallManagementTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_recall_management_table_with_options_async(
        self,
        recall_management_table_id: str,
        request: main_models.GetRecallManagementTableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRecallManagementTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRecallManagementTable',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementtables/{DaraURL.percent_encode(recall_management_table_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRecallManagementTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_recall_management_table(
        self,
        recall_management_table_id: str,
        request: main_models.GetRecallManagementTableRequest,
    ) -> main_models.GetRecallManagementTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_recall_management_table_with_options(recall_management_table_id, request, headers, runtime)

    async def get_recall_management_table_async(
        self,
        recall_management_table_id: str,
        request: main_models.GetRecallManagementTableRequest,
    ) -> main_models.GetRecallManagementTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_recall_management_table_with_options_async(recall_management_table_id, request, headers, runtime)

    def get_resource_rule_with_options(
        self,
        resource_rule_id: str,
        request: main_models.GetResourceRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceRule',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resourcerules/{DaraURL.percent_encode(resource_rule_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_rule_with_options_async(
        self,
        resource_rule_id: str,
        request: main_models.GetResourceRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceRule',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resourcerules/{DaraURL.percent_encode(resource_rule_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_rule(
        self,
        resource_rule_id: str,
        request: main_models.GetResourceRuleRequest,
    ) -> main_models.GetResourceRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_resource_rule_with_options(resource_rule_id, request, headers, runtime)

    async def get_resource_rule_async(
        self,
        resource_rule_id: str,
        request: main_models.GetResourceRuleRequest,
    ) -> main_models.GetResourceRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_resource_rule_with_options_async(resource_rule_id, request, headers, runtime)

    def get_sample_consistency_job_with_options(
        self,
        sample_consistency_job_id: str,
        request: main_models.GetSampleConsistencyJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSampleConsistencyJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSampleConsistencyJob',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sampleconsistencyjobs/{DaraURL.percent_encode(sample_consistency_job_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSampleConsistencyJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sample_consistency_job_with_options_async(
        self,
        sample_consistency_job_id: str,
        request: main_models.GetSampleConsistencyJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSampleConsistencyJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSampleConsistencyJob',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sampleconsistencyjobs/{DaraURL.percent_encode(sample_consistency_job_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSampleConsistencyJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sample_consistency_job(
        self,
        sample_consistency_job_id: str,
        request: main_models.GetSampleConsistencyJobRequest,
    ) -> main_models.GetSampleConsistencyJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_sample_consistency_job_with_options(sample_consistency_job_id, request, headers, runtime)

    async def get_sample_consistency_job_async(
        self,
        sample_consistency_job_id: str,
        request: main_models.GetSampleConsistencyJobRequest,
    ) -> main_models.GetSampleConsistencyJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_sample_consistency_job_with_options_async(sample_consistency_job_id, request, headers, runtime)

    def get_scene_with_options(
        self,
        scene_id: str,
        request: main_models.GetSceneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScene',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/scenes/{DaraURL.percent_encode(scene_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scene_with_options_async(
        self,
        scene_id: str,
        request: main_models.GetSceneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScene',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/scenes/{DaraURL.percent_encode(scene_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scene(
        self,
        scene_id: str,
        request: main_models.GetSceneRequest,
    ) -> main_models.GetSceneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_scene_with_options(scene_id, request, headers, runtime)

    async def get_scene_async(
        self,
        scene_id: str,
        request: main_models.GetSceneRequest,
    ) -> main_models.GetSceneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_scene_with_options_async(scene_id, request, headers, runtime)

    def get_service_with_options(
        self,
        service_id: str,
        request: main_models.GetServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetService',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/services/{DaraURL.percent_encode(service_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_with_options_async(
        self,
        service_id: str,
        request: main_models.GetServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetService',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/services/{DaraURL.percent_encode(service_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service(
        self,
        service_id: str,
        request: main_models.GetServiceRequest,
    ) -> main_models.GetServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_service_with_options(service_id, request, headers, runtime)

    async def get_service_async(
        self,
        service_id: str,
        request: main_models.GetServiceRequest,
    ) -> main_models.GetServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_service_with_options_async(service_id, request, headers, runtime)

    def get_sub_crowd_with_options(
        self,
        crowd_id: str,
        sub_crowd_id: str,
        request: main_models.GetSubCrowdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSubCrowdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSubCrowd',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/crowds/{DaraURL.percent_encode(crowd_id)}/subcrowds/{DaraURL.percent_encode(sub_crowd_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSubCrowdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sub_crowd_with_options_async(
        self,
        crowd_id: str,
        sub_crowd_id: str,
        request: main_models.GetSubCrowdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSubCrowdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSubCrowd',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/crowds/{DaraURL.percent_encode(crowd_id)}/subcrowds/{DaraURL.percent_encode(sub_crowd_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSubCrowdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sub_crowd(
        self,
        crowd_id: str,
        sub_crowd_id: str,
        request: main_models.GetSubCrowdRequest,
    ) -> main_models.GetSubCrowdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_sub_crowd_with_options(crowd_id, sub_crowd_id, request, headers, runtime)

    async def get_sub_crowd_async(
        self,
        crowd_id: str,
        sub_crowd_id: str,
        request: main_models.GetSubCrowdRequest,
    ) -> main_models.GetSubCrowdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_sub_crowd_with_options_async(crowd_id, sub_crowd_id, request, headers, runtime)

    def get_table_meta_with_options(
        self,
        table_meta_id: str,
        request: main_models.GetTableMetaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTableMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTableMeta',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tablemetas/{DaraURL.percent_encode(table_meta_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_meta_with_options_async(
        self,
        table_meta_id: str,
        request: main_models.GetTableMetaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTableMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTableMeta',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tablemetas/{DaraURL.percent_encode(table_meta_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_meta(
        self,
        table_meta_id: str,
        request: main_models.GetTableMetaRequest,
    ) -> main_models.GetTableMetaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_table_meta_with_options(table_meta_id, request, headers, runtime)

    async def get_table_meta_async(
        self,
        table_meta_id: str,
        request: main_models.GetTableMetaRequest,
    ) -> main_models.GetTableMetaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_table_meta_with_options_async(table_meta_id, request, headers, runtime)

    def get_traffic_control_target_with_options(
        self,
        traffic_control_target_id: str,
        request: main_models.GetTrafficControlTargetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTrafficControlTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTrafficControlTarget',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltargets/{DaraURL.percent_encode(traffic_control_target_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTrafficControlTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_traffic_control_target_with_options_async(
        self,
        traffic_control_target_id: str,
        request: main_models.GetTrafficControlTargetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTrafficControlTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTrafficControlTarget',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltargets/{DaraURL.percent_encode(traffic_control_target_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTrafficControlTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_traffic_control_target(
        self,
        traffic_control_target_id: str,
        request: main_models.GetTrafficControlTargetRequest,
    ) -> main_models.GetTrafficControlTargetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_traffic_control_target_with_options(traffic_control_target_id, request, headers, runtime)

    async def get_traffic_control_target_async(
        self,
        traffic_control_target_id: str,
        request: main_models.GetTrafficControlTargetRequest,
    ) -> main_models.GetTrafficControlTargetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_traffic_control_target_with_options_async(traffic_control_target_id, request, headers, runtime)

    def get_traffic_control_task_with_options(
        self,
        traffic_control_task_id: str,
        request: main_models.GetTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTrafficControlTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.control_target_filter):
            query['ControlTargetFilter'] = request.control_target_filter
        if not DaraCore.is_null(request.environment):
            query['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTrafficControlTask',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltasks/{DaraURL.percent_encode(traffic_control_task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTrafficControlTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_traffic_control_task_with_options_async(
        self,
        traffic_control_task_id: str,
        request: main_models.GetTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTrafficControlTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.control_target_filter):
            query['ControlTargetFilter'] = request.control_target_filter
        if not DaraCore.is_null(request.environment):
            query['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTrafficControlTask',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltasks/{DaraURL.percent_encode(traffic_control_task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTrafficControlTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_traffic_control_task(
        self,
        traffic_control_task_id: str,
        request: main_models.GetTrafficControlTaskRequest,
    ) -> main_models.GetTrafficControlTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_traffic_control_task_with_options(traffic_control_task_id, request, headers, runtime)

    async def get_traffic_control_task_async(
        self,
        traffic_control_task_id: str,
        request: main_models.GetTrafficControlTaskRequest,
    ) -> main_models.GetTrafficControlTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_traffic_control_task_with_options_async(traffic_control_task_id, request, headers, runtime)

    def get_traffic_control_task_traffic_with_options(
        self,
        traffic_control_task_id: str,
        request: main_models.GetTrafficControlTaskTrafficRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTrafficControlTaskTrafficResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment):
            query['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTrafficControlTaskTraffic',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltasks/{DaraURL.percent_encode(traffic_control_task_id)}/trafficinfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTrafficControlTaskTrafficResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_traffic_control_task_traffic_with_options_async(
        self,
        traffic_control_task_id: str,
        request: main_models.GetTrafficControlTaskTrafficRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTrafficControlTaskTrafficResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment):
            query['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTrafficControlTaskTraffic',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltasks/{DaraURL.percent_encode(traffic_control_task_id)}/trafficinfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTrafficControlTaskTrafficResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_traffic_control_task_traffic(
        self,
        traffic_control_task_id: str,
        request: main_models.GetTrafficControlTaskTrafficRequest,
    ) -> main_models.GetTrafficControlTaskTrafficResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_traffic_control_task_traffic_with_options(traffic_control_task_id, request, headers, runtime)

    async def get_traffic_control_task_traffic_async(
        self,
        traffic_control_task_id: str,
        request: main_models.GetTrafficControlTaskTrafficRequest,
    ) -> main_models.GetTrafficControlTaskTrafficResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_traffic_control_task_traffic_with_options_async(traffic_control_task_id, request, headers, runtime)

    def list_abmetric_groups_with_options(
        self,
        request: main_models.ListABMetricGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListABMetricGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.realtime):
            query['Realtime'] = request.realtime
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListABMetricGroups',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/abmetricgroups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListABMetricGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_abmetric_groups_with_options_async(
        self,
        request: main_models.ListABMetricGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListABMetricGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.realtime):
            query['Realtime'] = request.realtime
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListABMetricGroups',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/abmetricgroups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListABMetricGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_abmetric_groups(
        self,
        request: main_models.ListABMetricGroupsRequest,
    ) -> main_models.ListABMetricGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_abmetric_groups_with_options(request, headers, runtime)

    async def list_abmetric_groups_async(
        self,
        request: main_models.ListABMetricGroupsRequest,
    ) -> main_models.ListABMetricGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_abmetric_groups_with_options_async(request, headers, runtime)

    def list_abmetrics_with_options(
        self,
        request: main_models.ListABMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListABMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.realtime):
            query['Realtime'] = request.realtime
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.table_meta_id):
            query['TableMetaId'] = request.table_meta_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListABMetrics',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/abmetrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListABMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_abmetrics_with_options_async(
        self,
        request: main_models.ListABMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListABMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.realtime):
            query['Realtime'] = request.realtime
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.table_meta_id):
            query['TableMetaId'] = request.table_meta_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListABMetrics',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/abmetrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListABMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_abmetrics(
        self,
        request: main_models.ListABMetricsRequest,
    ) -> main_models.ListABMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_abmetrics_with_options(request, headers, runtime)

    async def list_abmetrics_async(
        self,
        request: main_models.ListABMetricsRequest,
    ) -> main_models.ListABMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_abmetrics_with_options_async(request, headers, runtime)

    def list_calculation_jobs_with_options(
        self,
        request: main_models.ListCalculationJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCalculationJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCalculationJobs',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/calculationjobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCalculationJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_calculation_jobs_with_options_async(
        self,
        request: main_models.ListCalculationJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCalculationJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCalculationJobs',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/calculationjobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCalculationJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_calculation_jobs(
        self,
        request: main_models.ListCalculationJobsRequest,
    ) -> main_models.ListCalculationJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_calculation_jobs_with_options(request, headers, runtime)

    async def list_calculation_jobs_async(
        self,
        request: main_models.ListCalculationJobsRequest,
    ) -> main_models.ListCalculationJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_calculation_jobs_with_options_async(request, headers, runtime)

    def list_crowd_users_with_options(
        self,
        crowd_id: str,
        request: main_models.ListCrowdUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCrowdUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCrowdUsers',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/crowds/{DaraURL.percent_encode(crowd_id)}/users',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCrowdUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_crowd_users_with_options_async(
        self,
        crowd_id: str,
        request: main_models.ListCrowdUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCrowdUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCrowdUsers',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/crowds/{DaraURL.percent_encode(crowd_id)}/users',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCrowdUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_crowd_users(
        self,
        crowd_id: str,
        request: main_models.ListCrowdUsersRequest,
    ) -> main_models.ListCrowdUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_crowd_users_with_options(crowd_id, request, headers, runtime)

    async def list_crowd_users_async(
        self,
        crowd_id: str,
        request: main_models.ListCrowdUsersRequest,
    ) -> main_models.ListCrowdUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_crowd_users_with_options_async(crowd_id, request, headers, runtime)

    def list_crowds_with_options(
        self,
        request: main_models.ListCrowdsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCrowdsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCrowds',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/crowds',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCrowdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_crowds_with_options_async(
        self,
        request: main_models.ListCrowdsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCrowdsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCrowds',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/crowds',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCrowdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_crowds(
        self,
        request: main_models.ListCrowdsRequest,
    ) -> main_models.ListCrowdsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_crowds_with_options(request, headers, runtime)

    async def list_crowds_async(
        self,
        request: main_models.ListCrowdsRequest,
    ) -> main_models.ListCrowdsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_crowds_with_options_async(request, headers, runtime)

    def list_engine_configs_with_options(
        self,
        request: main_models.ListEngineConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEngineConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment):
            query['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEngineConfigs',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/engineconfigs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEngineConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_engine_configs_with_options_async(
        self,
        request: main_models.ListEngineConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEngineConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment):
            query['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEngineConfigs',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/engineconfigs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEngineConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_engine_configs(
        self,
        request: main_models.ListEngineConfigsRequest,
    ) -> main_models.ListEngineConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_engine_configs_with_options(request, headers, runtime)

    async def list_engine_configs_async(
        self,
        request: main_models.ListEngineConfigsRequest,
    ) -> main_models.ListEngineConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_engine_configs_with_options_async(request, headers, runtime)

    def list_experiment_groups_with_options(
        self,
        request: main_models.ListExperimentGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListExperimentGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.layer_id):
            query['LayerId'] = request.layer_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.time_range_end):
            query['TimeRangeEnd'] = request.time_range_end
        if not DaraCore.is_null(request.time_range_start):
            query['TimeRangeStart'] = request.time_range_start
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExperimentGroups',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experimentgroups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExperimentGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_experiment_groups_with_options_async(
        self,
        request: main_models.ListExperimentGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListExperimentGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.layer_id):
            query['LayerId'] = request.layer_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.time_range_end):
            query['TimeRangeEnd'] = request.time_range_end
        if not DaraCore.is_null(request.time_range_start):
            query['TimeRangeStart'] = request.time_range_start
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExperimentGroups',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experimentgroups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExperimentGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_experiment_groups(
        self,
        request: main_models.ListExperimentGroupsRequest,
    ) -> main_models.ListExperimentGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_experiment_groups_with_options(request, headers, runtime)

    async def list_experiment_groups_async(
        self,
        request: main_models.ListExperimentGroupsRequest,
    ) -> main_models.ListExperimentGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_experiment_groups_with_options_async(request, headers, runtime)

    def list_experiments_with_options(
        self,
        request: main_models.ListExperimentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListExperimentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.experiment_group_id):
            query['ExperimentGroupId'] = request.experiment_group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExperiments',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExperimentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_experiments_with_options_async(
        self,
        request: main_models.ListExperimentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListExperimentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.experiment_group_id):
            query['ExperimentGroupId'] = request.experiment_group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExperiments',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExperimentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_experiments(
        self,
        request: main_models.ListExperimentsRequest,
    ) -> main_models.ListExperimentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_experiments_with_options(request, headers, runtime)

    async def list_experiments_async(
        self,
        request: main_models.ListExperimentsRequest,
    ) -> main_models.ListExperimentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_experiments_with_options_async(request, headers, runtime)

    def list_feature_consistency_check_job_configs_with_options(
        self,
        request: main_models.ListFeatureConsistencyCheckJobConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFeatureConsistencyCheckJobConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action = 'ListFeatureConsistencyCheckJobConfigs',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/featureconsistencycheck/jobconfigs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFeatureConsistencyCheckJobConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_feature_consistency_check_job_configs_with_options_async(
        self,
        request: main_models.ListFeatureConsistencyCheckJobConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFeatureConsistencyCheckJobConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action = 'ListFeatureConsistencyCheckJobConfigs',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/featureconsistencycheck/jobconfigs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFeatureConsistencyCheckJobConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_feature_consistency_check_job_configs(
        self,
        request: main_models.ListFeatureConsistencyCheckJobConfigsRequest,
    ) -> main_models.ListFeatureConsistencyCheckJobConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_feature_consistency_check_job_configs_with_options(request, headers, runtime)

    async def list_feature_consistency_check_job_configs_async(
        self,
        request: main_models.ListFeatureConsistencyCheckJobConfigsRequest,
    ) -> main_models.ListFeatureConsistencyCheckJobConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_feature_consistency_check_job_configs_with_options_async(request, headers, runtime)

    def list_feature_consistency_check_job_feature_reports_with_options(
        self,
        feature_consistency_check_job_id: str,
        request: main_models.ListFeatureConsistencyCheckJobFeatureReportsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFeatureConsistencyCheckJobFeatureReportsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.log_item_id):
            query['LogItemId'] = request.log_item_id
        if not DaraCore.is_null(request.log_request_id):
            query['LogRequestId'] = request.log_request_id
        if not DaraCore.is_null(request.log_user_id):
            query['LogUserId'] = request.log_user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFeatureConsistencyCheckJobFeatureReports',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/featureconsistencycheck/jobs/{DaraURL.percent_encode(feature_consistency_check_job_id)}/featurereports',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFeatureConsistencyCheckJobFeatureReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_feature_consistency_check_job_feature_reports_with_options_async(
        self,
        feature_consistency_check_job_id: str,
        request: main_models.ListFeatureConsistencyCheckJobFeatureReportsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFeatureConsistencyCheckJobFeatureReportsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.log_item_id):
            query['LogItemId'] = request.log_item_id
        if not DaraCore.is_null(request.log_request_id):
            query['LogRequestId'] = request.log_request_id
        if not DaraCore.is_null(request.log_user_id):
            query['LogUserId'] = request.log_user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFeatureConsistencyCheckJobFeatureReports',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/featureconsistencycheck/jobs/{DaraURL.percent_encode(feature_consistency_check_job_id)}/featurereports',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFeatureConsistencyCheckJobFeatureReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_feature_consistency_check_job_feature_reports(
        self,
        feature_consistency_check_job_id: str,
        request: main_models.ListFeatureConsistencyCheckJobFeatureReportsRequest,
    ) -> main_models.ListFeatureConsistencyCheckJobFeatureReportsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_feature_consistency_check_job_feature_reports_with_options(feature_consistency_check_job_id, request, headers, runtime)

    async def list_feature_consistency_check_job_feature_reports_async(
        self,
        feature_consistency_check_job_id: str,
        request: main_models.ListFeatureConsistencyCheckJobFeatureReportsRequest,
    ) -> main_models.ListFeatureConsistencyCheckJobFeatureReportsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_feature_consistency_check_job_feature_reports_with_options_async(feature_consistency_check_job_id, request, headers, runtime)

    def list_feature_consistency_check_job_score_reports_with_options(
        self,
        feature_consistency_check_job_id: str,
        tmp_req: main_models.ListFeatureConsistencyCheckJobScoreReportsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFeatureConsistencyCheckJobScoreReportsResponse:
        tmp_req.validate()
        request = main_models.ListFeatureConsistencyCheckJobScoreReportsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.exclude_request_ids):
            request.exclude_request_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.exclude_request_ids, 'ExcludeRequestIds', 'json')
        query = {}
        if not DaraCore.is_null(request.exclude_request_ids_shrink):
            query['ExcludeRequestIds'] = request.exclude_request_ids_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFeatureConsistencyCheckJobScoreReports',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/featureconsistencycheck/jobs/{DaraURL.percent_encode(feature_consistency_check_job_id)}/scorereports',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFeatureConsistencyCheckJobScoreReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_feature_consistency_check_job_score_reports_with_options_async(
        self,
        feature_consistency_check_job_id: str,
        tmp_req: main_models.ListFeatureConsistencyCheckJobScoreReportsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFeatureConsistencyCheckJobScoreReportsResponse:
        tmp_req.validate()
        request = main_models.ListFeatureConsistencyCheckJobScoreReportsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.exclude_request_ids):
            request.exclude_request_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.exclude_request_ids, 'ExcludeRequestIds', 'json')
        query = {}
        if not DaraCore.is_null(request.exclude_request_ids_shrink):
            query['ExcludeRequestIds'] = request.exclude_request_ids_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFeatureConsistencyCheckJobScoreReports',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/featureconsistencycheck/jobs/{DaraURL.percent_encode(feature_consistency_check_job_id)}/scorereports',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFeatureConsistencyCheckJobScoreReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_feature_consistency_check_job_score_reports(
        self,
        feature_consistency_check_job_id: str,
        request: main_models.ListFeatureConsistencyCheckJobScoreReportsRequest,
    ) -> main_models.ListFeatureConsistencyCheckJobScoreReportsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_feature_consistency_check_job_score_reports_with_options(feature_consistency_check_job_id, request, headers, runtime)

    async def list_feature_consistency_check_job_score_reports_async(
        self,
        feature_consistency_check_job_id: str,
        request: main_models.ListFeatureConsistencyCheckJobScoreReportsRequest,
    ) -> main_models.ListFeatureConsistencyCheckJobScoreReportsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_feature_consistency_check_job_score_reports_with_options_async(feature_consistency_check_job_id, request, headers, runtime)

    def list_feature_consistency_check_jobs_with_options(
        self,
        request: main_models.ListFeatureConsistencyCheckJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFeatureConsistencyCheckJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action = 'ListFeatureConsistencyCheckJobs',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/featureconsistencycheck/jobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFeatureConsistencyCheckJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_feature_consistency_check_jobs_with_options_async(
        self,
        request: main_models.ListFeatureConsistencyCheckJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFeatureConsistencyCheckJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action = 'ListFeatureConsistencyCheckJobs',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/featureconsistencycheck/jobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFeatureConsistencyCheckJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_feature_consistency_check_jobs(
        self,
        request: main_models.ListFeatureConsistencyCheckJobsRequest,
    ) -> main_models.ListFeatureConsistencyCheckJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_feature_consistency_check_jobs_with_options(request, headers, runtime)

    async def list_feature_consistency_check_jobs_async(
        self,
        request: main_models.ListFeatureConsistencyCheckJobsRequest,
    ) -> main_models.ListFeatureConsistencyCheckJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_feature_consistency_check_jobs_with_options_async(request, headers, runtime)

    def list_instance_resources_with_options(
        self,
        instance_id: str,
        request: main_models.ListInstanceResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceResources',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/resources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_resources_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListInstanceResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.group):
            query['Group'] = request.group
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceResources',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/resources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_resources(
        self,
        instance_id: str,
        request: main_models.ListInstanceResourcesRequest,
    ) -> main_models.ListInstanceResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_instance_resources_with_options(instance_id, request, headers, runtime)

    async def list_instance_resources_async(
        self,
        instance_id: str,
        request: main_models.ListInstanceResourcesRequest,
    ) -> main_models.ListInstanceResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_instance_resources_with_options_async(instance_id, request, headers, runtime)

    def list_instances_with_options(
        self,
        request: main_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2022-12-13',
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
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2022-12-13',
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

    def list_laboratories_with_options(
        self,
        request: main_models.ListLaboratoriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLaboratoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment):
            query['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLaboratories',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/laboratories',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLaboratoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_laboratories_with_options_async(
        self,
        request: main_models.ListLaboratoriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLaboratoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment):
            query['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLaboratories',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/laboratories',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLaboratoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_laboratories(
        self,
        request: main_models.ListLaboratoriesRequest,
    ) -> main_models.ListLaboratoriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_laboratories_with_options(request, headers, runtime)

    async def list_laboratories_async(
        self,
        request: main_models.ListLaboratoriesRequest,
    ) -> main_models.ListLaboratoriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_laboratories_with_options_async(request, headers, runtime)

    def list_layers_with_options(
        self,
        request: main_models.ListLayersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLayersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.laboratory_id):
            query['LaboratoryId'] = request.laboratory_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLayers',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/layers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLayersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_layers_with_options_async(
        self,
        request: main_models.ListLayersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLayersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.laboratory_id):
            query['LaboratoryId'] = request.laboratory_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLayers',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/layers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLayersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_layers(
        self,
        request: main_models.ListLayersRequest,
    ) -> main_models.ListLayersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_layers_with_options(request, headers, runtime)

    async def list_layers_async(
        self,
        request: main_models.ListLayersRequest,
    ) -> main_models.ListLayersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_layers_with_options_async(request, headers, runtime)

    def list_params_with_options(
        self,
        request: main_models.ListParamsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListParamsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encrypted):
            query['Encrypted'] = request.encrypted
        if not DaraCore.is_null(request.environment):
            query['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListParams',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/params',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListParamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_params_with_options_async(
        self,
        request: main_models.ListParamsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListParamsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encrypted):
            query['Encrypted'] = request.encrypted
        if not DaraCore.is_null(request.environment):
            query['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListParams',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/params',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListParamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_params(
        self,
        request: main_models.ListParamsRequest,
    ) -> main_models.ListParamsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_params_with_options(request, headers, runtime)

    async def list_params_async(
        self,
        request: main_models.ListParamsRequest,
    ) -> main_models.ListParamsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_params_with_options_async(request, headers, runtime)

    def list_recall_management_jobs_with_options(
        self,
        request: main_models.ListRecallManagementJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRecallManagementJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.condition):
            query['Condition'] = request.condition
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
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
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRecallManagementJobs',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementjobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecallManagementJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_recall_management_jobs_with_options_async(
        self,
        request: main_models.ListRecallManagementJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRecallManagementJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.condition):
            query['Condition'] = request.condition
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
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
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRecallManagementJobs',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementjobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecallManagementJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_recall_management_jobs(
        self,
        request: main_models.ListRecallManagementJobsRequest,
    ) -> main_models.ListRecallManagementJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_recall_management_jobs_with_options(request, headers, runtime)

    async def list_recall_management_jobs_async(
        self,
        request: main_models.ListRecallManagementJobsRequest,
    ) -> main_models.ListRecallManagementJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_recall_management_jobs_with_options_async(request, headers, runtime)

    def list_recall_management_service_versions_with_options(
        self,
        recall_management_service_id: str,
        request: main_models.ListRecallManagementServiceVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRecallManagementServiceVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action = 'ListRecallManagementServiceVersions',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices/{DaraURL.percent_encode(recall_management_service_id)}/versions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecallManagementServiceVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_recall_management_service_versions_with_options_async(
        self,
        recall_management_service_id: str,
        request: main_models.ListRecallManagementServiceVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRecallManagementServiceVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action = 'ListRecallManagementServiceVersions',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices/{DaraURL.percent_encode(recall_management_service_id)}/versions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecallManagementServiceVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_recall_management_service_versions(
        self,
        recall_management_service_id: str,
        request: main_models.ListRecallManagementServiceVersionsRequest,
    ) -> main_models.ListRecallManagementServiceVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_recall_management_service_versions_with_options(recall_management_service_id, request, headers, runtime)

    async def list_recall_management_service_versions_async(
        self,
        recall_management_service_id: str,
        request: main_models.ListRecallManagementServiceVersionsRequest,
    ) -> main_models.ListRecallManagementServiceVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_recall_management_service_versions_with_options_async(recall_management_service_id, request, headers, runtime)

    def list_recall_management_services_with_options(
        self,
        request: main_models.ListRecallManagementServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRecallManagementServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
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
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRecallManagementServices',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecallManagementServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_recall_management_services_with_options_async(
        self,
        request: main_models.ListRecallManagementServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRecallManagementServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
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
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRecallManagementServices',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecallManagementServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_recall_management_services(
        self,
        request: main_models.ListRecallManagementServicesRequest,
    ) -> main_models.ListRecallManagementServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_recall_management_services_with_options(request, headers, runtime)

    async def list_recall_management_services_async(
        self,
        request: main_models.ListRecallManagementServicesRequest,
    ) -> main_models.ListRecallManagementServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_recall_management_services_with_options_async(request, headers, runtime)

    def list_recall_management_table_versions_with_options(
        self,
        recall_management_table_id: str,
        request: main_models.ListRecallManagementTableVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRecallManagementTableVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action = 'ListRecallManagementTableVersions',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementtables/{DaraURL.percent_encode(recall_management_table_id)}/versions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecallManagementTableVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_recall_management_table_versions_with_options_async(
        self,
        recall_management_table_id: str,
        request: main_models.ListRecallManagementTableVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRecallManagementTableVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action = 'ListRecallManagementTableVersions',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementtables/{DaraURL.percent_encode(recall_management_table_id)}/versions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecallManagementTableVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_recall_management_table_versions(
        self,
        recall_management_table_id: str,
        request: main_models.ListRecallManagementTableVersionsRequest,
    ) -> main_models.ListRecallManagementTableVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_recall_management_table_versions_with_options(recall_management_table_id, request, headers, runtime)

    async def list_recall_management_table_versions_async(
        self,
        recall_management_table_id: str,
        request: main_models.ListRecallManagementTableVersionsRequest,
    ) -> main_models.ListRecallManagementTableVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_recall_management_table_versions_with_options_async(recall_management_table_id, request, headers, runtime)

    def list_recall_management_tables_with_options(
        self,
        request: main_models.ListRecallManagementTablesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRecallManagementTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRecallManagementTables',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementtables',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecallManagementTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_recall_management_tables_with_options_async(
        self,
        request: main_models.ListRecallManagementTablesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRecallManagementTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRecallManagementTables',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementtables',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecallManagementTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_recall_management_tables(
        self,
        request: main_models.ListRecallManagementTablesRequest,
    ) -> main_models.ListRecallManagementTablesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_recall_management_tables_with_options(request, headers, runtime)

    async def list_recall_management_tables_async(
        self,
        request: main_models.ListRecallManagementTablesRequest,
    ) -> main_models.ListRecallManagementTablesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_recall_management_tables_with_options_async(request, headers, runtime)

    def list_resource_rules_with_options(
        self,
        request: main_models.ListResourceRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_rule_id):
            query['ResourceRuleId'] = request.resource_rule_id
        if not DaraCore.is_null(request.resource_rule_name):
            query['ResourceRuleName'] = request.resource_rule_name
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceRules',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resourcerules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_rules_with_options_async(
        self,
        request: main_models.ListResourceRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_rule_id):
            query['ResourceRuleId'] = request.resource_rule_id
        if not DaraCore.is_null(request.resource_rule_name):
            query['ResourceRuleName'] = request.resource_rule_name
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceRules',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resourcerules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_rules(
        self,
        request: main_models.ListResourceRulesRequest,
    ) -> main_models.ListResourceRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_resource_rules_with_options(request, headers, runtime)

    async def list_resource_rules_async(
        self,
        request: main_models.ListResourceRulesRequest,
    ) -> main_models.ListResourceRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_resource_rules_with_options_async(request, headers, runtime)

    def list_sample_consistency_jobs_with_options(
        self,
        request: main_models.ListSampleConsistencyJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSampleConsistencyJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action = 'ListSampleConsistencyJobs',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sampleconsistencyjobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSampleConsistencyJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sample_consistency_jobs_with_options_async(
        self,
        request: main_models.ListSampleConsistencyJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSampleConsistencyJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action = 'ListSampleConsistencyJobs',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sampleconsistencyjobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSampleConsistencyJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sample_consistency_jobs(
        self,
        request: main_models.ListSampleConsistencyJobsRequest,
    ) -> main_models.ListSampleConsistencyJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_sample_consistency_jobs_with_options(request, headers, runtime)

    async def list_sample_consistency_jobs_async(
        self,
        request: main_models.ListSampleConsistencyJobsRequest,
    ) -> main_models.ListSampleConsistencyJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_sample_consistency_jobs_with_options_async(request, headers, runtime)

    def list_scenes_with_options(
        self,
        request: main_models.ListScenesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListScenesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScenes',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/scenes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScenesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scenes_with_options_async(
        self,
        request: main_models.ListScenesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListScenesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScenes',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/scenes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScenesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scenes(
        self,
        request: main_models.ListScenesRequest,
    ) -> main_models.ListScenesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_scenes_with_options(request, headers, runtime)

    async def list_scenes_async(
        self,
        request: main_models.ListScenesRequest,
    ) -> main_models.ListScenesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_scenes_with_options_async(request, headers, runtime)

    def list_sub_crowds_with_options(
        self,
        crowd_id: str,
        request: main_models.ListSubCrowdsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSubCrowdsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSubCrowds',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/crowds/{DaraURL.percent_encode(crowd_id)}/subcrowds',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubCrowdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sub_crowds_with_options_async(
        self,
        crowd_id: str,
        request: main_models.ListSubCrowdsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSubCrowdsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSubCrowds',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/crowds/{DaraURL.percent_encode(crowd_id)}/subcrowds',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubCrowdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sub_crowds(
        self,
        crowd_id: str,
        request: main_models.ListSubCrowdsRequest,
    ) -> main_models.ListSubCrowdsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_sub_crowds_with_options(crowd_id, request, headers, runtime)

    async def list_sub_crowds_async(
        self,
        crowd_id: str,
        request: main_models.ListSubCrowdsRequest,
    ) -> main_models.ListSubCrowdsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_sub_crowds_with_options_async(crowd_id, request, headers, runtime)

    def list_table_metas_with_options(
        self,
        request: main_models.ListTableMetasRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTableMetasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module):
            query['Module'] = request.module
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTableMetas',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tablemetas',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTableMetasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_table_metas_with_options_async(
        self,
        request: main_models.ListTableMetasRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTableMetasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module):
            query['Module'] = request.module
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTableMetas',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tablemetas',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTableMetasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_table_metas(
        self,
        request: main_models.ListTableMetasRequest,
    ) -> main_models.ListTableMetasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_table_metas_with_options(request, headers, runtime)

    async def list_table_metas_async(
        self,
        request: main_models.ListTableMetasRequest,
    ) -> main_models.ListTableMetasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_table_metas_with_options_async(request, headers, runtime)

    def list_traffic_control_target_traffic_history_with_options(
        self,
        traffic_control_target_id: str,
        request: main_models.ListTrafficControlTargetTrafficHistoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTrafficControlTargetTrafficHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.environment):
            query['Environment'] = request.environment
        if not DaraCore.is_null(request.experiment_group_id):
            query['ExperimentGroupId'] = request.experiment_group_id
        if not DaraCore.is_null(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.item_id):
            query['ItemId'] = request.item_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTrafficControlTargetTrafficHistory',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltargets/{DaraURL.percent_encode(traffic_control_target_id)}/traffichistories',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTrafficControlTargetTrafficHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_traffic_control_target_traffic_history_with_options_async(
        self,
        traffic_control_target_id: str,
        request: main_models.ListTrafficControlTargetTrafficHistoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTrafficControlTargetTrafficHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.environment):
            query['Environment'] = request.environment
        if not DaraCore.is_null(request.experiment_group_id):
            query['ExperimentGroupId'] = request.experiment_group_id
        if not DaraCore.is_null(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.item_id):
            query['ItemId'] = request.item_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTrafficControlTargetTrafficHistory',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltargets/{DaraURL.percent_encode(traffic_control_target_id)}/traffichistories',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTrafficControlTargetTrafficHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_traffic_control_target_traffic_history(
        self,
        traffic_control_target_id: str,
        request: main_models.ListTrafficControlTargetTrafficHistoryRequest,
    ) -> main_models.ListTrafficControlTargetTrafficHistoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_traffic_control_target_traffic_history_with_options(traffic_control_target_id, request, headers, runtime)

    async def list_traffic_control_target_traffic_history_async(
        self,
        traffic_control_target_id: str,
        request: main_models.ListTrafficControlTargetTrafficHistoryRequest,
    ) -> main_models.ListTrafficControlTargetTrafficHistoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_traffic_control_target_traffic_history_with_options_async(traffic_control_target_id, request, headers, runtime)

    def list_traffic_control_tasks_with_options(
        self,
        request: main_models.ListTrafficControlTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTrafficControlTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.control_target_filter):
            query['ControlTargetFilter'] = request.control_target_filter
        if not DaraCore.is_null(request.environment):
            query['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.traffic_control_task_id):
            query['TrafficControlTaskId'] = request.traffic_control_task_id
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTrafficControlTasks',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTrafficControlTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_traffic_control_tasks_with_options_async(
        self,
        request: main_models.ListTrafficControlTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTrafficControlTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.control_target_filter):
            query['ControlTargetFilter'] = request.control_target_filter
        if not DaraCore.is_null(request.environment):
            query['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.traffic_control_task_id):
            query['TrafficControlTaskId'] = request.traffic_control_task_id
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTrafficControlTasks',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTrafficControlTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_traffic_control_tasks(
        self,
        request: main_models.ListTrafficControlTasksRequest,
    ) -> main_models.ListTrafficControlTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_traffic_control_tasks_with_options(request, headers, runtime)

    async def list_traffic_control_tasks_async(
        self,
        request: main_models.ListTrafficControlTasksRequest,
    ) -> main_models.ListTrafficControlTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_traffic_control_tasks_with_options_async(request, headers, runtime)

    def offline_experiment_with_options(
        self,
        experiment_id: str,
        request: main_models.OfflineExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OfflineExperimentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OfflineExperiment',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(experiment_id)}/action/offline',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OfflineExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def offline_experiment_with_options_async(
        self,
        experiment_id: str,
        request: main_models.OfflineExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OfflineExperimentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OfflineExperiment',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(experiment_id)}/action/offline',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OfflineExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def offline_experiment(
        self,
        experiment_id: str,
        request: main_models.OfflineExperimentRequest,
    ) -> main_models.OfflineExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.offline_experiment_with_options(experiment_id, request, headers, runtime)

    async def offline_experiment_async(
        self,
        experiment_id: str,
        request: main_models.OfflineExperimentRequest,
    ) -> main_models.OfflineExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.offline_experiment_with_options_async(experiment_id, request, headers, runtime)

    def offline_experiment_group_with_options(
        self,
        experiment_group_id: str,
        request: main_models.OfflineExperimentGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OfflineExperimentGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OfflineExperimentGroup',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experimentgroups/{DaraURL.percent_encode(experiment_group_id)}/action/offline',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OfflineExperimentGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def offline_experiment_group_with_options_async(
        self,
        experiment_group_id: str,
        request: main_models.OfflineExperimentGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OfflineExperimentGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OfflineExperimentGroup',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experimentgroups/{DaraURL.percent_encode(experiment_group_id)}/action/offline',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OfflineExperimentGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def offline_experiment_group(
        self,
        experiment_group_id: str,
        request: main_models.OfflineExperimentGroupRequest,
    ) -> main_models.OfflineExperimentGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.offline_experiment_group_with_options(experiment_group_id, request, headers, runtime)

    async def offline_experiment_group_async(
        self,
        experiment_group_id: str,
        request: main_models.OfflineExperimentGroupRequest,
    ) -> main_models.OfflineExperimentGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.offline_experiment_group_with_options_async(experiment_group_id, request, headers, runtime)

    def offline_laboratory_with_options(
        self,
        laboratory_id: str,
        request: main_models.OfflineLaboratoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OfflineLaboratoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OfflineLaboratory',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/laboratories/{DaraURL.percent_encode(laboratory_id)}/action/offline',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OfflineLaboratoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def offline_laboratory_with_options_async(
        self,
        laboratory_id: str,
        request: main_models.OfflineLaboratoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OfflineLaboratoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OfflineLaboratory',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/laboratories/{DaraURL.percent_encode(laboratory_id)}/action/offline',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OfflineLaboratoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def offline_laboratory(
        self,
        laboratory_id: str,
        request: main_models.OfflineLaboratoryRequest,
    ) -> main_models.OfflineLaboratoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.offline_laboratory_with_options(laboratory_id, request, headers, runtime)

    async def offline_laboratory_async(
        self,
        laboratory_id: str,
        request: main_models.OfflineLaboratoryRequest,
    ) -> main_models.OfflineLaboratoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.offline_laboratory_with_options_async(laboratory_id, request, headers, runtime)

    def offline_recall_management_service_with_options(
        self,
        recall_management_service_id: str,
        request: main_models.OfflineRecallManagementServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OfflineRecallManagementServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OfflineRecallManagementService',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices/{DaraURL.percent_encode(recall_management_service_id)}/action/offline',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OfflineRecallManagementServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def offline_recall_management_service_with_options_async(
        self,
        recall_management_service_id: str,
        request: main_models.OfflineRecallManagementServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OfflineRecallManagementServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OfflineRecallManagementService',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices/{DaraURL.percent_encode(recall_management_service_id)}/action/offline',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OfflineRecallManagementServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def offline_recall_management_service(
        self,
        recall_management_service_id: str,
        request: main_models.OfflineRecallManagementServiceRequest,
    ) -> main_models.OfflineRecallManagementServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.offline_recall_management_service_with_options(recall_management_service_id, request, headers, runtime)

    async def offline_recall_management_service_async(
        self,
        recall_management_service_id: str,
        request: main_models.OfflineRecallManagementServiceRequest,
    ) -> main_models.OfflineRecallManagementServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.offline_recall_management_service_with_options_async(recall_management_service_id, request, headers, runtime)

    def online_experiment_with_options(
        self,
        experiment_id: str,
        request: main_models.OnlineExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OnlineExperimentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OnlineExperiment',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(experiment_id)}/action/online',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnlineExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def online_experiment_with_options_async(
        self,
        experiment_id: str,
        request: main_models.OnlineExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OnlineExperimentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OnlineExperiment',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(experiment_id)}/action/online',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnlineExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def online_experiment(
        self,
        experiment_id: str,
        request: main_models.OnlineExperimentRequest,
    ) -> main_models.OnlineExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.online_experiment_with_options(experiment_id, request, headers, runtime)

    async def online_experiment_async(
        self,
        experiment_id: str,
        request: main_models.OnlineExperimentRequest,
    ) -> main_models.OnlineExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.online_experiment_with_options_async(experiment_id, request, headers, runtime)

    def online_experiment_group_with_options(
        self,
        experiment_group_id: str,
        request: main_models.OnlineExperimentGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OnlineExperimentGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OnlineExperimentGroup',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experimentgroups/{DaraURL.percent_encode(experiment_group_id)}/action/online',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnlineExperimentGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def online_experiment_group_with_options_async(
        self,
        experiment_group_id: str,
        request: main_models.OnlineExperimentGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OnlineExperimentGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OnlineExperimentGroup',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experimentgroups/{DaraURL.percent_encode(experiment_group_id)}/action/online',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnlineExperimentGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def online_experiment_group(
        self,
        experiment_group_id: str,
        request: main_models.OnlineExperimentGroupRequest,
    ) -> main_models.OnlineExperimentGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.online_experiment_group_with_options(experiment_group_id, request, headers, runtime)

    async def online_experiment_group_async(
        self,
        experiment_group_id: str,
        request: main_models.OnlineExperimentGroupRequest,
    ) -> main_models.OnlineExperimentGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.online_experiment_group_with_options_async(experiment_group_id, request, headers, runtime)

    def online_laboratory_with_options(
        self,
        laboratory_id: str,
        request: main_models.OnlineLaboratoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OnlineLaboratoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OnlineLaboratory',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/laboratories/{DaraURL.percent_encode(laboratory_id)}/action/online',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnlineLaboratoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def online_laboratory_with_options_async(
        self,
        laboratory_id: str,
        request: main_models.OnlineLaboratoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OnlineLaboratoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OnlineLaboratory',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/laboratories/{DaraURL.percent_encode(laboratory_id)}/action/online',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnlineLaboratoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def online_laboratory(
        self,
        laboratory_id: str,
        request: main_models.OnlineLaboratoryRequest,
    ) -> main_models.OnlineLaboratoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.online_laboratory_with_options(laboratory_id, request, headers, runtime)

    async def online_laboratory_async(
        self,
        laboratory_id: str,
        request: main_models.OnlineLaboratoryRequest,
    ) -> main_models.OnlineLaboratoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.online_laboratory_with_options_async(laboratory_id, request, headers, runtime)

    def online_recall_management_service_with_options(
        self,
        recall_management_service_id: str,
        request: main_models.OnlineRecallManagementServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OnlineRecallManagementServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OnlineRecallManagementService',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices/{DaraURL.percent_encode(recall_management_service_id)}/action/online',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnlineRecallManagementServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def online_recall_management_service_with_options_async(
        self,
        recall_management_service_id: str,
        request: main_models.OnlineRecallManagementServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OnlineRecallManagementServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OnlineRecallManagementService',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices/{DaraURL.percent_encode(recall_management_service_id)}/action/online',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnlineRecallManagementServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def online_recall_management_service(
        self,
        recall_management_service_id: str,
        request: main_models.OnlineRecallManagementServiceRequest,
    ) -> main_models.OnlineRecallManagementServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.online_recall_management_service_with_options(recall_management_service_id, request, headers, runtime)

    async def online_recall_management_service_async(
        self,
        recall_management_service_id: str,
        request: main_models.OnlineRecallManagementServiceRequest,
    ) -> main_models.OnlineRecallManagementServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.online_recall_management_service_with_options_async(recall_management_service_id, request, headers, runtime)

    def publish_recall_management_table_with_options(
        self,
        recall_management_table_id: str,
        request: main_models.PublishRecallManagementTableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PublishRecallManagementTableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mode):
            body['Mode'] = request.mode
        if not DaraCore.is_null(request.partition):
            body['Partition'] = request.partition
        if not DaraCore.is_null(request.skip_threshold_check):
            body['SkipThresholdCheck'] = request.skip_threshold_check
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PublishRecallManagementTable',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementtables/{DaraURL.percent_encode(recall_management_table_id)}/action/publish',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishRecallManagementTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_recall_management_table_with_options_async(
        self,
        recall_management_table_id: str,
        request: main_models.PublishRecallManagementTableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PublishRecallManagementTableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mode):
            body['Mode'] = request.mode
        if not DaraCore.is_null(request.partition):
            body['Partition'] = request.partition
        if not DaraCore.is_null(request.skip_threshold_check):
            body['SkipThresholdCheck'] = request.skip_threshold_check
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PublishRecallManagementTable',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementtables/{DaraURL.percent_encode(recall_management_table_id)}/action/publish',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishRecallManagementTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_recall_management_table(
        self,
        recall_management_table_id: str,
        request: main_models.PublishRecallManagementTableRequest,
    ) -> main_models.PublishRecallManagementTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.publish_recall_management_table_with_options(recall_management_table_id, request, headers, runtime)

    async def publish_recall_management_table_async(
        self,
        recall_management_table_id: str,
        request: main_models.PublishRecallManagementTableRequest,
    ) -> main_models.PublishRecallManagementTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.publish_recall_management_table_with_options_async(recall_management_table_id, request, headers, runtime)

    def push_all_experiment_with_options(
        self,
        experiment_id: str,
        request: main_models.PushAllExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PushAllExperimentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushAllExperiment',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(experiment_id)}/action/pushall',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushAllExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_all_experiment_with_options_async(
        self,
        experiment_id: str,
        request: main_models.PushAllExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PushAllExperimentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushAllExperiment',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(experiment_id)}/action/pushall',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushAllExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_all_experiment(
        self,
        experiment_id: str,
        request: main_models.PushAllExperimentRequest,
    ) -> main_models.PushAllExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.push_all_experiment_with_options(experiment_id, request, headers, runtime)

    async def push_all_experiment_async(
        self,
        experiment_id: str,
        request: main_models.PushAllExperimentRequest,
    ) -> main_models.PushAllExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.push_all_experiment_with_options_async(experiment_id, request, headers, runtime)

    def push_resource_rule_with_options(
        self,
        resource_rule_id: str,
        tmp_req: main_models.PushResourceRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PushResourceRuleResponse:
        tmp_req.validate()
        request = main_models.PushResourceRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.metric_info):
            request.metric_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.metric_info, 'MetricInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.metric_info_shrink):
            query['MetricInfo'] = request.metric_info_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PushResourceRule',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resourcerules/{DaraURL.percent_encode(resource_rule_id)}/action/push',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushResourceRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_resource_rule_with_options_async(
        self,
        resource_rule_id: str,
        tmp_req: main_models.PushResourceRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PushResourceRuleResponse:
        tmp_req.validate()
        request = main_models.PushResourceRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.metric_info):
            request.metric_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.metric_info, 'MetricInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.metric_info_shrink):
            query['MetricInfo'] = request.metric_info_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PushResourceRule',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resourcerules/{DaraURL.percent_encode(resource_rule_id)}/action/push',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushResourceRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_resource_rule(
        self,
        resource_rule_id: str,
        request: main_models.PushResourceRuleRequest,
    ) -> main_models.PushResourceRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.push_resource_rule_with_options(resource_rule_id, request, headers, runtime)

    async def push_resource_rule_async(
        self,
        resource_rule_id: str,
        request: main_models.PushResourceRuleRequest,
    ) -> main_models.PushResourceRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.push_resource_rule_with_options_async(resource_rule_id, request, headers, runtime)

    def query_sample_consistency_job_difference_with_options(
        self,
        sample_consistency_job_id: str,
        request: main_models.QuerySampleConsistencyJobDifferenceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QuerySampleConsistencyJobDifferenceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySampleConsistencyJobDifference',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sampleconsistencyjobs/{DaraURL.percent_encode(sample_consistency_job_id)}/action/querydifference',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySampleConsistencyJobDifferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sample_consistency_job_difference_with_options_async(
        self,
        sample_consistency_job_id: str,
        request: main_models.QuerySampleConsistencyJobDifferenceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QuerySampleConsistencyJobDifferenceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySampleConsistencyJobDifference',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sampleconsistencyjobs/{DaraURL.percent_encode(sample_consistency_job_id)}/action/querydifference',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySampleConsistencyJobDifferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sample_consistency_job_difference(
        self,
        sample_consistency_job_id: str,
        request: main_models.QuerySampleConsistencyJobDifferenceRequest,
    ) -> main_models.QuerySampleConsistencyJobDifferenceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_sample_consistency_job_difference_with_options(sample_consistency_job_id, request, headers, runtime)

    async def query_sample_consistency_job_difference_async(
        self,
        sample_consistency_job_id: str,
        request: main_models.QuerySampleConsistencyJobDifferenceRequest,
    ) -> main_models.QuerySampleConsistencyJobDifferenceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_sample_consistency_job_difference_with_options_async(sample_consistency_job_id, request, headers, runtime)

    def query_traffic_control_target_item_report_detail_with_options(
        self,
        traffic_control_target_id: str,
        request: main_models.QueryTrafficControlTargetItemReportDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryTrafficControlTargetItemReportDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.date):
            query['Date'] = request.date
        if not DaraCore.is_null(request.environment):
            query['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTrafficControlTargetItemReportDetail',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltargets/{DaraURL.percent_encode(traffic_control_target_id)}/itemcontrolreportdetail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTrafficControlTargetItemReportDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_traffic_control_target_item_report_detail_with_options_async(
        self,
        traffic_control_target_id: str,
        request: main_models.QueryTrafficControlTargetItemReportDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryTrafficControlTargetItemReportDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.date):
            query['Date'] = request.date
        if not DaraCore.is_null(request.environment):
            query['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTrafficControlTargetItemReportDetail',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltargets/{DaraURL.percent_encode(traffic_control_target_id)}/itemcontrolreportdetail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTrafficControlTargetItemReportDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_traffic_control_target_item_report_detail(
        self,
        traffic_control_target_id: str,
        request: main_models.QueryTrafficControlTargetItemReportDetailRequest,
    ) -> main_models.QueryTrafficControlTargetItemReportDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_traffic_control_target_item_report_detail_with_options(traffic_control_target_id, request, headers, runtime)

    async def query_traffic_control_target_item_report_detail_async(
        self,
        traffic_control_target_id: str,
        request: main_models.QueryTrafficControlTargetItemReportDetailRequest,
    ) -> main_models.QueryTrafficControlTargetItemReportDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_traffic_control_target_item_report_detail_with_options_async(traffic_control_target_id, request, headers, runtime)

    def release_traffic_control_task_with_options(
        self,
        traffic_control_task_id: str,
        request: main_models.ReleaseTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseTrafficControlTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseTrafficControlTask',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltasks/{DaraURL.percent_encode(traffic_control_task_id)}/action/release',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseTrafficControlTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_traffic_control_task_with_options_async(
        self,
        traffic_control_task_id: str,
        request: main_models.ReleaseTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseTrafficControlTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseTrafficControlTask',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltasks/{DaraURL.percent_encode(traffic_control_task_id)}/action/release',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseTrafficControlTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_traffic_control_task(
        self,
        traffic_control_task_id: str,
        request: main_models.ReleaseTrafficControlTaskRequest,
    ) -> main_models.ReleaseTrafficControlTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.release_traffic_control_task_with_options(traffic_control_task_id, request, headers, runtime)

    async def release_traffic_control_task_async(
        self,
        traffic_control_task_id: str,
        request: main_models.ReleaseTrafficControlTaskRequest,
    ) -> main_models.ReleaseTrafficControlTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.release_traffic_control_task_with_options_async(traffic_control_task_id, request, headers, runtime)

    def report_abmetric_group_with_options(
        self,
        abmetric_group_id: str,
        request: main_models.ReportABMetricGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReportABMetricGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.base_experiment_id):
            body['BaseExperimentId'] = request.base_experiment_id
        if not DaraCore.is_null(request.dimension_fields):
            body['DimensionFields'] = request.dimension_fields
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.experiment_group_id):
            body['ExperimentGroupId'] = request.experiment_group_id
        if not DaraCore.is_null(request.experiment_ids):
            body['ExperimentIds'] = request.experiment_ids
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.report_type):
            body['ReportType'] = request.report_type
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        if not DaraCore.is_null(request.time_statistics_method):
            body['TimeStatisticsMethod'] = request.time_statistics_method
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReportABMetricGroup',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/abmetricgroups/{DaraURL.percent_encode(abmetric_group_id)}/action/report',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReportABMetricGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_abmetric_group_with_options_async(
        self,
        abmetric_group_id: str,
        request: main_models.ReportABMetricGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReportABMetricGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.base_experiment_id):
            body['BaseExperimentId'] = request.base_experiment_id
        if not DaraCore.is_null(request.dimension_fields):
            body['DimensionFields'] = request.dimension_fields
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.experiment_group_id):
            body['ExperimentGroupId'] = request.experiment_group_id
        if not DaraCore.is_null(request.experiment_ids):
            body['ExperimentIds'] = request.experiment_ids
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.report_type):
            body['ReportType'] = request.report_type
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        if not DaraCore.is_null(request.time_statistics_method):
            body['TimeStatisticsMethod'] = request.time_statistics_method
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReportABMetricGroup',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/abmetricgroups/{DaraURL.percent_encode(abmetric_group_id)}/action/report',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReportABMetricGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_abmetric_group(
        self,
        abmetric_group_id: str,
        request: main_models.ReportABMetricGroupRequest,
    ) -> main_models.ReportABMetricGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.report_abmetric_group_with_options(abmetric_group_id, request, headers, runtime)

    async def report_abmetric_group_async(
        self,
        abmetric_group_id: str,
        request: main_models.ReportABMetricGroupRequest,
    ) -> main_models.ReportABMetricGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.report_abmetric_group_with_options_async(abmetric_group_id, request, headers, runtime)

    def report_sample_consistency_job_with_options(
        self,
        sample_consistency_job_id: str,
        request: main_models.ReportSampleConsistencyJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReportSampleConsistencyJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReportSampleConsistencyJob',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sampleconsistencyjobs/{DaraURL.percent_encode(sample_consistency_job_id)}/action/report',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReportSampleConsistencyJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_sample_consistency_job_with_options_async(
        self,
        sample_consistency_job_id: str,
        request: main_models.ReportSampleConsistencyJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReportSampleConsistencyJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReportSampleConsistencyJob',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sampleconsistencyjobs/{DaraURL.percent_encode(sample_consistency_job_id)}/action/report',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReportSampleConsistencyJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_sample_consistency_job(
        self,
        sample_consistency_job_id: str,
        request: main_models.ReportSampleConsistencyJobRequest,
    ) -> main_models.ReportSampleConsistencyJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.report_sample_consistency_job_with_options(sample_consistency_job_id, request, headers, runtime)

    async def report_sample_consistency_job_async(
        self,
        sample_consistency_job_id: str,
        request: main_models.ReportSampleConsistencyJobRequest,
    ) -> main_models.ReportSampleConsistencyJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.report_sample_consistency_job_with_options_async(sample_consistency_job_id, request, headers, runtime)

    def split_traffic_control_target_with_options(
        self,
        traffic_control_target_id: str,
        request: main_models.SplitTrafficControlTargetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SplitTrafficControlTargetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.set_points):
            body['SetPoints'] = request.set_points
        if not DaraCore.is_null(request.set_values):
            body['SetValues'] = request.set_values
        if not DaraCore.is_null(request.time_points):
            body['TimePoints'] = request.time_points
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SplitTrafficControlTarget',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltargets/{DaraURL.percent_encode(traffic_control_target_id)}/action/split',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SplitTrafficControlTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def split_traffic_control_target_with_options_async(
        self,
        traffic_control_target_id: str,
        request: main_models.SplitTrafficControlTargetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SplitTrafficControlTargetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.set_points):
            body['SetPoints'] = request.set_points
        if not DaraCore.is_null(request.set_values):
            body['SetValues'] = request.set_values
        if not DaraCore.is_null(request.time_points):
            body['TimePoints'] = request.time_points
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SplitTrafficControlTarget',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltargets/{DaraURL.percent_encode(traffic_control_target_id)}/action/split',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SplitTrafficControlTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def split_traffic_control_target(
        self,
        traffic_control_target_id: str,
        request: main_models.SplitTrafficControlTargetRequest,
    ) -> main_models.SplitTrafficControlTargetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.split_traffic_control_target_with_options(traffic_control_target_id, request, headers, runtime)

    async def split_traffic_control_target_async(
        self,
        traffic_control_target_id: str,
        request: main_models.SplitTrafficControlTargetRequest,
    ) -> main_models.SplitTrafficControlTargetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.split_traffic_control_target_with_options_async(traffic_control_target_id, request, headers, runtime)

    def start_traffic_control_target_with_options(
        self,
        traffic_control_target_id: str,
        request: main_models.StartTrafficControlTargetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartTrafficControlTargetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartTrafficControlTarget',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltargets/{DaraURL.percent_encode(traffic_control_target_id)}/action/start',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartTrafficControlTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_traffic_control_target_with_options_async(
        self,
        traffic_control_target_id: str,
        request: main_models.StartTrafficControlTargetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartTrafficControlTargetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartTrafficControlTarget',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltargets/{DaraURL.percent_encode(traffic_control_target_id)}/action/start',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartTrafficControlTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_traffic_control_target(
        self,
        traffic_control_target_id: str,
        request: main_models.StartTrafficControlTargetRequest,
    ) -> main_models.StartTrafficControlTargetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_traffic_control_target_with_options(traffic_control_target_id, request, headers, runtime)

    async def start_traffic_control_target_async(
        self,
        traffic_control_target_id: str,
        request: main_models.StartTrafficControlTargetRequest,
    ) -> main_models.StartTrafficControlTargetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_traffic_control_target_with_options_async(traffic_control_target_id, request, headers, runtime)

    def start_traffic_control_task_with_options(
        self,
        traffic_control_task_id: str,
        request: main_models.StartTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartTrafficControlTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartTrafficControlTask',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltasks/{DaraURL.percent_encode(traffic_control_task_id)}/action/start',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartTrafficControlTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_traffic_control_task_with_options_async(
        self,
        traffic_control_task_id: str,
        request: main_models.StartTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartTrafficControlTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartTrafficControlTask',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltasks/{DaraURL.percent_encode(traffic_control_task_id)}/action/start',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartTrafficControlTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_traffic_control_task(
        self,
        traffic_control_task_id: str,
        request: main_models.StartTrafficControlTaskRequest,
    ) -> main_models.StartTrafficControlTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_traffic_control_task_with_options(traffic_control_task_id, request, headers, runtime)

    async def start_traffic_control_task_async(
        self,
        traffic_control_task_id: str,
        request: main_models.StartTrafficControlTaskRequest,
    ) -> main_models.StartTrafficControlTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_traffic_control_task_with_options_async(traffic_control_task_id, request, headers, runtime)

    def stop_sample_consistency_job_with_options(
        self,
        sample_consistency_job_id: str,
        request: main_models.StopSampleConsistencyJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopSampleConsistencyJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopSampleConsistencyJob',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sampleconsistencyjobs/{DaraURL.percent_encode(sample_consistency_job_id)}/action/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopSampleConsistencyJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_sample_consistency_job_with_options_async(
        self,
        sample_consistency_job_id: str,
        request: main_models.StopSampleConsistencyJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopSampleConsistencyJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopSampleConsistencyJob',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/sampleconsistencyjobs/{DaraURL.percent_encode(sample_consistency_job_id)}/action/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopSampleConsistencyJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_sample_consistency_job(
        self,
        sample_consistency_job_id: str,
        request: main_models.StopSampleConsistencyJobRequest,
    ) -> main_models.StopSampleConsistencyJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_sample_consistency_job_with_options(sample_consistency_job_id, request, headers, runtime)

    async def stop_sample_consistency_job_async(
        self,
        sample_consistency_job_id: str,
        request: main_models.StopSampleConsistencyJobRequest,
    ) -> main_models.StopSampleConsistencyJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_sample_consistency_job_with_options_async(sample_consistency_job_id, request, headers, runtime)

    def stop_traffic_control_target_with_options(
        self,
        traffic_control_target_id: str,
        request: main_models.StopTrafficControlTargetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopTrafficControlTargetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopTrafficControlTarget',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltargets/{DaraURL.percent_encode(traffic_control_target_id)}/action/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopTrafficControlTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_traffic_control_target_with_options_async(
        self,
        traffic_control_target_id: str,
        request: main_models.StopTrafficControlTargetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopTrafficControlTargetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopTrafficControlTarget',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltargets/{DaraURL.percent_encode(traffic_control_target_id)}/action/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopTrafficControlTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_traffic_control_target(
        self,
        traffic_control_target_id: str,
        request: main_models.StopTrafficControlTargetRequest,
    ) -> main_models.StopTrafficControlTargetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_traffic_control_target_with_options(traffic_control_target_id, request, headers, runtime)

    async def stop_traffic_control_target_async(
        self,
        traffic_control_target_id: str,
        request: main_models.StopTrafficControlTargetRequest,
    ) -> main_models.StopTrafficControlTargetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_traffic_control_target_with_options_async(traffic_control_target_id, request, headers, runtime)

    def stop_traffic_control_task_with_options(
        self,
        traffic_control_task_id: str,
        request: main_models.StopTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopTrafficControlTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopTrafficControlTask',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltasks/{DaraURL.percent_encode(traffic_control_task_id)}/action/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopTrafficControlTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_traffic_control_task_with_options_async(
        self,
        traffic_control_task_id: str,
        request: main_models.StopTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopTrafficControlTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopTrafficControlTask',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltasks/{DaraURL.percent_encode(traffic_control_task_id)}/action/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopTrafficControlTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_traffic_control_task(
        self,
        traffic_control_task_id: str,
        request: main_models.StopTrafficControlTaskRequest,
    ) -> main_models.StopTrafficControlTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_traffic_control_task_with_options(traffic_control_task_id, request, headers, runtime)

    async def stop_traffic_control_task_async(
        self,
        traffic_control_task_id: str,
        request: main_models.StopTrafficControlTaskRequest,
    ) -> main_models.StopTrafficControlTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_traffic_control_task_with_options_async(traffic_control_task_id, request, headers, runtime)

    def sync_feature_consistency_check_job_replay_log_with_options(
        self,
        request: main_models.SyncFeatureConsistencyCheckJobReplayLogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SyncFeatureConsistencyCheckJobReplayLogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.context_features):
            body['ContextFeatures'] = request.context_features
        if not DaraCore.is_null(request.feature_consistency_check_job_config_id):
            body['FeatureConsistencyCheckJobConfigId'] = request.feature_consistency_check_job_config_id
        if not DaraCore.is_null(request.generated_features):
            body['GeneratedFeatures'] = request.generated_features
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.log_item_id):
            body['LogItemId'] = request.log_item_id
        if not DaraCore.is_null(request.log_request_id):
            body['LogRequestId'] = request.log_request_id
        if not DaraCore.is_null(request.log_request_time):
            body['LogRequestTime'] = request.log_request_time
        if not DaraCore.is_null(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not DaraCore.is_null(request.raw_features):
            body['RawFeatures'] = request.raw_features
        if not DaraCore.is_null(request.scene_name):
            body['SceneName'] = request.scene_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SyncFeatureConsistencyCheckJobReplayLog',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/featureconsistencycheck/jobs/action/syncreplaylog',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncFeatureConsistencyCheckJobReplayLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_feature_consistency_check_job_replay_log_with_options_async(
        self,
        request: main_models.SyncFeatureConsistencyCheckJobReplayLogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SyncFeatureConsistencyCheckJobReplayLogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.context_features):
            body['ContextFeatures'] = request.context_features
        if not DaraCore.is_null(request.feature_consistency_check_job_config_id):
            body['FeatureConsistencyCheckJobConfigId'] = request.feature_consistency_check_job_config_id
        if not DaraCore.is_null(request.generated_features):
            body['GeneratedFeatures'] = request.generated_features
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.log_item_id):
            body['LogItemId'] = request.log_item_id
        if not DaraCore.is_null(request.log_request_id):
            body['LogRequestId'] = request.log_request_id
        if not DaraCore.is_null(request.log_request_time):
            body['LogRequestTime'] = request.log_request_time
        if not DaraCore.is_null(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not DaraCore.is_null(request.raw_features):
            body['RawFeatures'] = request.raw_features
        if not DaraCore.is_null(request.scene_name):
            body['SceneName'] = request.scene_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SyncFeatureConsistencyCheckJobReplayLog',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/featureconsistencycheck/jobs/action/syncreplaylog',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncFeatureConsistencyCheckJobReplayLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_feature_consistency_check_job_replay_log(
        self,
        request: main_models.SyncFeatureConsistencyCheckJobReplayLogRequest,
    ) -> main_models.SyncFeatureConsistencyCheckJobReplayLogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.sync_feature_consistency_check_job_replay_log_with_options(request, headers, runtime)

    async def sync_feature_consistency_check_job_replay_log_async(
        self,
        request: main_models.SyncFeatureConsistencyCheckJobReplayLogRequest,
    ) -> main_models.SyncFeatureConsistencyCheckJobReplayLogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.sync_feature_consistency_check_job_replay_log_with_options_async(request, headers, runtime)

    def terminate_feature_consistency_check_job_with_options(
        self,
        feature_consistency_check_job_id: str,
        request: main_models.TerminateFeatureConsistencyCheckJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TerminateFeatureConsistencyCheckJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TerminateFeatureConsistencyCheckJob',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/featureconsistencycheck/jobs/{DaraURL.percent_encode(feature_consistency_check_job_id)}/action/terminate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TerminateFeatureConsistencyCheckJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def terminate_feature_consistency_check_job_with_options_async(
        self,
        feature_consistency_check_job_id: str,
        request: main_models.TerminateFeatureConsistencyCheckJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TerminateFeatureConsistencyCheckJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TerminateFeatureConsistencyCheckJob',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/featureconsistencycheck/jobs/{DaraURL.percent_encode(feature_consistency_check_job_id)}/action/terminate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TerminateFeatureConsistencyCheckJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def terminate_feature_consistency_check_job(
        self,
        feature_consistency_check_job_id: str,
        request: main_models.TerminateFeatureConsistencyCheckJobRequest,
    ) -> main_models.TerminateFeatureConsistencyCheckJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.terminate_feature_consistency_check_job_with_options(feature_consistency_check_job_id, request, headers, runtime)

    async def terminate_feature_consistency_check_job_async(
        self,
        feature_consistency_check_job_id: str,
        request: main_models.TerminateFeatureConsistencyCheckJobRequest,
    ) -> main_models.TerminateFeatureConsistencyCheckJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.terminate_feature_consistency_check_job_with_options_async(feature_consistency_check_job_id, request, headers, runtime)

    def update_abmetric_with_options(
        self,
        abmetric_id: str,
        request: main_models.UpdateABMetricRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateABMetricResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.definition):
            body['Definition'] = request.definition
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.left_metric_id):
            body['LeftMetricId'] = request.left_metric_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.operator):
            body['Operator'] = request.operator
        if not DaraCore.is_null(request.realtime):
            body['Realtime'] = request.realtime
        if not DaraCore.is_null(request.result_resource_id):
            body['ResultResourceId'] = request.result_resource_id
        if not DaraCore.is_null(request.right_metric_id):
            body['RightMetricId'] = request.right_metric_id
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.statistics_cycle):
            body['StatisticsCycle'] = request.statistics_cycle
        if not DaraCore.is_null(request.table_meta_id):
            body['TableMetaId'] = request.table_meta_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateABMetric',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/abmetrics/{DaraURL.percent_encode(abmetric_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateABMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_abmetric_with_options_async(
        self,
        abmetric_id: str,
        request: main_models.UpdateABMetricRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateABMetricResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.definition):
            body['Definition'] = request.definition
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.left_metric_id):
            body['LeftMetricId'] = request.left_metric_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.operator):
            body['Operator'] = request.operator
        if not DaraCore.is_null(request.realtime):
            body['Realtime'] = request.realtime
        if not DaraCore.is_null(request.result_resource_id):
            body['ResultResourceId'] = request.result_resource_id
        if not DaraCore.is_null(request.right_metric_id):
            body['RightMetricId'] = request.right_metric_id
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.statistics_cycle):
            body['StatisticsCycle'] = request.statistics_cycle
        if not DaraCore.is_null(request.table_meta_id):
            body['TableMetaId'] = request.table_meta_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateABMetric',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/abmetrics/{DaraURL.percent_encode(abmetric_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateABMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_abmetric(
        self,
        abmetric_id: str,
        request: main_models.UpdateABMetricRequest,
    ) -> main_models.UpdateABMetricResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_abmetric_with_options(abmetric_id, request, headers, runtime)

    async def update_abmetric_async(
        self,
        abmetric_id: str,
        request: main_models.UpdateABMetricRequest,
    ) -> main_models.UpdateABMetricResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_abmetric_with_options_async(abmetric_id, request, headers, runtime)

    def update_abmetric_group_with_options(
        self,
        abmetric_group_id: str,
        request: main_models.UpdateABMetricGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateABMetricGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.abmetric_ids):
            body['ABMetricIds'] = request.abmetric_ids
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.realtime):
            body['Realtime'] = request.realtime
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateABMetricGroup',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/abmetricgroups/{DaraURL.percent_encode(abmetric_group_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateABMetricGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_abmetric_group_with_options_async(
        self,
        abmetric_group_id: str,
        request: main_models.UpdateABMetricGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateABMetricGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.abmetric_ids):
            body['ABMetricIds'] = request.abmetric_ids
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.realtime):
            body['Realtime'] = request.realtime
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateABMetricGroup',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/abmetricgroups/{DaraURL.percent_encode(abmetric_group_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateABMetricGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_abmetric_group(
        self,
        abmetric_group_id: str,
        request: main_models.UpdateABMetricGroupRequest,
    ) -> main_models.UpdateABMetricGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_abmetric_group_with_options(abmetric_group_id, request, headers, runtime)

    async def update_abmetric_group_async(
        self,
        abmetric_group_id: str,
        request: main_models.UpdateABMetricGroupRequest,
    ) -> main_models.UpdateABMetricGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_abmetric_group_with_options_async(abmetric_group_id, request, headers, runtime)

    def update_crowd_with_options(
        self,
        crowd_id: str,
        request: main_models.UpdateCrowdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCrowdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCrowd',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/crowds/{DaraURL.percent_encode(crowd_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCrowdResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_crowd_with_options_async(
        self,
        crowd_id: str,
        request: main_models.UpdateCrowdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCrowdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCrowd',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/crowds/{DaraURL.percent_encode(crowd_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCrowdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_crowd(
        self,
        crowd_id: str,
        request: main_models.UpdateCrowdRequest,
    ) -> main_models.UpdateCrowdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_crowd_with_options(crowd_id, request, headers, runtime)

    async def update_crowd_async(
        self,
        crowd_id: str,
        request: main_models.UpdateCrowdRequest,
    ) -> main_models.UpdateCrowdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_crowd_with_options_async(crowd_id, request, headers, runtime)

    def update_engine_config_with_options(
        self,
        engine_config_id: str,
        request: main_models.UpdateEngineConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEngineConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config_value):
            body['ConfigValue'] = request.config_value
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEngineConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/engineconfigs/{DaraURL.percent_encode(engine_config_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEngineConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_engine_config_with_options_async(
        self,
        engine_config_id: str,
        request: main_models.UpdateEngineConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEngineConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config_value):
            body['ConfigValue'] = request.config_value
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEngineConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/engineconfigs/{DaraURL.percent_encode(engine_config_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEngineConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_engine_config(
        self,
        engine_config_id: str,
        request: main_models.UpdateEngineConfigRequest,
    ) -> main_models.UpdateEngineConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_engine_config_with_options(engine_config_id, request, headers, runtime)

    async def update_engine_config_async(
        self,
        engine_config_id: str,
        request: main_models.UpdateEngineConfigRequest,
    ) -> main_models.UpdateEngineConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_engine_config_with_options_async(engine_config_id, request, headers, runtime)

    def update_experiment_with_options(
        self,
        experiment_id: str,
        request: main_models.UpdateExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateExperimentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not DaraCore.is_null(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.flow_percent):
            body['FlowPercent'] = request.flow_percent
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateExperiment',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(experiment_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_experiment_with_options_async(
        self,
        experiment_id: str,
        request: main_models.UpdateExperimentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateExperimentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not DaraCore.is_null(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.flow_percent):
            body['FlowPercent'] = request.flow_percent
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateExperiment',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experiments/{DaraURL.percent_encode(experiment_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_experiment(
        self,
        experiment_id: str,
        request: main_models.UpdateExperimentRequest,
    ) -> main_models.UpdateExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_experiment_with_options(experiment_id, request, headers, runtime)

    async def update_experiment_async(
        self,
        experiment_id: str,
        request: main_models.UpdateExperimentRequest,
    ) -> main_models.UpdateExperimentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_experiment_with_options_async(experiment_id, request, headers, runtime)

    def update_experiment_group_with_options(
        self,
        experiment_group_id: str,
        request: main_models.UpdateExperimentGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateExperimentGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.crowd_id):
            body['CrowdId'] = request.crowd_id
        if not DaraCore.is_null(request.crowd_target_type):
            body['CrowdTargetType'] = request.crowd_target_type
        if not DaraCore.is_null(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not DaraCore.is_null(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.distribution_time_duration):
            body['DistributionTimeDuration'] = request.distribution_time_duration
        if not DaraCore.is_null(request.distribution_type):
            body['DistributionType'] = request.distribution_type
        if not DaraCore.is_null(request.filter):
            body['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.layer_id):
            body['LayerId'] = request.layer_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.need_aa):
            body['NeedAA'] = request.need_aa
        if not DaraCore.is_null(request.random_flow):
            body['RandomFlow'] = request.random_flow
        if not DaraCore.is_null(request.reservced_buckets):
            body['ReservcedBuckets'] = request.reservced_buckets
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateExperimentGroup',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experimentgroups/{DaraURL.percent_encode(experiment_group_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateExperimentGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_experiment_group_with_options_async(
        self,
        experiment_group_id: str,
        request: main_models.UpdateExperimentGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateExperimentGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.crowd_id):
            body['CrowdId'] = request.crowd_id
        if not DaraCore.is_null(request.crowd_target_type):
            body['CrowdTargetType'] = request.crowd_target_type
        if not DaraCore.is_null(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not DaraCore.is_null(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.distribution_time_duration):
            body['DistributionTimeDuration'] = request.distribution_time_duration
        if not DaraCore.is_null(request.distribution_type):
            body['DistributionType'] = request.distribution_type
        if not DaraCore.is_null(request.filter):
            body['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.layer_id):
            body['LayerId'] = request.layer_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.need_aa):
            body['NeedAA'] = request.need_aa
        if not DaraCore.is_null(request.random_flow):
            body['RandomFlow'] = request.random_flow
        if not DaraCore.is_null(request.reservced_buckets):
            body['ReservcedBuckets'] = request.reservced_buckets
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateExperimentGroup',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/experimentgroups/{DaraURL.percent_encode(experiment_group_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateExperimentGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_experiment_group(
        self,
        experiment_group_id: str,
        request: main_models.UpdateExperimentGroupRequest,
    ) -> main_models.UpdateExperimentGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_experiment_group_with_options(experiment_group_id, request, headers, runtime)

    async def update_experiment_group_async(
        self,
        experiment_group_id: str,
        request: main_models.UpdateExperimentGroupRequest,
    ) -> main_models.UpdateExperimentGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_experiment_group_with_options_async(experiment_group_id, request, headers, runtime)

    def update_feature_consistency_check_job_config_with_options(
        self,
        feature_consistency_check_job_config_id: str,
        request: main_models.UpdateFeatureConsistencyCheckJobConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFeatureConsistencyCheckJobConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.compare_feature):
            body['CompareFeature'] = request.compare_feature
        if not DaraCore.is_null(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_mount_path):
            body['DatasetMountPath'] = request.dataset_mount_path
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.dataset_type):
            body['DatasetType'] = request.dataset_type
        if not DaraCore.is_null(request.dataset_uri):
            body['DatasetUri'] = request.dataset_uri
        if not DaraCore.is_null(request.default_route):
            body['DefaultRoute'] = request.default_route
        if not DaraCore.is_null(request.eas_service_name):
            body['EasServiceName'] = request.eas_service_name
        if not DaraCore.is_null(request.easy_rec_package_path):
            body['EasyRecPackagePath'] = request.easy_rec_package_path
        if not DaraCore.is_null(request.easy_rec_version):
            body['EasyRecVersion'] = request.easy_rec_version
        if not DaraCore.is_null(request.feature_display_exclude):
            body['FeatureDisplayExclude'] = request.feature_display_exclude
        if not DaraCore.is_null(request.feature_landing_resource_id):
            body['FeatureLandingResourceId'] = request.feature_landing_resource_id
        if not DaraCore.is_null(request.feature_priority):
            body['FeaturePriority'] = request.feature_priority
        if not DaraCore.is_null(request.feature_store_item_id):
            body['FeatureStoreItemId'] = request.feature_store_item_id
        if not DaraCore.is_null(request.feature_store_model_id):
            body['FeatureStoreModelId'] = request.feature_store_model_id
        if not DaraCore.is_null(request.feature_store_project_id):
            body['FeatureStoreProjectId'] = request.feature_store_project_id
        if not DaraCore.is_null(request.feature_store_project_name):
            body['FeatureStoreProjectName'] = request.feature_store_project_name
        if not DaraCore.is_null(request.feature_store_seq_feature_view):
            body['FeatureStoreSeqFeatureView'] = request.feature_store_seq_feature_view
        if not DaraCore.is_null(request.feature_store_user_id):
            body['FeatureStoreUserId'] = request.feature_store_user_id
        if not DaraCore.is_null(request.fg_jar_version):
            body['FgJarVersion'] = request.fg_jar_version
        if not DaraCore.is_null(request.fg_json_file_name):
            body['FgJsonFileName'] = request.fg_json_file_name
        if not DaraCore.is_null(request.generate_zip):
            body['GenerateZip'] = request.generate_zip
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_use_feature_store):
            body['IsUseFeatureStore'] = request.is_use_feature_store
        if not DaraCore.is_null(request.item_id_field):
            body['ItemIdField'] = request.item_id_field
        if not DaraCore.is_null(request.item_table):
            body['ItemTable'] = request.item_table
        if not DaraCore.is_null(request.item_table_partition_field):
            body['ItemTablePartitionField'] = request.item_table_partition_field
        if not DaraCore.is_null(request.item_table_partition_field_format):
            body['ItemTablePartitionFieldFormat'] = request.item_table_partition_field_format
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.oss_resource_id):
            body['OssResourceId'] = request.oss_resource_id
        if not DaraCore.is_null(request.predict_worker_count):
            body['PredictWorkerCount'] = request.predict_worker_count
        if not DaraCore.is_null(request.predict_worker_cpu):
            body['PredictWorkerCpu'] = request.predict_worker_cpu
        if not DaraCore.is_null(request.predict_worker_memory):
            body['PredictWorkerMemory'] = request.predict_worker_memory
        if not DaraCore.is_null(request.resource_config):
            body['ResourceConfig'] = request.resource_config
        if not DaraCore.is_null(request.sample_rate):
            body['SampleRate'] = request.sample_rate
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.security_group_id):
            body['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.service_id):
            body['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.switch_id):
            body['SwitchId'] = request.switch_id
        if not DaraCore.is_null(request.user_id_field):
            body['UserIdField'] = request.user_id_field
        if not DaraCore.is_null(request.user_table):
            body['UserTable'] = request.user_table
        if not DaraCore.is_null(request.user_table_partition_field):
            body['UserTablePartitionField'] = request.user_table_partition_field
        if not DaraCore.is_null(request.user_table_partition_field_format):
            body['UserTablePartitionFieldFormat'] = request.user_table_partition_field_format
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.workflow_name):
            body['WorkflowName'] = request.workflow_name
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFeatureConsistencyCheckJobConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/featureconsistencycheck/jobconfigs/{DaraURL.percent_encode(feature_consistency_check_job_config_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFeatureConsistencyCheckJobConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_feature_consistency_check_job_config_with_options_async(
        self,
        feature_consistency_check_job_config_id: str,
        request: main_models.UpdateFeatureConsistencyCheckJobConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFeatureConsistencyCheckJobConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.compare_feature):
            body['CompareFeature'] = request.compare_feature
        if not DaraCore.is_null(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_mount_path):
            body['DatasetMountPath'] = request.dataset_mount_path
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.dataset_type):
            body['DatasetType'] = request.dataset_type
        if not DaraCore.is_null(request.dataset_uri):
            body['DatasetUri'] = request.dataset_uri
        if not DaraCore.is_null(request.default_route):
            body['DefaultRoute'] = request.default_route
        if not DaraCore.is_null(request.eas_service_name):
            body['EasServiceName'] = request.eas_service_name
        if not DaraCore.is_null(request.easy_rec_package_path):
            body['EasyRecPackagePath'] = request.easy_rec_package_path
        if not DaraCore.is_null(request.easy_rec_version):
            body['EasyRecVersion'] = request.easy_rec_version
        if not DaraCore.is_null(request.feature_display_exclude):
            body['FeatureDisplayExclude'] = request.feature_display_exclude
        if not DaraCore.is_null(request.feature_landing_resource_id):
            body['FeatureLandingResourceId'] = request.feature_landing_resource_id
        if not DaraCore.is_null(request.feature_priority):
            body['FeaturePriority'] = request.feature_priority
        if not DaraCore.is_null(request.feature_store_item_id):
            body['FeatureStoreItemId'] = request.feature_store_item_id
        if not DaraCore.is_null(request.feature_store_model_id):
            body['FeatureStoreModelId'] = request.feature_store_model_id
        if not DaraCore.is_null(request.feature_store_project_id):
            body['FeatureStoreProjectId'] = request.feature_store_project_id
        if not DaraCore.is_null(request.feature_store_project_name):
            body['FeatureStoreProjectName'] = request.feature_store_project_name
        if not DaraCore.is_null(request.feature_store_seq_feature_view):
            body['FeatureStoreSeqFeatureView'] = request.feature_store_seq_feature_view
        if not DaraCore.is_null(request.feature_store_user_id):
            body['FeatureStoreUserId'] = request.feature_store_user_id
        if not DaraCore.is_null(request.fg_jar_version):
            body['FgJarVersion'] = request.fg_jar_version
        if not DaraCore.is_null(request.fg_json_file_name):
            body['FgJsonFileName'] = request.fg_json_file_name
        if not DaraCore.is_null(request.generate_zip):
            body['GenerateZip'] = request.generate_zip
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_use_feature_store):
            body['IsUseFeatureStore'] = request.is_use_feature_store
        if not DaraCore.is_null(request.item_id_field):
            body['ItemIdField'] = request.item_id_field
        if not DaraCore.is_null(request.item_table):
            body['ItemTable'] = request.item_table
        if not DaraCore.is_null(request.item_table_partition_field):
            body['ItemTablePartitionField'] = request.item_table_partition_field
        if not DaraCore.is_null(request.item_table_partition_field_format):
            body['ItemTablePartitionFieldFormat'] = request.item_table_partition_field_format
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.oss_resource_id):
            body['OssResourceId'] = request.oss_resource_id
        if not DaraCore.is_null(request.predict_worker_count):
            body['PredictWorkerCount'] = request.predict_worker_count
        if not DaraCore.is_null(request.predict_worker_cpu):
            body['PredictWorkerCpu'] = request.predict_worker_cpu
        if not DaraCore.is_null(request.predict_worker_memory):
            body['PredictWorkerMemory'] = request.predict_worker_memory
        if not DaraCore.is_null(request.resource_config):
            body['ResourceConfig'] = request.resource_config
        if not DaraCore.is_null(request.sample_rate):
            body['SampleRate'] = request.sample_rate
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.security_group_id):
            body['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.service_id):
            body['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.switch_id):
            body['SwitchId'] = request.switch_id
        if not DaraCore.is_null(request.user_id_field):
            body['UserIdField'] = request.user_id_field
        if not DaraCore.is_null(request.user_table):
            body['UserTable'] = request.user_table
        if not DaraCore.is_null(request.user_table_partition_field):
            body['UserTablePartitionField'] = request.user_table_partition_field
        if not DaraCore.is_null(request.user_table_partition_field_format):
            body['UserTablePartitionFieldFormat'] = request.user_table_partition_field_format
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.workflow_name):
            body['WorkflowName'] = request.workflow_name
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFeatureConsistencyCheckJobConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/featureconsistencycheck/jobconfigs/{DaraURL.percent_encode(feature_consistency_check_job_config_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFeatureConsistencyCheckJobConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_feature_consistency_check_job_config(
        self,
        feature_consistency_check_job_config_id: str,
        request: main_models.UpdateFeatureConsistencyCheckJobConfigRequest,
    ) -> main_models.UpdateFeatureConsistencyCheckJobConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_feature_consistency_check_job_config_with_options(feature_consistency_check_job_config_id, request, headers, runtime)

    async def update_feature_consistency_check_job_config_async(
        self,
        feature_consistency_check_job_config_id: str,
        request: main_models.UpdateFeatureConsistencyCheckJobConfigRequest,
    ) -> main_models.UpdateFeatureConsistencyCheckJobConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_feature_consistency_check_job_config_with_options_async(feature_consistency_check_job_config_id, request, headers, runtime)

    def update_instance_resource_with_options(
        self,
        instance_id: str,
        resource_id: str,
        request: main_models.UpdateInstanceResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.uri):
            body['Uri'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceResource',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/resources/{DaraURL.percent_encode(resource_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_resource_with_options_async(
        self,
        instance_id: str,
        resource_id: str,
        request: main_models.UpdateInstanceResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.uri):
            body['Uri'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceResource',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/resources/{DaraURL.percent_encode(resource_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_resource(
        self,
        instance_id: str,
        resource_id: str,
        request: main_models.UpdateInstanceResourceRequest,
    ) -> main_models.UpdateInstanceResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_instance_resource_with_options(instance_id, resource_id, request, headers, runtime)

    async def update_instance_resource_async(
        self,
        instance_id: str,
        resource_id: str,
        request: main_models.UpdateInstanceResourceRequest,
    ) -> main_models.UpdateInstanceResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_instance_resource_with_options_async(instance_id, resource_id, request, headers, runtime)

    def update_laboratory_with_options(
        self,
        laboratory_id: str,
        request: main_models.UpdateLaboratoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLaboratoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.bucket_count):
            body['BucketCount'] = request.bucket_count
        if not DaraCore.is_null(request.bucket_type):
            body['BucketType'] = request.bucket_type
        if not DaraCore.is_null(request.buckets):
            body['Buckets'] = request.buckets
        if not DaraCore.is_null(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not DaraCore.is_null(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.filter):
            body['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLaboratory',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/laboratories/{DaraURL.percent_encode(laboratory_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLaboratoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_laboratory_with_options_async(
        self,
        laboratory_id: str,
        request: main_models.UpdateLaboratoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLaboratoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.bucket_count):
            body['BucketCount'] = request.bucket_count
        if not DaraCore.is_null(request.bucket_type):
            body['BucketType'] = request.bucket_type
        if not DaraCore.is_null(request.buckets):
            body['Buckets'] = request.buckets
        if not DaraCore.is_null(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not DaraCore.is_null(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.filter):
            body['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLaboratory',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/laboratories/{DaraURL.percent_encode(laboratory_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLaboratoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_laboratory(
        self,
        laboratory_id: str,
        request: main_models.UpdateLaboratoryRequest,
    ) -> main_models.UpdateLaboratoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_laboratory_with_options(laboratory_id, request, headers, runtime)

    async def update_laboratory_async(
        self,
        laboratory_id: str,
        request: main_models.UpdateLaboratoryRequest,
    ) -> main_models.UpdateLaboratoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_laboratory_with_options_async(laboratory_id, request, headers, runtime)

    def update_layer_with_options(
        self,
        layer_id: str,
        request: main_models.UpdateLayerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLayerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLayer',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/layers/{DaraURL.percent_encode(layer_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_layer_with_options_async(
        self,
        layer_id: str,
        request: main_models.UpdateLayerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLayerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLayer',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/layers/{DaraURL.percent_encode(layer_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_layer(
        self,
        layer_id: str,
        request: main_models.UpdateLayerRequest,
    ) -> main_models.UpdateLayerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_layer_with_options(layer_id, request, headers, runtime)

    async def update_layer_async(
        self,
        layer_id: str,
        request: main_models.UpdateLayerRequest,
    ) -> main_models.UpdateLayerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_layer_with_options_async(layer_id, request, headers, runtime)

    def update_param_with_options(
        self,
        param_id: str,
        request: main_models.UpdateParamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateParamResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.value):
            body['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateParam',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/params/{DaraURL.percent_encode(param_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateParamResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_param_with_options_async(
        self,
        param_id: str,
        request: main_models.UpdateParamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateParamResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.value):
            body['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateParam',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/params/{DaraURL.percent_encode(param_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateParamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_param(
        self,
        param_id: str,
        request: main_models.UpdateParamRequest,
    ) -> main_models.UpdateParamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_param_with_options(param_id, request, headers, runtime)

    async def update_param_async(
        self,
        param_id: str,
        request: main_models.UpdateParamRequest,
    ) -> main_models.UpdateParamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_param_with_options_async(param_id, request, headers, runtime)

    def update_recall_management_config_with_options(
        self,
        request: main_models.UpdateRecallManagementConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecallManagementConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_configs):
            body['NetworkConfigs'] = request.network_configs
        if not DaraCore.is_null(request.password):
            body['Password'] = request.password
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecallManagementConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementconfigs',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecallManagementConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_recall_management_config_with_options_async(
        self,
        request: main_models.UpdateRecallManagementConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecallManagementConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_configs):
            body['NetworkConfigs'] = request.network_configs
        if not DaraCore.is_null(request.password):
            body['Password'] = request.password
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecallManagementConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementconfigs',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecallManagementConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_recall_management_config(
        self,
        request: main_models.UpdateRecallManagementConfigRequest,
    ) -> main_models.UpdateRecallManagementConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_recall_management_config_with_options(request, headers, runtime)

    async def update_recall_management_config_async(
        self,
        request: main_models.UpdateRecallManagementConfigRequest,
    ) -> main_models.UpdateRecallManagementConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_recall_management_config_with_options_async(request, headers, runtime)

    def update_recall_management_service_with_options(
        self,
        recall_management_service_id: str,
        request: main_models.UpdateRecallManagementServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecallManagementServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecallManagementService',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices/{DaraURL.percent_encode(recall_management_service_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecallManagementServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_recall_management_service_with_options_async(
        self,
        recall_management_service_id: str,
        request: main_models.UpdateRecallManagementServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecallManagementServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecallManagementService',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices/{DaraURL.percent_encode(recall_management_service_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecallManagementServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_recall_management_service(
        self,
        recall_management_service_id: str,
        request: main_models.UpdateRecallManagementServiceRequest,
    ) -> main_models.UpdateRecallManagementServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_recall_management_service_with_options(recall_management_service_id, request, headers, runtime)

    async def update_recall_management_service_async(
        self,
        recall_management_service_id: str,
        request: main_models.UpdateRecallManagementServiceRequest,
    ) -> main_models.UpdateRecallManagementServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_recall_management_service_with_options_async(recall_management_service_id, request, headers, runtime)

    def update_recall_management_service_version_config_with_options(
        self,
        recall_management_service_id: str,
        recall_management_service_version_id: str,
        recall_management_service_version_config_id: str,
        request: main_models.UpdateRecallManagementServiceVersionConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecallManagementServiceVersionConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.config_type):
            body['ConfigType'] = request.config_type
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.merge_config):
            body['MergeConfig'] = request.merge_config
        if not DaraCore.is_null(request.recall_config):
            body['RecallConfig'] = request.recall_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecallManagementServiceVersionConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices/{DaraURL.percent_encode(recall_management_service_id)}/versions/{DaraURL.percent_encode(recall_management_service_version_id)}/configs/{DaraURL.percent_encode(recall_management_service_version_config_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecallManagementServiceVersionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_recall_management_service_version_config_with_options_async(
        self,
        recall_management_service_id: str,
        recall_management_service_version_id: str,
        recall_management_service_version_config_id: str,
        request: main_models.UpdateRecallManagementServiceVersionConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecallManagementServiceVersionConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.config_type):
            body['ConfigType'] = request.config_type
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.merge_config):
            body['MergeConfig'] = request.merge_config
        if not DaraCore.is_null(request.recall_config):
            body['RecallConfig'] = request.recall_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecallManagementServiceVersionConfig',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementservices/{DaraURL.percent_encode(recall_management_service_id)}/versions/{DaraURL.percent_encode(recall_management_service_version_id)}/configs/{DaraURL.percent_encode(recall_management_service_version_config_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecallManagementServiceVersionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_recall_management_service_version_config(
        self,
        recall_management_service_id: str,
        recall_management_service_version_id: str,
        recall_management_service_version_config_id: str,
        request: main_models.UpdateRecallManagementServiceVersionConfigRequest,
    ) -> main_models.UpdateRecallManagementServiceVersionConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_recall_management_service_version_config_with_options(recall_management_service_id, recall_management_service_version_id, recall_management_service_version_config_id, request, headers, runtime)

    async def update_recall_management_service_version_config_async(
        self,
        recall_management_service_id: str,
        recall_management_service_version_id: str,
        recall_management_service_version_config_id: str,
        request: main_models.UpdateRecallManagementServiceVersionConfigRequest,
    ) -> main_models.UpdateRecallManagementServiceVersionConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_recall_management_service_version_config_with_options_async(recall_management_service_id, recall_management_service_version_id, recall_management_service_version_config_id, request, headers, runtime)

    def update_recall_management_table_with_options(
        self,
        recall_management_table_id: str,
        request: main_models.UpdateRecallManagementTableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecallManagementTableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enable_data_size_fluctuation_threshold):
            body['EnableDataSizeFluctuationThreshold'] = request.enable_data_size_fluctuation_threshold
        if not DaraCore.is_null(request.enable_row_count_fluctuation_threshold):
            body['EnableRowCountFluctuationThreshold'] = request.enable_row_count_fluctuation_threshold
        if not DaraCore.is_null(request.index_version_id):
            body['IndexVersionId'] = request.index_version_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_data_size_fluctuation_threshold):
            body['MaxDataSizeFluctuationThreshold'] = request.max_data_size_fluctuation_threshold
        if not DaraCore.is_null(request.max_row_count_fluctuation_threshold):
            body['MaxRowCountFluctuationThreshold'] = request.max_row_count_fluctuation_threshold
        if not DaraCore.is_null(request.min_data_size_fluctuation_threshold):
            body['MinDataSizeFluctuationThreshold'] = request.min_data_size_fluctuation_threshold
        if not DaraCore.is_null(request.min_row_count_fluctuation_threshold):
            body['MinRowCountFluctuationThreshold'] = request.min_row_count_fluctuation_threshold
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecallManagementTable',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementtables/{DaraURL.percent_encode(recall_management_table_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecallManagementTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_recall_management_table_with_options_async(
        self,
        recall_management_table_id: str,
        request: main_models.UpdateRecallManagementTableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecallManagementTableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enable_data_size_fluctuation_threshold):
            body['EnableDataSizeFluctuationThreshold'] = request.enable_data_size_fluctuation_threshold
        if not DaraCore.is_null(request.enable_row_count_fluctuation_threshold):
            body['EnableRowCountFluctuationThreshold'] = request.enable_row_count_fluctuation_threshold
        if not DaraCore.is_null(request.index_version_id):
            body['IndexVersionId'] = request.index_version_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_data_size_fluctuation_threshold):
            body['MaxDataSizeFluctuationThreshold'] = request.max_data_size_fluctuation_threshold
        if not DaraCore.is_null(request.max_row_count_fluctuation_threshold):
            body['MaxRowCountFluctuationThreshold'] = request.max_row_count_fluctuation_threshold
        if not DaraCore.is_null(request.min_data_size_fluctuation_threshold):
            body['MinDataSizeFluctuationThreshold'] = request.min_data_size_fluctuation_threshold
        if not DaraCore.is_null(request.min_row_count_fluctuation_threshold):
            body['MinRowCountFluctuationThreshold'] = request.min_row_count_fluctuation_threshold
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecallManagementTable',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recallmanagementtables/{DaraURL.percent_encode(recall_management_table_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecallManagementTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_recall_management_table(
        self,
        recall_management_table_id: str,
        request: main_models.UpdateRecallManagementTableRequest,
    ) -> main_models.UpdateRecallManagementTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_recall_management_table_with_options(recall_management_table_id, request, headers, runtime)

    async def update_recall_management_table_async(
        self,
        recall_management_table_id: str,
        request: main_models.UpdateRecallManagementTableRequest,
    ) -> main_models.UpdateRecallManagementTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_recall_management_table_with_options_async(recall_management_table_id, request, headers, runtime)

    def update_resource_rule_with_options(
        self,
        resource_rule_id: str,
        request: main_models.UpdateResourceRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.metric_operation_type):
            body['MetricOperationType'] = request.metric_operation_type
        if not DaraCore.is_null(request.metric_pull_info):
            body['MetricPullInfo'] = request.metric_pull_info
        if not DaraCore.is_null(request.metric_pull_period):
            body['MetricPullPeriod'] = request.metric_pull_period
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.rule_computing_definition):
            body['RuleComputingDefinition'] = request.rule_computing_definition
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResourceRule',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resourcerules/{DaraURL.percent_encode(resource_rule_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_rule_with_options_async(
        self,
        resource_rule_id: str,
        request: main_models.UpdateResourceRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.metric_operation_type):
            body['MetricOperationType'] = request.metric_operation_type
        if not DaraCore.is_null(request.metric_pull_info):
            body['MetricPullInfo'] = request.metric_pull_info
        if not DaraCore.is_null(request.metric_pull_period):
            body['MetricPullPeriod'] = request.metric_pull_period
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.rule_computing_definition):
            body['RuleComputingDefinition'] = request.rule_computing_definition
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResourceRule',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resourcerules/{DaraURL.percent_encode(resource_rule_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_rule(
        self,
        resource_rule_id: str,
        request: main_models.UpdateResourceRuleRequest,
    ) -> main_models.UpdateResourceRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_resource_rule_with_options(resource_rule_id, request, headers, runtime)

    async def update_resource_rule_async(
        self,
        resource_rule_id: str,
        request: main_models.UpdateResourceRuleRequest,
    ) -> main_models.UpdateResourceRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_resource_rule_with_options_async(resource_rule_id, request, headers, runtime)

    def update_resource_rule_item_with_options(
        self,
        resource_rule_id: str,
        resource_rule_item_id: str,
        request: main_models.UpdateResourceRuleItemRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceRuleItemResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_value):
            body['MaxValue'] = request.max_value
        if not DaraCore.is_null(request.min_value):
            body['MinValue'] = request.min_value
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.value):
            body['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResourceRuleItem',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resourcerules/{DaraURL.percent_encode(resource_rule_id)}/items/{DaraURL.percent_encode(resource_rule_item_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceRuleItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_rule_item_with_options_async(
        self,
        resource_rule_id: str,
        resource_rule_item_id: str,
        request: main_models.UpdateResourceRuleItemRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceRuleItemResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_value):
            body['MaxValue'] = request.max_value
        if not DaraCore.is_null(request.min_value):
            body['MinValue'] = request.min_value
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.value):
            body['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResourceRuleItem',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resourcerules/{DaraURL.percent_encode(resource_rule_id)}/items/{DaraURL.percent_encode(resource_rule_item_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceRuleItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_rule_item(
        self,
        resource_rule_id: str,
        resource_rule_item_id: str,
        request: main_models.UpdateResourceRuleItemRequest,
    ) -> main_models.UpdateResourceRuleItemResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_resource_rule_item_with_options(resource_rule_id, resource_rule_item_id, request, headers, runtime)

    async def update_resource_rule_item_async(
        self,
        resource_rule_id: str,
        resource_rule_item_id: str,
        request: main_models.UpdateResourceRuleItemRequest,
    ) -> main_models.UpdateResourceRuleItemResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_resource_rule_item_with_options_async(resource_rule_id, resource_rule_item_id, request, headers, runtime)

    def update_scene_with_options(
        self,
        scene_id: str,
        request: main_models.UpdateSceneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSceneResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.flows):
            body['Flows'] = request.flows
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateScene',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/scenes/{DaraURL.percent_encode(scene_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_scene_with_options_async(
        self,
        scene_id: str,
        request: main_models.UpdateSceneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSceneResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.flows):
            body['Flows'] = request.flows
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateScene',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/scenes/{DaraURL.percent_encode(scene_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_scene(
        self,
        scene_id: str,
        request: main_models.UpdateSceneRequest,
    ) -> main_models.UpdateSceneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_scene_with_options(scene_id, request, headers, runtime)

    async def update_scene_async(
        self,
        scene_id: str,
        request: main_models.UpdateSceneRequest,
    ) -> main_models.UpdateSceneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_scene_with_options_async(scene_id, request, headers, runtime)

    def update_table_meta_with_options(
        self,
        table_meta_id: str,
        request: main_models.UpdateTableMetaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTableMetaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.fields):
            body['Fields'] = request.fields
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module):
            body['Module'] = request.module
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTableMeta',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tablemetas/{DaraURL.percent_encode(table_meta_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTableMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_table_meta_with_options_async(
        self,
        table_meta_id: str,
        request: main_models.UpdateTableMetaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTableMetaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.fields):
            body['Fields'] = request.fields
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module):
            body['Module'] = request.module
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.table_name):
            body['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTableMeta',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tablemetas/{DaraURL.percent_encode(table_meta_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTableMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_table_meta(
        self,
        table_meta_id: str,
        request: main_models.UpdateTableMetaRequest,
    ) -> main_models.UpdateTableMetaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_table_meta_with_options(table_meta_id, request, headers, runtime)

    async def update_table_meta_async(
        self,
        table_meta_id: str,
        request: main_models.UpdateTableMetaRequest,
    ) -> main_models.UpdateTableMetaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_table_meta_with_options_async(table_meta_id, request, headers, runtime)

    def update_traffic_control_target_with_options(
        self,
        traffic_control_target_id: str,
        request: main_models.UpdateTrafficControlTargetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTrafficControlTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_param_3):
            query['new-param-3'] = request.new_param_3
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event):
            body['Event'] = request.event
        if not DaraCore.is_null(request.item_condition_array):
            body['ItemConditionArray'] = request.item_condition_array
        if not DaraCore.is_null(request.item_condition_express):
            body['ItemConditionExpress'] = request.item_condition_express
        if not DaraCore.is_null(request.item_condition_type):
            body['ItemConditionType'] = request.item_condition_type
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.new_product_regulation):
            body['NewProductRegulation'] = request.new_product_regulation
        if not DaraCore.is_null(request.recall_name):
            body['RecallName'] = request.recall_name
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.statis_period):
            body['StatisPeriod'] = request.statis_period
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tolerance_value):
            body['ToleranceValue'] = request.tolerance_value
        if not DaraCore.is_null(request.value):
            body['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTrafficControlTarget',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltargets/{DaraURL.percent_encode(traffic_control_target_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTrafficControlTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_traffic_control_target_with_options_async(
        self,
        traffic_control_target_id: str,
        request: main_models.UpdateTrafficControlTargetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTrafficControlTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_param_3):
            query['new-param-3'] = request.new_param_3
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event):
            body['Event'] = request.event
        if not DaraCore.is_null(request.item_condition_array):
            body['ItemConditionArray'] = request.item_condition_array
        if not DaraCore.is_null(request.item_condition_express):
            body['ItemConditionExpress'] = request.item_condition_express
        if not DaraCore.is_null(request.item_condition_type):
            body['ItemConditionType'] = request.item_condition_type
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.new_product_regulation):
            body['NewProductRegulation'] = request.new_product_regulation
        if not DaraCore.is_null(request.recall_name):
            body['RecallName'] = request.recall_name
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.statis_period):
            body['StatisPeriod'] = request.statis_period
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tolerance_value):
            body['ToleranceValue'] = request.tolerance_value
        if not DaraCore.is_null(request.value):
            body['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTrafficControlTarget',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltargets/{DaraURL.percent_encode(traffic_control_target_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTrafficControlTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_traffic_control_target(
        self,
        traffic_control_target_id: str,
        request: main_models.UpdateTrafficControlTargetRequest,
    ) -> main_models.UpdateTrafficControlTargetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_traffic_control_target_with_options(traffic_control_target_id, request, headers, runtime)

    async def update_traffic_control_target_async(
        self,
        traffic_control_target_id: str,
        request: main_models.UpdateTrafficControlTargetRequest,
    ) -> main_models.UpdateTrafficControlTargetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_traffic_control_target_with_options_async(traffic_control_target_id, request, headers, runtime)

    def update_traffic_control_task_with_options(
        self,
        traffic_control_task_id: str,
        request: main_models.UpdateTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTrafficControlTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.behavior_table_meta_id):
            body['BehaviorTableMetaId'] = request.behavior_table_meta_id
        if not DaraCore.is_null(request.control_granularity):
            body['ControlGranularity'] = request.control_granularity
        if not DaraCore.is_null(request.control_logic):
            body['ControlLogic'] = request.control_logic
        if not DaraCore.is_null(request.control_type):
            body['ControlType'] = request.control_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.effective_scene_ids):
            body['EffectiveSceneIds'] = request.effective_scene_ids
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.execution_time):
            body['ExecutionTime'] = request.execution_time
        if not DaraCore.is_null(request.flink_resource_id):
            body['FlinkResourceId'] = request.flink_resource_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.item_condition_array):
            body['ItemConditionArray'] = request.item_condition_array
        if not DaraCore.is_null(request.item_condition_express):
            body['ItemConditionExpress'] = request.item_condition_express
        if not DaraCore.is_null(request.item_condition_type):
            body['ItemConditionType'] = request.item_condition_type
        if not DaraCore.is_null(request.item_table_meta_id):
            body['ItemTableMetaId'] = request.item_table_meta_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.pre_experiment_ids):
            body['PreExperimentIds'] = request.pre_experiment_ids
        if not DaraCore.is_null(request.prod_experiment_ids):
            body['ProdExperimentIds'] = request.prod_experiment_ids
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.service_id):
            body['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_ids):
            body['ServiceIds'] = request.service_ids
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.statis_baeavior_condition_array):
            body['StatisBaeaviorConditionArray'] = request.statis_baeavior_condition_array
        if not DaraCore.is_null(request.statis_behavior_condition_array):
            body['StatisBehaviorConditionArray'] = request.statis_behavior_condition_array
        if not DaraCore.is_null(request.statis_behavior_condition_express):
            body['StatisBehaviorConditionExpress'] = request.statis_behavior_condition_express
        if not DaraCore.is_null(request.statis_behavior_condition_type):
            body['StatisBehaviorConditionType'] = request.statis_behavior_condition_type
        if not DaraCore.is_null(request.traffic_control_targets):
            body['TrafficControlTargets'] = request.traffic_control_targets
        if not DaraCore.is_null(request.user_condition_array):
            body['UserConditionArray'] = request.user_condition_array
        if not DaraCore.is_null(request.user_condition_express):
            body['UserConditionExpress'] = request.user_condition_express
        if not DaraCore.is_null(request.user_condition_type):
            body['UserConditionType'] = request.user_condition_type
        if not DaraCore.is_null(request.user_table_meta_id):
            body['UserTableMetaId'] = request.user_table_meta_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTrafficControlTask',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltasks/{DaraURL.percent_encode(traffic_control_task_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTrafficControlTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_traffic_control_task_with_options_async(
        self,
        traffic_control_task_id: str,
        request: main_models.UpdateTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTrafficControlTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.behavior_table_meta_id):
            body['BehaviorTableMetaId'] = request.behavior_table_meta_id
        if not DaraCore.is_null(request.control_granularity):
            body['ControlGranularity'] = request.control_granularity
        if not DaraCore.is_null(request.control_logic):
            body['ControlLogic'] = request.control_logic
        if not DaraCore.is_null(request.control_type):
            body['ControlType'] = request.control_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.effective_scene_ids):
            body['EffectiveSceneIds'] = request.effective_scene_ids
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.execution_time):
            body['ExecutionTime'] = request.execution_time
        if not DaraCore.is_null(request.flink_resource_id):
            body['FlinkResourceId'] = request.flink_resource_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.item_condition_array):
            body['ItemConditionArray'] = request.item_condition_array
        if not DaraCore.is_null(request.item_condition_express):
            body['ItemConditionExpress'] = request.item_condition_express
        if not DaraCore.is_null(request.item_condition_type):
            body['ItemConditionType'] = request.item_condition_type
        if not DaraCore.is_null(request.item_table_meta_id):
            body['ItemTableMetaId'] = request.item_table_meta_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.pre_experiment_ids):
            body['PreExperimentIds'] = request.pre_experiment_ids
        if not DaraCore.is_null(request.prod_experiment_ids):
            body['ProdExperimentIds'] = request.prod_experiment_ids
        if not DaraCore.is_null(request.scene_id):
            body['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.service_id):
            body['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_ids):
            body['ServiceIds'] = request.service_ids
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.statis_baeavior_condition_array):
            body['StatisBaeaviorConditionArray'] = request.statis_baeavior_condition_array
        if not DaraCore.is_null(request.statis_behavior_condition_array):
            body['StatisBehaviorConditionArray'] = request.statis_behavior_condition_array
        if not DaraCore.is_null(request.statis_behavior_condition_express):
            body['StatisBehaviorConditionExpress'] = request.statis_behavior_condition_express
        if not DaraCore.is_null(request.statis_behavior_condition_type):
            body['StatisBehaviorConditionType'] = request.statis_behavior_condition_type
        if not DaraCore.is_null(request.traffic_control_targets):
            body['TrafficControlTargets'] = request.traffic_control_targets
        if not DaraCore.is_null(request.user_condition_array):
            body['UserConditionArray'] = request.user_condition_array
        if not DaraCore.is_null(request.user_condition_express):
            body['UserConditionExpress'] = request.user_condition_express
        if not DaraCore.is_null(request.user_condition_type):
            body['UserConditionType'] = request.user_condition_type
        if not DaraCore.is_null(request.user_table_meta_id):
            body['UserTableMetaId'] = request.user_table_meta_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTrafficControlTask',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltasks/{DaraURL.percent_encode(traffic_control_task_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTrafficControlTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_traffic_control_task(
        self,
        traffic_control_task_id: str,
        request: main_models.UpdateTrafficControlTaskRequest,
    ) -> main_models.UpdateTrafficControlTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_traffic_control_task_with_options(traffic_control_task_id, request, headers, runtime)

    async def update_traffic_control_task_async(
        self,
        traffic_control_task_id: str,
        request: main_models.UpdateTrafficControlTaskRequest,
    ) -> main_models.UpdateTrafficControlTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_traffic_control_task_with_options_async(traffic_control_task_id, request, headers, runtime)

    def update_traffic_control_task_traffic_with_options(
        self,
        traffic_control_task_id: str,
        request: main_models.UpdateTrafficControlTaskTrafficRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTrafficControlTaskTrafficResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_param_3):
            query['new-param-3'] = request.new_param_3
        body = {}
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.traffics):
            body['Traffics'] = request.traffics
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTrafficControlTaskTraffic',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltasks/{DaraURL.percent_encode(traffic_control_task_id)}/action/traffic',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTrafficControlTaskTrafficResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_traffic_control_task_traffic_with_options_async(
        self,
        traffic_control_task_id: str,
        request: main_models.UpdateTrafficControlTaskTrafficRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTrafficControlTaskTrafficResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_param_3):
            query['new-param-3'] = request.new_param_3
        body = {}
        if not DaraCore.is_null(request.environment):
            body['Environment'] = request.environment
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.traffics):
            body['Traffics'] = request.traffics
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTrafficControlTaskTraffic',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trafficcontroltasks/{DaraURL.percent_encode(traffic_control_task_id)}/action/traffic',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTrafficControlTaskTrafficResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_traffic_control_task_traffic(
        self,
        traffic_control_task_id: str,
        request: main_models.UpdateTrafficControlTaskTrafficRequest,
    ) -> main_models.UpdateTrafficControlTaskTrafficResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_traffic_control_task_traffic_with_options(traffic_control_task_id, request, headers, runtime)

    async def update_traffic_control_task_traffic_async(
        self,
        traffic_control_task_id: str,
        request: main_models.UpdateTrafficControlTaskTrafficRequest,
    ) -> main_models.UpdateTrafficControlTaskTrafficResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_traffic_control_task_traffic_with_options_async(traffic_control_task_id, request, headers, runtime)

    def upload_recommendation_data_with_options(
        self,
        request: main_models.UploadRecommendationDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UploadRecommendationDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.data_type):
            body['DataType'] = request.data_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadRecommendationData',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recommendationdata/action/upload',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadRecommendationDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_recommendation_data_with_options_async(
        self,
        request: main_models.UploadRecommendationDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UploadRecommendationDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.data_type):
            body['DataType'] = request.data_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadRecommendationData',
            version = '2022-12-13',
            protocol = 'HTTPS',
            pathname = f'/api/v1/recommendationdata/action/upload',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadRecommendationDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_recommendation_data(
        self,
        request: main_models.UploadRecommendationDataRequest,
    ) -> main_models.UploadRecommendationDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.upload_recommendation_data_with_options(request, headers, runtime)

    async def upload_recommendation_data_async(
        self,
        request: main_models.UploadRecommendationDataRequest,
    ) -> main_models.UploadRecommendationDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.upload_recommendation_data_with_options_async(request, headers, runtime)
