# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_contactcenterai20240603 import models as contact_center_ai20240603_models
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
        self._endpoint = self.get_endpoint('contactcenterai', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def run_completion_with_options(
        self,
        workspace_id: str,
        app_id: str,
        request: contact_center_ai20240603_models.RunCompletionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> contact_center_ai20240603_models.RunCompletionResponse:
        """
        @summary CCAI服务面API
        
        @param request: RunCompletionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCompletionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dialogue):
            body['Dialogue'] = request.dialogue
        if not UtilClient.is_unset(request.fields):
            body['Fields'] = request.fields
        if not UtilClient.is_unset(request.model_code):
            body['ModelCode'] = request.model_code
        if not UtilClient.is_unset(request.service_inspection):
            body['ServiceInspection'] = request.service_inspection
        if not UtilClient.is_unset(request.stream):
            body['Stream'] = request.stream
        if not UtilClient.is_unset(request.template_ids):
            body['TemplateIds'] = request.template_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunCompletion',
            version='2024-06-03',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/ccai/app/{OpenApiUtilClient.get_encode_param(app_id)}/completion',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            contact_center_ai20240603_models.RunCompletionResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_completion_with_options_async(
        self,
        workspace_id: str,
        app_id: str,
        request: contact_center_ai20240603_models.RunCompletionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> contact_center_ai20240603_models.RunCompletionResponse:
        """
        @summary CCAI服务面API
        
        @param request: RunCompletionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCompletionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dialogue):
            body['Dialogue'] = request.dialogue
        if not UtilClient.is_unset(request.fields):
            body['Fields'] = request.fields
        if not UtilClient.is_unset(request.model_code):
            body['ModelCode'] = request.model_code
        if not UtilClient.is_unset(request.service_inspection):
            body['ServiceInspection'] = request.service_inspection
        if not UtilClient.is_unset(request.stream):
            body['Stream'] = request.stream
        if not UtilClient.is_unset(request.template_ids):
            body['TemplateIds'] = request.template_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunCompletion',
            version='2024-06-03',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/ccai/app/{OpenApiUtilClient.get_encode_param(app_id)}/completion',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            contact_center_ai20240603_models.RunCompletionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_completion(
        self,
        workspace_id: str,
        app_id: str,
        request: contact_center_ai20240603_models.RunCompletionRequest,
    ) -> contact_center_ai20240603_models.RunCompletionResponse:
        """
        @summary CCAI服务面API
        
        @param request: RunCompletionRequest
        @return: RunCompletionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_completion_with_options(workspace_id, app_id, request, headers, runtime)

    async def run_completion_async(
        self,
        workspace_id: str,
        app_id: str,
        request: contact_center_ai20240603_models.RunCompletionRequest,
    ) -> contact_center_ai20240603_models.RunCompletionResponse:
        """
        @summary CCAI服务面API
        
        @param request: RunCompletionRequest
        @return: RunCompletionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_completion_with_options_async(workspace_id, app_id, request, headers, runtime)

    def run_completion_message_with_options(
        self,
        workspace_id: str,
        app_id: str,
        request: contact_center_ai20240603_models.RunCompletionMessageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> contact_center_ai20240603_models.RunCompletionMessageResponse:
        """
        @summary CCAI服务面API
        
        @param request: RunCompletionMessageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCompletionMessageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.messages):
            body['Messages'] = request.messages
        if not UtilClient.is_unset(request.model_code):
            body['ModelCode'] = request.model_code
        if not UtilClient.is_unset(request.stream):
            body['Stream'] = request.stream
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunCompletionMessage',
            version='2024-06-03',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/ccai/app/{OpenApiUtilClient.get_encode_param(app_id)}/completion_message',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            contact_center_ai20240603_models.RunCompletionMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_completion_message_with_options_async(
        self,
        workspace_id: str,
        app_id: str,
        request: contact_center_ai20240603_models.RunCompletionMessageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> contact_center_ai20240603_models.RunCompletionMessageResponse:
        """
        @summary CCAI服务面API
        
        @param request: RunCompletionMessageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCompletionMessageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.messages):
            body['Messages'] = request.messages
        if not UtilClient.is_unset(request.model_code):
            body['ModelCode'] = request.model_code
        if not UtilClient.is_unset(request.stream):
            body['Stream'] = request.stream
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunCompletionMessage',
            version='2024-06-03',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/ccai/app/{OpenApiUtilClient.get_encode_param(app_id)}/completion_message',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            contact_center_ai20240603_models.RunCompletionMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_completion_message(
        self,
        workspace_id: str,
        app_id: str,
        request: contact_center_ai20240603_models.RunCompletionMessageRequest,
    ) -> contact_center_ai20240603_models.RunCompletionMessageResponse:
        """
        @summary CCAI服务面API
        
        @param request: RunCompletionMessageRequest
        @return: RunCompletionMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_completion_message_with_options(workspace_id, app_id, request, headers, runtime)

    async def run_completion_message_async(
        self,
        workspace_id: str,
        app_id: str,
        request: contact_center_ai20240603_models.RunCompletionMessageRequest,
    ) -> contact_center_ai20240603_models.RunCompletionMessageResponse:
        """
        @summary CCAI服务面API
        
        @param request: RunCompletionMessageRequest
        @return: RunCompletionMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_completion_message_with_options_async(workspace_id, app_id, request, headers, runtime)
