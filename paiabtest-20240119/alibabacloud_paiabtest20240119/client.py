# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_paiabtest20240119 import models as paiabtest_20240119_models
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
        self._endpoint = self.get_endpoint('paiabtest', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def check_layer_with_options(
        self,
        layer_id: str,
        request: paiabtest_20240119_models.CheckLayerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.CheckLayerResponse:
        """
        @summary 对层上的参数进行校验
        
        @param request: CheckLayerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckLayerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param_names):
            query['ParamNames'] = request.param_names
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckLayer',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/layers/{OpenApiUtilClient.get_encode_param(layer_id)}/action/check',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.CheckLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_layer_with_options_async(
        self,
        layer_id: str,
        request: paiabtest_20240119_models.CheckLayerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.CheckLayerResponse:
        """
        @summary 对层上的参数进行校验
        
        @param request: CheckLayerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckLayerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param_names):
            query['ParamNames'] = request.param_names
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckLayer',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/layers/{OpenApiUtilClient.get_encode_param(layer_id)}/action/check',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.CheckLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_layer(
        self,
        layer_id: str,
        request: paiabtest_20240119_models.CheckLayerRequest,
    ) -> paiabtest_20240119_models.CheckLayerResponse:
        """
        @summary 对层上的参数进行校验
        
        @param request: CheckLayerRequest
        @return: CheckLayerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_layer_with_options(layer_id, request, headers, runtime)

    async def check_layer_async(
        self,
        layer_id: str,
        request: paiabtest_20240119_models.CheckLayerRequest,
    ) -> paiabtest_20240119_models.CheckLayerResponse:
        """
        @summary 对层上的参数进行校验
        
        @param request: CheckLayerRequest
        @return: CheckLayerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.check_layer_with_options_async(layer_id, request, headers, runtime)

    def create_crowd_with_options(
        self,
        request: paiabtest_20240119_models.CreateCrowdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.CreateCrowdResponse:
        """
        @summary 创建人群
        
        @param request: CreateCrowdRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCrowdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCrowd',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/crowds',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.CreateCrowdResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_crowd_with_options_async(
        self,
        request: paiabtest_20240119_models.CreateCrowdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.CreateCrowdResponse:
        """
        @summary 创建人群
        
        @param request: CreateCrowdRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCrowdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCrowd',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/crowds',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.CreateCrowdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_crowd(
        self,
        request: paiabtest_20240119_models.CreateCrowdRequest,
    ) -> paiabtest_20240119_models.CreateCrowdResponse:
        """
        @summary 创建人群
        
        @param request: CreateCrowdRequest
        @return: CreateCrowdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_crowd_with_options(request, headers, runtime)

    async def create_crowd_async(
        self,
        request: paiabtest_20240119_models.CreateCrowdRequest,
    ) -> paiabtest_20240119_models.CreateCrowdResponse:
        """
        @summary 创建人群
        
        @param request: CreateCrowdRequest
        @return: CreateCrowdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_crowd_with_options_async(request, headers, runtime)

    def create_domain_with_options(
        self,
        request: paiabtest_20240119_models.CreateDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.CreateDomainResponse:
        """
        @summary 创建实验域
        
        @param request: CreateDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDomainResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bucket_type):
            body['BucketType'] = request.bucket_type
        if not UtilClient.is_unset(request.condition):
            body['Condition'] = request.condition
        if not UtilClient.is_unset(request.crowd_ids):
            body['CrowdIds'] = request.crowd_ids
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.flow):
            body['Flow'] = request.flow
        if not UtilClient.is_unset(request.layer_id):
            body['LayerId'] = request.layer_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/domains',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.CreateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_domain_with_options_async(
        self,
        request: paiabtest_20240119_models.CreateDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.CreateDomainResponse:
        """
        @summary 创建实验域
        
        @param request: CreateDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDomainResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bucket_type):
            body['BucketType'] = request.bucket_type
        if not UtilClient.is_unset(request.condition):
            body['Condition'] = request.condition
        if not UtilClient.is_unset(request.crowd_ids):
            body['CrowdIds'] = request.crowd_ids
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.flow):
            body['Flow'] = request.flow
        if not UtilClient.is_unset(request.layer_id):
            body['LayerId'] = request.layer_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/domains',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.CreateDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_domain(
        self,
        request: paiabtest_20240119_models.CreateDomainRequest,
    ) -> paiabtest_20240119_models.CreateDomainResponse:
        """
        @summary 创建实验域
        
        @param request: CreateDomainRequest
        @return: CreateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_domain_with_options(request, headers, runtime)

    async def create_domain_async(
        self,
        request: paiabtest_20240119_models.CreateDomainRequest,
    ) -> paiabtest_20240119_models.CreateDomainResponse:
        """
        @summary 创建实验域
        
        @param request: CreateDomainRequest
        @return: CreateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_domain_with_options_async(request, headers, runtime)

    def create_experiment_with_options(
        self,
        request: paiabtest_20240119_models.CreateExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.CreateExperimentResponse:
        """
        @summary 创建实验
        
        @param request: CreateExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateExperimentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bucket_type):
            body['BucketType'] = request.bucket_type
        if not UtilClient.is_unset(request.condition):
            body['Condition'] = request.condition
        if not UtilClient.is_unset(request.core_metric_id):
            body['CoreMetricId'] = request.core_metric_id
        if not UtilClient.is_unset(request.crowd_ids):
            body['CrowdIds'] = request.crowd_ids
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.flow):
            body['Flow'] = request.flow
        if not UtilClient.is_unset(request.focus_metric_ids):
            body['FocusMetricIds'] = request.focus_metric_ids
        if not UtilClient.is_unset(request.layer_id):
            body['LayerId'] = request.layer_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateExperiment',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.CreateExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_experiment_with_options_async(
        self,
        request: paiabtest_20240119_models.CreateExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.CreateExperimentResponse:
        """
        @summary 创建实验
        
        @param request: CreateExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateExperimentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bucket_type):
            body['BucketType'] = request.bucket_type
        if not UtilClient.is_unset(request.condition):
            body['Condition'] = request.condition
        if not UtilClient.is_unset(request.core_metric_id):
            body['CoreMetricId'] = request.core_metric_id
        if not UtilClient.is_unset(request.crowd_ids):
            body['CrowdIds'] = request.crowd_ids
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.flow):
            body['Flow'] = request.flow
        if not UtilClient.is_unset(request.focus_metric_ids):
            body['FocusMetricIds'] = request.focus_metric_ids
        if not UtilClient.is_unset(request.layer_id):
            body['LayerId'] = request.layer_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateExperiment',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.CreateExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_experiment(
        self,
        request: paiabtest_20240119_models.CreateExperimentRequest,
    ) -> paiabtest_20240119_models.CreateExperimentResponse:
        """
        @summary 创建实验
        
        @param request: CreateExperimentRequest
        @return: CreateExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_experiment_with_options(request, headers, runtime)

    async def create_experiment_async(
        self,
        request: paiabtest_20240119_models.CreateExperimentRequest,
    ) -> paiabtest_20240119_models.CreateExperimentResponse:
        """
        @summary 创建实验
        
        @param request: CreateExperimentRequest
        @return: CreateExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_experiment_with_options_async(request, headers, runtime)

    def create_experiment_version_with_options(
        self,
        request: paiabtest_20240119_models.CreateExperimentVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.CreateExperimentVersionResponse:
        """
        @summary 创建实验版本
        
        @param request: CreateExperimentVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateExperimentVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.crowd_ids):
            body['CrowdIds'] = request.crowd_ids
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.experiment_id):
            body['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.flow):
            body['Flow'] = request.flow
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateExperimentVersion',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/experimentversions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.CreateExperimentVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_experiment_version_with_options_async(
        self,
        request: paiabtest_20240119_models.CreateExperimentVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.CreateExperimentVersionResponse:
        """
        @summary 创建实验版本
        
        @param request: CreateExperimentVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateExperimentVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.crowd_ids):
            body['CrowdIds'] = request.crowd_ids
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.experiment_id):
            body['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.flow):
            body['Flow'] = request.flow
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateExperimentVersion',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/experimentversions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.CreateExperimentVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_experiment_version(
        self,
        request: paiabtest_20240119_models.CreateExperimentVersionRequest,
    ) -> paiabtest_20240119_models.CreateExperimentVersionResponse:
        """
        @summary 创建实验版本
        
        @param request: CreateExperimentVersionRequest
        @return: CreateExperimentVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_experiment_version_with_options(request, headers, runtime)

    async def create_experiment_version_async(
        self,
        request: paiabtest_20240119_models.CreateExperimentVersionRequest,
    ) -> paiabtest_20240119_models.CreateExperimentVersionResponse:
        """
        @summary 创建实验版本
        
        @param request: CreateExperimentVersionRequest
        @return: CreateExperimentVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_experiment_version_with_options_async(request, headers, runtime)

    def create_feature_with_options(
        self,
        request: paiabtest_20240119_models.CreateFeatureRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.CreateFeatureResponse:
        """
        @summary 创建Feature
        
        @param request: CreateFeatureRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFeatureResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFeature',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/features',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.CreateFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_feature_with_options_async(
        self,
        request: paiabtest_20240119_models.CreateFeatureRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.CreateFeatureResponse:
        """
        @summary 创建Feature
        
        @param request: CreateFeatureRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFeatureResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFeature',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/features',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.CreateFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_feature(
        self,
        request: paiabtest_20240119_models.CreateFeatureRequest,
    ) -> paiabtest_20240119_models.CreateFeatureResponse:
        """
        @summary 创建Feature
        
        @param request: CreateFeatureRequest
        @return: CreateFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_feature_with_options(request, headers, runtime)

    async def create_feature_async(
        self,
        request: paiabtest_20240119_models.CreateFeatureRequest,
    ) -> paiabtest_20240119_models.CreateFeatureResponse:
        """
        @summary 创建Feature
        
        @param request: CreateFeatureRequest
        @return: CreateFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_feature_with_options_async(request, headers, runtime)

    def create_layer_with_options(
        self,
        request: paiabtest_20240119_models.CreateLayerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.CreateLayerResponse:
        """
        @summary 创建实验层
        
        @param request: CreateLayerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLayerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.domain_id):
            body['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLayer',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/layers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.CreateLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_layer_with_options_async(
        self,
        request: paiabtest_20240119_models.CreateLayerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.CreateLayerResponse:
        """
        @summary 创建实验层
        
        @param request: CreateLayerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLayerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.domain_id):
            body['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLayer',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/layers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.CreateLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_layer(
        self,
        request: paiabtest_20240119_models.CreateLayerRequest,
    ) -> paiabtest_20240119_models.CreateLayerResponse:
        """
        @summary 创建实验层
        
        @param request: CreateLayerRequest
        @return: CreateLayerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_layer_with_options(request, headers, runtime)

    async def create_layer_async(
        self,
        request: paiabtest_20240119_models.CreateLayerRequest,
    ) -> paiabtest_20240119_models.CreateLayerResponse:
        """
        @summary 创建实验层
        
        @param request: CreateLayerRequest
        @return: CreateLayerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_layer_with_options_async(request, headers, runtime)

    def create_metric_with_options(
        self,
        request: paiabtest_20240119_models.CreateMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.CreateMetricResponse:
        """
        @summary 创建指标
        
        @param request: CreateMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMetricResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.definition):
            body['Definition'] = request.definition
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.metric_group_id):
            body['MetricGroupId'] = request.metric_group_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.source_table_meta_id):
            body['SourceTableMetaId'] = request.source_table_meta_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMetric',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/metrics',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.CreateMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_metric_with_options_async(
        self,
        request: paiabtest_20240119_models.CreateMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.CreateMetricResponse:
        """
        @summary 创建指标
        
        @param request: CreateMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMetricResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.definition):
            body['Definition'] = request.definition
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.metric_group_id):
            body['MetricGroupId'] = request.metric_group_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.source_table_meta_id):
            body['SourceTableMetaId'] = request.source_table_meta_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMetric',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/metrics',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.CreateMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_metric(
        self,
        request: paiabtest_20240119_models.CreateMetricRequest,
    ) -> paiabtest_20240119_models.CreateMetricResponse:
        """
        @summary 创建指标
        
        @param request: CreateMetricRequest
        @return: CreateMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_metric_with_options(request, headers, runtime)

    async def create_metric_async(
        self,
        request: paiabtest_20240119_models.CreateMetricRequest,
    ) -> paiabtest_20240119_models.CreateMetricResponse:
        """
        @summary 创建指标
        
        @param request: CreateMetricRequest
        @return: CreateMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_metric_with_options_async(request, headers, runtime)

    def create_metric_group_with_options(
        self,
        request: paiabtest_20240119_models.CreateMetricGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.CreateMetricGroupResponse:
        """
        @summary 创建指标组
        
        @param request: CreateMetricGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMetricGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMetricGroup',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/metricgroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.CreateMetricGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_metric_group_with_options_async(
        self,
        request: paiabtest_20240119_models.CreateMetricGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.CreateMetricGroupResponse:
        """
        @summary 创建指标组
        
        @param request: CreateMetricGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMetricGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMetricGroup',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/metricgroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.CreateMetricGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_metric_group(
        self,
        request: paiabtest_20240119_models.CreateMetricGroupRequest,
    ) -> paiabtest_20240119_models.CreateMetricGroupResponse:
        """
        @summary 创建指标组
        
        @param request: CreateMetricGroupRequest
        @return: CreateMetricGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_metric_group_with_options(request, headers, runtime)

    async def create_metric_group_async(
        self,
        request: paiabtest_20240119_models.CreateMetricGroupRequest,
    ) -> paiabtest_20240119_models.CreateMetricGroupResponse:
        """
        @summary 创建指标组
        
        @param request: CreateMetricGroupRequest
        @return: CreateMetricGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_metric_group_with_options_async(request, headers, runtime)

    def create_project_with_options(
        self,
        request: paiabtest_20240119_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.CreateProjectResponse:
        """
        @summary 创建实验项目
        
        @param request: CreateProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/projects',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_with_options_async(
        self,
        request: paiabtest_20240119_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.CreateProjectResponse:
        """
        @summary 创建实验项目
        
        @param request: CreateProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/projects',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.CreateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project(
        self,
        request: paiabtest_20240119_models.CreateProjectRequest,
    ) -> paiabtest_20240119_models.CreateProjectResponse:
        """
        @summary 创建实验项目
        
        @param request: CreateProjectRequest
        @return: CreateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_project_with_options(request, headers, runtime)

    async def create_project_async(
        self,
        request: paiabtest_20240119_models.CreateProjectRequest,
    ) -> paiabtest_20240119_models.CreateProjectResponse:
        """
        @summary 创建实验项目
        
        @param request: CreateProjectRequest
        @return: CreateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_project_with_options_async(request, headers, runtime)

    def create_table_meta_with_options(
        self,
        request: paiabtest_20240119_models.CreateTableMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.CreateTableMetaResponse:
        """
        @summary 创建数据表
        
        @param request: CreateTableMetaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTableMetaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.datasource_info):
            body['DatasourceInfo'] = request.datasource_info
        if not UtilClient.is_unset(request.datasource_type):
            body['DatasourceType'] = request.datasource_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.fields):
            body['Fields'] = request.fields
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTableMeta',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/tablemetas',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.CreateTableMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_table_meta_with_options_async(
        self,
        request: paiabtest_20240119_models.CreateTableMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.CreateTableMetaResponse:
        """
        @summary 创建数据表
        
        @param request: CreateTableMetaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTableMetaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.datasource_info):
            body['DatasourceInfo'] = request.datasource_info
        if not UtilClient.is_unset(request.datasource_type):
            body['DatasourceType'] = request.datasource_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.fields):
            body['Fields'] = request.fields
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTableMeta',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/tablemetas',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.CreateTableMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_table_meta(
        self,
        request: paiabtest_20240119_models.CreateTableMetaRequest,
    ) -> paiabtest_20240119_models.CreateTableMetaResponse:
        """
        @summary 创建数据表
        
        @param request: CreateTableMetaRequest
        @return: CreateTableMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_table_meta_with_options(request, headers, runtime)

    async def create_table_meta_async(
        self,
        request: paiabtest_20240119_models.CreateTableMetaRequest,
    ) -> paiabtest_20240119_models.CreateTableMetaResponse:
        """
        @summary 创建数据表
        
        @param request: CreateTableMetaRequest
        @return: CreateTableMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_table_meta_with_options_async(request, headers, runtime)

    def delete_crowd_with_options(
        self,
        crowd_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.DeleteCrowdResponse:
        """
        @summary 删除指定的人群
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCrowdResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteCrowd',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/crowds/{OpenApiUtilClient.get_encode_param(crowd_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.DeleteCrowdResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_crowd_with_options_async(
        self,
        crowd_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.DeleteCrowdResponse:
        """
        @summary 删除指定的人群
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCrowdResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteCrowd',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/crowds/{OpenApiUtilClient.get_encode_param(crowd_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.DeleteCrowdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_crowd(
        self,
        crowd_id: str,
    ) -> paiabtest_20240119_models.DeleteCrowdResponse:
        """
        @summary 删除指定的人群
        
        @return: DeleteCrowdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_crowd_with_options(crowd_id, headers, runtime)

    async def delete_crowd_async(
        self,
        crowd_id: str,
    ) -> paiabtest_20240119_models.DeleteCrowdResponse:
        """
        @summary 删除指定的人群
        
        @return: DeleteCrowdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_crowd_with_options_async(crowd_id, headers, runtime)

    def delete_domain_with_options(
        self,
        domain_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.DeleteDomainResponse:
        """
        @summary 删除指定的实验域
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/domains/{OpenApiUtilClient.get_encode_param(domain_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.DeleteDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        domain_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.DeleteDomainResponse:
        """
        @summary 删除指定的实验域
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/domains/{OpenApiUtilClient.get_encode_param(domain_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.DeleteDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain(
        self,
        domain_id: str,
    ) -> paiabtest_20240119_models.DeleteDomainResponse:
        """
        @summary 删除指定的实验域
        
        @return: DeleteDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_domain_with_options(domain_id, headers, runtime)

    async def delete_domain_async(
        self,
        domain_id: str,
    ) -> paiabtest_20240119_models.DeleteDomainResponse:
        """
        @summary 删除指定的实验域
        
        @return: DeleteDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_domain_with_options_async(domain_id, headers, runtime)

    def delete_experiment_with_options(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.DeleteExperimentResponse:
        """
        @summary 删除指定的实验
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteExperiment',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.DeleteExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_experiment_with_options_async(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.DeleteExperimentResponse:
        """
        @summary 删除指定的实验
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteExperiment',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.DeleteExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_experiment(
        self,
        experiment_id: str,
    ) -> paiabtest_20240119_models.DeleteExperimentResponse:
        """
        @summary 删除指定的实验
        
        @return: DeleteExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_experiment_with_options(experiment_id, headers, runtime)

    async def delete_experiment_async(
        self,
        experiment_id: str,
    ) -> paiabtest_20240119_models.DeleteExperimentResponse:
        """
        @summary 删除指定的实验
        
        @return: DeleteExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_experiment_with_options_async(experiment_id, headers, runtime)

    def delete_experiment_version_with_options(
        self,
        experiment_version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.DeleteExperimentVersionResponse:
        """
        @summary 删除指定的实验版本
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExperimentVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteExperimentVersion',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/experimentversions/{OpenApiUtilClient.get_encode_param(experiment_version_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.DeleteExperimentVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_experiment_version_with_options_async(
        self,
        experiment_version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.DeleteExperimentVersionResponse:
        """
        @summary 删除指定的实验版本
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExperimentVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteExperimentVersion',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/experimentversions/{OpenApiUtilClient.get_encode_param(experiment_version_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.DeleteExperimentVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_experiment_version(
        self,
        experiment_version_id: str,
    ) -> paiabtest_20240119_models.DeleteExperimentVersionResponse:
        """
        @summary 删除指定的实验版本
        
        @return: DeleteExperimentVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_experiment_version_with_options(experiment_version_id, headers, runtime)

    async def delete_experiment_version_async(
        self,
        experiment_version_id: str,
    ) -> paiabtest_20240119_models.DeleteExperimentVersionResponse:
        """
        @summary 删除指定的实验版本
        
        @return: DeleteExperimentVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_experiment_version_with_options_async(experiment_version_id, headers, runtime)

    def delete_feature_with_options(
        self,
        feature_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.DeleteFeatureResponse:
        """
        @summary 删除Feature
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFeatureResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFeature',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/features/{OpenApiUtilClient.get_encode_param(feature_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.DeleteFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_feature_with_options_async(
        self,
        feature_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.DeleteFeatureResponse:
        """
        @summary 删除Feature
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFeatureResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFeature',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/features/{OpenApiUtilClient.get_encode_param(feature_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.DeleteFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_feature(
        self,
        feature_id: str,
    ) -> paiabtest_20240119_models.DeleteFeatureResponse:
        """
        @summary 删除Feature
        
        @return: DeleteFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_feature_with_options(feature_id, headers, runtime)

    async def delete_feature_async(
        self,
        feature_id: str,
    ) -> paiabtest_20240119_models.DeleteFeatureResponse:
        """
        @summary 删除Feature
        
        @return: DeleteFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_feature_with_options_async(feature_id, headers, runtime)

    def delete_layer_with_options(
        self,
        layer_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.DeleteLayerResponse:
        """
        @summary 删除指定的实验层
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLayerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteLayer',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/layers/{OpenApiUtilClient.get_encode_param(layer_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.DeleteLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_layer_with_options_async(
        self,
        layer_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.DeleteLayerResponse:
        """
        @summary 删除指定的实验层
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLayerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteLayer',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/layers/{OpenApiUtilClient.get_encode_param(layer_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.DeleteLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_layer(
        self,
        layer_id: str,
    ) -> paiabtest_20240119_models.DeleteLayerResponse:
        """
        @summary 删除指定的实验层
        
        @return: DeleteLayerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_layer_with_options(layer_id, headers, runtime)

    async def delete_layer_async(
        self,
        layer_id: str,
    ) -> paiabtest_20240119_models.DeleteLayerResponse:
        """
        @summary 删除指定的实验层
        
        @return: DeleteLayerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_layer_with_options_async(layer_id, headers, runtime)

    def delete_metric_with_options(
        self,
        metric_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.DeleteMetricResponse:
        """
        @summary 删除指定指标
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMetricResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteMetric',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/metrics/{OpenApiUtilClient.get_encode_param(metric_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.DeleteMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_metric_with_options_async(
        self,
        metric_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.DeleteMetricResponse:
        """
        @summary 删除指定指标
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMetricResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteMetric',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/metrics/{OpenApiUtilClient.get_encode_param(metric_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.DeleteMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_metric(
        self,
        metric_id: str,
    ) -> paiabtest_20240119_models.DeleteMetricResponse:
        """
        @summary 删除指定指标
        
        @return: DeleteMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_metric_with_options(metric_id, headers, runtime)

    async def delete_metric_async(
        self,
        metric_id: str,
    ) -> paiabtest_20240119_models.DeleteMetricResponse:
        """
        @summary 删除指定指标
        
        @return: DeleteMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_metric_with_options_async(metric_id, headers, runtime)

    def delete_metric_group_with_options(
        self,
        metric_group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.DeleteMetricGroupResponse:
        """
        @summary 删除指定的指标组
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMetricGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteMetricGroup',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/metricgroups/{OpenApiUtilClient.get_encode_param(metric_group_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.DeleteMetricGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_metric_group_with_options_async(
        self,
        metric_group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.DeleteMetricGroupResponse:
        """
        @summary 删除指定的指标组
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMetricGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteMetricGroup',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/metricgroups/{OpenApiUtilClient.get_encode_param(metric_group_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.DeleteMetricGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_metric_group(
        self,
        metric_group_id: str,
    ) -> paiabtest_20240119_models.DeleteMetricGroupResponse:
        """
        @summary 删除指定的指标组
        
        @return: DeleteMetricGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_metric_group_with_options(metric_group_id, headers, runtime)

    async def delete_metric_group_async(
        self,
        metric_group_id: str,
    ) -> paiabtest_20240119_models.DeleteMetricGroupResponse:
        """
        @summary 删除指定的指标组
        
        @return: DeleteMetricGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_metric_group_with_options_async(metric_group_id, headers, runtime)

    def delete_project_with_options(
        self,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.DeleteProjectResponse:
        """
        @summary 删除实验项目
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProjectResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.DeleteProjectResponse:
        """
        @summary 删除实验项目
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProjectResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.DeleteProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_project(
        self,
        project_id: str,
    ) -> paiabtest_20240119_models.DeleteProjectResponse:
        """
        @summary 删除实验项目
        
        @return: DeleteProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_project_with_options(project_id, headers, runtime)

    async def delete_project_async(
        self,
        project_id: str,
    ) -> paiabtest_20240119_models.DeleteProjectResponse:
        """
        @summary 删除实验项目
        
        @return: DeleteProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_project_with_options_async(project_id, headers, runtime)

    def delete_table_meta_with_options(
        self,
        table_meta_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.DeleteTableMetaResponse:
        """
        @summary 删除数据表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTableMetaResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTableMeta',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/tablemetas/{OpenApiUtilClient.get_encode_param(table_meta_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.DeleteTableMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_table_meta_with_options_async(
        self,
        table_meta_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.DeleteTableMetaResponse:
        """
        @summary 删除数据表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTableMetaResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTableMeta',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/tablemetas/{OpenApiUtilClient.get_encode_param(table_meta_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.DeleteTableMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_table_meta(
        self,
        table_meta_id: str,
    ) -> paiabtest_20240119_models.DeleteTableMetaResponse:
        """
        @summary 删除数据表
        
        @return: DeleteTableMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_table_meta_with_options(table_meta_id, headers, runtime)

    async def delete_table_meta_async(
        self,
        table_meta_id: str,
    ) -> paiabtest_20240119_models.DeleteTableMetaResponse:
        """
        @summary 删除数据表
        
        @return: DeleteTableMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_table_meta_with_options_async(table_meta_id, headers, runtime)

    def get_crowd_with_options(
        self,
        crowd_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.GetCrowdResponse:
        """
        @summary 获取指定人群详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCrowdResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCrowd',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/crowds/{OpenApiUtilClient.get_encode_param(crowd_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.GetCrowdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_crowd_with_options_async(
        self,
        crowd_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.GetCrowdResponse:
        """
        @summary 获取指定人群详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCrowdResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCrowd',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/crowds/{OpenApiUtilClient.get_encode_param(crowd_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.GetCrowdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_crowd(
        self,
        crowd_id: str,
    ) -> paiabtest_20240119_models.GetCrowdResponse:
        """
        @summary 获取指定人群详情
        
        @return: GetCrowdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_crowd_with_options(crowd_id, headers, runtime)

    async def get_crowd_async(
        self,
        crowd_id: str,
    ) -> paiabtest_20240119_models.GetCrowdResponse:
        """
        @summary 获取指定人群详情
        
        @return: GetCrowdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_crowd_with_options_async(crowd_id, headers, runtime)

    def get_domain_with_options(
        self,
        domain_id: str,
        request: paiabtest_20240119_models.GetDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.GetDomainResponse:
        """
        @summary 获取指定实验域详情
        
        @param request: GetDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomain',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/domains/{OpenApiUtilClient.get_encode_param(domain_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.GetDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_domain_with_options_async(
        self,
        domain_id: str,
        request: paiabtest_20240119_models.GetDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.GetDomainResponse:
        """
        @summary 获取指定实验域详情
        
        @param request: GetDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomain',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/domains/{OpenApiUtilClient.get_encode_param(domain_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.GetDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_domain(
        self,
        domain_id: str,
        request: paiabtest_20240119_models.GetDomainRequest,
    ) -> paiabtest_20240119_models.GetDomainResponse:
        """
        @summary 获取指定实验域详情
        
        @param request: GetDomainRequest
        @return: GetDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_domain_with_options(domain_id, request, headers, runtime)

    async def get_domain_async(
        self,
        domain_id: str,
        request: paiabtest_20240119_models.GetDomainRequest,
    ) -> paiabtest_20240119_models.GetDomainResponse:
        """
        @summary 获取指定实验域详情
        
        @param request: GetDomainRequest
        @return: GetDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_domain_with_options_async(domain_id, request, headers, runtime)

    def get_experiment_with_options(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.GetExperimentResponse:
        """
        @summary 获取指定实验的详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetExperiment',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.GetExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_experiment_with_options_async(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.GetExperimentResponse:
        """
        @summary 获取指定实验的详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetExperiment',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.GetExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_experiment(
        self,
        experiment_id: str,
    ) -> paiabtest_20240119_models.GetExperimentResponse:
        """
        @summary 获取指定实验的详情
        
        @return: GetExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_experiment_with_options(experiment_id, headers, runtime)

    async def get_experiment_async(
        self,
        experiment_id: str,
    ) -> paiabtest_20240119_models.GetExperimentResponse:
        """
        @summary 获取指定实验的详情
        
        @return: GetExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_experiment_with_options_async(experiment_id, headers, runtime)

    def get_experiment_version_with_options(
        self,
        experiment_version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.GetExperimentVersionResponse:
        """
        @summary 获取指定实验版本的详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExperimentVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetExperimentVersion',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/experimentversions/{OpenApiUtilClient.get_encode_param(experiment_version_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.GetExperimentVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_experiment_version_with_options_async(
        self,
        experiment_version_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.GetExperimentVersionResponse:
        """
        @summary 获取指定实验版本的详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExperimentVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetExperimentVersion',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/experimentversions/{OpenApiUtilClient.get_encode_param(experiment_version_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.GetExperimentVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_experiment_version(
        self,
        experiment_version_id: str,
    ) -> paiabtest_20240119_models.GetExperimentVersionResponse:
        """
        @summary 获取指定实验版本的详情
        
        @return: GetExperimentVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_experiment_version_with_options(experiment_version_id, headers, runtime)

    async def get_experiment_version_async(
        self,
        experiment_version_id: str,
    ) -> paiabtest_20240119_models.GetExperimentVersionResponse:
        """
        @summary 获取指定实验版本的详情
        
        @return: GetExperimentVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_experiment_version_with_options_async(experiment_version_id, headers, runtime)

    def get_feature_with_options(
        self,
        feature_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.GetFeatureResponse:
        """
        @summary 获取Feature详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFeatureResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFeature',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/features/{OpenApiUtilClient.get_encode_param(feature_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.GetFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_feature_with_options_async(
        self,
        feature_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.GetFeatureResponse:
        """
        @summary 获取Feature详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFeatureResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFeature',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/features/{OpenApiUtilClient.get_encode_param(feature_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.GetFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_feature(
        self,
        feature_id: str,
    ) -> paiabtest_20240119_models.GetFeatureResponse:
        """
        @summary 获取Feature详情
        
        @return: GetFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_feature_with_options(feature_id, headers, runtime)

    async def get_feature_async(
        self,
        feature_id: str,
    ) -> paiabtest_20240119_models.GetFeatureResponse:
        """
        @summary 获取Feature详情
        
        @return: GetFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_feature_with_options_async(feature_id, headers, runtime)

    def get_layer_with_options(
        self,
        layer_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.GetLayerResponse:
        """
        @summary 获取指定的实验层详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLayerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLayer',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/layers/{OpenApiUtilClient.get_encode_param(layer_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.GetLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_layer_with_options_async(
        self,
        layer_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.GetLayerResponse:
        """
        @summary 获取指定的实验层详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLayerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLayer',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/layers/{OpenApiUtilClient.get_encode_param(layer_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.GetLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_layer(
        self,
        layer_id: str,
    ) -> paiabtest_20240119_models.GetLayerResponse:
        """
        @summary 获取指定的实验层详情
        
        @return: GetLayerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_layer_with_options(layer_id, headers, runtime)

    async def get_layer_async(
        self,
        layer_id: str,
    ) -> paiabtest_20240119_models.GetLayerResponse:
        """
        @summary 获取指定的实验层详情
        
        @return: GetLayerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_layer_with_options_async(layer_id, headers, runtime)

    def get_metric_with_options(
        self,
        metric_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.GetMetricResponse:
        """
        @summary 获取指标详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMetricResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMetric',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/metrics/{OpenApiUtilClient.get_encode_param(metric_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.GetMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_metric_with_options_async(
        self,
        metric_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.GetMetricResponse:
        """
        @summary 获取指标详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMetricResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMetric',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/metrics/{OpenApiUtilClient.get_encode_param(metric_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.GetMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_metric(
        self,
        metric_id: str,
    ) -> paiabtest_20240119_models.GetMetricResponse:
        """
        @summary 获取指标详情
        
        @return: GetMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_metric_with_options(metric_id, headers, runtime)

    async def get_metric_async(
        self,
        metric_id: str,
    ) -> paiabtest_20240119_models.GetMetricResponse:
        """
        @summary 获取指标详情
        
        @return: GetMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_metric_with_options_async(metric_id, headers, runtime)

    def get_metric_group_with_options(
        self,
        metric_group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.GetMetricGroupResponse:
        """
        @summary 获取指标组的详细信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMetricGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMetricGroup',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/metricgroups/{OpenApiUtilClient.get_encode_param(metric_group_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.GetMetricGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_metric_group_with_options_async(
        self,
        metric_group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.GetMetricGroupResponse:
        """
        @summary 获取指标组的详细信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMetricGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMetricGroup',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/metricgroups/{OpenApiUtilClient.get_encode_param(metric_group_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.GetMetricGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_metric_group(
        self,
        metric_group_id: str,
    ) -> paiabtest_20240119_models.GetMetricGroupResponse:
        """
        @summary 获取指标组的详细信息
        
        @return: GetMetricGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_metric_group_with_options(metric_group_id, headers, runtime)

    async def get_metric_group_async(
        self,
        metric_group_id: str,
    ) -> paiabtest_20240119_models.GetMetricGroupResponse:
        """
        @summary 获取指标组的详细信息
        
        @return: GetMetricGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_metric_group_with_options_async(metric_group_id, headers, runtime)

    def get_project_with_options(
        self,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.GetProjectResponse:
        """
        @summary 获取指定的实验项目
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.GetProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_with_options_async(
        self,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.GetProjectResponse:
        """
        @summary 获取指定的实验项目
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.GetProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project(
        self,
        project_id: str,
    ) -> paiabtest_20240119_models.GetProjectResponse:
        """
        @summary 获取指定的实验项目
        
        @return: GetProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_with_options(project_id, headers, runtime)

    async def get_project_async(
        self,
        project_id: str,
    ) -> paiabtest_20240119_models.GetProjectResponse:
        """
        @summary 获取指定的实验项目
        
        @return: GetProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_with_options_async(project_id, headers, runtime)

    def get_table_meta_with_options(
        self,
        table_meta_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.GetTableMetaResponse:
        """
        @summary 获取数据表详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTableMetaResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTableMeta',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/tablemetas/{OpenApiUtilClient.get_encode_param(table_meta_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.GetTableMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_meta_with_options_async(
        self,
        table_meta_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.GetTableMetaResponse:
        """
        @summary 获取数据表详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTableMetaResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTableMeta',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/tablemetas/{OpenApiUtilClient.get_encode_param(table_meta_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.GetTableMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_meta(
        self,
        table_meta_id: str,
    ) -> paiabtest_20240119_models.GetTableMetaResponse:
        """
        @summary 获取数据表详情
        
        @return: GetTableMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_table_meta_with_options(table_meta_id, headers, runtime)

    async def get_table_meta_async(
        self,
        table_meta_id: str,
    ) -> paiabtest_20240119_models.GetTableMetaResponse:
        """
        @summary 获取数据表详情
        
        @return: GetTableMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_table_meta_with_options_async(table_meta_id, headers, runtime)

    def list_crowds_with_options(
        self,
        request: paiabtest_20240119_models.ListCrowdsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.ListCrowdsResponse:
        """
        @summary 获取人群列表
        
        @param request: ListCrowdsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCrowdsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.crowd_id):
            query['CrowdId'] = request.crowd_id
        if not UtilClient.is_unset(request.crowd_name):
            query['CrowdName'] = request.crowd_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCrowds',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/crowds',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.ListCrowdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_crowds_with_options_async(
        self,
        request: paiabtest_20240119_models.ListCrowdsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.ListCrowdsResponse:
        """
        @summary 获取人群列表
        
        @param request: ListCrowdsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCrowdsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.crowd_id):
            query['CrowdId'] = request.crowd_id
        if not UtilClient.is_unset(request.crowd_name):
            query['CrowdName'] = request.crowd_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCrowds',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/crowds',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.ListCrowdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_crowds(
        self,
        request: paiabtest_20240119_models.ListCrowdsRequest,
    ) -> paiabtest_20240119_models.ListCrowdsResponse:
        """
        @summary 获取人群列表
        
        @param request: ListCrowdsRequest
        @return: ListCrowdsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_crowds_with_options(request, headers, runtime)

    async def list_crowds_async(
        self,
        request: paiabtest_20240119_models.ListCrowdsRequest,
    ) -> paiabtest_20240119_models.ListCrowdsResponse:
        """
        @summary 获取人群列表
        
        @param request: ListCrowdsRequest
        @return: ListCrowdsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_crowds_with_options_async(request, headers, runtime)

    def list_domains_with_options(
        self,
        request: paiabtest_20240119_models.ListDomainsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.ListDomainsResponse:
        """
        @summary 获取实验域列表
        
        @param request: ListDomainsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.layer_id):
            query['LayerId'] = request.layer_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDomains',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/domains',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.ListDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_domains_with_options_async(
        self,
        request: paiabtest_20240119_models.ListDomainsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.ListDomainsResponse:
        """
        @summary 获取实验域列表
        
        @param request: ListDomainsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.layer_id):
            query['LayerId'] = request.layer_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDomains',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/domains',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.ListDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_domains(
        self,
        request: paiabtest_20240119_models.ListDomainsRequest,
    ) -> paiabtest_20240119_models.ListDomainsResponse:
        """
        @summary 获取实验域列表
        
        @param request: ListDomainsRequest
        @return: ListDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_domains_with_options(request, headers, runtime)

    async def list_domains_async(
        self,
        request: paiabtest_20240119_models.ListDomainsRequest,
    ) -> paiabtest_20240119_models.ListDomainsResponse:
        """
        @summary 获取实验域列表
        
        @param request: ListDomainsRequest
        @return: ListDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_domains_with_options_async(request, headers, runtime)

    def list_experiment_versions_with_options(
        self,
        request: paiabtest_20240119_models.ListExperimentVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.ListExperimentVersionsResponse:
        """
        @summary 获取实验版本列表
        
        @param request: ListExperimentVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExperimentVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
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
            action='ListExperimentVersions',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/experimentversions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.ListExperimentVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_experiment_versions_with_options_async(
        self,
        request: paiabtest_20240119_models.ListExperimentVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.ListExperimentVersionsResponse:
        """
        @summary 获取实验版本列表
        
        @param request: ListExperimentVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExperimentVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
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
            action='ListExperimentVersions',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/experimentversions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.ListExperimentVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_experiment_versions(
        self,
        request: paiabtest_20240119_models.ListExperimentVersionsRequest,
    ) -> paiabtest_20240119_models.ListExperimentVersionsResponse:
        """
        @summary 获取实验版本列表
        
        @param request: ListExperimentVersionsRequest
        @return: ListExperimentVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_experiment_versions_with_options(request, headers, runtime)

    async def list_experiment_versions_async(
        self,
        request: paiabtest_20240119_models.ListExperimentVersionsRequest,
    ) -> paiabtest_20240119_models.ListExperimentVersionsResponse:
        """
        @summary 获取实验版本列表
        
        @param request: ListExperimentVersionsRequest
        @return: ListExperimentVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_experiment_versions_with_options_async(request, headers, runtime)

    def list_experiments_with_options(
        self,
        request: paiabtest_20240119_models.ListExperimentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.ListExperimentsResponse:
        """
        @summary 获取实验列表
        
        @param request: ListExperimentsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExperimentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.experiment_name):
            query['ExperimentName'] = request.experiment_name
        if not UtilClient.is_unset(request.layer_id):
            query['LayerId'] = request.layer_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExperiments',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.ListExperimentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_experiments_with_options_async(
        self,
        request: paiabtest_20240119_models.ListExperimentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.ListExperimentsResponse:
        """
        @summary 获取实验列表
        
        @param request: ListExperimentsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExperimentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.experiment_name):
            query['ExperimentName'] = request.experiment_name
        if not UtilClient.is_unset(request.layer_id):
            query['LayerId'] = request.layer_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExperiments',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.ListExperimentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_experiments(
        self,
        request: paiabtest_20240119_models.ListExperimentsRequest,
    ) -> paiabtest_20240119_models.ListExperimentsResponse:
        """
        @summary 获取实验列表
        
        @param request: ListExperimentsRequest
        @return: ListExperimentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_experiments_with_options(request, headers, runtime)

    async def list_experiments_async(
        self,
        request: paiabtest_20240119_models.ListExperimentsRequest,
    ) -> paiabtest_20240119_models.ListExperimentsResponse:
        """
        @summary 获取实验列表
        
        @param request: ListExperimentsRequest
        @return: ListExperimentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_experiments_with_options_async(request, headers, runtime)

    def list_features_with_options(
        self,
        request: paiabtest_20240119_models.ListFeaturesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.ListFeaturesResponse:
        """
        @summary 获取Faeture列表
        
        @param request: ListFeaturesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFeaturesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.feature_id):
            query['FeatureId'] = request.feature_id
        if not UtilClient.is_unset(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFeatures',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/features',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.ListFeaturesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_features_with_options_async(
        self,
        request: paiabtest_20240119_models.ListFeaturesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.ListFeaturesResponse:
        """
        @summary 获取Faeture列表
        
        @param request: ListFeaturesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFeaturesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.feature_id):
            query['FeatureId'] = request.feature_id
        if not UtilClient.is_unset(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFeatures',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/features',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.ListFeaturesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_features(
        self,
        request: paiabtest_20240119_models.ListFeaturesRequest,
    ) -> paiabtest_20240119_models.ListFeaturesResponse:
        """
        @summary 获取Faeture列表
        
        @param request: ListFeaturesRequest
        @return: ListFeaturesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_features_with_options(request, headers, runtime)

    async def list_features_async(
        self,
        request: paiabtest_20240119_models.ListFeaturesRequest,
    ) -> paiabtest_20240119_models.ListFeaturesResponse:
        """
        @summary 获取Faeture列表
        
        @param request: ListFeaturesRequest
        @return: ListFeaturesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_features_with_options_async(request, headers, runtime)

    def list_layers_with_options(
        self,
        request: paiabtest_20240119_models.ListLayersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.ListLayersResponse:
        """
        @summary 获取实验层列表
        
        @param request: ListLayersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLayersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.layer_id):
            query['LayerId'] = request.layer_id
        if not UtilClient.is_unset(request.layer_name):
            query['LayerName'] = request.layer_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLayers',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/layers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.ListLayersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_layers_with_options_async(
        self,
        request: paiabtest_20240119_models.ListLayersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.ListLayersResponse:
        """
        @summary 获取实验层列表
        
        @param request: ListLayersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLayersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.layer_id):
            query['LayerId'] = request.layer_id
        if not UtilClient.is_unset(request.layer_name):
            query['LayerName'] = request.layer_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLayers',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/layers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.ListLayersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_layers(
        self,
        request: paiabtest_20240119_models.ListLayersRequest,
    ) -> paiabtest_20240119_models.ListLayersResponse:
        """
        @summary 获取实验层列表
        
        @param request: ListLayersRequest
        @return: ListLayersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_layers_with_options(request, headers, runtime)

    async def list_layers_async(
        self,
        request: paiabtest_20240119_models.ListLayersRequest,
    ) -> paiabtest_20240119_models.ListLayersResponse:
        """
        @summary 获取实验层列表
        
        @param request: ListLayersRequest
        @return: ListLayersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_layers_with_options_async(request, headers, runtime)

    def list_metric_groups_with_options(
        self,
        request: paiabtest_20240119_models.ListMetricGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.ListMetricGroupsResponse:
        """
        @summary 获取指标组列表
        
        @param request: ListMetricGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMetricGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.metric_group_id):
            query['MetricGroupId'] = request.metric_group_id
        if not UtilClient.is_unset(request.metric_group_name):
            query['MetricGroupName'] = request.metric_group_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMetricGroups',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/metricgroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.ListMetricGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_metric_groups_with_options_async(
        self,
        request: paiabtest_20240119_models.ListMetricGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.ListMetricGroupsResponse:
        """
        @summary 获取指标组列表
        
        @param request: ListMetricGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMetricGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.metric_group_id):
            query['MetricGroupId'] = request.metric_group_id
        if not UtilClient.is_unset(request.metric_group_name):
            query['MetricGroupName'] = request.metric_group_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMetricGroups',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/metricgroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.ListMetricGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_metric_groups(
        self,
        request: paiabtest_20240119_models.ListMetricGroupsRequest,
    ) -> paiabtest_20240119_models.ListMetricGroupsResponse:
        """
        @summary 获取指标组列表
        
        @param request: ListMetricGroupsRequest
        @return: ListMetricGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_metric_groups_with_options(request, headers, runtime)

    async def list_metric_groups_async(
        self,
        request: paiabtest_20240119_models.ListMetricGroupsRequest,
    ) -> paiabtest_20240119_models.ListMetricGroupsResponse:
        """
        @summary 获取指标组列表
        
        @param request: ListMetricGroupsRequest
        @return: ListMetricGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_metric_groups_with_options_async(request, headers, runtime)

    def list_metrics_with_options(
        self,
        request: paiabtest_20240119_models.ListMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.ListMetricsResponse:
        """
        @summary 获取指标列表
        
        @param request: ListMetricsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMetricsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.metric_group_id):
            query['MetricGroupId'] = request.metric_group_id
        if not UtilClient.is_unset(request.metric_id):
            query['MetricId'] = request.metric_id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
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
            action='ListMetrics',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/metrics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.ListMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_metrics_with_options_async(
        self,
        request: paiabtest_20240119_models.ListMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.ListMetricsResponse:
        """
        @summary 获取指标列表
        
        @param request: ListMetricsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMetricsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.metric_group_id):
            query['MetricGroupId'] = request.metric_group_id
        if not UtilClient.is_unset(request.metric_id):
            query['MetricId'] = request.metric_id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
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
            action='ListMetrics',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/metrics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.ListMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_metrics(
        self,
        request: paiabtest_20240119_models.ListMetricsRequest,
    ) -> paiabtest_20240119_models.ListMetricsResponse:
        """
        @summary 获取指标列表
        
        @param request: ListMetricsRequest
        @return: ListMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_metrics_with_options(request, headers, runtime)

    async def list_metrics_async(
        self,
        request: paiabtest_20240119_models.ListMetricsRequest,
    ) -> paiabtest_20240119_models.ListMetricsResponse:
        """
        @summary 获取指标列表
        
        @param request: ListMetricsRequest
        @return: ListMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_metrics_with_options_async(request, headers, runtime)

    def list_projects_with_options(
        self,
        request: paiabtest_20240119_models.ListProjectsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.ListProjectsResponse:
        """
        @summary 获取实验项目列表
        
        @param request: ListProjectsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/projects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.ListProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_projects_with_options_async(
        self,
        request: paiabtest_20240119_models.ListProjectsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.ListProjectsResponse:
        """
        @summary 获取实验项目列表
        
        @param request: ListProjectsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/projects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.ListProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_projects(
        self,
        request: paiabtest_20240119_models.ListProjectsRequest,
    ) -> paiabtest_20240119_models.ListProjectsResponse:
        """
        @summary 获取实验项目列表
        
        @param request: ListProjectsRequest
        @return: ListProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_projects_with_options(request, headers, runtime)

    async def list_projects_async(
        self,
        request: paiabtest_20240119_models.ListProjectsRequest,
    ) -> paiabtest_20240119_models.ListProjectsResponse:
        """
        @summary 获取实验项目列表
        
        @param request: ListProjectsRequest
        @return: ListProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_projects_with_options_async(request, headers, runtime)

    def list_table_metas_with_options(
        self,
        request: paiabtest_20240119_models.ListTableMetasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.ListTableMetasResponse:
        """
        @summary 获取数据表列表
        
        @param request: ListTableMetasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTableMetasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.datasource_type):
            query['DatasourceType'] = request.datasource_type
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.table_meta_id):
            query['TableMetaId'] = request.table_meta_id
        if not UtilClient.is_unset(request.table_meta_name):
            query['TableMetaName'] = request.table_meta_name
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTableMetas',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/tablemetas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.ListTableMetasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_table_metas_with_options_async(
        self,
        request: paiabtest_20240119_models.ListTableMetasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.ListTableMetasResponse:
        """
        @summary 获取数据表列表
        
        @param request: ListTableMetasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTableMetasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.datasource_type):
            query['DatasourceType'] = request.datasource_type
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.table_meta_id):
            query['TableMetaId'] = request.table_meta_id
        if not UtilClient.is_unset(request.table_meta_name):
            query['TableMetaName'] = request.table_meta_name
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTableMetas',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/tablemetas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.ListTableMetasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_table_metas(
        self,
        request: paiabtest_20240119_models.ListTableMetasRequest,
    ) -> paiabtest_20240119_models.ListTableMetasResponse:
        """
        @summary 获取数据表列表
        
        @param request: ListTableMetasRequest
        @return: ListTableMetasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_table_metas_with_options(request, headers, runtime)

    async def list_table_metas_async(
        self,
        request: paiabtest_20240119_models.ListTableMetasRequest,
    ) -> paiabtest_20240119_models.ListTableMetasResponse:
        """
        @summary 获取数据表列表
        
        @param request: ListTableMetasRequest
        @return: ListTableMetasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_table_metas_with_options_async(request, headers, runtime)

    def push_all_experiment_version_with_options(
        self,
        experiment_version_id: str,
        request: paiabtest_20240119_models.PushAllExperimentVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.PushAllExperimentVersionResponse:
        """
        @summary 对实验版本推全
        
        @param request: PushAllExperimentVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushAllExperimentVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.feature_name):
            body['FeatureName'] = request.feature_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushAllExperimentVersion',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/experimentversions/{OpenApiUtilClient.get_encode_param(experiment_version_id)}/action/pushall',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.PushAllExperimentVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_all_experiment_version_with_options_async(
        self,
        experiment_version_id: str,
        request: paiabtest_20240119_models.PushAllExperimentVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.PushAllExperimentVersionResponse:
        """
        @summary 对实验版本推全
        
        @param request: PushAllExperimentVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushAllExperimentVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.feature_name):
            body['FeatureName'] = request.feature_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushAllExperimentVersion',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/experimentversions/{OpenApiUtilClient.get_encode_param(experiment_version_id)}/action/pushall',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.PushAllExperimentVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_all_experiment_version(
        self,
        experiment_version_id: str,
        request: paiabtest_20240119_models.PushAllExperimentVersionRequest,
    ) -> paiabtest_20240119_models.PushAllExperimentVersionResponse:
        """
        @summary 对实验版本推全
        
        @param request: PushAllExperimentVersionRequest
        @return: PushAllExperimentVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_all_experiment_version_with_options(experiment_version_id, request, headers, runtime)

    async def push_all_experiment_version_async(
        self,
        experiment_version_id: str,
        request: paiabtest_20240119_models.PushAllExperimentVersionRequest,
    ) -> paiabtest_20240119_models.PushAllExperimentVersionResponse:
        """
        @summary 对实验版本推全
        
        @param request: PushAllExperimentVersionRequest
        @return: PushAllExperimentVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.push_all_experiment_version_with_options_async(experiment_version_id, request, headers, runtime)

    def start_experiment_with_options(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.StartExperimentResponse:
        """
        @summary 启动实验
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartExperiment',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}/action/start',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.StartExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_experiment_with_options_async(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.StartExperimentResponse:
        """
        @summary 启动实验
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartExperiment',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}/action/start',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.StartExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_experiment(
        self,
        experiment_id: str,
    ) -> paiabtest_20240119_models.StartExperimentResponse:
        """
        @summary 启动实验
        
        @return: StartExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_experiment_with_options(experiment_id, headers, runtime)

    async def start_experiment_async(
        self,
        experiment_id: str,
    ) -> paiabtest_20240119_models.StartExperimentResponse:
        """
        @summary 启动实验
        
        @return: StartExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_experiment_with_options_async(experiment_id, headers, runtime)

    def stop_experiment_with_options(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.StopExperimentResponse:
        """
        @summary 停止实验
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopExperiment',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}/action/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.StopExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_experiment_with_options_async(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.StopExperimentResponse:
        """
        @summary 停止实验
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopExperiment',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}/action/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.StopExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_experiment(
        self,
        experiment_id: str,
    ) -> paiabtest_20240119_models.StopExperimentResponse:
        """
        @summary 停止实验
        
        @return: StopExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_experiment_with_options(experiment_id, headers, runtime)

    async def stop_experiment_async(
        self,
        experiment_id: str,
    ) -> paiabtest_20240119_models.StopExperimentResponse:
        """
        @summary 停止实验
        
        @return: StopExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_experiment_with_options_async(experiment_id, headers, runtime)

    def update_crowd_with_options(
        self,
        crowd_id: str,
        request: paiabtest_20240119_models.UpdateCrowdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.UpdateCrowdResponse:
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
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCrowd',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/crowds/{OpenApiUtilClient.get_encode_param(crowd_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.UpdateCrowdResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_crowd_with_options_async(
        self,
        crowd_id: str,
        request: paiabtest_20240119_models.UpdateCrowdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.UpdateCrowdResponse:
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
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCrowd',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/crowds/{OpenApiUtilClient.get_encode_param(crowd_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.UpdateCrowdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_crowd(
        self,
        crowd_id: str,
        request: paiabtest_20240119_models.UpdateCrowdRequest,
    ) -> paiabtest_20240119_models.UpdateCrowdResponse:
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
        request: paiabtest_20240119_models.UpdateCrowdRequest,
    ) -> paiabtest_20240119_models.UpdateCrowdResponse:
        """
        @summary 更新指定人群。
        
        @param request: UpdateCrowdRequest
        @return: UpdateCrowdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_crowd_with_options_async(crowd_id, request, headers, runtime)

    def update_domain_with_options(
        self,
        domain_id: str,
        request: paiabtest_20240119_models.UpdateDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.UpdateDomainResponse:
        """
        @summary 更新指定实验域
        
        @param request: UpdateDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDomainResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bucket_type):
            body['BucketType'] = request.bucket_type
        if not UtilClient.is_unset(request.condition):
            body['Condition'] = request.condition
        if not UtilClient.is_unset(request.crow_ids):
            body['CrowIds'] = request.crow_ids
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.flow):
            body['Flow'] = request.flow
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDomain',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/domains/{OpenApiUtilClient.get_encode_param(domain_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.UpdateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_domain_with_options_async(
        self,
        domain_id: str,
        request: paiabtest_20240119_models.UpdateDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.UpdateDomainResponse:
        """
        @summary 更新指定实验域
        
        @param request: UpdateDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDomainResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bucket_type):
            body['BucketType'] = request.bucket_type
        if not UtilClient.is_unset(request.condition):
            body['Condition'] = request.condition
        if not UtilClient.is_unset(request.crow_ids):
            body['CrowIds'] = request.crow_ids
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.flow):
            body['Flow'] = request.flow
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDomain',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/domains/{OpenApiUtilClient.get_encode_param(domain_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.UpdateDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_domain(
        self,
        domain_id: str,
        request: paiabtest_20240119_models.UpdateDomainRequest,
    ) -> paiabtest_20240119_models.UpdateDomainResponse:
        """
        @summary 更新指定实验域
        
        @param request: UpdateDomainRequest
        @return: UpdateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_domain_with_options(domain_id, request, headers, runtime)

    async def update_domain_async(
        self,
        domain_id: str,
        request: paiabtest_20240119_models.UpdateDomainRequest,
    ) -> paiabtest_20240119_models.UpdateDomainResponse:
        """
        @summary 更新指定实验域
        
        @param request: UpdateDomainRequest
        @return: UpdateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_domain_with_options_async(domain_id, request, headers, runtime)

    def update_experiment_with_options(
        self,
        experiment_id: str,
        request: paiabtest_20240119_models.UpdateExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.UpdateExperimentResponse:
        """
        @summary 更新指定的实验
        
        @param request: UpdateExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExperimentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bucket_type):
            body['BucketType'] = request.bucket_type
        if not UtilClient.is_unset(request.condition):
            body['Condition'] = request.condition
        if not UtilClient.is_unset(request.core_metric_id):
            body['CoreMetricId'] = request.core_metric_id
        if not UtilClient.is_unset(request.crowd_ids):
            body['CrowdIds'] = request.crowd_ids
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.flow):
            body['Flow'] = request.flow
        if not UtilClient.is_unset(request.focus_metric_ids):
            body['FocusMetricIds'] = request.focus_metric_ids
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateExperiment',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.UpdateExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_experiment_with_options_async(
        self,
        experiment_id: str,
        request: paiabtest_20240119_models.UpdateExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.UpdateExperimentResponse:
        """
        @summary 更新指定的实验
        
        @param request: UpdateExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExperimentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bucket_type):
            body['BucketType'] = request.bucket_type
        if not UtilClient.is_unset(request.condition):
            body['Condition'] = request.condition
        if not UtilClient.is_unset(request.core_metric_id):
            body['CoreMetricId'] = request.core_metric_id
        if not UtilClient.is_unset(request.crowd_ids):
            body['CrowdIds'] = request.crowd_ids
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.flow):
            body['Flow'] = request.flow
        if not UtilClient.is_unset(request.focus_metric_ids):
            body['FocusMetricIds'] = request.focus_metric_ids
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateExperiment',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/experiments/{OpenApiUtilClient.get_encode_param(experiment_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.UpdateExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_experiment(
        self,
        experiment_id: str,
        request: paiabtest_20240119_models.UpdateExperimentRequest,
    ) -> paiabtest_20240119_models.UpdateExperimentResponse:
        """
        @summary 更新指定的实验
        
        @param request: UpdateExperimentRequest
        @return: UpdateExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_experiment_with_options(experiment_id, request, headers, runtime)

    async def update_experiment_async(
        self,
        experiment_id: str,
        request: paiabtest_20240119_models.UpdateExperimentRequest,
    ) -> paiabtest_20240119_models.UpdateExperimentResponse:
        """
        @summary 更新指定的实验
        
        @param request: UpdateExperimentRequest
        @return: UpdateExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_experiment_with_options_async(experiment_id, request, headers, runtime)

    def update_experiment_version_with_options(
        self,
        experiment_version_id: str,
        request: paiabtest_20240119_models.UpdateExperimentVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.UpdateExperimentVersionResponse:
        """
        @summary 更新指定的实验版本
        
        @param request: UpdateExperimentVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExperimentVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.crowd_ids):
            body['CrowdIds'] = request.crowd_ids
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.flow):
            body['Flow'] = request.flow
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateExperimentVersion',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/experimentversions/{OpenApiUtilClient.get_encode_param(experiment_version_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.UpdateExperimentVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_experiment_version_with_options_async(
        self,
        experiment_version_id: str,
        request: paiabtest_20240119_models.UpdateExperimentVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.UpdateExperimentVersionResponse:
        """
        @summary 更新指定的实验版本
        
        @param request: UpdateExperimentVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExperimentVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.crowd_ids):
            body['CrowdIds'] = request.crowd_ids
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.flow):
            body['Flow'] = request.flow
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateExperimentVersion',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/experimentversions/{OpenApiUtilClient.get_encode_param(experiment_version_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.UpdateExperimentVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_experiment_version(
        self,
        experiment_version_id: str,
        request: paiabtest_20240119_models.UpdateExperimentVersionRequest,
    ) -> paiabtest_20240119_models.UpdateExperimentVersionResponse:
        """
        @summary 更新指定的实验版本
        
        @param request: UpdateExperimentVersionRequest
        @return: UpdateExperimentVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_experiment_version_with_options(experiment_version_id, request, headers, runtime)

    async def update_experiment_version_async(
        self,
        experiment_version_id: str,
        request: paiabtest_20240119_models.UpdateExperimentVersionRequest,
    ) -> paiabtest_20240119_models.UpdateExperimentVersionResponse:
        """
        @summary 更新指定的实验版本
        
        @param request: UpdateExperimentVersionRequest
        @return: UpdateExperimentVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_experiment_version_with_options_async(experiment_version_id, request, headers, runtime)

    def update_feature_with_options(
        self,
        feature_id: str,
        request: paiabtest_20240119_models.UpdateFeatureRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.UpdateFeatureResponse:
        """
        @summary 更新Feature
        
        @param request: UpdateFeatureRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFeatureResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFeature',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/features/{OpenApiUtilClient.get_encode_param(feature_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.UpdateFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_feature_with_options_async(
        self,
        feature_id: str,
        request: paiabtest_20240119_models.UpdateFeatureRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.UpdateFeatureResponse:
        """
        @summary 更新Feature
        
        @param request: UpdateFeatureRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFeatureResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFeature',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/features/{OpenApiUtilClient.get_encode_param(feature_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.UpdateFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_feature(
        self,
        feature_id: str,
        request: paiabtest_20240119_models.UpdateFeatureRequest,
    ) -> paiabtest_20240119_models.UpdateFeatureResponse:
        """
        @summary 更新Feature
        
        @param request: UpdateFeatureRequest
        @return: UpdateFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_feature_with_options(feature_id, request, headers, runtime)

    async def update_feature_async(
        self,
        feature_id: str,
        request: paiabtest_20240119_models.UpdateFeatureRequest,
    ) -> paiabtest_20240119_models.UpdateFeatureResponse:
        """
        @summary 更新Feature
        
        @param request: UpdateFeatureRequest
        @return: UpdateFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_feature_with_options_async(feature_id, request, headers, runtime)

    def update_layer_with_options(
        self,
        layer_id: str,
        request: paiabtest_20240119_models.UpdateLayerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.UpdateLayerResponse:
        """
        @summary 更新指定的实验层
        
        @param request: UpdateLayerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLayerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.domain_id):
            body['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLayer',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/layers/{OpenApiUtilClient.get_encode_param(layer_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.UpdateLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_layer_with_options_async(
        self,
        layer_id: str,
        request: paiabtest_20240119_models.UpdateLayerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.UpdateLayerResponse:
        """
        @summary 更新指定的实验层
        
        @param request: UpdateLayerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLayerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.domain_id):
            body['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLayer',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/layers/{OpenApiUtilClient.get_encode_param(layer_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.UpdateLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_layer(
        self,
        layer_id: str,
        request: paiabtest_20240119_models.UpdateLayerRequest,
    ) -> paiabtest_20240119_models.UpdateLayerResponse:
        """
        @summary 更新指定的实验层
        
        @param request: UpdateLayerRequest
        @return: UpdateLayerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_layer_with_options(layer_id, request, headers, runtime)

    async def update_layer_async(
        self,
        layer_id: str,
        request: paiabtest_20240119_models.UpdateLayerRequest,
    ) -> paiabtest_20240119_models.UpdateLayerResponse:
        """
        @summary 更新指定的实验层
        
        @param request: UpdateLayerRequest
        @return: UpdateLayerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_layer_with_options_async(layer_id, request, headers, runtime)

    def update_metric_with_options(
        self,
        metric_id: str,
        request: paiabtest_20240119_models.UpdateMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.UpdateMetricResponse:
        """
        @summary 更新指标
        
        @param request: UpdateMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMetricResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.definition):
            body['Definition'] = request.definition
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.source_table_meta_id):
            body['SourceTableMetaId'] = request.source_table_meta_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMetric',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/metrics/{OpenApiUtilClient.get_encode_param(metric_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.UpdateMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_metric_with_options_async(
        self,
        metric_id: str,
        request: paiabtest_20240119_models.UpdateMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.UpdateMetricResponse:
        """
        @summary 更新指标
        
        @param request: UpdateMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMetricResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.definition):
            body['Definition'] = request.definition
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.source_table_meta_id):
            body['SourceTableMetaId'] = request.source_table_meta_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMetric',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/metrics/{OpenApiUtilClient.get_encode_param(metric_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.UpdateMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_metric(
        self,
        metric_id: str,
        request: paiabtest_20240119_models.UpdateMetricRequest,
    ) -> paiabtest_20240119_models.UpdateMetricResponse:
        """
        @summary 更新指标
        
        @param request: UpdateMetricRequest
        @return: UpdateMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_metric_with_options(metric_id, request, headers, runtime)

    async def update_metric_async(
        self,
        metric_id: str,
        request: paiabtest_20240119_models.UpdateMetricRequest,
    ) -> paiabtest_20240119_models.UpdateMetricResponse:
        """
        @summary 更新指标
        
        @param request: UpdateMetricRequest
        @return: UpdateMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_metric_with_options_async(metric_id, request, headers, runtime)

    def update_metric_group_with_options(
        self,
        metric_group_id: str,
        request: paiabtest_20240119_models.UpdateMetricGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.UpdateMetricGroupResponse:
        """
        @summary 更新指定的指标组
        
        @param request: UpdateMetricGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMetricGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMetricGroup',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/metricgroups/{OpenApiUtilClient.get_encode_param(metric_group_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.UpdateMetricGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_metric_group_with_options_async(
        self,
        metric_group_id: str,
        request: paiabtest_20240119_models.UpdateMetricGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.UpdateMetricGroupResponse:
        """
        @summary 更新指定的指标组
        
        @param request: UpdateMetricGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMetricGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMetricGroup',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/metricgroups/{OpenApiUtilClient.get_encode_param(metric_group_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.UpdateMetricGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_metric_group(
        self,
        metric_group_id: str,
        request: paiabtest_20240119_models.UpdateMetricGroupRequest,
    ) -> paiabtest_20240119_models.UpdateMetricGroupResponse:
        """
        @summary 更新指定的指标组
        
        @param request: UpdateMetricGroupRequest
        @return: UpdateMetricGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_metric_group_with_options(metric_group_id, request, headers, runtime)

    async def update_metric_group_async(
        self,
        metric_group_id: str,
        request: paiabtest_20240119_models.UpdateMetricGroupRequest,
    ) -> paiabtest_20240119_models.UpdateMetricGroupResponse:
        """
        @summary 更新指定的指标组
        
        @param request: UpdateMetricGroupRequest
        @return: UpdateMetricGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_metric_group_with_options_async(metric_group_id, request, headers, runtime)

    def update_project_with_options(
        self,
        project_id: str,
        request: paiabtest_20240119_models.UpdateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.UpdateProjectResponse:
        """
        @summary 更新指定的实验项目
        
        @param request: UpdateProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.UpdateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_with_options_async(
        self,
        project_id: str,
        request: paiabtest_20240119_models.UpdateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.UpdateProjectResponse:
        """
        @summary 更新指定的实验项目
        
        @param request: UpdateProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.UpdateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project(
        self,
        project_id: str,
        request: paiabtest_20240119_models.UpdateProjectRequest,
    ) -> paiabtest_20240119_models.UpdateProjectResponse:
        """
        @summary 更新指定的实验项目
        
        @param request: UpdateProjectRequest
        @return: UpdateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_project_with_options(project_id, request, headers, runtime)

    async def update_project_async(
        self,
        project_id: str,
        request: paiabtest_20240119_models.UpdateProjectRequest,
    ) -> paiabtest_20240119_models.UpdateProjectResponse:
        """
        @summary 更新指定的实验项目
        
        @param request: UpdateProjectRequest
        @return: UpdateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_project_with_options_async(project_id, request, headers, runtime)

    def update_table_meta_with_options(
        self,
        table_meta_id: str,
        request: paiabtest_20240119_models.UpdateTableMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.UpdateTableMetaResponse:
        """
        @summary 更新数据表
        
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
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTableMeta',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/tablemetas/{OpenApiUtilClient.get_encode_param(table_meta_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.UpdateTableMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_table_meta_with_options_async(
        self,
        table_meta_id: str,
        request: paiabtest_20240119_models.UpdateTableMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paiabtest_20240119_models.UpdateTableMetaResponse:
        """
        @summary 更新数据表
        
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
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTableMeta',
            version='2024-01-19',
            protocol='HTTPS',
            pathname=f'/api/v1/tablemetas/{OpenApiUtilClient.get_encode_param(table_meta_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paiabtest_20240119_models.UpdateTableMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_table_meta(
        self,
        table_meta_id: str,
        request: paiabtest_20240119_models.UpdateTableMetaRequest,
    ) -> paiabtest_20240119_models.UpdateTableMetaResponse:
        """
        @summary 更新数据表
        
        @param request: UpdateTableMetaRequest
        @return: UpdateTableMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_table_meta_with_options(table_meta_id, request, headers, runtime)

    async def update_table_meta_async(
        self,
        table_meta_id: str,
        request: paiabtest_20240119_models.UpdateTableMetaRequest,
    ) -> paiabtest_20240119_models.UpdateTableMetaResponse:
        """
        @summary 更新数据表
        
        @param request: UpdateTableMetaRequest
        @return: UpdateTableMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_table_meta_with_options_async(table_meta_id, request, headers, runtime)
