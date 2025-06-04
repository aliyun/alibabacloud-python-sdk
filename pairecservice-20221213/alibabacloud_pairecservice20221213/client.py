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

    def apply_engine_config_with_options(
        self,
        engine_config_id: str,
        request: pai_rec_service_20221213_models.ApplyEngineConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ApplyEngineConfigResponse:
        """
        @summary 应用/发布指定的推荐引擎配置
        
        @param request: ApplyEngineConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyEngineConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyEngineConfig',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/engineconfigs/{OpenApiUtilClient.get_encode_param(engine_config_id)}/action/apply',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ApplyEngineConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_engine_config_with_options_async(
        self,
        engine_config_id: str,
        request: pai_rec_service_20221213_models.ApplyEngineConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ApplyEngineConfigResponse:
        """
        @summary 应用/发布指定的推荐引擎配置
        
        @param request: ApplyEngineConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyEngineConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyEngineConfig',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/engineconfigs/{OpenApiUtilClient.get_encode_param(engine_config_id)}/action/apply',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ApplyEngineConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_engine_config(
        self,
        engine_config_id: str,
        request: pai_rec_service_20221213_models.ApplyEngineConfigRequest,
    ) -> pai_rec_service_20221213_models.ApplyEngineConfigResponse:
        """
        @summary 应用/发布指定的推荐引擎配置
        
        @param request: ApplyEngineConfigRequest
        @return: ApplyEngineConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.apply_engine_config_with_options(engine_config_id, request, headers, runtime)

    async def apply_engine_config_async(
        self,
        engine_config_id: str,
        request: pai_rec_service_20221213_models.ApplyEngineConfigRequest,
    ) -> pai_rec_service_20221213_models.ApplyEngineConfigResponse:
        """
        @summary 应用/发布指定的推荐引擎配置
        
        @param request: ApplyEngineConfigRequest
        @return: ApplyEngineConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.apply_engine_config_with_options_async(engine_config_id, request, headers, runtime)

    def backflow_feature_consistency_check_job_data_with_options(
        self,
        request: pai_rec_service_20221213_models.BackflowFeatureConsistencyCheckJobDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.BackflowFeatureConsistencyCheckJobDataResponse:
        """
        @summary 特征一致性检查数据回流。
        
        @param request: BackflowFeatureConsistencyCheckJobDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BackflowFeatureConsistencyCheckJobDataResponse
        """
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
        if not UtilClient.is_unset(request.service_name):
            body['ServiceName'] = request.service_name
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
        """
        @summary 特征一致性检查数据回流。
        
        @param request: BackflowFeatureConsistencyCheckJobDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BackflowFeatureConsistencyCheckJobDataResponse
        """
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
        if not UtilClient.is_unset(request.service_name):
            body['ServiceName'] = request.service_name
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
        """
        @summary 特征一致性检查数据回流。
        
        @param request: BackflowFeatureConsistencyCheckJobDataRequest
        @return: BackflowFeatureConsistencyCheckJobDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.backflow_feature_consistency_check_job_data_with_options(request, headers, runtime)

    async def backflow_feature_consistency_check_job_data_async(
        self,
        request: pai_rec_service_20221213_models.BackflowFeatureConsistencyCheckJobDataRequest,
    ) -> pai_rec_service_20221213_models.BackflowFeatureConsistencyCheckJobDataResponse:
        """
        @summary 特征一致性检查数据回流。
        
        @param request: BackflowFeatureConsistencyCheckJobDataRequest
        @return: BackflowFeatureConsistencyCheckJobDataResponse
        """
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
        """
        @summary 检测实例下配置的资源的连接状态。
        
        @param request: CheckInstanceResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckInstanceResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
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
        """
        @summary 检测实例下配置的资源的连接状态。
        
        @param request: CheckInstanceResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckInstanceResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
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
        """
        @summary 检测实例下配置的资源的连接状态。
        
        @param request: CheckInstanceResourcesRequest
        @return: CheckInstanceResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_instance_resources_with_options(instance_id, request, headers, runtime)

    async def check_instance_resources_async(
        self,
        instance_id: str,
        request: pai_rec_service_20221213_models.CheckInstanceResourcesRequest,
    ) -> pai_rec_service_20221213_models.CheckInstanceResourcesResponse:
        """
        @summary 检测实例下配置的资源的连接状态。
        
        @param request: CheckInstanceResourcesRequest
        @return: CheckInstanceResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.check_instance_resources_with_options_async(instance_id, request, headers, runtime)

    def check_traffic_control_task_expression_with_options(
        self,
        request: pai_rec_service_20221213_models.CheckTrafficControlTaskExpressionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CheckTrafficControlTaskExpressionResponse:
        """
        @summary 校验流量调控任务中的表达式
        
        @param request: CheckTrafficControlTaskExpressionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckTrafficControlTaskExpressionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expression):
            query['Expression'] = request.expression
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.table_meta_id):
            query['TableMetaId'] = request.table_meta_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckTrafficControlTaskExpression',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltasks/action/checkexpression',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CheckTrafficControlTaskExpressionResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_traffic_control_task_expression_with_options_async(
        self,
        request: pai_rec_service_20221213_models.CheckTrafficControlTaskExpressionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CheckTrafficControlTaskExpressionResponse:
        """
        @summary 校验流量调控任务中的表达式
        
        @param request: CheckTrafficControlTaskExpressionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckTrafficControlTaskExpressionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expression):
            query['Expression'] = request.expression
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.table_meta_id):
            query['TableMetaId'] = request.table_meta_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckTrafficControlTaskExpression',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltasks/action/checkexpression',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CheckTrafficControlTaskExpressionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_traffic_control_task_expression(
        self,
        request: pai_rec_service_20221213_models.CheckTrafficControlTaskExpressionRequest,
    ) -> pai_rec_service_20221213_models.CheckTrafficControlTaskExpressionResponse:
        """
        @summary 校验流量调控任务中的表达式
        
        @param request: CheckTrafficControlTaskExpressionRequest
        @return: CheckTrafficControlTaskExpressionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_traffic_control_task_expression_with_options(request, headers, runtime)

    async def check_traffic_control_task_expression_async(
        self,
        request: pai_rec_service_20221213_models.CheckTrafficControlTaskExpressionRequest,
    ) -> pai_rec_service_20221213_models.CheckTrafficControlTaskExpressionResponse:
        """
        @summary 校验流量调控任务中的表达式
        
        @param request: CheckTrafficControlTaskExpressionRequest
        @return: CheckTrafficControlTaskExpressionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.check_traffic_control_task_expression_with_options_async(request, headers, runtime)

    def clone_engine_config_with_options(
        self,
        engine_config_id: str,
        request: pai_rec_service_20221213_models.CloneEngineConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CloneEngineConfigResponse:
        """
        @summary 克隆指定的推荐引擎配置
        
        @param request: CloneEngineConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneEngineConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config_value):
            body['ConfigValue'] = request.config_value
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloneEngineConfig',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/engineconfigs/{OpenApiUtilClient.get_encode_param(engine_config_id)}/action/clone',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CloneEngineConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_engine_config_with_options_async(
        self,
        engine_config_id: str,
        request: pai_rec_service_20221213_models.CloneEngineConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CloneEngineConfigResponse:
        """
        @summary 克隆指定的推荐引擎配置
        
        @param request: CloneEngineConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneEngineConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config_value):
            body['ConfigValue'] = request.config_value
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloneEngineConfig',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/engineconfigs/{OpenApiUtilClient.get_encode_param(engine_config_id)}/action/clone',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CloneEngineConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_engine_config(
        self,
        engine_config_id: str,
        request: pai_rec_service_20221213_models.CloneEngineConfigRequest,
    ) -> pai_rec_service_20221213_models.CloneEngineConfigResponse:
        """
        @summary 克隆指定的推荐引擎配置
        
        @param request: CloneEngineConfigRequest
        @return: CloneEngineConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clone_engine_config_with_options(engine_config_id, request, headers, runtime)

    async def clone_engine_config_async(
        self,
        engine_config_id: str,
        request: pai_rec_service_20221213_models.CloneEngineConfigRequest,
    ) -> pai_rec_service_20221213_models.CloneEngineConfigResponse:
        """
        @summary 克隆指定的推荐引擎配置
        
        @param request: CloneEngineConfigRequest
        @return: CloneEngineConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.clone_engine_config_with_options_async(engine_config_id, request, headers, runtime)

    def clone_experiment_with_options(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.CloneExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CloneExperimentResponse:
        """
        @summary 克隆实验。
        
        @param request: CloneExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneExperimentResponse
        """
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
        """
        @summary 克隆实验。
        
        @param request: CloneExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneExperimentResponse
        """
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
        """
        @summary 克隆实验。
        
        @param request: CloneExperimentRequest
        @return: CloneExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clone_experiment_with_options(experiment_id, request, headers, runtime)

    async def clone_experiment_async(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.CloneExperimentRequest,
    ) -> pai_rec_service_20221213_models.CloneExperimentResponse:
        """
        @summary 克隆实验。
        
        @param request: CloneExperimentRequest
        @return: CloneExperimentResponse
        """
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
        """
        @summary 克隆实验组，并克隆实验组下的所有实验至新的实验组中。
        
        @param request: CloneExperimentGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneExperimentGroupResponse
        """
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
        """
        @summary 克隆实验组，并克隆实验组下的所有实验至新的实验组中。
        
        @param request: CloneExperimentGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneExperimentGroupResponse
        """
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
        """
        @summary 克隆实验组，并克隆实验组下的所有实验至新的实验组中。
        
        @param request: CloneExperimentGroupRequest
        @return: CloneExperimentGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clone_experiment_group_with_options(experiment_group_id, request, headers, runtime)

    async def clone_experiment_group_async(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.CloneExperimentGroupRequest,
    ) -> pai_rec_service_20221213_models.CloneExperimentGroupResponse:
        """
        @summary 克隆实验组，并克隆实验组下的所有实验至新的实验组中。
        
        @param request: CloneExperimentGroupRequest
        @return: CloneExperimentGroupResponse
        """
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
        """
        @summary 克隆特征一致性检查配置。
        
        @param request: CloneFeatureConsistencyCheckJobConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneFeatureConsistencyCheckJobConfigResponse
        """
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
        """
        @summary 克隆特征一致性检查配置。
        
        @param request: CloneFeatureConsistencyCheckJobConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneFeatureConsistencyCheckJobConfigResponse
        """
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
        """
        @summary 克隆特征一致性检查配置。
        
        @param request: CloneFeatureConsistencyCheckJobConfigRequest
        @return: CloneFeatureConsistencyCheckJobConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clone_feature_consistency_check_job_config_with_options(source_feature_consistency_check_job_config_id, request, headers, runtime)

    async def clone_feature_consistency_check_job_config_async(
        self,
        source_feature_consistency_check_job_config_id: str,
        request: pai_rec_service_20221213_models.CloneFeatureConsistencyCheckJobConfigRequest,
    ) -> pai_rec_service_20221213_models.CloneFeatureConsistencyCheckJobConfigResponse:
        """
        @summary 克隆特征一致性检查配置。
        
        @param request: CloneFeatureConsistencyCheckJobConfigRequest
        @return: CloneFeatureConsistencyCheckJobConfigResponse
        """
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
        """
        @summary 克隆实验室。
        
        @param request: CloneLaboratoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneLaboratoryResponse
        """
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
        """
        @summary 克隆实验室。
        
        @param request: CloneLaboratoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneLaboratoryResponse
        """
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
        """
        @summary 克隆实验室。
        
        @param request: CloneLaboratoryRequest
        @return: CloneLaboratoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clone_laboratory_with_options(laboratory_id, request, headers, runtime)

    async def clone_laboratory_async(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.CloneLaboratoryRequest,
    ) -> pai_rec_service_20221213_models.CloneLaboratoryResponse:
        """
        @summary 克隆实验室。
        
        @param request: CloneLaboratoryRequest
        @return: CloneLaboratoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.clone_laboratory_with_options_async(laboratory_id, request, headers, runtime)

    def clone_traffic_control_task_with_options(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.CloneTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CloneTrafficControlTaskResponse:
        """
        @summary 克隆流量调控任务
        
        @param request: CloneTrafficControlTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneTrafficControlTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloneTrafficControlTask',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltasks/{OpenApiUtilClient.get_encode_param(traffic_control_task_id)}/action/clone',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CloneTrafficControlTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_traffic_control_task_with_options_async(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.CloneTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CloneTrafficControlTaskResponse:
        """
        @summary 克隆流量调控任务
        
        @param request: CloneTrafficControlTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneTrafficControlTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloneTrafficControlTask',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltasks/{OpenApiUtilClient.get_encode_param(traffic_control_task_id)}/action/clone',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CloneTrafficControlTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_traffic_control_task(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.CloneTrafficControlTaskRequest,
    ) -> pai_rec_service_20221213_models.CloneTrafficControlTaskResponse:
        """
        @summary 克隆流量调控任务
        
        @param request: CloneTrafficControlTaskRequest
        @return: CloneTrafficControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clone_traffic_control_task_with_options(traffic_control_task_id, request, headers, runtime)

    async def clone_traffic_control_task_async(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.CloneTrafficControlTaskRequest,
    ) -> pai_rec_service_20221213_models.CloneTrafficControlTaskResponse:
        """
        @summary 克隆流量调控任务
        
        @param request: CloneTrafficControlTaskRequest
        @return: CloneTrafficControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.clone_traffic_control_task_with_options_async(traffic_control_task_id, request, headers, runtime)

    def compare_sample_consistency_job_with_options(
        self,
        sample_consistency_job_id: str,
        request: pai_rec_service_20221213_models.CompareSampleConsistencyJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CompareSampleConsistencyJobResponse:
        """
        @summary 对比样本一致性任务
        
        @param request: CompareSampleConsistencyJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CompareSampleConsistencyJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CompareSampleConsistencyJob',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/sampleconsistencyjobs/{OpenApiUtilClient.get_encode_param(sample_consistency_job_id)}/action/compare',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CompareSampleConsistencyJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def compare_sample_consistency_job_with_options_async(
        self,
        sample_consistency_job_id: str,
        request: pai_rec_service_20221213_models.CompareSampleConsistencyJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CompareSampleConsistencyJobResponse:
        """
        @summary 对比样本一致性任务
        
        @param request: CompareSampleConsistencyJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CompareSampleConsistencyJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CompareSampleConsistencyJob',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/sampleconsistencyjobs/{OpenApiUtilClient.get_encode_param(sample_consistency_job_id)}/action/compare',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CompareSampleConsistencyJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def compare_sample_consistency_job(
        self,
        sample_consistency_job_id: str,
        request: pai_rec_service_20221213_models.CompareSampleConsistencyJobRequest,
    ) -> pai_rec_service_20221213_models.CompareSampleConsistencyJobResponse:
        """
        @summary 对比样本一致性任务
        
        @param request: CompareSampleConsistencyJobRequest
        @return: CompareSampleConsistencyJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.compare_sample_consistency_job_with_options(sample_consistency_job_id, request, headers, runtime)

    async def compare_sample_consistency_job_async(
        self,
        sample_consistency_job_id: str,
        request: pai_rec_service_20221213_models.CompareSampleConsistencyJobRequest,
    ) -> pai_rec_service_20221213_models.CompareSampleConsistencyJobResponse:
        """
        @summary 对比样本一致性任务
        
        @param request: CompareSampleConsistencyJobRequest
        @return: CompareSampleConsistencyJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.compare_sample_consistency_job_with_options_async(sample_consistency_job_id, request, headers, runtime)

    def create_abmetric_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateABMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateABMetricResponse:
        """
        @summary 创建AB test实验指标
        
        @param request: CreateABMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateABMetricResponse
        """
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
        """
        @summary 创建AB test实验指标
        
        @param request: CreateABMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateABMetricResponse
        """
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
        """
        @summary 创建AB test实验指标
        
        @param request: CreateABMetricRequest
        @return: CreateABMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_abmetric_with_options(request, headers, runtime)

    async def create_abmetric_async(
        self,
        request: pai_rec_service_20221213_models.CreateABMetricRequest,
    ) -> pai_rec_service_20221213_models.CreateABMetricResponse:
        """
        @summary 创建AB test实验指标
        
        @param request: CreateABMetricRequest
        @return: CreateABMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_abmetric_with_options_async(request, headers, runtime)

    def create_abmetric_group_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateABMetricGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateABMetricGroupResponse:
        """
        @summary 创建指标组
        
        @param request: CreateABMetricGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateABMetricGroupResponse
        """
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
        """
        @summary 创建指标组
        
        @param request: CreateABMetricGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateABMetricGroupResponse
        """
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
        """
        @summary 创建指标组
        
        @param request: CreateABMetricGroupRequest
        @return: CreateABMetricGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_abmetric_group_with_options(request, headers, runtime)

    async def create_abmetric_group_async(
        self,
        request: pai_rec_service_20221213_models.CreateABMetricGroupRequest,
    ) -> pai_rec_service_20221213_models.CreateABMetricGroupResponse:
        """
        @summary 创建指标组
        
        @param request: CreateABMetricGroupRequest
        @return: CreateABMetricGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_abmetric_group_with_options_async(request, headers, runtime)

    def create_calculation_jobs_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateCalculationJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateCalculationJobsResponse:
        """
        @summary 创建AB指标的计算任务。
        
        @param request: CreateCalculationJobsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCalculationJobsResponse
        """
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
        """
        @summary 创建AB指标的计算任务。
        
        @param request: CreateCalculationJobsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCalculationJobsResponse
        """
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
        """
        @summary 创建AB指标的计算任务。
        
        @param request: CreateCalculationJobsRequest
        @return: CreateCalculationJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_calculation_jobs_with_options(request, headers, runtime)

    async def create_calculation_jobs_async(
        self,
        request: pai_rec_service_20221213_models.CreateCalculationJobsRequest,
    ) -> pai_rec_service_20221213_models.CreateCalculationJobsResponse:
        """
        @summary 创建AB指标的计算任务。
        
        @param request: CreateCalculationJobsRequest
        @return: CreateCalculationJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_calculation_jobs_with_options_async(request, headers, runtime)

    def create_crowd_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateCrowdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateCrowdResponse:
        """
        @summary 创建人群。
        
        @param request: CreateCrowdRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCrowdResponse
        """
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
        """
        @summary 创建人群。
        
        @param request: CreateCrowdRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCrowdResponse
        """
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
        """
        @summary 创建人群。
        
        @param request: CreateCrowdRequest
        @return: CreateCrowdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_crowd_with_options(request, headers, runtime)

    async def create_crowd_async(
        self,
        request: pai_rec_service_20221213_models.CreateCrowdRequest,
    ) -> pai_rec_service_20221213_models.CreateCrowdResponse:
        """
        @summary 创建人群。
        
        @param request: CreateCrowdRequest
        @return: CreateCrowdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_crowd_with_options_async(request, headers, runtime)

    def create_engine_config_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateEngineConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateEngineConfigResponse:
        """
        @summary 创建引擎配置
        
        @param request: CreateEngineConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEngineConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config_value):
            body['ConfigValue'] = request.config_value
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEngineConfig',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/engineconfigs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateEngineConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_engine_config_with_options_async(
        self,
        request: pai_rec_service_20221213_models.CreateEngineConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateEngineConfigResponse:
        """
        @summary 创建引擎配置
        
        @param request: CreateEngineConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEngineConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config_value):
            body['ConfigValue'] = request.config_value
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEngineConfig',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/engineconfigs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateEngineConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_engine_config(
        self,
        request: pai_rec_service_20221213_models.CreateEngineConfigRequest,
    ) -> pai_rec_service_20221213_models.CreateEngineConfigResponse:
        """
        @summary 创建引擎配置
        
        @param request: CreateEngineConfigRequest
        @return: CreateEngineConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_engine_config_with_options(request, headers, runtime)

    async def create_engine_config_async(
        self,
        request: pai_rec_service_20221213_models.CreateEngineConfigRequest,
    ) -> pai_rec_service_20221213_models.CreateEngineConfigResponse:
        """
        @summary 创建引擎配置
        
        @param request: CreateEngineConfigRequest
        @return: CreateEngineConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_engine_config_with_options_async(request, headers, runtime)

    def create_experiment_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateExperimentResponse:
        """
        @summary 创建实验。
        
        @param request: CreateExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateExperimentResponse
        """
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
        """
        @summary 创建实验。
        
        @param request: CreateExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateExperimentResponse
        """
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
        """
        @summary 创建实验。
        
        @param request: CreateExperimentRequest
        @return: CreateExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_experiment_with_options(request, headers, runtime)

    async def create_experiment_async(
        self,
        request: pai_rec_service_20221213_models.CreateExperimentRequest,
    ) -> pai_rec_service_20221213_models.CreateExperimentResponse:
        """
        @summary 创建实验。
        
        @param request: CreateExperimentRequest
        @return: CreateExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_experiment_with_options_async(request, headers, runtime)

    def create_experiment_group_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateExperimentGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateExperimentGroupResponse:
        """
        @summary 创建实验组。
        
        @param request: CreateExperimentGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateExperimentGroupResponse
        """
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
        """
        @summary 创建实验组。
        
        @param request: CreateExperimentGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateExperimentGroupResponse
        """
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
        """
        @summary 创建实验组。
        
        @param request: CreateExperimentGroupRequest
        @return: CreateExperimentGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_experiment_group_with_options(request, headers, runtime)

    async def create_experiment_group_async(
        self,
        request: pai_rec_service_20221213_models.CreateExperimentGroupRequest,
    ) -> pai_rec_service_20221213_models.CreateExperimentGroupResponse:
        """
        @summary 创建实验组。
        
        @param request: CreateExperimentGroupRequest
        @return: CreateExperimentGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_experiment_group_with_options_async(request, headers, runtime)

    def create_feature_consistency_check_job_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobResponse:
        """
        @summary 创建特征一致性检查任务。
        
        @param request: CreateFeatureConsistencyCheckJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFeatureConsistencyCheckJobResponse
        """
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
        """
        @summary 创建特征一致性检查任务。
        
        @param request: CreateFeatureConsistencyCheckJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFeatureConsistencyCheckJobResponse
        """
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
        """
        @summary 创建特征一致性检查任务。
        
        @param request: CreateFeatureConsistencyCheckJobRequest
        @return: CreateFeatureConsistencyCheckJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_feature_consistency_check_job_with_options(request, headers, runtime)

    async def create_feature_consistency_check_job_async(
        self,
        request: pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobRequest,
    ) -> pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobResponse:
        """
        @summary 创建特征一致性检查任务。
        
        @param request: CreateFeatureConsistencyCheckJobRequest
        @return: CreateFeatureConsistencyCheckJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_feature_consistency_check_job_with_options_async(request, headers, runtime)

    def create_feature_consistency_check_job_config_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobConfigResponse:
        """
        @summary 创建特征一致性检查配置。
        
        @param request: CreateFeatureConsistencyCheckJobConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFeatureConsistencyCheckJobConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.compare_feature):
            body['CompareFeature'] = request.compare_feature
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.dataset_mount_path):
            body['DatasetMountPath'] = request.dataset_mount_path
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.dataset_type):
            body['DatasetType'] = request.dataset_type
        if not UtilClient.is_unset(request.dataset_uri):
            body['DatasetUri'] = request.dataset_uri
        if not UtilClient.is_unset(request.default_route):
            body['DefaultRoute'] = request.default_route
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
        if not UtilClient.is_unset(request.predict_worker_count):
            body['PredictWorkerCount'] = request.predict_worker_count
        if not UtilClient.is_unset(request.predict_worker_cpu):
            body['PredictWorkerCpu'] = request.predict_worker_cpu
        if not UtilClient.is_unset(request.predict_worker_memory):
            body['PredictWorkerMemory'] = request.predict_worker_memory
        if not UtilClient.is_unset(request.resource_config):
            body['ResourceConfig'] = request.resource_config
        if not UtilClient.is_unset(request.sample_rate):
            body['SampleRate'] = request.sample_rate
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.security_group_id):
            body['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.switch_id):
            body['SwitchId'] = request.switch_id
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
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.workflow_name):
            body['WorkflowName'] = request.workflow_name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
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
        """
        @summary 创建特征一致性检查配置。
        
        @param request: CreateFeatureConsistencyCheckJobConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFeatureConsistencyCheckJobConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.compare_feature):
            body['CompareFeature'] = request.compare_feature
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.dataset_mount_path):
            body['DatasetMountPath'] = request.dataset_mount_path
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.dataset_type):
            body['DatasetType'] = request.dataset_type
        if not UtilClient.is_unset(request.dataset_uri):
            body['DatasetUri'] = request.dataset_uri
        if not UtilClient.is_unset(request.default_route):
            body['DefaultRoute'] = request.default_route
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
        if not UtilClient.is_unset(request.predict_worker_count):
            body['PredictWorkerCount'] = request.predict_worker_count
        if not UtilClient.is_unset(request.predict_worker_cpu):
            body['PredictWorkerCpu'] = request.predict_worker_cpu
        if not UtilClient.is_unset(request.predict_worker_memory):
            body['PredictWorkerMemory'] = request.predict_worker_memory
        if not UtilClient.is_unset(request.resource_config):
            body['ResourceConfig'] = request.resource_config
        if not UtilClient.is_unset(request.sample_rate):
            body['SampleRate'] = request.sample_rate
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.security_group_id):
            body['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.switch_id):
            body['SwitchId'] = request.switch_id
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
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.workflow_name):
            body['WorkflowName'] = request.workflow_name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
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
        """
        @summary 创建特征一致性检查配置。
        
        @param request: CreateFeatureConsistencyCheckJobConfigRequest
        @return: CreateFeatureConsistencyCheckJobConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_feature_consistency_check_job_config_with_options(request, headers, runtime)

    async def create_feature_consistency_check_job_config_async(
        self,
        request: pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobConfigRequest,
    ) -> pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobConfigResponse:
        """
        @summary 创建特征一致性检查配置。
        
        @param request: CreateFeatureConsistencyCheckJobConfigRequest
        @return: CreateFeatureConsistencyCheckJobConfigResponse
        """
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
        """
        @summary 为指定实例配置创建新的配置资源
        
        @param request: CreateInstanceResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResourceResponse
        """
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
        """
        @summary 为指定实例配置创建新的配置资源
        
        @param request: CreateInstanceResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResourceResponse
        """
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
        """
        @summary 为指定实例配置创建新的配置资源
        
        @param request: CreateInstanceResourceRequest
        @return: CreateInstanceResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_resource_with_options(instance_id, request, headers, runtime)

    async def create_instance_resource_async(
        self,
        instance_id: str,
        request: pai_rec_service_20221213_models.CreateInstanceResourceRequest,
    ) -> pai_rec_service_20221213_models.CreateInstanceResourceResponse:
        """
        @summary 为指定实例配置创建新的配置资源
        
        @param request: CreateInstanceResourceRequest
        @return: CreateInstanceResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_resource_with_options_async(instance_id, request, headers, runtime)

    def create_laboratory_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateLaboratoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateLaboratoryResponse:
        """
        @summary 创建实验室
        
        @param request: CreateLaboratoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLaboratoryResponse
        """
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
        """
        @summary 创建实验室
        
        @param request: CreateLaboratoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLaboratoryResponse
        """
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
        """
        @summary 创建实验室
        
        @param request: CreateLaboratoryRequest
        @return: CreateLaboratoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_laboratory_with_options(request, headers, runtime)

    async def create_laboratory_async(
        self,
        request: pai_rec_service_20221213_models.CreateLaboratoryRequest,
    ) -> pai_rec_service_20221213_models.CreateLaboratoryResponse:
        """
        @summary 创建实验室
        
        @param request: CreateLaboratoryRequest
        @return: CreateLaboratoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_laboratory_with_options_async(request, headers, runtime)

    def create_layer_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateLayerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateLayerResponse:
        """
        @summary 创建层。
        
        @param request: CreateLayerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLayerResponse
        """
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
        """
        @summary 创建层。
        
        @param request: CreateLayerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLayerResponse
        """
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
        """
        @summary 创建层。
        
        @param request: CreateLayerRequest
        @return: CreateLayerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_layer_with_options(request, headers, runtime)

    async def create_layer_async(
        self,
        request: pai_rec_service_20221213_models.CreateLayerRequest,
    ) -> pai_rec_service_20221213_models.CreateLayerResponse:
        """
        @summary 创建层。
        
        @param request: CreateLayerRequest
        @return: CreateLayerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_layer_with_options_async(request, headers, runtime)

    def create_param_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateParamRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateParamResponse:
        """
        @summary 创建参数。
        
        @param request: CreateParamRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateParamResponse
        """
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
        """
        @summary 创建参数。
        
        @param request: CreateParamRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateParamResponse
        """
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
        """
        @summary 创建参数。
        
        @param request: CreateParamRequest
        @return: CreateParamResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_param_with_options(request, headers, runtime)

    async def create_param_async(
        self,
        request: pai_rec_service_20221213_models.CreateParamRequest,
    ) -> pai_rec_service_20221213_models.CreateParamResponse:
        """
        @summary 创建参数。
        
        @param request: CreateParamRequest
        @return: CreateParamResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_param_with_options_async(request, headers, runtime)

    def create_resource_rule_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateResourceRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateResourceRuleResponse:
        """
        @summary 创建资源规则
        
        @param request: CreateResourceRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.metric_operation_type):
            body['MetricOperationType'] = request.metric_operation_type
        if not UtilClient.is_unset(request.metric_pull_info):
            body['MetricPullInfo'] = request.metric_pull_info
        if not UtilClient.is_unset(request.metric_pull_period):
            body['MetricPullPeriod'] = request.metric_pull_period
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.rule_computing_definition):
            body['RuleComputingDefinition'] = request.rule_computing_definition
        if not UtilClient.is_unset(request.rule_items):
            body['RuleItems'] = request.rule_items
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceRule',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/resourcerules',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateResourceRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_rule_with_options_async(
        self,
        request: pai_rec_service_20221213_models.CreateResourceRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateResourceRuleResponse:
        """
        @summary 创建资源规则
        
        @param request: CreateResourceRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.metric_operation_type):
            body['MetricOperationType'] = request.metric_operation_type
        if not UtilClient.is_unset(request.metric_pull_info):
            body['MetricPullInfo'] = request.metric_pull_info
        if not UtilClient.is_unset(request.metric_pull_period):
            body['MetricPullPeriod'] = request.metric_pull_period
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.rule_computing_definition):
            body['RuleComputingDefinition'] = request.rule_computing_definition
        if not UtilClient.is_unset(request.rule_items):
            body['RuleItems'] = request.rule_items
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceRule',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/resourcerules',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateResourceRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_rule(
        self,
        request: pai_rec_service_20221213_models.CreateResourceRuleRequest,
    ) -> pai_rec_service_20221213_models.CreateResourceRuleResponse:
        """
        @summary 创建资源规则
        
        @param request: CreateResourceRuleRequest
        @return: CreateResourceRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_resource_rule_with_options(request, headers, runtime)

    async def create_resource_rule_async(
        self,
        request: pai_rec_service_20221213_models.CreateResourceRuleRequest,
    ) -> pai_rec_service_20221213_models.CreateResourceRuleResponse:
        """
        @summary 创建资源规则
        
        @param request: CreateResourceRuleRequest
        @return: CreateResourceRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_resource_rule_with_options_async(request, headers, runtime)

    def create_resource_rule_item_with_options(
        self,
        resource_rule_id: str,
        request: pai_rec_service_20221213_models.CreateResourceRuleItemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateResourceRuleItemResponse:
        """
        @summary 创建资源规则条目
        
        @param request: CreateResourceRuleItemRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceRuleItemResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_value):
            body['MaxValue'] = request.max_value
        if not UtilClient.is_unset(request.min_value):
            body['MinValue'] = request.min_value
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceRuleItem',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/resourcerules/{OpenApiUtilClient.get_encode_param(resource_rule_id)}/items',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateResourceRuleItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_rule_item_with_options_async(
        self,
        resource_rule_id: str,
        request: pai_rec_service_20221213_models.CreateResourceRuleItemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateResourceRuleItemResponse:
        """
        @summary 创建资源规则条目
        
        @param request: CreateResourceRuleItemRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceRuleItemResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_value):
            body['MaxValue'] = request.max_value
        if not UtilClient.is_unset(request.min_value):
            body['MinValue'] = request.min_value
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceRuleItem',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/resourcerules/{OpenApiUtilClient.get_encode_param(resource_rule_id)}/items',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateResourceRuleItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_rule_item(
        self,
        resource_rule_id: str,
        request: pai_rec_service_20221213_models.CreateResourceRuleItemRequest,
    ) -> pai_rec_service_20221213_models.CreateResourceRuleItemResponse:
        """
        @summary 创建资源规则条目
        
        @param request: CreateResourceRuleItemRequest
        @return: CreateResourceRuleItemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_resource_rule_item_with_options(resource_rule_id, request, headers, runtime)

    async def create_resource_rule_item_async(
        self,
        resource_rule_id: str,
        request: pai_rec_service_20221213_models.CreateResourceRuleItemRequest,
    ) -> pai_rec_service_20221213_models.CreateResourceRuleItemResponse:
        """
        @summary 创建资源规则条目
        
        @param request: CreateResourceRuleItemRequest
        @return: CreateResourceRuleItemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_resource_rule_item_with_options_async(resource_rule_id, request, headers, runtime)

    def create_sample_consistency_job_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateSampleConsistencyJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateSampleConsistencyJobResponse:
        """
        @summary 创建样本一致性任务
        
        @param request: CreateSampleConsistencyJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSampleConsistencyJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.eas_model_service_name):
            body['EasModelServiceName'] = request.eas_model_service_name
        if not UtilClient.is_unset(request.feature_save_resource_id):
            body['FeatureSaveResourceId'] = request.feature_save_resource_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.item_id_field):
            body['ItemIdField'] = request.item_id_field
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.partition_field):
            body['PartitionField'] = request.partition_field
        if not UtilClient.is_unset(request.partition_field_format):
            body['PartitionFieldFormat'] = request.partition_field_format
        if not UtilClient.is_unset(request.request_id_field):
            body['RequestIdField'] = request.request_id_field
        if not UtilClient.is_unset(request.sample_rate):
            body['SampleRate'] = request.sample_rate
        if not UtilClient.is_unset(request.sample_table_name):
            body['SampleTableName'] = request.sample_table_name
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.user_id_field):
            body['UserIdField'] = request.user_id_field
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSampleConsistencyJob',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/sampleconsistencyjobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateSampleConsistencyJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sample_consistency_job_with_options_async(
        self,
        request: pai_rec_service_20221213_models.CreateSampleConsistencyJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateSampleConsistencyJobResponse:
        """
        @summary 创建样本一致性任务
        
        @param request: CreateSampleConsistencyJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSampleConsistencyJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.eas_model_service_name):
            body['EasModelServiceName'] = request.eas_model_service_name
        if not UtilClient.is_unset(request.feature_save_resource_id):
            body['FeatureSaveResourceId'] = request.feature_save_resource_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.item_id_field):
            body['ItemIdField'] = request.item_id_field
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.partition_field):
            body['PartitionField'] = request.partition_field
        if not UtilClient.is_unset(request.partition_field_format):
            body['PartitionFieldFormat'] = request.partition_field_format
        if not UtilClient.is_unset(request.request_id_field):
            body['RequestIdField'] = request.request_id_field
        if not UtilClient.is_unset(request.sample_rate):
            body['SampleRate'] = request.sample_rate
        if not UtilClient.is_unset(request.sample_table_name):
            body['SampleTableName'] = request.sample_table_name
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.user_id_field):
            body['UserIdField'] = request.user_id_field
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSampleConsistencyJob',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/sampleconsistencyjobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateSampleConsistencyJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sample_consistency_job(
        self,
        request: pai_rec_service_20221213_models.CreateSampleConsistencyJobRequest,
    ) -> pai_rec_service_20221213_models.CreateSampleConsistencyJobResponse:
        """
        @summary 创建样本一致性任务
        
        @param request: CreateSampleConsistencyJobRequest
        @return: CreateSampleConsistencyJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_sample_consistency_job_with_options(request, headers, runtime)

    async def create_sample_consistency_job_async(
        self,
        request: pai_rec_service_20221213_models.CreateSampleConsistencyJobRequest,
    ) -> pai_rec_service_20221213_models.CreateSampleConsistencyJobResponse:
        """
        @summary 创建样本一致性任务
        
        @param request: CreateSampleConsistencyJobRequest
        @return: CreateSampleConsistencyJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_sample_consistency_job_with_options_async(request, headers, runtime)

    def create_scene_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateSceneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateSceneResponse:
        """
        @summary 创建场景
        
        @param request: CreateSceneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSceneResponse
        """
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
        """
        @summary 创建场景
        
        @param request: CreateSceneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSceneResponse
        """
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
        """
        @summary 创建场景
        
        @param request: CreateSceneRequest
        @return: CreateSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_scene_with_options(request, headers, runtime)

    async def create_scene_async(
        self,
        request: pai_rec_service_20221213_models.CreateSceneRequest,
    ) -> pai_rec_service_20221213_models.CreateSceneResponse:
        """
        @summary 创建场景
        
        @param request: CreateSceneRequest
        @return: CreateSceneResponse
        """
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
        """
        @summary 在指定人群下创建子人群。
        
        @param request: CreateSubCrowdRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSubCrowdResponse
        """
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
        """
        @summary 在指定人群下创建子人群。
        
        @param request: CreateSubCrowdRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSubCrowdResponse
        """
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
        """
        @summary 在指定人群下创建子人群。
        
        @param request: CreateSubCrowdRequest
        @return: CreateSubCrowdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_sub_crowd_with_options(crowd_id, request, headers, runtime)

    async def create_sub_crowd_async(
        self,
        crowd_id: str,
        request: pai_rec_service_20221213_models.CreateSubCrowdRequest,
    ) -> pai_rec_service_20221213_models.CreateSubCrowdResponse:
        """
        @summary 在指定人群下创建子人群。
        
        @param request: CreateSubCrowdRequest
        @return: CreateSubCrowdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_sub_crowd_with_options_async(crowd_id, request, headers, runtime)

    def create_table_meta_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateTableMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateTableMetaResponse:
        """
        @summary 创建数据表。
        
        @param request: CreateTableMetaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTableMetaResponse
        """
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
        """
        @summary 创建数据表。
        
        @param request: CreateTableMetaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTableMetaResponse
        """
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
        """
        @summary 创建数据表。
        
        @param request: CreateTableMetaRequest
        @return: CreateTableMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_table_meta_with_options(request, headers, runtime)

    async def create_table_meta_async(
        self,
        request: pai_rec_service_20221213_models.CreateTableMetaRequest,
    ) -> pai_rec_service_20221213_models.CreateTableMetaResponse:
        """
        @summary 创建数据表。
        
        @param request: CreateTableMetaRequest
        @return: CreateTableMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_table_meta_with_options_async(request, headers, runtime)

    def create_traffic_control_target_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateTrafficControlTargetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateTrafficControlTargetResponse:
        """
        @summary 创建流量调控目标
        
        @param request: CreateTrafficControlTargetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTrafficControlTargetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event):
            body['Event'] = request.event
        if not UtilClient.is_unset(request.item_condition_array):
            body['ItemConditionArray'] = request.item_condition_array
        if not UtilClient.is_unset(request.item_condition_express):
            body['ItemConditionExpress'] = request.item_condition_express
        if not UtilClient.is_unset(request.item_condition_type):
            body['ItemConditionType'] = request.item_condition_type
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.new_product_regulation):
            body['NewProductRegulation'] = request.new_product_regulation
        if not UtilClient.is_unset(request.recall_name):
            body['RecallName'] = request.recall_name
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.statis_period):
            body['StatisPeriod'] = request.statis_period
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tolerance_value):
            body['ToleranceValue'] = request.tolerance_value
        if not UtilClient.is_unset(request.traffic_control_task_id):
            body['TrafficControlTaskId'] = request.traffic_control_task_id
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTrafficControlTarget',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltargets',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateTrafficControlTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_traffic_control_target_with_options_async(
        self,
        request: pai_rec_service_20221213_models.CreateTrafficControlTargetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateTrafficControlTargetResponse:
        """
        @summary 创建流量调控目标
        
        @param request: CreateTrafficControlTargetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTrafficControlTargetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event):
            body['Event'] = request.event
        if not UtilClient.is_unset(request.item_condition_array):
            body['ItemConditionArray'] = request.item_condition_array
        if not UtilClient.is_unset(request.item_condition_express):
            body['ItemConditionExpress'] = request.item_condition_express
        if not UtilClient.is_unset(request.item_condition_type):
            body['ItemConditionType'] = request.item_condition_type
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.new_product_regulation):
            body['NewProductRegulation'] = request.new_product_regulation
        if not UtilClient.is_unset(request.recall_name):
            body['RecallName'] = request.recall_name
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.statis_period):
            body['StatisPeriod'] = request.statis_period
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tolerance_value):
            body['ToleranceValue'] = request.tolerance_value
        if not UtilClient.is_unset(request.traffic_control_task_id):
            body['TrafficControlTaskId'] = request.traffic_control_task_id
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTrafficControlTarget',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltargets',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateTrafficControlTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_traffic_control_target(
        self,
        request: pai_rec_service_20221213_models.CreateTrafficControlTargetRequest,
    ) -> pai_rec_service_20221213_models.CreateTrafficControlTargetResponse:
        """
        @summary 创建流量调控目标
        
        @param request: CreateTrafficControlTargetRequest
        @return: CreateTrafficControlTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_traffic_control_target_with_options(request, headers, runtime)

    async def create_traffic_control_target_async(
        self,
        request: pai_rec_service_20221213_models.CreateTrafficControlTargetRequest,
    ) -> pai_rec_service_20221213_models.CreateTrafficControlTargetResponse:
        """
        @summary 创建流量调控目标
        
        @param request: CreateTrafficControlTargetRequest
        @return: CreateTrafficControlTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_traffic_control_target_with_options_async(request, headers, runtime)

    def create_traffic_control_task_with_options(
        self,
        request: pai_rec_service_20221213_models.CreateTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateTrafficControlTaskResponse:
        """
        @summary 创建流量调控任务
        
        @param request: CreateTrafficControlTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTrafficControlTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.behavior_table_meta_id):
            body['BehaviorTableMetaId'] = request.behavior_table_meta_id
        if not UtilClient.is_unset(request.control_granularity):
            body['ControlGranularity'] = request.control_granularity
        if not UtilClient.is_unset(request.control_logic):
            body['ControlLogic'] = request.control_logic
        if not UtilClient.is_unset(request.control_type):
            body['ControlType'] = request.control_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.execution_time):
            body['ExecutionTime'] = request.execution_time
        if not UtilClient.is_unset(request.flink_resource_id):
            body['FlinkResourceId'] = request.flink_resource_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.item_condition_array):
            body['ItemConditionArray'] = request.item_condition_array
        if not UtilClient.is_unset(request.item_condition_express):
            body['ItemConditionExpress'] = request.item_condition_express
        if not UtilClient.is_unset(request.item_condition_type):
            body['ItemConditionType'] = request.item_condition_type
        if not UtilClient.is_unset(request.item_table_meta_id):
            body['ItemTableMetaId'] = request.item_table_meta_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.pre_experiment_ids):
            body['PreExperimentIds'] = request.pre_experiment_ids
        if not UtilClient.is_unset(request.prod_experiment_ids):
            body['ProdExperimentIds'] = request.prod_experiment_ids
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.statis_behavior_condition_array):
            body['StatisBehaviorConditionArray'] = request.statis_behavior_condition_array
        if not UtilClient.is_unset(request.statis_behavior_condition_express):
            body['StatisBehaviorConditionExpress'] = request.statis_behavior_condition_express
        if not UtilClient.is_unset(request.statis_behavior_condition_type):
            body['StatisBehaviorConditionType'] = request.statis_behavior_condition_type
        if not UtilClient.is_unset(request.traffic_control_targets):
            body['TrafficControlTargets'] = request.traffic_control_targets
        if not UtilClient.is_unset(request.user_condition_array):
            body['UserConditionArray'] = request.user_condition_array
        if not UtilClient.is_unset(request.user_condition_express):
            body['UserConditionExpress'] = request.user_condition_express
        if not UtilClient.is_unset(request.user_condition_type):
            body['UserConditionType'] = request.user_condition_type
        if not UtilClient.is_unset(request.user_table_meta_id):
            body['UserTableMetaId'] = request.user_table_meta_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTrafficControlTask',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateTrafficControlTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_traffic_control_task_with_options_async(
        self,
        request: pai_rec_service_20221213_models.CreateTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.CreateTrafficControlTaskResponse:
        """
        @summary 创建流量调控任务
        
        @param request: CreateTrafficControlTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTrafficControlTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.behavior_table_meta_id):
            body['BehaviorTableMetaId'] = request.behavior_table_meta_id
        if not UtilClient.is_unset(request.control_granularity):
            body['ControlGranularity'] = request.control_granularity
        if not UtilClient.is_unset(request.control_logic):
            body['ControlLogic'] = request.control_logic
        if not UtilClient.is_unset(request.control_type):
            body['ControlType'] = request.control_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.execution_time):
            body['ExecutionTime'] = request.execution_time
        if not UtilClient.is_unset(request.flink_resource_id):
            body['FlinkResourceId'] = request.flink_resource_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.item_condition_array):
            body['ItemConditionArray'] = request.item_condition_array
        if not UtilClient.is_unset(request.item_condition_express):
            body['ItemConditionExpress'] = request.item_condition_express
        if not UtilClient.is_unset(request.item_condition_type):
            body['ItemConditionType'] = request.item_condition_type
        if not UtilClient.is_unset(request.item_table_meta_id):
            body['ItemTableMetaId'] = request.item_table_meta_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.pre_experiment_ids):
            body['PreExperimentIds'] = request.pre_experiment_ids
        if not UtilClient.is_unset(request.prod_experiment_ids):
            body['ProdExperimentIds'] = request.prod_experiment_ids
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.statis_behavior_condition_array):
            body['StatisBehaviorConditionArray'] = request.statis_behavior_condition_array
        if not UtilClient.is_unset(request.statis_behavior_condition_express):
            body['StatisBehaviorConditionExpress'] = request.statis_behavior_condition_express
        if not UtilClient.is_unset(request.statis_behavior_condition_type):
            body['StatisBehaviorConditionType'] = request.statis_behavior_condition_type
        if not UtilClient.is_unset(request.traffic_control_targets):
            body['TrafficControlTargets'] = request.traffic_control_targets
        if not UtilClient.is_unset(request.user_condition_array):
            body['UserConditionArray'] = request.user_condition_array
        if not UtilClient.is_unset(request.user_condition_express):
            body['UserConditionExpress'] = request.user_condition_express
        if not UtilClient.is_unset(request.user_condition_type):
            body['UserConditionType'] = request.user_condition_type
        if not UtilClient.is_unset(request.user_table_meta_id):
            body['UserTableMetaId'] = request.user_table_meta_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTrafficControlTask',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateTrafficControlTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_traffic_control_task(
        self,
        request: pai_rec_service_20221213_models.CreateTrafficControlTaskRequest,
    ) -> pai_rec_service_20221213_models.CreateTrafficControlTaskResponse:
        """
        @summary 创建流量调控任务
        
        @param request: CreateTrafficControlTaskRequest
        @return: CreateTrafficControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_traffic_control_task_with_options(request, headers, runtime)

    async def create_traffic_control_task_async(
        self,
        request: pai_rec_service_20221213_models.CreateTrafficControlTaskRequest,
    ) -> pai_rec_service_20221213_models.CreateTrafficControlTaskResponse:
        """
        @summary 创建流量调控任务
        
        @param request: CreateTrafficControlTaskRequest
        @return: CreateTrafficControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_traffic_control_task_with_options_async(request, headers, runtime)

    def debug_resource_rule_with_options(
        self,
        resource_rule_id: str,
        tmp_req: pai_rec_service_20221213_models.DebugResourceRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DebugResourceRuleResponse:
        """
        @summary 对指定资源规则中的计算公式进行调试
        
        @param tmp_req: DebugResourceRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DebugResourceRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_rec_service_20221213_models.DebugResourceRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.metric_info):
            request.metric_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.metric_info, 'MetricInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.metric_info_shrink):
            query['MetricInfo'] = request.metric_info_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DebugResourceRule',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/resourcerules/{OpenApiUtilClient.get_encode_param(resource_rule_id)}/action/debug',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DebugResourceRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def debug_resource_rule_with_options_async(
        self,
        resource_rule_id: str,
        tmp_req: pai_rec_service_20221213_models.DebugResourceRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DebugResourceRuleResponse:
        """
        @summary 对指定资源规则中的计算公式进行调试
        
        @param tmp_req: DebugResourceRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DebugResourceRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_rec_service_20221213_models.DebugResourceRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.metric_info):
            request.metric_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.metric_info, 'MetricInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.metric_info_shrink):
            query['MetricInfo'] = request.metric_info_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DebugResourceRule',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/resourcerules/{OpenApiUtilClient.get_encode_param(resource_rule_id)}/action/debug',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DebugResourceRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def debug_resource_rule(
        self,
        resource_rule_id: str,
        request: pai_rec_service_20221213_models.DebugResourceRuleRequest,
    ) -> pai_rec_service_20221213_models.DebugResourceRuleResponse:
        """
        @summary 对指定资源规则中的计算公式进行调试
        
        @param request: DebugResourceRuleRequest
        @return: DebugResourceRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.debug_resource_rule_with_options(resource_rule_id, request, headers, runtime)

    async def debug_resource_rule_async(
        self,
        resource_rule_id: str,
        request: pai_rec_service_20221213_models.DebugResourceRuleRequest,
    ) -> pai_rec_service_20221213_models.DebugResourceRuleResponse:
        """
        @summary 对指定资源规则中的计算公式进行调试
        
        @param request: DebugResourceRuleRequest
        @return: DebugResourceRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.debug_resource_rule_with_options_async(resource_rule_id, request, headers, runtime)

    def delete_abmetric_with_options(
        self,
        abmetric_id: str,
        request: pai_rec_service_20221213_models.DeleteABMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteABMetricResponse:
        """
        @summary 删除指定AB实验指标。
        
        @param request: DeleteABMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteABMetricResponse
        """
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
        """
        @summary 删除指定AB实验指标。
        
        @param request: DeleteABMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteABMetricResponse
        """
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
        """
        @summary 删除指定AB实验指标。
        
        @param request: DeleteABMetricRequest
        @return: DeleteABMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_abmetric_with_options(abmetric_id, request, headers, runtime)

    async def delete_abmetric_async(
        self,
        abmetric_id: str,
        request: pai_rec_service_20221213_models.DeleteABMetricRequest,
    ) -> pai_rec_service_20221213_models.DeleteABMetricResponse:
        """
        @summary 删除指定AB实验指标。
        
        @param request: DeleteABMetricRequest
        @return: DeleteABMetricResponse
        """
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
        """
        @summary 删除AB实验指标组。
        
        @param request: DeleteABMetricGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteABMetricGroupResponse
        """
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
        """
        @summary 删除AB实验指标组。
        
        @param request: DeleteABMetricGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteABMetricGroupResponse
        """
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
        """
        @summary 删除AB实验指标组。
        
        @param request: DeleteABMetricGroupRequest
        @return: DeleteABMetricGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_abmetric_group_with_options(abmetric_group_id, request, headers, runtime)

    async def delete_abmetric_group_async(
        self,
        abmetric_group_id: str,
        request: pai_rec_service_20221213_models.DeleteABMetricGroupRequest,
    ) -> pai_rec_service_20221213_models.DeleteABMetricGroupResponse:
        """
        @summary 删除AB实验指标组。
        
        @param request: DeleteABMetricGroupRequest
        @return: DeleteABMetricGroupResponse
        """
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
        """
        @summary 删除指定人群。
        
        @param request: DeleteCrowdRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCrowdResponse
        """
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
        """
        @summary 删除指定人群。
        
        @param request: DeleteCrowdRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCrowdResponse
        """
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
        """
        @summary 删除指定人群。
        
        @param request: DeleteCrowdRequest
        @return: DeleteCrowdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_crowd_with_options(crowd_id, request, headers, runtime)

    async def delete_crowd_async(
        self,
        crowd_id: str,
        request: pai_rec_service_20221213_models.DeleteCrowdRequest,
    ) -> pai_rec_service_20221213_models.DeleteCrowdResponse:
        """
        @summary 删除指定人群。
        
        @param request: DeleteCrowdRequest
        @return: DeleteCrowdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_crowd_with_options_async(crowd_id, request, headers, runtime)

    def delete_engine_config_with_options(
        self,
        engine_config_id: str,
        request: pai_rec_service_20221213_models.DeleteEngineConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteEngineConfigResponse:
        """
        @summary 删除指定推荐引擎配置。
        
        @param request: DeleteEngineConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEngineConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEngineConfig',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/engineconfigs/{OpenApiUtilClient.get_encode_param(engine_config_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteEngineConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_engine_config_with_options_async(
        self,
        engine_config_id: str,
        request: pai_rec_service_20221213_models.DeleteEngineConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteEngineConfigResponse:
        """
        @summary 删除指定推荐引擎配置。
        
        @param request: DeleteEngineConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEngineConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEngineConfig',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/engineconfigs/{OpenApiUtilClient.get_encode_param(engine_config_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteEngineConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_engine_config(
        self,
        engine_config_id: str,
        request: pai_rec_service_20221213_models.DeleteEngineConfigRequest,
    ) -> pai_rec_service_20221213_models.DeleteEngineConfigResponse:
        """
        @summary 删除指定推荐引擎配置。
        
        @param request: DeleteEngineConfigRequest
        @return: DeleteEngineConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_engine_config_with_options(engine_config_id, request, headers, runtime)

    async def delete_engine_config_async(
        self,
        engine_config_id: str,
        request: pai_rec_service_20221213_models.DeleteEngineConfigRequest,
    ) -> pai_rec_service_20221213_models.DeleteEngineConfigResponse:
        """
        @summary 删除指定推荐引擎配置。
        
        @param request: DeleteEngineConfigRequest
        @return: DeleteEngineConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_engine_config_with_options_async(engine_config_id, request, headers, runtime)

    def delete_experiment_with_options(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.DeleteExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteExperimentResponse:
        """
        @summary 删除实验。
        
        @param request: DeleteExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExperimentResponse
        """
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
        """
        @summary 删除实验。
        
        @param request: DeleteExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExperimentResponse
        """
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
        """
        @summary 删除实验。
        
        @param request: DeleteExperimentRequest
        @return: DeleteExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_experiment_with_options(experiment_id, request, headers, runtime)

    async def delete_experiment_async(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.DeleteExperimentRequest,
    ) -> pai_rec_service_20221213_models.DeleteExperimentResponse:
        """
        @summary 删除实验。
        
        @param request: DeleteExperimentRequest
        @return: DeleteExperimentResponse
        """
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
        """
        @summary 删除指定实验组。
        
        @param request: DeleteExperimentGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExperimentGroupResponse
        """
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
        """
        @summary 删除指定实验组。
        
        @param request: DeleteExperimentGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExperimentGroupResponse
        """
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
        """
        @summary 删除指定实验组。
        
        @param request: DeleteExperimentGroupRequest
        @return: DeleteExperimentGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_experiment_group_with_options(experiment_group_id, request, headers, runtime)

    async def delete_experiment_group_async(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.DeleteExperimentGroupRequest,
    ) -> pai_rec_service_20221213_models.DeleteExperimentGroupResponse:
        """
        @summary 删除指定实验组。
        
        @param request: DeleteExperimentGroupRequest
        @return: DeleteExperimentGroupResponse
        """
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
        """
        @summary 删除指定实例下的指定配置资源。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResourceResponse
        """
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
        """
        @summary 删除指定实例下的指定配置资源。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResourceResponse
        """
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
        """
        @summary 删除指定实例下的指定配置资源。
        
        @return: DeleteInstanceResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_resource_with_options(instance_id, resource_id, headers, runtime)

    async def delete_instance_resource_async(
        self,
        instance_id: str,
        resource_id: str,
    ) -> pai_rec_service_20221213_models.DeleteInstanceResourceResponse:
        """
        @summary 删除指定实例下的指定配置资源。
        
        @return: DeleteInstanceResourceResponse
        """
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
        """
        @summary 删除实验室。
        
        @param request: DeleteLaboratoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLaboratoryResponse
        """
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
        """
        @summary 删除实验室。
        
        @param request: DeleteLaboratoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLaboratoryResponse
        """
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
        """
        @summary 删除实验室。
        
        @param request: DeleteLaboratoryRequest
        @return: DeleteLaboratoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_laboratory_with_options(laboratory_id, request, headers, runtime)

    async def delete_laboratory_async(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.DeleteLaboratoryRequest,
    ) -> pai_rec_service_20221213_models.DeleteLaboratoryResponse:
        """
        @summary 删除实验室。
        
        @param request: DeleteLaboratoryRequest
        @return: DeleteLaboratoryResponse
        """
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
        """
        @summary 删除层。
        
        @param request: DeleteLayerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLayerResponse
        """
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
        """
        @summary 删除层。
        
        @param request: DeleteLayerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLayerResponse
        """
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
        """
        @summary 删除层。
        
        @param request: DeleteLayerRequest
        @return: DeleteLayerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_layer_with_options(layer_id, request, headers, runtime)

    async def delete_layer_async(
        self,
        layer_id: str,
        request: pai_rec_service_20221213_models.DeleteLayerRequest,
    ) -> pai_rec_service_20221213_models.DeleteLayerResponse:
        """
        @summary 删除层。
        
        @param request: DeleteLayerRequest
        @return: DeleteLayerResponse
        """
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
        """
        @summary 删除指定参数。
        
        @param request: DeleteParamRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteParamResponse
        """
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
        """
        @summary 删除指定参数。
        
        @param request: DeleteParamRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteParamResponse
        """
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
        """
        @summary 删除指定参数。
        
        @param request: DeleteParamRequest
        @return: DeleteParamResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_param_with_options(param_id, request, headers, runtime)

    async def delete_param_async(
        self,
        param_id: str,
        request: pai_rec_service_20221213_models.DeleteParamRequest,
    ) -> pai_rec_service_20221213_models.DeleteParamResponse:
        """
        @summary 删除指定参数。
        
        @param request: DeleteParamRequest
        @return: DeleteParamResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_param_with_options_async(param_id, request, headers, runtime)

    def delete_resource_rule_with_options(
        self,
        resource_rule_id: str,
        request: pai_rec_service_20221213_models.DeleteResourceRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteResourceRuleResponse:
        """
        @summary 删除资源规则
        
        @param request: DeleteResourceRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResourceRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResourceRule',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/resourcerules/{OpenApiUtilClient.get_encode_param(resource_rule_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteResourceRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_rule_with_options_async(
        self,
        resource_rule_id: str,
        request: pai_rec_service_20221213_models.DeleteResourceRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteResourceRuleResponse:
        """
        @summary 删除资源规则
        
        @param request: DeleteResourceRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResourceRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResourceRule',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/resourcerules/{OpenApiUtilClient.get_encode_param(resource_rule_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteResourceRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_rule(
        self,
        resource_rule_id: str,
        request: pai_rec_service_20221213_models.DeleteResourceRuleRequest,
    ) -> pai_rec_service_20221213_models.DeleteResourceRuleResponse:
        """
        @summary 删除资源规则
        
        @param request: DeleteResourceRuleRequest
        @return: DeleteResourceRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_rule_with_options(resource_rule_id, request, headers, runtime)

    async def delete_resource_rule_async(
        self,
        resource_rule_id: str,
        request: pai_rec_service_20221213_models.DeleteResourceRuleRequest,
    ) -> pai_rec_service_20221213_models.DeleteResourceRuleResponse:
        """
        @summary 删除资源规则
        
        @param request: DeleteResourceRuleRequest
        @return: DeleteResourceRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_resource_rule_with_options_async(resource_rule_id, request, headers, runtime)

    def delete_resource_rule_item_with_options(
        self,
        resource_rule_id: str,
        resource_rule_item_id: str,
        request: pai_rec_service_20221213_models.DeleteResourceRuleItemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteResourceRuleItemResponse:
        """
        @summary 删除资源规则条目
        
        @param request: DeleteResourceRuleItemRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResourceRuleItemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResourceRuleItem',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/resourcerules/{OpenApiUtilClient.get_encode_param(resource_rule_id)}/items/{OpenApiUtilClient.get_encode_param(resource_rule_item_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteResourceRuleItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_rule_item_with_options_async(
        self,
        resource_rule_id: str,
        resource_rule_item_id: str,
        request: pai_rec_service_20221213_models.DeleteResourceRuleItemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteResourceRuleItemResponse:
        """
        @summary 删除资源规则条目
        
        @param request: DeleteResourceRuleItemRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResourceRuleItemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResourceRuleItem',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/resourcerules/{OpenApiUtilClient.get_encode_param(resource_rule_id)}/items/{OpenApiUtilClient.get_encode_param(resource_rule_item_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteResourceRuleItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_rule_item(
        self,
        resource_rule_id: str,
        resource_rule_item_id: str,
        request: pai_rec_service_20221213_models.DeleteResourceRuleItemRequest,
    ) -> pai_rec_service_20221213_models.DeleteResourceRuleItemResponse:
        """
        @summary 删除资源规则条目
        
        @param request: DeleteResourceRuleItemRequest
        @return: DeleteResourceRuleItemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_rule_item_with_options(resource_rule_id, resource_rule_item_id, request, headers, runtime)

    async def delete_resource_rule_item_async(
        self,
        resource_rule_id: str,
        resource_rule_item_id: str,
        request: pai_rec_service_20221213_models.DeleteResourceRuleItemRequest,
    ) -> pai_rec_service_20221213_models.DeleteResourceRuleItemResponse:
        """
        @summary 删除资源规则条目
        
        @param request: DeleteResourceRuleItemRequest
        @return: DeleteResourceRuleItemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_resource_rule_item_with_options_async(resource_rule_id, resource_rule_item_id, request, headers, runtime)

    def delete_sample_consistency_job_with_options(
        self,
        sample_consistency_job_id: str,
        request: pai_rec_service_20221213_models.DeleteSampleConsistencyJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteSampleConsistencyJobResponse:
        """
        @summary 删除指定的样本一致性任务
        
        @param request: DeleteSampleConsistencyJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSampleConsistencyJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSampleConsistencyJob',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/sampleconsistencyjobs/{OpenApiUtilClient.get_encode_param(sample_consistency_job_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteSampleConsistencyJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sample_consistency_job_with_options_async(
        self,
        sample_consistency_job_id: str,
        request: pai_rec_service_20221213_models.DeleteSampleConsistencyJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteSampleConsistencyJobResponse:
        """
        @summary 删除指定的样本一致性任务
        
        @param request: DeleteSampleConsistencyJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSampleConsistencyJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSampleConsistencyJob',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/sampleconsistencyjobs/{OpenApiUtilClient.get_encode_param(sample_consistency_job_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteSampleConsistencyJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sample_consistency_job(
        self,
        sample_consistency_job_id: str,
        request: pai_rec_service_20221213_models.DeleteSampleConsistencyJobRequest,
    ) -> pai_rec_service_20221213_models.DeleteSampleConsistencyJobResponse:
        """
        @summary 删除指定的样本一致性任务
        
        @param request: DeleteSampleConsistencyJobRequest
        @return: DeleteSampleConsistencyJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_sample_consistency_job_with_options(sample_consistency_job_id, request, headers, runtime)

    async def delete_sample_consistency_job_async(
        self,
        sample_consistency_job_id: str,
        request: pai_rec_service_20221213_models.DeleteSampleConsistencyJobRequest,
    ) -> pai_rec_service_20221213_models.DeleteSampleConsistencyJobResponse:
        """
        @summary 删除指定的样本一致性任务
        
        @param request: DeleteSampleConsistencyJobRequest
        @return: DeleteSampleConsistencyJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_sample_consistency_job_with_options_async(sample_consistency_job_id, request, headers, runtime)

    def delete_scene_with_options(
        self,
        scene_id: str,
        request: pai_rec_service_20221213_models.DeleteSceneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteSceneResponse:
        """
        @summary 删除场景
        
        @param request: DeleteSceneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSceneResponse
        """
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
        """
        @summary 删除场景
        
        @param request: DeleteSceneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSceneResponse
        """
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
        """
        @summary 删除场景
        
        @param request: DeleteSceneRequest
        @return: DeleteSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_scene_with_options(scene_id, request, headers, runtime)

    async def delete_scene_async(
        self,
        scene_id: str,
        request: pai_rec_service_20221213_models.DeleteSceneRequest,
    ) -> pai_rec_service_20221213_models.DeleteSceneResponse:
        """
        @summary 删除场景
        
        @param request: DeleteSceneRequest
        @return: DeleteSceneResponse
        """
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
        """
        @summary 删除指定人群下的指定子人群。
        
        @param request: DeleteSubCrowdRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSubCrowdResponse
        """
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
        """
        @summary 删除指定人群下的指定子人群。
        
        @param request: DeleteSubCrowdRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSubCrowdResponse
        """
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
        """
        @summary 删除指定人群下的指定子人群。
        
        @param request: DeleteSubCrowdRequest
        @return: DeleteSubCrowdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_sub_crowd_with_options(crowd_id, sub_crowd_id, request, headers, runtime)

    async def delete_sub_crowd_async(
        self,
        crowd_id: str,
        sub_crowd_id: str,
        request: pai_rec_service_20221213_models.DeleteSubCrowdRequest,
    ) -> pai_rec_service_20221213_models.DeleteSubCrowdResponse:
        """
        @summary 删除指定人群下的指定子人群。
        
        @param request: DeleteSubCrowdRequest
        @return: DeleteSubCrowdResponse
        """
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
        """
        @summary 删除数据表。
        
        @param request: DeleteTableMetaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTableMetaResponse
        """
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
        """
        @summary 删除数据表。
        
        @param request: DeleteTableMetaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTableMetaResponse
        """
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
        """
        @summary 删除数据表。
        
        @param request: DeleteTableMetaRequest
        @return: DeleteTableMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_table_meta_with_options(table_meta_id, request, headers, runtime)

    async def delete_table_meta_async(
        self,
        table_meta_id: str,
        request: pai_rec_service_20221213_models.DeleteTableMetaRequest,
    ) -> pai_rec_service_20221213_models.DeleteTableMetaResponse:
        """
        @summary 删除数据表。
        
        @param request: DeleteTableMetaRequest
        @return: DeleteTableMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_table_meta_with_options_async(table_meta_id, request, headers, runtime)

    def delete_traffic_control_target_with_options(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.DeleteTrafficControlTargetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteTrafficControlTargetResponse:
        """
        @summary 更新流量调控目标
        
        @param request: DeleteTrafficControlTargetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTrafficControlTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTrafficControlTarget',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltargets/{OpenApiUtilClient.get_encode_param(traffic_control_target_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteTrafficControlTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_traffic_control_target_with_options_async(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.DeleteTrafficControlTargetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteTrafficControlTargetResponse:
        """
        @summary 更新流量调控目标
        
        @param request: DeleteTrafficControlTargetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTrafficControlTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTrafficControlTarget',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltargets/{OpenApiUtilClient.get_encode_param(traffic_control_target_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteTrafficControlTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_traffic_control_target(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.DeleteTrafficControlTargetRequest,
    ) -> pai_rec_service_20221213_models.DeleteTrafficControlTargetResponse:
        """
        @summary 更新流量调控目标
        
        @param request: DeleteTrafficControlTargetRequest
        @return: DeleteTrafficControlTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_traffic_control_target_with_options(traffic_control_target_id, request, headers, runtime)

    async def delete_traffic_control_target_async(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.DeleteTrafficControlTargetRequest,
    ) -> pai_rec_service_20221213_models.DeleteTrafficControlTargetResponse:
        """
        @summary 更新流量调控目标
        
        @param request: DeleteTrafficControlTargetRequest
        @return: DeleteTrafficControlTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_traffic_control_target_with_options_async(traffic_control_target_id, request, headers, runtime)

    def delete_traffic_control_task_with_options(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.DeleteTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteTrafficControlTaskResponse:
        """
        @summary 删除指定的流量调控任务
        
        @param request: DeleteTrafficControlTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTrafficControlTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTrafficControlTask',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltasks/{OpenApiUtilClient.get_encode_param(traffic_control_task_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteTrafficControlTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_traffic_control_task_with_options_async(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.DeleteTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.DeleteTrafficControlTaskResponse:
        """
        @summary 删除指定的流量调控任务
        
        @param request: DeleteTrafficControlTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTrafficControlTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTrafficControlTask',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltasks/{OpenApiUtilClient.get_encode_param(traffic_control_task_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteTrafficControlTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_traffic_control_task(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.DeleteTrafficControlTaskRequest,
    ) -> pai_rec_service_20221213_models.DeleteTrafficControlTaskResponse:
        """
        @summary 删除指定的流量调控任务
        
        @param request: DeleteTrafficControlTaskRequest
        @return: DeleteTrafficControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_traffic_control_task_with_options(traffic_control_task_id, request, headers, runtime)

    async def delete_traffic_control_task_async(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.DeleteTrafficControlTaskRequest,
    ) -> pai_rec_service_20221213_models.DeleteTrafficControlTaskResponse:
        """
        @summary 删除指定的流量调控任务
        
        @param request: DeleteTrafficControlTaskRequest
        @return: DeleteTrafficControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_traffic_control_task_with_options_async(traffic_control_task_id, request, headers, runtime)

    def generate_traffic_control_task_code_with_options(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.GenerateTrafficControlTaskCodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GenerateTrafficControlTaskCodeResponse:
        """
        @summary 产生流量调控的相关代码
        
        @param request: GenerateTrafficControlTaskCodeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateTrafficControlTaskCodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateTrafficControlTaskCode',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltasks/{OpenApiUtilClient.get_encode_param(traffic_control_task_id)}/action/generatecode',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GenerateTrafficControlTaskCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_traffic_control_task_code_with_options_async(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.GenerateTrafficControlTaskCodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GenerateTrafficControlTaskCodeResponse:
        """
        @summary 产生流量调控的相关代码
        
        @param request: GenerateTrafficControlTaskCodeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateTrafficControlTaskCodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateTrafficControlTaskCode',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltasks/{OpenApiUtilClient.get_encode_param(traffic_control_task_id)}/action/generatecode',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GenerateTrafficControlTaskCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_traffic_control_task_code(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.GenerateTrafficControlTaskCodeRequest,
    ) -> pai_rec_service_20221213_models.GenerateTrafficControlTaskCodeResponse:
        """
        @summary 产生流量调控的相关代码
        
        @param request: GenerateTrafficControlTaskCodeRequest
        @return: GenerateTrafficControlTaskCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_traffic_control_task_code_with_options(traffic_control_task_id, request, headers, runtime)

    async def generate_traffic_control_task_code_async(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.GenerateTrafficControlTaskCodeRequest,
    ) -> pai_rec_service_20221213_models.GenerateTrafficControlTaskCodeResponse:
        """
        @summary 产生流量调控的相关代码
        
        @param request: GenerateTrafficControlTaskCodeRequest
        @return: GenerateTrafficControlTaskCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.generate_traffic_control_task_code_with_options_async(traffic_control_task_id, request, headers, runtime)

    def generate_traffic_control_task_config_with_options(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.GenerateTrafficControlTaskConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GenerateTrafficControlTaskConfigResponse:
        """
        @summary 产生流量调控的相关召回配置
        
        @param request: GenerateTrafficControlTaskConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateTrafficControlTaskConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateTrafficControlTaskConfig',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltasks/{OpenApiUtilClient.get_encode_param(traffic_control_task_id)}/action/generateconfig',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GenerateTrafficControlTaskConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_traffic_control_task_config_with_options_async(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.GenerateTrafficControlTaskConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GenerateTrafficControlTaskConfigResponse:
        """
        @summary 产生流量调控的相关召回配置
        
        @param request: GenerateTrafficControlTaskConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateTrafficControlTaskConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateTrafficControlTaskConfig',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltasks/{OpenApiUtilClient.get_encode_param(traffic_control_task_id)}/action/generateconfig',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GenerateTrafficControlTaskConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_traffic_control_task_config(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.GenerateTrafficControlTaskConfigRequest,
    ) -> pai_rec_service_20221213_models.GenerateTrafficControlTaskConfigResponse:
        """
        @summary 产生流量调控的相关召回配置
        
        @param request: GenerateTrafficControlTaskConfigRequest
        @return: GenerateTrafficControlTaskConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_traffic_control_task_config_with_options(traffic_control_task_id, request, headers, runtime)

    async def generate_traffic_control_task_config_async(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.GenerateTrafficControlTaskConfigRequest,
    ) -> pai_rec_service_20221213_models.GenerateTrafficControlTaskConfigResponse:
        """
        @summary 产生流量调控的相关召回配置
        
        @param request: GenerateTrafficControlTaskConfigRequest
        @return: GenerateTrafficControlTaskConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.generate_traffic_control_task_config_with_options_async(traffic_control_task_id, request, headers, runtime)

    def get_abmetric_with_options(
        self,
        abmetric_id: str,
        request: pai_rec_service_20221213_models.GetABMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetABMetricResponse:
        """
        @summary 获取AB Test实验指标详细信息。
        
        @param request: GetABMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetABMetricResponse
        """
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
        """
        @summary 获取AB Test实验指标详细信息。
        
        @param request: GetABMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetABMetricResponse
        """
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
        """
        @summary 获取AB Test实验指标详细信息。
        
        @param request: GetABMetricRequest
        @return: GetABMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_abmetric_with_options(abmetric_id, request, headers, runtime)

    async def get_abmetric_async(
        self,
        abmetric_id: str,
        request: pai_rec_service_20221213_models.GetABMetricRequest,
    ) -> pai_rec_service_20221213_models.GetABMetricResponse:
        """
        @summary 获取AB Test实验指标详细信息。
        
        @param request: GetABMetricRequest
        @return: GetABMetricResponse
        """
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
        """
        @summary 获取AB实验指标组详细信息。
        
        @param request: GetABMetricGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetABMetricGroupResponse
        """
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
        """
        @summary 获取AB实验指标组详细信息。
        
        @param request: GetABMetricGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetABMetricGroupResponse
        """
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
        """
        @summary 获取AB实验指标组详细信息。
        
        @param request: GetABMetricGroupRequest
        @return: GetABMetricGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_abmetric_group_with_options(abmetric_group_id, request, headers, runtime)

    async def get_abmetric_group_async(
        self,
        abmetric_group_id: str,
        request: pai_rec_service_20221213_models.GetABMetricGroupRequest,
    ) -> pai_rec_service_20221213_models.GetABMetricGroupResponse:
        """
        @summary 获取AB实验指标组详细信息。
        
        @param request: GetABMetricGroupRequest
        @return: GetABMetricGroupResponse
        """
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
        """
        @summary 获取指定计算任务详细信息。
        
        @param request: GetCalculationJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCalculationJobResponse
        """
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
        """
        @summary 获取指定计算任务详细信息。
        
        @param request: GetCalculationJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCalculationJobResponse
        """
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
        """
        @summary 获取指定计算任务详细信息。
        
        @param request: GetCalculationJobRequest
        @return: GetCalculationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_calculation_job_with_options(calculation_job_id, request, headers, runtime)

    async def get_calculation_job_async(
        self,
        calculation_job_id: str,
        request: pai_rec_service_20221213_models.GetCalculationJobRequest,
    ) -> pai_rec_service_20221213_models.GetCalculationJobResponse:
        """
        @summary 获取指定计算任务详细信息。
        
        @param request: GetCalculationJobRequest
        @return: GetCalculationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_calculation_job_with_options_async(calculation_job_id, request, headers, runtime)

    def get_engine_config_with_options(
        self,
        engine_config_id: str,
        request: pai_rec_service_20221213_models.GetEngineConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetEngineConfigResponse:
        """
        @summary 获取引擎配置详细信息。
        
        @param request: GetEngineConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEngineConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEngineConfig',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/engineconfigs/{OpenApiUtilClient.get_encode_param(engine_config_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetEngineConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_engine_config_with_options_async(
        self,
        engine_config_id: str,
        request: pai_rec_service_20221213_models.GetEngineConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetEngineConfigResponse:
        """
        @summary 获取引擎配置详细信息。
        
        @param request: GetEngineConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEngineConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEngineConfig',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/engineconfigs/{OpenApiUtilClient.get_encode_param(engine_config_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetEngineConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_engine_config(
        self,
        engine_config_id: str,
        request: pai_rec_service_20221213_models.GetEngineConfigRequest,
    ) -> pai_rec_service_20221213_models.GetEngineConfigResponse:
        """
        @summary 获取引擎配置详细信息。
        
        @param request: GetEngineConfigRequest
        @return: GetEngineConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_engine_config_with_options(engine_config_id, request, headers, runtime)

    async def get_engine_config_async(
        self,
        engine_config_id: str,
        request: pai_rec_service_20221213_models.GetEngineConfigRequest,
    ) -> pai_rec_service_20221213_models.GetEngineConfigResponse:
        """
        @summary 获取引擎配置详细信息。
        
        @param request: GetEngineConfigRequest
        @return: GetEngineConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_engine_config_with_options_async(engine_config_id, request, headers, runtime)

    def get_experiment_with_options(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.GetExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetExperimentResponse:
        """
        @summary 获取实验详细信息。
        
        @param request: GetExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExperimentResponse
        """
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
        """
        @summary 获取实验详细信息。
        
        @param request: GetExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExperimentResponse
        """
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
        """
        @summary 获取实验详细信息。
        
        @param request: GetExperimentRequest
        @return: GetExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_experiment_with_options(experiment_id, request, headers, runtime)

    async def get_experiment_async(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.GetExperimentRequest,
    ) -> pai_rec_service_20221213_models.GetExperimentResponse:
        """
        @summary 获取实验详细信息。
        
        @param request: GetExperimentRequest
        @return: GetExperimentResponse
        """
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
        """
        @summary 获取指定实验组详细信息。
        
        @param request: GetExperimentGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExperimentGroupResponse
        """
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
        """
        @summary 获取指定实验组详细信息。
        
        @param request: GetExperimentGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExperimentGroupResponse
        """
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
        """
        @summary 获取指定实验组详细信息。
        
        @param request: GetExperimentGroupRequest
        @return: GetExperimentGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_experiment_group_with_options(experiment_group_id, request, headers, runtime)

    async def get_experiment_group_async(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.GetExperimentGroupRequest,
    ) -> pai_rec_service_20221213_models.GetExperimentGroupResponse:
        """
        @summary 获取指定实验组详细信息。
        
        @param request: GetExperimentGroupRequest
        @return: GetExperimentGroupResponse
        """
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
        """
        @summary 获取特征一致性检查任务详细信息。
        
        @param request: GetFeatureConsistencyCheckJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFeatureConsistencyCheckJobResponse
        """
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
        """
        @summary 获取特征一致性检查任务详细信息。
        
        @param request: GetFeatureConsistencyCheckJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFeatureConsistencyCheckJobResponse
        """
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
        """
        @summary 获取特征一致性检查任务详细信息。
        
        @param request: GetFeatureConsistencyCheckJobRequest
        @return: GetFeatureConsistencyCheckJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_feature_consistency_check_job_with_options(feature_consistency_check_job_id, request, headers, runtime)

    async def get_feature_consistency_check_job_async(
        self,
        feature_consistency_check_job_id: str,
        request: pai_rec_service_20221213_models.GetFeatureConsistencyCheckJobRequest,
    ) -> pai_rec_service_20221213_models.GetFeatureConsistencyCheckJobResponse:
        """
        @summary 获取特征一致性检查任务详细信息。
        
        @param request: GetFeatureConsistencyCheckJobRequest
        @return: GetFeatureConsistencyCheckJobResponse
        """
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
        """
        @summary 获取特征一致性检测配置详情。
        
        @param request: GetFeatureConsistencyCheckJobConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFeatureConsistencyCheckJobConfigResponse
        """
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
        """
        @summary 获取特征一致性检测配置详情。
        
        @param request: GetFeatureConsistencyCheckJobConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFeatureConsistencyCheckJobConfigResponse
        """
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
        """
        @summary 获取特征一致性检测配置详情。
        
        @param request: GetFeatureConsistencyCheckJobConfigRequest
        @return: GetFeatureConsistencyCheckJobConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_feature_consistency_check_job_config_with_options(feature_consistency_check_job_config_id, request, headers, runtime)

    async def get_feature_consistency_check_job_config_async(
        self,
        feature_consistency_check_job_config_id: str,
        request: pai_rec_service_20221213_models.GetFeatureConsistencyCheckJobConfigRequest,
    ) -> pai_rec_service_20221213_models.GetFeatureConsistencyCheckJobConfigResponse:
        """
        @summary 获取特征一致性检测配置详情。
        
        @param request: GetFeatureConsistencyCheckJobConfigRequest
        @return: GetFeatureConsistencyCheckJobConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_feature_consistency_check_job_config_with_options_async(feature_consistency_check_job_config_id, request, headers, runtime)

    def get_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetInstanceResponse:
        """
        @summary 获取指定推荐全链路深度定制开发平台实例信息。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceResponse
        """
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
        """
        @summary 获取指定推荐全链路深度定制开发平台实例信息。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceResponse
        """
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
        """
        @summary 获取指定推荐全链路深度定制开发平台实例信息。
        
        @return: GetInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(instance_id, headers, runtime)

    async def get_instance_async(
        self,
        instance_id: str,
    ) -> pai_rec_service_20221213_models.GetInstanceResponse:
        """
        @summary 获取指定推荐全链路深度定制开发平台实例信息。
        
        @return: GetInstanceResponse
        """
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
        """
        @summary 获取指定实例下指定资源的详细信息。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceResourceResponse
        """
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
        """
        @summary 获取指定实例下指定资源的详细信息。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceResourceResponse
        """
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
        """
        @summary 获取指定实例下指定资源的详细信息。
        
        @return: GetInstanceResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_resource_with_options(instance_id, resource_id, headers, runtime)

    async def get_instance_resource_async(
        self,
        instance_id: str,
        resource_id: str,
    ) -> pai_rec_service_20221213_models.GetInstanceResourceResponse:
        """
        @summary 获取指定实例下指定资源的详细信息。
        
        @return: GetInstanceResourceResponse
        """
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
        """
        @summary 获取数据源下指定表的详细信息。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceResourceTableResponse
        """
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
        """
        @summary 获取数据源下指定表的详细信息。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceResourceTableResponse
        """
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
        """
        @summary 获取数据源下指定表的详细信息。
        
        @return: GetInstanceResourceTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_resource_table_with_options(instance_id, resource_id, table_name, headers, runtime)

    async def get_instance_resource_table_async(
        self,
        instance_id: str,
        resource_id: str,
        table_name: str,
    ) -> pai_rec_service_20221213_models.GetInstanceResourceTableResponse:
        """
        @summary 获取数据源下指定表的详细信息。
        
        @return: GetInstanceResourceTableResponse
        """
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
        """
        @summary 获取实验室详细信息。
        
        @param request: GetLaboratoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLaboratoryResponse
        """
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
        """
        @summary 获取实验室详细信息。
        
        @param request: GetLaboratoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLaboratoryResponse
        """
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
        """
        @summary 获取实验室详细信息。
        
        @param request: GetLaboratoryRequest
        @return: GetLaboratoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_laboratory_with_options(laboratory_id, request, headers, runtime)

    async def get_laboratory_async(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.GetLaboratoryRequest,
    ) -> pai_rec_service_20221213_models.GetLaboratoryResponse:
        """
        @summary 获取实验室详细信息。
        
        @param request: GetLaboratoryRequest
        @return: GetLaboratoryResponse
        """
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
        """
        @summary 获取层详细信息。
        
        @param request: GetLayerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLayerResponse
        """
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
        """
        @summary 获取层详细信息。
        
        @param request: GetLayerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLayerResponse
        """
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
        """
        @summary 获取层详细信息。
        
        @param request: GetLayerRequest
        @return: GetLayerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_layer_with_options(layer_id, request, headers, runtime)

    async def get_layer_async(
        self,
        layer_id: str,
        request: pai_rec_service_20221213_models.GetLayerRequest,
    ) -> pai_rec_service_20221213_models.GetLayerResponse:
        """
        @summary 获取层详细信息。
        
        @param request: GetLayerRequest
        @return: GetLayerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_layer_with_options_async(layer_id, request, headers, runtime)

    def get_resource_rule_with_options(
        self,
        resource_rule_id: str,
        request: pai_rec_service_20221213_models.GetResourceRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetResourceRuleResponse:
        """
        @summary 获取资源规则详细信息
        
        @param request: GetResourceRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceRule',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/resourcerules/{OpenApiUtilClient.get_encode_param(resource_rule_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetResourceRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_rule_with_options_async(
        self,
        resource_rule_id: str,
        request: pai_rec_service_20221213_models.GetResourceRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetResourceRuleResponse:
        """
        @summary 获取资源规则详细信息
        
        @param request: GetResourceRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceRule',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/resourcerules/{OpenApiUtilClient.get_encode_param(resource_rule_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetResourceRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_rule(
        self,
        resource_rule_id: str,
        request: pai_rec_service_20221213_models.GetResourceRuleRequest,
    ) -> pai_rec_service_20221213_models.GetResourceRuleResponse:
        """
        @summary 获取资源规则详细信息
        
        @param request: GetResourceRuleRequest
        @return: GetResourceRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resource_rule_with_options(resource_rule_id, request, headers, runtime)

    async def get_resource_rule_async(
        self,
        resource_rule_id: str,
        request: pai_rec_service_20221213_models.GetResourceRuleRequest,
    ) -> pai_rec_service_20221213_models.GetResourceRuleResponse:
        """
        @summary 获取资源规则详细信息
        
        @param request: GetResourceRuleRequest
        @return: GetResourceRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_resource_rule_with_options_async(resource_rule_id, request, headers, runtime)

    def get_sample_consistency_job_with_options(
        self,
        sample_consistency_job_id: str,
        request: pai_rec_service_20221213_models.GetSampleConsistencyJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetSampleConsistencyJobResponse:
        """
        @summary 获取样本一致性任务详细信息
        
        @param request: GetSampleConsistencyJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSampleConsistencyJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSampleConsistencyJob',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/sampleconsistencyjobs/{OpenApiUtilClient.get_encode_param(sample_consistency_job_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetSampleConsistencyJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sample_consistency_job_with_options_async(
        self,
        sample_consistency_job_id: str,
        request: pai_rec_service_20221213_models.GetSampleConsistencyJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetSampleConsistencyJobResponse:
        """
        @summary 获取样本一致性任务详细信息
        
        @param request: GetSampleConsistencyJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSampleConsistencyJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSampleConsistencyJob',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/sampleconsistencyjobs/{OpenApiUtilClient.get_encode_param(sample_consistency_job_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetSampleConsistencyJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sample_consistency_job(
        self,
        sample_consistency_job_id: str,
        request: pai_rec_service_20221213_models.GetSampleConsistencyJobRequest,
    ) -> pai_rec_service_20221213_models.GetSampleConsistencyJobResponse:
        """
        @summary 获取样本一致性任务详细信息
        
        @param request: GetSampleConsistencyJobRequest
        @return: GetSampleConsistencyJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_sample_consistency_job_with_options(sample_consistency_job_id, request, headers, runtime)

    async def get_sample_consistency_job_async(
        self,
        sample_consistency_job_id: str,
        request: pai_rec_service_20221213_models.GetSampleConsistencyJobRequest,
    ) -> pai_rec_service_20221213_models.GetSampleConsistencyJobResponse:
        """
        @summary 获取样本一致性任务详细信息
        
        @param request: GetSampleConsistencyJobRequest
        @return: GetSampleConsistencyJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_sample_consistency_job_with_options_async(sample_consistency_job_id, request, headers, runtime)

    def get_scene_with_options(
        self,
        scene_id: str,
        request: pai_rec_service_20221213_models.GetSceneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetSceneResponse:
        """
        @summary 获取场景详细信息
        
        @param request: GetSceneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSceneResponse
        """
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
        """
        @summary 获取场景详细信息
        
        @param request: GetSceneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSceneResponse
        """
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
        """
        @summary 获取场景详细信息
        
        @param request: GetSceneRequest
        @return: GetSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_scene_with_options(scene_id, request, headers, runtime)

    async def get_scene_async(
        self,
        scene_id: str,
        request: pai_rec_service_20221213_models.GetSceneRequest,
    ) -> pai_rec_service_20221213_models.GetSceneResponse:
        """
        @summary 获取场景详细信息
        
        @param request: GetSceneRequest
        @return: GetSceneResponse
        """
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
        """
        @summary 获取指定人群下的指定子人群的详细信息。
        
        @param request: GetSubCrowdRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSubCrowdResponse
        """
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
        """
        @summary 获取指定人群下的指定子人群的详细信息。
        
        @param request: GetSubCrowdRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSubCrowdResponse
        """
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
        """
        @summary 获取指定人群下的指定子人群的详细信息。
        
        @param request: GetSubCrowdRequest
        @return: GetSubCrowdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_sub_crowd_with_options(crowd_id, sub_crowd_id, request, headers, runtime)

    async def get_sub_crowd_async(
        self,
        crowd_id: str,
        sub_crowd_id: str,
        request: pai_rec_service_20221213_models.GetSubCrowdRequest,
    ) -> pai_rec_service_20221213_models.GetSubCrowdResponse:
        """
        @summary 获取指定人群下的指定子人群的详细信息。
        
        @param request: GetSubCrowdRequest
        @return: GetSubCrowdResponse
        """
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
        """
        @summary 获取数据表详细信息。
        
        @param request: GetTableMetaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTableMetaResponse
        """
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
        """
        @summary 获取数据表详细信息。
        
        @param request: GetTableMetaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTableMetaResponse
        """
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
        """
        @summary 获取数据表详细信息。
        
        @param request: GetTableMetaRequest
        @return: GetTableMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_table_meta_with_options(table_meta_id, request, headers, runtime)

    async def get_table_meta_async(
        self,
        table_meta_id: str,
        request: pai_rec_service_20221213_models.GetTableMetaRequest,
    ) -> pai_rec_service_20221213_models.GetTableMetaResponse:
        """
        @summary 获取数据表详细信息。
        
        @param request: GetTableMetaRequest
        @return: GetTableMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_table_meta_with_options_async(table_meta_id, request, headers, runtime)

    def get_traffic_control_target_with_options(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.GetTrafficControlTargetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetTrafficControlTargetResponse:
        """
        @summary 获取流量调控目标详情
        
        @param request: GetTrafficControlTargetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTrafficControlTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrafficControlTarget',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltargets/{OpenApiUtilClient.get_encode_param(traffic_control_target_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetTrafficControlTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_traffic_control_target_with_options_async(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.GetTrafficControlTargetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetTrafficControlTargetResponse:
        """
        @summary 获取流量调控目标详情
        
        @param request: GetTrafficControlTargetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTrafficControlTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrafficControlTarget',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltargets/{OpenApiUtilClient.get_encode_param(traffic_control_target_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetTrafficControlTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_traffic_control_target(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.GetTrafficControlTargetRequest,
    ) -> pai_rec_service_20221213_models.GetTrafficControlTargetResponse:
        """
        @summary 获取流量调控目标详情
        
        @param request: GetTrafficControlTargetRequest
        @return: GetTrafficControlTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_traffic_control_target_with_options(traffic_control_target_id, request, headers, runtime)

    async def get_traffic_control_target_async(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.GetTrafficControlTargetRequest,
    ) -> pai_rec_service_20221213_models.GetTrafficControlTargetResponse:
        """
        @summary 获取流量调控目标详情
        
        @param request: GetTrafficControlTargetRequest
        @return: GetTrafficControlTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_traffic_control_target_with_options_async(traffic_control_target_id, request, headers, runtime)

    def get_traffic_control_task_with_options(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.GetTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetTrafficControlTaskResponse:
        """
        @summary 获取流量调控任务详情
        
        @param request: GetTrafficControlTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTrafficControlTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.control_target_filter):
            query['ControlTargetFilter'] = request.control_target_filter
        if not UtilClient.is_unset(request.environment):
            query['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.version):
            query['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrafficControlTask',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltasks/{OpenApiUtilClient.get_encode_param(traffic_control_task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetTrafficControlTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_traffic_control_task_with_options_async(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.GetTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetTrafficControlTaskResponse:
        """
        @summary 获取流量调控任务详情
        
        @param request: GetTrafficControlTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTrafficControlTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.control_target_filter):
            query['ControlTargetFilter'] = request.control_target_filter
        if not UtilClient.is_unset(request.environment):
            query['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.version):
            query['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrafficControlTask',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltasks/{OpenApiUtilClient.get_encode_param(traffic_control_task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetTrafficControlTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_traffic_control_task(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.GetTrafficControlTaskRequest,
    ) -> pai_rec_service_20221213_models.GetTrafficControlTaskResponse:
        """
        @summary 获取流量调控任务详情
        
        @param request: GetTrafficControlTaskRequest
        @return: GetTrafficControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_traffic_control_task_with_options(traffic_control_task_id, request, headers, runtime)

    async def get_traffic_control_task_async(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.GetTrafficControlTaskRequest,
    ) -> pai_rec_service_20221213_models.GetTrafficControlTaskResponse:
        """
        @summary 获取流量调控任务详情
        
        @param request: GetTrafficControlTaskRequest
        @return: GetTrafficControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_traffic_control_task_with_options_async(traffic_control_task_id, request, headers, runtime)

    def get_traffic_control_task_traffic_with_options(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.GetTrafficControlTaskTrafficRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetTrafficControlTaskTrafficResponse:
        """
        @summary 获取流量调控任务的流量详情
        
        @param request: GetTrafficControlTaskTrafficRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTrafficControlTaskTrafficResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment):
            query['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrafficControlTaskTraffic',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltasks/{OpenApiUtilClient.get_encode_param(traffic_control_task_id)}/trafficinfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetTrafficControlTaskTrafficResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_traffic_control_task_traffic_with_options_async(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.GetTrafficControlTaskTrafficRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.GetTrafficControlTaskTrafficResponse:
        """
        @summary 获取流量调控任务的流量详情
        
        @param request: GetTrafficControlTaskTrafficRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTrafficControlTaskTrafficResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment):
            query['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrafficControlTaskTraffic',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltasks/{OpenApiUtilClient.get_encode_param(traffic_control_task_id)}/trafficinfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetTrafficControlTaskTrafficResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_traffic_control_task_traffic(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.GetTrafficControlTaskTrafficRequest,
    ) -> pai_rec_service_20221213_models.GetTrafficControlTaskTrafficResponse:
        """
        @summary 获取流量调控任务的流量详情
        
        @param request: GetTrafficControlTaskTrafficRequest
        @return: GetTrafficControlTaskTrafficResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_traffic_control_task_traffic_with_options(traffic_control_task_id, request, headers, runtime)

    async def get_traffic_control_task_traffic_async(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.GetTrafficControlTaskTrafficRequest,
    ) -> pai_rec_service_20221213_models.GetTrafficControlTaskTrafficResponse:
        """
        @summary 获取流量调控任务的流量详情
        
        @param request: GetTrafficControlTaskTrafficRequest
        @return: GetTrafficControlTaskTrafficResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_traffic_control_task_traffic_with_options_async(traffic_control_task_id, request, headers, runtime)

    def list_abmetric_groups_with_options(
        self,
        request: pai_rec_service_20221213_models.ListABMetricGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListABMetricGroupsResponse:
        """
        @summary 获取AB Test实验指标组列表。
        
        @param request: ListABMetricGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListABMetricGroupsResponse
        """
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
        """
        @summary 获取AB Test实验指标组列表。
        
        @param request: ListABMetricGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListABMetricGroupsResponse
        """
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
        """
        @summary 获取AB Test实验指标组列表。
        
        @param request: ListABMetricGroupsRequest
        @return: ListABMetricGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_abmetric_groups_with_options(request, headers, runtime)

    async def list_abmetric_groups_async(
        self,
        request: pai_rec_service_20221213_models.ListABMetricGroupsRequest,
    ) -> pai_rec_service_20221213_models.ListABMetricGroupsResponse:
        """
        @summary 获取AB Test实验指标组列表。
        
        @param request: ListABMetricGroupsRequest
        @return: ListABMetricGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_abmetric_groups_with_options_async(request, headers, runtime)

    def list_abmetrics_with_options(
        self,
        request: pai_rec_service_20221213_models.ListABMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListABMetricsResponse:
        """
        @summary 获取AB Test实验指标列表。
        
        @param request: ListABMetricsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListABMetricsResponse
        """
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
        """
        @summary 获取AB Test实验指标列表。
        
        @param request: ListABMetricsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListABMetricsResponse
        """
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
        """
        @summary 获取AB Test实验指标列表。
        
        @param request: ListABMetricsRequest
        @return: ListABMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_abmetrics_with_options(request, headers, runtime)

    async def list_abmetrics_async(
        self,
        request: pai_rec_service_20221213_models.ListABMetricsRequest,
    ) -> pai_rec_service_20221213_models.ListABMetricsResponse:
        """
        @summary 获取AB Test实验指标列表。
        
        @param request: ListABMetricsRequest
        @return: ListABMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_abmetrics_with_options_async(request, headers, runtime)

    def list_calculation_jobs_with_options(
        self,
        request: pai_rec_service_20221213_models.ListCalculationJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListCalculationJobsResponse:
        """
        @summary 获取计算任务列表。
        
        @param request: ListCalculationJobsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCalculationJobsResponse
        """
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
        """
        @summary 获取计算任务列表。
        
        @param request: ListCalculationJobsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCalculationJobsResponse
        """
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
        """
        @summary 获取计算任务列表。
        
        @param request: ListCalculationJobsRequest
        @return: ListCalculationJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_calculation_jobs_with_options(request, headers, runtime)

    async def list_calculation_jobs_async(
        self,
        request: pai_rec_service_20221213_models.ListCalculationJobsRequest,
    ) -> pai_rec_service_20221213_models.ListCalculationJobsResponse:
        """
        @summary 获取计算任务列表。
        
        @param request: ListCalculationJobsRequest
        @return: ListCalculationJobsResponse
        """
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
        """
        @summary 获取人群下的所有用户。
        
        @param request: ListCrowdUsersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCrowdUsersResponse
        """
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
        """
        @summary 获取人群下的所有用户。
        
        @param request: ListCrowdUsersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCrowdUsersResponse
        """
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
        """
        @summary 获取人群下的所有用户。
        
        @param request: ListCrowdUsersRequest
        @return: ListCrowdUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_crowd_users_with_options(crowd_id, request, headers, runtime)

    async def list_crowd_users_async(
        self,
        crowd_id: str,
        request: pai_rec_service_20221213_models.ListCrowdUsersRequest,
    ) -> pai_rec_service_20221213_models.ListCrowdUsersResponse:
        """
        @summary 获取人群下的所有用户。
        
        @param request: ListCrowdUsersRequest
        @return: ListCrowdUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_crowd_users_with_options_async(crowd_id, request, headers, runtime)

    def list_crowds_with_options(
        self,
        request: pai_rec_service_20221213_models.ListCrowdsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListCrowdsResponse:
        """
        @summary 获取人群列表。
        
        @param request: ListCrowdsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCrowdsResponse
        """
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
        """
        @summary 获取人群列表。
        
        @param request: ListCrowdsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCrowdsResponse
        """
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
        """
        @summary 获取人群列表。
        
        @param request: ListCrowdsRequest
        @return: ListCrowdsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_crowds_with_options(request, headers, runtime)

    async def list_crowds_async(
        self,
        request: pai_rec_service_20221213_models.ListCrowdsRequest,
    ) -> pai_rec_service_20221213_models.ListCrowdsResponse:
        """
        @summary 获取人群列表。
        
        @param request: ListCrowdsRequest
        @return: ListCrowdsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_crowds_with_options_async(request, headers, runtime)

    def list_engine_configs_with_options(
        self,
        request: pai_rec_service_20221213_models.ListEngineConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListEngineConfigsResponse:
        """
        @summary 获取引擎配置列表。
        
        @param request: ListEngineConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEngineConfigsResponse
        """
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.version):
            query['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEngineConfigs',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/engineconfigs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListEngineConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_engine_configs_with_options_async(
        self,
        request: pai_rec_service_20221213_models.ListEngineConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListEngineConfigsResponse:
        """
        @summary 获取引擎配置列表。
        
        @param request: ListEngineConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEngineConfigsResponse
        """
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.version):
            query['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEngineConfigs',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/engineconfigs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListEngineConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_engine_configs(
        self,
        request: pai_rec_service_20221213_models.ListEngineConfigsRequest,
    ) -> pai_rec_service_20221213_models.ListEngineConfigsResponse:
        """
        @summary 获取引擎配置列表。
        
        @param request: ListEngineConfigsRequest
        @return: ListEngineConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_engine_configs_with_options(request, headers, runtime)

    async def list_engine_configs_async(
        self,
        request: pai_rec_service_20221213_models.ListEngineConfigsRequest,
    ) -> pai_rec_service_20221213_models.ListEngineConfigsResponse:
        """
        @summary 获取引擎配置列表。
        
        @param request: ListEngineConfigsRequest
        @return: ListEngineConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_engine_configs_with_options_async(request, headers, runtime)

    def list_experiment_groups_with_options(
        self,
        request: pai_rec_service_20221213_models.ListExperimentGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListExperimentGroupsResponse:
        """
        @summary 获取实验组列表。
        
        @param request: ListExperimentGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExperimentGroupsResponse
        """
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
        if not UtilClient.is_unset(request.time_range_end):
            query['TimeRangeEnd'] = request.time_range_end
        if not UtilClient.is_unset(request.time_range_start):
            query['TimeRangeStart'] = request.time_range_start
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
        """
        @summary 获取实验组列表。
        
        @param request: ListExperimentGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExperimentGroupsResponse
        """
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
        if not UtilClient.is_unset(request.time_range_end):
            query['TimeRangeEnd'] = request.time_range_end
        if not UtilClient.is_unset(request.time_range_start):
            query['TimeRangeStart'] = request.time_range_start
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
        """
        @summary 获取实验组列表。
        
        @param request: ListExperimentGroupsRequest
        @return: ListExperimentGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_experiment_groups_with_options(request, headers, runtime)

    async def list_experiment_groups_async(
        self,
        request: pai_rec_service_20221213_models.ListExperimentGroupsRequest,
    ) -> pai_rec_service_20221213_models.ListExperimentGroupsResponse:
        """
        @summary 获取实验组列表。
        
        @param request: ListExperimentGroupsRequest
        @return: ListExperimentGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_experiment_groups_with_options_async(request, headers, runtime)

    def list_experiments_with_options(
        self,
        request: pai_rec_service_20221213_models.ListExperimentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListExperimentsResponse:
        """
        @summary 获取实验列表。
        
        @param request: ListExperimentsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExperimentsResponse
        """
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
        """
        @summary 获取实验列表。
        
        @param request: ListExperimentsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExperimentsResponse
        """
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
        """
        @summary 获取实验列表。
        
        @param request: ListExperimentsRequest
        @return: ListExperimentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_experiments_with_options(request, headers, runtime)

    async def list_experiments_async(
        self,
        request: pai_rec_service_20221213_models.ListExperimentsRequest,
    ) -> pai_rec_service_20221213_models.ListExperimentsResponse:
        """
        @summary 获取实验列表。
        
        @param request: ListExperimentsRequest
        @return: ListExperimentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_experiments_with_options_async(request, headers, runtime)

    def list_feature_consistency_check_job_configs_with_options(
        self,
        request: pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobConfigsResponse:
        """
        @summary 获取特征一致性检查配置列表。
        
        @param request: ListFeatureConsistencyCheckJobConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFeatureConsistencyCheckJobConfigsResponse
        """
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
        """
        @summary 获取特征一致性检查配置列表。
        
        @param request: ListFeatureConsistencyCheckJobConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFeatureConsistencyCheckJobConfigsResponse
        """
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
        """
        @summary 获取特征一致性检查配置列表。
        
        @param request: ListFeatureConsistencyCheckJobConfigsRequest
        @return: ListFeatureConsistencyCheckJobConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_feature_consistency_check_job_configs_with_options(request, headers, runtime)

    async def list_feature_consistency_check_job_configs_async(
        self,
        request: pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobConfigsRequest,
    ) -> pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobConfigsResponse:
        """
        @summary 获取特征一致性检查配置列表。
        
        @param request: ListFeatureConsistencyCheckJobConfigsRequest
        @return: ListFeatureConsistencyCheckJobConfigsResponse
        """
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
        """
        @summary 获取特征一致性检查任务的特征报表/比对结果。
        
        @param request: ListFeatureConsistencyCheckJobFeatureReportsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFeatureConsistencyCheckJobFeatureReportsResponse
        """
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
        """
        @summary 获取特征一致性检查任务的特征报表/比对结果。
        
        @param request: ListFeatureConsistencyCheckJobFeatureReportsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFeatureConsistencyCheckJobFeatureReportsResponse
        """
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
        """
        @summary 获取特征一致性检查任务的特征报表/比对结果。
        
        @param request: ListFeatureConsistencyCheckJobFeatureReportsRequest
        @return: ListFeatureConsistencyCheckJobFeatureReportsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_feature_consistency_check_job_feature_reports_with_options(feature_consistency_check_job_id, request, headers, runtime)

    async def list_feature_consistency_check_job_feature_reports_async(
        self,
        feature_consistency_check_job_id: str,
        request: pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobFeatureReportsRequest,
    ) -> pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobFeatureReportsResponse:
        """
        @summary 获取特征一致性检查任务的特征报表/比对结果。
        
        @param request: ListFeatureConsistencyCheckJobFeatureReportsRequest
        @return: ListFeatureConsistencyCheckJobFeatureReportsResponse
        """
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
        """
        @summary 获取特征一致性检查任务分数报表/比对结果。
        
        @param tmp_req: ListFeatureConsistencyCheckJobScoreReportsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFeatureConsistencyCheckJobScoreReportsResponse
        """
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
        """
        @summary 获取特征一致性检查任务分数报表/比对结果。
        
        @param tmp_req: ListFeatureConsistencyCheckJobScoreReportsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFeatureConsistencyCheckJobScoreReportsResponse
        """
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
        """
        @summary 获取特征一致性检查任务分数报表/比对结果。
        
        @param request: ListFeatureConsistencyCheckJobScoreReportsRequest
        @return: ListFeatureConsistencyCheckJobScoreReportsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_feature_consistency_check_job_score_reports_with_options(feature_consistency_check_job_id, request, headers, runtime)

    async def list_feature_consistency_check_job_score_reports_async(
        self,
        feature_consistency_check_job_id: str,
        request: pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobScoreReportsRequest,
    ) -> pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobScoreReportsResponse:
        """
        @summary 获取特征一致性检查任务分数报表/比对结果。
        
        @param request: ListFeatureConsistencyCheckJobScoreReportsRequest
        @return: ListFeatureConsistencyCheckJobScoreReportsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_feature_consistency_check_job_score_reports_with_options_async(feature_consistency_check_job_id, request, headers, runtime)

    def list_feature_consistency_check_jobs_with_options(
        self,
        request: pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobsResponse:
        """
        @summary 获取特征一致性检查任务列表。
        
        @param request: ListFeatureConsistencyCheckJobsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFeatureConsistencyCheckJobsResponse
        """
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
        """
        @summary 获取特征一致性检查任务列表。
        
        @param request: ListFeatureConsistencyCheckJobsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFeatureConsistencyCheckJobsResponse
        """
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
        """
        @summary 获取特征一致性检查任务列表。
        
        @param request: ListFeatureConsistencyCheckJobsRequest
        @return: ListFeatureConsistencyCheckJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_feature_consistency_check_jobs_with_options(request, headers, runtime)

    async def list_feature_consistency_check_jobs_async(
        self,
        request: pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobsRequest,
    ) -> pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobsResponse:
        """
        @summary 获取特征一致性检查任务列表。
        
        @param request: ListFeatureConsistencyCheckJobsRequest
        @return: ListFeatureConsistencyCheckJobsResponse
        """
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
        """
        @summary 获取实例下配置的资源列表。
        
        @param request: ListInstanceResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceResourcesResponse
        """
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
        """
        @summary 获取实例下配置的资源列表。
        
        @param request: ListInstanceResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceResourcesResponse
        """
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
        """
        @summary 获取实例下配置的资源列表。
        
        @param request: ListInstanceResourcesRequest
        @return: ListInstanceResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_resources_with_options(instance_id, request, headers, runtime)

    async def list_instance_resources_async(
        self,
        instance_id: str,
        request: pai_rec_service_20221213_models.ListInstanceResourcesRequest,
    ) -> pai_rec_service_20221213_models.ListInstanceResourcesResponse:
        """
        @summary 获取实例下配置的资源列表。
        
        @param request: ListInstanceResourcesRequest
        @return: ListInstanceResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instance_resources_with_options_async(instance_id, request, headers, runtime)

    def list_instances_with_options(
        self,
        request: pai_rec_service_20221213_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListInstancesResponse:
        """
        @summary 获取推荐全链路深度定制开发平台实例信息列表。
        
        @param request: ListInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
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
        """
        @summary 获取推荐全链路深度定制开发平台实例信息列表。
        
        @param request: ListInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
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
        """
        @summary 获取推荐全链路深度定制开发平台实例信息列表。
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    async def list_instances_async(
        self,
        request: pai_rec_service_20221213_models.ListInstancesRequest,
    ) -> pai_rec_service_20221213_models.ListInstancesResponse:
        """
        @summary 获取推荐全链路深度定制开发平台实例信息列表。
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instances_with_options_async(request, headers, runtime)

    def list_laboratories_with_options(
        self,
        request: pai_rec_service_20221213_models.ListLaboratoriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListLaboratoriesResponse:
        """
        @summary 获取实验室列表。
        
        @param request: ListLaboratoriesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLaboratoriesResponse
        """
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
        """
        @summary 获取实验室列表。
        
        @param request: ListLaboratoriesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLaboratoriesResponse
        """
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
        """
        @summary 获取实验室列表。
        
        @param request: ListLaboratoriesRequest
        @return: ListLaboratoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_laboratories_with_options(request, headers, runtime)

    async def list_laboratories_async(
        self,
        request: pai_rec_service_20221213_models.ListLaboratoriesRequest,
    ) -> pai_rec_service_20221213_models.ListLaboratoriesResponse:
        """
        @summary 获取实验室列表。
        
        @param request: ListLaboratoriesRequest
        @return: ListLaboratoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_laboratories_with_options_async(request, headers, runtime)

    def list_layers_with_options(
        self,
        request: pai_rec_service_20221213_models.ListLayersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListLayersResponse:
        """
        @summary 获取层列表。
        
        @param request: ListLayersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLayersResponse
        """
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
        """
        @summary 获取层列表。
        
        @param request: ListLayersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLayersResponse
        """
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
        """
        @summary 获取层列表。
        
        @param request: ListLayersRequest
        @return: ListLayersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_layers_with_options(request, headers, runtime)

    async def list_layers_async(
        self,
        request: pai_rec_service_20221213_models.ListLayersRequest,
    ) -> pai_rec_service_20221213_models.ListLayersResponse:
        """
        @summary 获取层列表。
        
        @param request: ListLayersRequest
        @return: ListLayersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_layers_with_options_async(request, headers, runtime)

    def list_params_with_options(
        self,
        request: pai_rec_service_20221213_models.ListParamsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListParamsResponse:
        """
        @summary 获取参数列表。
        
        @param request: ListParamsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListParamsResponse
        """
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
        """
        @summary 获取参数列表。
        
        @param request: ListParamsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListParamsResponse
        """
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
        """
        @summary 获取参数列表。
        
        @param request: ListParamsRequest
        @return: ListParamsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_params_with_options(request, headers, runtime)

    async def list_params_async(
        self,
        request: pai_rec_service_20221213_models.ListParamsRequest,
    ) -> pai_rec_service_20221213_models.ListParamsResponse:
        """
        @summary 获取参数列表。
        
        @param request: ListParamsRequest
        @return: ListParamsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_params_with_options_async(request, headers, runtime)

    def list_resource_rules_with_options(
        self,
        request: pai_rec_service_20221213_models.ListResourceRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListResourceRulesResponse:
        """
        @summary 获取资源规则列表
        
        @param request: ListResourceRulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_rule_id):
            query['ResourceRuleId'] = request.resource_rule_id
        if not UtilClient.is_unset(request.resource_rule_name):
            query['ResourceRuleName'] = request.resource_rule_name
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceRules',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/resourcerules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListResourceRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_rules_with_options_async(
        self,
        request: pai_rec_service_20221213_models.ListResourceRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListResourceRulesResponse:
        """
        @summary 获取资源规则列表
        
        @param request: ListResourceRulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_rule_id):
            query['ResourceRuleId'] = request.resource_rule_id
        if not UtilClient.is_unset(request.resource_rule_name):
            query['ResourceRuleName'] = request.resource_rule_name
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceRules',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/resourcerules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListResourceRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_rules(
        self,
        request: pai_rec_service_20221213_models.ListResourceRulesRequest,
    ) -> pai_rec_service_20221213_models.ListResourceRulesResponse:
        """
        @summary 获取资源规则列表
        
        @param request: ListResourceRulesRequest
        @return: ListResourceRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_rules_with_options(request, headers, runtime)

    async def list_resource_rules_async(
        self,
        request: pai_rec_service_20221213_models.ListResourceRulesRequest,
    ) -> pai_rec_service_20221213_models.ListResourceRulesResponse:
        """
        @summary 获取资源规则列表
        
        @param request: ListResourceRulesRequest
        @return: ListResourceRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resource_rules_with_options_async(request, headers, runtime)

    def list_sample_consistency_jobs_with_options(
        self,
        request: pai_rec_service_20221213_models.ListSampleConsistencyJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListSampleConsistencyJobsResponse:
        """
        @summary 获取样本一致性任务列表
        
        @param request: ListSampleConsistencyJobsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSampleConsistencyJobsResponse
        """
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
            action='ListSampleConsistencyJobs',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/sampleconsistencyjobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListSampleConsistencyJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sample_consistency_jobs_with_options_async(
        self,
        request: pai_rec_service_20221213_models.ListSampleConsistencyJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListSampleConsistencyJobsResponse:
        """
        @summary 获取样本一致性任务列表
        
        @param request: ListSampleConsistencyJobsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSampleConsistencyJobsResponse
        """
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
            action='ListSampleConsistencyJobs',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/sampleconsistencyjobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListSampleConsistencyJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sample_consistency_jobs(
        self,
        request: pai_rec_service_20221213_models.ListSampleConsistencyJobsRequest,
    ) -> pai_rec_service_20221213_models.ListSampleConsistencyJobsResponse:
        """
        @summary 获取样本一致性任务列表
        
        @param request: ListSampleConsistencyJobsRequest
        @return: ListSampleConsistencyJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_sample_consistency_jobs_with_options(request, headers, runtime)

    async def list_sample_consistency_jobs_async(
        self,
        request: pai_rec_service_20221213_models.ListSampleConsistencyJobsRequest,
    ) -> pai_rec_service_20221213_models.ListSampleConsistencyJobsResponse:
        """
        @summary 获取样本一致性任务列表
        
        @param request: ListSampleConsistencyJobsRequest
        @return: ListSampleConsistencyJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_sample_consistency_jobs_with_options_async(request, headers, runtime)

    def list_scenes_with_options(
        self,
        request: pai_rec_service_20221213_models.ListScenesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListScenesResponse:
        """
        @summary 获取场景列表
        
        @param request: ListScenesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScenesResponse
        """
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
        """
        @summary 获取场景列表
        
        @param request: ListScenesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScenesResponse
        """
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
        """
        @summary 获取场景列表
        
        @param request: ListScenesRequest
        @return: ListScenesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_scenes_with_options(request, headers, runtime)

    async def list_scenes_async(
        self,
        request: pai_rec_service_20221213_models.ListScenesRequest,
    ) -> pai_rec_service_20221213_models.ListScenesResponse:
        """
        @summary 获取场景列表
        
        @param request: ListScenesRequest
        @return: ListScenesResponse
        """
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
        """
        @summary 获取人群下的所有子人群。
        
        @param request: ListSubCrowdsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSubCrowdsResponse
        """
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
        """
        @summary 获取人群下的所有子人群。
        
        @param request: ListSubCrowdsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSubCrowdsResponse
        """
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
        """
        @summary 获取人群下的所有子人群。
        
        @param request: ListSubCrowdsRequest
        @return: ListSubCrowdsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_sub_crowds_with_options(crowd_id, request, headers, runtime)

    async def list_sub_crowds_async(
        self,
        crowd_id: str,
        request: pai_rec_service_20221213_models.ListSubCrowdsRequest,
    ) -> pai_rec_service_20221213_models.ListSubCrowdsResponse:
        """
        @summary 获取人群下的所有子人群。
        
        @param request: ListSubCrowdsRequest
        @return: ListSubCrowdsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_sub_crowds_with_options_async(crowd_id, request, headers, runtime)

    def list_table_metas_with_options(
        self,
        request: pai_rec_service_20221213_models.ListTableMetasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListTableMetasResponse:
        """
        @summary 获取数据表列表。
        
        @param request: ListTableMetasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTableMetasResponse
        """
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
        """
        @summary 获取数据表列表。
        
        @param request: ListTableMetasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTableMetasResponse
        """
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
        """
        @summary 获取数据表列表。
        
        @param request: ListTableMetasRequest
        @return: ListTableMetasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_table_metas_with_options(request, headers, runtime)

    async def list_table_metas_async(
        self,
        request: pai_rec_service_20221213_models.ListTableMetasRequest,
    ) -> pai_rec_service_20221213_models.ListTableMetasResponse:
        """
        @summary 获取数据表列表。
        
        @param request: ListTableMetasRequest
        @return: ListTableMetasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_table_metas_with_options_async(request, headers, runtime)

    def list_traffic_control_target_traffic_history_with_options(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.ListTrafficControlTargetTrafficHistoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListTrafficControlTargetTrafficHistoryResponse:
        """
        @summary 获取流量调控任务流量变更的历史列表
        
        @param request: ListTrafficControlTargetTrafficHistoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTrafficControlTargetTrafficHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.environment):
            query['Environment'] = request.environment
        if not UtilClient.is_unset(request.experiment_group_id):
            query['ExperimentGroupId'] = request.experiment_group_id
        if not UtilClient.is_unset(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTrafficControlTargetTrafficHistory',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltargets/{OpenApiUtilClient.get_encode_param(traffic_control_target_id)}/traffichistories',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListTrafficControlTargetTrafficHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_traffic_control_target_traffic_history_with_options_async(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.ListTrafficControlTargetTrafficHistoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListTrafficControlTargetTrafficHistoryResponse:
        """
        @summary 获取流量调控任务流量变更的历史列表
        
        @param request: ListTrafficControlTargetTrafficHistoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTrafficControlTargetTrafficHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.environment):
            query['Environment'] = request.environment
        if not UtilClient.is_unset(request.experiment_group_id):
            query['ExperimentGroupId'] = request.experiment_group_id
        if not UtilClient.is_unset(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTrafficControlTargetTrafficHistory',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltargets/{OpenApiUtilClient.get_encode_param(traffic_control_target_id)}/traffichistories',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListTrafficControlTargetTrafficHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_traffic_control_target_traffic_history(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.ListTrafficControlTargetTrafficHistoryRequest,
    ) -> pai_rec_service_20221213_models.ListTrafficControlTargetTrafficHistoryResponse:
        """
        @summary 获取流量调控任务流量变更的历史列表
        
        @param request: ListTrafficControlTargetTrafficHistoryRequest
        @return: ListTrafficControlTargetTrafficHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_traffic_control_target_traffic_history_with_options(traffic_control_target_id, request, headers, runtime)

    async def list_traffic_control_target_traffic_history_async(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.ListTrafficControlTargetTrafficHistoryRequest,
    ) -> pai_rec_service_20221213_models.ListTrafficControlTargetTrafficHistoryResponse:
        """
        @summary 获取流量调控任务流量变更的历史列表
        
        @param request: ListTrafficControlTargetTrafficHistoryRequest
        @return: ListTrafficControlTargetTrafficHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_traffic_control_target_traffic_history_with_options_async(traffic_control_target_id, request, headers, runtime)

    def list_traffic_control_tasks_with_options(
        self,
        request: pai_rec_service_20221213_models.ListTrafficControlTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListTrafficControlTasksResponse:
        """
        @summary 获取流量调控列表
        
        @param request: ListTrafficControlTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTrafficControlTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.control_target_filter):
            query['ControlTargetFilter'] = request.control_target_filter
        if not UtilClient.is_unset(request.environment):
            query['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.traffic_control_task_id):
            query['TrafficControlTaskId'] = request.traffic_control_task_id
        if not UtilClient.is_unset(request.version):
            query['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTrafficControlTasks',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListTrafficControlTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_traffic_control_tasks_with_options_async(
        self,
        request: pai_rec_service_20221213_models.ListTrafficControlTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ListTrafficControlTasksResponse:
        """
        @summary 获取流量调控列表
        
        @param request: ListTrafficControlTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTrafficControlTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.control_target_filter):
            query['ControlTargetFilter'] = request.control_target_filter
        if not UtilClient.is_unset(request.environment):
            query['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.traffic_control_task_id):
            query['TrafficControlTaskId'] = request.traffic_control_task_id
        if not UtilClient.is_unset(request.version):
            query['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTrafficControlTasks',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListTrafficControlTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_traffic_control_tasks(
        self,
        request: pai_rec_service_20221213_models.ListTrafficControlTasksRequest,
    ) -> pai_rec_service_20221213_models.ListTrafficControlTasksResponse:
        """
        @summary 获取流量调控列表
        
        @param request: ListTrafficControlTasksRequest
        @return: ListTrafficControlTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_traffic_control_tasks_with_options(request, headers, runtime)

    async def list_traffic_control_tasks_async(
        self,
        request: pai_rec_service_20221213_models.ListTrafficControlTasksRequest,
    ) -> pai_rec_service_20221213_models.ListTrafficControlTasksResponse:
        """
        @summary 获取流量调控列表
        
        @param request: ListTrafficControlTasksRequest
        @return: ListTrafficControlTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_traffic_control_tasks_with_options_async(request, headers, runtime)

    def offline_experiment_with_options(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.OfflineExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.OfflineExperimentResponse:
        """
        @summary 上线实验。
        
        @param request: OfflineExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OfflineExperimentResponse
        """
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
        """
        @summary 上线实验。
        
        @param request: OfflineExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OfflineExperimentResponse
        """
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
        """
        @summary 上线实验。
        
        @param request: OfflineExperimentRequest
        @return: OfflineExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.offline_experiment_with_options(experiment_id, request, headers, runtime)

    async def offline_experiment_async(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.OfflineExperimentRequest,
    ) -> pai_rec_service_20221213_models.OfflineExperimentResponse:
        """
        @summary 上线实验。
        
        @param request: OfflineExperimentRequest
        @return: OfflineExperimentResponse
        """
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
        """
        @summary 下线实验组。
        
        @param request: OfflineExperimentGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OfflineExperimentGroupResponse
        """
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
        """
        @summary 下线实验组。
        
        @param request: OfflineExperimentGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OfflineExperimentGroupResponse
        """
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
        """
        @summary 下线实验组。
        
        @param request: OfflineExperimentGroupRequest
        @return: OfflineExperimentGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.offline_experiment_group_with_options(experiment_group_id, request, headers, runtime)

    async def offline_experiment_group_async(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.OfflineExperimentGroupRequest,
    ) -> pai_rec_service_20221213_models.OfflineExperimentGroupResponse:
        """
        @summary 下线实验组。
        
        @param request: OfflineExperimentGroupRequest
        @return: OfflineExperimentGroupResponse
        """
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
        """
        @summary 下线实验室。
        
        @param request: OfflineLaboratoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OfflineLaboratoryResponse
        """
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
        """
        @summary 下线实验室。
        
        @param request: OfflineLaboratoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OfflineLaboratoryResponse
        """
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
        """
        @summary 下线实验室。
        
        @param request: OfflineLaboratoryRequest
        @return: OfflineLaboratoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.offline_laboratory_with_options(laboratory_id, request, headers, runtime)

    async def offline_laboratory_async(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.OfflineLaboratoryRequest,
    ) -> pai_rec_service_20221213_models.OfflineLaboratoryResponse:
        """
        @summary 下线实验室。
        
        @param request: OfflineLaboratoryRequest
        @return: OfflineLaboratoryResponse
        """
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
        """
        @summary 上线实验
        
        @param request: OnlineExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnlineExperimentResponse
        """
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
        """
        @summary 上线实验
        
        @param request: OnlineExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnlineExperimentResponse
        """
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
        """
        @summary 上线实验
        
        @param request: OnlineExperimentRequest
        @return: OnlineExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.online_experiment_with_options(experiment_id, request, headers, runtime)

    async def online_experiment_async(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.OnlineExperimentRequest,
    ) -> pai_rec_service_20221213_models.OnlineExperimentResponse:
        """
        @summary 上线实验
        
        @param request: OnlineExperimentRequest
        @return: OnlineExperimentResponse
        """
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
        """
        @summary 上线实验组。
        
        @param request: OnlineExperimentGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnlineExperimentGroupResponse
        """
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
        """
        @summary 上线实验组。
        
        @param request: OnlineExperimentGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnlineExperimentGroupResponse
        """
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
        """
        @summary 上线实验组。
        
        @param request: OnlineExperimentGroupRequest
        @return: OnlineExperimentGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.online_experiment_group_with_options(experiment_group_id, request, headers, runtime)

    async def online_experiment_group_async(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.OnlineExperimentGroupRequest,
    ) -> pai_rec_service_20221213_models.OnlineExperimentGroupResponse:
        """
        @summary 上线实验组。
        
        @param request: OnlineExperimentGroupRequest
        @return: OnlineExperimentGroupResponse
        """
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
        """
        @summary 上线实验室。
        
        @param request: OnlineLaboratoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnlineLaboratoryResponse
        """
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
        """
        @summary 上线实验室。
        
        @param request: OnlineLaboratoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnlineLaboratoryResponse
        """
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
        """
        @summary 上线实验室。
        
        @param request: OnlineLaboratoryRequest
        @return: OnlineLaboratoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.online_laboratory_with_options(laboratory_id, request, headers, runtime)

    async def online_laboratory_async(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.OnlineLaboratoryRequest,
    ) -> pai_rec_service_20221213_models.OnlineLaboratoryResponse:
        """
        @summary 上线实验室。
        
        @param request: OnlineLaboratoryRequest
        @return: OnlineLaboratoryResponse
        """
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
        """
        @summary 推全。
        
        @param request: PushAllExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushAllExperimentResponse
        """
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
        """
        @summary 推全。
        
        @param request: PushAllExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushAllExperimentResponse
        """
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
        """
        @summary 推全。
        
        @param request: PushAllExperimentRequest
        @return: PushAllExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_all_experiment_with_options(experiment_id, request, headers, runtime)

    async def push_all_experiment_async(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.PushAllExperimentRequest,
    ) -> pai_rec_service_20221213_models.PushAllExperimentResponse:
        """
        @summary 推全。
        
        @param request: PushAllExperimentRequest
        @return: PushAllExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.push_all_experiment_with_options_async(experiment_id, request, headers, runtime)

    def push_resource_rule_with_options(
        self,
        resource_rule_id: str,
        tmp_req: pai_rec_service_20221213_models.PushResourceRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.PushResourceRuleResponse:
        """
        @summary 推送指标到指定资源规则
        
        @param tmp_req: PushResourceRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushResourceRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_rec_service_20221213_models.PushResourceRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.metric_info):
            request.metric_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.metric_info, 'MetricInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.metric_info_shrink):
            query['MetricInfo'] = request.metric_info_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushResourceRule',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/resourcerules/{OpenApiUtilClient.get_encode_param(resource_rule_id)}/action/push',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.PushResourceRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_resource_rule_with_options_async(
        self,
        resource_rule_id: str,
        tmp_req: pai_rec_service_20221213_models.PushResourceRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.PushResourceRuleResponse:
        """
        @summary 推送指标到指定资源规则
        
        @param tmp_req: PushResourceRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushResourceRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_rec_service_20221213_models.PushResourceRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.metric_info):
            request.metric_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.metric_info, 'MetricInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.metric_info_shrink):
            query['MetricInfo'] = request.metric_info_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushResourceRule',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/resourcerules/{OpenApiUtilClient.get_encode_param(resource_rule_id)}/action/push',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.PushResourceRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_resource_rule(
        self,
        resource_rule_id: str,
        request: pai_rec_service_20221213_models.PushResourceRuleRequest,
    ) -> pai_rec_service_20221213_models.PushResourceRuleResponse:
        """
        @summary 推送指标到指定资源规则
        
        @param request: PushResourceRuleRequest
        @return: PushResourceRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_resource_rule_with_options(resource_rule_id, request, headers, runtime)

    async def push_resource_rule_async(
        self,
        resource_rule_id: str,
        request: pai_rec_service_20221213_models.PushResourceRuleRequest,
    ) -> pai_rec_service_20221213_models.PushResourceRuleResponse:
        """
        @summary 推送指标到指定资源规则
        
        @param request: PushResourceRuleRequest
        @return: PushResourceRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.push_resource_rule_with_options_async(resource_rule_id, request, headers, runtime)

    def query_sample_consistency_job_difference_with_options(
        self,
        sample_consistency_job_id: str,
        request: pai_rec_service_20221213_models.QuerySampleConsistencyJobDifferenceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.QuerySampleConsistencyJobDifferenceResponse:
        """
        @summary 查看样本一致性任务差异的详情
        
        @param request: QuerySampleConsistencyJobDifferenceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySampleConsistencyJobDifferenceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not UtilClient.is_unset(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySampleConsistencyJobDifference',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/sampleconsistencyjobs/{OpenApiUtilClient.get_encode_param(sample_consistency_job_id)}/action/querydifference',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.QuerySampleConsistencyJobDifferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sample_consistency_job_difference_with_options_async(
        self,
        sample_consistency_job_id: str,
        request: pai_rec_service_20221213_models.QuerySampleConsistencyJobDifferenceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.QuerySampleConsistencyJobDifferenceResponse:
        """
        @summary 查看样本一致性任务差异的详情
        
        @param request: QuerySampleConsistencyJobDifferenceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySampleConsistencyJobDifferenceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not UtilClient.is_unset(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySampleConsistencyJobDifference',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/sampleconsistencyjobs/{OpenApiUtilClient.get_encode_param(sample_consistency_job_id)}/action/querydifference',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.QuerySampleConsistencyJobDifferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sample_consistency_job_difference(
        self,
        sample_consistency_job_id: str,
        request: pai_rec_service_20221213_models.QuerySampleConsistencyJobDifferenceRequest,
    ) -> pai_rec_service_20221213_models.QuerySampleConsistencyJobDifferenceResponse:
        """
        @summary 查看样本一致性任务差异的详情
        
        @param request: QuerySampleConsistencyJobDifferenceRequest
        @return: QuerySampleConsistencyJobDifferenceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_sample_consistency_job_difference_with_options(sample_consistency_job_id, request, headers, runtime)

    async def query_sample_consistency_job_difference_async(
        self,
        sample_consistency_job_id: str,
        request: pai_rec_service_20221213_models.QuerySampleConsistencyJobDifferenceRequest,
    ) -> pai_rec_service_20221213_models.QuerySampleConsistencyJobDifferenceResponse:
        """
        @summary 查看样本一致性任务差异的详情
        
        @param request: QuerySampleConsistencyJobDifferenceRequest
        @return: QuerySampleConsistencyJobDifferenceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_sample_consistency_job_difference_with_options_async(sample_consistency_job_id, request, headers, runtime)

    def query_traffic_control_target_item_report_detail_with_options(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.QueryTrafficControlTargetItemReportDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.QueryTrafficControlTargetItemReportDetailResponse:
        """
        @summary 查询流量调控目标的单品调控报表详情。
        
        @param request: QueryTrafficControlTargetItemReportDetailRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTrafficControlTargetItemReportDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.date):
            query['Date'] = request.date
        if not UtilClient.is_unset(request.environment):
            query['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTrafficControlTargetItemReportDetail',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltargets/{OpenApiUtilClient.get_encode_param(traffic_control_target_id)}/itemcontrolreportdetail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.QueryTrafficControlTargetItemReportDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_traffic_control_target_item_report_detail_with_options_async(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.QueryTrafficControlTargetItemReportDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.QueryTrafficControlTargetItemReportDetailResponse:
        """
        @summary 查询流量调控目标的单品调控报表详情。
        
        @param request: QueryTrafficControlTargetItemReportDetailRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTrafficControlTargetItemReportDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.date):
            query['Date'] = request.date
        if not UtilClient.is_unset(request.environment):
            query['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTrafficControlTargetItemReportDetail',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltargets/{OpenApiUtilClient.get_encode_param(traffic_control_target_id)}/itemcontrolreportdetail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.QueryTrafficControlTargetItemReportDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_traffic_control_target_item_report_detail(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.QueryTrafficControlTargetItemReportDetailRequest,
    ) -> pai_rec_service_20221213_models.QueryTrafficControlTargetItemReportDetailResponse:
        """
        @summary 查询流量调控目标的单品调控报表详情。
        
        @param request: QueryTrafficControlTargetItemReportDetailRequest
        @return: QueryTrafficControlTargetItemReportDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_traffic_control_target_item_report_detail_with_options(traffic_control_target_id, request, headers, runtime)

    async def query_traffic_control_target_item_report_detail_async(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.QueryTrafficControlTargetItemReportDetailRequest,
    ) -> pai_rec_service_20221213_models.QueryTrafficControlTargetItemReportDetailResponse:
        """
        @summary 查询流量调控目标的单品调控报表详情。
        
        @param request: QueryTrafficControlTargetItemReportDetailRequest
        @return: QueryTrafficControlTargetItemReportDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_traffic_control_target_item_report_detail_with_options_async(traffic_control_target_id, request, headers, runtime)

    def release_traffic_control_task_with_options(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.ReleaseTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ReleaseTrafficControlTaskResponse:
        """
        @summary 发布流量调控任务
        
        @param request: ReleaseTrafficControlTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseTrafficControlTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseTrafficControlTask',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltasks/{OpenApiUtilClient.get_encode_param(traffic_control_task_id)}/action/release',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ReleaseTrafficControlTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_traffic_control_task_with_options_async(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.ReleaseTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ReleaseTrafficControlTaskResponse:
        """
        @summary 发布流量调控任务
        
        @param request: ReleaseTrafficControlTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseTrafficControlTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseTrafficControlTask',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltasks/{OpenApiUtilClient.get_encode_param(traffic_control_task_id)}/action/release',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ReleaseTrafficControlTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_traffic_control_task(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.ReleaseTrafficControlTaskRequest,
    ) -> pai_rec_service_20221213_models.ReleaseTrafficControlTaskResponse:
        """
        @summary 发布流量调控任务
        
        @param request: ReleaseTrafficControlTaskRequest
        @return: ReleaseTrafficControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.release_traffic_control_task_with_options(traffic_control_task_id, request, headers, runtime)

    async def release_traffic_control_task_async(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.ReleaseTrafficControlTaskRequest,
    ) -> pai_rec_service_20221213_models.ReleaseTrafficControlTaskResponse:
        """
        @summary 发布流量调控任务
        
        @param request: ReleaseTrafficControlTaskRequest
        @return: ReleaseTrafficControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.release_traffic_control_task_with_options_async(traffic_control_task_id, request, headers, runtime)

    def report_abmetric_group_with_options(
        self,
        abmetric_group_id: str,
        request: pai_rec_service_20221213_models.ReportABMetricGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ReportABMetricGroupResponse:
        """
        @summary 对指标组进行报表。
        
        @param request: ReportABMetricGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReportABMetricGroupResponse
        """
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
        """
        @summary 对指标组进行报表。
        
        @param request: ReportABMetricGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReportABMetricGroupResponse
        """
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
        """
        @summary 对指标组进行报表。
        
        @param request: ReportABMetricGroupRequest
        @return: ReportABMetricGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.report_abmetric_group_with_options(abmetric_group_id, request, headers, runtime)

    async def report_abmetric_group_async(
        self,
        abmetric_group_id: str,
        request: pai_rec_service_20221213_models.ReportABMetricGroupRequest,
    ) -> pai_rec_service_20221213_models.ReportABMetricGroupResponse:
        """
        @summary 对指标组进行报表。
        
        @param request: ReportABMetricGroupRequest
        @return: ReportABMetricGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.report_abmetric_group_with_options_async(abmetric_group_id, request, headers, runtime)

    def report_sample_consistency_job_with_options(
        self,
        sample_consistency_job_id: str,
        request: pai_rec_service_20221213_models.ReportSampleConsistencyJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ReportSampleConsistencyJobResponse:
        """
        @summary 样本一致性任务报表
        
        @param request: ReportSampleConsistencyJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReportSampleConsistencyJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportSampleConsistencyJob',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/sampleconsistencyjobs/{OpenApiUtilClient.get_encode_param(sample_consistency_job_id)}/action/report',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ReportSampleConsistencyJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_sample_consistency_job_with_options_async(
        self,
        sample_consistency_job_id: str,
        request: pai_rec_service_20221213_models.ReportSampleConsistencyJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.ReportSampleConsistencyJobResponse:
        """
        @summary 样本一致性任务报表
        
        @param request: ReportSampleConsistencyJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReportSampleConsistencyJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportSampleConsistencyJob',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/sampleconsistencyjobs/{OpenApiUtilClient.get_encode_param(sample_consistency_job_id)}/action/report',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ReportSampleConsistencyJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_sample_consistency_job(
        self,
        sample_consistency_job_id: str,
        request: pai_rec_service_20221213_models.ReportSampleConsistencyJobRequest,
    ) -> pai_rec_service_20221213_models.ReportSampleConsistencyJobResponse:
        """
        @summary 样本一致性任务报表
        
        @param request: ReportSampleConsistencyJobRequest
        @return: ReportSampleConsistencyJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.report_sample_consistency_job_with_options(sample_consistency_job_id, request, headers, runtime)

    async def report_sample_consistency_job_async(
        self,
        sample_consistency_job_id: str,
        request: pai_rec_service_20221213_models.ReportSampleConsistencyJobRequest,
    ) -> pai_rec_service_20221213_models.ReportSampleConsistencyJobResponse:
        """
        @summary 样本一致性任务报表
        
        @param request: ReportSampleConsistencyJobRequest
        @return: ReportSampleConsistencyJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.report_sample_consistency_job_with_options_async(sample_consistency_job_id, request, headers, runtime)

    def split_traffic_control_target_with_options(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.SplitTrafficControlTargetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.SplitTrafficControlTargetResponse:
        """
        @summary 拆分流量调控目标
        
        @param request: SplitTrafficControlTargetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SplitTrafficControlTargetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.set_points):
            body['SetPoints'] = request.set_points
        if not UtilClient.is_unset(request.set_values):
            body['SetValues'] = request.set_values
        if not UtilClient.is_unset(request.time_points):
            body['TimePoints'] = request.time_points
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SplitTrafficControlTarget',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltargets/{OpenApiUtilClient.get_encode_param(traffic_control_target_id)}/action/split',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.SplitTrafficControlTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def split_traffic_control_target_with_options_async(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.SplitTrafficControlTargetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.SplitTrafficControlTargetResponse:
        """
        @summary 拆分流量调控目标
        
        @param request: SplitTrafficControlTargetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SplitTrafficControlTargetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.set_points):
            body['SetPoints'] = request.set_points
        if not UtilClient.is_unset(request.set_values):
            body['SetValues'] = request.set_values
        if not UtilClient.is_unset(request.time_points):
            body['TimePoints'] = request.time_points
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SplitTrafficControlTarget',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltargets/{OpenApiUtilClient.get_encode_param(traffic_control_target_id)}/action/split',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.SplitTrafficControlTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def split_traffic_control_target(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.SplitTrafficControlTargetRequest,
    ) -> pai_rec_service_20221213_models.SplitTrafficControlTargetResponse:
        """
        @summary 拆分流量调控目标
        
        @param request: SplitTrafficControlTargetRequest
        @return: SplitTrafficControlTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.split_traffic_control_target_with_options(traffic_control_target_id, request, headers, runtime)

    async def split_traffic_control_target_async(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.SplitTrafficControlTargetRequest,
    ) -> pai_rec_service_20221213_models.SplitTrafficControlTargetResponse:
        """
        @summary 拆分流量调控目标
        
        @param request: SplitTrafficControlTargetRequest
        @return: SplitTrafficControlTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.split_traffic_control_target_with_options_async(traffic_control_target_id, request, headers, runtime)

    def start_traffic_control_target_with_options(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.StartTrafficControlTargetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.StartTrafficControlTargetResponse:
        """
        @summary 开启流量调控目标
        
        @param request: StartTrafficControlTargetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartTrafficControlTargetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartTrafficControlTarget',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltargets/{OpenApiUtilClient.get_encode_param(traffic_control_target_id)}/action/start',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.StartTrafficControlTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_traffic_control_target_with_options_async(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.StartTrafficControlTargetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.StartTrafficControlTargetResponse:
        """
        @summary 开启流量调控目标
        
        @param request: StartTrafficControlTargetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartTrafficControlTargetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartTrafficControlTarget',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltargets/{OpenApiUtilClient.get_encode_param(traffic_control_target_id)}/action/start',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.StartTrafficControlTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_traffic_control_target(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.StartTrafficControlTargetRequest,
    ) -> pai_rec_service_20221213_models.StartTrafficControlTargetResponse:
        """
        @summary 开启流量调控目标
        
        @param request: StartTrafficControlTargetRequest
        @return: StartTrafficControlTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_traffic_control_target_with_options(traffic_control_target_id, request, headers, runtime)

    async def start_traffic_control_target_async(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.StartTrafficControlTargetRequest,
    ) -> pai_rec_service_20221213_models.StartTrafficControlTargetResponse:
        """
        @summary 开启流量调控目标
        
        @param request: StartTrafficControlTargetRequest
        @return: StartTrafficControlTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_traffic_control_target_with_options_async(traffic_control_target_id, request, headers, runtime)

    def start_traffic_control_task_with_options(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.StartTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.StartTrafficControlTaskResponse:
        """
        @summary 开启流量调控任务
        
        @param request: StartTrafficControlTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartTrafficControlTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartTrafficControlTask',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltasks/{OpenApiUtilClient.get_encode_param(traffic_control_task_id)}/action/start',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.StartTrafficControlTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_traffic_control_task_with_options_async(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.StartTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.StartTrafficControlTaskResponse:
        """
        @summary 开启流量调控任务
        
        @param request: StartTrafficControlTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartTrafficControlTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartTrafficControlTask',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltasks/{OpenApiUtilClient.get_encode_param(traffic_control_task_id)}/action/start',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.StartTrafficControlTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_traffic_control_task(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.StartTrafficControlTaskRequest,
    ) -> pai_rec_service_20221213_models.StartTrafficControlTaskResponse:
        """
        @summary 开启流量调控任务
        
        @param request: StartTrafficControlTaskRequest
        @return: StartTrafficControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_traffic_control_task_with_options(traffic_control_task_id, request, headers, runtime)

    async def start_traffic_control_task_async(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.StartTrafficControlTaskRequest,
    ) -> pai_rec_service_20221213_models.StartTrafficControlTaskResponse:
        """
        @summary 开启流量调控任务
        
        @param request: StartTrafficControlTaskRequest
        @return: StartTrafficControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_traffic_control_task_with_options_async(traffic_control_task_id, request, headers, runtime)

    def stop_sample_consistency_job_with_options(
        self,
        sample_consistency_job_id: str,
        request: pai_rec_service_20221213_models.StopSampleConsistencyJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.StopSampleConsistencyJobResponse:
        """
        @summary 停止样本一致性任务
        
        @param request: StopSampleConsistencyJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopSampleConsistencyJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopSampleConsistencyJob',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/sampleconsistencyjobs/{OpenApiUtilClient.get_encode_param(sample_consistency_job_id)}/action/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.StopSampleConsistencyJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_sample_consistency_job_with_options_async(
        self,
        sample_consistency_job_id: str,
        request: pai_rec_service_20221213_models.StopSampleConsistencyJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.StopSampleConsistencyJobResponse:
        """
        @summary 停止样本一致性任务
        
        @param request: StopSampleConsistencyJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopSampleConsistencyJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopSampleConsistencyJob',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/sampleconsistencyjobs/{OpenApiUtilClient.get_encode_param(sample_consistency_job_id)}/action/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.StopSampleConsistencyJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_sample_consistency_job(
        self,
        sample_consistency_job_id: str,
        request: pai_rec_service_20221213_models.StopSampleConsistencyJobRequest,
    ) -> pai_rec_service_20221213_models.StopSampleConsistencyJobResponse:
        """
        @summary 停止样本一致性任务
        
        @param request: StopSampleConsistencyJobRequest
        @return: StopSampleConsistencyJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_sample_consistency_job_with_options(sample_consistency_job_id, request, headers, runtime)

    async def stop_sample_consistency_job_async(
        self,
        sample_consistency_job_id: str,
        request: pai_rec_service_20221213_models.StopSampleConsistencyJobRequest,
    ) -> pai_rec_service_20221213_models.StopSampleConsistencyJobResponse:
        """
        @summary 停止样本一致性任务
        
        @param request: StopSampleConsistencyJobRequest
        @return: StopSampleConsistencyJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_sample_consistency_job_with_options_async(sample_consistency_job_id, request, headers, runtime)

    def stop_traffic_control_target_with_options(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.StopTrafficControlTargetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.StopTrafficControlTargetResponse:
        """
        @summary 停止流量调控目标
        
        @param request: StopTrafficControlTargetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopTrafficControlTargetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopTrafficControlTarget',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltargets/{OpenApiUtilClient.get_encode_param(traffic_control_target_id)}/action/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.StopTrafficControlTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_traffic_control_target_with_options_async(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.StopTrafficControlTargetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.StopTrafficControlTargetResponse:
        """
        @summary 停止流量调控目标
        
        @param request: StopTrafficControlTargetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopTrafficControlTargetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopTrafficControlTarget',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltargets/{OpenApiUtilClient.get_encode_param(traffic_control_target_id)}/action/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.StopTrafficControlTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_traffic_control_target(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.StopTrafficControlTargetRequest,
    ) -> pai_rec_service_20221213_models.StopTrafficControlTargetResponse:
        """
        @summary 停止流量调控目标
        
        @param request: StopTrafficControlTargetRequest
        @return: StopTrafficControlTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_traffic_control_target_with_options(traffic_control_target_id, request, headers, runtime)

    async def stop_traffic_control_target_async(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.StopTrafficControlTargetRequest,
    ) -> pai_rec_service_20221213_models.StopTrafficControlTargetResponse:
        """
        @summary 停止流量调控目标
        
        @param request: StopTrafficControlTargetRequest
        @return: StopTrafficControlTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_traffic_control_target_with_options_async(traffic_control_target_id, request, headers, runtime)

    def stop_traffic_control_task_with_options(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.StopTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.StopTrafficControlTaskResponse:
        """
        @summary 停止流量调控任务
        
        @param request: StopTrafficControlTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopTrafficControlTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopTrafficControlTask',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltasks/{OpenApiUtilClient.get_encode_param(traffic_control_task_id)}/action/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.StopTrafficControlTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_traffic_control_task_with_options_async(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.StopTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.StopTrafficControlTaskResponse:
        """
        @summary 停止流量调控任务
        
        @param request: StopTrafficControlTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopTrafficControlTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopTrafficControlTask',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltasks/{OpenApiUtilClient.get_encode_param(traffic_control_task_id)}/action/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.StopTrafficControlTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_traffic_control_task(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.StopTrafficControlTaskRequest,
    ) -> pai_rec_service_20221213_models.StopTrafficControlTaskResponse:
        """
        @summary 停止流量调控任务
        
        @param request: StopTrafficControlTaskRequest
        @return: StopTrafficControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_traffic_control_task_with_options(traffic_control_task_id, request, headers, runtime)

    async def stop_traffic_control_task_async(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.StopTrafficControlTaskRequest,
    ) -> pai_rec_service_20221213_models.StopTrafficControlTaskResponse:
        """
        @summary 停止流量调控任务
        
        @param request: StopTrafficControlTaskRequest
        @return: StopTrafficControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_traffic_control_task_with_options_async(traffic_control_task_id, request, headers, runtime)

    def sync_feature_consistency_check_job_replay_log_with_options(
        self,
        request: pai_rec_service_20221213_models.SyncFeatureConsistencyCheckJobReplayLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.SyncFeatureConsistencyCheckJobReplayLogResponse:
        """
        @summary 同步特征一致性检测任务重放日志。
        
        @param request: SyncFeatureConsistencyCheckJobReplayLogRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncFeatureConsistencyCheckJobReplayLogResponse
        """
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
        """
        @summary 同步特征一致性检测任务重放日志。
        
        @param request: SyncFeatureConsistencyCheckJobReplayLogRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncFeatureConsistencyCheckJobReplayLogResponse
        """
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
        """
        @summary 同步特征一致性检测任务重放日志。
        
        @param request: SyncFeatureConsistencyCheckJobReplayLogRequest
        @return: SyncFeatureConsistencyCheckJobReplayLogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.sync_feature_consistency_check_job_replay_log_with_options(request, headers, runtime)

    async def sync_feature_consistency_check_job_replay_log_async(
        self,
        request: pai_rec_service_20221213_models.SyncFeatureConsistencyCheckJobReplayLogRequest,
    ) -> pai_rec_service_20221213_models.SyncFeatureConsistencyCheckJobReplayLogResponse:
        """
        @summary 同步特征一致性检测任务重放日志。
        
        @param request: SyncFeatureConsistencyCheckJobReplayLogRequest
        @return: SyncFeatureConsistencyCheckJobReplayLogResponse
        """
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
        """
        @summary 取消指定特征一致性检查正在运行中的任务。
        
        @param request: TerminateFeatureConsistencyCheckJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TerminateFeatureConsistencyCheckJobResponse
        """
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
        """
        @summary 取消指定特征一致性检查正在运行中的任务。
        
        @param request: TerminateFeatureConsistencyCheckJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TerminateFeatureConsistencyCheckJobResponse
        """
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
        """
        @summary 取消指定特征一致性检查正在运行中的任务。
        
        @param request: TerminateFeatureConsistencyCheckJobRequest
        @return: TerminateFeatureConsistencyCheckJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.terminate_feature_consistency_check_job_with_options(feature_consistency_check_job_id, request, headers, runtime)

    async def terminate_feature_consistency_check_job_async(
        self,
        feature_consistency_check_job_id: str,
        request: pai_rec_service_20221213_models.TerminateFeatureConsistencyCheckJobRequest,
    ) -> pai_rec_service_20221213_models.TerminateFeatureConsistencyCheckJobResponse:
        """
        @summary 取消指定特征一致性检查正在运行中的任务。
        
        @param request: TerminateFeatureConsistencyCheckJobRequest
        @return: TerminateFeatureConsistencyCheckJobResponse
        """
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
        """
        @summary 更新AB Test实验指标。
        
        @param request: UpdateABMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateABMetricResponse
        """
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
        """
        @summary 更新AB Test实验指标。
        
        @param request: UpdateABMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateABMetricResponse
        """
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
        """
        @summary 更新AB Test实验指标。
        
        @param request: UpdateABMetricRequest
        @return: UpdateABMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_abmetric_with_options(abmetric_id, request, headers, runtime)

    async def update_abmetric_async(
        self,
        abmetric_id: str,
        request: pai_rec_service_20221213_models.UpdateABMetricRequest,
    ) -> pai_rec_service_20221213_models.UpdateABMetricResponse:
        """
        @summary 更新AB Test实验指标。
        
        @param request: UpdateABMetricRequest
        @return: UpdateABMetricResponse
        """
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
        """
        @summary 更新AB test实验指标组。
        
        @param request: UpdateABMetricGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateABMetricGroupResponse
        """
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
        """
        @summary 更新AB test实验指标组。
        
        @param request: UpdateABMetricGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateABMetricGroupResponse
        """
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
        """
        @summary 更新AB test实验指标组。
        
        @param request: UpdateABMetricGroupRequest
        @return: UpdateABMetricGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_abmetric_group_with_options(abmetric_group_id, request, headers, runtime)

    async def update_abmetric_group_async(
        self,
        abmetric_group_id: str,
        request: pai_rec_service_20221213_models.UpdateABMetricGroupRequest,
    ) -> pai_rec_service_20221213_models.UpdateABMetricGroupResponse:
        """
        @summary 更新AB test实验指标组。
        
        @param request: UpdateABMetricGroupRequest
        @return: UpdateABMetricGroupResponse
        """
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
        """
        @summary 更新指定人群。
        
        @param request: UpdateCrowdRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCrowdResponse
        """
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
        """
        @summary 更新指定人群。
        
        @param request: UpdateCrowdRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCrowdResponse
        """
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
        """
        @summary 更新指定人群。
        
        @param request: UpdateCrowdRequest
        @return: UpdateCrowdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_crowd_with_options(crowd_id, request, headers, runtime)

    async def update_crowd_async(
        self,
        crowd_id: str,
        request: pai_rec_service_20221213_models.UpdateCrowdRequest,
    ) -> pai_rec_service_20221213_models.UpdateCrowdResponse:
        """
        @summary 更新指定人群。
        
        @param request: UpdateCrowdRequest
        @return: UpdateCrowdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_crowd_with_options_async(crowd_id, request, headers, runtime)

    def update_engine_config_with_options(
        self,
        engine_config_id: str,
        request: pai_rec_service_20221213_models.UpdateEngineConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateEngineConfigResponse:
        """
        @summary 更新引擎配置。
        
        @param request: UpdateEngineConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateEngineConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config_value):
            body['ConfigValue'] = request.config_value
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEngineConfig',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/engineconfigs/{OpenApiUtilClient.get_encode_param(engine_config_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateEngineConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_engine_config_with_options_async(
        self,
        engine_config_id: str,
        request: pai_rec_service_20221213_models.UpdateEngineConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateEngineConfigResponse:
        """
        @summary 更新引擎配置。
        
        @param request: UpdateEngineConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateEngineConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config_value):
            body['ConfigValue'] = request.config_value
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEngineConfig',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/engineconfigs/{OpenApiUtilClient.get_encode_param(engine_config_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateEngineConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_engine_config(
        self,
        engine_config_id: str,
        request: pai_rec_service_20221213_models.UpdateEngineConfigRequest,
    ) -> pai_rec_service_20221213_models.UpdateEngineConfigResponse:
        """
        @summary 更新引擎配置。
        
        @param request: UpdateEngineConfigRequest
        @return: UpdateEngineConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_engine_config_with_options(engine_config_id, request, headers, runtime)

    async def update_engine_config_async(
        self,
        engine_config_id: str,
        request: pai_rec_service_20221213_models.UpdateEngineConfigRequest,
    ) -> pai_rec_service_20221213_models.UpdateEngineConfigResponse:
        """
        @summary 更新引擎配置。
        
        @param request: UpdateEngineConfigRequest
        @return: UpdateEngineConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_engine_config_with_options_async(engine_config_id, request, headers, runtime)

    def update_experiment_with_options(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.UpdateExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateExperimentResponse:
        """
        @summary 更新实验。
        
        @param request: UpdateExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExperimentResponse
        """
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
        """
        @summary 更新实验。
        
        @param request: UpdateExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExperimentResponse
        """
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
        """
        @summary 更新实验。
        
        @param request: UpdateExperimentRequest
        @return: UpdateExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_experiment_with_options(experiment_id, request, headers, runtime)

    async def update_experiment_async(
        self,
        experiment_id: str,
        request: pai_rec_service_20221213_models.UpdateExperimentRequest,
    ) -> pai_rec_service_20221213_models.UpdateExperimentResponse:
        """
        @summary 更新实验。
        
        @param request: UpdateExperimentRequest
        @return: UpdateExperimentResponse
        """
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
        """
        @summary 更新指定实验组。
        
        @param request: UpdateExperimentGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExperimentGroupResponse
        """
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
        """
        @summary 更新指定实验组。
        
        @param request: UpdateExperimentGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExperimentGroupResponse
        """
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
        """
        @summary 更新指定实验组。
        
        @param request: UpdateExperimentGroupRequest
        @return: UpdateExperimentGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_experiment_group_with_options(experiment_group_id, request, headers, runtime)

    async def update_experiment_group_async(
        self,
        experiment_group_id: str,
        request: pai_rec_service_20221213_models.UpdateExperimentGroupRequest,
    ) -> pai_rec_service_20221213_models.UpdateExperimentGroupResponse:
        """
        @summary 更新指定实验组。
        
        @param request: UpdateExperimentGroupRequest
        @return: UpdateExperimentGroupResponse
        """
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
        """
        @summary 更新特征一致性检查配置信息。
        
        @param request: UpdateFeatureConsistencyCheckJobConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFeatureConsistencyCheckJobConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.compare_feature):
            body['CompareFeature'] = request.compare_feature
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.dataset_mount_path):
            body['DatasetMountPath'] = request.dataset_mount_path
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.dataset_type):
            body['DatasetType'] = request.dataset_type
        if not UtilClient.is_unset(request.dataset_uri):
            body['DatasetUri'] = request.dataset_uri
        if not UtilClient.is_unset(request.default_route):
            body['DefaultRoute'] = request.default_route
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
        if not UtilClient.is_unset(request.predict_worker_count):
            body['PredictWorkerCount'] = request.predict_worker_count
        if not UtilClient.is_unset(request.predict_worker_cpu):
            body['PredictWorkerCpu'] = request.predict_worker_cpu
        if not UtilClient.is_unset(request.predict_worker_memory):
            body['PredictWorkerMemory'] = request.predict_worker_memory
        if not UtilClient.is_unset(request.resource_config):
            body['ResourceConfig'] = request.resource_config
        if not UtilClient.is_unset(request.sample_rate):
            body['SampleRate'] = request.sample_rate
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.security_group_id):
            body['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.switch_id):
            body['SwitchId'] = request.switch_id
        if not UtilClient.is_unset(request.user_id_field):
            body['UserIdField'] = request.user_id_field
        if not UtilClient.is_unset(request.user_table):
            body['UserTable'] = request.user_table
        if not UtilClient.is_unset(request.user_table_partition_field):
            body['UserTablePartitionField'] = request.user_table_partition_field
        if not UtilClient.is_unset(request.user_table_partition_field_format):
            body['UserTablePartitionFieldFormat'] = request.user_table_partition_field_format
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.workflow_name):
            body['WorkflowName'] = request.workflow_name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
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
        """
        @summary 更新特征一致性检查配置信息。
        
        @param request: UpdateFeatureConsistencyCheckJobConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFeatureConsistencyCheckJobConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.compare_feature):
            body['CompareFeature'] = request.compare_feature
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.dataset_mount_path):
            body['DatasetMountPath'] = request.dataset_mount_path
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.dataset_type):
            body['DatasetType'] = request.dataset_type
        if not UtilClient.is_unset(request.dataset_uri):
            body['DatasetUri'] = request.dataset_uri
        if not UtilClient.is_unset(request.default_route):
            body['DefaultRoute'] = request.default_route
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
        if not UtilClient.is_unset(request.predict_worker_count):
            body['PredictWorkerCount'] = request.predict_worker_count
        if not UtilClient.is_unset(request.predict_worker_cpu):
            body['PredictWorkerCpu'] = request.predict_worker_cpu
        if not UtilClient.is_unset(request.predict_worker_memory):
            body['PredictWorkerMemory'] = request.predict_worker_memory
        if not UtilClient.is_unset(request.resource_config):
            body['ResourceConfig'] = request.resource_config
        if not UtilClient.is_unset(request.sample_rate):
            body['SampleRate'] = request.sample_rate
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.security_group_id):
            body['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.switch_id):
            body['SwitchId'] = request.switch_id
        if not UtilClient.is_unset(request.user_id_field):
            body['UserIdField'] = request.user_id_field
        if not UtilClient.is_unset(request.user_table):
            body['UserTable'] = request.user_table
        if not UtilClient.is_unset(request.user_table_partition_field):
            body['UserTablePartitionField'] = request.user_table_partition_field
        if not UtilClient.is_unset(request.user_table_partition_field_format):
            body['UserTablePartitionFieldFormat'] = request.user_table_partition_field_format
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.workflow_name):
            body['WorkflowName'] = request.workflow_name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
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
        """
        @summary 更新特征一致性检查配置信息。
        
        @param request: UpdateFeatureConsistencyCheckJobConfigRequest
        @return: UpdateFeatureConsistencyCheckJobConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_feature_consistency_check_job_config_with_options(feature_consistency_check_job_config_id, request, headers, runtime)

    async def update_feature_consistency_check_job_config_async(
        self,
        feature_consistency_check_job_config_id: str,
        request: pai_rec_service_20221213_models.UpdateFeatureConsistencyCheckJobConfigRequest,
    ) -> pai_rec_service_20221213_models.UpdateFeatureConsistencyCheckJobConfigResponse:
        """
        @summary 更新特征一致性检查配置信息。
        
        @param request: UpdateFeatureConsistencyCheckJobConfigRequest
        @return: UpdateFeatureConsistencyCheckJobConfigResponse
        """
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
        """
        @summary 更新指定实例下指定资源的信息。
        
        @param request: UpdateInstanceResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceResourceResponse
        """
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
        """
        @summary 更新指定实例下指定资源的信息。
        
        @param request: UpdateInstanceResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceResourceResponse
        """
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
        """
        @summary 更新指定实例下指定资源的信息。
        
        @param request: UpdateInstanceResourceRequest
        @return: UpdateInstanceResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_resource_with_options(instance_id, resource_id, request, headers, runtime)

    async def update_instance_resource_async(
        self,
        instance_id: str,
        resource_id: str,
        request: pai_rec_service_20221213_models.UpdateInstanceResourceRequest,
    ) -> pai_rec_service_20221213_models.UpdateInstanceResourceResponse:
        """
        @summary 更新指定实例下指定资源的信息。
        
        @param request: UpdateInstanceResourceRequest
        @return: UpdateInstanceResourceResponse
        """
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
        """
        @summary 更新实验室。
        
        @param request: UpdateLaboratoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLaboratoryResponse
        """
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
        """
        @summary 更新实验室。
        
        @param request: UpdateLaboratoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLaboratoryResponse
        """
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
        """
        @summary 更新实验室。
        
        @param request: UpdateLaboratoryRequest
        @return: UpdateLaboratoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_laboratory_with_options(laboratory_id, request, headers, runtime)

    async def update_laboratory_async(
        self,
        laboratory_id: str,
        request: pai_rec_service_20221213_models.UpdateLaboratoryRequest,
    ) -> pai_rec_service_20221213_models.UpdateLaboratoryResponse:
        """
        @summary 更新实验室。
        
        @param request: UpdateLaboratoryRequest
        @return: UpdateLaboratoryResponse
        """
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
        """
        @summary 更新层。
        
        @param request: UpdateLayerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLayerResponse
        """
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
        """
        @summary 更新层。
        
        @param request: UpdateLayerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLayerResponse
        """
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
        """
        @summary 更新层。
        
        @param request: UpdateLayerRequest
        @return: UpdateLayerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_layer_with_options(layer_id, request, headers, runtime)

    async def update_layer_async(
        self,
        layer_id: str,
        request: pai_rec_service_20221213_models.UpdateLayerRequest,
    ) -> pai_rec_service_20221213_models.UpdateLayerResponse:
        """
        @summary 更新层。
        
        @param request: UpdateLayerRequest
        @return: UpdateLayerResponse
        """
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
        """
        @summary 更新参数。
        
        @param request: UpdateParamRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateParamResponse
        """
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
        """
        @summary 更新参数。
        
        @param request: UpdateParamRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateParamResponse
        """
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
        """
        @summary 更新参数。
        
        @param request: UpdateParamRequest
        @return: UpdateParamResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_param_with_options(param_id, request, headers, runtime)

    async def update_param_async(
        self,
        param_id: str,
        request: pai_rec_service_20221213_models.UpdateParamRequest,
    ) -> pai_rec_service_20221213_models.UpdateParamResponse:
        """
        @summary 更新参数。
        
        @param request: UpdateParamRequest
        @return: UpdateParamResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_param_with_options_async(param_id, request, headers, runtime)

    def update_resource_rule_with_options(
        self,
        resource_rule_id: str,
        request: pai_rec_service_20221213_models.UpdateResourceRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateResourceRuleResponse:
        """
        @summary 获取资源规则列表
        
        @param request: UpdateResourceRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourceRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.metric_operation_type):
            body['MetricOperationType'] = request.metric_operation_type
        if not UtilClient.is_unset(request.metric_pull_info):
            body['MetricPullInfo'] = request.metric_pull_info
        if not UtilClient.is_unset(request.metric_pull_period):
            body['MetricPullPeriod'] = request.metric_pull_period
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.rule_computing_definition):
            body['RuleComputingDefinition'] = request.rule_computing_definition
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceRule',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/resourcerules/{OpenApiUtilClient.get_encode_param(resource_rule_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateResourceRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_rule_with_options_async(
        self,
        resource_rule_id: str,
        request: pai_rec_service_20221213_models.UpdateResourceRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateResourceRuleResponse:
        """
        @summary 获取资源规则列表
        
        @param request: UpdateResourceRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourceRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.metric_operation_type):
            body['MetricOperationType'] = request.metric_operation_type
        if not UtilClient.is_unset(request.metric_pull_info):
            body['MetricPullInfo'] = request.metric_pull_info
        if not UtilClient.is_unset(request.metric_pull_period):
            body['MetricPullPeriod'] = request.metric_pull_period
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.rule_computing_definition):
            body['RuleComputingDefinition'] = request.rule_computing_definition
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceRule',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/resourcerules/{OpenApiUtilClient.get_encode_param(resource_rule_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateResourceRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_rule(
        self,
        resource_rule_id: str,
        request: pai_rec_service_20221213_models.UpdateResourceRuleRequest,
    ) -> pai_rec_service_20221213_models.UpdateResourceRuleResponse:
        """
        @summary 获取资源规则列表
        
        @param request: UpdateResourceRuleRequest
        @return: UpdateResourceRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_resource_rule_with_options(resource_rule_id, request, headers, runtime)

    async def update_resource_rule_async(
        self,
        resource_rule_id: str,
        request: pai_rec_service_20221213_models.UpdateResourceRuleRequest,
    ) -> pai_rec_service_20221213_models.UpdateResourceRuleResponse:
        """
        @summary 获取资源规则列表
        
        @param request: UpdateResourceRuleRequest
        @return: UpdateResourceRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_resource_rule_with_options_async(resource_rule_id, request, headers, runtime)

    def update_resource_rule_item_with_options(
        self,
        resource_rule_id: str,
        resource_rule_item_id: str,
        request: pai_rec_service_20221213_models.UpdateResourceRuleItemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateResourceRuleItemResponse:
        """
        @summary 更新资源规则条目
        
        @param request: UpdateResourceRuleItemRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourceRuleItemResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_value):
            body['MaxValue'] = request.max_value
        if not UtilClient.is_unset(request.min_value):
            body['MinValue'] = request.min_value
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceRuleItem',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/resourcerules/{OpenApiUtilClient.get_encode_param(resource_rule_id)}/items/{OpenApiUtilClient.get_encode_param(resource_rule_item_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateResourceRuleItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_rule_item_with_options_async(
        self,
        resource_rule_id: str,
        resource_rule_item_id: str,
        request: pai_rec_service_20221213_models.UpdateResourceRuleItemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateResourceRuleItemResponse:
        """
        @summary 更新资源规则条目
        
        @param request: UpdateResourceRuleItemRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourceRuleItemResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_value):
            body['MaxValue'] = request.max_value
        if not UtilClient.is_unset(request.min_value):
            body['MinValue'] = request.min_value
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceRuleItem',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/resourcerules/{OpenApiUtilClient.get_encode_param(resource_rule_id)}/items/{OpenApiUtilClient.get_encode_param(resource_rule_item_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateResourceRuleItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_rule_item(
        self,
        resource_rule_id: str,
        resource_rule_item_id: str,
        request: pai_rec_service_20221213_models.UpdateResourceRuleItemRequest,
    ) -> pai_rec_service_20221213_models.UpdateResourceRuleItemResponse:
        """
        @summary 更新资源规则条目
        
        @param request: UpdateResourceRuleItemRequest
        @return: UpdateResourceRuleItemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_resource_rule_item_with_options(resource_rule_id, resource_rule_item_id, request, headers, runtime)

    async def update_resource_rule_item_async(
        self,
        resource_rule_id: str,
        resource_rule_item_id: str,
        request: pai_rec_service_20221213_models.UpdateResourceRuleItemRequest,
    ) -> pai_rec_service_20221213_models.UpdateResourceRuleItemResponse:
        """
        @summary 更新资源规则条目
        
        @param request: UpdateResourceRuleItemRequest
        @return: UpdateResourceRuleItemResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_resource_rule_item_with_options_async(resource_rule_id, resource_rule_item_id, request, headers, runtime)

    def update_scene_with_options(
        self,
        scene_id: str,
        request: pai_rec_service_20221213_models.UpdateSceneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateSceneResponse:
        """
        @summary 更新场景
        
        @param request: UpdateSceneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSceneResponse
        """
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
        """
        @summary 更新场景
        
        @param request: UpdateSceneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSceneResponse
        """
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
        """
        @summary 更新场景
        
        @param request: UpdateSceneRequest
        @return: UpdateSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_scene_with_options(scene_id, request, headers, runtime)

    async def update_scene_async(
        self,
        scene_id: str,
        request: pai_rec_service_20221213_models.UpdateSceneRequest,
    ) -> pai_rec_service_20221213_models.UpdateSceneResponse:
        """
        @summary 更新场景
        
        @param request: UpdateSceneRequest
        @return: UpdateSceneResponse
        """
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
        """
        @summary 获取数据表详细信息。
        
        @param request: UpdateTableMetaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTableMetaResponse
        """
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
        """
        @summary 获取数据表详细信息。
        
        @param request: UpdateTableMetaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTableMetaResponse
        """
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
        """
        @summary 获取数据表详细信息。
        
        @param request: UpdateTableMetaRequest
        @return: UpdateTableMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_table_meta_with_options(table_meta_id, request, headers, runtime)

    async def update_table_meta_async(
        self,
        table_meta_id: str,
        request: pai_rec_service_20221213_models.UpdateTableMetaRequest,
    ) -> pai_rec_service_20221213_models.UpdateTableMetaResponse:
        """
        @summary 获取数据表详细信息。
        
        @param request: UpdateTableMetaRequest
        @return: UpdateTableMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_table_meta_with_options_async(table_meta_id, request, headers, runtime)

    def update_traffic_control_target_with_options(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.UpdateTrafficControlTargetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateTrafficControlTargetResponse:
        """
        @summary 更新流量调控目标
        
        @param request: UpdateTrafficControlTargetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTrafficControlTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_param_3):
            query['new-param-3'] = request.new_param_3
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event):
            body['Event'] = request.event
        if not UtilClient.is_unset(request.item_condition_array):
            body['ItemConditionArray'] = request.item_condition_array
        if not UtilClient.is_unset(request.item_condition_express):
            body['ItemConditionExpress'] = request.item_condition_express
        if not UtilClient.is_unset(request.item_condition_type):
            body['ItemConditionType'] = request.item_condition_type
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.new_product_regulation):
            body['NewProductRegulation'] = request.new_product_regulation
        if not UtilClient.is_unset(request.recall_name):
            body['RecallName'] = request.recall_name
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.statis_period):
            body['StatisPeriod'] = request.statis_period
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tolerance_value):
            body['ToleranceValue'] = request.tolerance_value
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTrafficControlTarget',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltargets/{OpenApiUtilClient.get_encode_param(traffic_control_target_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateTrafficControlTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_traffic_control_target_with_options_async(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.UpdateTrafficControlTargetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateTrafficControlTargetResponse:
        """
        @summary 更新流量调控目标
        
        @param request: UpdateTrafficControlTargetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTrafficControlTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_param_3):
            query['new-param-3'] = request.new_param_3
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event):
            body['Event'] = request.event
        if not UtilClient.is_unset(request.item_condition_array):
            body['ItemConditionArray'] = request.item_condition_array
        if not UtilClient.is_unset(request.item_condition_express):
            body['ItemConditionExpress'] = request.item_condition_express
        if not UtilClient.is_unset(request.item_condition_type):
            body['ItemConditionType'] = request.item_condition_type
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.new_product_regulation):
            body['NewProductRegulation'] = request.new_product_regulation
        if not UtilClient.is_unset(request.recall_name):
            body['RecallName'] = request.recall_name
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.statis_period):
            body['StatisPeriod'] = request.statis_period
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tolerance_value):
            body['ToleranceValue'] = request.tolerance_value
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTrafficControlTarget',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltargets/{OpenApiUtilClient.get_encode_param(traffic_control_target_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateTrafficControlTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_traffic_control_target(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.UpdateTrafficControlTargetRequest,
    ) -> pai_rec_service_20221213_models.UpdateTrafficControlTargetResponse:
        """
        @summary 更新流量调控目标
        
        @param request: UpdateTrafficControlTargetRequest
        @return: UpdateTrafficControlTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_traffic_control_target_with_options(traffic_control_target_id, request, headers, runtime)

    async def update_traffic_control_target_async(
        self,
        traffic_control_target_id: str,
        request: pai_rec_service_20221213_models.UpdateTrafficControlTargetRequest,
    ) -> pai_rec_service_20221213_models.UpdateTrafficControlTargetResponse:
        """
        @summary 更新流量调控目标
        
        @param request: UpdateTrafficControlTargetRequest
        @return: UpdateTrafficControlTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_traffic_control_target_with_options_async(traffic_control_target_id, request, headers, runtime)

    def update_traffic_control_task_with_options(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.UpdateTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateTrafficControlTaskResponse:
        """
        @summary 更新流量调控任务
        
        @param request: UpdateTrafficControlTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTrafficControlTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.behavior_table_meta_id):
            body['BehaviorTableMetaId'] = request.behavior_table_meta_id
        if not UtilClient.is_unset(request.control_granularity):
            body['ControlGranularity'] = request.control_granularity
        if not UtilClient.is_unset(request.control_logic):
            body['ControlLogic'] = request.control_logic
        if not UtilClient.is_unset(request.control_type):
            body['ControlType'] = request.control_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.execution_time):
            body['ExecutionTime'] = request.execution_time
        if not UtilClient.is_unset(request.flink_resource_id):
            body['FlinkResourceId'] = request.flink_resource_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.item_condition_array):
            body['ItemConditionArray'] = request.item_condition_array
        if not UtilClient.is_unset(request.item_condition_express):
            body['ItemConditionExpress'] = request.item_condition_express
        if not UtilClient.is_unset(request.item_condition_type):
            body['ItemConditionType'] = request.item_condition_type
        if not UtilClient.is_unset(request.item_table_meta_id):
            body['ItemTableMetaId'] = request.item_table_meta_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.pre_experiment_ids):
            body['PreExperimentIds'] = request.pre_experiment_ids
        if not UtilClient.is_unset(request.prod_experiment_ids):
            body['ProdExperimentIds'] = request.prod_experiment_ids
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.statis_baeavior_condition_array):
            body['StatisBaeaviorConditionArray'] = request.statis_baeavior_condition_array
        if not UtilClient.is_unset(request.statis_behavior_condition_express):
            body['StatisBehaviorConditionExpress'] = request.statis_behavior_condition_express
        if not UtilClient.is_unset(request.statis_behavior_condition_type):
            body['StatisBehaviorConditionType'] = request.statis_behavior_condition_type
        if not UtilClient.is_unset(request.traffic_control_targets):
            body['TrafficControlTargets'] = request.traffic_control_targets
        if not UtilClient.is_unset(request.user_condition_array):
            body['UserConditionArray'] = request.user_condition_array
        if not UtilClient.is_unset(request.user_condition_express):
            body['UserConditionExpress'] = request.user_condition_express
        if not UtilClient.is_unset(request.user_condition_type):
            body['UserConditionType'] = request.user_condition_type
        if not UtilClient.is_unset(request.user_table_meta_id):
            body['UserTableMetaId'] = request.user_table_meta_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTrafficControlTask',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltasks/{OpenApiUtilClient.get_encode_param(traffic_control_task_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateTrafficControlTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_traffic_control_task_with_options_async(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.UpdateTrafficControlTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateTrafficControlTaskResponse:
        """
        @summary 更新流量调控任务
        
        @param request: UpdateTrafficControlTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTrafficControlTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.behavior_table_meta_id):
            body['BehaviorTableMetaId'] = request.behavior_table_meta_id
        if not UtilClient.is_unset(request.control_granularity):
            body['ControlGranularity'] = request.control_granularity
        if not UtilClient.is_unset(request.control_logic):
            body['ControlLogic'] = request.control_logic
        if not UtilClient.is_unset(request.control_type):
            body['ControlType'] = request.control_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.execution_time):
            body['ExecutionTime'] = request.execution_time
        if not UtilClient.is_unset(request.flink_resource_id):
            body['FlinkResourceId'] = request.flink_resource_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.item_condition_array):
            body['ItemConditionArray'] = request.item_condition_array
        if not UtilClient.is_unset(request.item_condition_express):
            body['ItemConditionExpress'] = request.item_condition_express
        if not UtilClient.is_unset(request.item_condition_type):
            body['ItemConditionType'] = request.item_condition_type
        if not UtilClient.is_unset(request.item_table_meta_id):
            body['ItemTableMetaId'] = request.item_table_meta_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.pre_experiment_ids):
            body['PreExperimentIds'] = request.pre_experiment_ids
        if not UtilClient.is_unset(request.prod_experiment_ids):
            body['ProdExperimentIds'] = request.prod_experiment_ids
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.statis_baeavior_condition_array):
            body['StatisBaeaviorConditionArray'] = request.statis_baeavior_condition_array
        if not UtilClient.is_unset(request.statis_behavior_condition_express):
            body['StatisBehaviorConditionExpress'] = request.statis_behavior_condition_express
        if not UtilClient.is_unset(request.statis_behavior_condition_type):
            body['StatisBehaviorConditionType'] = request.statis_behavior_condition_type
        if not UtilClient.is_unset(request.traffic_control_targets):
            body['TrafficControlTargets'] = request.traffic_control_targets
        if not UtilClient.is_unset(request.user_condition_array):
            body['UserConditionArray'] = request.user_condition_array
        if not UtilClient.is_unset(request.user_condition_express):
            body['UserConditionExpress'] = request.user_condition_express
        if not UtilClient.is_unset(request.user_condition_type):
            body['UserConditionType'] = request.user_condition_type
        if not UtilClient.is_unset(request.user_table_meta_id):
            body['UserTableMetaId'] = request.user_table_meta_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTrafficControlTask',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltasks/{OpenApiUtilClient.get_encode_param(traffic_control_task_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateTrafficControlTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_traffic_control_task(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.UpdateTrafficControlTaskRequest,
    ) -> pai_rec_service_20221213_models.UpdateTrafficControlTaskResponse:
        """
        @summary 更新流量调控任务
        
        @param request: UpdateTrafficControlTaskRequest
        @return: UpdateTrafficControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_traffic_control_task_with_options(traffic_control_task_id, request, headers, runtime)

    async def update_traffic_control_task_async(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.UpdateTrafficControlTaskRequest,
    ) -> pai_rec_service_20221213_models.UpdateTrafficControlTaskResponse:
        """
        @summary 更新流量调控任务
        
        @param request: UpdateTrafficControlTaskRequest
        @return: UpdateTrafficControlTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_traffic_control_task_with_options_async(traffic_control_task_id, request, headers, runtime)

    def update_traffic_control_task_traffic_with_options(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.UpdateTrafficControlTaskTrafficRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateTrafficControlTaskTrafficResponse:
        """
        @summary 更新流量调控任务的流量参数
        
        @param request: UpdateTrafficControlTaskTrafficRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTrafficControlTaskTrafficResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_param_3):
            query['new-param-3'] = request.new_param_3
        body = {}
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.traffics):
            body['Traffics'] = request.traffics
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTrafficControlTaskTraffic',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltasks/{OpenApiUtilClient.get_encode_param(traffic_control_task_id)}/action/traffic',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateTrafficControlTaskTrafficResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_traffic_control_task_traffic_with_options_async(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.UpdateTrafficControlTaskTrafficRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UpdateTrafficControlTaskTrafficResponse:
        """
        @summary 更新流量调控任务的流量参数
        
        @param request: UpdateTrafficControlTaskTrafficRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTrafficControlTaskTrafficResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_param_3):
            query['new-param-3'] = request.new_param_3
        body = {}
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.traffics):
            body['Traffics'] = request.traffics
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTrafficControlTaskTraffic',
            version='2022-12-13',
            protocol='HTTPS',
            pathname=f'/api/v1/trafficcontroltasks/{OpenApiUtilClient.get_encode_param(traffic_control_task_id)}/action/traffic',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateTrafficControlTaskTrafficResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_traffic_control_task_traffic(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.UpdateTrafficControlTaskTrafficRequest,
    ) -> pai_rec_service_20221213_models.UpdateTrafficControlTaskTrafficResponse:
        """
        @summary 更新流量调控任务的流量参数
        
        @param request: UpdateTrafficControlTaskTrafficRequest
        @return: UpdateTrafficControlTaskTrafficResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_traffic_control_task_traffic_with_options(traffic_control_task_id, request, headers, runtime)

    async def update_traffic_control_task_traffic_async(
        self,
        traffic_control_task_id: str,
        request: pai_rec_service_20221213_models.UpdateTrafficControlTaskTrafficRequest,
    ) -> pai_rec_service_20221213_models.UpdateTrafficControlTaskTrafficResponse:
        """
        @summary 更新流量调控任务的流量参数
        
        @param request: UpdateTrafficControlTaskTrafficRequest
        @return: UpdateTrafficControlTaskTrafficResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_traffic_control_task_traffic_with_options_async(traffic_control_task_id, request, headers, runtime)

    def upload_recommendation_data_with_options(
        self,
        request: pai_rec_service_20221213_models.UploadRecommendationDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_rec_service_20221213_models.UploadRecommendationDataResponse:
        """
        @summary 上传数据
        
        @param request: UploadRecommendationDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadRecommendationDataResponse
        """
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
        """
        @summary 上传数据
        
        @param request: UploadRecommendationDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadRecommendationDataResponse
        """
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
        """
        @summary 上传数据
        
        @param request: UploadRecommendationDataRequest
        @return: UploadRecommendationDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upload_recommendation_data_with_options(request, headers, runtime)

    async def upload_recommendation_data_async(
        self,
        request: pai_rec_service_20221213_models.UploadRecommendationDataRequest,
    ) -> pai_rec_service_20221213_models.UploadRecommendationDataResponse:
        """
        @summary 上传数据
        
        @param request: UploadRecommendationDataRequest
        @return: UploadRecommendationDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upload_recommendation_data_with_options_async(request, headers, runtime)
