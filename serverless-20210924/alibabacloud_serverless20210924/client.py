# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_serverless20210924 import models as serverless_20210924_models
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
        self._endpoint = self.get_endpoint('serverless', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_environment(
        self,
        name: str,
    ) -> serverless_20210924_models.GetEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_environment_with_options(name, headers, runtime)

    async def get_environment_async(
        self,
        name: str,
    ) -> serverless_20210924_models.GetEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_environment_with_options_async(name, headers, runtime)

    def get_environment_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.GetEnvironmentResponse:
        name = OpenApiUtilClient.get_encode_param(name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetEnvironment',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/environments/{name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_environment_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.GetEnvironmentResponse:
        name = OpenApiUtilClient.get_encode_param(name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetEnvironment',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/environments/{name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service(
        self,
        name: str,
    ) -> serverless_20210924_models.GetServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_with_options(name, headers, runtime)

    async def get_service_async(
        self,
        name: str,
    ) -> serverless_20210924_models.GetServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_service_with_options_async(name, headers, runtime)

    def get_service_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.GetServiceResponse:
        name = OpenApiUtilClient.get_encode_param(name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetService',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/services/{name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.GetServiceResponse:
        name = OpenApiUtilClient.get_encode_param(name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetService',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/services/{name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_environments(self) -> serverless_20210924_models.ListEnvironmentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_environments_with_options(headers, runtime)

    async def list_environments_async(self) -> serverless_20210924_models.ListEnvironmentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_environments_with_options_async(headers, runtime)

    def list_environments_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.ListEnvironmentsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListEnvironments',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/environments/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListEnvironmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_environments_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.ListEnvironmentsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListEnvironments',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/environments/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListEnvironmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_services(self) -> serverless_20210924_models.ListServicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_services_with_options(headers, runtime)

    async def list_services_async(self) -> serverless_20210924_models.ListServicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_services_with_options_async(headers, runtime)

    def list_services_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.ListServicesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/services/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_services_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.ListServicesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/services/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_environment(
        self,
        name: str,
        request: serverless_20210924_models.PutEnvironmentRequest,
    ) -> serverless_20210924_models.PutEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_environment_with_options(name, request, headers, runtime)

    async def put_environment_async(
        self,
        name: str,
        request: serverless_20210924_models.PutEnvironmentRequest,
    ) -> serverless_20210924_models.PutEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_environment_with_options_async(name, request, headers, runtime)

    def put_environment_with_options(
        self,
        name: str,
        request: serverless_20210924_models.PutEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.PutEnvironmentResponse:
        UtilClient.validate_model(request)
        name = OpenApiUtilClient.get_encode_param(name)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='PutEnvironment',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/environments/{name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.PutEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_environment_with_options_async(
        self,
        name: str,
        request: serverless_20210924_models.PutEnvironmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.PutEnvironmentResponse:
        UtilClient.validate_model(request)
        name = OpenApiUtilClient.get_encode_param(name)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='PutEnvironment',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/environments/{name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.PutEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_service(
        self,
        name: str,
        request: serverless_20210924_models.PutServiceRequest,
    ) -> serverless_20210924_models.PutServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_service_with_options(name, request, headers, runtime)

    async def put_service_async(
        self,
        name: str,
        request: serverless_20210924_models.PutServiceRequest,
    ) -> serverless_20210924_models.PutServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_service_with_options_async(name, request, headers, runtime)

    def put_service_with_options(
        self,
        name: str,
        request: serverless_20210924_models.PutServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.PutServiceResponse:
        UtilClient.validate_model(request)
        name = OpenApiUtilClient.get_encode_param(name)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='PutService',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/services/{name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.PutServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_service_with_options_async(
        self,
        name: str,
        request: serverless_20210924_models.PutServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> serverless_20210924_models.PutServiceResponse:
        UtilClient.validate_model(request)
        name = OpenApiUtilClient.get_encode_param(name)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='PutService',
            version='2021-09-24',
            protocol='HTTPS',
            pathname=f'/apis/serverlessdeployment/v1/services/{name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.PutServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )
