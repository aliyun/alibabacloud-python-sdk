# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_edututor20250707 import models as edu_tutor_20250707_models
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
        self._endpoint = self.get_endpoint('edututor', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def answer_ssewith_options(
        self,
        request: edu_tutor_20250707_models.AnswerSSERequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edu_tutor_20250707_models.AnswerSSEResponse:
        """
        @summary AnswerSSE
        
        @param request: AnswerSSERequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AnswerSSEResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.messages):
            body['messages'] = request.messages
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AnswerSSE',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/service/answerSSE',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_tutor_20250707_models.AnswerSSEResponse(),
            self.call_api(params, req, runtime)
        )

    async def answer_ssewith_options_async(
        self,
        request: edu_tutor_20250707_models.AnswerSSERequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edu_tutor_20250707_models.AnswerSSEResponse:
        """
        @summary AnswerSSE
        
        @param request: AnswerSSERequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AnswerSSEResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.messages):
            body['messages'] = request.messages
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AnswerSSE',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/service/answerSSE',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_tutor_20250707_models.AnswerSSEResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def answer_sse(
        self,
        request: edu_tutor_20250707_models.AnswerSSERequest,
    ) -> edu_tutor_20250707_models.AnswerSSEResponse:
        """
        @summary AnswerSSE
        
        @param request: AnswerSSERequest
        @return: AnswerSSEResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.answer_ssewith_options(request, headers, runtime)

    async def answer_sse_async(
        self,
        request: edu_tutor_20250707_models.AnswerSSERequest,
    ) -> edu_tutor_20250707_models.AnswerSSEResponse:
        """
        @summary AnswerSSE
        
        @param request: AnswerSSERequest
        @return: AnswerSSEResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.answer_ssewith_options_async(request, headers, runtime)

    def cut_questions_with_options(
        self,
        request: edu_tutor_20250707_models.CutQuestionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edu_tutor_20250707_models.CutQuestionsResponse:
        """
        @summary CutQuestions
        
        @param request: CutQuestionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CutQuestionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.image):
            body['image'] = request.image
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CutQuestions',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/service/cutApi',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_tutor_20250707_models.CutQuestionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def cut_questions_with_options_async(
        self,
        request: edu_tutor_20250707_models.CutQuestionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edu_tutor_20250707_models.CutQuestionsResponse:
        """
        @summary CutQuestions
        
        @param request: CutQuestionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CutQuestionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.image):
            body['image'] = request.image
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CutQuestions',
            version='2025-07-07',
            protocol='HTTPS',
            pathname=f'/service/cutApi',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edu_tutor_20250707_models.CutQuestionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cut_questions(
        self,
        request: edu_tutor_20250707_models.CutQuestionsRequest,
    ) -> edu_tutor_20250707_models.CutQuestionsResponse:
        """
        @summary CutQuestions
        
        @param request: CutQuestionsRequest
        @return: CutQuestionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cut_questions_with_options(request, headers, runtime)

    async def cut_questions_async(
        self,
        request: edu_tutor_20250707_models.CutQuestionsRequest,
    ) -> edu_tutor_20250707_models.CutQuestionsResponse:
        """
        @summary CutQuestions
        
        @param request: CutQuestionsRequest
        @return: CutQuestionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cut_questions_with_options_async(request, headers, runtime)
