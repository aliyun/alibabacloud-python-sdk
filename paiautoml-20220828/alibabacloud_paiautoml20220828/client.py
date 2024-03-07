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

    def create_hpo_experiment_with_options(
        self,
        request: pai_auto_ml20220828_models.CreateHpoExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.CreateHpoExperimentResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_hpo_experiment_with_options(request, headers, runtime)

    async def create_hpo_experiment_async(
        self,
        request: pai_auto_ml20220828_models.CreateHpoExperimentRequest,
    ) -> pai_auto_ml20220828_models.CreateHpoExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_hpo_experiment_with_options_async(request, headers, runtime)

    def list_hpo_experiments_with_options(
        self,
        request: pai_auto_ml20220828_models.ListHpoExperimentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_auto_ml20220828_models.ListHpoExperimentsResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_hpo_experiments_with_options(request, headers, runtime)

    async def list_hpo_experiments_async(
        self,
        request: pai_auto_ml20220828_models.ListHpoExperimentsRequest,
    ) -> pai_auto_ml20220828_models.ListHpoExperimentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_hpo_experiments_with_options_async(request, headers, runtime)
