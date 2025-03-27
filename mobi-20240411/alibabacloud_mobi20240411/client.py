# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_mobi20240411 import models as mobi_20240411_models
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
        self._endpoint = self.get_endpoint('mobi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_app_from_template_with_options(
        self,
        request: mobi_20240411_models.CreateAppFromTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mobi_20240411_models.CreateAppFromTemplateResponse:
        """
        @summary 通过模板创建应用
        
        @param request: CreateAppFromTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppFromTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.actual_parameters):
            query['ActualParameters'] = request.actual_parameters
        if not UtilClient.is_unset(request.connections_content):
            query['ConnectionsContent'] = request.connections_content
        if not UtilClient.is_unset(request.databases_content):
            query['DatabasesContent'] = request.databases_content
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.icon):
            query['Icon'] = request.icon
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.variables_content):
            query['VariablesContent'] = request.variables_content
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppFromTemplate',
            version='2024-04-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mobi_20240411_models.CreateAppFromTemplateResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mobi_20240411_models.CreateAppFromTemplateResponse(),
                self.execute(params, req, runtime)
            )

    async def create_app_from_template_with_options_async(
        self,
        request: mobi_20240411_models.CreateAppFromTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mobi_20240411_models.CreateAppFromTemplateResponse:
        """
        @summary 通过模板创建应用
        
        @param request: CreateAppFromTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppFromTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.actual_parameters):
            query['ActualParameters'] = request.actual_parameters
        if not UtilClient.is_unset(request.connections_content):
            query['ConnectionsContent'] = request.connections_content
        if not UtilClient.is_unset(request.databases_content):
            query['DatabasesContent'] = request.databases_content
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.icon):
            query['Icon'] = request.icon
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.variables_content):
            query['VariablesContent'] = request.variables_content
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppFromTemplate',
            version='2024-04-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mobi_20240411_models.CreateAppFromTemplateResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mobi_20240411_models.CreateAppFromTemplateResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_app_from_template(
        self,
        request: mobi_20240411_models.CreateAppFromTemplateRequest,
    ) -> mobi_20240411_models.CreateAppFromTemplateResponse:
        """
        @summary 通过模板创建应用
        
        @param request: CreateAppFromTemplateRequest
        @return: CreateAppFromTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_app_from_template_with_options(request, runtime)

    async def create_app_from_template_async(
        self,
        request: mobi_20240411_models.CreateAppFromTemplateRequest,
    ) -> mobi_20240411_models.CreateAppFromTemplateResponse:
        """
        @summary 通过模板创建应用
        
        @param request: CreateAppFromTemplateRequest
        @return: CreateAppFromTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_app_from_template_with_options_async(request, runtime)
