# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dashdeviceconsole20250408 import models as dash_device_console_20250408_models
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
        self._endpoint = self.get_endpoint('dashdeviceconsole', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_prompt_with_options(
        self,
        request: dash_device_console_20250408_models.GetPromptRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dash_device_console_20250408_models.GetPromptResponse:
        """
        @summary get prompt
        
        @param request: GetPromptRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPromptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['groupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrompt',
            version='2025-04-08',
            protocol='HTTPS',
            pathname=f'/prompt/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dash_device_console_20250408_models.GetPromptResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dash_device_console_20250408_models.GetPromptResponse(),
                self.execute(params, req, runtime)
            )

    async def get_prompt_with_options_async(
        self,
        request: dash_device_console_20250408_models.GetPromptRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dash_device_console_20250408_models.GetPromptResponse:
        """
        @summary get prompt
        
        @param request: GetPromptRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPromptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['groupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrompt',
            version='2025-04-08',
            protocol='HTTPS',
            pathname=f'/prompt/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dash_device_console_20250408_models.GetPromptResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dash_device_console_20250408_models.GetPromptResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_prompt(
        self,
        request: dash_device_console_20250408_models.GetPromptRequest,
    ) -> dash_device_console_20250408_models.GetPromptResponse:
        """
        @summary get prompt
        
        @param request: GetPromptRequest
        @return: GetPromptResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_prompt_with_options(request, headers, runtime)

    async def get_prompt_async(
        self,
        request: dash_device_console_20250408_models.GetPromptRequest,
    ) -> dash_device_console_20250408_models.GetPromptResponse:
        """
        @summary get prompt
        
        @param request: GetPromptRequest
        @return: GetPromptResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_prompt_with_options_async(request, headers, runtime)

    def push_prompt_with_options(
        self,
        request: dash_device_console_20250408_models.PushPromptRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dash_device_console_20250408_models.PushPromptResponse:
        """
        @summary push prompt
        
        @param request: PushPromptRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushPromptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['groupId'] = request.group_id
        body = {}
        if not UtilClient.is_unset(request.prompt_content):
            body['promptContent'] = request.prompt_content
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushPrompt',
            version='2025-04-08',
            protocol='HTTPS',
            pathname=f'/prompt/push',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dash_device_console_20250408_models.PushPromptResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dash_device_console_20250408_models.PushPromptResponse(),
                self.execute(params, req, runtime)
            )

    async def push_prompt_with_options_async(
        self,
        request: dash_device_console_20250408_models.PushPromptRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> dash_device_console_20250408_models.PushPromptResponse:
        """
        @summary push prompt
        
        @param request: PushPromptRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushPromptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['groupId'] = request.group_id
        body = {}
        if not UtilClient.is_unset(request.prompt_content):
            body['promptContent'] = request.prompt_content
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushPrompt',
            version='2025-04-08',
            protocol='HTTPS',
            pathname=f'/prompt/push',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                dash_device_console_20250408_models.PushPromptResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                dash_device_console_20250408_models.PushPromptResponse(),
                await self.execute_async(params, req, runtime)
            )

    def push_prompt(
        self,
        request: dash_device_console_20250408_models.PushPromptRequest,
    ) -> dash_device_console_20250408_models.PushPromptResponse:
        """
        @summary push prompt
        
        @param request: PushPromptRequest
        @return: PushPromptResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_prompt_with_options(request, headers, runtime)

    async def push_prompt_async(
        self,
        request: dash_device_console_20250408_models.PushPromptRequest,
    ) -> dash_device_console_20250408_models.PushPromptResponse:
        """
        @summary push prompt
        
        @param request: PushPromptRequest
        @return: PushPromptResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.push_prompt_with_options_async(request, headers, runtime)
