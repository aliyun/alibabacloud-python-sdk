# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_sysom20231230 import models as sys_om20231230_models
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
        self._endpoint = self.get_endpoint('sysom', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def auth_diagnosis_with_options(
        self,
        request: sys_om20231230_models.AuthDiagnosisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.AuthDiagnosisResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instances):
            body['instances'] = request.instances
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AuthDiagnosis',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/diagnosis/auth',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.AuthDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    async def auth_diagnosis_with_options_async(
        self,
        request: sys_om20231230_models.AuthDiagnosisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.AuthDiagnosisResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instances):
            body['instances'] = request.instances
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AuthDiagnosis',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/diagnosis/auth',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.AuthDiagnosisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def auth_diagnosis(
        self,
        request: sys_om20231230_models.AuthDiagnosisRequest,
    ) -> sys_om20231230_models.AuthDiagnosisResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.auth_diagnosis_with_options(request, headers, runtime)

    async def auth_diagnosis_async(
        self,
        request: sys_om20231230_models.AuthDiagnosisRequest,
    ) -> sys_om20231230_models.AuthDiagnosisResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.auth_diagnosis_with_options_async(request, headers, runtime)

    def get_diagnosis_result_with_options(
        self,
        request: sys_om20231230_models.GetDiagnosisResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetDiagnosisResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiagnosisResult',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/diagnosis/get_diagnosis_results',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetDiagnosisResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_diagnosis_result_with_options_async(
        self,
        request: sys_om20231230_models.GetDiagnosisResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.GetDiagnosisResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiagnosisResult',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/diagnosis/get_diagnosis_results',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.GetDiagnosisResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_diagnosis_result(
        self,
        request: sys_om20231230_models.GetDiagnosisResultRequest,
    ) -> sys_om20231230_models.GetDiagnosisResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_diagnosis_result_with_options(request, headers, runtime)

    async def get_diagnosis_result_async(
        self,
        request: sys_om20231230_models.GetDiagnosisResultRequest,
    ) -> sys_om20231230_models.GetDiagnosisResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_diagnosis_result_with_options_async(request, headers, runtime)

    def invoke_diagnosis_with_options(
        self,
        request: sys_om20231230_models.InvokeDiagnosisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.InvokeDiagnosisResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel):
            body['channel'] = request.channel
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        if not UtilClient.is_unset(request.service_name):
            body['service_name'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InvokeDiagnosis',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/diagnosis/invoke_diagnosis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.InvokeDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    async def invoke_diagnosis_with_options_async(
        self,
        request: sys_om20231230_models.InvokeDiagnosisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sys_om20231230_models.InvokeDiagnosisResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel):
            body['channel'] = request.channel
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        if not UtilClient.is_unset(request.service_name):
            body['service_name'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InvokeDiagnosis',
            version='2023-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/openapi/diagnosis/invoke_diagnosis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sys_om20231230_models.InvokeDiagnosisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invoke_diagnosis(
        self,
        request: sys_om20231230_models.InvokeDiagnosisRequest,
    ) -> sys_om20231230_models.InvokeDiagnosisResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.invoke_diagnosis_with_options(request, headers, runtime)

    async def invoke_diagnosis_async(
        self,
        request: sys_om20231230_models.InvokeDiagnosisRequest,
    ) -> sys_om20231230_models.InvokeDiagnosisResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.invoke_diagnosis_with_options_async(request, headers, runtime)
