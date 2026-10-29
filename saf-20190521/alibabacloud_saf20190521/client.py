# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_saf20190521 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-hangzhou': 'saf.cn-shanghai.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('saf', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def execute_request_with_options(
        self,
        request: main_models.ExecuteRequestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteRequestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.service):
            query['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteRequest',
            version = '2019-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_request_with_options_async(
        self,
        request: main_models.ExecuteRequestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteRequestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.service):
            query['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteRequest',
            version = '2019-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_request(
        self,
        request: main_models.ExecuteRequestRequest,
    ) -> main_models.ExecuteRequestResponse:
        runtime = RuntimeOptions()
        return self.execute_request_with_options(request, runtime)

    async def execute_request_async(
        self,
        request: main_models.ExecuteRequestRequest,
    ) -> main_models.ExecuteRequestResponse:
        runtime = RuntimeOptions()
        return await self.execute_request_with_options_async(request, runtime)

    def execute_request_mlwith_options(
        self,
        request: main_models.ExecuteRequestMLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteRequestMLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.service):
            query['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteRequestML',
            version = '2019-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteRequestMLResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_request_mlwith_options_async(
        self,
        request: main_models.ExecuteRequestMLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteRequestMLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.service):
            query['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteRequestML',
            version = '2019-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteRequestMLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_request_ml(
        self,
        request: main_models.ExecuteRequestMLRequest,
    ) -> main_models.ExecuteRequestMLResponse:
        runtime = RuntimeOptions()
        return self.execute_request_mlwith_options(request, runtime)

    async def execute_request_ml_async(
        self,
        request: main_models.ExecuteRequestMLRequest,
    ) -> main_models.ExecuteRequestMLResponse:
        runtime = RuntimeOptions()
        return await self.execute_request_mlwith_options_async(request, runtime)

    def execute_request_sgwith_options(
        self,
        request: main_models.ExecuteRequestSGRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteRequestSGResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.service):
            query['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteRequestSG',
            version = '2019-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteRequestSGResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_request_sgwith_options_async(
        self,
        request: main_models.ExecuteRequestSGRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteRequestSGResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.service):
            query['Service'] = request.service
        if not DaraCore.is_null(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteRequestSG',
            version = '2019-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteRequestSGResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_request_sg(
        self,
        request: main_models.ExecuteRequestSGRequest,
    ) -> main_models.ExecuteRequestSGResponse:
        runtime = RuntimeOptions()
        return self.execute_request_sgwith_options(request, runtime)

    async def execute_request_sg_async(
        self,
        request: main_models.ExecuteRequestSGRequest,
    ) -> main_models.ExecuteRequestSGResponse:
        runtime = RuntimeOptions()
        return await self.execute_request_sgwith_options_async(request, runtime)

    def request_decision_with_options(
        self,
        request: main_models.RequestDecisionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RequestDecisionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_code):
            query['EventCode'] = request.event_code
        if not DaraCore.is_null(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RequestDecision',
            version = '2019-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RequestDecisionResponse(),
            self.call_api(params, req, runtime)
        )

    async def request_decision_with_options_async(
        self,
        request: main_models.RequestDecisionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RequestDecisionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_code):
            query['EventCode'] = request.event_code
        if not DaraCore.is_null(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RequestDecision',
            version = '2019-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RequestDecisionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def request_decision(
        self,
        request: main_models.RequestDecisionRequest,
    ) -> main_models.RequestDecisionResponse:
        runtime = RuntimeOptions()
        return self.request_decision_with_options(request, runtime)

    async def request_decision_async(
        self,
        request: main_models.RequestDecisionRequest,
    ) -> main_models.RequestDecisionResponse:
        runtime = RuntimeOptions()
        return await self.request_decision_with_options_async(request, runtime)
