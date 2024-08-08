# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_paiautoml20220828 import models as pai_auto_ml20220828_models
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
        self._endpoint = self.get_endpoint('paiautoml', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_autofe_experiment_with_options(
        self,
        request: pai_auto_ml20220828_models.CreateAutofeExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.CreateAutofeExperimentResponse:
        """
        @summary CreateAutofeExperiment
        
        @param request: CreateAutofeExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAutofeExperimentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.autofe_experiment_configuration):
            body['AutofeExperimentConfiguration'] = request.autofe_experiment_configuration
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
            action='CreateAutofeExperiment',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/autofe/experiment',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.CreateAutofeExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_autofe_experiment_with_options_async(
        self,
        request: pai_auto_ml20220828_models.CreateAutofeExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.CreateAutofeExperimentResponse:
        """
        @summary CreateAutofeExperiment
        
        @param request: CreateAutofeExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAutofeExperimentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.autofe_experiment_configuration):
            body['AutofeExperimentConfiguration'] = request.autofe_experiment_configuration
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
            action='CreateAutofeExperiment',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/autofe/experiment',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.CreateAutofeExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_autofe_experiment(
        self,
        request: pai_auto_ml20220828_models.CreateAutofeExperimentRequest,
    ) -> pai_auto_ml20220828_models.CreateAutofeExperimentResponse:
        """
        @summary CreateAutofeExperiment
        
        @param request: CreateAutofeExperimentRequest
        @return: CreateAutofeExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_autofe_experiment_with_options(request, headers, runtime)

    async def create_autofe_experiment_async(
        self,
        request: pai_auto_ml20220828_models.CreateAutofeExperimentRequest,
    ) -> pai_auto_ml20220828_models.CreateAutofeExperimentResponse:
        """
        @summary CreateAutofeExperiment
        
        @param request: CreateAutofeExperimentRequest
        @return: CreateAutofeExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_autofe_experiment_with_options_async(request, headers, runtime)

    def create_hpo_experiment_with_options(
        self,
        request: pai_auto_ml20220828_models.CreateHpoExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.CreateHpoExperimentResponse:
        """
        @summary Create an HyperParameter Optimization experiment.
        
        @param request: CreateHpoExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHpoExperimentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.hpo_experiment_configuration):
            body['HpoExperimentConfiguration'] = request.hpo_experiment_configuration
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHpoExperiment',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/hpo/experiment',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.CreateHpoExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_hpo_experiment_with_options_async(
        self,
        request: pai_auto_ml20220828_models.CreateHpoExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.CreateHpoExperimentResponse:
        """
        @summary Create an HyperParameter Optimization experiment.
        
        @param request: CreateHpoExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHpoExperimentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.hpo_experiment_configuration):
            body['HpoExperimentConfiguration'] = request.hpo_experiment_configuration
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHpoExperiment',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/hpo/experiment',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.CreateHpoExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_hpo_experiment(
        self,
        request: pai_auto_ml20220828_models.CreateHpoExperimentRequest,
    ) -> pai_auto_ml20220828_models.CreateHpoExperimentResponse:
        """
        @summary Create an HyperParameter Optimization experiment.
        
        @param request: CreateHpoExperimentRequest
        @return: CreateHpoExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_hpo_experiment_with_options(request, headers, runtime)

    async def create_hpo_experiment_async(
        self,
        request: pai_auto_ml20220828_models.CreateHpoExperimentRequest,
    ) -> pai_auto_ml20220828_models.CreateHpoExperimentResponse:
        """
        @summary Create an HyperParameter Optimization experiment.
        
        @param request: CreateHpoExperimentRequest
        @return: CreateHpoExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_hpo_experiment_with_options_async(request, headers, runtime)

    def create_service_identity_role_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.CreateServiceIdentityRoleResponse:
        """
        @summary CreateServiceIdentityRole
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceIdentityRoleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateServiceIdentityRole',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/serviceidentityrole',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.CreateServiceIdentityRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_identity_role_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.CreateServiceIdentityRoleResponse:
        """
        @summary CreateServiceIdentityRole
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceIdentityRoleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateServiceIdentityRole',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/serviceidentityrole',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.CreateServiceIdentityRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_identity_role(self) -> pai_auto_ml20220828_models.CreateServiceIdentityRoleResponse:
        """
        @summary CreateServiceIdentityRole
        
        @return: CreateServiceIdentityRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_identity_role_with_options(headers, runtime)

    async def create_service_identity_role_async(self) -> pai_auto_ml20220828_models.CreateServiceIdentityRoleResponse:
        """
        @summary CreateServiceIdentityRole
        
        @return: CreateServiceIdentityRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_service_identity_role_with_options_async(headers, runtime)

    def delete_hpo_experiment_with_options(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.DeleteHpoExperimentResponse:
        """
        @summary Delete an HPO experiment
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHpoExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteHpoExperiment',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/hpo/experiment/{OpenApiUtilClient.get_encode_param(experiment_id)}/delete',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.DeleteHpoExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hpo_experiment_with_options_async(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.DeleteHpoExperimentResponse:
        """
        @summary Delete an HPO experiment
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHpoExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteHpoExperiment',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/hpo/experiment/{OpenApiUtilClient.get_encode_param(experiment_id)}/delete',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.DeleteHpoExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hpo_experiment(
        self,
        experiment_id: str,
    ) -> pai_auto_ml20220828_models.DeleteHpoExperimentResponse:
        """
        @summary Delete an HPO experiment
        
        @return: DeleteHpoExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_hpo_experiment_with_options(experiment_id, headers, runtime)

    async def delete_hpo_experiment_async(
        self,
        experiment_id: str,
    ) -> pai_auto_ml20220828_models.DeleteHpoExperimentResponse:
        """
        @summary Delete an HPO experiment
        
        @return: DeleteHpoExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_hpo_experiment_with_options_async(experiment_id, headers, runtime)

    def get_autofe_experiment_with_options(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.GetAutofeExperimentResponse:
        """
        @summary Get AutoFE Experiment。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAutofeExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAutofeExperiment',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/autofe/experiment/{OpenApiUtilClient.get_encode_param(experiment_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.GetAutofeExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_autofe_experiment_with_options_async(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.GetAutofeExperimentResponse:
        """
        @summary Get AutoFE Experiment。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAutofeExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAutofeExperiment',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/autofe/experiment/{OpenApiUtilClient.get_encode_param(experiment_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.GetAutofeExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_autofe_experiment(
        self,
        experiment_id: str,
    ) -> pai_auto_ml20220828_models.GetAutofeExperimentResponse:
        """
        @summary Get AutoFE Experiment。
        
        @return: GetAutofeExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_autofe_experiment_with_options(experiment_id, headers, runtime)

    async def get_autofe_experiment_async(
        self,
        experiment_id: str,
    ) -> pai_auto_ml20220828_models.GetAutofeExperimentResponse:
        """
        @summary Get AutoFE Experiment。
        
        @return: GetAutofeExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_autofe_experiment_with_options_async(experiment_id, headers, runtime)

    def get_hpo_experiment_with_options(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.GetHpoExperimentResponse:
        """
        @summary get hpo experiment by user id and exp id
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHpoExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetHpoExperiment',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/hpo/experiment/{OpenApiUtilClient.get_encode_param(experiment_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.GetHpoExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hpo_experiment_with_options_async(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.GetHpoExperimentResponse:
        """
        @summary get hpo experiment by user id and exp id
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHpoExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetHpoExperiment',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/hpo/experiment/{OpenApiUtilClient.get_encode_param(experiment_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.GetHpoExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hpo_experiment(
        self,
        experiment_id: str,
    ) -> pai_auto_ml20220828_models.GetHpoExperimentResponse:
        """
        @summary get hpo experiment by user id and exp id
        
        @return: GetHpoExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_hpo_experiment_with_options(experiment_id, headers, runtime)

    async def get_hpo_experiment_async(
        self,
        experiment_id: str,
    ) -> pai_auto_ml20220828_models.GetHpoExperimentResponse:
        """
        @summary get hpo experiment by user id and exp id
        
        @return: GetHpoExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_hpo_experiment_with_options_async(experiment_id, headers, runtime)

    def get_hpo_trial_with_options(
        self,
        experiment_id: str,
        trial_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.GetHpoTrialResponse:
        """
        @summary Get trial detail information
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHpoTrialResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetHpoTrial',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/hpo/experiment/{OpenApiUtilClient.get_encode_param(experiment_id)}/trial/{OpenApiUtilClient.get_encode_param(trial_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.GetHpoTrialResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hpo_trial_with_options_async(
        self,
        experiment_id: str,
        trial_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.GetHpoTrialResponse:
        """
        @summary Get trial detail information
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHpoTrialResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetHpoTrial',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/hpo/experiment/{OpenApiUtilClient.get_encode_param(experiment_id)}/trial/{OpenApiUtilClient.get_encode_param(trial_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.GetHpoTrialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hpo_trial(
        self,
        experiment_id: str,
        trial_id: str,
    ) -> pai_auto_ml20220828_models.GetHpoTrialResponse:
        """
        @summary Get trial detail information
        
        @return: GetHpoTrialResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_hpo_trial_with_options(experiment_id, trial_id, headers, runtime)

    async def get_hpo_trial_async(
        self,
        experiment_id: str,
        trial_id: str,
    ) -> pai_auto_ml20220828_models.GetHpoTrialResponse:
        """
        @summary Get trial detail information
        
        @return: GetHpoTrialResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_hpo_trial_with_options_async(experiment_id, trial_id, headers, runtime)

    def get_service_identity_role_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.GetServiceIdentityRoleResponse:
        """
        @summary GetServiceIdentityRole, return role name if SLR exists, empty otherwise
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceIdentityRoleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetServiceIdentityRole',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/serviceidentityrole',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.GetServiceIdentityRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_identity_role_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.GetServiceIdentityRoleResponse:
        """
        @summary GetServiceIdentityRole, return role name if SLR exists, empty otherwise
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceIdentityRoleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetServiceIdentityRole',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/serviceidentityrole',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.GetServiceIdentityRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_identity_role(self) -> pai_auto_ml20220828_models.GetServiceIdentityRoleResponse:
        """
        @summary GetServiceIdentityRole, return role name if SLR exists, empty otherwise
        
        @return: GetServiceIdentityRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_identity_role_with_options(headers, runtime)

    async def get_service_identity_role_async(self) -> pai_auto_ml20220828_models.GetServiceIdentityRoleResponse:
        """
        @summary GetServiceIdentityRole, return role name if SLR exists, empty otherwise
        
        @return: GetServiceIdentityRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_service_identity_role_with_options_async(headers, runtime)

    def list_hpo_experiment_logs_with_options(
        self,
        experiment_id: str,
        request: pai_auto_ml20220828_models.ListHpoExperimentLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.ListHpoExperimentLogsResponse:
        """
        @summary list the content of a specified hpo experiment log
        
        @param request: ListHpoExperimentLogsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHpoExperimentLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_name):
            query['LogName'] = request.log_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHpoExperimentLogs',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/hpo/experiment/{OpenApiUtilClient.get_encode_param(experiment_id)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.ListHpoExperimentLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hpo_experiment_logs_with_options_async(
        self,
        experiment_id: str,
        request: pai_auto_ml20220828_models.ListHpoExperimentLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.ListHpoExperimentLogsResponse:
        """
        @summary list the content of a specified hpo experiment log
        
        @param request: ListHpoExperimentLogsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHpoExperimentLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_name):
            query['LogName'] = request.log_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHpoExperimentLogs',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/hpo/experiment/{OpenApiUtilClient.get_encode_param(experiment_id)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.ListHpoExperimentLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hpo_experiment_logs(
        self,
        experiment_id: str,
        request: pai_auto_ml20220828_models.ListHpoExperimentLogsRequest,
    ) -> pai_auto_ml20220828_models.ListHpoExperimentLogsResponse:
        """
        @summary list the content of a specified hpo experiment log
        
        @param request: ListHpoExperimentLogsRequest
        @return: ListHpoExperimentLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_hpo_experiment_logs_with_options(experiment_id, request, headers, runtime)

    async def list_hpo_experiment_logs_async(
        self,
        experiment_id: str,
        request: pai_auto_ml20220828_models.ListHpoExperimentLogsRequest,
    ) -> pai_auto_ml20220828_models.ListHpoExperimentLogsResponse:
        """
        @summary list the content of a specified hpo experiment log
        
        @param request: ListHpoExperimentLogsRequest
        @return: ListHpoExperimentLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_hpo_experiment_logs_with_options_async(experiment_id, request, headers, runtime)

    def list_hpo_experiments_with_options(
        self,
        request: pai_auto_ml20220828_models.ListHpoExperimentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.ListHpoExperimentsResponse:
        """
        @summary List HPO experiments
        
        @param request: ListHpoExperimentsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHpoExperimentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accessibility):
            query['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.creator):
            query['Creator'] = request.creator
        if not UtilClient.is_unset(request.include_config_data):
            query['IncludeConfigData'] = request.include_config_data
        if not UtilClient.is_unset(request.max_create_time):
            query['MaxCreateTime'] = request.max_create_time
        if not UtilClient.is_unset(request.min_create_time):
            query['MinCreateTime'] = request.min_create_time
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
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
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHpoExperiments',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/hpo/experiments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.ListHpoExperimentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hpo_experiments_with_options_async(
        self,
        request: pai_auto_ml20220828_models.ListHpoExperimentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.ListHpoExperimentsResponse:
        """
        @summary List HPO experiments
        
        @param request: ListHpoExperimentsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHpoExperimentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accessibility):
            query['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.creator):
            query['Creator'] = request.creator
        if not UtilClient.is_unset(request.include_config_data):
            query['IncludeConfigData'] = request.include_config_data
        if not UtilClient.is_unset(request.max_create_time):
            query['MaxCreateTime'] = request.max_create_time
        if not UtilClient.is_unset(request.min_create_time):
            query['MinCreateTime'] = request.min_create_time
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
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
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHpoExperiments',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/hpo/experiments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.ListHpoExperimentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hpo_experiments(
        self,
        request: pai_auto_ml20220828_models.ListHpoExperimentsRequest,
    ) -> pai_auto_ml20220828_models.ListHpoExperimentsResponse:
        """
        @summary List HPO experiments
        
        @param request: ListHpoExperimentsRequest
        @return: ListHpoExperimentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_hpo_experiments_with_options(request, headers, runtime)

    async def list_hpo_experiments_async(
        self,
        request: pai_auto_ml20220828_models.ListHpoExperimentsRequest,
    ) -> pai_auto_ml20220828_models.ListHpoExperimentsResponse:
        """
        @summary List HPO experiments
        
        @param request: ListHpoExperimentsRequest
        @return: ListHpoExperimentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_hpo_experiments_with_options_async(request, headers, runtime)

    def list_hpo_trial_commands_with_options(
        self,
        experiment_id: str,
        trial_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.ListHpoTrialCommandsResponse:
        """
        @summary 返回一个trial所对应的任务里所有已经执行的命令
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHpoTrialCommandsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListHpoTrialCommands',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/hpo/experiment/{OpenApiUtilClient.get_encode_param(experiment_id)}/trial/{OpenApiUtilClient.get_encode_param(trial_id)}/commands',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.ListHpoTrialCommandsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hpo_trial_commands_with_options_async(
        self,
        experiment_id: str,
        trial_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.ListHpoTrialCommandsResponse:
        """
        @summary 返回一个trial所对应的任务里所有已经执行的命令
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHpoTrialCommandsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListHpoTrialCommands',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/hpo/experiment/{OpenApiUtilClient.get_encode_param(experiment_id)}/trial/{OpenApiUtilClient.get_encode_param(trial_id)}/commands',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.ListHpoTrialCommandsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hpo_trial_commands(
        self,
        experiment_id: str,
        trial_id: str,
    ) -> pai_auto_ml20220828_models.ListHpoTrialCommandsResponse:
        """
        @summary 返回一个trial所对应的任务里所有已经执行的命令
        
        @return: ListHpoTrialCommandsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_hpo_trial_commands_with_options(experiment_id, trial_id, headers, runtime)

    async def list_hpo_trial_commands_async(
        self,
        experiment_id: str,
        trial_id: str,
    ) -> pai_auto_ml20220828_models.ListHpoTrialCommandsResponse:
        """
        @summary 返回一个trial所对应的任务里所有已经执行的命令
        
        @return: ListHpoTrialCommandsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_hpo_trial_commands_with_options_async(experiment_id, trial_id, headers, runtime)

    def list_hpo_trial_log_names_with_options(
        self,
        experiment_id: str,
        trial_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.ListHpoTrialLogNamesResponse:
        """
        @summary List all log file names a trial have.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHpoTrialLogNamesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListHpoTrialLogNames',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/hpo/experiment/{OpenApiUtilClient.get_encode_param(experiment_id)}/trial/{OpenApiUtilClient.get_encode_param(trial_id)}/lognames',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.ListHpoTrialLogNamesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hpo_trial_log_names_with_options_async(
        self,
        experiment_id: str,
        trial_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.ListHpoTrialLogNamesResponse:
        """
        @summary List all log file names a trial have.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHpoTrialLogNamesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListHpoTrialLogNames',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/hpo/experiment/{OpenApiUtilClient.get_encode_param(experiment_id)}/trial/{OpenApiUtilClient.get_encode_param(trial_id)}/lognames',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.ListHpoTrialLogNamesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hpo_trial_log_names(
        self,
        experiment_id: str,
        trial_id: str,
    ) -> pai_auto_ml20220828_models.ListHpoTrialLogNamesResponse:
        """
        @summary List all log file names a trial have.
        
        @return: ListHpoTrialLogNamesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_hpo_trial_log_names_with_options(experiment_id, trial_id, headers, runtime)

    async def list_hpo_trial_log_names_async(
        self,
        experiment_id: str,
        trial_id: str,
    ) -> pai_auto_ml20220828_models.ListHpoTrialLogNamesResponse:
        """
        @summary List all log file names a trial have.
        
        @return: ListHpoTrialLogNamesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_hpo_trial_log_names_with_options_async(experiment_id, trial_id, headers, runtime)

    def list_hpo_trial_logs_with_options(
        self,
        experiment_id: str,
        trial_id: str,
        request: pai_auto_ml20220828_models.ListHpoTrialLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.ListHpoTrialLogsResponse:
        """
        @summary List Trial log lines
        
        @param request: ListHpoTrialLogsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHpoTrialLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_name):
            query['LogName'] = request.log_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHpoTrialLogs',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/hpo/experiment/{OpenApiUtilClient.get_encode_param(experiment_id)}/trial/{OpenApiUtilClient.get_encode_param(trial_id)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.ListHpoTrialLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hpo_trial_logs_with_options_async(
        self,
        experiment_id: str,
        trial_id: str,
        request: pai_auto_ml20220828_models.ListHpoTrialLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.ListHpoTrialLogsResponse:
        """
        @summary List Trial log lines
        
        @param request: ListHpoTrialLogsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHpoTrialLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_name):
            query['LogName'] = request.log_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHpoTrialLogs',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/hpo/experiment/{OpenApiUtilClient.get_encode_param(experiment_id)}/trial/{OpenApiUtilClient.get_encode_param(trial_id)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.ListHpoTrialLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hpo_trial_logs(
        self,
        experiment_id: str,
        trial_id: str,
        request: pai_auto_ml20220828_models.ListHpoTrialLogsRequest,
    ) -> pai_auto_ml20220828_models.ListHpoTrialLogsResponse:
        """
        @summary List Trial log lines
        
        @param request: ListHpoTrialLogsRequest
        @return: ListHpoTrialLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_hpo_trial_logs_with_options(experiment_id, trial_id, request, headers, runtime)

    async def list_hpo_trial_logs_async(
        self,
        experiment_id: str,
        trial_id: str,
        request: pai_auto_ml20220828_models.ListHpoTrialLogsRequest,
    ) -> pai_auto_ml20220828_models.ListHpoTrialLogsResponse:
        """
        @summary List Trial log lines
        
        @param request: ListHpoTrialLogsRequest
        @return: ListHpoTrialLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_hpo_trial_logs_with_options_async(experiment_id, trial_id, request, headers, runtime)

    def list_hpo_trials_with_options(
        self,
        experiment_id: str,
        request: pai_auto_ml20220828_models.ListHpoTrialsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.ListHpoTrialsResponse:
        """
        @summary List HPO trials
        
        @param request: ListHpoTrialsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHpoTrialsResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='ListHpoTrials',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/hpo/experiment/{OpenApiUtilClient.get_encode_param(experiment_id)}/trials',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.ListHpoTrialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hpo_trials_with_options_async(
        self,
        experiment_id: str,
        request: pai_auto_ml20220828_models.ListHpoTrialsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.ListHpoTrialsResponse:
        """
        @summary List HPO trials
        
        @param request: ListHpoTrialsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHpoTrialsResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='ListHpoTrials',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/hpo/experiment/{OpenApiUtilClient.get_encode_param(experiment_id)}/trials',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.ListHpoTrialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hpo_trials(
        self,
        experiment_id: str,
        request: pai_auto_ml20220828_models.ListHpoTrialsRequest,
    ) -> pai_auto_ml20220828_models.ListHpoTrialsResponse:
        """
        @summary List HPO trials
        
        @param request: ListHpoTrialsRequest
        @return: ListHpoTrialsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_hpo_trials_with_options(experiment_id, request, headers, runtime)

    async def list_hpo_trials_async(
        self,
        experiment_id: str,
        request: pai_auto_ml20220828_models.ListHpoTrialsRequest,
    ) -> pai_auto_ml20220828_models.ListHpoTrialsResponse:
        """
        @summary List HPO trials
        
        @param request: ListHpoTrialsRequest
        @return: ListHpoTrialsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_hpo_trials_with_options_async(experiment_id, request, headers, runtime)

    def restart_hpo_trials_with_options(
        self,
        experiment_id: str,
        request: pai_auto_ml20220828_models.RestartHpoTrialsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.RestartHpoTrialsResponse:
        """
        @summary Restart HPO trials
        
        @param request: RestartHpoTrialsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartHpoTrialsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.trial_hyper_parameters):
            body['TrialHyperParameters'] = request.trial_hyper_parameters
        if not UtilClient.is_unset(request.trial_ids):
            body['TrialIds'] = request.trial_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RestartHpoTrials',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/hpo/experiment/{OpenApiUtilClient.get_encode_param(experiment_id)}/restart_trials',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.RestartHpoTrialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_hpo_trials_with_options_async(
        self,
        experiment_id: str,
        request: pai_auto_ml20220828_models.RestartHpoTrialsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.RestartHpoTrialsResponse:
        """
        @summary Restart HPO trials
        
        @param request: RestartHpoTrialsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartHpoTrialsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.trial_hyper_parameters):
            body['TrialHyperParameters'] = request.trial_hyper_parameters
        if not UtilClient.is_unset(request.trial_ids):
            body['TrialIds'] = request.trial_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RestartHpoTrials',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/hpo/experiment/{OpenApiUtilClient.get_encode_param(experiment_id)}/restart_trials',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.RestartHpoTrialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_hpo_trials(
        self,
        experiment_id: str,
        request: pai_auto_ml20220828_models.RestartHpoTrialsRequest,
    ) -> pai_auto_ml20220828_models.RestartHpoTrialsResponse:
        """
        @summary Restart HPO trials
        
        @param request: RestartHpoTrialsRequest
        @return: RestartHpoTrialsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restart_hpo_trials_with_options(experiment_id, request, headers, runtime)

    async def restart_hpo_trials_async(
        self,
        experiment_id: str,
        request: pai_auto_ml20220828_models.RestartHpoTrialsRequest,
    ) -> pai_auto_ml20220828_models.RestartHpoTrialsResponse:
        """
        @summary Restart HPO trials
        
        @param request: RestartHpoTrialsRequest
        @return: RestartHpoTrialsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.restart_hpo_trials_with_options_async(experiment_id, request, headers, runtime)

    def stop_hpo_experiment_with_options(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.StopHpoExperimentResponse:
        """
        @summary calling hpo StopExperiment
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopHpoExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopHpoExperiment',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/hpo/experiment/{OpenApiUtilClient.get_encode_param(experiment_id)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.StopHpoExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_hpo_experiment_with_options_async(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.StopHpoExperimentResponse:
        """
        @summary calling hpo StopExperiment
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopHpoExperimentResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopHpoExperiment',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/hpo/experiment/{OpenApiUtilClient.get_encode_param(experiment_id)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.StopHpoExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_hpo_experiment(
        self,
        experiment_id: str,
    ) -> pai_auto_ml20220828_models.StopHpoExperimentResponse:
        """
        @summary calling hpo StopExperiment
        
        @return: StopHpoExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_hpo_experiment_with_options(experiment_id, headers, runtime)

    async def stop_hpo_experiment_async(
        self,
        experiment_id: str,
    ) -> pai_auto_ml20220828_models.StopHpoExperimentResponse:
        """
        @summary calling hpo StopExperiment
        
        @return: StopHpoExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_hpo_experiment_with_options_async(experiment_id, headers, runtime)

    def stop_hpo_trials_with_options(
        self,
        experiment_id: str,
        request: pai_auto_ml20220828_models.StopHpoTrialsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.StopHpoTrialsResponse:
        """
        @summary Stop an HPO trial.
        
        @param request: StopHpoTrialsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopHpoTrialsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.trial_ids):
            body['TrialIds'] = request.trial_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopHpoTrials',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/hpo/experiment/{OpenApiUtilClient.get_encode_param(experiment_id)}/stop_trials',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.StopHpoTrialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_hpo_trials_with_options_async(
        self,
        experiment_id: str,
        request: pai_auto_ml20220828_models.StopHpoTrialsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.StopHpoTrialsResponse:
        """
        @summary Stop an HPO trial.
        
        @param request: StopHpoTrialsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopHpoTrialsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.trial_ids):
            body['TrialIds'] = request.trial_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopHpoTrials',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/hpo/experiment/{OpenApiUtilClient.get_encode_param(experiment_id)}/stop_trials',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.StopHpoTrialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_hpo_trials(
        self,
        experiment_id: str,
        request: pai_auto_ml20220828_models.StopHpoTrialsRequest,
    ) -> pai_auto_ml20220828_models.StopHpoTrialsResponse:
        """
        @summary Stop an HPO trial.
        
        @param request: StopHpoTrialsRequest
        @return: StopHpoTrialsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_hpo_trials_with_options(experiment_id, request, headers, runtime)

    async def stop_hpo_trials_async(
        self,
        experiment_id: str,
        request: pai_auto_ml20220828_models.StopHpoTrialsRequest,
    ) -> pai_auto_ml20220828_models.StopHpoTrialsResponse:
        """
        @summary Stop an HPO trial.
        
        @param request: StopHpoTrialsRequest
        @return: StopHpoTrialsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_hpo_trials_with_options_async(experiment_id, request, headers, runtime)

    def update_hpo_experiment_with_options(
        self,
        experiment_id: str,
        request: pai_auto_ml20220828_models.UpdateHpoExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.UpdateHpoExperimentResponse:
        """
        @summary Update a running HPO experiment\\"s configuration
        
        @param request: UpdateHpoExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHpoExperimentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.hpo_experiment_configuration):
            body['HpoExperimentConfiguration'] = request.hpo_experiment_configuration
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHpoExperiment',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/hpo/experiment/{OpenApiUtilClient.get_encode_param(experiment_id)}/update',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.UpdateHpoExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_hpo_experiment_with_options_async(
        self,
        experiment_id: str,
        request: pai_auto_ml20220828_models.UpdateHpoExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.UpdateHpoExperimentResponse:
        """
        @summary Update a running HPO experiment\\"s configuration
        
        @param request: UpdateHpoExperimentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHpoExperimentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.hpo_experiment_configuration):
            body['HpoExperimentConfiguration'] = request.hpo_experiment_configuration
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHpoExperiment',
            version='2022-08-28',
            protocol='HTTPS',
            pathname=f'/api/automl/v1/hpo/experiment/{OpenApiUtilClient.get_encode_param(experiment_id)}/update',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.UpdateHpoExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_hpo_experiment(
        self,
        experiment_id: str,
        request: pai_auto_ml20220828_models.UpdateHpoExperimentRequest,
    ) -> pai_auto_ml20220828_models.UpdateHpoExperimentResponse:
        """
        @summary Update a running HPO experiment\\"s configuration
        
        @param request: UpdateHpoExperimentRequest
        @return: UpdateHpoExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_hpo_experiment_with_options(experiment_id, request, headers, runtime)

    async def update_hpo_experiment_async(
        self,
        experiment_id: str,
        request: pai_auto_ml20220828_models.UpdateHpoExperimentRequest,
    ) -> pai_auto_ml20220828_models.UpdateHpoExperimentResponse:
        """
        @summary Update a running HPO experiment\\"s configuration
        
        @param request: UpdateHpoExperimentRequest
        @return: UpdateHpoExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_hpo_experiment_with_options_async(experiment_id, request, headers, runtime)
